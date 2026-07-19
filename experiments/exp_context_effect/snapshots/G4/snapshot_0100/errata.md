# 错题集 (G4 grid-bank)

Items failed at batch judgment. Each entry names the item, my diagnosis
(structural + panel-style thinking), and the specific fix to try on the
next retry. Retries are governed by the shared 错题集 rules (see
`../../protocol/shared_rules.md`).

## Batch 1 — item p1_stroke_19_横斜钩 (FAIL)

**Item**: 横斜钩 (héng xié gōu) — 横 opening → slanted descent → up-left hook.
**Attempt anchors used**:
- head    = ('TL', 0.35, 0.30)
- corner  = ('TR', 0.55, 0.40)
- belly   = ('C',  0.55, 0.75)
- hook_pt = ('BC', 0.30, 0.70)
- tip     = ('BC', 0.10, 0.30)

**Diagnosis (structural)**:
- Stroke count OK (one continuous compound stroke rendered as three phases).
- Cell placement broke down at the 斜 (slanted) descent phase. The
  method `ctrl = 2*belly - midpoint(corner, hook_pt)` places the body
  Bezier's control point far to the LEFT of the chord, so the descent
  swept leftward toward BC/BL instead of down-and-right toward BR.
- Hook_pt at BC (0.30, 0.70) is directly BELOW head, not down-and-right.
  A real 横斜钩 ends at the LOWER-RIGHT (BR region), then flicks the
  hook up-and-LEFT into BC. Placing hook_pt in BC and tip further left
  in BC collapses the whole stroke onto the left side of the canvas.

**Diagnosis (panel)**:
- The rendered PNG reads as a stylized "7" — a short 横 at the top and
  a long curved descent hooking down at the bottom. A viewer would not
  identify it as 横斜钩; it looks closer to 横折弯钩 or a mangled 弯钩.
- The distinguishing feature of 横斜钩 — a substantial RIGHTWARD-DOWN
  slanted descent BETWEEN the 横 and the hook — is invisible.

**Specific fix for next retry**:
1. Place `hook_pt` in the BR region, e.g. ('BR', 0.55, 0.70), so the
   slanted descent spans from TR corner (~top-right) down-and-RIGHT to
   BR (~bottom-right). The chord direction should read as
   top-right → bottom-right, slanting slightly rightward as it descends
   (this is the "斜" phase).
2. Place `belly` slightly RIGHT of the chord midpoint (e.g. C 0.70
   0.75 or MR 0.15 0.75) so the concave-up bow reads correctly.
3. Place `tip` UP-and-LEFT of hook_pt but still inside the BR/BC
   junction, e.g. ('BR', 0.20, 0.35). The hook direction on 横斜钩 is
   up-and-left with a short flick — length ≈ 25% of the slanted body's
   chord.
4. Sanity check: after computing `p_corner`, `p_hook`, `p_tip` in
   pixels, confirm `p_hook.x > p_corner.x` (rightward descent) and
   `p_tip.x < p_hook.x` and `p_tip.y < p_hook.y` (up-left hook). Assert
   these inequalities before rendering — the failed attempt would have
   caught the leftward drift.
5. Alternative — reuse `draw_heng_gou` composed with an added slanted
   segment, so the compound structure is explicit instead of hidden
   inside one big Bezier with a mis-derived control point.

Retry after 20 more items per shared 错题集 rules.

## Batch 2 — item p1_stroke_21_横折弯 (GRADUATED via batch-3 retry PASS)

Retry PASS in batch 3. Promoted to Success Bank as `heng_zhe_wan.py`.
Root fix that worked: hand off descent+sweep to `draw_shu_wan` (which
uses a smooth Bezier for the round bottom) instead of a straight
fat_line corner. Removed from active errata.

## Batch 2 — item p1_stroke_25_横折弯钩 (FAIL)

**Item**: 横折弯钩 (héng zhé wān gōu) — 横折弯 + upward hook flick. The
canonical stroke of 乙 and 九.

