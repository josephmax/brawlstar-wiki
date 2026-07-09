export const PROFILE_SCHEMA = "brawlstar.strength_profile.v1";

export function emptyTierMap(tierOrder = []) {
  return Object.fromEntries(tierOrder.map((tier) => [tier, []]));
}

export function createEmptyProfile(catalog, options = {}) {
  return {
    schema: PROFILE_SCHEMA,
    profile_id: options.profileId || "local-strength-profile",
    patch_id: options.patchId || "current",
    source: {
      kind: "local-strength-profile-editor",
    },
    tier_order: [...catalog.tiers],
    profiles: {
      global: {
        scope: "global",
        tiers: emptyTierMap(catalog.tiers),
      },
      modes: {},
      maps: {},
    },
  };
}

export function foldName(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[\s._'’\-&/]+/g, "");
}

function buildLookup(catalog) {
  const exact = new Map();
  const folded = new Map();
  const ambiguousExact = new Map();
  const ambiguousFolded = new Map();

  for (const [alias, name] of Object.entries(catalog.alias_index || {})) {
    exact.set(alias, name);
    folded.set(foldName(alias), name);
  }

  for (const brawler of catalog.brawlers || []) {
    exact.set(brawler.name, brawler.name);
    folded.set(foldName(brawler.name), brawler.name);
  }

  for (const [alias, candidates] of Object.entries(catalog.ambiguous || {})) {
    ambiguousExact.set(alias, candidates);
    ambiguousFolded.set(foldName(alias), candidates);
  }

  return { exact, folded, ambiguousExact, ambiguousFolded };
}

export function normalizeBrawlerName(input, catalog) {
  const value = String(input || "").trim();
  if (!value) {
    return { status: "missing", input };
  }

  const lookup = buildLookup(catalog);
  if (lookup.ambiguousExact.has(value)) {
    return { status: "ambiguous", input: value, candidates: lookup.ambiguousExact.get(value) };
  }
  const foldedValue = foldName(value);
  if (lookup.ambiguousFolded.has(foldedValue)) {
    return { status: "ambiguous", input: value, candidates: lookup.ambiguousFolded.get(foldedValue) };
  }
  if (lookup.exact.has(value)) {
    return { status: "ok", name: lookup.exact.get(value), input: value };
  }
  if (lookup.folded.has(foldedValue)) {
    return { status: "ok", name: lookup.folded.get(foldedValue), input: value };
  }
  return { status: "unknown", input: value };
}

function normalizeTierMap(tiers, tierOrder) {
  const seen = new Set();
  const normalized = emptyTierMap(tierOrder);
  for (const tier of tierOrder) {
    const entries = Array.isArray(tiers?.[tier]) ? tiers[tier] : [];
    for (const name of entries) {
      if (!seen.has(name)) {
        normalized[tier].push(name);
        seen.add(name);
      }
    }
  }
  return normalized;
}

export function mapScopeKey(mode, map) {
  return `${mode || ""}/${map || ""}`;
}

export function setScopeTiers(profile, target, tiers) {
  const tierMap = normalizeTierMap(tiers, profile.tier_order || []);

  if (target.scope === "global") {
    profile.profiles.global = {
      scope: "global",
      tiers: tierMap,
    };
    return profile.profiles.global;
  }

  if (target.scope === "mode") {
    if (!target.mode) {
      throw new Error("mode scope requires target.mode");
    }
    profile.profiles.modes[target.mode] = {
      scope: "mode",
      mode: target.mode,
      tiers: tierMap,
    };
    return profile.profiles.modes[target.mode];
  }

  if (target.scope === "map") {
    if (!target.mode || !target.map) {
      throw new Error("map scope requires target.mode and target.map");
    }
    const key = mapScopeKey(target.mode, target.map);
    profile.profiles.maps[key] = {
      scope: "map",
      mode: target.mode,
      map: target.map,
      tiers: tierMap,
    };
    return profile.profiles.maps[key];
  }

  throw new Error(`unsupported scope: ${target.scope}`);
}

function sanitizedProfile(input, catalog) {
  const profile = createEmptyProfile(catalog, {
    profileId: input?.profile_id || "imported-strength-profile",
    patchId: input?.patch_id || "current",
  });
  profile.source = input?.source || profile.source;

  if (input?.profiles?.global?.tiers) {
    setScopeTiers(profile, { scope: "global" }, input.profiles.global.tiers);
  }

  for (const [mode, record] of Object.entries(input?.profiles?.modes || {})) {
    if (record?.tiers) {
      setScopeTiers(profile, { scope: "mode", mode: record.mode || mode }, record.tiers);
    }
  }

  for (const [key, record] of Object.entries(input?.profiles?.maps || {})) {
    const mode = record?.mode || key.split("/")[0];
    const map = record?.map || key.split("/").slice(1).join("/");
    if (mode && map && record?.tiers) {
      setScopeTiers(profile, { scope: "map", mode, map }, record.tiers);
    }
  }

  return profile;
}

export function getScopeRecord(profile, target) {
  if (target.scope === "global") {
    return profile.profiles.global;
  }
  if (target.scope === "mode") {
    return profile.profiles.modes[target.mode];
  }
  if (target.scope === "map") {
    return profile.profiles.maps[mapScopeKey(target.mode, target.map)];
  }
  return null;
}

export function hasTierEntries(record) {
  if (!record?.tiers) {
    return false;
  }
  return Object.values(record.tiers).some((entries) => Array.isArray(entries) && entries.length > 0);
}

export function getSelectedScopeStrength(profile, target) {
  const record = getScopeRecord(profile, target);
  if (hasTierEntries(record)) {
    return { scope: target.scope, record };
  }
  return { scope: "none", record: null };
}

export function importStrengthProfile(input, catalog) {
  if (input?.schema === PROFILE_SCHEMA && input.profiles) {
    return sanitizedProfile(input, catalog);
  }

  const profile = createEmptyProfile(catalog, {
    profileId: input?.profile_id || "imported-strength-profile",
    patchId: input?.patch_id || "current",
  });

  if (input?.global_tiers) {
    setScopeTiers(profile, { scope: "global" }, input.global_tiers);
  }

  return profile;
}

function recordEntries(record) {
  return Object.values(record?.tiers || {}).flat();
}

function validateRecord(record, catalog, label, options = {}) {
  const errors = [];
  const tierOrder = new Set(catalog.tiers);
  const validNames = new Set((catalog.brawlers || []).map((brawler) => brawler.name));
  const seen = new Set();
  const duplicates = new Set();
  const unknownNames = new Set();

  for (const tier of Object.keys(record?.tiers || {})) {
    if (!tierOrder.has(tier)) {
      errors.push(`${label}: 不允许的档位 ${tier}`);
    }
  }

  for (const name of recordEntries(record)) {
    if (!validNames.has(name)) {
      unknownNames.add(name);
    }
    if (seen.has(name)) {
      duplicates.add(name);
    }
    seen.add(name);
  }

  if (unknownNames.size) {
    errors.push(`${label}: 包含未知英雄 ${[...unknownNames].join(", ")}`);
  }
  if (duplicates.size) {
    errors.push(`${label}: 重复英雄 ${[...duplicates].join(", ")}`);
  }

  const missing = [...validNames].filter((name) => !seen.has(name));
  if (options.requireComplete && missing.length) {
    errors.push(`${label}: 还缺 ${missing.length} 个英雄未排完`);
  }

  return errors;
}

export function validateProfileForExport(profile, catalog) {
  const errors = [];

  errors.push(
    ...validateRecord(profile?.profiles?.global, catalog, "通用强度", {
      requireComplete: true,
    }),
  );

  for (const [mode, record] of Object.entries(profile?.profiles?.modes || {})) {
    if (hasTierEntries(record)) {
      errors.push(
        ...validateRecord(record, catalog, `${record.mode || mode} 模式强度`, {
          requireComplete: true,
        }),
      );
    }
  }

  for (const [key, record] of Object.entries(profile?.profiles?.maps || {})) {
    if (hasTierEntries(record)) {
      errors.push(
        ...validateRecord(record, catalog, `${record.mode || key} / ${record.map || ""} 地图强度`, {
          requireComplete: true,
        }),
      );
    }
  }

  return {
    ok: errors.length === 0,
    errors,
  };
}

export function tierListMakerToTierMap(input, catalog) {
  const sourceTiers = input?.value?.tiers || input?.tiers || [];
  const result = emptyTierMap(catalog.tiers);
  const warnings = [];

  for (const tier of sourceTiers) {
    const label = tier.label || tier.id;
    if (!label || !result[label]) {
      continue;
    }
    for (const item of tier.items || []) {
      const normalized = normalizeBrawlerName(item.name || item.id, catalog);
      if (normalized.status === "ok") {
        result[label].push(normalized.name);
      } else {
        warnings.push(normalized);
      }
    }
  }

  return { tiers: result, warnings };
}
