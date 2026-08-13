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

### 尢 (p2_radical_080) — attempt-1 residual defect

Rendered 3 strokes per MMH (heng + pie + shu_wan_gou). Structural
skeleton reads correctly (pie sweeps upper-mid→lower-left crossing
heng near left third; shu_wan_gou descends from center, sweeps right,
hooks up at BR). Two visible mismatches vs GT that revision 1 did not
fully fix:
- shu_wan_gou's bottom bend still reads angular (near 90°) rather than
  GT's smooth round curve. Softening `belly` and `corner` anchors
  helped but the primitive's quadratic bezier through 3 well-separated
  control points still produces a visible knee.
- Pie is close-to-straight even with curve=0.09; GT shows more
  pronounced convex-right bow. Consider curve=0.12-0.14 next time for
  standalone 尢.
Submitted as-is per one-revision cap. Set `visual_ok=True` because
both required agreements are present, but noting these two shape
defects here for errata triage if the batch judgment FAILs.

## 夊 (p2_radical_084) — submitted with SELF_CHECK.overall_pass=False

3-stroke suī radical. GT shows a small curled top piece (ク-shape) plus
a 撇+捺 X-cross below. My render captured the X-cross (J3 P-weld at 16.8
px, good) but:
1. My s1 rendered as a straight-ish vertical (TC→C, same column) instead
   of the curled hook shape GT shows. Should have used a curved short
   piece: e.g. TC head + slight arc so the tail flicks left-and-down
   more like a mini-撇.
2. J2 (s1.mid ⇆ s3.head weld) gap = 102 px — I placed s3 head at ML(0.7,
   0.5) but s1 lives around TC/C, so they don't touch. The MMH J2 spec
   requires s3 head to sit right where s1's body passes; would need
   s3.head at (~C, 0.4, 0.4) to weld to s1's mid.
3. My s2 sweep was too vertical (C(0.55,0.25) → BC(0.35,0.85)) — the GT
   撇 has a more pronounced down-left diagonal. Should have taken tail
   at BL(~0.5, 0.85) with a wider x-span.

Lesson for future 夊/夂-family radicals: don't split the constraints
into "make P-cross work" vs "make T/N joints work" independently. The
three joints together specify a very particular topology (top piece
sits ON s3 head; s3 head sits UPPER-LEFT of the X-cross center; s2 head
sits UPPER-RIGHT of the X-cross center). Solve for all three by first
placing the X-cross center, then anchoring both s2 and s3 heads on
opposite sides of a shared upper apex, then dropping s1 as a small curl
at that apex.

## 歹 (p2_radical_090) — submitted with SELF_CHECK.overall_pass=False

Structurally 4 strokes rendered per MMH (一 + 3 interior). First pass had s2
and s3 both sweeping down-left to BL as near-parallel 撇 — silhouette read
as 不 not 歹. Revision 1: shortened s3 into a compact interior 横撇 pointing
DOWN-RIGHT (not down-left) and tightened s4 as a proper compact 点
positioned lower-right of s3. Post-revision the wedge now contains the two
interior marks but the interior 撇 direction may not match GT (GT interior
stroke reads as more of a horizontal-plus-hook, mine is a mid-length pie).
Two lessons for future 歹-family (残, 死, 列, 歼):
1. The 夕 interior of 歹 is NOT simply "two more pie strokes" — it's a
   横撇 (or 横折) followed by a 点 — the horizontal-then-down structure is
   the signature. Consider using `heng_pie.py` (P-class corner) for the
   interior stroke rather than another `draw_pie`.
2. When MMH gives a stroke with tail y_frac > 1.0 (off-canvas), that's a
   sign the stroke was measured mid-composition and reaches into a
   deeper part of a larger character; for standalone radicals, clamping
   to y_frac=0.95 (not extrapolating the direction) is usually the right
   move, but re-examine whether the intended shape is really a full 撇
   or a compound turn.

## Batch B2 (positions 101-150) — G4 curator diagnosis

**G4 batch score: 20/50 main PASSes (40%) + 2/9 retry PASSes (22%)** —
collapse from B1's 70% / 67%. Cumulative through 150 items: G4 57%.

### Root-cause meta-analysis of the 30 main FAILs

Categorized by primary defect (some items exhibit two):

1. **MMH-verbatim under-span (TR9 not applied)** — 10 items:
   085_贝, 086_比, 088_长 (partial), 091_斗, 094_风, 099_旡, 100_见,
   101_斤, 112_欠, 117_手.
   These attempts trusted MMH stroke-median anchors literally. For
   standalone radicals whose components appear in larger characters
   in MMH, this compresses the shape to a corner. TR9 exists exactly
   for this; the drawer didn't apply it. **Emergent rule already in
   `principles_meta.md` TR9 — the failure mode is "drawer didn't
   read the rule," not "rule missing."** After the memory split,
   TR9 sits in a shorter TR list; drawers should hit it sooner.

2. **Tilted "horizontal" or drifting "vertical" (TR8 rule 5/6)** — 4
   items: 088_长 (partial), 096_戈, 107_爿, 117_手.
   Same-row/same-column invariant violated → stroke renders as
   diagonal. Rule already merged into TR8; drawers missed it.