**Diagnosis (structural)**: The attempt uses one big quad-Bezier for the
descent+sweep with belly at `('MR', 0.15, 0.60)`. That control pulls the
curve LEFT-and-DOWN, producing a stroke that reads as a huge 弯钩 leaning
left, not a 横折 opening followed by a rightward round sweep. The distinctive
top-横 phase is present but is dwarfed by the swooping body.

**Diagnosis (panel)**: A reader would identify the shape as 弯钩 with an
extraneous top-line, not 横折弯钩. The 弯 sweep must terminate on the
LOWER-RIGHT with a short upward hook — the attempt's `hook_pt=('BC', 0.55, 0.55)`
puts the hook base in the center-bottom, missing the rightward extent.

**Specific fix for next retry (anchor-format)**:
1. Reuse the batch-2 primitive `draw_yi` (which passed as 乙 — same
   compound structure, different name). Rebrand it as the primitive
   for stroke 25 with a slightly rebalanced anchor plan.
2. If deriving fresh: place `hook_pt` in BR (not BC) — e.g. `('BR', 0.75, 0.55)`,
   with `tip` at `('BR', 0.75, 0.15)` (directly above → upward flick).
3. Split the descent+sweep into TWO Bezier segments (like `draw_yi`):
   one for the down-left descent (shoulder → knee), one for the
   rounded rightward sweep (knee → hook_pt). This makes the shape
   analyzable per-phase and matches how MMH decomposes it.

## Batch 2 — item p1_stroke_26_横折折 (GRADUATED via batch-3 retry PASS)

Retry PASS in batch 3. Promoted to Success Bank as `heng_zhe_zhe.py`.
Root fix that worked: hard assertion `|tail.y - corner2.y| < 12`
guards against extrapolating stroke 30's fourth drop. Explicit
3-segment fat_line staircase with horizontal termination. Removed
from active errata.

## Batch 2 — item p1_stroke_27_竖折撇 (GRADUATED via batch-3 retry PASS)

Retry PASS in batch 3. Promoted to Success Bank as `shu_zhe_pie.py`.
Root fix that worked: reuse `draw_shu_zhe` + `draw_pie` (tapered
needle tip) with P joint 顿笔 disc at the pivot. Removed from active
errata.

## Batch 2 — item p1_stroke_29_横折折撇 (FAIL)

**Item**: 横折折撇 (héng zhé zhé piě) — 横折折 opening + tapered 撇
tail. Occurs in 及, 廷, 建.

**Diagnosis (structural)**: The attempt sets `pie_tail_w=1` in code,
so the rasterizer intent is right, but the anchor plan
`corner3=('C', 0.85, 0.45) → tip=('BL', 0.30, 0.85)` crosses the whole
canvas — the 撇 becomes so long it dominates the character. The
横折折 opening ends up looking like a small hat on top of a giant 撇.
Additionally the middle `corner2` at `('C', 0.30, 0.35)` places the
横→竖 fold going leftward (opposite direction from stroke 30's rightward
staircase), which breaks pattern-recognition.

**Diagnosis (panel)**: A reader would identify the shape as "一撇 with
a decorative 横折 header" — recognizable as 撇 but not as the specific
横折折撇 stroke.

**Specific fix for next retry (anchor-format)**:
1. Keep the 横折折 opening compact in the upper half of the canvas
   (all corners with y_frac ≤ 0.5 relative to canvas midline).
2. Anchor plan (proposed):
   - head    = ('TL', 0.35, 0.30)
   - corner1 = ('TR', 0.55, 0.35)   # end heng1 (right)
   - corner2 = ('MR', 0.05, 0.35)   # short shu drop (down; same x as c1)
   - corner3 = ('MR', 0.80, 0.35)   # end heng2 (right)
   - tip     = ('BL', 0.50, 0.80)   # 撇 tail down-and-left, tapered
3. Reuse `draw_heng_zhe_zhe_zhe` (batch2 promoted) for the header
   staircase, then `draw_pie` for the terminal segment. Compositional
   structure makes the fault modes obvious.
4. Assert `p_tip.x < p_corner3.x` (撇 goes LEFT).

## Batch 2 — item p2_radical_003_丿 (FAIL)

