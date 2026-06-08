---
name: cycle
description: Run one full DC-ACE training cycle (Teacher → Drawer-skeleton → Curator-skeleton-review → Drawer-brushwork → Curator-brushwork-review → commit). Two phases per cycle (skeleton + brushwork). Operates on whichever run directory `active_run.txt` points to.
---

# /cycle — One DC-ACE training cycle (run_4: two-phase)

You are the orchestrator for one cycle of an emergent-memory experiment.
Across the cycle you play **two roles directly** (Teacher, Curator) and
**dispatch the Drawer to a fresh subagent twice** (once for skeleton,
once for brushwork) so it cannot inherit your conversation context.

## 0. Pre-flight

Read `active_run.txt` from the project root.

```bash
PROJECT_ROOT="$(pwd)"
RUN_REL=$(cat active_run.txt 2>/dev/null || echo runs/run_4)
RUN_DIR="$PROJECT_ROOT/$RUN_REL"
cd "$RUN_DIR"
```

**Single-repo git model.** Runs are plain folders in the one project
repo. Every commit is scoped to the run folder:

```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "<message>"
```

Never `git add -A` at the project root.

**Per-run postmortem rule.** Before activating a new run, the prior
run's `POSTMORTEM.md` MUST exist (enforced by `new_run.sh`).

**Quarantine crash recovery.** If `$RUN_DIR/.drawer_quarantine`
exists, restore before doing anything else:

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

**Stop check.** If `./.stop` exists in the run dir, exit without
doing anything else. Do not commit.

Otherwise, read into working memory:
- `cycle_state.json` — current cycle number, focus, last attempt.
- `teaching_plan.md`, `teaching_log.md`, `cycle_summary.md`.
- `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`.

Let `N = cycle_state.json["cycle"] + 1`.

## 1. Teacher phase (main thread plays this role)

Read `.claude/skills/teacher/SKILL.md` and follow it. Pick ONE focus
for this cycle. Verify all prerequisites are in the Success Bank
(or switch focus to the missing prerequisite). Output:

- `task_briefs/cycle_<N>.md` and `task_briefs/cycle_<N>_dataset.json`.
- Updated `teaching_plan.md` and appended `teaching_log.md`.
- `ground_truths/cycle_<N>/` (only if eval includes `gt`).

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} teacher: focus=<char>, phase=<…>"
```

## 2. Drawer phase A — SKELETON (fresh subagent)

The Drawer writes `attempts/cycle_<N>/generated_skel.py` using
uniform pensize 3 (no brushwork). Goal: get composition right.

### 2a. Quarantine (BEFORE spawning)

Move `ground_truths/` and `tools/` to a temp location:

```bash
TS=$(date +%Y%m%d_%H%M%S)
Q="/tmp/dcace_quarantine/${RUN_REL//\//_}_cycle_${N}_${TS}_$$"
mkdir -p "$Q"
[ -d "$RUN_DIR/ground_truths" ] && mv "$RUN_DIR/ground_truths" "$Q/ground_truths"
[ -d "$RUN_DIR/tools" ]         && mv "$RUN_DIR/tools"         "$Q/tools"
printf '%s\n' "$Q" > "$RUN_DIR/.drawer_quarantine"
ls "$RUN_DIR" | grep -Eq '^(ground_truths|tools)$' && \
  { echo "QUARANTINE FAILED"; exit 1; }
```

### 2b. Spawn Drawer subagent for skeleton

Spawn a fresh Agent (`subagent_type: general-purpose`) with the
contents of `.claude/skills/drawer/SKILL.md` and an explicit
phase indicator: **"PHASE = A (skeleton). Use uniform pensize 3.
Output `attempts/cycle_<N>/generated_skel.py`. Self-preview budget = 2."**

The subagent reads `success_bank/`, `principle_bank.md`, `sandbox.md`,
and the task brief. It writes the skeleton script, runs it, views its
own PNG, refines (max 2 iterations), and commits.

### 2c. Restore + run + audit

```bash
Q=$(cat "$RUN_DIR/.drawer_quarantine" 2>/dev/null || true)
if [ -n "$Q" ] && [ -d "$Q" ]; then
  [ -d "$Q/ground_truths" ] && mv "$Q/ground_truths" "$RUN_DIR/ground_truths"
  [ -d "$Q/tools" ]         && mv "$Q/tools"         "$RUN_DIR/tools"
  rmdir "$Q" 2>/dev/null
  rm "$RUN_DIR/.drawer_quarantine"
