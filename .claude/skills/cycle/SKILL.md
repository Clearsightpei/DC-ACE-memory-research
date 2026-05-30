---
name: cycle
description: Run one full DC-ACE training cycle (Teacher → Drawer → Judge → Curator → commit). Designed to be fired repeatedly via `/loop 10m /cycle`. Operates on whichever run directory `active_run.txt` points to.
---

# /cycle — One DC-ACE training cycle

You are the orchestrator for one cycle of an emergent-memory experiment.
Across the cycle you play **two roles directly** (Teacher, Curator) and
**dispatch the Drawer to a fresh subagent** so it cannot inherit your
conversation context.

## 0. Pre-flight

Read `active_run.txt` from the project root. It contains one line — the
path (relative to the project root) of the active run directory. If it
doesn't exist, default to `runs/run_2`.

```bash
PROJECT_ROOT="$(pwd)"                                  # the single git repo
RUN_REL=$(cat active_run.txt 2>/dev/null || echo runs/run_2)
RUN_DIR="$PROJECT_ROOT/$RUN_REL"
cd "$RUN_DIR"                                           # tool cmds use run-relative paths
```

**Single-repo git model.** Runs are plain folders inside the ONE
project repo (`github.com/Clearsightpei/DC-ACE-memory-research`). There
is no per-run repo. **Every commit in this skill goes to the project
repo, scoped to the run folder**, using:

```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "<message>"
```

NEVER run `git add -A` / `git add .` at the project root (the root has
unrelated work-in-progress and untracked files, incl. secrets). Only
ever stage `"$RUN_REL"`. The commit-message scheme is unchanged.

**Per-run postmortem rule.** Every run folder must contain a
`POSTMORTEM.md` written when it is *frozen* (the core problem that run
surfaced and why it motivates the next run). This is enforced at run
creation (`new_run.sh` warns if the previously-active run lacks one).
`/cycle` does not block on it, but never start a *new* run without
having written the prior run's `POSTMORTEM.md` first.

**Quarantine crash recovery.** If `$RUN_DIR/.drawer_quarantine` exists,
a prior Drawer phase was interrupted between quarantining the GTs and
restoring them. Recover **before doing anything else**:

```bash
if [ -f "$RUN_DIR/.drawer_quarantine" ]; then
  Q=$(cat "$RUN_DIR/.drawer_quarantine")
  echo "RECOVER: prior quarantine $Q — restoring"
  [ -d "$Q/ground_truths" ] && [ ! -e "$RUN_DIR/ground_truths" ] && mv "$Q/ground_truths" "$RUN_DIR/ground_truths"
  [ -d "$Q/tools" ]         && [ ! -e "$RUN_DIR/tools" ]         && mv "$Q/tools"         "$RUN_DIR/tools"
  rmdir "$Q" 2>/dev/null
  rm "$RUN_DIR/.drawer_quarantine"
fi
```

**Stop check.** If `./.stop` exists in the run dir, output exactly:
> Loop stopped (.stop sentinel present in $RUN_DIR). To resume, delete that file. To halt /loop fully, press Esc.

…and exit the cycle without doing anything else. Do **not** commit.

Otherwise, read these files into your working memory:
- `cycle_state.json` — current cycle number, phase, last batch
- `teaching_plan.md` — Teacher's pedagogy (Teacher-owned)
- `teaching_log.md` — Teacher's append-only history (Teacher-owned)
- `cycle_summary.md` — Curator's last-cycle note to Teacher
- `drawer_memory.md` — current drawer memory (Curator-owned)

