import {
  createEmptyProfile,
  emptyTierMap,
  getSelectedScopeStrength,
  getScopeRecord,
  hasTierEntries,
  importStrengthProfile,
  normalizeBrawlerName,
  setScopeTiers,
  tierListMakerToTierMap,
  validateProfileForExport,
} from "./profile-core.mjs";

const STORAGE_KEY = "brawlstar.strength-profile-editor.v1";

const dom = {
  contextLabel: document.querySelector("#contextLabel"),
  coverageLabel: document.querySelector("#coverageLabel"),
  scopeTabs: [...document.querySelectorAll(".scope-tab")],
  modeSelect: document.querySelector("#modeSelect"),
  mapSelect: document.querySelector("#mapSelect"),
  modeField: document.querySelector("#modeSelect").closest(".field"),
  mapField: document.querySelector("#mapSelect").closest(".field"),
  patchInput: document.querySelector("#patchInput"),
  clearScopeButton: document.querySelector("#clearScopeButton"),
  tierBoard: document.querySelector("#tierBoard"),
  poolDropzone: document.querySelector("#poolDropzone"),
  searchInput: document.querySelector("#searchInput"),
  searchStatus: document.querySelector("#searchStatus"),
  effectiveSource: document.querySelector("#effectiveSource"),
  exportStatus: document.querySelector("#exportStatus"),
  jsonInput: document.querySelector("#jsonInput"),
  jsonPreview: document.querySelector("#jsonPreview"),
  importFileButton: document.querySelector("#importFileButton"),
  importFileInput: document.querySelector("#importFileInput"),
  importTextButton: document.querySelector("#importTextButton"),
  copyButton: document.querySelector("#copyButton"),
  exportButton: document.querySelector("#exportButton"),
};

let catalog = null;
let profile = null;
let currentScope = "global";
let draggedName = "";
let activeTier = "";

const brawlerByName = new Map();

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function currentTarget() {
  const mode = dom.modeSelect.value;
  const map = dom.mapSelect.value;
  if (currentScope === "global") {
    return { scope: "global" };
  }
  if (currentScope === "mode") {
    return { scope: "mode", mode };
  }
  return { scope: "map", mode, map };
}

function canEditCurrentScope() {
  const target = currentTarget();
  return target.scope !== "map" || Boolean(target.mode && target.map);
}

function getCurrentTierMap() {
  const record = getScopeRecord(profile, currentTarget());
  return clone(record?.tiers || emptyTierMap(catalog.tiers));
}

function persist() {
  profile.patch_id = dom.patchInput.value.trim() || "current";
  localStorage.setItem(STORAGE_KEY, JSON.stringify(profile));
}

function setExportStatus(message, kind = "") {
  dom.exportStatus.textContent = message;
  dom.exportStatus.classList.toggle("ok", kind === "ok");
  dom.exportStatus.classList.toggle("error", kind === "error");
}

function loadPersistedProfile() {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) {
    return createEmptyProfile(catalog);
  }
  try {
    return importStrengthProfile(JSON.parse(saved), catalog);
  } catch {
    return createEmptyProfile(catalog);
  }
}

function serializeProfile() {
  const payload = clone(profile);
  payload.patch_id = dom.patchInput.value.trim() || "current";
  payload.exported_at = new Date().toISOString();
  return payload;
}

function scopeLabel(target = currentTarget()) {
  if (target.scope === "global") {
    return "通用强度";
  }
  if (target.scope === "mode") {
    return `${target.mode} 模式强度`;
  }
  return `${target.mode} / ${target.map || "未选择地图"} 地图强度`;
}

function populateSelectors() {
  dom.modeSelect.replaceChildren(...catalog.modes.map((mode) => new Option(mode, mode)));
  if (!dom.modeSelect.value && catalog.modes.length) {
    dom.modeSelect.value = catalog.modes[0];
  }
  populateMapSelect();
}

function populateMapSelect() {
  const selectedMode = dom.modeSelect.value;
  const maps = catalog.maps.filter((map) => map.mode === selectedMode);
  if (!maps.length) {
    dom.mapSelect.replaceChildren(new Option("无地图实体", ""));
    return;
  }
  dom.mapSelect.replaceChildren(...maps.map((map) => new Option(map.name, map.name)));
}

