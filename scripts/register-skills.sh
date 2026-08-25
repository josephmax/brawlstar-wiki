#!/usr/bin/env bash
# =============================================================================
# register-skills.sh — 项目内 skill 环境归一化注册脚本
#
# 把本仓库 skills/ 下的 bundle skill（<name>/SKILL.md）注册到当前项目目录，
# 供主流 agent 在项目范围内发现，不做任何全局/用户级安装。
#
# 支持的 agent 及项目内注册位置：
#   dsh          <repo>/.dsh/skills/<name>/            (rank 100, 每会话自动发现)
#   claude-code  <repo>/.claude/skills/<name>/          (项目级 skills, Claude Code 0.1.x+)
#   codex        <repo>/AGENTS.md 的 @skills/<name> 引用 (声明式项目规则)
#   pi           <repo>/.pi/skills/<name>/              (pi-ai 项目级 skills)
#
# 设计原则：
#   - 只写项目内路径，绝不触碰 ~/.dsh ~/.claude ~/.codex ~/.pi 等全局目录
#   - 幂等：已注册且内容一致时跳过；重跑只补新增/更新变更
#   - bundle 复制：整目录（SKILL.md + references/ scripts/ agents/），保持相对引用可用
#   - 软链优先（节省磁盘、跟随仓库更新），不可软链时降级为复制
#
# 用法：
#   scripts/register-skills.sh                      # 自动检测所有已安装 agent 并注册
#   scripts/register-skills.sh --agent dsh          # 只注册到 DSH
#   scripts/register-skills.sh --agent claude-code,codex
#   scripts/register-skills.sh --dry-run            # 只打印将做什么，不写盘
#   scripts/register-skills.sh --link|--copy        # 强制软链或强制复制
# =============================================================================
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="${REPO_ROOT}/skills"
AGENTS=("dsh" "claude-code" "codex" "pi")

MODE="auto"          # link | copy | auto
DRY_RUN=0
TARGET_AGENTS=()

log()  { printf '\033[36m[register]\033[0m %s\n' "$*"; }
warn() { printf '\033[33m[register!]\033[0m %s\n' "$*" >&2; }
err()  { printf '\033[31m[register!]\033[0m %s\n' "$*" >&2; }
die()  { err "$*"; exit 1; }

usage() {
  sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  echo
  echo "选项:"
  echo "  --agent <list>  逗号分隔: dsh,claude-code,codex,pi（默认: 自动检测）"
  echo "  --link          强制软链（默认 auto：可链则链）"
  echo "  --copy          强制复制"
  echo "  --dry-run       只打印计划，不写盘"
  echo "  -h, --help      显示帮助"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)   IFS=',' read -ra TARGET_AGENTS <<< "$2"; shift 2 ;;
    --link)    MODE="link"; shift ;;
    --copy)    MODE="copy"; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "未知参数: $1（用 --help 查看用法）" ;;
  esac
done

[[ -d "$SKILLS_SRC" ]] || die "未找到 skills 目录: $SKILLS_SRC"

# ---------- 0. DSH 项目根标记 ----------
# dsh-skill-filesystem 用 findProjectRoot(cwd) 找最近含 .git 的祖先作为项目根，
# 再扫描 <项目根>/.dsh/skills。本仓库位于无 .git 的 vault 内（git 根在上级），
# 若不标记，DSH 会把上级目录当项目根、永远扫不到本目录的 .dsh/skills。
# 解法：在仓库根放一个 gitlink 文件 .git（内容 "gitdir: <相对上级路径>"），
# findProjectRoot 从 cwd 向上第一层即命中；git 本身支持该文件形式（同 submodule）。
ensure_dsh_project_root_marker() {
  if [[ -e "$REPO_ROOT/.git" ]]; then
    return 0   # 已有 .git（目录或 gitlink），项目根判定正确
  fi
  # 找上级最近含 .git 的祖先，生成相对 gitdir 路径
  local parent="$REPO_ROOT"
  local rel=""
  while :; do
    if [[ -e "$parent/.git" ]]; then
      break
    fi
    local next_parent; next_parent="$(dirname "$parent")"
    if [[ "$next_parent" == "$parent" ]]; then
      warn "未找到上级 .git，无法生成 DSH 项目根标记（跳过，.dsh/skills 可能不会被 DSH 发现）"
      return 1
    fi
    parent="$next_parent"
    rel="${rel}../"
  done
  local gitdir="${rel}.git"
  if [[ $DRY_RUN -eq 1 ]]; then
    log "[dsh] 将创建项目根标记: $REPO_ROOT/.git -> gitdir: $gitdir"
    return 0
  fi
  printf 'gitdir: %s\n' "$gitdir" > "$REPO_ROOT/.git"
  log "[dsh] 已创建项目根标记: $REPO_ROOT/.git -> gitdir: $gitdir（DSH 会据此把项目根判定在本目录）"
}