Let `N` = `cycle_state.json["cycle"] + 1` (this run's cycle number).

## 1. Teacher phase (main thread plays this role)

Read `.claude/skills/teacher/SKILL.md` and follow it as your role brief.
Output of this phase:
- 1–N ground-truth PNGs in `ground_truths/cycle_{N}/`
- `task_briefs/cycle_{N}.md` describing what the Drawer must draw
  - **Describe each task by key/character/meaning only** — do NOT include the GT image filename in any human-readable hint that the Drawer subagent will receive. The Drawer cannot see GT images.
- `task_briefs/cycle_{N}_dataset.json` (judge-compatible dataset file)
- updates to `teaching_plan.md` (if pedagogy evolved) and `teaching_log.md` (always)

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} teacher: <one-line summary of today's plan>"
```

## 2. Drawer phase (dispatched to a fresh subagent — DO NOT play this role yourself)

**Experimental integrity — hard isolation.** The Drawer subagent runs
in the same harness with the same `Read`/`Bash` tools as the
orchestrator. Prompt-only restrictions are NOT enough. Before spawning
it you MUST physically quarantine the answer key and tools so they
cannot be accessed even if the subagent ignored the prompt. After it
returns, audit its output. Both steps are mandatory.

### 2a. Quarantine (A: hard prevention) — BEFORE spawning the subagent

Move `ground_truths/` and `tools/` out of the project tree to a temp
location, leaving a marker for crash recovery:

```bash
TS=$(date +%Y%m%d_%H%M%S)
Q="/tmp/dcace_quarantine/${RUN_REL//\//_}_cycle_${N}_${TS}_$$"
mkdir -p "$Q"
[ -d "$RUN_DIR/ground_truths" ] && mv "$RUN_DIR/ground_truths" "$Q/ground_truths"
[ -d "$RUN_DIR/tools" ]         && mv "$RUN_DIR/tools"         "$Q/tools"
printf '%s\n' "$Q" > "$RUN_DIR/.drawer_quarantine"
ls "$RUN_DIR" | grep -Eq '^(ground_truths|tools)$' && \
  { echo "QUARANTINE FAILED — ground_truths or tools still present; ABORT"; exit 1; }
echo "quarantined to $Q"
```

Verify (sanity, must print "MISSING" for both before continuing):
```bash
test -e "$RUN_DIR/ground_truths" && echo "ground_truths PRESENT (BAD)" || echo "ground_truths MISSING (good)"
test -e "$RUN_DIR/tools"         && echo "tools PRESENT (BAD)"         || echo "tools MISSING (good)"
```

### 2b. Spawn the Drawer subagent

Spawn a fresh Agent with `subagent_type: general-purpose` and a prompt
that includes:
1. The full contents of `.claude/skills/drawer/SKILL.md`.
2. The active run dir path (so the subagent knows where to write).
3. The cycle number `N`.
4. An explicit allowlist:

> You may read ONLY these files:
> - `<RUN_DIR>/drawer_memory.md`
> - `<RUN_DIR>/task_briefs/cycle_${N}.md`
>
> You may write ONLY these files:
> - `<RUN_DIR>/attempts/cycle_${N}/generated.py`
> - PNGs rendered by your script into `<RUN_DIR>/attempts/cycle_${N}/`
>
> You MUST NOT read:
> - `<RUN_DIR>/ground_truths/` (the answer key)
> - `<RUN_DIR>/tools/` (the canonical Teacher implementation)
> - any prior `attempts/`, `judge_results/`, or `teaching_*` files
> - any other run directory under `runs/`
>
> If you find yourself wanting to read any forbidden file, that is a
> leak — stop and close it. Your only knowledge sources are the two
> allowed files plus what you can derive from the task brief's
> textual description.

The subagent does not inherit this conversation's context — it starts
fresh. The prompt's "MUST NOT read" list is now redundant defense —
the paths physically don't exist during its turn (Step 2a) — but keep
the list for clarity and as documentation of intent.

After it returns, verify that `attempts/cycle_${N}/generated.py`
and at least one PNG exist. Then **immediately do Steps 2c (restore)
and 2d (audit) BEFORE running the generated code or committing.**

### 2c. Restore (always, even on subagent failure)

```bash
Q=$(cat "$RUN_DIR/.drawer_quarantine" 2>/dev/null || true)
if [ -n "$Q" ] && [ -d "$Q" ]; then
  [ -d "$Q/ground_truths" ] && mv "$Q/ground_truths" "$RUN_DIR/ground_truths"
  [ -d "$Q/tools" ]         && mv "$Q/tools"         "$RUN_DIR/tools"
  rmdir "$Q" 2>/dev/null
  rm "$RUN_DIR/.drawer_quarantine"
  echo "restored from $Q"
