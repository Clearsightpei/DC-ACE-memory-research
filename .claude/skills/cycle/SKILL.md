---
name: cycle
description: Run one full DC-ACE training cycle (run_5). Teacher picks 3 tasks → Drawer renders them in a fresh subagent (with GT vision access, tools/ quarantined) → Judge runs OCR+visual → Curator promotes via strict Claude-vision identity check. Operates on whichever run directory `active_run.txt` points to.
---

# /cycle — One DC-ACE training cycle (run_5: 3 tasks, mimic-by-vision)

You are the orchestrator for one cycle. You play **two roles
directly** (Teacher, Curator) and **dispatch the Drawer to a fresh
subagent once** (it renders all 3 tasks in one shot).

run_5 vs run_4:
- **3 tasks per cycle** (not 1).
- **Single phase** (no skeleton→brushwork split — the Drawer mimics
  the GT directly).
- **`ground_truths/` is NOT quarantined** — the Drawer sees it. Only
  `tools/` is quarantined.
- **Curator promotes only on strict Claude-vision identity check**.

## 0. Pre-flight

Read `active_run.txt` from the project root.

```bash
PROJECT_ROOT="$(pwd)"
RUN_REL=$(cat active_run.txt 2>/dev/null || echo runs/run_5)
RUN_DIR="$PROJECT_ROOT/$RUN_REL"
cd "$RUN_DIR"
```

**Single-repo git model.** Runs are plain folders in the one
project repo. Every commit is scoped to the run folder:

```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "<message>"
```

Never `git add -A` at the project root.

**Per-run postmortem rule.** Before activating a new run, the
prior run's `POSTMORTEM.md` MUST exist (enforced by `new_run.sh`).

**Quarantine crash recovery.** If `$RUN_DIR/.drawer_quarantine`
exists from a prior crash, restore:

```bash
if [ -f "$RUN_DIR/.drawer_quarantine" ]; then
  Q=$(cat "$RUN_DIR/.drawer_quarantine")
  echo "RECOVER: prior quarantine $Q — restoring"
  [ -d "$Q/tools" ] && [ ! -e "$RUN_DIR/tools" ] && mv "$Q/tools" "$RUN_DIR/tools"
  rmdir "$Q" 2>/dev/null
  rm "$RUN_DIR/.drawer_quarantine"
fi
```

(Note: run_5 only quarantines `tools/`, not `ground_truths/`.)

**Stop check.** If `./.stop` exists in the run dir, exit without
doing anything else.

Otherwise, read into working memory:
- `cycle_state.json` — current cycle number.
- `teaching_plan.md`, `teaching_log.md`, `cycle_summary.md`.
- `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`.

Let `N = cycle_state.json["cycle"] + 1`.

## 1. Teacher phase (main thread plays this role)

Read `.claude/skills/teacher/SKILL.md` and follow it. Output:

- **Mastery audit of cycle N-1** (Claude-vision check of last
  batch's attempts vs GTs; carry-overs flagged).
- 3-task slate.
- `task_briefs/cycle_<N>.md` and `task_briefs/cycle_<N>_dataset.json`.
- `ground_truths/cycle_<N>/0K_<char>.png` for K = 1, 2, 3
  (generated via `tools/make_char_gt.py`).
- Updated `teaching_plan.md` and appended `teaching_log.md`.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} teacher: slate=<c1>/<c2>/<c3>, phase=<…>"
```

## 2. Drawer phase (fresh subagent)

The Drawer writes ONE `attempts/cycle_<N>/generated.py` that
renders all 3 tasks, each to `attempts/cycle_<N>/0K_<char>.png`.

### 2a. Quarantine `tools/` BEFORE spawning

```bash
TS=$(date +%Y%m%d_%H%M%S)
Q="/tmp/dcace_quarantine/${RUN_REL//\//_}_cycle_${N}_${TS}_$$"
mkdir -p "$Q"
[ -d "$RUN_DIR/tools" ] && mv "$RUN_DIR/tools" "$Q/tools"
printf '%s\n' "$Q" > "$RUN_DIR/.drawer_quarantine"
ls "$RUN_DIR" | grep -Eq '^tools$' && { echo "QUARANTINE FAILED"; exit 1; }
```

(`ground_truths/` stays in place — the Drawer needs to see it.)

### 2b. Spawn the Drawer subagent

Spawn a fresh Agent (`subagent_type: general-purpose`). The prompt:

- Contents of `.claude/skills/drawer/SKILL.md`.
- The cycle number `N`.
- An explicit allowlist reminder: the Drawer may read the GT PNGs
  in `ground_truths/cycle_${N}/`, `success_bank/`,
  `principle_bank.md`, `sandbox.md`, the task brief, and its own
  attempt PNGs. It may NOT read `tools/` (physically absent),
  prior `attempts/`, `judge_results/`, `teaching_*`, or other runs.

The subagent:
1. Reads the 3 GT PNGs.
2. Reads success_bank + principle_bank.
3. Writes `attempts/cycle_<N>/generated.py` with `task_01/02/03`.
4. Runs it, viewing each task's PNG vs its GT, refining ≤ 2x per task.
5. Returns a brief summary.

### 2c. Restore + run + audit

```bash
Q=$(cat "$RUN_DIR/.drawer_quarantine" 2>/dev/null || true)
if [ -n "$Q" ] && [ -d "$Q" ]; then
  [ -d "$Q/tools" ] && mv "$Q/tools" "$RUN_DIR/tools"
  rmdir "$Q" 2>/dev/null
  rm "$RUN_DIR/.drawer_quarantine"