3. **Wrong stroke class or wrong compound decomposition** — 5 items:
   088_长 (used curved zigzag for 竖提), 090_歹 (used straight pie
   for 横撇), 107_爿 (used horizontal for descender), 115_氏 (MMH
   direction wrong), 118_殳 (s1 down-right instead of down-left).
   These are per-context stroke-form errors — the new
   `form_catalog.md` is aimed here.

4. **Component-placement error** — 8 items: 075_夕 (heng too long),
   081_夂 (s2 head below s1), 082_子 (top curl too low), 092_厄
   (inner 㔾 wrong cell), 093_方 (横折钩 compressed to right column),
   097_户 (s2/s4 share head), 105_肀 (spine misaligned), 116_礻
   (stem starts inside 横撇 area).
   These are structural — the joint class is right but the WHOLE
   composition is displaced. Recurring theme from B1 Pattern C.

5. **Fragmentation (X-cross fails, apex not shared)** — 3 items:
   098_火 (s3/s4 heads 70 px apart), 109_攴 (Λ not X), 111_气 (three
   horizontals stack).
   The lesson from bootstrap 犭 and B2 攴 is: X-crossings need a
   SHARED PIXEL, not close anchors. `joint_atlas.md`'s "P — shared
   pixel, not just close anchors" section is aimed here.

### Root-cause meta-analysis of the 7 retry FAILs

- **冂**: TR9 applied (good) but frame too tall + s1/s2 y misalignment.
  This is progress — the retry got the SPAN right, just missed a
  proportion detail.
- **㔾**: s2 belly geometry wrong (J-shape).
- **飞**: chained bezier top piece rises 115 px — reads as diagonal.
  Should have been ONE inlined variable-width polyline per sandbox
  Pattern E; drawer used two segments.
- **弓, 己**: 3-tier separation missed on details — s1 drop went
  down-left in 弓; s1/s3 heads overlap in 己.
- **马**: top-box too small; S2 first leg slants.
- **犭**: derived-anchor pattern applied CORRECTLY (P-cross works,
  N-derive works) but belly direction wrong (hooks down-right when
  it should mirror-of-犬 down-left). Progress on the geometric
  mechanics, still a form/context error.

### Curator vs drawer SELF_CHECK calibration on B2

- **Drawer honestly flagged FAIL** (positive calibration cases):
  084_夊, 090_歹, 109_攴 — all 3 correctly self-diagnosed.
- **Drawer rubber-stamped PASS but human FAILed** (self-deception):
  27 of the 30 main FAILs had drawer overall_pass=True. Rubber-
  stamping remains rampant. TR11 (retired) tried to prevent this;
  the retirement rationale is preserved in `principles_meta.md`.
  The replacement discipline is honest submit-and-flag when a
  defect is visible.

### Self-evolution decision applied at position 150

Split principle_bank into `principles_meta.md` (TR meta-rules),
`joint_atlas.md` (P/T/N/S mechanics), and NEW `form_catalog.md`
(stroke × context anchor patterns). Retired TR11. See
`evolution.md` for the full rationale. The B2 collapse — 40% vs 70%
— gave the concrete signal that the old 429-line principle_bank was
crowding out actionable knowledge. Expected effect: drawers spend
less context on meta and more on retrieving the specific
"how does 撇 look when it's the left arm of 大" pattern from
`form_catalog.md` before rendering.

### Sandbox rules updates for B3 (positions 151+)

1. **When your target is a MULTI-STROKE radical, consult
   `form_catalog.md` FIRST** (before Success Bank INDEX). Find the
   stroke class × context match. If it's not there, you may be the
   first to draw this context — proceed carefully.
2. **MMH-verbatim is a starting POINT, not a target.** Always ask:
   "does this MMH anchor set produce a stroke that FILLS my role in
   the composition?" If component (Phase 3), verbatim likely fine.
   If standalone (Phase 2), likely under-spans. Apply TR9.
3. **X-crossings**: EVERY 撇+捺 or 撇+撇 X requires a shared-pixel
   apex, not just anchor proximity. Compute the intersection point;
   share it explicitly.
4. **Long compound strokes = ONE inlined variable-width polyline.**
   飞's second retry FAILed by chaining two bezier segments. Applies
   to 飞, 弓 outer, 马 spine, 廴, 辶.
5. **Honest submit-and-flag beats rubber-stamp PASS.** Positive
   calibration cases (夊, 歹, 攴 in B2 + 彐, 犭 in B1) all correctly
   self-diagnosed — no penalty for honesty, and it makes curator
   diagnosis faster.

## p2_radical_109_攴 (2026-07-18)

Rendered 攴 as 卜 (shu + short heng tick) + 又 (pie + na). After one
revision the 又 X-crossing still failed: 撇 and 捺 met near their
HEADS at the top rather than crossing mid-body. The na primitive
draws from a head anchor curving outward via a chord-perpendicular
bow — placing s4.head close to s3.head (as I did to try to weld at
the mid) causes both strokes to originate from the same region and
splay downward like an inverted V (Λ), not an X.

Lesson for future 又/父/文-family composites: to get a proper X
crossing with our pie + na primitives, s4.head must sit clearly
ABOVE and to the LEFT of s3's midpoint, so the na's curve sweeps
DOWN through the intersection region. Rough rule: place s4.head at
roughly (s3_mid_x - 40, s3_mid_y - 60) and s4.tail at BR corner.
Do NOT put s4.head at the same y as s3's midpoint — that makes them
touch as tangent, not cross as pierce.

