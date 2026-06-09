# Cycle 4 — 3 tasks

## Phase
1 (continuing — 横+竖 compositions)

## Tasks

### Task 1 — 下 (xià) — CARRY OVER from c3
- GT PNG: `ground_truths/cycle_4/01_下.png`
- Output PNG: `attempts/cycle_4/01_下.png`
- Output code: `attempts/cycle_4/generated.py`
- Why this task: c3 attempt had the 竖 PIERCING above the heng (like 十) — that made the silhouette read as "十 with a dot" and OCR returned 十. Fix per Sandbox: 竖's `oy_top` must sit AT or just below the heng's centerline (NOT above).
- Reusable: `success_bank/code/heng.py`, `success_bank/code/shu.py`. The 点 (right-of-竖) is a small brushed teardrop — see c3's `draw_dian` pattern in `attempts/cycle_3/generated.py` if you can reuse it (it's not in the Success Bank yet).
- Concrete brief: `draw_heng(d, ox=0, oy=+80, length=330, scale=1.0)` for the top heng; `draw_shu(d, ox=0, oy_top=+70, length=240, scale=1.0)` for the 竖 (note oy_top=+70 is 10 below the heng centerline at +80, so the 竖 hangs WITHOUT poking above); 点 at ~(+50, +25).

### Task 2 — 干 (gān)
- GT PNG: `ground_truths/cycle_4/02_干.png`
- Output PNG: `attempts/cycle_4/02_干.png`
- Why this task: 短横 (top) + 长横 (middle) + 竖 piercing through the middle (like 十). 三 strokes total. Tests the "竖 piercing" pattern again with two heng's above the cross.
- Reusable: `draw_heng` × 2 + `draw_shu`. The 竖 crosses through the LOWER heng (not the upper short heng).

### Task 3 — 工 (gōng)
- GT PNG: `ground_truths/cycle_4/03_工.png`
- Output PNG: `attempts/cycle_4/03_工.png`
- Why this task: 横 (top) + 竖 (middle) + 横 (bottom). The 竖 stands BETWEEN the two heng's (top of 竖 sits at the top heng, bottom of 竖 sits at the bottom heng). Different from both 十 (piercing) and 下 (hanging).
- Reusable: `draw_heng` × 2 + `draw_shu`. Key positional: 竖's `oy_top` is at the top heng's y, length is roughly the gap between the two heng's.

## Eval
`vision+ocr+gt`.

## Notes from Principle Bank / Sandbox

- **§1.1 横 width profile** — use `draw_heng`.
- **竖 primitive** — use `draw_shu` (mastered c3). Key choice: where to place `oy_top` depends on the structural relationship between the 竖 and any heng:
  - **下 / 卜**: 竖 hangs FROM the heng → `oy_top` at-or-below the heng's centerline.
  - **十 / 干 / 千**: 竖 pierces THROUGH the heng → `oy_top` 50–100px above.
  - **工**: 竖 spans BETWEEN two hengs → `oy_top` at the top heng, length = vertical gap.
- **§2.1 PIL reuse interface** unchanged.
- The 点 for 下 doesn't exist in the Success Bank yet. You may define it inline.

## Self-preview budget

Max 2 internal iterations per task. Check each PNG against its GT — does the structural relationship (piercing / hanging / spanning) match?