fi
```

Run the generated script (the Drawer may have already run it, but
re-run on the orchestrator side as the source of truth):

```bash
python3 -c "
import subprocess, sys
try:
    r = subprocess.run(['python3', 'attempts/cycle_${N}/generated.py'],
                       timeout=120, capture_output=True, text=True)
    print(r.stdout); print(r.stderr, file=sys.stderr)
    sys.exit(r.returncode)
except subprocess.TimeoutExpired:
    print('TIMEOUT'); sys.exit(124)
"
```

Audit `generated.py` for forbidden-path references. The Drawer
legitimately reads `ground_truths/` in run_5, so only flag:
`tools/`, `from strokes`, `import strokes`, references to other
run directories under `runs/`, and `subprocess` / `os.system`.
Write `judge_results/cycle_${N}_drawer_audit.txt`. Abort the cycle
if a leak is detected.

Verify the 3 PNGs exist at `attempts/cycle_<N>/0K_<char>.png`.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} drawer: <c1>/<c2>/<c3>"
```

## 3. Judge phase

Read `task_briefs/cycle_<N>_dataset.json`. Run `tools/judge.py`
(visual_score + OCR) on the 3 tasks:

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

The Curator will augment this JSON with the per-task vision
rubric.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge: <K>/3 OCR-correct (judge panel pending)"
```

## 3.5. Judge Panel — 3 fresh-context skeptics per task

For each task K in {1, 2, 3}, spawn **3 fresh `general-purpose`
Agent subagents in parallel**. Each gets only:

- The cycle number, the task index K, and the **target character `c`**.
- Paths to `attempts/cycle_<N>/0K_<c>.png` and `ground_truths/cycle_<N>/0K_<c>.png`.
- A frozen brief (verbatim): *"You are an independent skeptic. Open
  both images. Answer one question with one word + one sentence: is
  the attempt UNAMBIGUOUSLY the target character `<c>`? Reply with
  YES or NO on line 1 and a single sentence reason on line 2. Bias
  toward NO when in doubt — false-positive promotions contaminate
  the success bank. You have no access to the Drawer's intent, the
  brief, or prior commentary. Pure visual identity judgment only."*
- Subagent type: `general-purpose`.
- No other context, no project files, no Success Bank.

Collect the 3 verdicts per task. Record them in
`judge_results/cycle_<N>.json` under `judge_panel`:

```json
{ "index": K, "verdicts": ["YES", "YES", "NO"],
  "reasons": ["sentence 1", "sentence 2", "sentence 3"],
  "unanimous_yes": false }
```

**Spawning all 9 subagents (3 tasks × 3 judges) in a SINGLE message
with parallel Agent tool calls is preferred** to keep wall-clock low.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge panel: <K>/3 unanimous"
```

## 4. Curator phase (main thread plays this role)

Read `.claude/skills/curator/SKILL.md`. For each task K = 1, 2, 3:

1. Open attempt PNG and GT PNG.
2. Apply the **strict-vision identity check**: is this
   unambiguously the target character?
3. If YES, score rubric. If ≥ 7 with no 0, promote to Success
   Bank. Else carry over with sandbox notes.
4. If NO or uncertain, carry over with sandbox notes.

After all 3:
- Update `success_bank/INDEX.md` for any promotions.
- Run `python3 success_bank/build_visual_index.py` if promotions.
- Promote any verified rules from Sandbox to Principle Bank.
- Write `cycle_summary.md` and `dashboard.md`.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} curator: <K>/3 promoted (<promoted-list>)"
```

## 5. Wrap

Update `cycle_state.json`:

```json
{
  "cycle": <N>,
  "phase": <1..4 educational phase>,
  "current_slate": ["<c1>", "<c2>", "<c3>"],
  "last_promoted": ["<chars promoted>"],
  "last_carry_overs": ["<chars carried over>"],
  "last_finished_at": "<ISO>",
  "success_bank_size": <count>,
  "notes": "..."
}
```

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL/cycle_state.json"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} state: bump"
```

## 6. Push

```bash
git -C "$PROJECT_ROOT" push origin HEAD || echo "push deferred"
```

## Error policy

- Never `git add -A` at project root.
- Never delete `ground_truths/`, `attempts/`, or `judge_results/`.
- If the Drawer audit detects a `tools/` leak, abort and commit
  `cycle ${N} blocked: tools-leak detected`.

## Done

Output a final line:
> Cycle <N> complete. Slate: <c1>/<c2>/<c3>. Promoted: <K>/3 (<list>). Carry-overs: <list>. Success Bank size: <M>.