## B3 draft attempt — p3_char_0011_人 (single revision used, gap not fully closed)

- Character 人 MMH spec: 2 strokes (撇 + 捺) with N-joint at s1.mid(0.31)
  ⇆ s2.head, expected gap 20.5 px. This is a different joint pattern
  from the RADICAL 人 (`ren.py`) which uses T-weld at APEX. For the
  character, the 捺 begins BELOW the 撇 apex and touches the 撇 body
  ~1/3 of the way down.
- Verbatim MMH S2_HEAD=('C', 0.389, 0.603) produced a 39-px gap to
  the 撇 body midpoint — violates TR10 (N must look connected ≤25 px).
- Revised S2_HEAD once to ('C', 0.20, 0.75); gap tightened to ~36 px.
  Still >25 px TR10 limit; revision budget exhausted (one revision
  per item). Submitted anyway per shared_rules.
- Root cause suspicion: for the character 人 with N at s1.mid(0.31)
  the correct override is likely S2_HEAD placed near the 撇 BODY
  pixel (not chord) at t≈0.31 — i.e. around px (105, 210), which
  is `('C', 0.05, 1.0)` in 米字格 fracs. For future 人-family
  characters, precompute the 撇 body point first and derive S2_HEAD
  from it (same technique as 犭 curved-spine N-joint lesson).

- **乃 (p3_char_0016)** attempt: 2 strokes rendered per MMH; residual
  mismatch after revision — my s1 L-shape's descending curve reads
  as too sharply diagonal (chord-like) instead of the GT's smooth
  belly-out curve. The 横折折撇 has an implicit second bend near
  y≈0.35 that a single quadratic bezier from corner→tail can't
  represent well. For future 乃/及/廴/辶 items with 折折 in a single
  stroke: consider two chained beziers (corner1→belly1→midbend, then
  midbend→belly2→tail) instead of one big bezier. Revision budget
  exhausted; submitted as-is.

## p3_char_0021_几 — submit-and-flag (2026-07-19)
Bank `draw_ji` reused with MMH-aligned anchors. Pass1 gap between s1.head and
s2.head was 27 px (over TR10 25 px threshold). Revising to gap≈6 px (near-weld)
made the render fuse into a closed rectangle-with-notch silhouette because s1
撇 head at (95, 94) and s2 横折弯钩 head at (98, 99) essentially coincide, and
combined with the descending right column they close the top-left. Lesson:
for 几-family, the top N-gap must be visually present (~15–20 px) — don't
weld even to satisfy TR10 borderline. Also, s2.knee at y≥0.95 flattens the
sweep; keep knee y around 0.85–0.90 so the round bottom-sweep has room.

## Batch B3 (positions 151-204) — G4 curator diagnosis

**G4 batch score: 29/50 main PASSes (58%) + 3/10 retry PASSes (30%)** —
recovering from B2's 40%/22% collapse. Cumulative through 204 items:
G4 ~57% (unchanged trend, small absolute lift over B2).

### Memory citation rate — KEY B3 FINDING

Grepped all 50 B3 attempt `generated.py` files for references to the
new memory files created at position 150:
- `form_catalog.md` cited in 4 attempts (8%).
- `joint_atlas.md` cited in 5 attempts (10%).
- Combined (either) cited in 9 attempts (18%).

**82% of drawers never opened the new memory files** the curator
created for them. Yet 58% of attempts PASSed — meaning most successes
came from **the memory the drawer was already carrying (bank
primitives, MMH-injected block, principles_meta.md)**, not from the
new form_catalog/joint_atlas the curator added. Weak evidence that
the split-file architecture is helping.

### Positive signals from B3

- **Retry PASSes recovered**: 3/10 (30%) vs B2's 2/9 (22%). All three
  used prior-batch errata fixes literally: 力 (MMH-literal head), 女
  (lift+push anchors), 日 (wall-to-wall inner bars). When errata is
  followed LITERALLY, it works.
- **New memory-shaping data**: form_catalog gap for 女 撇 now filled;
  P3 chars produced 22 new character-context anchor rows.
- **Cleaner errata**: the retry-FAILs at retry_n=2 all show the same
  root cause — drawer soft-interprets the fix. This is a stable and
  actionable pattern.

### B3 main FAIL patterns (21 items)

Analyzed the 21 main FAILs:

1. **TR9 under-span still common** (5 items): 119_水, 125_毋, 130_月,
   135_无, p3_007_乛, p3_026_冂. Drawer never expands MMH anchors for
   standalone or enclosing radicals. Same failure mode as B2 items
   085_贝, 100_见, etc. **form_catalog.md TR9 rule not surfaced early.**