**Item**: 丿 (piě-radical, 1画) — standalone. Same primitive as stroke
03 (`draw_pie`), but as a radical it must occupy the 米字格 diagonal
prominently.

**Diagnosis (structural)**: Attempt anchor plan is TR(0.55, 0.20) →
BL(0.20, 0.85). Head at 0.55 within TR sits well inside the top-right
cell rather than reaching the corner; tail at 0.20 within BL is far
from the BL corner. Result: a shortened 撇 that reads as a mid-canvas
stroke fragment, not a spanning radical. Head-width=14 is fine; span
is the problem.

**Diagnosis (panel)**: A reader viewing the standalone PNG would say
"this looks like a small 撇, not a page-worthy radical" — the human
judge likely rejected because the shape doesn't fill the 米字格 as a
radical is expected to.

**Specific fix for next retry (anchor-format)**:
1. Widen the anchor span to reach cell corners of the anti-diagonal:
   - head = ('TR', 0.85, 0.15)  # far upper-right corner
   - tail = ('BL', 0.15, 0.85)  # far lower-left corner
2. Consider slightly thicker head (head_width=16) and higher curve
   (curve=0.15) so the radical reads as a full anti-diagonal sweep.
3. This is a wrapper-with-tuned-defaults problem — no primitive
   rewrite needed. Same pattern that succeeded for R01 丨, R02 亅,
   R04 乛, R05 一, R08 丶.

## Batch 2 — item p2_radical_007_乚 (FAIL)

**Item**: 乚 (1画 radical, 竖弯 family). Standalone.

**Diagnosis (structural)**: Attempt reuses `draw_shu_wan` (stroke 13,
which passed) with anchors head=TC(0.30,0.15), corner=BC(0.30,0.70),
tail=BR(0.70,0.45). The horizontal finish at BR(0.70,0.45) ends
mid-canvas-right — probably not far enough right for a standalone
radical whose signature is a bold reach across the bottom of the
米字格. Also `corner` at BC(0.30,0.70) leaves the turn near mid-left,
not at bottom-center — the "L" reads as an off-center wan rather than
a symmetric standalone radical.

**Diagnosis (panel)**: A reader viewing the PNG would say "this is a
竖弯 primitive, not the radical 乚" — because a radical is expected to
show a distinct proportion (deeper hook shape, longer horizontal
finish reaching into BR corner).

**Specific fix for next retry (anchor-format)**:
1. Move the vertical column to the mid-column and extend the horizontal
   finish to the right edge:
   - head   = ('TC', 0.50, 0.10)
   - belly  = ('C',  0.50, 0.75)
   - corner = ('BC', 0.55, 0.80)   # turn near bottom-center-right
   - tail   = ('BR', 0.95, 0.50)   # reach nearly to canvas right edge
2. Consider a subtle upward flick at tail (or terminate with a
   thicker 顿笔 disc) so the radical reads as intentional not truncated.
3. Alternative: this radical is actually canonically a 竖折 (or 乙-family
   without the hook) — worth revisiting whether `draw_shu_wan` is the
   right base primitive at all. Check GT if reference material becomes
   available.

---

# Batch 3 — retry outcomes

## p1_stroke_19_横斜钩 (RETRY FAIL — still in errata)

Retry attempt used the "wider hook_pt at BR + rightward-slant descent"
fix from the batch-2 errata but still FAILED at human judgment.
Diagnosis carries over: the compound stroke's identifying signature
(rightward-slanted descent + short up-left hook) remains hard to render
without a visible bend transition. Next retry idea: split into two
explicit Bezier segments (top 横 + slanted descent + hook), NOT one
big Bezier; and use `_anchor.fat_line` for the top 横 opening so the
shape reads as "横 → 斜 → 钩" rather than a single swoosh. Cool-down
20 items.

## p1_stroke_25_横折弯钩 (RETRY FAIL — still in errata)

