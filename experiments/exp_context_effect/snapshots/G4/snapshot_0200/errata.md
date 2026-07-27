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

## Batch B2 — retry outcomes (B1 failures)

## p2_radical_054_彐 (RETRY PASS) — graduated to Success Bank (`xue_broom.py`)
Fix that worked: every 横's endpoints in the SAME cell row (TR8 rule 5).
Prior failure: s3 head in BL (row=2) + tail in C (row=1) → 100 px tilt.

## p2_radical_059_门 (RETRY PASS) — graduated to Success Bank (`men.py`)
Fix that worked: enclosing-radical layout enforced (TR2). All three
strokes clamped into a coherent central-column enclosure; s1 dot as a
lid above s2 head; s3 top bar continues at s2 head y.

## p2_radical_024_冂 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: TR9-expanded — s1 shu TL(0.10,0.25)→BL(0.10,0.95);
s2 heng_zhe TL(0.15,0.10)→TR(0.90,0.10)→BR(0.90,0.95).
**Failure mode**: frame nearly square (280×285 px), too tall vs 冂
canonical proportion. s1 head at y=25 drops below s2 top-bar left
endpoint at y=10 — left corner has visible overshoot.
**Fix**: align s1 head y with s2 top-bar y (both at 15); reduce frame
width to ~230 for canonical proportion. Cool-down 50 items.

## p2_radical_038_㔾 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: s1 rebuilt as tiny 横+短撇 fold in upper-left; s2
big 竖弯钩 bowl with belly BL(0.80, 0.98).
**Failure mode**: s2 quad_bezier belly control makes body bulge
down-left then swing up-right — J-shape belly at bottom-left, not
smooth vertical→right sweep. s1 tail sits INSIDE the s2 belly area.
**Fix**: rewrite s2 as strict 竖弯钩 sequence (straight vertical descent
→ rounded corner → rightward sweep → up-flick). Reuse `wan_gou.py`
+ `shu_wan_gou.py` recipe with tighter belly.x = head.x. Place s1
CLEARLY above s2 head with ≥15 px gap. Cool-down 50 items.

## p2_radical_047_飞 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: s1 as two chained quad_bezier; s2 short 撇; s3 tiny
tick.
**Failure mode**: s1 "horizontal" opening rises 115 px over 225 px x
→ reads as diagonal not horizontal. Second control pulls arc deep
into lower-left, sweeping through mid-canvas and overlapping the
inner marks.
**Fix**: draw s1 as ONE inlined variable-width polyline (per sandbox
Pattern E) with true horizontal opening: head ML(0.2, 0.3) + bend
TR(0.5, 0.4) + tip BR(0.5, 0.9). Position s2/s3 marks strictly INSIDE
the arc — not on the arc line. Cool-down 50 items.

## p2_radical_050_弓 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: 3-tier separation attempted with s1 横折 top, s2
short 横 mid, s3 竖折折钩 bottom.
**Failure mode**: s1 "drop" segment goes DOWN-LEFT from corner
(255,40) to tail (175,130) instead of straight down (TR8 rule 6
violation — column mismatch). s3 loop inverted/reversed.
**Fix**: rewrite EVERY 横折 as {heng, straight down-drop sharing
corner.x with tail.x}. Redo s3 as `shu_zhe_zhe_gou.py` composed:
descend vertically → 横 sweep left → up-flick. Cool-down 50 items.

## p2_radical_053_己 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: s1 横折 upper, s2 short 横 mid, s3 竖弯钩 with
corner in BL rather than BC.
**Failure mode**: s1 head and s3 head both at ~(85, 80) — overlapping
strokes at top-left corner. s1 tail at (180, 130) is 130 px above s3
corner at (90, 240); the three tiers look disconnected even with s2.
**Fix**: enforce s1.tail y aligned with s2 body region; use
`heng_zhe.py` with straight down drop; the three vertical tiers must
touch at intended endpoints (share anchor tuples per TR4).
Cool-down 50 items.