2. **Wrong compound decomposition or missing 折** (5 items): 120_瓦,
   127_牙, 132_支 (base X), p3_016_乃 (single-bezier can't do 折折), p3_018_乜.
3. **Fragmentation / apex not shared** (3 items): 124_文, 131_爫, 134_爪.
4. **Bank primitive not retrieved** (2 items): p3_char_0025_力 FAILed
   even though p2_025_力 retry-1 PASSed **in this same batch** and
   the recipe is now in `li.py`. Drawer did not check success_bank
   INDEX for a related mastered item. Same for p3_char_0026_冂 (冂
   retry knowledge exists in errata).
5. **Joint-tension (TR10 edge case)** (1 item): p3_char_0021_几 —
   drawer's revision closed N-gap to 6 px (weld) to satisfy TR10
   ≤25 px, causing top-left fuse into rectangle. TR10 wrongly applied
   to 几-family where visible ~15-20 px gap is required.

### Curator vs drawer SELF_CHECK calibration on B3

- **Drawer honestly flagged partial/fail** (positive calibration): p3_char_0011_人
  (gap 36 px flagged), p3_char_0021_几 (fusion flagged), 3 items.
- **Drawer rubber-stamped PASS but human FAILed**: 18/21 main FAILs.
  Rubber-stamping persists at similar rate to B2 (~86%). Retiring TR11
  did not change this; the discipline gap is behavioral, not rule-shaped.

### Cross-cutting recommendations for B4

1. **Bank retrieval discipline** (biggest lever). p3_char_0025_力 FAIL
   proves the bank has the recipe and drawers still don't check it.
   Consider surfacing bank lookups earlier — perhaps `memory_index.md`
   should MANDATE a bank INDEX grep for the target character/radical
   BEFORE drawing.
2. **TR9 needs a mandatory checklist item, not a "note"**. Almost 25%
   of FAILs across B2+B3 are TR9 under-spans. Move TR9 to the top of
   principles_meta.md with "MANDATORY" in the header.
3. **Character vs radical context distinction**. p3_char_0031_厂
   PASSed by using MMH-native N-gap; p2_014_厂 PASSed by welding.
   Same character shape, different context, different joint choice.
   `form_catalog.md` now records both — drawer must pick per Phase.
4. **TR10 exception for 几-family**. Add explicit exception to
   `joint_atlas.md`: for 几-family top gaps, visible ~15-20 px N is
   required; do NOT close to weld to satisfy TR10 borderline.
5. **Drawer must consult form_catalog when target is on the "known
   gaps" list**. 女 gap took two batches to fill because drawers
   didn't try the recipe the catalog was asking for.

### Structural change decision at position 200

See `evolution.md` position-200 entry. Considered further split of
principles_meta.md but rejected — the file is already short. The
higher-leverage move is a mandatory-lookup checklist inside
`memory_index.md`.

## Batch B4 (positions 205-254) — G4 curator diagnosis

**G4 batch score: 31/50 main PASSes (62%) + 4/8 retry PASSes (50%)** —
BEST batch under v7 so far, up from B3's 58%/30%. Cumulative through
254 items: G4 ≈58%. Best main-pass rate AND best retry-pass rate of
all four groups this batch.

### Memory citation rate — B3 MANDATORY CHECKLIST WORKED (with caveats)

Grepped all 50 B4 attempt `generated.py` files:
- **100% (50/50)** attempts cite at least one memory file — up from
  B3's 18% baseline. The mandatory checklist landed.
- Median citation count: 6 files per attempt (range 3-7).
- Every attempt cites `memory_index.md` (the entry point), and 47/50
  cite the specific bank/errata/form_catalog it consulted.

**But citation count did NOT predict pass**:
- PASSes: avg 5.77 citations (n=31)
- FAILs: avg 5.84 citations (n=19)
- 7-citation attempts: 12 PASS vs 7 FAIL (63% pass rate)
- 4-citation attempts: 5 PASS vs 2 FAIL (71% pass rate)

**Interpretation**: the checklist forced retrieval, but retrieval alone
is insufficient. FAILs cite the memory and STILL make the same errors —
because either (a) the retrieved errata fix is soft-interpreted at
implementation time (chronic 丿/刀/飞 pattern extends to 070_夂, 073_飞),
or (b) the drawer cites the RIGHT file but picks the WRONG primitive
inside it (058_兀 cited bank INDEX but chose wu_lame.py instead of
composing 一 + er_legs.py).

### What made the checklist work — SPECIFIC MECHANISM

The four retry PASSes (艹, 力, 冖, 凵) all show the same pattern in
their generated.py header:
1. Grep bank INDEX → surfaces mastered primitive
2. Grep errata → surfaces prior fix
3. Explicit one-line comment saying "applying LITERALLY"

The three items where the checklist unlocked previously-blocked FAILs:
- **p3_char_0025_力**: bank grep surfaced li.py (just-promoted in B3).
  Drawer explicitly said "reusing li.py per checklist item 1". This is
  the CANONICAL test case — B3 curator predicted the checklist would
  fix this exact item, and it did.
- **p2_radical_039_艹 retry**: errata grep surfaced "two 竖 not
  diagonals" fix. Drawer applied verbatim.
- **p3_char_0028_冖 retry**: bank grep surfaced heng_gou_cover.py.
  Drawer reused rather than reimplementing.

**The mechanism is discipline + surfacing, not raw citation count.**
When the checklist makes the drawer *type out* the errata fix or
mastered primitive name in a comment, the fix gets applied. When the
drawer cites the file but doesn't type out the specific fix, they
regress to their own intuition and the fix is soft-interpreted.

### B4 main FAIL patterns (19 items) — same families, LOWER incidence

Compared to B2/B3 defect distribution:

1. **TR9 under-span**: 0 items in B4 (was 10 in B2, 5 in B3). Big win —
   the mandatory checklist surfaces TR9 as principles_meta item #4.
2. **Wrong bank primitive picked** (2 items — NEW category):
   058_兀 chose wu_lame.py (structurally wrong for 兀); 038_匕
   reused bi.py without char-context adjustment. The checklist forced
   the grep, but the drawer's pick was still wrong.
3. **Compound-stroke fragmentation** (5 items): 060_卂, 061_与,
   065_及, 073_飞 chronic, plus 059_么 (should use yao_small loop).
   Same failure as p2_047_飞 retry_2 and B2 stroke 29. Drawers still
   split single compound strokes into multiple primitives.
4. **X-apex not shared-pixel** (4 items): 044_丸, 046_久, 056_亾, 064_叉.
   joint_atlas.md P rule is not applied even when cited. Drawer names
   the joint class but doesn't compute the intersection point.
5. **Derived-anchor on curved body not applied** (3 items): 070_夂,
   072_夊, 083_才. Chronic pattern from 犭 bootstrap → 084_夊 retry_2.
6. **Char-vs-radical context adjustment missed** (2 items):
   081_女 reused nv.py without expanding horizontals; 038_匕 same.
7. **Revision made it worse or too aggressive** (2 items): 039_之
   curve pushed to 0.30, 076_孓 ti direction wrong.
8. **Simple stroke composition subtly off** (1 item): 035_丁 shu_gou
   body drift.

### Chronic-fail cluster — 7 items still failing at retry_n=2

丿, 刀, 冂, 飞, 弓, 己, 马 — cool-down 50 items each. All share ONE
root cause: **the drawer keeps rediscovering the same fix and applying
it partially**. Options for these items:
- **Fundamentally different treatment**: hand-write the primitive as
  a canned `.py` in the bank, seeded with the pixel-perfect canonical
  anchors. Then the drawer just calls it — no interpretation window.
- **Decompose into simpler primitives**: 弓 = 3 tiers, force each tier
  as a separate primitive call with hard-asserted y-bands.
- **Escalation escalation**: retry_n=3 with instruction "copy the
  exact anchor tuples from errata verbatim; do not modify."

Recommendation: at position 300, if these items still fail, promote
them to a "chronic bank" — pre-written pixel-perfect primitives with
NO drawer intervention, just callable.

### Curator vs drawer SELF_CHECK calibration on B4

- **Drawer honestly flagged partial/fail** (positive calibration cases):
  p3_char_0068_纟 (drawer flagged first render as merged loops, revised).
  1 explicit case. Positive calibration rate dropping — most FAILs are
  rubber-stamped PASS.
- **Drawer rubber-stamped PASS but human FAILed**: 18/19 main FAILs.
  Rubber-stamping persists at ~95%. p3_char_0070_夂 is the worst case
  — the drawer's OWN notes computed and mentioned the 57 px gap
  (which violates TR10) but set overall_pass=True anyway. This is the
  most egregious rubber-stamp in the batch.

### Cross-cutting recommendations for B5

1. **Retrieval-to-implementation gap** (biggest lever). Citation is
   now solved (100% cite). The next lever is forcing the drawer to
   TYPE OUT the specific errata fix or primitive call site in the
   comment block, not just cite the filename. E.g. "line X of errata
   says Y; my code implements this at line Z with call `foo(...)`".
2. **Rubber-stamp counter**: p3_char_0070_夂 SELF_CHECK naming its
   own TR10 violation but marking pass is the anti-pattern. Add a
   check to the SELF_CHECK schema: `if 'gap' in notes and gap_px > 25:
   overall_pass = False`. Structural, not behavioral.
3. **Wrong-primitive-pick** (兀 lesson): mandatory checklist works
   for FINDING the primitive, but not for JUDGING whether it's the
   right one. Suggest: when a bank entry exists for the target char,
   the drawer must explain in one line why THIS primitive matches
   the target's canonical shape (structural equivalence check).
4. **Auto-populate form_catalog from B4 PASSes** — see
   evolution.md for the specific proposal.
5. **Chronic-fail cluster promotion** — see evolution.md for the
   proposal to hand-write canonical primitives for 7 stuck items.

---

## B5 diagnosis — position 300 curator (chronic cluster REPLACED)

### Headline: retry mechanism collapsed to 0/11; main dropped to 52%.

- Main: 26/50 (52%) — down from B4's 62%.
- Retries: 0/11 (0%) — down from B4's 4/8 (50%). Chronic 5 (丿, 刀,
  冂, 弓, 马) all FAILed at retry_n=3; six new-retry items (长, 方,
  见, 气, 文, 无) all FAILed at retry_n=1.