Retry attempt still FAILED. The 横折弯钩 signature is very close to
乙 (which passed as `draw_yi`), but the anchor-format demands a
different balance: the top 横 is shorter, the descent is more vertical
(not斜), and the round sweep at the bottom is tighter. Next retry:
adapt `draw_yi` with `shoulder` moved closer to `head` (shorter top
横), and `belly1` placed at MC (0.55, 0.55) so the descent stays
vertical rather than slanting left. Cool-down 20 items.

## p1_stroke_29_横折折撇 (RETRY FAIL — still in errata)

Retry attempt kept the 3-segment staircase compact in the upper half
but still FAILED. Suspicion: the terminal 撇 tip x-position (`('BL',
0.50, 0.80)`) doesn't sweep far enough LEFT — the 撇 phase reads as
a short accent rather than the dominant tail. Next retry: extend
`tip` to `('BL', 0.20, 0.90)` (near BL corner) so the 撇 reads as
the dominant final gesture, matching how 及/廷/建 use this stroke.
Cool-down 20 items.

---

# Bootstrap batch (positions 33-50) — G4 FAILs

## p2_radical_003_丿 (FAIL, bootstrap — 2nd time in errata)

**Attempt anchors**: head TL(0.627, 0.794) → tail BL(0.141, 0.892).
**Diagnosis**: Verbatim-MMH anchors produce a stroke crammed into the
lower-left. Head y_frac=0.794 puts start at ~py 79 in TL and tail
y_frac=0.892 puts tip at ~py 89 in BL — the whole stroke lives in the
lower half. GT has 撇 sweeping from upper-mid through mid-canvas down
to lower-left, spanning ~80% of canvas height. This is the SAME failure
mode as batch-2's 丿; the errata fix (widen to anti-diagonal ('TR',
0.85, 0.15)→('BL', 0.15, 0.85)) was not applied because the drawer
did not consult errata before drawing.
**SELF_CHECK vs human**: DISAGREE — self-check rubber-stamped MMH
anchors as passing.
**Fix**: Override MMH — use head=('TR', 0.85, 0.15), tail=('BL', 0.15, 0.85),
head_width=16, curve=0.15. Cool-down 20 items.

## p2_radical_007_乚 (FAIL, bootstrap — 2nd time in errata)

**Attempt**: draw_shu_wan head TL(0.636, 0.867), corner BL(0.70, 0.30),
tail BR(0.552, 0.124).
**Diagnosis (visual)**: The L-shape reads OK proportion-wise, but the
tail terminates ABRUPT (flat) at mid-right. GT's tail has a small
upward tick and the whole shape is more elongated. Attempt uses
draw_shu_wan (no hook), GT expects a subtle tick.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: Use draw_shu_wan_gou (add tip at ('MR', 0.5, 0.3) for a short
up-tick), or add a 顿笔 disc at the tail terminus so the ending reads
intentional. Cool-down 20 items.

## p2_radical_014_厂 (FAIL, bootstrap)

**Attempt**: 横 head TC(0.011, 0.97) tail TR(0.432, 0.838); 撇 head
TL(0.773, 0.94) tail BL(0.202, 0.974).
**Diagnosis (visual — CRITICAL)**: 横 and 撇 render as visually
DISCONNECTED fragments — horizontal in upper-right, curved 撇 in
lower-left, large void between them. Root cause: the drawer treated
N-class joint as literal separation. Actual pixel positions: 横 head
at (100, 97), 撇 head at (77, 94) — but the 撇 body sweeps AWAY from
the 横 downward-left, so the visual gap opens up dramatically. Also
撇 tail at BL(0.202, 0.974) → (20, 97) puts the tail at the extreme
lower-left; the sweep is too long and diagonal, making the two strokes
occupy separate quadrants.
**SELF_CHECK vs human**: DISAGREE — visual disconnect should have been
obvious.
**Fix**: Weld or near-weld 撇 head to 横 head using SHARED anchor
tuple like ('TC', 0.15, 0.5). The 撇 body then hangs off the LEFT end
of the 横 in a canonical inverted-J shape. See principle_bank TR4 —
shared anchor tuple pattern.
Cool-down 20 items.

## p2_radical_015_刀 (FAIL, bootstrap)

