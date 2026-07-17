#!/usr/bin/env python3
"""Focused contract tests for audit_balance_breakpoints.py."""

from __future__ import annotations

import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import audit_balance_breakpoints as audit


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def raw_capture(name: str, health: int, date: str = "2026-07-17", *, future: bool = False) -> str:
    future_marker = "{{FutureUpdate}}\n" if future else ""
    return f"""# Direct Raw Capture: Fandom {name}

- Title: {name}
- URL: https://brawlstars.fandom.com/wiki/{name.replace(' ', '_')}
- Capture date: {date}
- Capture method: fixture

## Infobox Fields

- HealthLabel: Health
- Health: {health}

## Selected Wikitext Excerpts

{future_marker}fixture
"""


def wrapped_json(key: str, payload: dict) -> str:
    return "```json\n" + json.dumps({key: payload}, ensure_ascii=False, indent=2) + "\n```"


class BreakpointMathTest(unittest.TestCase):
    def test_reference_command_aliases(self) -> None:
        args = audit.parse_args(
            [
                "--manifest-source",
                "June.md",
                "--patch-id",
                "june",
                "--output",
                "audit.json",
                "--report",
                "audit.md",
            ]
        )
        self.assertEqual(args.patch_source, [Path("June.md")])
        self.assertEqual(args.patch_id, ["june"])
        self.assertEqual(args.json_output, Path("audit.json"))
        self.assertEqual(args.markdown_output, Path("audit.md"))

    def test_change_type_and_change_class_contract(self) -> None:
        self.assertTrue(
            audit.change_supported(
                {"type": "damage_packet", "change_class": "breakpoint_supported"}
            )
        )
        self.assertFalse(
            audit.change_supported(
                {"type": "damage_packet", "change_class": "source_conflict"}
            )
        )
        # A support disposition alone cannot identify which input is changing.
        self.assertFalse(audit.change_supported({"change_class": "breakpoint_supported"}))
        # Existing v1 manifests without change_class remain replayable.
        self.assertTrue(audit.change_supported({"type": "target_state"}))

    def test_power_11_scale_and_fixed_shield(self) -> None:
        self.assertEqual(audit.scale_between_powers(2500, 1, 11), 5000)
        # A P5 value already includes the 1.4x P1 multiplier.
        self.assertEqual(audit.scale_between_powers(1400, 5, 11), 2000)
        self.assertEqual(audit.scale_between_powers(5000, 11, 11), 5000)
        # The full Shield gear is added after level scaling, not doubled.
        self.assertEqual(
            audit.effective_health(audit.scale_between_powers(2500, 1, 11), flat_shield=audit.SHIELD_GEAR_P11),
            5900,
        )

    def test_distinct_damage_reductions_add_and_exact_kill_uses_ceil(self) -> None:
        self.assertEqual(
            audit.effective_health(10_000, damage_reductions=[Fraction(1, 5), Fraction(1, 5)]),
            Fraction(50_000, 3),
        )
        self.assertEqual(audit.hits_to_kill(6000, 2000), 3)
        self.assertEqual(audit.hits_to_kill(Fraction(6001), 2000), 4)
        self.assertEqual(audit.hits_to_kill(Fraction(50_000, 3), 5000), 4)