## p2_radical_058_马 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: S1 compact top 横折; S2 竖折折钩 with first leg
slanting LEFT then heng right; S3 long bottom 横.
**Failure mode**: S1 top piece only ~75 px wide / 55 px tall — too
small vs GT proportion. S2's first leg slants left-down instead of
vertical, top-box asymmetric. S3 bottom heng shares y=250 with S2
hook_pt → passes through S2 body, visual overlap.
**Fix**: enlarge top-box; straighten S2 first leg to strict vertical
(column-share per TR8); separate S3 heng from S2 hook_pt by ≥25 px in
y. Reuse `shu_zhe_zhe_gou.py`. Cool-down 50 items.

## p2_radical_062_犭 (RETRY FAIL — retry_n=1)
**Retry-1 attempt**: derived-anchor pattern applied per sandbox lesson:
s2 bowed pie; s1 endpoints DERIVED to pass through P_cross on spine at
t=0.28; s3 belly head DERIVED from spine at t=0.48. Structural asserts
pass (best_p<3, n_gap~8).
**Failure mode**: s3 tail at BC(0.15, 0.85)=(115, 285) — hooks
DOWN-RIGHT via MR belly, whereas 犭's belly should hook DOWN-LEFT
(mirror-of-犬). Belly bulges right when it should sweep left.
**Fix**: reposition s3 tail to BL (not BC) so belly hooks correctly;
reverse belly control so shape looks like 犬-radical's 弯 downstroke
(mirror-flipped). Cool-down 50 items.

---

# Batch B2 — main-item FAILs (30 items)

Format: item, human FAIL diagnosis, SELF_CHECK calibration, fix idea.

## p2_radical_070_纟 (FAIL)
**Attempt**: two draw_pie_zhe stacked + one draw_ti. All anchors kept
in tall isolated bands.
**Failure mode**: Both 撇折 use tall pie segments in isolation rather
than compact stacked 幺 units — reads as scattered zigzags. s3 提 far
right, disconnected from folds.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: compact both 撇折 (~<60 px each), stack tightly along x=0.35
with pivots in same column; s3 提 head directly under s2 tail,
sweeping up-right. Model after `yao_small.py` (幺).

## p2_radical_075_夕 (FAIL)
**Attempt**: draw_pie + draw_heng_pie + draw_dian. s2 corner at
C(0.85, 0.40).
**Failure mode**: s2 heng too long relative to pie sweep; GT has short
heng shoulder then large pie sweep.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: shorten s2 heng (corner at C(0.55, 0.35)); lengthen pie tip.

## p2_radical_081_夂 (FAIL)
**Attempt**: draw_pie s1 tiny + draw_pie s2 (head TC(0.85, 0.75)) +
draw_na s3 with P-cross near C.
**Failure mode**: s2 head BELOW s1 tail; s3 starts INSIDE pie body →
cross reads as overlap not proper X.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s2 head TC(0.35, 0.10) → BL(0.10, 0.90); s3 head attaches ON
s2 body mid, sweeps to BR corner.

## p2_radical_082_子 (FAIL)
**Attempt**: draw_heng_pie top curl + draw_wan_gou centered + draw_heng
middle.
**Failure mode**: 弯钩 body too centered/vertical without characteristic
子 belly curve; top curl (s1 head at TL(0.55, 0.55)) sits too low.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: raise s1 head to TL(0.55, 0.20); s2 belly x further right in
C; hook_pt further left so tip sweeps well up-left.

## p2_radical_084_夊 (FAIL — drawer flagged overall_pass=False)
**Attempt**: s1 straight vertical (should be curled), s2 too vertical,
s3 disconnected (~102 px from s1). Drawer honestly flagged.
**SELF_CHECK vs human**: AGREE (positive calibration).
**Fix**: draw s1 as small ク-shape at top-center; s2 head just below
s1 tail with N-gap ~15 px; s3 head T-welds s1 body at (~90, 150).

## p2_radical_085_贝 (FAIL)
**Attempt**: MMH-verbatim: draw_shu left + draw_heng_zhe top+right +
draw_pie inner + draw_dian right.
**Failure mode**: TR9 not applied — frame compressed to upper-middle
(y=79 to 232). Long BL pie + tiny 点 read as disjoint pieces.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: TR9 span expansion — frame TL(0.2, 0.15) → BL(0.2, 0.60);
shorten s3 pie so it exits just below frame; enlarge s4 dot.

