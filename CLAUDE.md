# CLAUDE.md — DC-ACE: Emergent Memory Run

This project is a research observation, not a controlled comparison.
A repeating Claude-driven loop trains itself to draw Chinese characters
with Python `turtle`. We watch what kind of memory **emerges** from
its own outputs over many cycles. We do **not** prescribe a memory
schema or compare strategies.

## The loop

A repeating cycle, fired every 10 minutes by Claude Code's `/loop`:

```
Teacher → Drawer (fresh subagent) → Judge → Curator → 4 git commits → next fire
```

- **Teacher** (main thread) decides **6 tasks**, generates ground-truth PNGs, writes a task brief. Pacing is the Teacher's *except* a hard no-skipping gate: it may not leave Phase 1 while any introduced stroke is below the fidelity threshold (see Phase progression).
- **Drawer** is **dispatched to a fresh subagent each cycle**, with strict read-access limits — it cannot see ground truths or `tools/` (those leak the answer key into its memory). Reads only `drawer_memory.md` and the task brief; writes only its `attempts/cycle_N/` output.
- **Judge** (`tools/judge.py`) — primary signal is a **composite shape-fidelity score** (`visual_score` = Dice overlap + symmetric Chamfer + proportion; monotonic, detail-sensitive, calibrated so faithful single strokes ≈0.94–1.00). OCR (RapidOCR) is an **optional, Teacher-configured aid** via the dataset's `judge.use_ocr` block (off for strokes, on for characters by default); OCR can pass a glyph that is obviously wrong to a human, so it is secondary. `--legacy-visual` reproduces the old phase-correlation metric. DeepSeek-OCR `comparison_markdown` still optional.
- **Curator** (main thread) reads judge results + drawer code + ground truths (legitimately, for diagnosis), and edits `drawer_memory.md` plus writes `cycle_summary.md` for the next Teacher.

Single-writer rule per file. The Curator is the only writer of
`drawer_memory.md`, which is **the artifact under study**.

## Multi-run support — ONE repo, runs are folders

All runs live as **plain folders inside this single project repo**
(`github.com/Clearsightpei/DC-ACE-memory-research`). There are no
per-run git repos and no per-run GitHub remotes — every run's
cycle-by-cycle history is committed to and pushed from the one project
repo. This is deliberate: a research paper needs one repository whose
commit log *is* the emergence record; many commits in one repo is
clean, many repos is not.

```
.claude/skills/cycle|teacher|drawer|curator/SKILL.md   # role briefings (shared)
dc_ace_template/                                       # pristine scaffold, source for new_run.sh
runs/run_1/                                            # the first run (12-cycle log, frozen)
runs/run_2/                                            # the active run
runs/<run_name>/                                       # additional runs (plain folders)
new_run.sh                                             # create a fresh run from the template
active_run.txt                                         # one line: path of the active run
```

- **Start a new run**: `./new_run.sh run_3` — creates `runs/run_3/`
  from the template (a plain folder) and commits "cycle 0 init" to the
  project repo.
- **Switch active run**: `echo runs/run_3 > active_run.txt`. The
  `/cycle` skill reads this file.
- **Old runs are never overwritten** — each is a permanent folder; its
  history is the project repo's commit log filtered to that folder
  (`git log -- runs/run_1`).
- **`/cycle` git rule**: commits stage **only** the active run folder
  (`git -C <root> add runs/<name>`), never `-A` at root (root carries
  unrelated WIP + secrets), and push every cycle to `origin`.

`runs/run_1/` is the completed 12-cycle first experiment (old
phase-correlation judge). Its granular cycle-by-cycle history also
remains archived at https://github.com/Clearsightpei/dc-ace-run as a
redundant backup; the consolidated repo holds run_1's final state and
carries run_2-onward with full per-cycle history.

## Starting and stopping

From Claude Code in the project root, three usage modes:

