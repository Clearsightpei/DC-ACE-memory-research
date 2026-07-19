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
