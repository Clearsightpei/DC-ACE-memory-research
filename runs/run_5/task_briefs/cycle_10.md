# Cycle 10 — 八 / 人 / 入 (CARRY-OVER from c9)

## c9 failure modes (from Sandbox)

- 八: structure OK (gap visible), but `visual_score=0.46` because position/scale don't match MMH GT. Heavy 撇 dunbi blob too prominent.
- 人: structure OK (shared apex), but OCR returned 入 (confusion class) and visual=0.37 (way off MMH).
- 入: **structural error** — 撇 placed ABOVE 捺's head. In 入, the 撇 must be BELOW the 捺's apex (撇 attaches as a shorter secondary stroke to the 捺's upper section).

## Hard gate (4-component)
- OCR is_correct AND `ocr_margin >= 0.3`
- `visual_score > 0.8`
- Judge panel unanimous YES

## Pre-measured GT bounding boxes (Teacher-side measurement)

Pixel-coord bounding boxes of the dark strokes in each GT:
- 八: x=[231,591] (w=360), y=[228,461] (h=233) → character center ≈ (411, 344) in pixel; in turtle math-coords ≈ (+11, -44)
- 人: x=[224,594] (w=370), y=[212,474] (h=262) → center ≈ (409, 343) → math-coords (+9, -43)
- 入: x=[242,588] (w=346), y=[233,475] (h=242) → center ≈ (415, 354) → math-coords (+15, -54)

(turtle convert: `tx = px - 400`, `ty = 300 - py`.)

So all three characters' overall bounding box is ~360×250 px and centered slightly right-and-down of canvas center.

Canonical run_4 primitives have wider extents:
- pie scale=1: head (+150,+200) → tail (-180,-180) → 330 wide × 380 tall
- na scale=1: head (-150,+200) → kick tip (+240,-172) → 390 wide × 372 tall

At scale 0.6, those become ~200×230 — too narrow. At scale 0.95 they're ~310×360, closer to the 360×250 GT bbox but still tall. **Suggest scale ~0.65–0.75** for the diagonals, with explicit ox/oy to center the character at (+10, -45).

## Tasks

1. **八**: 撇 + 捺 separated. Place 撇 head around (-30, +75), 撇 tail (-150, -150). Place 捺 head around (+50, +70), 捺 tail (+170, -130). Gap of ~80 px between heads. Use pie/na at scale ~0.55-0.65.
2. **人**: 撇 + 捺 sharing apex. Both heads at one point, around (+10, +80). 撇 tail (-150, -170). 捺 tail (+180, -160). Use scale ~0.65-0.75.
3. **入** (the structural-error char): 捺 dominant from upper-left to lower-right. 捺 head at (-20, +90) (or even (-40, +100)), 捺 tail (+200, -150) with kick. 撇 head BELOW the 捺's apex, around (+50, +30). 撇 tail (-100, -130). Use 捺 scale ~0.75, 撇 scale ~0.45 (shorter).

Read each GT carefully and verify your stroke heads land where the GT's stroke heads land.

## Renderer

Same turtle + postscript pattern that worked in c6/c8. No subprocess. `t.reset()` between tasks.

## Self-preview

Open each rendered PNG and the GT. The structural distinction (gap vs shared vs 捺-dominant-撇-below) must be visible. Measure pixel-band positions against the GT and refine within 2 iterations.

## Output

`attempts/cycle_10/generated.py` + 3 PNGs.