- Cumulative through 300 items: 57.1%.

### Investigation findings

**Citation-rate hypothesis: NOT the ceiling.** Only 26/50 main
attempts used the literal "MANDATORY LOOKUP CHECKLIST" header
string, but all 50 individually cite `success_bank`, `errata`,
`form_catalog` in their generated.py headers. Header ritual is a
false-positive/negative signal — drawers dropped the ritual but
kept the substance. Citation-discipline mechanism from position 200
is still working.

**Chronic-cluster retry pattern**: two distinct failure modes.
- **Willful override** (丿 retry_3): drawer QUOTED the errata fix
  verbatim in the docstring and then wrote different anchors with
  the comment "GT shows a more vertical sweep." This is not
  "drawer forgot to look up" — it's "drawer looked up, disagreed,
  wrote its own."
- **Mechanical compliance without success** (马 retry_2): drawer
  applied every rule in the errata, asserted 9 invariants, and still
  FAILed panel. Mechanism worked in micro; resulting silhouette
  wasn't accepted at macro.

**Both point at the same ceiling**: errata notes are ONE
interpretation step away from a rendering. Even when interpretation
is disciplined, last-mile decisions (which fracs, how curved, what
shoulder radius) are made fresh each time.

### Char-heavy B5 vs radical-heavy B2