fi
test -d "$RUN_DIR/ground_truths" || echo "WARN: ground_truths not restored"
test -d "$RUN_DIR/tools"         || echo "WARN: tools not restored"
```

### 2d. Audit the subagent's output (B: post-spawn audit)

Even with quarantine, audit the produced artifacts for any
forbidden-path references — a defense-in-depth integrity check that
also produces an audit log for the experimental record:

```bash
AUDIT="$RUN_DIR/judge_results/cycle_${N}_drawer_audit.txt"
mkdir -p "$RUN_DIR/judge_results"
LEAK=0
{
  echo "Drawer audit — cycle ${N} ($(date -u +%FT%TZ))"
  echo "Quarantine path: $Q"
  echo
  echo "[1] Files in attempts/cycle_${N}/ (only expected PNGs + generated.py):"
  ls -1 "$RUN_DIR/attempts/cycle_${N}/" 2>/dev/null
  echo
  echo "[2] Forbidden-path references in generated.py:"
  if grep -nE 'ground_truths|/tools/|tools\.(strokes|make_(stroke|char)_gt|judge)|/dcace_quarantine/|\.\./\.\./draw_character' "$RUN_DIR/attempts/cycle_${N}/generated.py" 2>/dev/null; then
    echo "→ LEAK INDICATOR: generated.py references a forbidden path."
    LEAK=1
  else
    echo "(none — clean)"
  fi
  echo
  echo "[3] Quarantine marker cleanup:"
  [ -f "$RUN_DIR/.drawer_quarantine" ] && { echo "→ LEAK INDICATOR: quarantine marker still present"; LEAK=1; } \
                                       || echo "(marker removed — clean)"
} > "$AUDIT"
cat "$AUDIT"
if [ "$LEAK" -ne 0 ]; then
  echo "DRAWER AUDIT FAILED — committing block-out and aborting cycle."
  git -C "$PROJECT_ROOT" add "$RUN_REL"
  git -C "$PROJECT_ROOT" commit -m "cycle ${N} blocked: drawer-audit leak (see judge_results/cycle_${N}_drawer_audit.txt)"
  exit 1
fi
```

Also inspect the subagent's returned summary text for any
"no such file" / "ground_truths" / "tools" mentions — those would
indicate the subagent *tried* to access quarantined paths. If found,
note in the audit and treat as a soft warning (the access was blocked
by Step 2a, but the attempt is worth recording).

### 2e. Run the generated code with a hard timeout

```bash
python3 -c "
import subprocess, sys
try:
    r = subprocess.run(['python3', 'attempts/cycle_${N}/generated.py'], timeout=60, capture_output=True, text=True)
    print(r.stdout); print(r.stderr, file=sys.stderr)
    sys.exit(r.returncode)
except subprocess.TimeoutExpired:
    print('TIMEOUT after 60s', file=sys.stderr); sys.exit(124)
"
```

(macOS doesn't ship the `timeout` command; this Python wrapper is portable.)

If the script crashes or times out, write `attempts/cycle_${N}/ERROR.txt`
with the failure message and continue (the judge will record blank/missing
PNGs as failures — that's the correct signal).

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} drawer: <one-line note on what the subagent produced>"
```

## 3. Judge phase (GT / OCR signals — only if the Teacher selected them)

Read the dataset's `judge.eval` field
(`task_briefs/cycle_${N}_dataset.json`). It is a `+`-joined subset of
`gt`, `ocr`, `vision` (defaults if absent: strokes → `vision`;
characters → `gt+ocr+vision`). The Teacher is the tool orchestrator —
**honor its choice**.

**Run `tools/judge.py` only if `eval` includes `gt` or `ocr`.** (If
`eval` is `vision` only — the typical stroke cycle — there is no GT;
**skip judge.py entirely** and `judge_results/cycle_${N}.json` is
created fresh by Step 3.5 instead.)

```bash
python tools/judge.py \
    --mode 1 \
    --ai-png-dir attempts/cycle_${N}/ \
    --gt-png-dir ground_truths/cycle_${N}/ \
    --dataset task_briefs/cycle_${N}_dataset.json \
    --generated-code attempts/cycle_${N}/generated.py \
    --output judge_results/cycle_${N}.json \
    --skip-coords
```

`--skip-coords` is the safe default (the DeepSeek-OCR Ollama call requires
a remote server that may not be reachable). `use_ocr` in the dataset
drives RapidOCR; do **not** pass `--skip-ocr` (emergency override only).
`visual_score` is the composite shape-fidelity metric (Dice+Chamfer+
proportion); `scoring_mode` is `visual_only` (OCR off) or
`blended_0.6_0.4` (OCR on). For **characters** a low `visual_score` is
normal (cross-renderer; run_1 correct chars sat 0.03–0.40) — it is a
regression signal, not a pass/fail gate. `--legacy-visual` is never
used in normal cycles. If the judge command itself errors, write stderr
to `judge_results/cycle_${N}_error.txt` and continue; don't retry.