## p2_radical_086_比 (FAIL)
**Attempt**: MMH raw anchors — draw_ti + draw_shu + draw_pie +
draw_shu_wan_gou. J1 26.9px vs expected 14.9; J2 33.6px vs 17.2.
**Failure mode**: MMH under-spans → 比 doesn't split into two
symmetric halves. s4 up-flick tiny (blob hook).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: TR9 — left half x∈[0.1, 0.5], right half x∈[0.55, 0.95];
ensure s4 has visible vertical descent and clear hook flick.

## p2_radical_088_长 (FAIL)
**Attempt**: s3 drawn as curved zigzag (quad_bezier TC→C→BL), s1 短撇
at TR (should be upper-left).
**Failure mode**: s3 should be strict 竖提 (straight vertical + 提
flick), not curved. s1 in wrong quadrant.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s3 = straight 竖 TC→BC + short 提 flick. Reuse `shu_ti.py`.
Move s1 to TC(0.55, 0.20) → ML(0.65, 0.40).

## p2_radical_090_歹 (FAIL — drawer flagged overall_pass=False)
**Attempt**: s3 drawn as straight pie DOWN-RIGHT, s4 tiny dot.
**Failure mode**: s3 should be 横撇 (short heng + pie down-LEFT), not
straight pie down-right. Interior 夕 structure absent.
**SELF_CHECK vs human**: AGREE (positive calibration).
**Fix**: replace s3 with `heng_pie.py` (short heng + pie down-left);
s4 as proper 点 inside the wedge below s3.

## p2_radical_091_斗 (FAIL)
**Attempt**: two 点 in upper-left corner; long 竖 TC→BC; horizontal at
y=175.
**Failure mode**: two dots should flank vertical near top of 十 cross,
not stack in upper-left corner. Horizontal too low.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: dots flank vertical at y=100–120 (ML(0.6, 0.4) and C(0.1, 0.2));
raise 横 y so 竖 crosses at mid.

## p2_radical_092_厄 (FAIL)
**Attempt**: 厂 frame + inner 横折 at C(0.00, 0.15)→C(0.95, 0.15)→C(0.95,
0.95) + shu_wan_gou hook.
**Failure mode**: inner 㔾 placed entirely in C — should be in MR
(lower-right) inside 厂 enclosure. Hook flick only ~20 px (blob).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: inner 㔾 in MR cell; s4 belly extending down; enlarge hook
flick to ~40 px upward.

## p2_radical_093_方 (FAIL)
**Attempt**: dot + heng + 横折钩 in MR/BR only + pie.
**Failure mode**: 横折钩 body descends only 20 px — compressed to right
column, no visible vertical drop.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: extend 横折钩 vertical (corner MR(0.65, 0.55), tail BR(0.65,
0.75), tip BC(0.65, 0.55)); ensure visible descent + up-left hook.

## p2_radical_094_风 (FAIL)
**Attempt**: pie left wall + custom 横斜钩 + inner 撇/捺 crossing.
**Failure mode**: 横斜钩 hook_pt at BR(0.55, 0.40) → right descent
only slight slant, not full-height enclosing wall. s4 essentially
straight 10-px bar (should be 捺).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: push hook_pt down to BR(0.50, 0.80); s4 as proper 捺
(peak_width toward tail); enlarge enclosure x∈[70, 280], y∈[100, 260].

## p2_radical_096_戈 (FAIL)
**Attempt**: xie_gou main + tilted 短横 + pie + dot upper-right.
**Failure mode**: s1 短横 strongly TILTED (rise ~35 px over 120 px) —
TR8 rule 5 violation. s3 pie starts INSIDE xie_gou body.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: flatten s1 (ML(0.5, 0.55) → C(0.75, 0.45), both in M-row);
s3 crosses s2 at true mid; move dot higher and right (TR(0.5, 0.3)).

## p2_radical_097_户 (FAIL)
**Attempt**: dot + heng + custom inline 横折-like right bump + pie.
**Failure mode**: s3 as tiny inline bump doesn't look like 户's
characteristic 尸-portion. s2 and s4 share the same head anchor (should
have 15 px gap).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: replace s3 with proper 横折 spanning wider to form full 尸
shape; separate s4 head from s2 head by ~15 px.

