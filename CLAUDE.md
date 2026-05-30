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

- **Teacher** (main thread) is the **curriculum designer AND tool
  orchestrator**. Its one goal: teach the Drawer to draw the best
  *characters* possible. It decides **6 tasks** and, crucially, **which
  evaluation tool(s) to use** (`judge.eval` in the dataset): `vision`
  (reference-free Claude-vision calligraphy rubric), `gt` (composite
  shape-fidelity vs a GT), `ocr`, or any `+` combination. Pacing is a
  **soft, Teacher-judged gate** (depth over breadth — no hard pixel
  threshold).
- **Drawer** is **dispatched to a fresh subagent each cycle**, with **hard filesystem isolation** (not just a prompt restriction): `/cycle` physically moves `ground_truths/` and `tools/` out of the project tree to a quarantine location *before* spawning the subagent and restores them after. The subagent literally cannot read those paths during its turn. A post-spawn audit greps the produced `generated.py` for forbidden-path references and aborts the cycle with a leak report if any are found. Reads only `drawer_memory.md` + the task brief; writes only `attempts/cycle_N/`.
- **Judge** — *not a fixed pipeline*. Three selectable signals: (1)
  **Claude-vision rubric** (orchestrator-side, no API; reference-free;
  顿笔/弧度/粗细/proportion/overall, bands 0–2, /10) — the **default
  for strokes**, because the hand-coded stroke GTs are weaker than the
  model's own strokes (`runs/run_2/POSTMORTEM.md`); (2)
  **`tools/judge.py`** composite shape-fidelity `visual_score`
  (Dice+Chamfer+proportion) — trustworthy for **characters** (GTs are
  MakeMeAHanzi standard glyphs), low absolute scores normal
  cross-renderer; (3) **OCR** (RapidOCR) recognizability, characters
  only, weak secondary. Signals are logged separately, never blended.
- **Curator** (main thread) reads judge results + drawer code + ground truths (legitimately, for diagnosis), and edits `drawer_memory.md` plus writes `cycle_summary.md` for the next Teacher.
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

## Phase progression (Teacher decides) + mandatory per-run postmortem

| Phase | What is taught         | GT tool (only if `eval` uses `gt`) |
|-------|------------------------|------------------------------------|
| 1     | Atomic/compound strokes | `tools/make_stroke_gt.py` (hand-coded — *optional aid only*; strokes default to `eval:vision`, no GT) |
| 2     | Simple characters (≈1–4 strokes) | `tools/make_char_gt.py` (graphics.txt — trustworthy) |
| 3     | Complex characters (≈5–18 strokes) | `tools/make_char_gt.py` |

The Teacher picks the character pool per phase by stroke count via
`tools/list_chars.py` (enumerates `draw_character/graphics.txt`;
seeded common-frequency list by default, `--all` for the full band).

Pacing is a **soft, Teacher-judged gate** (no hard pixel threshold —
the old 0.85 stroke gate was removed because the stroke GT is a weak
reference). "Mastered" is judged by the signal the Teacher selected:
strokes → Claude-vision rubric `total ≥ 7/10` (no 0 criterion),
post-reflection; characters → OCR `is_correct` AND rubric `≥ 7/10`
(GT `visual_score` for characters is tracked for *regression* only —
correct cross-renderer chars legitimately score low, run_1: 0.03–0.40).
Don't *skip* learning (depth over breadth) but the gate is the
Teacher's judgement, recorded in `teaching_plan.md`.

**Mandatory per-run postmortem.** Every run folder must contain a
`POSTMORTEM.md` written when the run is frozen: 1–2 paragraphs naming
the core problem that run surfaced and why it motivates the next run
(see `runs/run_1/POSTMORTEM.md`, `runs/run_2/POSTMORTEM.md`).
**Before activating a new run you MUST write the previous run's
POSTMORTEM.** `new_run.sh` warns if the previously-active run lacks
one. The postmortem chain is part of the experimental record.

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