**Attempt**: 横折钩 (heng_zhe_gou) + 撇 (pie).
**Diagnosis (visual — CRITICAL)**: The 横折钩 hook flick points down/
down-left instead of up-and-left (canonical). The 撇 starts at C
(center) instead of at the left end of the 横 — visually splits the
character. Whole shape reads as chaotic 4-sided bounding box, not
elegant 2-stroke 刀.
**SELF_CHECK vs human**: DISAGREE — drawer noted `gap≈56 px` as
"N-class satisfied" but ignored compositional problems.
**Fix**: (1) 撇 head shares anchor with 横 head: both at ('ML', 0.5, 0.4)
= T-class weld. (2) heng_zhe_gou tip at ('BR', 0.4, 0.5) so the flick
goes UP-and-LEFT (tip.y < tail.y AND tip.x < tail.x). (3) Reduce the
horizontal extent of the 横 — GT shows a fairly compact top-bar.
Cool-down 20 items.

## p2_radical_016_刂 (FAIL, bootstrap)

**Attempt**: 短竖 C(0.113, 0.16)→BC(0.187, 0.174) + 竖钩 head
TC(0.614, 0.712), hook_pt BC(0.342, 0.701), tip BC(0.05, 0.35).
**Diagnosis (visual — CRITICAL)**: The 竖钩 body is a SLANTED descent,
not a straight vertical: head.x=161 vs hook_pt.x=134 → body drifts
leftward. shu_gou requires belly.x == head.x for a straight body, but
MMH anchors put head and hook_pt at different x_fracs. The drawer's
own docstring flagged this incompatibility but rendered anyway (TR8
violation).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: Override hook_pt to share head's x_frac: hook_pt=('BC', 0.614, 0.9).
Then tip=('BC', 0.35, 0.6) for up-left flick. 短竖 also should extend
from ('ML', 0.5, 0.3) to ('C', 0.35, 0.8) to read as a proper vertical
partner. Cool-down 20 items.

## p2_radical_017_儿 (FAIL, bootstrap)

**Attempt**: 撇 (pie) + 竖弯钩 (shu_wan_gou).
**Diagnosis (visual — CRITICAL)**: 撇 is OK. 竖弯钩 is broken — with
head at TC(0.567, 0.838) (y_frac 0.84 → py 84), belly C(0.567, 0.65) →
py 165, corner BC(0.62, 0.82) → py 282, hook_pt BR(0.35, 0.55) → py
255, tip BR(0.71, 0.227) → py 223. The tip is BELOW-RIGHT of head,
making the "hook" look like a long tail extending rightward, not the
canonical up-tick.
**SELF_CHECK vs human**: DISAGREE — drawer's asserts (tip above
hook_pt) held numerically but shape was unrecognizable.
**Fix**: Canonical 竖弯钩 anchor recipe for 儿:
  head=('TC', 0.55, 0.2), belly=('C', 0.55, 0.5),
  corner=('BC', 0.6, 0.75), hook_pt=('BR', 0.2, 0.7),
  tip=('BR', 0.25, 0.4).
Bend at bottom, hook_pt to the right, tip up-right (canonical up-flick).
Cool-down 20 items.

---

# Batch B1 — retry outcomes (bootstrap-batch failures)

## p2_radical_007_乚 (RETRY PASS) — graduated to Success Bank (`yi_hook.py`)
Fix that worked: swapped `draw_shu_wan` → `draw_shu_wan_gou` and mapped the tip
directly to the MMH tail so the up-tick reads intentional. TR11 self-check:
process notes only ("Fix applied per errata"), no named PNG-vs-GT visual
agreements. Passed anyway; the mechanical fix carried it.

## p2_radical_014_厂 (RETRY PASS) — graduated to Success Bank (`chang.py`)
Fix that worked: T-weld override — 撇 head shares anchor with 横 head via a
SHARED anchor tuple, deviating from MMH's nominal N spec. Canonical
inverted-J now reads as 厂 to a human judge. TR11: process notes only.