class DefenseProfileTest(unittest.TestCase):
    def world(self) -> audit.WorldState:
        return audit.WorldState(base_health={"Bibi": Fraction(10_000)}, state_health={}, packet_damage={}, defense_overrides={})

    def test_bibi_and_pearl_variants_and_additive_combo(self) -> None:
        bibi = {
            "schema": audit.PROFILE_SCHEMA,
            "target_states": [
                {
                    "id": "body",
                    "entity_class": "brawler_body",
                    "roster_target": True,
                    "health": {"amount": 5000, "at_power_level": 1, "scaling": "standard"},
                },
                {
                    "id": "fixture_alternate_form",
                    "entity_class": "brawler_alternate_form",
                    "roster_target": False,
                    "health": {"amount": 3000, "at_power_level": 1, "scaling": "standard"},
                }
            ],
            "damage_packets": [
                {
                    "id": "main.full_connect",
                    "packet_unit": "ammo",
                    "repeat_model": "identical",
                    "damage": {"amount": 1400, "at_power_level": 1, "scaling": "standard"},
                    "active_when": "full connect",
                }
            ],
            "defense_modifiers": [
                {
                    "id": "batting_stance",
                    "loadout_group": "star_power",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "20%"},
                },
                {
                    "id": "star_buffie",
                    "loadout_group": "star_buffie",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "1/5"},
                },
            ],
        }
        states, exclusions = audit.build_target_states("Bibi", Fraction(10_000), bibi, self.world())
        self.assertEqual(exclusions, [])
        self.assertEqual(states["body+batting_stance"]["effective_health"], 12_500)
        self.assertEqual(states["body+batting_stance+star_buffie"]["effective_health"], Fraction(50_000, 3))
        self.assertEqual(
            states["body+batting_stance+star_buffie+shield_gear_full"]["effective_health"],
            Fraction(54_500, 3),
        )
        packet_world = audit.WorldState(
            base_health={"Bibi": Fraction(10_000)},
            state_health={},
            packet_damage={("Bibi", "main.full_connect"): Fraction(2800)},
            defense_overrides={},
        )
        summary = audit.threshold_summary(
            "fixture",
            ("Bibi", "main.full_connect"),
            packet_world,
            packet_world,
            {"Bibi": states},
            {"Bibi": states},
            "identical",
        )
        # Alternate forms and defensive variants never duplicate the unique
        # Brawler denominator used by threshold summaries.
        self.assertEqual(summary["base_target_count"], 1)

        pearl_world = audit.WorldState(
            base_health={"Pearl": Fraction(8600)}, state_health={}, packet_damage={}, defense_overrides={}
        )
        pearl = {
            "schema": audit.PROFILE_SCHEMA,
            "target_states": [
                {
                    "id": "body",
                    "entity_class": "brawler_body",
                    "roster_target": True,
                    "health": {"amount": 4300, "at_power_level": 1, "scaling": "standard"},
                }
            ],
            "defense_modifiers": [
                {
                    "id": "heat_shield",
                    "loadout_group": "star_power",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "20%"},
                    "active_when": "Heat above 80%",
                }
            ],
        }
        states, exclusions = audit.build_target_states("Pearl", Fraction(8600), pearl, pearl_world)
        self.assertEqual(exclusions, [])
        self.assertEqual(states["body+heat_shield"]["effective_health"], 10_750)
        self.assertEqual(states["body+heat_shield"]["conditions"], ["Heat above 80%"])

    def test_intrinsic_target_reduction_and_replacement(self) -> None:
        profile = {
            "schema": audit.PROFILE_SCHEMA,
            "target_states": [
                {
                    "id": "body",
                    "entity_class": "brawler_body",
                    "roster_target": True,
                    "health": {"amount": 5000, "at_power_level": 1, "scaling": "standard"},
                },
                {
                    "id": "legs",
                    "entity_class": "brawler_split_part",
                    "roster_target": False,
                    "health": {"amount": 3000, "at_power_level": 1, "scaling": "standard"},
                    "intrinsic_damage_reduction": "29%",
                    "intrinsic_modifier_id": "legs_intrinsic",
                },
            ],
            "defense_modifiers": [
                {
                    "id": "recording_legs",
                    "loadout_group": "star_power",
                    "applies_to_states": ["legs"],
                    "effect": {"type": "damage_reduction", "ratio": "50%"},
                    "replaces_intrinsic_damage_reduction": True,
                }
            ],
        }
        states, exclusions = audit.build_target_states(
            "Bibi", Fraction(10_000), profile, self.world()
        )
        self.assertEqual(exclusions, [])
        self.assertEqual(states["legs"]["damage_reduction"], Fraction(29, 100))
        self.assertEqual(states["legs"]["effective_health"], Fraction(600_000, 71))
        self.assertEqual(states["legs+recording_legs"]["damage_reduction"], Fraction(1, 2))
        self.assertEqual(states["legs+recording_legs"]["effective_health"], 12_000)


class EndToEndAuditTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.roster = self.root / "raw/sources/roster/roster.md"
        self.fandom = self.root / "raw/sources/fandom/heroes"
        self.entities = self.root / "wiki/entities/brawlers"
        self.sources = self.root / "wiki/sources"

        rows = ["Bibi", "Crow", "Pearl", "Piper"]
        roster_lines = [
            "| canonical_name | fandom_url | plp_url |",
            "| --- | --- | --- |",
            *[
                f"| {name} | https://brawlstars.fandom.com/wiki/{name} | https://example.test/{name.lower()} |"
                for name in rows
            ],
        ]
        write(self.roster, "\n".join(roster_lines) + "\n")
        for name, hp in {"Bibi": 5000, "Crow": 2800, "Pearl": 4300, "Piper": 2800}.items():
            write(self.fandom / f"{audit.slugify(name)}-2026-07-17.md", raw_capture(name, hp))
        # A direct current raw not yet present in the older roster is included.
        write(self.fandom / "nori-2026-07-17.md", raw_capture("Nori", 3800))
        # A future-only raw must not leak into target coverage.
        write(self.fandom / "wendy-2026-07-17.md", raw_capture("Wendy", 2000, future=True))

        bibi_profile = {
            "schema": audit.PROFILE_SCHEMA,
            "target_states": [
                {
                    "id": "body",
                    "entity_class": "brawler_body",
                    "roster_target": True,
                    "health": {"amount": 5000, "at_power_level": 1, "scaling": "standard"},
                }
            ],
            "damage_packets": [
                {
                    "id": "main.full_connect",
                    "packet_unit": "ammo",
                    "repeat_model": "identical",
                    "damage": {"amount": 1400, "at_power_level": 1, "scaling": "standard"},
                    "active_when": "full connect",
                }
            ],
            "defense_modifiers": [
                {
                    "id": "batting_stance",
                    "loadout_group": "star_power",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "1/5"},
                },
                {
                    "id": "star_buffie",
                    "loadout_group": "star_buffie",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "1/5"},
                },
            ],
        }
        # Put the combat block second to prove extraction is semantic, not positional.
        write(
            self.entities / "Bibi.md",
            "# Bibi\n\n```json\n{\"unrelated\": true}\n```\n\n" + wrapped_json("combat_breakpoint_profile", bibi_profile) + "\n",
        )
        pearl_profile = {
            "schema": audit.PROFILE_SCHEMA,
            "target_states": [
                {
                    "id": "body",
                    "entity_class": "brawler_body",
                    "roster_target": True,
                    "health": {"amount": 4300, "at_power_level": 1, "scaling": "standard"},
                }
            ],
            "defense_modifiers": [
                {
                    "id": "heat_shield",
                    "loadout_group": "star_power",
                    "applies_to_states": ["body"],
                    "effect": {"type": "damage_reduction", "ratio": "20%"},
                }
            ],
        }
        write(
            self.entities / "Pearl.md",
            "# Pearl\n\n" + wrapped_json("combat_breakpoint_profile", pearl_profile) + "\n",
        )

        june = {
            "schema": audit.MANIFEST_SCHEMA,
            "patch_id": "2026-06",
            "effective_order": 1,
            "source_power_level": 1,
            "changes": [
                {
                    "type": "damage_packet",
                    "brawler": "Crow",
                    "packet_id": "main_one_dagger",
                    "old_damage": 320,
                    "new_damage": 420,
                },
                {"type": "target_state", "brawler": "Piper", "state_id": "base", "stat": "health", "old": 2500, "new": 2800},
                {"type": "target_state", "brawler": "Crow", "state_id": "body", "stat": "health", "old": 3000, "new": 2800},
                {
                    "type": "damage_packet",
                    "brawler": "Crow",
                    "packet_id": "synthetic_breakpoint_packet",
                    "old_damage": 1000,
                    "new_damage": 1300,
                },
                {
                    "type": "defense_modifier",
                    "brawler": "Bibi",
                    "modifier_id": "batting_stance",
                    "state_id": "body",
                    "stat": "damage_reduction",
                    "old": "10%",
                    "new": "20%",
                },
                {
                    "type": "unsupported",
                    "brawler": "Crow",
                    "reason": "reload change has no identical damage packet",
                },
            ],
        }
        july = {
            "schema": audit.MANIFEST_SCHEMA,
            "patch_id": "2026-07",
            "effective_order": 2,
            "source_power_level": 1,
            "changes": [
                {
                    "type": "damage_packet",
                    "brawler": "Crow",
                    "packet_id": "main_one_dagger",
                    "old_damage": 420,
                    "new_damage": 380,
                }
            ],
        }
        self.june_path = self.sources / "June.md"
        self.july_path = self.sources / "July.md"
        write(self.june_path, "# June\n\n" + wrapped_json("balance_patch_manifest", june) + "\n")
        write(self.july_path, "# July\n\n" + wrapped_json("balance_patch_manifest", july) + "\n")

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_ordered_chain_coverage_pair_deltas_and_build_pressure(self) -> None:
        result = audit.build_audit(
            roster_path=self.roster,
            fandom_dir=self.fandom,
            entity_dir=self.entities,
            patch_sources=[self.july_path, self.june_path],  # deliberately reversed input order
            output_power=11,
        )
        self.assertEqual(result["schema"], audit.OUTPUT_SCHEMA)
        self.assertEqual(result["coverage"]["roster_manifest_row_count"], 4)
        self.assertEqual(result["coverage"]["active_target_count"], 5)
        self.assertEqual(result["coverage"]["base_health_covered_count"], 5)
        self.assertEqual(result["coverage"]["roster_base_health_covered_count"], 4)
        self.assertEqual(result["coverage"]["combat_profile_count"], 2)
        self.assertEqual(result["coverage"]["reviewed_defense_modifier_profile_count"], 2)
        self.assertEqual(len(result["health_index"]), 4)
        self.assertNotIn("Wendy", [item["brawler"] for item in result["target_index"]])
        self.assertIn("Nori", [item["brawler"] for item in result["target_index"]])
        self.assertNotIn("Nori", [item["brawler"] for item in result["health_index"]])

        crow_chain = [
            item
            for item in result["threshold_summaries"]
            if item["attacker"] == "Crow" and item["packet_id"] == "main_one_dagger"
        ]
        self.assertEqual(
            [(item["patch_id"], item["packet_damage_before"], item["packet_damage_after"]) for item in crow_chain],
            [("2026-06", 640, 840), ("2026-07", 840, 760)],
        )
        self.assertFalse(
            any(item["reason"] == "old_value_does_not_match_previous_new_value" for item in result["exclusions"])
        )

        piper_pressure = [
            item
            for item in result["build_pressure_deltas"]
            if item["patch_id"] == "2026-06"
            and item["packet_id"] == "synthetic_breakpoint_packet"
            and item["target"] == "Piper"
            and item["target_state"] == "body+shield_gear_full"
        ]
        # Before the simultaneous patch Piper had 5000 HP and Crow did 2000:
        # exactly 3 packets. Afterwards 5600 / 2600 still takes 3, so the HP
        # buff offsets this synthetic damage increase. Use a separate current
        # raw-only target to check increased build pressure below.
        self.assertEqual(piper_pressure, [])

        bibi_states = next(item for item in result["target_index"] if item["brawler"] == "Bibi")["states"]
        self.assertEqual(bibi_states["body+batting_stance"]["damage_reduction"], "1/5")
        self.assertEqual(bibi_states["body+batting_stance+star_buffie"]["damage_reduction"], "2/5")
        self.assertEqual(bibi_states["body+batting_stance+star_buffie+shield_gear_full"]["flat_shield"], 900)
        self.assertTrue(
            any(
                item["patch_id"] == "2026-06"
                and item["attacker"] == "Bibi"
                and item["target"] == "Crow"
                and "target_health" in item["change_drivers"]
                for item in result["pair_deltas"]
            )
        )
        self.assertTrue(
            any(
                item["patch_id"] == "2026-06"
                and item["target"] == "Bibi"
                and "damage_reduction" in item["change_drivers"]
                for item in result["pair_deltas"]
            )
        )

        self.assertTrue(any(item.get("change_class") == "unsupported_mechanic" for item in result["exclusions"]))

    def test_current_health_and_defense_values_are_checked(self) -> None:
        # Make the latest direct HP and reviewed DR stale relative to the
        # manifest's final values. Replay may continue, but the mismatch must
        # be explicit rather than hidden by reverse patch reconstruction.
        write(self.fandom / "piper-2026-07-17.md", raw_capture("Piper", 2700))
        bibi_path = self.entities / "Bibi.md"
        text = bibi_path.read_text(encoding="utf-8")
        bibi_path.write_text(text.replace('"ratio": "1/5"', '"ratio": "3/20"', 1), encoding="utf-8")
        result = audit.build_audit(
            roster_path=self.roster,
            fandom_dir=self.fandom,
            entity_dir=self.entities,
            patch_sources=[self.june_path, self.july_path],
            output_power=11,
        )
        scopes = {item.get("scope") for item in result["exclusions"]}
        self.assertIn("target_state_current_value", scopes)
        self.assertIn("defense_modifier_current_value", scopes)
        serialized = json.dumps(result, ensure_ascii=False).casefold()
        for forbidden in ('"tier"', '"favored"', '"pick_priority"', '"pick priority"'):
            self.assertNotIn(forbidden, serialized)

    def test_build_pressure_when_only_full_shield_preserves_old_breakpoint(self) -> None:
        pressure_patch = {
            "schema": audit.MANIFEST_SCHEMA,
            "patch_id": "pressure",
            "effective_order": 1,
            "source_power_level": 1,
            "changes": [
                {
                    "type": "damage_packet",
                    "brawler": "Crow",
                    "packet_id": "pressure_packet",
                    "old_damage": 1000,
                    "new_damage": 1500,
                }
            ],
        }
        pressure_path = self.sources / "Pressure.md"
        write(pressure_path, "# Pressure\n\n" + wrapped_json("balance_patch_manifest", pressure_patch) + "\n")
        result = audit.build_audit(
            roster_path=self.roster,
            fandom_dir=self.fandom,
            entity_dir=self.entities,
            patch_sources=[pressure_path],
            output_power=11,
        )
        pressure = [
            item
            for item in result["build_pressure_deltas"]
            if item["target"] == "Piper" and item["target_state"] == "body+shield_gear_full"
        ]
        self.assertEqual(len(pressure), 1)
        self.assertEqual(pressure[0]["base_hits_to_kill_before"], 3)
        self.assertEqual(pressure[0]["base_hits_to_kill_after"], 2)
        self.assertEqual(pressure[0]["defense_state_hits_to_kill_after"], 3)
        self.assertEqual(
            pressure[0]["direction"],
            "defense_state_now_required_to_preserve_previous_base_breakpoint",
        )

    def test_markdown_has_scope_limit_and_no_decision_language(self) -> None:
        result = audit.build_audit(
            roster_path=self.roster,
            fandom_dir=self.fandom,
            entity_dir=self.entities,
            patch_sources=[self.june_path, self.july_path],
            output_power=11,
        )
        markdown = audit.render_markdown(result)
        self.assertIn("not a complete attack-packet catalog", markdown)
        self.assertIn("Suppressed higher-count pair transitions in Markdown", markdown)
        self.assertIn("Suppressed higher-count build-pressure transitions in Markdown", markdown)
        for forbidden in ("favored", "pick priority"):
            self.assertNotIn(forbidden, markdown.casefold())


if __name__ == "__main__":
    unittest.main()