fi
```

Run the generated skeleton script:
```bash
python3 -c "
import subprocess, sys
try:
    r = subprocess.run(['python3', 'attempts/cycle_${N}/generated_skel.py'],
                       timeout=60, capture_output=True, text=True)
    print(r.stdout); print(r.stderr, file=sys.stderr)
    sys.exit(r.returncode)
except subprocess.TimeoutExpired:
    print('TIMEOUT'); sys.exit(124)
"
```

Audit `generated_skel.py` for forbidden-path references and write
`judge_results/cycle_${N}_drawer_audit.txt`. Abort cycle if leak
detected.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} drawer-skel: <focus>"
```

## 3. Curator phase A — Skeleton review (main thread, has GT access)

Read `.claude/skills/curator/SKILL.md`. Open the attempt skeleton PNG
side by side with the GT skeleton PNG. Compare composition only:
endpoints, stroke count, proportions, layout. **DO NOT judge
brushwork** — the skeleton has none.

Two outcomes:

**Approved**: write `attempts/cycle_<N>/SKELETON_APPROVED` (empty
file). Append approval note to `sandbox.md`. Proceed to Phase B.

**Rejected**: write `attempts/cycle_<N>/SKELETON_REJECTED` with a
one-line reason. Write detailed composition feedback into
`sandbox.md`. **Skip Phase B** (no brushwork without an approved
skeleton). Jump to Step 5 (Curator finalize) with no Phase-B data.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} curator-skel: <approved|rejected>"
```

## 4. Drawer phase B — BRUSHWORK (only if skeleton approved)

If `attempts/cycle_<N>/SKELETON_APPROVED` exists, dispatch the Drawer
again (fresh subagent) with **"PHASE = B (brushwork). Add per-sample
pensize per Principle Bank §1 width floors to the approved skeleton.
DO NOT change any endpoint. Output `attempts/cycle_<N>/generated.py`.
Self-preview budget = 2."**

### 4a. Quarantine + spawn + restore + audit + run

Same pattern as Phase A — quarantine ground_truths and tools, spawn
the Drawer subagent, restore, audit, then run `generated.py` and
verify the brushed PNG exists at `attempts/cycle_<N>/01_<char>.png`.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} drawer-brush: <focus>"
```

### 4b. Run the judge

Read `task_briefs/cycle_<N>_dataset.json` for `judge.eval`. Run
`tools/judge.py` only if `eval` includes `gt` or `ocr`:

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

### 4c. Calligraphy rubric (vision)

If `eval` includes `vision`, you (the orchestrator) score the
calligraphy rubric by opening each attempt PNG (not the GT) and
scoring `dunbi/hudu/taper/proportion/overall` (0–2 each). Augment
`judge_results/cycle_<N>.json` with the `calligraphy_rubric` field
per task. Same rubric and JSON shape as run_3.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge: <signal summary>"
```

## 5. Curator phase B (or finalize on skeleton-rejection)

Read `.claude/skills/curator/SKILL.md`. Phase B's job:

- If Phase B ran and mastery gate met (`is_correct AND
  ocr_confidence >= 0.4 AND rubric_total >= 7 AND no rubric 0`):
  promote the entry to Success Bank, regenerate the visual index,
  promote sandbox findings to Principle Bank, reset sandbox.
- If Phase B ran but mastery gate NOT met: write detailed
  brushwork feedback to sandbox; don't add to Success Bank.
- If Phase A was rejected: just finalize the sandbox composition
  feedback from Step 3.

Write `cycle_summary.md` (overwrite) and `dashboard.md` (overwrite).

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} curator: <focus> <outcome>"
```

## 6. Wrap

Update `cycle_state.json`:

```json
{
  "cycle": <N>,
  "phase": <1..5 educational phase>,
  "current_focus": "<char or null if mastered>",
  "last_outcome": "skeleton_rejected | brushwork_failed | mastered",
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

## 7. Push

```bash
git -C "$PROJECT_ROOT" push origin HEAD || echo "push deferred"
```

## Error policy

- Never `git add -A` at project root.
- Never delete `ground_truths/`, `attempts/`, or `judge_results/`.
- If a phase is blocked, write to `dashboard.md` and commit
  `cycle ${N} blocked: <reason>`.

## Done

Output a final line:
> Cycle <N> complete. Focus: <char>. Outcome: <mastered|brushwork_failed|skeleton_rejected>. Success Bank size: <M>.