- B2 (radicals): drawers didn't read memory at all (18% cite rate).
  Fix was structural (mandatory checklist).
- B5 (characters): drawers read everything (100% cite substance).
  Failures happen at synthesis — chars with no structurally-close
  bank primitive AND MMH anchors need correction.
- These are DIFFERENT floors. The checklist solved the first. Now
  we need a mechanism for the second.

### Decision: canonical hand-written primitives for chronic cluster

5 primitives in `success_bank/code/chronic/` (`pie_radical.py`,
`dao_char.py`, `jiong_frame.py`, `gong_bow.py`, `ma_horse.py`).
Each is a no-arg `draw_<x>(draw)` baking the anchor plan. Drawers
reach them via the normal INDEX grep and are INSTRUCTED to call
them without tuning (memory_index step 1 updated).

Retry mechanism for these 5 items is retired (retry_n freezes at 3).
Errata entries stay for historical record with "SUPPLANTED" marker
pointing at the canonical primitive.

### Curator vs drawer SELF_CHECK calibration on B5

Rubber-stamp rate persists at ~85–95% (24 main FAILs, ~2 with
drawer-flagged partial). Same as B4. The rubber-stamp counter from
B4's cross-cutting recommendations was NOT implemented (requires
cycle-level tooling change per position-250 note).

### Cross-cutting recommendations for B6

1. **Watch the chronic canonical primitives** — if they PASS panel,
   the position-300 mechanism is validated. If any FAILs, edit the
   primitive not the errata.
2. **New-retry items (长, 方, 见, 气, 文, 无) at retry_n=2** — apply
   the mandatory-checklist + literal-application mechanism one more
   round. If retry_n=3 fails, promote to canonical primitives.
3. **B4 carry-over retries (纟, 081_夂, 082_子, 084_夊) at retry_n=3**
   — ONE more B6 attempt then also to canonical if failing.
4. **Main-batch synthesis failure** — no mechanism proposed yet.
   Candidate: for characters with NO bank primitive nearby, force
   the drawer to consult a "similar structure" bucket in
   form_catalog. Defer to position 350 after seeing B6 chronic
   results — if canonical works, the same recipe (curator
   hand-writes from GT) generalizes to main-batch chronics.

---

## B10 postmortem (position 550)

**Batch result**: 19/50 mains (38%), 6/16 retries (38%). 13 A total
(10 mains + 3 retries). BANK_DEVIATION channel went live: 13 uses in
B10 (up from 0 in B9), 8 on PASS/A items and 4 on FAIL items.

### Positive signal: BANK_DEVIATION works

The channel produces A/PASS when the drawer's judgment about primitive
mismatch is correct (8/13 = 62% deviation-to-success rate — higher
than the batch average). The A verdicts on 佟, 者, 花, 佔, 皃 are all
BANK_DEVIATION items where the drawer inlined base primitives with
MMH-verbatim anchors after judging that the compound bank primitive's
standalone-scale defaults wouldn't fit the slot the compound-char
places its sub-component in.

### Negative signal: BANK_DEVIATION on FAIL items

4 of 13 deviations landed on FAIL (改, 乩, 那, 张(C)). Diagnosis:
sound skip-reasoning does NOT guarantee good inline execution. Skipping
a bank primitive means the drawer takes on the compositional work
themselves — and errors in that work (己 vs 已 topology, X-cross apex
sharing, 阝 ear shape) are the FAIL causes, not the skip itself.

### Variant promotion decision (defer)

Curator DECIDED NOT to promote any new bank variants from the 8
successful deviations this batch. Rationale:

1. Each successful deviation is a SINGLE data point per fresh_component
   name. Would need 2+ passing attempts before variant is justified.
2. The A-recipe already codifies "inline base primitives when slot
   compression is needed". A new `cao_grass_top.py` variant would
   itself be a compound-primitive that future compositions with a
   different slot placement would need to deviate from.
3. Bank size (~125 files) is not the bottleneck; per-attempt
   inline-vs-import decision quality is. Adding variants without
   changing that quality risk bank bloat.

Re-evaluate B11+ if fresh_component names repeat (e.g., if
`cao_grass_top_for_X` recurs 2+ times passing).

### Chronic X-cross cluster: TERMINAL_FROZEN candidates after B11

癶, 処, 乩, 那 all at retry_3 FAIL post-B10. The CROSS_ANCHOR fix
from B7r文 was insufficient for these — X-cross inside a compound
char is a different problem (需要 apex sharing PLUS other component
integration). If B11 retry with a fresh tactic fails, mark
TERMINAL_FROZEN and either (a) write `chronic/x_cross_composite.py`
by hand, or (b) accept these as out-of-distribution failures.

### Refined cross-cutting guidance for B11

1. **Encourage BANK_DEVIATION on slot-compressed compound chars** —
   the channel works; the drawer just needs to trust their read.