## p2_radical_098_火 (FAIL)
**Attempt**: dot + short right pie + main pie + na. J1 gap ~55 px.
**Failure mode**: MMH-verbatim s3 and s4 heads ~70 px apart — no shared
apex for 人-base. Reads as scattered strokes, not compact 人 + upper
dots.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s3 head and s4 head SHARE apex point near TC(0.5, 0.5); s3
sweeps down-left, s4 down-right symmetrically. Reuse `ren.py` pattern
+ two upper dots.

## p2_radical_099_旡 (FAIL)
**Attempt**: tiny top 横 + diagonal middle 横 + pie + custom
shu_wan_gou.
**Failure mode**: s1 top 横 tiny (~10 px wide). s2 noticeably tilted.
s3 pie starts at mid-canvas (should be near top). All strokes fail
TR8 rule 5.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: enlarge s1 (spanning TC→TR at y=0.5); s3 head at TC(0.6, 0.1)
so pie starts near top and crosses mid 横.

## p2_radical_100_见 (FAIL)
**Attempt**: small eye-box (y=20–155) + two legs (pie down-left,
shu_wan_gou down-right, heads 25 px apart).
**Failure mode**: box compressed to upper half. Legs don't splay from
opposite bottom corners.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: enlarge box y∈[20, 180]; move s3 head to left edge of box
(ML(0.9, 0.7)); s4 head to right edge.

## p2_radical_101_斤 (FAIL)
**Attempt**: MMH-verbatim two pie + tilted heng + shu right of center.
**Failure mode**: TR9 not applied — everything crammed right of center.
Character asymmetric.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: TR9 span expansion — s1 short pie at top-center only; s2 main
pie TC(0.9, 0.3) → BL(0.3, 0.9); s3 flat horizontal ML→MR; s4 竖 at
x=0.7 spanning M→B rows.

## p2_radical_102_耂 (FAIL)
**Attempt**: short top 横 + short 竖 (~100 px) + long 横 + long pie.
**Failure mode**: s2 vertical too short (100 px) relative to 220-px
horizontal below. 十 cross undersized.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: lengthen s2 vertical to y∈[30, 180]; extend s1 top 横 wider
than 竖's x-travel.

## p2_radical_105_肀 (FAIL)
**Attempt**: custom 2-fat_line top piece + two horizontals + long 竖
at x=145.
**Failure mode**: top piece a small bump, not 聿-top 横折 shape. Spine
竖 not centered on horizontals ([20, 285]).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: replace s1 with proper 横折 primitive; align spine 竖 x with
horizontals' mid (~150).

## p2_radical_107_爿 (FAIL)
**Attempt**: custom curved variable-width strokes — s1 upper-left
bump, s2 slanted "vertical" TC(0.85, 0.55)→BR(0.05, 1.0), s3 提, s4
horizontal.
**Failure mode**: s2 drifts 80 px in x — TR8 rule 6 violation. s4
horizontal when MMH s4 is a descender (wrong stroke class).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: straighten s2 to constant x; s4 as descender not horizontal;
shorten s3 提 span.

## p2_radical_109_攴 (FAIL — drawer flagged overall_pass=False)
**Attempt**: shu top + short heng + 又 (pie + na). s4 head close to
s3 head → inverted-V (Λ) not X.
**SELF_CHECK vs human**: AGREE (positive calibration).
**Fix**: s4 head UPPER-RIGHT of s3 head (e.g. C(0.20, 0.50) → BR(0.85,
0.95)) so 撇 and 捺 cross around BC. Extend 卜 竖 further down.

## p2_radical_111_气 (FAIL)
**Attempt**: pie + two short heng + custom compound 横折弯钩 with 4
quad_bezier segments. J1, J2 gaps 48–84 px.
**Failure mode**: s4 top-heng at same y=155 as s3 → visually overlap.
Three horizontal-like elements stack awkwardly.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s4 top-heng at y=0.35 (C or ML row); extend descent to canvas
bottom; separate s2/s3 to distinct rows (y=0.35 and y=0.55).

