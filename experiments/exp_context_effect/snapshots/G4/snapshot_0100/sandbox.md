# Sandbox (G4 grid-bank) — free-form persistent notes

Sandbox reset with Phase-2 restart. Persistent free-form memory.

## Carry-over observations (Phase-1 → Phase-2, applies to any GT-supported drawing)

- **Anchor-plan comments before code.** Writing the anchor plan as a
  comment block (each stroke's head/tail cells + fracs + width, plus
  joint class per pivot) before touching primitive calls catches
  mismatches early. Same discipline applies whether the target is a
  standalone stroke, a radical, or a full character.
- **Assert direction invariants immediately after anchor→pixel
  conversion.** One-line asserts (`assert p_hook.x > p_corner.x`,
  `assert p_tip.y < p_flick_start.y`, etc.) turn silent geometry bugs
  into loud failures. Cheap in code, expensive if omitted.
- **Prefer raw belly as Bezier control** unless the shape genuinely
  requires the curve to pass THROUGH the belly point. The
  `2*belly - midpoint` derivation is fragile when belly and chord
  midpoint diverge and can throw the control point off-canvas.

## Bootstrap batch (positions 33-50) — G4 curator diagnosis

**G4 pass rate was 12/18 (67%)** — lowest of all four groups.
Cross-cutting failure patterns from the 6 FAILs (丿, 乚, 厂, 刀, 刂, 儿):

### Pattern 1: MMH-anchor blind trust

MMH stroke-median data is derived from character glyphs, not
standalone radicals. A single-stroke radical (丿, 乚) rendered with
verbatim MMH anchors produces a stroke that occupies only a
sub-region of the 米字格, not the full anti-diagonal / full L that a
radical requires. **Rule**: For single-stroke radicals, OVERRIDE
MMH's stroke-median anchors to span the full 米字格 anti-diagonal or
axis. MMH-verbatim is a sanity floor, not a design target for
standalone radicals.

### Pattern 2: N-class ≠ literal separation (厂, 刀 failure)

The N-class joint spec means "small natural gap ≈15-20 px" — a hair
of visual clearance between two strokes that read as touching in
context. When MMH gives two anchor tuples for an N-class joint and
they happen to be in DIFFERENT CELLS (e.g. TC and TL), the drawer must
NOT interpret this as "strokes are independent." Cell-adjacency in
米字格 space at nearby y_fracs still means "should read as connected."
**Rule**: When implementing N-class, use SHARED-cell placement or
verify pixel distance is ≤ 25 px. If MMH's two anchors put the
strokes visually apart, override to weld or near-weld.

### Pattern 3: Forcing incompatible primitives (刂 failure)

刂's shu_gou was called with head.x ≠ hook_pt.x, which means the body
cannot be straight (shu_gou requires belly.x = head.x for straight
body). The drawer NOTED the incompatibility in code comments then
rendered anyway. TR6 says: if a primitive's assumptions don't fit,
INLINE the recipe or override anchors. Do not force-fit.

### Pattern 4: SELF_CHECK rubber-stamping (all 6 FAILs)

All 6 FAILs had `SELF_CHECK.overall_pass = True`. The self-check habit
has degenerated into a checkbox exercise — the drawer answers the
structural fields (stroke_count_ok, endpoint_mismatches) but writes
`visual_ok=True` without actually comparing PNG to GT.
**Curator recommendation to future drawers**: `visual_ok=True` should
require a specific text observation about what matches GT and what
doesn't. If you can't name 2+ specific visual features that agree
between your PNG and GT, `visual_ok` is False and you should revise.

### Pattern 5: Long primitive chains for simple items

儿's 竖弯钩 used a 5-anchor primitive (head/belly/corner/hook_pt/tip)
which the drawer set inconsistently — corner BC(0.62, 0.82) with
hook_pt BR(0.35, 0.55) had hook_pt geometrically BEFORE the corner in
descent order, breaking the primitive's assumption. For 2-stroke
radicals with one compound stroke, inlining the compound stroke as
2 separate Bezier segments (descent + hook) is often cleaner than
setting 5 anchors for a canned primitive.

### Positive observations from PASSes

- 1画 wrapper radicals (丨→shu, 亅→shu_gou, 乛→heng_gou, 一→heng, 丶→dian)
  are RELIABLE — 5/5 PASS. These are the sweet spot for bank reuse:
  primitive definition matches the radical exactly, only anchors need
  tuning.
- 2-画 radicals with clear component structure (八, 二, 冫, 卜) — 4/4
  PASS. When the two strokes are BOTH single primitives and the joint
  is S (separate) or clear N, the composition is robust.