function setScope(scope) {
  currentScope = scope;
  activeTier = "";
  dom.scopeTabs.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.scope === scope);
  });
  dom.modeField.classList.toggle("is-hidden", scope === "global");
  dom.mapField.classList.toggle("is-hidden", scope !== "map");
  render();
}

function ensureCurrentRecord() {
  if (!canEditCurrentScope()) {
    return;
  }
  const target = currentTarget();
  if (!getScopeRecord(profile, target)) {
    setScopeTiers(profile, target, emptyTierMap(catalog.tiers));
  }
}

function assignedNames(tierMap) {
  return new Set(Object.values(tierMap).flat());
}

function visibleBrawlers(tierMap) {
  const assigned = assignedNames(tierMap);
  const query = dom.searchInput.value.trim();
  const normalized = query ? normalizeBrawlerName(query, catalog) : null;

  dom.searchStatus.classList.remove("warn");
  if (!query) {
    dom.searchStatus.textContent = activeTier
      ? `批量入列：${activeTier}；${catalog.brawlers.length - assigned.size} 个未分配`
      : `${catalog.brawlers.length - assigned.size} 个未分配`;
    return catalog.brawlers.filter((brawler) => !assigned.has(brawler.name));
  }

  if (normalized?.status === "ambiguous") {
    dom.searchStatus.classList.add("warn");
    dom.searchStatus.textContent = `${normalized.input}: ${normalized.candidates.join(" / ")}`;
    return catalog.brawlers.filter((brawler) => normalized.candidates.includes(brawler.name));
  }

  if (normalized?.status === "ok") {
    dom.searchStatus.textContent = `${normalized.input} → ${normalized.name}`;
    return catalog.brawlers.filter((brawler) => brawler.name === normalized.name);
  }

  const foldedQuery = query.toLowerCase();
  const matches = catalog.brawlers.filter((brawler) => {
    const fields = [brawler.name, ...(brawler.aliases || [])].join(" ").toLowerCase();
    return fields.includes(foldedQuery);
  });
  dom.searchStatus.textContent = matches.length ? `${matches.length} 个匹配` : "无匹配";
  return matches.filter((brawler) => !assigned.has(brawler.name));
}

function initials(name) {
  return name
    .split(/\s+/)
    .map((part) => part[0])
    .join("")
    .slice(0, 3)
    .toUpperCase();
}

function brawlerCard(name) {
  const brawler = brawlerByName.get(name) || { name, aliases: [], image_url: "" };
  const card = document.createElement("div");
  card.className = "brawler-card";
  card.draggable = true;
  card.dataset.name = name;

  if (brawler.image_url) {
    const image = document.createElement("img");
    image.src = brawler.image_url;
    image.alt = name;
    image.loading = "lazy";
    image.referrerPolicy = "no-referrer";
    image.addEventListener("error", () => {
      image.replaceWith(fallbackAvatar(name));
    });
    card.append(image);
  } else {
    card.append(fallbackAvatar(name));
  }

  const label = document.createElement("div");
  label.className = "brawler-name";
  label.textContent = name;
  card.append(label);
  return card;
}

function fallbackAvatar(name) {
  const avatar = document.createElement("div");
  avatar.className = "avatar-fallback";
  avatar.textContent = initials(name);
  return avatar;
}

function renderPool(tierMap) {
  const items = visibleBrawlers(tierMap);
  dom.poolDropzone.replaceChildren(
    ...items.map((brawler) => {
      const card = brawlerCard(brawler.name);
      card.addEventListener("click", () => {
        if (activeTier) {
          moveBrawler(brawler.name, activeTier);
        }
      });
      return card;
    }),
  );
  if (!items.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "无未分配项";
    dom.poolDropzone.append(empty);
  }
}