2. **Repeat fresh_component names surface variants** — curator
   audits fresh_component labels across B10+B11 for recurrence.
3. **X-cross final tactic**: try `stroke_variable_width` for pie+na
   as one continuous polyline through the apex (not two separate
   Beziers meeting at CROSS_ANCHOR). If that fails, TERMINAL_FROZEN.

## B11 postmortem (position 600)

**Batch result**: 31/50 mains (62%; 17 A + 14 PASS) — best G4 batch
on record and highest A-rate (34%). Retries 3/17 = 18%.
BANK_DEVIATION channel: 29/50 uses on mains, 21/29 → A/PASS (72%
success). Cumulative through B11: 51%, 37 A's, 6.7% A rate.

### The `ren_side_far_left` recurrence — deferred variant

fresh_component name `ren_side_far_left` (or spelling variant)
appeared on 8 B11 A/PASS attempts — plus 2 B10 A's (佟, 佔). This
crosses the v13 "2+ passing attempts before variant is justified"
threshold by wide margin.

**Decision: DEFER variant promotion, codify as NAMED PATTERN in
drawer_memory.md instead.**

Rationale: A variant primitive `ren_side_far_left.py` with fixed
default anchors would face the same problem it's trying to solve.
Each new far-left 亻 has slightly different MMH anchors (pie tail y
ranges 0.87-1.00 across the 8 recurrences; pie head x ranges 0.80-
0.95). If a drawer calls the variant with its defaults, MMH won't
match and they'll partial-override → hits the p3_char_0252_伊 anti-
pattern the deviation was trying to avoid. If a drawer calls the
variant with per-item MMH anchors, it's functionally identical to
inline pie+shu.

The winning tactic is the DISCIPLINE of MMH-verbatim inline, not the
identity of the calling function. Codifying as a named pattern in
drawer_memory.md preserves the discipline. Same reasoning applies to
shui/yi_side/cao_grass_top/kou_bc_compressed/mian_top_band/ji_gather_top/
nv_bottom_slot recurrences.

### The 8 C's — deviation reasoning right, execution slipped

