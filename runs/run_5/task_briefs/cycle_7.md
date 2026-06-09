# Cycle 7 — 3 tasks (carry-over of 一/二/三 with thin-variant fix)

## Hard gate
OCR conf > 0.95 AND visual_score > 0.9 AND Claude vision unambiguous. ALL THREE.

## Sandbox finding from c6

Run_4's `heng.py` has width profile 16 → 11 → 19. The MMH GT skeleton is ~pensize 3. Dice/Chamfer/proportion blended visual capped at 0.88 for 一/二/三 because the wide brushwork over-paints the thin skeleton. OCR conf was also marginal (一 at 0.79).

## Tasks — same characters, new render strategy

1. 一 → `attempts/cycle_7/01_一.png` (GT `ground_truths/cycle_7/01_一.png`)
2. 二 → `attempts/cycle_7/02_二.png`
3. 三 → `attempts/cycle_7/03_三.png`

## Approach — thin-stroke variant (NEW Success Bank entry, not a modification)

Create `success_bank/code/heng_thin.py` with `draw(t, ox, oy, scale)` that draws a **THIN** uniform horizontal stroke matching the MMH skeleton thickness:
- Uniform pensize ~3-4 (matches GT)
- Same Bezier centerline as `heng.py` (so position/tilt match)
- No entry-press / closing-press width variation
- Same `(ox, oy, scale)` interface as the brushed `heng.py`

This is a SECOND variant of heng. It does NOT replace the brushed one. Both live in the Success Bank with distinct tags:
- `heng.py` → tag:`brushed` (run_4 c1, for calligraphic renders)
- `heng_thin.py` → tag:`thin-variant` (for matching MMH char GTs at visual > 0.9)

Future characters can pick whichever variant fits their gate.

## Place centerlines to match GTs

Read the GT PNG, measure each stroke band's vertical center (numpy dark<100 row centers worked well in c6). Pass `(ox, oy, scale)` to `heng_thin` for tight centerline alignment.

## Renderer

`turtle.Turtle` + getcanvas().postscript() → PIL save (same pattern as c6).

## Self-preview budget

Max 2 iterations per task. Run the judge mentally: does centerline align with GT? Is the stroke thin enough to avoid Dice penalty?

## Output

Single `attempts/cycle_7/generated.py`. Define `draw_heng_thin(t, ox, oy, scale)` INLINE in this file (do NOT write to the Success Bank — that's the Curator's job). If the renders pass the hard gate, the Curator will promote `draw_heng_thin` to `success_bank/code/heng_thin.py`.

Do not import or modify the existing brushed `heng.py`. The brushed version stays in the Success Bank for compositions where thicker strokes are appropriate.
