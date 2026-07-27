# Principles — META rules (G3 coord-bank)

*Created 2026-07-18 (v7 self-evolution). Split from the monolithic
`principle_bank.md`. These are meta-cognitive rules about HOW to use
the bank. For stroke-family form knowledge see
`principles_stroke_family.md`. For stroke-in-context lookup see
`form_catalog.md`.*

## BANK IS SUPPLEMENTARY

The Success Bank is a SUPPLEMENTARY resource, not a primary source of
truth. For any character or radical drawing task, ground truth (GT)
and the current brief take priority over bank recipes. Consult the
bank when a primitive shape genuinely matches the target; otherwise
derive coords fresh. Never call a bank primitive without deliberate
placement.

## P-HELPER-SKEPTIC (added 2026-07-24 after B5 falsification)

**When your recommended helper contradicts what you SEE in the GT,
PREFER GT.**

Evidence: B5 retries had 17/17 checklist compliance and 17/17 helper
imports. Only 丷 PASSed — and 丷 PASSed by explicitly REJECTING
`mirror_dian_pair` in its Q3 answer because the GT was asymmetric.
The three X-crossing terminal freezes (人, 入, 大) followed
`kiss_apex` to the letter and failed anyway.

The helpers (`kiss_apex`, `pie_point`, `mirror_dian_pair`,
`variant_*`) are RECOMMENDATIONS grounded in prior PASSes for
similar-looking cases. They are not commands. When the GT for your
current item disagrees with the helper's assumed geometry:

- Say so explicitly in the Q3 answer ("mirror_dian_pair — NO, GT
  is asymmetric").
- Render per GT observation with plain PIL / tapered_line /
  tapered_bezier and thin uniform widths (P12).
- The Curator will not penalize helper-rejection; the Curator
  penalizes GT-disagreement.

Do not mechanically comply with the RETRY-TIME CHECKLIST if the
helpers it recommends don't fit your item.

## TR1. Every primitive call must be deliberate placement, not a default call

Wrong:
```python
from shu import draw_shu
draw_shu(t)  # default position, default scale, hope it fits
```

Right:
```python
from shu import draw_shu
# For 亻: 竖 is right-half, offset right of the 撇, shorter than standalone
draw_shu(t, ox=+18, oy=-8, scale=0.75)
```

Before calling ANY primitive from the bank, decide three numbers:
1. **Where** should its origin land (`ox, oy`)?
2. **How big** should it be relative to its standalone size (`scale`)?
3. **How** should its endpoints meet any adjacent stroke (shared pixels)?

If you can't answer all three, don't call the primitive — inline the
recipe or use an adaptive helper (see `_shared_helpers.variant_*`).

## TR2. Radical-position scaling defaults

Component role → scale (relative to standalone bank default of 1.0):
- **Left/right radical position**: scale = 0.55–0.75
- **Top radical position**: scale = 0.75–0.90 (wider than tall)
- **Bottom radical position**: scale = 0.75–0.90
- **Enclosing radical**: scale = 0.90–1.0
- **Full-standalone**: scale = 1.0

## TR3. Origin (ox, oy) places the stroke's center of mass

`(ox, oy)` in every G3 primitive is the canvas-coord offset from the
primitive's own internal origin (usually its geometric center). To
place a component, compute the target center pixel and subtract the
primitive's default center.

## TR4. When two primitives share a joint pixel, compute it FIRST

For crossings (十: heng and shu through center) use the SAME
`(ox, oy)`. For welds (亻: shu head touches pie tail) compute the
pie's tail pixel at the chosen scale, then set shu's `(ox, oy)` so
its head lands within 3 px. **Compute the pixel explicitly in
comments before the render call.**

## TR5. If a primitive doesn't have the right transform, INLINE — do
## not stretch with extreme (ox, oy) or scale

Signs to inline instead of reuse:
- `scale < 0.4`
- Endpoint anchors of the transformed primitive would fall outside
  their bank-tuned expected cells
- The component needs different width taper than the standalone
  primitive provides
- Non-uniform aspect ratio needed (e.g. 日 is 1:2, kou is 1:1)
- Mirror reflection needed (dian primitive is one-directional)

When inlining, prefer the **adaptive helpers** in
`success_bank/code/_shared_helpers.py` (`variant_pie`, `variant_na`,
`variant_dian`) — they give you angle/taper/width knobs without a
fresh from-scratch bezier every time.

## TR6. Record the transform in a comment before every primitive call

Comments force explicit derivation and give the Curator diagnostic
signal on FAIL (which transform was wrong).

## TR7. Eyeball sanity check before render

Before running `python3 generated.py`, mentally simulate:
1. Where does each stroke start and end in canvas pixels?
2. Do any two strokes that SHOULD meet share a pixel (weld) or land
   within their expected small gap (~10-15 px)?
3. Does the composition fit within the 300×300 canvas with ~10 px
   margin on all sides?

If any answer is uncertain, adjust before rendering.

## RETIRED RULES (documented so we can measure their absence)

- **TR8 INLINE-FRESH TEST** (retired 2026-07-18 in v7 evolution).
  Added at end of B1 to save 大/人/入-family fails. In B2 drawers
  complied but the pass rate DROPPED (54% → 34%). Root cause was
  deeper: `(ox, oy, scale)` signature can't vary angle/taper/curve.
  Replaced by adaptive helpers + `form_catalog.md` (which name the
  variant to use per context).
- **TR9 bank-size discipline** (retired 2026-07-18 in v7 evolution).
  Never fired usefully — never rescued a fail. Removed as noise.

If any future batch shows drawers reflexively force-fitting again
without checking form, re-introduce a leaner form-focused version.
