# Cycle 1 — 3 tasks

## Phase
1 (1–3 stroke characters, MMH GTs)

## Tasks

### Task 1 — 一 (yī)
- GT PNG: `ground_truths/cycle_1/01_一.png`
- Output PNG: `attempts/cycle_1/01_一.png`
- Output code: `attempts/cycle_1/generated.py` (one file, all 3 tasks)
- Why this task: simplest single-stroke character; establishes the
  brushed-横 primitive.
- Reusable from Success Bank: (none yet — Success Bank is empty)

### Task 2 — 二 (èr)
- GT PNG: `ground_truths/cycle_1/02_二.png`
- Output PNG: `attempts/cycle_1/02_二.png`
- Why this task: two stacked 横 with the bottom one longer; tests
  the same primitive at two scales/positions.
- Reusable from Success Bank: if you mastered 一's 横 first within
  this file, reuse it here.

### Task 3 — 三 (sān)
- GT PNG: `ground_truths/cycle_1/03_三.png`
- Output PNG: `attempts/cycle_1/03_三.png`
- Why this task: three 横, top short / middle short / bottom long.
- Reusable from Success Bank: same primitive as Task 1 / 2.

## Eval

`vision+ocr+gt` (default for characters).

## Self-preview budget

Max 2 internal iterations per task. **Open each attempt PNG and
the corresponding GT PNG and compare them with your own vision** —
the gate is "does my render look unambiguously like the GT
character?", not numeric coordinates.

## Notes from Principle Bank

- §1.0: every brushed stroke uses `brushed_bezier(...)` with
  `pensize(max(3, w(s)))` floor. Hairline-thin (< 3) strokes will
  fail the rubric.
- §2.1: if you write a reusable `draw_heng(t, ox, oy, scale)`
  inside `generated.py`, call it for all three tasks with different
  positions/scales. This is the canonical reuse pattern.