1. **One cycle on demand**: `/cycle` — runs Teacher → Drawer → Judge → Curator once and stops.
2. **Batch run**: tell Claude `do N cycles` (e.g., "do 5 cycles") — Claude invokes `/cycle` N times in sequence in one turn, then stops. Use this for normal experimentation; the permission allowlist in `.claude/settings.local.json` covers everything `/cycle` does, so no per-step approvals.
3. **Auto-fire on a schedule** (rarely needed): `/loop 10m /cycle` — fires every 10 min until you Esc or until `.stop` is placed.

Pause / resume the auto-fire variant: `<run_dir>/stop_loop.sh` / `start_loop.sh`. The batch and on-demand variants don't need pausing — they stop themselves.

## File ownership (single-writer rule)

| File                              | Owner    |
|-----------------------------------|----------|
| `teaching_plan.md`                | Teacher  |
| `teaching_log.md` (append-only)   | Teacher  |
| `task_briefs/`, `ground_truths/`  | Teacher  |
| `attempts/cycle_<N>/`             | Drawer (subagent) |
| `judge_results/cycle_<N>.json`    | Judge    |
| `drawer_memory.md`                | Curator  |
| `cycle_summary.md`                | Curator  |
| `dashboard.md`                    | Curator  |
| `cycle_state.json`                | `/cycle` orchestrator |

## Phase progression (Teacher decides)

| Phase | What is taught       | Tool used by Teacher                 |
|-------|----------------------|--------------------------------------|
| 1     | Atomic strokes       | `tools/make_stroke_gt.py`            |
| 2     | Simple characters    | `tools/make_char_gt.py` (graphics.txt) |
| 3     | Complex characters   | `tools/make_char_gt.py`              |

Pacing within a phase is the Teacher's, and is part of what we observe
— **but advancement is gated**: the Teacher may not leave Phase 1 while
any stroke it has introduced is still below the fidelity threshold
(`visual_score >= 0.85`, measured on a cycle *after* the Curator's
reflection on that stroke). The old metric was too noisy for any
threshold; the new composite judge is calibrated so faithful single
strokes score 0.94–1.00 and crude/wrong ones ≤0.51, which makes 0.85 a
clean "the calligraphic detail (顿笔/小折/弧度) is actually there" line.
The Teacher tracks a stroke-mastery checklist in `teaching_plan.md`.
"At least finish the strokes" is a rule now, not a hope.

## Reading the experimental record

(One repo now — filter the log to the run folder.)

- **What memory emerged?** `git log -p -- runs/<name>/drawer_memory.md`
- **How did pedagogy evolve?** `git log -p -- runs/<name>/teaching_plan.md`
- **Per-cycle summary:** `git log --oneline -- runs/<name>`
- run_1's pre-consolidation granular log is also at the archived
  `dc-ace-run` GitHub repo.

## Existing assets retained

- `PNG生产程序/chinese_strock.py` — original 32-stroke library (vendored into `tools/strokes.py` of each run).
- `draw_character/graphics.txt` — MakeMeAHanzi stroke-median database. **MMH `medians` use math-convention coords (y grows UP); the `make_char_gt.py` transform is identity, not a flip.** Earlier versions flipped y and rendered every character upside-down.
- `PNG Ground Truth/` — historical reference data.
- `judge.py` (root) — the *original* phase-correlation judge, kept as a
  historical record. New runs get the **composite shape-fidelity judge**
  from `dc_ace_template/tools/judge.py`; the frozen `runs/run_1/` keeps
  the old judge it ran with.

## Pilot history (cycles 1–5, deleted)

The first 5 cycles ran but had two confounds: (1) the same Claude session played all three roles, so the Drawer recalled `strokes.py` parameters from earlier turns instead of deriving from observation; (2) the `make_char_gt.py` y-flip bug rendered all Phase-2 ground truths upside-down. Both have been fixed; the polluted history is removed from the git log of the original first run (now `runs/run_1/`, archived at the `dc-ace-run` repo). See `~/.claude/plans/should-i-install-rapid-lexical-lantern.md` for the postmortem.