function renderBoard(tierMap) {
  dom.tierBoard.replaceChildren();
  dom.tierBoard.classList.toggle("has-active", Boolean(activeTier));
  if (!canEditCurrentScope()) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "当前模式没有地图实体";
    dom.tierBoard.append(empty);
    return;
  }
  for (const tier of catalog.tiers) {
    const row = document.createElement("div");
    row.className = "tier-row";
    row.classList.toggle("is-active", activeTier === tier);
    row.classList.toggle("is-dimmed", Boolean(activeTier) && activeTier !== tier);

    const label = document.createElement("div");
    label.className = `tier-label tier-${tier.toLowerCase()}`;
    label.textContent = tier;
    label.title = activeTier === tier ? "退出批量输入" : `进入 ${tier} 档批量输入`;
    label.tabIndex = 0;
    label.addEventListener("click", () => {
      activeTier = activeTier === tier ? "" : tier;
      render();
    });
    label.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        activeTier = activeTier === tier ? "" : tier;
        render();
      }
    });

    const zone = document.createElement("div");
    zone.className = "drop-zone tier-items";
    zone.dataset.tier = tier;
    const names = tierMap[tier] || [];
    zone.replaceChildren(...names.map((name) => brawlerCard(name)));
    if (!names.length) {
      const empty = document.createElement("div");
      empty.className = "empty-state";
      empty.textContent = "Drop here";
      zone.append(empty);
    }

    row.append(label, zone);
    dom.tierBoard.append(row);
  }
}

function renderEffectiveSource() {
  const target = currentTarget();
  const selected = getSelectedScopeStrength(profile, target);

  const selectedText =
    selected.scope === "none"
      ? `当前层为空：${scopeLabel(target)}`
      : `当前层已填写：${scopeLabel(selected.record)}`;

  dom.effectiveSource.textContent = selectedText;
}

function renderPreview() {
  dom.jsonPreview.textContent = JSON.stringify(serializeProfile(), null, 2);
}

function render() {
  ensureCurrentRecord();
  dom.contextLabel.textContent = scopeLabel();
  dom.coverageLabel.textContent = "作用域独立：地图 / 模式 / 通用";
  const tierMap = getCurrentTierMap();
  renderPool(tierMap);
  renderBoard(tierMap);
  renderEffectiveSource();
  renderPreview();
}

function removeFromTierMap(tierMap, name) {
  for (const tier of Object.keys(tierMap)) {
    tierMap[tier] = tierMap[tier].filter((entry) => entry !== name);
  }
}

function moveBrawler(name, tier, beforeName = "") {
  if (!canEditCurrentScope()) {
    return;
  }
  const tierMap = getCurrentTierMap();
  removeFromTierMap(tierMap, name);
  if (tier && tierMap[tier]) {
    const beforeIndex = beforeName ? tierMap[tier].indexOf(beforeName) : -1;
    if (beforeIndex >= 0) {
      tierMap[tier].splice(beforeIndex, 0, name);
    } else {
      tierMap[tier].push(name);
    }
  }
  setScopeTiers(profile, currentTarget(), tierMap);
  persist();
  render();
}

function handleDragStart(event) {
  const card = event.target.closest(".brawler-card");
  if (!card) {
    return;
  }
  draggedName = card.dataset.name;
  event.dataTransfer.effectAllowed = "move";
  event.dataTransfer.setData("text/plain", draggedName);
}

function handleDragOver(event) {
  const zone = event.target.closest(".drop-zone");
  if (!zone) {
    return;
  }
  event.preventDefault();
  zone.classList.add("is-over");
}

function handleDragLeave(event) {
  const zone = event.target.closest(".drop-zone");
  if (zone) {
    zone.classList.remove("is-over");
  }
}

function handleDrop(event) {
  const zone = event.target.closest(".drop-zone");
  if (!zone) {
    return;
  }
  event.preventDefault();
  zone.classList.remove("is-over");
  const name = event.dataTransfer.getData("text/plain") || draggedName;
  if (!name) {
    return;
  }
  const targetCard = event.target.closest(".brawler-card");
  const beforeName = targetCard?.dataset?.name && targetCard.dataset.name !== name ? targetCard.dataset.name : "";
  moveBrawler(name, zone.dataset.tier || "", beforeName);
}