- 乙 inlined the compound stroke fresh (didn't force any bank
  primitive) — PASSED. Reinforces TR6: when in doubt, inline.
- 匕 and 勹 both used compound primitives (shu_wan_gou, heng_zhe_gou)
  with careful anchor plans — PASSED. Proof-of-concept that
  primitives CAN work for 2-stroke radicals when the drawer respects
  the primitive's internal geometry constraints (which 刂 and 儿 did
  not).

## 亻 (p2_radical_029) — remaining mismatch after revision

Submitted with SELF_CHECK.overall_pass=False. My chord-based N-gap
metric (distance from shu_head to pie CHORD at t=0.48) reported
28.1 px vs the ≤25 px TR10 threshold; visually the 竖 head still sits
just off the 撇 body. Two lessons for future 撇+竖 radicals (亻, 彳,
入-family):
1. The joint metric should use distance to the pie BODY (curved), not
   the chord. The pie bows down-left of the chord, so chord-distance
   overestimates the visible gap. Recomputing against the sampled
   Bezier would give a smaller, honest number.
2. When placing a 竖 head to meet a bowed 撇 body, aim slightly
   BELOW-LEFT of the chord midpoint (into the bow) rather than at the
   chord — that lands on the visible ink.

## 彐 (p2_radical_054) — submitted with post-revision regression

First render was a recognizable 彐 (bracket + 3 horizontals) but the top
横 was too short and the vertical of 横折 didn't descend far enough. In
revising, I moved stroke 3 head to BL(0.35, 0.0) and tail to C(0.90,
0.0) — but BL is row=2 and C is row=1, so the "horizontal" tail sits
100 px higher than the head, rendering as a diagonal.
**Rule for future 横**: BOTH endpoints of a 横 must sit in the same
CELL ROW (TL/TC/TR, or ML/C/MR, or BL/BC/BR). Mixing rows tilts the
stroke by exactly one cell height (100 px on 300 canvas). Same applies
to 竖 needing same CELL COLUMN. Add this to TR8 sanity checks.

## 犭 (p2_radical_062) — submitted with SELF_CHECK.overall_pass=False

3-stroke reverse-dog radical. GT shows two crossing 撇 at top forming
a clear X, plus a 弯 belly curve. Submitted after 2 passes:
- s1×s2 P-cross rendered as 21.6 px near-cross, not a welded intersection.
- s2.mid ⇆ s3.head N-gap rendered at 61.9 px (>>25 px target).

Two structural lessons for future multi-stroke radicals where MMH
declares P near the same cell:
1. **Enforce a P-cross with a shared pixel, not just close anchors.**
   When two 撇 must cross (犭, 反, 犬-family), compute the intersection
   in pixel space and set s1's chord to pass THROUGH s2's chord. Easiest
   pattern: pick a shared point P_cross, then s1 endpoints span P_cross
   with one on each side; same for s2. Anchor tuples alone don't
   guarantee crossing — they only bracket a region.
2. **N-joint on a curved spine needs derived anchor.** When s3's head
   must land ON s2's body mid, compute s2's pixel midpoint FIRST, then
   choose s3's head anchor to match that pixel (via inverse of
   anchor_to_xy: px/100 gives cell col + x_frac). Setting s3.head to a
   static ('C', ..., ...) statically ignores how the curved 撇 s2 bows
   away from its chord midpoint — 25-70 px error is typical.

## B1 batch (positions 51-100) — G4 curator diagnosis

**G4 batch score: 35/50 main PASSes (70%) + 4/6 retry PASSes (67%)** —
solid batch, up from bootstrap's 67% main / 0% retry. Retries in
particular jumped from 0/6 to 4/6, showing errata fixes actually work
when they specify concrete pixel-level surgery (T-weld override, MMH
straight-body override, canonical up-hook recipe).

### TR11 effect measurement (SPECIAL FINDING)

TR11 (added at bootstrap-batch end) requires SELF_CHECK.visual_ok to be
earned by naming two specific visual features that agree between the
rendered PNG and the GT. Cross-tabulated across B1:

**Main-batch (50 items):**
- 23/50 attempts show explicit TR11-style named agreements ("(1) ...
  (2) ...") or equivalent MATCH language in notes.
- Of those 23 TR11-compliant SELF_CHECKs: ~15 PASSed, ~8 FAILed
  (63% pass rate on TR11-compliant items).
- Of the 27 non-TR11-compliant SELF_CHECKs (process notes only, or
  minimal): ~20 PASSed, ~7 FAILed (74% pass rate).
- Counter-intuitive: TR11 compliance did NOT correlate with pass rate
  on the main batch. Naming agreements is a check on epistemic honesty
  but is not by itself predictive of success — the drawer can name
  agreements truthfully and still fail on other axes (layout, joint
  class, proportion).

**Retries (6 items):**
- 0/6 retries have TR11-compliant named-agreements SELF_CHECK. Every
  retry's `notes` field is process-oriented ("Fix applied per errata",
  "Straightened body per errata", etc.) rather than PNG-vs-GT
  agreement-oriented.
- 4/6 retries PASSed anyway. The mechanical fix from errata carried
  them; TR11 was skipped without penalty.
- Both retry FAILs (丿 and 刀) also skipped TR11. All 6 retries had
  `overall_pass=True`. Both retry-fail drawers were SELF-DECEIVED
  (drawer said pass, human said fail) — TR11 would likely have caught
  neither, because 丿's failure was a span problem (not a feature-
  agreement problem) and 刀's failure was a proportion problem
  (welded head landed in the right place per errata, but the horizontal
  crowded out the vertical).

**Interpretation**: TR11 is honest labor and the sandbox rule ("visual_ok
requires 2+ named agreements") should stay in principle_bank as an
anti-rubber-stamp measure. But it is NOT sufficient for pass prediction
— drawers can name true agreements and still miss layout/proportion
failures, and mechanical errata-fixes can pass even when TR11 is
skipped.

### B1 fail patterns (15 main FAILs)

**Pattern A — TR9 under-span**: 冂 kept MMH's tight anchors and
compressed the enclosing radical into the upper half. Same failure
mode as bootstrap 丿; TR9 not applied.

**Pattern B — Wrong stroke decomposition**: 卩 rendered as 3 strokes
instead of MMH's 2. When the drawer's mental decomposition disagrees
with MMH's stroke count, the render is very likely to fail.

**Pattern C — Component-placement error despite T/P joints**: 力, 女
had structurally correct joint classes but placed the welded anchor in
the wrong cell (力 welded on the right of the top-bar instead of the
left; 女 welded pivot low-left instead of upper-mid). The joint is
correct but the WHOLE COMPOSITION is displaced.

**Pattern D — 撇 direction confusion in complex radicals**: 艹 drew the
two "verticals" as diagonals (撇-like), turning the 艹 grass sign into
a broken 井. When MMH says 竖, don't render 撇.

**Pattern E — Long compound stroke fragmented**: 飞's continuous
top-hook-body-tick sweep got broken into stub segments that don't
visually chain. When MMH gives one long compound stroke, inline it as
one variable-width polyline, not two stubs.

**Pattern F — Enclosing radical without enclosing anchors**: 门, 马
scattered their strokes across the canvas with big gaps between the
left wall, top bar, and right wall/hook. TR2 span discipline was not
enforced.

**Pattern G — Horizontal tilted by cell-row mismatch (KNOWN)**: 彐's
stroke 3 had head in row 2, tail in row 1 → 100 px tilt. This is
already documented in the 彐-note above; add to TR8 sanity checks.

### Positive calibration cases (drawer honestly flagged FAIL)

- 彐 (SELF_CHECK.visual_ok=False in notes)
- 犭 (SELF_CHECK.overall_pass=False)

Both drawers noted the specific defect in `sandbox.md` after
submission. This is the RIGHT behavior when the render doesn't come
out — submit, honestly log, and let the errata carry the diagnosis
forward.

### Sandbox rule updates for future batches

1. **TR9 for enclosing/large radicals**: 冂, 门, 马 kind of radicals
   need x_frac 0.05-0.95 AND y_frac 0.05-0.95 to read as enclosing,
   not "compressed shape floating in a corner."
2. **Stroke-count parity**: if MMH stroke_count ≠ your mental count,
   STOP and re-decompose. Bootstrap batch's 儿 failure was partly
   this (5-anchor primitive for a 2-stroke radical → mismatch).
3. **Add to TR8**: assert that BOTH endpoints of a 横 sit in the same
   cell row (rows: T*={0}, M*={1}, B*={2}). Assert same for 竖 sitting
   in one column. Cell-row mismatch = guaranteed diagonal.
4. **Retry drawers can skip TR11 without penalty** IF they follow the
   errata fix literally. Retry-FAIL 丿 shows what happens when the
   drawer soft-interprets the errata (used TC head instead of TR head).
5. **Long compound strokes = one inlined polyline**, not two stubs.
   Applies to 弓, 飞, 马-family, 廴, 辶 — all in this batch.
