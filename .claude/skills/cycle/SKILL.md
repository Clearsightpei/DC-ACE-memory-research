---
name: cycle
description: Run one full DC-ACE training cycle (run_6: 1 task per cycle, 米字格 anchors + joint specs, 5-gate). Teacher picks one focus and writes a structural brief → Drawer dispatches as fresh subagent → Judge runs OCR + visual + stroke-count + anchor + joint gates → 3-judge panel as safety net → Curator promotes only if all five gates pass. Operates on whichever run directory `active_run.txt` points to.
---

# /cycle — One DC-ACE training cycle (run_6 architecture)

You are the orchestrator for one cycle. You play **two roles
directly** (Teacher, Curator) and **dispatch the Drawer to a fresh
subagent** for the one task.

Run_6 vs run_5:
- **1 task per cycle** (not 3). Depth over breadth.
- **米字格 anchors + joint specs** instead of (ox, oy, scale) numbers.
- **5-gate**: OCR + visual_score (informational) + stroke-count + anchor placement + joint placement + 3-judge panel.
- **Curriculum honesty**: c1–c6 atomic strokes, c7–c13 compound strokes, c14+ characters. Each phase has its own gate set.

## 0. Pre-flight

Read `active_run.txt` from the project root.

```bash
PROJECT_ROOT="$(pwd)"
RUN_REL=$(cat active_run.txt 2>/dev/null || echo runs/run_6)
RUN_DIR="$PROJECT_ROOT/$RUN_REL"
cd "$RUN_DIR"
```

**Quarantine crash recovery**: if `$RUN_DIR/.drawer_quarantine` exists,
restore before doing anything else (same pattern as prior runs).

**Stop check**: if `./.stop` exists in the run dir, exit without
doing anything else.

Read into working memory:
- `cycle_state.json` — current cycle number, phase, current focus.
- `teaching_plan.md`, `teaching_log.md`, `cycle_summary.md`.
- `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`, `to_be_learned.md`.

Let `N = cycle_state.json["cycle"] + 1`.

## 1. Teacher phase

Read `.claude/skills/teacher/SKILL.md` and follow it. Pick **ONE focus**
for this cycle:

- **Phase 1 (c1–c6)**: 6 atomic strokes — 横, 竖, 撇, 捺, 提, 点. Each cycle masters one.
- **Phase 1.5 (c7–c13)**: 7 compound strokes — 横折, 竖钩, 横折钩, 竖弯钩, 横撇, 竖折, 横折弯钩. Each cycle masters one.
- **Phase 2 (c14+)**: simple characters using mastered strokes (joints all in Success Bank).
- **Phase 3 (later)**: multi-component characters using mastered sub-characters.

For character cycles, the Teacher runs `python tools/joint_detector.py`-derived
calls to embed the joint spec in the brief. Output:
- `task_briefs/cycle_<N>.md` — the structural brief (target char, anchor spec for each stroke, joint spec from `find_joints`).
- `task_briefs/cycle_<N>_dataset.json` — judge config.
- `ground_truths/cycle_<N>/01_<char>.png` (only for character cycles, generated via `tools/make_char_gt.py`).

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} teacher: focus=<char> phase=<…>"
```

## 2. Drawer phase

### 2a. Quarantine

Move `tools/` to a temp location so the Drawer cannot read the joint
detector or judge code directly (it sees only the brief's joint spec).
`ground_truths/` stays visible for visual reference. `success_bank/`
stays visible for primitive reuse.

```bash
TS=$(date +%Y%m%d_%H%M%S)
Q="/tmp/dcace_quarantine/${RUN_REL//\//_}_cycle_${N}_${TS}_$$"
mkdir -p "$Q"
[ -d "$RUN_DIR/tools" ] && mv "$RUN_DIR/tools" "$Q/tools"
printf '%s\n' "$Q" > "$RUN_DIR/.drawer_quarantine"
```

### 2b. Spawn Drawer subagent

Spawn a fresh `general-purpose` Agent. Brief contents = `.claude/skills/drawer/SKILL.md` + the cycle number + target char name + an explicit allowlist for files the Drawer can read.

The Drawer:
- Reads the task brief (which includes anchor spec + joint spec).
- Optionally views the GT PNG.
- Writes `attempts/cycle_<N>/generated.py` using turtle + `success_bank/code/<primitive>.py` calls.
- Self-previews up to 2 iterations (render → open own PNG vs GT → refine).
- Refuses to commit if its turtle-call count doesn't match the brief's MMH stroke count (pre-flight check).
- Returns a short summary.

### 2c. Restore + run + audit

Restore `tools/`. Run the generated script. Audit `generated.py` for forbidden references (e.g. `subprocess`, `os.system`, paths into other runs). Write `judge_results/cycle_<N>_drawer_audit.txt`. Abort the cycle if a leak is detected.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} drawer: <focus>"
```