function handleImportPayload(payload) {
  if (payload?.schema === "tierlistmaker.online.localStorage.tlm_v3" || payload?.value?.tiers || payload?.tiers) {
    if (!canEditCurrentScope()) {
      dom.searchStatus.classList.add("warn");
      dom.searchStatus.textContent = "当前地图层没有可写入地图";
      return;
    }
    const converted = tierListMakerToTierMap(payload, catalog);
    setScopeTiers(profile, currentTarget(), converted.tiers);
    persist();
    render();
    return;
  }

  profile = importStrengthProfile(payload, catalog);
  dom.patchInput.value = profile.patch_id || "current";
  persist();
  render();
}

async function importFile(file) {
  const text = await file.text();
  handleImportPayload(JSON.parse(text));
}

function downloadJson() {
  const validation = validateProfileForExport(serializeProfile(), catalog);
  if (!validation.ok) {
    setExportStatus(`导出失败：\n${validation.errors.slice(0, 8).join("\n")}`, "error");
    return;
  }

  const payload = JSON.stringify(serializeProfile(), null, 2);
  const blob = new Blob([payload + "\n"], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `strength-profile-${Date.now()}.json`;
  link.click();
  URL.revokeObjectURL(url);

  navigator.clipboard
    .writeText(payload)
    .then(() => {
      const message = "已通过完整性校验，并复制到剪贴板。请粘贴到 agent 客户端。";
      setExportStatus(message, "ok");
      window.alert(message);
    })
    .catch(() => {
      const message = "已通过完整性校验并下载 JSON；剪贴板写入失败，请从右侧 JSON 预览手动复制后粘贴到 agent 客户端。";
      setExportStatus(message, "ok");
      window.alert(message);
    });
}

function wireEvents() {
  dom.scopeTabs.forEach((button) => {
    button.addEventListener("click", () => setScope(button.dataset.scope));
  });

  dom.modeSelect.addEventListener("change", () => {
    populateMapSelect();
    render();
  });
  dom.mapSelect.addEventListener("change", render);
  dom.patchInput.addEventListener("input", () => {
    persist();
    renderPreview();
  });
  dom.searchInput.addEventListener("input", render);

  dom.clearScopeButton.addEventListener("click", () => {
    if (!canEditCurrentScope()) {
      return;
    }
    setScopeTiers(profile, currentTarget(), emptyTierMap(catalog.tiers));
    persist();
    render();
  });

  document.addEventListener("dragstart", handleDragStart);
  document.addEventListener("dragover", handleDragOver);
  document.addEventListener("dragleave", handleDragLeave);
  document.addEventListener("drop", handleDrop);

  dom.importFileButton.addEventListener("click", () => dom.importFileInput.click());
  dom.importFileInput.addEventListener("change", async () => {
    const file = dom.importFileInput.files?.[0];
    if (file) {
      await importFile(file);
    }
    dom.importFileInput.value = "";
  });
  dom.importTextButton.addEventListener("click", () => {
    handleImportPayload(JSON.parse(dom.jsonInput.value));
    dom.jsonInput.value = "";
  });
  dom.copyButton.addEventListener("click", async () => {
    await navigator.clipboard.writeText(JSON.stringify(serializeProfile(), null, 2));
    setExportStatus("已复制当前草稿 JSON。正式导出仍需要通过完整性校验。", "ok");
  });
  dom.exportButton.addEventListener("click", downloadJson);
}

async function init() {
  catalog = await fetch("data/catalog.json").then((response) => {
    if (!response.ok) {
      throw new Error(`failed to load catalog: ${response.status}`);
    }
    return response.json();
  });

  for (const brawler of catalog.brawlers) {
    brawlerByName.set(brawler.name, brawler);
  }

  profile = loadPersistedProfile();
  dom.patchInput.value = profile.patch_id || "current";
  populateSelectors();
  wireEvents();
  setScope("global");
}

init().catch((error) => {
  document.body.innerHTML = `<pre class="fatal-error">${error.stack || error.message}</pre>`;
});