## p2_radical_112_欠 (FAIL)
**Attempt**: MMH-verbatim tiny top pie + heng_gou + pie + na cross
low.
**Failure mode**: MMH under-spans — s1 tiny 20-px sweep upper-left;
base X-cross squished lower-left; hook flick 30 px.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: TR9 — s1 full top span; wider s2 horizontal; enlarge hook
flick; center X-base symmetrically.

## p2_radical_114_日 (FAIL)
**Attempt**: fat_line frame + middle 横 ML(0.85, 0.65)→C(0.50, 0.65)
+ bottom 横 BL(0.85, 0.90)→BC(0.50, 0.90).
**Failure mode**: middle 横 only 65 px wide (frame is ~200) — doesn't
reach right wall. 日 requires middle bar touching both walls.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: extend s3 tail to C or MR so it reaches right wall (x=250);
same for s4 tail.

## p2_radical_115_氏 (FAIL)
**Attempt**: pie s1 + custom variable-width s2 sweeping RIGHT +
draw_ti s3 + xie_gou s4.
**Failure mode**: MMH s2 sweeps down-and-RIGHT (contra canonical 撇
which is down-LEFT). 提 flick into 斜钩 body — congested middle.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: override MMH — s2 should sweep down-LEFT (head TR(0.5, 0.2) →
tail BL(0.5, 0.9)); reposition 提 outside the tangle.

## p2_radical_116_礻 (FAIL)
**Attempt**: dot + heng_pie + shu C(0.55, 0.55)→BC(0.50, 0.95) + dot.
**Failure mode**: stem starts INSIDE the 横撇 sweep area; stem only
~140 px tall — reads as short bump under top piece.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: extend stem upward (head at C(0.55, 0.35)); shorten 横撇
horizontal so corner sits closer to center; two 点 flank stem
symmetrically.

## p2_radical_117_手 (FAIL)
**Attempt**: MMH-verbatim top pie + two tilted heng + custom 竖钩 with
head TC(0.389, 0.92)→hook_pt BC(0.09, 0.85) (drifts 30 px left).
**Failure mode**: 竖钩 body not vertical (TR8 rule 6 violation).
Horizontals tilted UP. All compressed.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: straighten 竖钩 (head.x = hook_pt.x = 139); TR9 span-expand
horizontals; reduce tilt.

## p2_radical_118_殳 (FAIL)
**Attempt**: custom curved s1 DOWN-RIGHT + s2 up-right + pie + na cross
at bottom.
**Failure mode**: s1 wrong direction (should sweep down-LEFT). s2
resembles hyphen, not 几-hook. X-cross disconnected from top.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s1 as short 撇 down-left; s2 as real 横折弯 hooking down-right
then turning; ensure top piece welds/attaches to 又 top.

---

# Bootstrap-era item still in errata (retry cool-downs)

## p2_radical_062_犭 — see "Batch B2 — retry outcomes" section above
Bootstrap-era diagnosis (P-cross needs shared pixel, N-joint on curved
spine needs derived anchor) rolled into B2 retry entry at retry_n=1.
The derived-anchor pattern was applied but belly direction was wrong
(bulges right when it should sweep left mirror-of-犬).

---

# Batch B3 — retry outcomes (B2 retry-failures)

## p2_radical_025_力 (RETRY PASS at retry_n=1) — graduated to Success Bank (`li.py`)
Fix that worked: MMH-literal head at TC(0.4, 0.671) — 撇 head sits above
the top-bar (upper-mid), not welded upper-LEFT as the old B1 errata
guessed. 撇 crosses through descent naturally (P at C).

## p2_radical_061_女 (RETRY PASS at retry_n=1) — graduated to Success Bank (`nv.py`)
Fix that worked: lift 撇点 head to TC(0.35, 0.20), push pivot to
C(0.30, 0.85), widen 横 at y≈0.60. 3 joints P-welded correctly. Fills
form_catalog "known gap" for 撇 in 女.

## p2_radical_114_日 (RETRY PASS at retry_n=1) — graduated to Success Bank (`ri.py`)
Fix that worked: extend middle+bottom 横 wall-to-wall (ML→MR / BL→BR)
per prior errata. Enclosure now closes properly.