5 of 8 C's had sound BANK_DEVIATION reasoning (佻, 佾, 例, 或, 说). The
FAILURE mode wasn't the skip — it was the interior/right-half sub-part
whose MMH anchors underspecified detail (兆's inner-column spacing;
月's inner heng placement; 兑's 3-part stack proportions; 戈's hook
angle after corner; 兑's 八 dot heights).

This adds a NEW lesson to B12: BANK_DEVIATION alone is insufficient
for compound chars with unusual sub-structure. The drawer needs to
add explicit sub-part y-band / x-band assertions AFTER committing to
inline. Documented in drawer_memory.md B11 addendum.

### X-cross TERMINAL_FROZEN (4 items)

癶, 処, 乩, 那 all reached retry_4 without PASS. Per B10 plan and
evidence-of-exhaustion (4 mechanisms tried across 4 retries per
item), all frozen. If a future curator wants to unfreeze, they need
to hand-write `chronic/x_cross_composite.py` with per-character
baked-in composite anchors.

### Escalation path for 10 retry_1 items → retry_2

The 10 non-frozen retry FAILs/C from B11 (佚, 社, 佛, 即, 改, 到, 事,
所, 学, 亥) all get one more shot in B12 with the B11 errata fix
ideas encoded per-item. If retry_2 fails on any, that specific item
moves to retry_3 consideration one batch later.

---

## B12 postmortem (position 650)

**Batch outcome**: 20/50 mains (40%; 8 A + 12 PASS + 10 C + 20 FAIL);
5/14 retries (36%; 0 A, 5 PASS via literal-errata mechanism).
Regression from B11 best-batch (62%) — expected reversion. A-rate
still highest of all groups. Cumulative through B12: ~50% success,
~45 A's, ~7.5% A rate.

**G5 format-effect isolation** (informational only, no G4 action):
G5 (G3 memory format + MMH dispatcher injection) ran at 34%/2 A;
G4 at 40%/8 A. Format contributes +6 PASS-points and 4× A rate at
MMH parity. `fat_line`-per-endpoint-width primitive is doing what
G3's PIL-uniform-line cannot. **Do NOT modify G4 format** based on
this — just an isolation result confirming the grid vocabulary +
per-endpoint-width primitive is load-bearing.

**Post-v14-rollback context**: Earlier B12v1 disabled MMH for G4,
collapsed to 16%, was rolled back same-day, all B12v1 attempts
deleted. Current B12 is the re-run with MMH restored. Nothing about
G4's memory changed across the rollback. Curator satisfaction log
entries for B12 correspond to the re-run attempts.

### Key signals

1. **Right-half is the failure surface (new).** In B12 the 亻+X-with-
   unusual-right cluster produced 6 FAILs. The 亻 far-left inline
   was correct in every case; the failure was in the right sub-radical
   (夸, 局, 系, 求, 吾, 夋 — all with no bank primitive AND MMH gives
   endpoints only, not curve/hook/taper). BANK_DEVIATION reasoning
   correct, execution insufficient. Rule for B13+: 亻-far-left inline
   is necessary-not-sufficient; add explicit per-stroke width/curve
   for the right half.

2. **ren_side_far_left DEGRADED (2/9 in B12 vs 8/8 in B11).** Same
   caveat: the tactic is still correct for the 亻 slot. The failure
   surface migrated. Do NOT retreat from named-pattern.

3. **Literal-errata retry mechanism is strong (5/5).** All 5 B12
   retry PASSes were C→PASS at retry_1 via literal errata application
   (物, 佾, 例, 或, 畋). The 8 retry FAILs were mostly cases where
   errata was directional ("proportions off", "3-tier collapsed") not
   literal.

4. **信 A used ren_side directly (first time this batch).** Rule:
   MMH-standard-column 亻 → use ren_side default anchors. MMH-far-
   left-column 亻 → inline pie+shu MMH-verbatim. Read MMH first,
   then pick.

5. **疒 cluster emerging (6 items, 0 PASS).** Candidate for canonical
   `chronic/ne_sick.py` if B13 疒 items also FAIL. Not promoting this
   batch (evidence-driven deferral).

6. **X-cross cluster grew: 亥 → TERMINAL_FROZEN at R4.** Cluster
   now 5 items (癶/処/乩/那/亥). Next mechanism attempt would be
   `chronic/x_cross_composite.py` per-character baked-composite.

### Non-signals / stable

- A-recipe (B9 5-point + B10/B11 points 6-8) unchanged.
- v13 BANK_DEVIATION channel still healthy (33/50 mains B12; too many
  to enumerate here — see attempts/*/generated.py scan).
- Chronic-mandatory-import: 6th null batch. Confirmed retired.
- Variant promotion: continue named-pattern codification. B12 added
  `kou_top_band_compressed_for_*` and strengthened `shui_far_left`
  and `cao_top_band` to 3-batch precedent.

---

## B13 key signals (2026-08-05, position 700)

**Post-B13 update**: 18/50 mains (36%; 6 A + 12 PASS + 11 C + 21 FAIL);
retries 5/14 (36%; 3 A + 2 PASS). Cumulative ~48% mains success,
~51 A total (7.8% A rate). Regression from B11's 62% best-batch
continues to settle around 36-40% baseline.

### Key signals (B13)

1. **A-recipe unchanged (0 new mechanism).** All 6 A's followed B9-B12
   recipe verbatim: explicit decomposition + MMH-verbatim + SELF_CHECK
   + base primitives + N-joint gaps + BANK_DEVIATION-when-slot-embedded
   + chronic-full-canvas awareness. No new principle discovered this
   batch. The recipe is stable.

2. **疒 cluster mechanism WORKS.** B12 6/6 FAIL → B13 6/8 non-FAIL
   (1 A + 1 PASS + 4 C + 2 FAIL). Inline 5-stroke top-left frame with
   MMH-verbatim endpoints + per-character interior slot handling
   reaches A quality (疽). **NO `chronic/ne_sick.py` promotion** —
   codified as named pattern `ne_sick_top_left_frame_for_*` instead.
   Same rationale as ren_side_far_left: baked defaults would defeat
   MMH-verbatim discipline.

3. **Right-half is still the primary failure surface (2nd batch).**
   Cluster A (7 B13 FAILs): 亻+X-with-unusual-right pattern continues
   dominant. `ren_side_far_left` slot handling correct in every case;
   right sub-radical fails on curve/hook/taper (MMH gives endpoints
   only). Same as B12. Awaiting form_catalog per-stroke-class taper
   upgrade to give drawers a fallback beyond MMH.

4. **X-cross cluster grew to 6.** 佚 R3 FAIL → TERMINAL_FROZEN.
   Cluster: 癶, 処, 乩, 那, 亥, 佚. All exhausted retry ladder.
   Mechanism candidate: `chronic/x_cross_composite.py` (per-char baked
   composites). Not attempting until enough evidence to design.

5. **新 candidate cluster: 礻-compound.** 社 R3 FAIL → TERMINAL_FROZEN.
   礻 dot-LAST defensive rule works; failure is 土 slouching into 礻
   slot. Also flagging 神 (C in B13 R1). If 2+ more 礻-compounds hit
   R2+ FAIL, consider `chronic/shi_altar_compound.py` (礻 as left-column
   radical with slot-width parameter).

6. **Literal-errata retry mechanism confirmed strong (5/14 R1 grads).**
   All 5 R1 graduations (畎A, 将A, 度A, 亲PASS, 说PASS) applied
   LITERAL geometry fix from B12 errata. 6 R1/R2 FAILs had directional
   errata or were chronic. Rule for B14: only queue retries with
   LITERAL errata.

7. **Format effect at MMH parity WIDENED.** B12: G4 +6 pts PASS, 4x
   A vs G5. B13: G4 +22 pts PASS, 6x A vs G5. Cumulative G4 A rate
   7.8% vs G5 3.0%. Confirms continuing current mechanism.

### Non-signals / stable

- A-recipe unchanged from B11.
- Chronic-mandatory-import: 7th null batch. Retired confirmed.
- Named-pattern codification remains the response to slot-embedded
  recurrences. `ne_sick_top_left_frame_for_*` added to registry.
- Bank size stable at ~125 files. No prune/promotion this batch.
- Memory index and file layout unchanged.
- Solo-wins observation (Obs-01): 3 G1 solo-A in B13 (俜, 畟, 热) —
  logged to root OBSERVATIONS.md; no G4 action.
