import json
import re
from pathlib import Path


CATALOG_SCHEMA = "brawlstar.strength_profile.catalog.v1"
KNOWN_MODE_ORDER = [
    "Gem Grab",
    "Brawl Ball",
    "Heist",
    "Hot Zone",
    "Knockout",
    "Bounty",
    "Showdown",
]


def _load_json(path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _quoted(value):
    return json.loads(value)


def _parse_alias_page(path):
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)\n```", text, re.S)
    if not match:
        raise ValueError(f"missing fenced yaml block in {path}")

    parsed = {}
    section = None
    current = None
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if not raw.startswith(" "):
            section = raw.rstrip(":")
            parsed[section] = {}
            current = None
            continue
        if raw.startswith("  ") and not raw.startswith("    "):
            item = raw.strip()
            if item.endswith(": []"):
                current = _quoted(item[:-4])
                parsed[section][current] = []
            elif item.endswith(":"):
                current = _quoted(item[:-1])
                parsed[section][current] = []
            else:
                raise ValueError(f"unsupported alias mapping line: {raw}")
            continue
        if raw.startswith("    - "):
            parsed[section][current].append(_quoted(raw.strip()[2:].strip()))
            continue
        raise ValueError(f"unsupported alias yaml line: {raw}")

    return parsed.get("aliases", {}), parsed.get("ambiguous", {})


def _image_key(name):
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def _build_image_index(repo):
    image_index = {}
    assets = repo / "wiki/syntheses/assets/tierlist-maker-research"
    tool_data = repo / "tools/strength-profile-editor/data"

    api = _load_json(assets / "metacoretroll-brawlers-api-export.json")
    if api:
        for brawler in api.get("brawlers", []):
            name = brawler.get("name", "")
            image_url = brawler.get("image_url", "")
            if name and image_url:
                image_index[_image_key(name)] = image_url

    tlm = _load_json(assets / "tierlistmaker-online-brawlstars-full-image-export.json")
    if tlm:
        for tier in tlm.get("value", {}).get("tiers", []):
            for item in tier.get("items", []):
                name = item.get("name", "")
                image_url = item.get("src", "")
                if name and image_url:
                    image_index[_image_key(name)] = image_url

    brawlapi = _load_json(tool_data / "brawlapi-brawler-images.json")
    if brawlapi:
        for name, image_url in brawlapi.get("images", {}).items():
            if name and image_url:
                image_index[_image_key(name)] = image_url

    return image_index


def _extract_map_mode(path):
    text = path.read_text(encoding="utf-8")
    bullet = re.search(r"^- 模式：`?([^`\n]+)`?", text, re.M)
    if bullet:
        return bullet.group(1).strip()
    yaml_mode = re.search(r"^\s*mode:\s*([^\n]+)", text, re.M)
    if yaml_mode:
        return yaml_mode.group(1).strip().strip('"').strip("'")
    return "Unclassified"


def _mode_sort_key(mode):
    if mode in KNOWN_MODE_ORDER:
        return (KNOWN_MODE_ORDER.index(mode), mode)
    return (len(KNOWN_MODE_ORDER), mode)


def build_catalog(repo):
    repo = Path(repo)
    aliases, ambiguous = _parse_alias_page(repo / "wiki/concepts/英雄名称归一化.md")
    image_index = _build_image_index(repo)

    brawlers = []
    alias_index = {}
    for path in sorted((repo / "wiki/entities/brawlers").glob("*.md")):
        name = path.stem
        brawler_aliases = aliases.get(name, [])
        image_url = image_index.get(_image_key(name), "")
        brawlers.append(
            {
                "name": name,
                "aliases": brawler_aliases,
                "image_url": image_url,
            }
        )
        alias_index[name] = name
        for alias in brawler_aliases:
            alias_index[alias] = name

    maps = []
    modes = set(KNOWN_MODE_ORDER)
    for path in sorted((repo / "wiki/entities/maps").glob("*.md")):
        mode = _extract_map_mode(path)
        modes.add(mode)
        maps.append({"name": path.stem, "mode": mode})

    maps.sort(key=lambda entry: (_mode_sort_key(entry["mode"]), entry["name"]))
    mode_list = sorted(modes, key=_mode_sort_key)

    return {
        "schema": CATALOG_SCHEMA,
        "source": {
            "brawlers": "wiki/entities/brawlers/*.md",
            "aliases": "wiki/concepts/英雄名称归一化.md",
            "maps": "wiki/entities/maps/*.md",
            "images": [
                "tools/strength-profile-editor/data/brawlapi-brawler-images.json",
                "wiki/syntheses/assets/tierlist-maker-research/*.json",
            ],
        },
        "tiers": ["S", "A", "B", "C", "D", "E"],
        "modes": mode_list,
        "maps": maps,
        "brawlers": brawlers,
        "alias_index": alias_index,
        "ambiguous": ambiguous,
    }


def write_catalog(repo, out_path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    catalog = build_catalog(repo)
    out_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return catalog


def main():
    repo = Path(__file__).resolve().parents[3]
    out_path = repo / "tools/strength-profile-editor/data/catalog.json"
    catalog = write_catalog(repo, out_path)
    with_images = sum(1 for brawler in catalog["brawlers"] if brawler["image_url"])
    print(
        f"wrote {out_path} "
        f"({len(catalog['brawlers'])} brawlers, {with_images} images, "
        f"{len(catalog['modes'])} modes, {len(catalog['maps'])} maps)"
    )


if __name__ == "__main__":
    main()
