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
fresh. After it returns, verify that `attempts/cycle_${N}/generated.py`
and at least one PNG exist. Then run the generated code with a hard
timeout:

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

## 3. Judge phase

Run the judge against this cycle's attempts and ground truths.

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
a remote server that may not be reachable). Drop it only if the operator
has confirmed the Ollama host is up.

**OCR is controlled by the Teacher, not here.** The judge reads the
`judge.use_ocr` block from the dataset file and enables/disables RapidOCR
itself (default: off for Phase-1 stroke datasets, on for Phase-2/3
character datasets). Do **not** add `--skip-ocr` to the command — let
the dataset drive it. (Passing `--skip-ocr` is only an emergency hard
override.)

The judge uses the new **composite shape-fidelity** `visual_score`
(Dice + Chamfer + proportion, monotonic, calibrated so faithful single
strokes ≈0.94–1.00). Each result also carries `visual_components`
(`dice`, `chamfer`, `proportion`, …) and a `scoring_mode`
(`visual_only` when OCR off → `final_score == visual_score`;
`blended_0.6_0.4` when OCR on). `--legacy-visual` exists only to
reproduce the old phaseCorrelate metric; never use it in normal cycles.

If the judge command itself errors (not the per-character results — those
are fine), write the stderr to `judge_results/cycle_${N}_error.txt` and
continue. Don't retry.

Commit:
```bash
git -C "$PROJECT_ROOT" add "$RUN_REL"
git -C "$PROJECT_ROOT" commit -m "cycle ${N} judge: <K>/<6> pass, avg_visual=<X.XX>"
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