## p2_radical_016_刂 (RETRY PASS) — graduated to Success Bank (`dao_side.py`)
Fix that worked: overrode hook_pt.x to share head.x_frac so `draw_shu_gou`'s
straight-body invariant is satisfied. This is the exact TR8 rule (do not
render a primitive with known-broken input). TR11: process notes only.

## p2_radical_017_儿 (RETRY PASS) — graduated to Success Bank (`er_legs.py`)
Fix that worked: canonical 竖弯钩 anchor recipe with the bend at the BOTTOM
(BC corner) and the hook flick going UP-right from BR. Prior attempt had
the geometry inverted. TR11: process notes only.

## p2_radical_003_丿 (RETRY FAIL — 2nd time in errata, retry_n=1)

**Retry-1 attempt**: head=('TC', 0.20, 0.65) → tail=('BL', 0.55, 0.80).
Fix idea from prior errata (widen to anti-diagonal ('TR',0.85,0.15) →
('BL',0.15,0.85)) was NOT applied — drawer used a milder shift.
**Failure mode**: same as bootstrap — stroke still lives too low; the
head at TC(0.20, 0.65) sits mid-canvas rather than at the upper-right
corner. This is the SAME failure mode; the fix in errata was not
followed literally.
**Next retry**: apply the literal errata fix — head=('TR', 0.85, 0.15),
tail=('BL', 0.15, 0.85), head_width=16, curve=0.15. Cool-down 20 items.

## p2_radical_015_刀 (RETRY FAIL — 2nd time in errata, retry_n=1)

**Retry-1 attempt**: T-weld at ('C', 0.10, 0.35), 横折钩 corner at
('MR', 0.55, 0.35), tail at ('BR', 0.30, 0.55), tip at ('BR', 0.05, 0.35);
撇 tail at ('BL', 0.20, 0.90).
**Failure mode**: DIFFERENT from bootstrap. Bootstrap failed because
the hook flicked down and the 撇 head sat mid-canvas. Retry-1 correctly
welded the heads AND flicked the hook up-left, but the horizontal 横 is
now too long and the whole 横折钩 leans too far right — the 撇 sweep
takes up the left half and the vertical descender of 横折钩 is compressed
into the right quarter. Character reads as a lopsided pinwheel, not 刀.
**Next retry**: (a) shorten the top 横 (corner at MR 0.10, not MR 0.55);
(b) let the vertical descender occupy more of the C→BC column (tail at
BC 0.60, 0.60 instead of BR 0.30, 0.55); (c) 撇 tail slightly less far
left (BL 0.35, 0.85). Cool-down 20 items.

---

# Batch B1 — main-item FAILs (15 items)

Format: item, human FAIL diagnosis (structural + panel), curator-vs-drawer
SELF_CHECK calibration, fix idea for future retry.

## p2_radical_023_卩 (FAIL)
**Attempt**: 3 strokes with 竖 body — the drawer chose to render 卩 as if it
had 3 strokes (short 横折折折 top + long descending 竖 body). MMH-official
stroke count for 卩 is 2. Silhouette reads as a mangled 阝 or garbled 3-
stroke composite; 卩's signature 横折钩 top + 竖 body did not read cleanly.
**SELF_CHECK vs human**: DISAGREE — overall_pass=True with TR11-style named
visual agreements. False confidence. Add to sandbox.md.
**Fix**: 2 strokes only. s1 = 横折钩 (small P-hook at upper-right). s2 = 竖
straight descending. Consider `heng_zhe_gou` primitive with tight anchors.

## p2_radical_024_冂 (FAIL)
**Attempt**: shu + heng_zhe with N-gap ~17 px at TL. Structurally correct
count and joint class. Visually the 竖 head sat well below the 横 head
because MMH anchors weren't expanded to standalone TR9 span — the whole
character was compressed to the upper half.
**SELF_CHECK vs human**: DISAGREE. Add to sandbox.md.
**Fix**: TR9 override — 竖 head at ('TL', 0.10, 0.15), 横折 head at ('TL',
0.20, 0.15), so both start at the top; span both walls to y_frac 0.85+.