## 3. Judge phase

Read `task_briefs/cycle_<N>_dataset.json` for `judge.eval`. Run `tools/judge.py` (the run_6 version) which now computes ALL FIVE gate inputs:

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

For each task, `judge_results/cycle_<N>.json` now contains:
- `visual_score`, `recognized_char`, `ocr_confidence`, `ocr_topk`, `ocr_margin`, `is_correct` (run_5 gate signals — informational in run_6)
- `mmh_stroke_count`, `drawer_stroke_count`, `stroke_count_pass` (Gate 4)
- `anchor_placement` — for each declared anchor, the distance from declared to rendered endpoint
- `joint_placement` — for each declared joint, the distance between participating points AND whether the meeting falls in the declared cell
- `structural_pass` — True iff stroke_count + all anchors + all joints pass

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge: structural=<pass|fail> visual=<...> OCR=<...>"
```

## 3.5. Judge Panel — 3 fresh-context skeptics

ONLY run if `structural_pass == True` from Step 3. If structural failed,
skip the panel — carry over.

Spawn **3 fresh `general-purpose` Agent subagents in parallel**. Each
gets only:
- Target character name `<c>`.
- Paths to `attempts/cycle_<N>/01_<c>.png` and `ground_truths/cycle_<N>/01_<c>.png`.
- A frozen brief: *"You are an independent skeptic. Open both images.
  Answer one question with one word + one sentence: is the attempt
  UNAMBIGUOUSLY the target character `<c>`? Reply with YES or NO on
  line 1 and a single sentence reason on line 2. Bias toward NO when
  in doubt — false-positive promotions contaminate the success bank.
  You have no access to the Drawer's intent, the brief, or prior
  commentary. Pure visual identity judgment only."*

Record verdicts in `judge_results/cycle_<N>.json` under `judge_panel`:
`{ "verdicts": ["YES","YES","NO"], "reasons": [...], "unanimous_yes": false }`.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} panel: <K>/3 YES"
```

## 4. Curator phase

Read `.claude/skills/curator/SKILL.md`. Apply the **5-gate**:

1. **OCR is_correct** AND `ocr_margin ≥ 0.3` (informational — log but don't gate on)
2. **visual_score > 0.8** (informational — log but don't gate on; was the run_5 fuzzy gate)
3. **`structural_pass == True`** — HARD gate (stroke count + all anchors + all joints)
4. **`judge_panel.unanimous_yes == True`** — HARD gate (safety net)
5. **Curator vision** — informational, used for nuance in Sandbox notes

A promotion requires gates 3 AND 4. Gates 1 + 2 are recorded but don't block.

**On promotion**:
- Write `success_bank/code/<char>.py` with anchor notation (no magic numbers).
- Append to `success_bank/INDEX.md`.
- If the character was in `to_be_learned.md`, delete its entry and append a one-line note to `to_be_learned_resolved.md`.

**On carry-over**:
- Write Sandbox feedback for the next cycle.
- If this is the 2nd consecutive carry-over for this focus, append a decomposition to `to_be_learned.md` (per the existing memory rule).

Write `cycle_summary.md` (overwrite). Write `dashboard.md` (overwrite).

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} curator: <focus> <outcome>"
```

## 5. Wrap

Update `cycle_state.json`:

```json
{
  "cycle": <N>,
  "phase": "1|1.5|2|3",
  "current_focus": "<char or null>",
  "last_outcome": "mastered | carried_over | structural_fail",
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

## Done

Output a final line:
> Cycle <N> complete. Focus: <char>. Outcome: <mastered|carried_over|structural_fail>. Success Bank size: <M>.
