import assert from "node:assert/strict";
import {
  createEmptyProfile,
  getSelectedScopeStrength,
  normalizeBrawlerName,
  setScopeTiers,
  validateProfileForExport,
} from "../profile-core.mjs";

const catalog = {
  tiers: ["S", "A", "B"],
  brawlers: [
    { name: "Brock", aliases: ["布洛克"], image_url: "https://example.test/brock.png" },
    { name: "Cordelius", aliases: ["64"], image_url: "https://example.test/cordelius.png" },
    { name: "Edgar", aliases: ["506"], image_url: "" },
    { name: "Mico", aliases: ["吗喽"], image_url: "" },
  ],
  alias_index: {
    Brock: "Brock",
    "布洛克": "Brock",
    Cordelius: "Cordelius",
    "64": "Cordelius",
    Edgar: "Edgar",
    "506": "Edgar",
    Mico: "Mico",
    "吗喽": "Mico",
  },
  ambiguous: {
    "猴子": ["Brock", "Mico"],
  },
};

const profile = createEmptyProfile(catalog, {
  patchId: "2026-test",
  profileId: "demo",
});

setScopeTiers(profile, { scope: "global" }, { S: ["Brock"], A: [], B: [] });
assert.equal(getSelectedScopeStrength(profile, { scope: "map", mode: "Brawl Ball", map: "Backyard Bowl" }).scope, "none");
assert.equal(getSelectedScopeStrength(profile, { scope: "global" }).scope, "global");

setScopeTiers(profile, { scope: "mode", mode: "Brawl Ball" }, { S: [], A: ["Edgar"], B: [] });
assert.equal(getSelectedScopeStrength(profile, { scope: "map", mode: "Brawl Ball", map: "Backyard Bowl" }).scope, "none");
assert.equal(getSelectedScopeStrength(profile, { scope: "mode", mode: "Brawl Ball" }).scope, "mode");

setScopeTiers(profile, { scope: "map", mode: "Brawl Ball", map: "Backyard Bowl" }, { S: ["Cordelius"], A: [], B: [] });
assert.equal(getSelectedScopeStrength(profile, { scope: "map", mode: "Brawl Ball", map: "Backyard Bowl" }).scope, "map");

assert.deepEqual(normalizeBrawlerName("506", catalog), { status: "ok", name: "Edgar", input: "506" });
assert.deepEqual(normalizeBrawlerName("猴子", catalog), {
  status: "ambiguous",
  input: "猴子",
  candidates: ["Brock", "Mico"],
});

const incomplete = createEmptyProfile(catalog);
setScopeTiers(incomplete, { scope: "global" }, { S: ["Brock"], A: [], B: [] });
assert.equal(validateProfileForExport(incomplete, catalog).ok, false);

const complete = createEmptyProfile(catalog);
setScopeTiers(complete, { scope: "global" }, { S: ["Brock"], A: ["Cordelius"], B: ["Edgar", "Mico"] });
assert.equal(validateProfileForExport(complete, catalog).ok, true);

const partialMode = createEmptyProfile(catalog);
setScopeTiers(partialMode, { scope: "global" }, { S: ["Brock"], A: ["Cordelius"], B: ["Edgar", "Mico"] });
setScopeTiers(partialMode, { scope: "mode", mode: "Brawl Ball" }, { S: ["Brock"], A: [], B: [] });
assert.equal(validateProfileForExport(partialMode, catalog).ok, false);