ensure_dsh_project_root_marker || true

# ---------- 1. 收集可注册的 bundle skill ----------
declare -a BUNDLES=()
for dir in "$SKILLS_SRC"/*/; do
  [[ -f "${dir}SKILL.md" ]] || continue
  name="$(basename "$dir")"
  # DSH/Claude/pi 要求 kebab-case 名称；校验 frontmatter 的 name/description
  if ! [[ "$name" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
    warn "跳过 '$name': 目录名不是 kebab-case，无法被 agent 目录发现"
    continue
  fi
  fm_name="$(sed -n 's/^name:[[:space:]]*//p' "${dir}SKILL.md" | head -1 | tr -d '[:space:]')"
  fm_desc="$(sed -n 's/^description:[[:space:]]*//p' "${dir}SKILL.md" | head -1 | tr -d '[:space:]')"
  if [[ -z "$fm_name" || -z "$fm_desc" ]]; then
    warn "跳过 '$name': SKILL.md frontmatter 缺少 name 或 description"
    continue
  fi
  if [[ "$fm_name" != "$name" ]]; then
    warn "跳过 '$name': frontmatter name='$fm_name' 与目录名不一致"
    continue
  fi
  BUNDLES+=("$name")
done

[[ ${#BUNDLES[@]} -gt 0 ]] || die "没有可注册的 skill bundle"
log "发现 ${#BUNDLES[@]} 个 skill: ${BUNDLES[*]}"

# ---------- 2. 检测目标 agent 是否可用 ----------
detect_agents() {
  local found=()
  command -v claude >/dev/null 2>&1 && found+=("claude-code")
  command -v codex  >/dev/null 2>&1 && found+=("codex")
  command -v pi     >/dev/null 2>&1 && found+=("pi")
  # DSH: 检查当前会话环境变量或用户根
  [[ -n "${DSH_HOME:-}" || -d "$HOME/.dsh" ]] && found+=("dsh")
  [[ ${#found[@]} -eq 0 ]] && found+=("dsh")   # 至少注册到 dsh 项目根
  printf '%s\n' "${found[@]}"
}

if [[ ${#TARGET_AGENTS[@]} -eq 0 ]]; then
  # macOS bash 3.2 无 mapfile，用 while read 填充
  TARGET_AGENTS=()
  while IFS= read -r line; do TARGET_AGENTS+=("$line"); done < <(detect_agents)
fi
log "目标 agent: ${TARGET_AGENTS[*]}"

# ---------- 3. 每 agent 的目标目录/注册方式 ----------
agent_dest() {  # $1=agent  $2=bundle
  case "$1" in
    dsh)         printf '%s' "${REPO_ROOT}/.dsh/skills/$2" ;;
    dsh-agents)  printf '%s' "${REPO_ROOT}/.agents/skills/$2" ;;
    claude-code) printf '%s' "${REPO_ROOT}/.claude/skills/$2" ;;
    codex)       printf '%s' "${REPO_ROOT}/.codex-skills-refs" ;;  # 占位，实际写 AGENTS.md
    pi)          printf '%s' "${REPO_ROOT}/.pi/skills/$2" ;;
  esac
}

# dsh 需要双路径：.dsh/skills（rank 100）+ .agents/skills（rank 200，与用户根同源更稳）
expand_agents() {
  local expanded=()
  for agent in "$@"; do
    if [[ "$agent" == "dsh" ]]; then
      expanded+=("dsh" "dsh-agents")
    else
      expanded+=("$agent")
    fi
  done
  printf '%s\n' "${expanded[@]}"
}

# ---------- 4. 执行安装 ----------
install_bundle() {  # $1=agent  $2=bundle
  local agent="$1" name="$2"
  case "$agent" in
    codex)
      # Codex: 在 AGENTS.md 维护 @skills/<name> 引用块
      local agents_md="${REPO_ROOT}/AGENTS.md"
      [[ -f "$agents_md" ]] || warn "AGENTS.md 不存在，将创建: $agents_md"
      local marker="<!-- register-skills: $name -->"
      if grep -qF "$marker" "$agents_md" 2>/dev/null; then
        log "[codex] $name 已注册（AGENTS.md 引用存在）"
        return 0
      fi
      if [[ $DRY_RUN -eq 1 ]]; then
        log "[codex] 将向 AGENTS.md 追加 @skills/$name 引用"
        return 0
      fi
      cat >> "$agents_md" <<EOF

$marker
- 引用仓库 skill: @skills/$name （SKILL.md 位于 skills/$name/SKILL.md）
EOF
      log "[codex] $name -> AGENTS.md 引用已追加"
      return 0
      ;;
  esac

  local dest; dest="$(agent_dest "$agent" "$name")"
  local src="$SKILLS_SRC/$name"

  if [[ -e "$dest" ]]; then
    if [[ -L "$dest" ]] && [[ "$(readlink "$dest")" == "$src" ]]; then
      log "[$agent] $name 已注册（软链一致）"; return 0
    fi
    if [[ -d "$dest" ]] && [[ ! -L "$dest" ]] && diff -rq "$src" "$dest" >/dev/null 2>&1; then
      log "[$agent] $name 已注册（内容一致）"; return 0
    fi
    log "[$agent] $name 已存在但内容/方式不同，更新为当前模式"
    if [[ $DRY_RUN -eq 0 ]]; then rm -rf "$dest"; fi
  fi

  if [[ $DRY_RUN -eq 1 ]]; then
    log "[$agent] 将注册 $name -> $dest"
    return 0
  fi

  mkdir -p "$(dirname "$dest")"
  case "$MODE" in
    link) ln -s "$src" "$dest" ;;
    copy) cp -R "$src" "$dest" ;;
    auto)
      if ln -s "$src" "$dest" 2>/dev/null; then
        :
      else
        warn "[$agent] $name 软链失败，降级为复制"
        rm -rf "$dest"; cp -R "$src" "$dest"
      fi
      ;;
  esac
  log "[$agent] $name 已注册 -> $dest"
}