## p2_radical_025_力 (FAIL)
**Attempt**: heng_zhe_gou + pie. TR11 self-check listed named visual
agreements. Failure mode: the 撇 sweeps from too far right (starting inside
the 横折钩 top-bar); GT has 撇 diverging from LEFT end of the top-bar.
**SELF_CHECK vs human**: DISAGREE despite TR11 compliance. Add to sandbox
as a NAMED counter-example: TR11-compliant SELF_CHECK still lost.
**Fix**: 撇 head must share anchor with 横折钩 head (upper-LEFT), T-weld.

## p2_radical_038_㔾 (FAIL)
**Attempt**: 2-stroke composition with heng_zhe (top piece) + big shu_wan_gou
outer bowl. Structurally sensible but visually the outer sweep landed too
tall and thin, and the top piece didn't nestle into it — reads as two
disconnected shapes.
**SELF_CHECK vs human**: DISAGREE. Add to sandbox.md.
**Fix**: this is 2画 but the top piece is TINY (~30 px wide, tucked into
upper-left of the bowl). Draw with s1 head=('TL', 0.30, 0.30), tiny corner
at ('TL', 0.60, 0.30), tail at ('TL', 0.55, 0.55). Then a full-canvas 竖弯钩
bowl.

## p2_radical_039_艹 (FAIL)
**Attempt**: 3 strokes — long horizontal + two crossing shorter strokes
descending through it (P-class). Drawer claimed TR11 agreements. Failure:
the two "descenders" landed as diagonals (撇-like) rather than clean 竖 or
short 竖 — reads as 卄 or a broken 井.
**SELF_CHECK vs human**: DISAGREE. Add to sandbox.md.
**Fix**: 艹 = 十 + 十 pattern (or 廾-like). Use two 竖 (vertical, no curve)
piercing a single wide 横. Left 竖 head-x < right 竖 head-x; both descend
straight below the horizontal.

## p2_radical_045_寸 (FAIL)
**Attempt**: 3 strokes: 横 (mid) + 竖钩 (through center) + 点 (right side).
Drawer claimed TR11 agreements — visually the 竖钩 looked reasonable but
the 点 landed too far right and too high (upper-right, not at bottom-mid).
GT has the 点 tucked into the CROTCH between the 竖钩's hook and the 横.
**SELF_CHECK vs human**: DISAGREE. Add to sandbox.md.
**Fix**: 点 anchor: head near ('C', 0.60, 0.55), tail toward ('C', 0.80, 0.75)
— NOT the upper-right corner. Alternatively write 寸 as 十 + 丶 with the
丶 near the bottom-right of the crossing.

## p2_radical_047_飞 (FAIL)
**Attempt**: 3 strokes. Drawer used one revision. Failure: the compound
sweep of 飞 (top 横折 opening → deep descent with wan → up-tick) got broken
into a 横折 that stopped too shallow and a wan_gou stub that didn't
continue the same visual line — reads as two disjoint pieces + a dot.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 飞 is best drawn as ONE compound top piece (横斜钩-style, single
inlined variable-width polyline) + one small 撇/点 for the inner mark. See
Phase-1 errata for 横斜钩 fix pattern.

## p2_radical_050_弓 (FAIL)
**Attempt**: complex 3-stroke composition. Failure: the middle 横折 sat too
close to the top 横折 — the middle "waist" of 弓 collapsed. Reads as 己-like
2-loop, not the 3-tier 弓 with an open belly.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: enforce vertical separation — s1 top-loop in TL/TC band (y_frac
0.0-0.35), s2 middle horizontal at y_frac 0.45-0.50, s3 bottom sweep at
y_frac 0.65-1.0. Anchors from bootstrap batch 乙 (`yi_second.py`) may be
adaptable.

## p2_radical_053_己 (FAIL)
**Attempt**: 3 strokes with s3 head overridden ML→TL "per sandbox
Pattern 1". Failure: even with the override, the descent of s3 was still
too short and the up-hook curled the wrong way — reads as 巳 or ㄹ.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 己 canonical shape = top 横折 + short 横 + 竖弯钩 with pronounced
UP-hook at bottom-right. Use `shu_wan_gou` for s3 with corner in BC and
tip flicking UP (tip.y < hook_pt.y).

