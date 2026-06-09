# Cycle 3 — 3 tasks

## Phase
1 (introduce 竖 stroke + position-relative-to-横)

## Tasks

### Task 1 — 十 (shí)
- GT PNG: `ground_truths/cycle_3/01_十.png`
- Output PNG: `attempts/cycle_3/01_十.png`
- Output code: `attempts/cycle_3/generated.py`
- Why this task: introduces 竖 (vertical stroke) crossing the 横. Stroke order: 横 first, then 竖 over it. The 竖 in 十 typically has a 垂露 (rounded-bottom) finish.
- Reusable: `success_bank/code/heng.py`'s `draw_heng(...)` for the horizontal. You will need to write a new `draw_shu(...)` primitive.

### Task 2 — 上 (shàng)
- GT PNG: `ground_truths/cycle_3/02_上.png`
- Output PNG: `attempts/cycle_3/02_上.png`
- Why this task: 短竖 (short 竖) + 短横 + 长横. The bottom 横 is the long base; the short 横 above it sits on the right of the 竖; the 竖 stands above the long bottom 横.
- Reusable: `draw_heng(...)` × 2 + new `draw_shu(...)` (short version).

### Task 3 — 下 (xià)
- GT PNG: `ground_truths/cycle_3/03_下.png`
- Output PNG: `attempts/cycle_3/03_下.png`
- Why this task: 长横 (top) + 长竖 (below it, centered) + 短点 (right of the 竖). Mirror-companion of 上.
- Reusable: `draw_heng(...)` for the top 横, the new `draw_shu(...)` for the 竖, and a small 点 (dot) drawn as a short brushed disk.

## Eval
`vision+ocr+gt`.

## Notes from Principle Bank

- **§1.1 横 width profile** is established. Use `draw_heng` from the bank.
- **§2.1 PIL reuse interface**: Success Bank entries take `(pil_draw, ox, oy, scale)`.
- **New stroke needed — 竖 (shu)**:
  - **垂露** variant for 十/下 (rounded heavy bottom)
  - Width profile suggestion: entry-press 16 (top) → shaft 11 → bottom-press 18 (rounded 垂露).
  - Length depends on character. For 十 the 竖 is the full vertical extent; for 上 the 竖 is short (~half the canvas height); for 下 the 竖 is mid-length.
- **§1.0 invariant**: `max(3, w(s))` floor; nothing should be hairline.

## Self-preview budget

Max 2 internal iterations per task. **Check each attempt PNG against its GT** — proportions (which strokes are short, which are long), position, and the closing-press on every 横.