## 3.5 Calligraphy rubric (Claude-vision — only if `eval` includes `vision`)

If `eval` includes `vision`, **you (the orchestrator) score a
reference-free calligraphy rubric using your built-in vision** — no
API, no subprocess. For each attempt PNG in `attempts/cycle_${N}/`
(the `NN_<key>.png` files), open **only the attempt** (NOT the GT —
this signal must stay reference-free) and score this **fixed rubric**,
each criterion an integer band **0 / 1 / 2**:

| criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| `dunbi` 顿笔 (pause/weight at start/turn/end) | absent | partial | clearly present |
| `hudu` 弧度 (natural curvature, not robotic) | wrong/none | crude | natural |
| `taper` 粗细 (stroke-width variation) | uniform line | slight | clear brush taper |
| `proportion` (relative size/placement/balance) | distorted | off | balanced |
| `overall` (reads as brush-written 楷书) | no | weak | yes |

`total` = sum (0–10). Write a **one-line rationale per criterion**
referencing only what is visible in the attempt.

Then write/augment `judge_results/cycle_${N}.json` (a JSON **list**,
one dict per task in index order). If judge.py ran (Step 3), augment
each existing dict; if it didn't (vision-only), create the list with
one dict per task containing at least
`{index, character, pinyin}`. Add to each dict:

```json
"calligraphy_rubric": {
  "dunbi": 0-2, "hudu": 0-2, "taper": 0-2, "proportion": 0-2, "overall": 0-2,
  "total": 0-10, "max": 10,
  "rationale": {"dunbi": "...", "hudu": "...", "taper": "...",
                "proportion": "...", "overall": "..."},
  "scored_by": "orchestrator-vision", "rubric_version": 1
}
```

Never blend the rubric into `final_score`/`visual_score` — it is a
parallel, independently logged signal. Keep `visual_score`, OCR
fields, `scoring_mode` untouched when augmenting.

Commit (single commit for steps 3 + 3.5):
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge: eval=<eval>, <signals summary e.g. avg_rubric=<Y>/10, K/6 ocr-ok, avg_visual=<X.XX>>"
```

## 4. Curator phase (main thread plays this role — DOES have GT access)

Read `.claude/skills/curator/SKILL.md` and follow it as your role brief.
The Curator legitimately needs full access — GTs, attempts, judge
results, drawer code — to diagnose what happened. Output:

- edits to `drawer_memory.md` (the Curator owns this file completely — may add, edit, restructure, or delete entries)
- `cycle_summary.md` — overwritten with a 1–3 sentence note describing what kind of mistake happened, for the next Teacher cycle to read
- `dashboard.md` — overwritten with a fresh status snapshot

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} curator: <one-line rationale for the memory edit>"
```

## 5. Wrap

Update `cycle_state.json`:
- increment `cycle` to `N`
- update `phase`, `last_batch`, `last_pass_count`, `last_total` from this run
- bump `last_finished_at` to current ISO timestamp

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL/cycle_state.json"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} state: bump"
```

## 6. Push to the one project repo

All cycle commits live in `github.com/Clearsightpei/DC-ACE-memory-research`.
Push the current branch (continuous history is the experiment's primary
artifact — push every cycle):

```bash
git -C "$PROJECT_ROOT" push origin HEAD || echo "push failed (offline?) — commits are safe locally, will push next cycle"
```

(`HEAD` pushes whatever branch the project repo is on; do not force.)

## Error policy (across all phases)

- Never use `git commit --no-verify`, `git push --force`, or `git reset --hard` from within `/cycle`.
- Never `git add -A`/`git add .` at the project root, and never `git -C "$PROJECT_ROOT" add` anything other than paths under `"$RUN_REL"`. The project root carries unrelated WIP and untracked secrets — staging only the run folder keeps cycle commits clean and safe.
- If a `git commit` fails because there are no changes, that is fine — skip and continue.
- Never delete `ground_truths/`, `attempts/`, or `judge_results/` from prior cycles.
- Never edit a file outside the active run dir (except for spawning the Drawer subagent, which lives in `.claude/skills/`).
- If you cannot complete a phase, write a short note to `dashboard.md`
  explaining what blocked you, commit it as
  `cycle ${N} blocked: <reason>`, and exit.

## Done

Output a single final line in your reply:
> Cycle N complete. K/T tasks correct. Next /cycle will fire in ~10 min (loop owns timing).