overall_ok=1
# 展开 dsh -> dsh + dsh-agents（双路径注册）
TARGET_AGENTS_EXPANDED=()
while IFS= read -r line; do TARGET_AGENTS_EXPANDED+=("$line"); done < <(expand_agents "${TARGET_AGENTS[@]}")
for agent in "${TARGET_AGENTS_EXPANDED[@]}"; do
  case "$agent" in
    dsh|dsh-agents|claude-code|codex|pi) ;;
    *) warn "未知 agent '$agent'，跳过"; continue ;;
  esac
  for name in "${BUNDLES[@]}"; do
    install_bundle "$agent" "$name" || overall_ok=0
  done
done

# ---------- 5. 汇总 ----------
if [[ $DRY_RUN -eq 1 ]]; then
  log "dry-run 完成，未写盘"
else
  log "注册完成"
  for agent in "${TARGET_AGENTS[@]}"; do
    case "$agent" in
      dsh)         log "DSH 项目根: ${REPO_ROOT}/.dsh/skills/ + ${REPO_ROOT}/.agents/skills/（重启会话后自动发现）" ;;
      claude-code) log "Claude Code 项目级: ${REPO_ROOT}/.claude/skills/" ;;
      codex)       log "Codex: AGENTS.md @skills/ 引用已维护" ;;
      pi)          log "pi-ai 项目级: ${REPO_ROOT}/.pi/skills/" ;;
    esac
  done
fi
exit $(( 1 - overall_ok ))