## p2_radical_003_丿 (RETRY FAIL — retry_n=2)
**Failure mode**: Third attempt still soft-interprets the errata —
did not use head=('TR', 0.85, 0.15), tail=('BL', 0.15, 0.85) verbatim.
**Fix (unchanged, follow LITERALLY)**: TR9 anti-diagonal span,
head_width=16, curve=0.15. Cool-down 50 items. If retry_n=3 still
fails, escalate to sandbox as chronic literal-instruction violation.

## p2_radical_015_刀 (RETRY FAIL — retry_n=2)
**Failure mode**: Joint welding correct but proportion balance still
off — the fix chain (shorten 横, lengthen 竖 descender, moderate pie)
has been suggested but not adopted whole. Cool-down 50 items.

## p2_radical_024_冂 (RETRY FAIL — retry_n=2)
**Failure mode**: Frame proportion still tall vs canonical; s1/s2 y
still misaligned at top-left. **Fix**: hard-align s1 head y with s2
top-bar y both at y=15; reduce frame width to ~230; use `_shorten`
helper to keep corner clean. Cool-down 50 items.

## p2_radical_047_飞 (RETRY FAIL — retry_n=2)
**Failure mode**: Top compound piece STILL chained beziers (drawer
keeps splitting). **Fix**: force ONE call to `stroke_variable_width`
with 5-6 polyline points, no bezier splitting. Cool-down 50 items.

## p2_radical_050_弓 (RETRY FAIL — retry_n=2)
**Failure mode**: 3-tier separation still failing; middle-tier joins
not clean. Cool-down 50 items.

## p2_radical_053_己 (RETRY FAIL — retry_n=2)
**Failure mode**: 3-tier compositional joins still off. Cool-down 50 items.

## p2_radical_058_马 (RETRY FAIL — retry_n=2)
**Failure mode**: Top-box/spine proportion not canonical; drawer
didn't leverage `shu_zhe_zhe_gou.py` as suggested. Cool-down 50 items.

---

# Batch B3 — main-item FAILs (21 items)

Format: item, human FAIL diagnosis, calibration, fix idea.

## p2_radical_119_水 (FAIL)
**Failure mode**: 3-drop 水 structure lost — likely wrong stroke
decomposition (should be 竖钩 + 左小撇 + 右小撇 or similar 4-stroke pattern).
**Fix**: use 竖钩 spine + two flanking short 撇 + short 捺. Reference
GT to confirm the exact stroke pattern.

## p2_radical_120_瓦 (FAIL)
**Failure mode**: Tile-shape displaced. **Fix**: 4-stroke composition
with top 横 + interior 折 + bottom hook — needs form_catalog entry.

## p2_radical_124_文 (FAIL)
**Failure mode**: 亠-top + X-body composition. Drawer cited
form_catalog but the base 撇+捺 X apex still not shared-pixel.
**Fix**: enforce shared-pixel P at X apex (joint_atlas P rule).

## p2_radical_125_毋 (FAIL)
**Failure mode**: Enclosure + internal strokes displaced.
**Fix**: TR9 span expansion + hard-anchor cross bars to span the frame.

## p2_radical_127_牙 (FAIL)
**Failure mode**: 4-stroke fang/tooth composition — component-placement
error. **Fix**: study MMH stroke order more carefully; enforce spine 竖钩
at right column.

## p2_radical_130_月 (FAIL)
**Failure mode**: Enclosing frame under-spanned (TR9 not applied)
or inner bars misaligned. **Fix**: use enclosing anchor conventions
(TR2/TR9) — like `men.py` but with two inner horizontals ML→C span.

## p2_radical_131_爫 (FAIL)
**Failure mode**: Claw radical — 4 small pie-like strokes displaced.
**Fix**: 4 evenly-spaced short strokes in T-row, each slanting slightly
different directions. Reference `zhao_claw` if it exists (none in B2 bank yet).

## p2_radical_132_支 (FAIL)
**Failure mode**: 十 top + 又 base — base X likely fragmented.
**Fix**: use `shi_ten` for top + p3_char_bank.draw_p3_you for base
(with shared-pixel P at base X).