## p2_radical_054_彐 (FAIL)
**Attempt**: revised once; SELF_CHECK set visual_ok=False after diagnosis
that stroke 3 landed as a diagonal (head in BL row=2, tail in C row=1 —
100 px cell-height tilt). Drawer submitted knowing it was wrong.
**SELF_CHECK vs human**: AGREE (both said fail). Positive calibration case.
**Fix (sandbox rule already noted)**: BOTH endpoints of a 横 must sit in
the SAME CELL ROW. Add to TR8 sanity checks. Redraw with s3 head ('BL',
0.35, 0.0) and s3 tail ('BC', 0.90, 0.0) — both in BL/BC row 2.

## p2_radical_055_彑 (FAIL)
**Attempt**: 3 strokes, drawer's SELF_CHECK carried TR11 named agreements
but flagged uncertainty. Failure: strokes read as a stack of 3 horizontals
with no clear pig-snout signature; the top point wasn't distinct.
**SELF_CHECK vs human**: PARTIAL agreement (drawer was uncertain).
**Fix**: 彑 = compact top-triangle (2 strokes forming inverted V) + one
short bottom horizontal. Ensure the top two strokes converge to a shared
TC anchor forming a P-weld apex.

## p2_radical_058_马 (FAIL)
**Attempt**: 3 strokes with two revisions used (drawer notes anchor plan
+ s3 y-level both revised). Failure: the 马 top-box + bottom horizontal +
hook composition came out as an ambiguous 3-stroke doodle. The bottom
horizontal did not clearly cross the right vertical.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: simplified 马 = 3 strokes: (1) 横折 for top box, (2) 竖折折钩 for
right descender+bottom+hook (single compound stroke, use `shu_zhe_zhe_gou.py`),
(3) 横 crossing through the middle. The compound stroke does most of the
work.

## p2_radical_059_门 (FAIL)
**Attempt**: 3 strokes: dian + shu + heng_zhe_gou. Structurally 门 IS 3
strokes, but the drawer laid them out with big gaps — the top dot sat
alone in the upper-center, the left 竖 was far to the left, and the right
heng_zhe_gou was far to the right. No enclosing feel.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: enforce enclosing-radical TR2 — spans x_frac 0.05-0.95, y_frac
0.05-0.95. Left 竖 head at ('TL', 0.30, 0.20), tail at ('BL', 0.30, 0.95).
Right heng_zhe_gou head at ('TL', 0.35, 0.20) (T-weld with left 竖 head)
so the top bar is continuous. Top 点 sits ABOVE the left 竖 as a lid, not
floating separately.

## p2_radical_061_女 (FAIL)
**Attempt**: 3 strokes: 撇点 + 撇 + 横. Drawer claimed TR11 agreements but
notes were minimal (single-line). Failure: the 撇点 P-pivot landed in the
lower-left rather than the upper-mid, so the character reads as a splayed
X rather than 女's characteristic top-cross-body-cross-arm.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 女 canonical: s1 撇点 with head at ('TC', 0.35, 0.20) and pivot at
('C', 0.30, 0.85); s2 撇 crossing s1 near the center; s3 horizontal arm at
y_frac ≈ 0.60 spanning wide. All 3 joints P-welded per MMH.

## p2_radical_062_犭 (FAIL, drawer knew — overall_pass=False)
**Attempt**: 3 strokes. Drawer's SELF_CHECK explicitly set overall_pass=
False after noting s1×s2 didn't visibly cross (21.6 px gap) and s2⇆s3
N-joint gapped 61.9 px. Sandbox already documents the two structural
lessons (P-cross needs shared pixel, N-joint on curved spine needs
derived anchor).
**SELF_CHECK vs human**: AGREE (both said fail). Positive calibration case.
**Fix**: implement sandbox's derived-anchor pattern — compute the pixel
midpoint of s2's bowed body first, then set s3.head anchor by inverting
anchor_to_xy so it lands ON that pixel. For s1×s2, pick a shared P_cross
point and construct both chords to pass through it.