## p2_radical_134_爪 (FAIL)
**Failure mode**: Claw radical (similar to 爫) — displaced strokes.
**Fix**: 4-stroke splayed pattern; keep all heads in T-row.

## p2_radical_135_无 (FAIL)
**Failure mode**: 无 = 一 + 尢-shape. Likely bottom 竖弯钩 leg misaligned
or top 横 tilted. **Fix**: reuse `wang_lame.py` (尣) base + 一 top,
enforce same-row 横.

## p3_char_0005_丿 (FAIL)
**Failure mode**: MMH-verbatim under-span (TR9 not applied) — same
failure as p2_003 bootstrap and B1 retry. Drawer did not consult
errata OR form_catalog 撇 section.
**Fix (literal)**: head=('TR', 0.85, 0.15), tail=('BL', 0.15, 0.85),
head_width=16, curve=0.15. Cool-down 50 items.

## p3_char_0007_乛 (FAIL)
**Failure mode**: 横钩 too compressed; standalone MMH under-spans.
**Fix**: TR9 expansion — full top-row 横 + hook flick down-left into
mid-canvas.

## p3_char_0011_人 (FAIL — drawer flagged partial)
**Failure mode**: 撇+捺 N-gap 36 px (>25 TR10 limit); apex weld not
achieved. Drawer submitted after 1 revision honestly flagging the
residual gap.
**Fix**: derive S2_HEAD by inverting anchor_to_xy against the s1 撇
body pixel at t=0.31 — same technique as 犭 curved-spine N lesson.
Cool-down 50 items.

## p3_char_0016_乃 (FAIL)
**Failure mode**: 横折折撇 single-bezier can't render two bends;
chord too diagonal.
**Fix**: chain TWO beziers (corner1→belly1→midbend, midbend→belly2→
tail) per drawer's own sandbox note. Cool-down 50 items.

## p3_char_0018_乜 (FAIL)
**Failure mode**: 2-stroke 乜 composition — likely 竖弯钩 body direction
wrong or top piece detached.
**Fix**: study GT; likely mirrors 乙 with a horizontal top stub.

## p3_char_0021_几 (FAIL — drawer flagged tension)
**Failure mode**: Tension between TR10 (~25 px cap) and 几's visible
N-gap (~15-20 px). Drawer's revision closed to gap≈6 px which fused
into closed rectangle.
**Fix**: for 几-family, allow ~18 px gap at top; DO NOT weld even to
satisfy TR10 borderline. Keep knee y around 0.85-0.90 not ≥0.95.
Cool-down 50 items. **New sandbox rule**: TR10 exception for 几-family
top gaps.

## p3_char_0023_九 (FAIL)
**Failure mode**: 撇 + 横折弯钩 — body direction or hook angle wrong.
**Fix**: similar structure to 几 but with 撇 head at TC/TR; enforce
hook flicking UP-and-LEFT at end.

## p3_char_0025_力 (FAIL — main-batch attempt at char level)
**Failure mode**: Same failure family as B1 p2_025_力 main — 撇
placement or top-bar span off. But p2_025_力 retry PASSed in B3, so
the drawer should have retrieved `li.py` from the bank.
**Fix**: reuse `li.py` (just promoted). Drawer skipped bank retrieval.
Cool-down 50 items.

## p3_char_0026_冂 (FAIL)
**Failure mode**: Enclosure TR9 not applied — same failure as
p2_024 冂 bootstrap. Drawer didn't cite errata or form_catalog
enclosing section.
**Fix**: TR9 override — cells span 0.05-0.95 both x and y; use
p2_024 errata anchors literally. Cool-down 50 items.

## p3_char_0028_冖 (FAIL)
**Failure mode**: Horizontal cover — likely too short or corner missing.
**Fix**: 冖 = short 点-like head + horizontal + short right-drop.
Use heng_gou_cover.py if it exists (bank has it).

## p3_char_0032_凵 (FAIL)
**Failure mode**: 凵 bracket — 3-stroke composition likely misjoined;
drawer cited joint_atlas but N-gaps still off.
**Fix**: 凵 = left 竖 + bottom 横 + right 竖 (all N-joints, small gap).
Enforce same-col for verticals (TR8 rule 6) and same-row for bottom.
Cool-down 50 items.
