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

## p2_radical_039_艹 (RETRY PASS at retry_n=1, B4) — graduated to `cao_grass_radical.py`
Fix that worked: two straight 竖 (not diagonals) piercing single wide 横;
verticals column-share (TR8 rule 6). Bank + form_catalog + errata all
consulted via mandatory checklist.

## p2_radical_070_纟 (RETRY FAIL — retry_n=2, B4)
**Failure mode**: Two 撇折 loops STILL merged into one long staircase.
Drawer flagged overall_pass=False and revised, but the two loops did not
separate visually — top loop and middle loop overlap in y-range.
**Fix**: hard-enforce distinct y bands — top 撇折 tail y ∈ [80, 130];
middle 撇折 tail y ∈ [150, 210]. Set the two pivot cells to DIFFERENT
rows: top pivot in ML/C, middle pivot in C/BC. Cool-down 50 items.

## p2_radical_081_夂 (RETRY FAIL — retry_n=2, B4)
**Failure mode**: Still the same X-cross topology problem. Drawer used
MMH verbatim but s3 (捺) head sits INSIDE the pie body rather than
tangent-touching. Chronic pattern from B2: derived-anchor on curved
body not applied.
**Fix (LITERAL)**: precompute s2 pie body pixel at t=0.35 (~px 130, 130);
place s3.head at that pixel via inverse anchor_to_xy. Same derived-anchor
technique as 犭 curved-spine N-joint. Do NOT use static ('C', ...)
anchor for the tangent. Cool-down 50 items.

## p2_radical_082_子 (RETRY FAIL — retry_n=2, B4)
**Failure mode**: 弯钩 body still not showing 子's characteristic BELLY
curve — reads as too vertical/centered. B2 errata fix (raise s1 head,
push belly right, hook_pt left) was applied only partially.
**Fix (LITERAL)**: s1 head=('TL', 0.55, 0.20); s2 head=('TC', 0.45, 0.20),
belly=('C', 0.65, 0.60) [push right hard], hook_pt=('BC', 0.25, 0.70)
[far left], tip=('BC', 0.35, 0.35) [up-left]. Do NOT symmetrize.
Cool-down 50 items.

## p2_radical_084_夊 (RETRY FAIL — retry_n=2, B4)
**Failure mode**: ク-shape top piece still rendered as near-straight
short stroke; T-weld between s3 head and s1 body still 60+ px off.
Same failure mode as B2 bootstrap.
**Fix (LITERAL)**: s1 as quad_bezier from TC(0.50, 0.10) → belly TC(0.70, 0.35)
→ tail ML(0.25, 0.55) — a real curl. Then s3.head at ('C', 0.05, 0.15)
so it lands exactly on s1's body pixel around t=0.7. Cool-down 50 items.

---

# Batch B4 — main-item FAILs (19 items)

Format: item, human FAIL diagnosis, calibration, fix idea.

## p3_char_0035_丁 (FAIL)
**Failure mode**: 2-stroke composition (heng + shu_gou) — likely N-gap
at joint too large OR shu_gou body not vertical (TR8 rule 6 violated).
**SELF_CHECK vs human**: DISAGREE — overall_pass=True.
**Fix**: enforce shu_gou head.x == hook_pt.x (both at column-C, x_frac=0.5);
heng full-width ML(0.10,0.5)→MR(0.90,0.5); shu head touches heng
underside near mid (T-weld at C(0.5, 0.5)).

## p3_char_0038_匕 (FAIL)
**Failure mode**: reused `bi.py` (mastered radical) but Phase-3 char
context needs stronger belly on the 竖弯钩. Silhouette compressed.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: override bi.py's s2 belly outward — belly=('C', 0.70, 0.60)
so the wan bulges wider; TR9 span for standalone char use.

## p3_char_0039_之 (FAIL)
**Failure mode**: 3-stroke composition (dian + heng_pie-short + ping_na)
— the 平捺 bottom sweep did not flatten enough vs the middle heng-pie.
Also revised curve from 0.10→0.30 was too aggressive.
**SELF_CHECK vs human**: DISAGREE despite revision.
**Fix**: use `chuo_walk.py` or `yin_stride.py` 平捺 primitive for s3;
keep s2 curve at 0.15 (moderate); s3 tail must reach BR corner clearly.

## p3_char_0044_丸 (FAIL)
**Failure mode**: Long pie + crossing heng + shu_wan_gou with two
P-welds — but the shu_wan_gou body direction wrong (should hook the
belly out to the right, not just descend). Similar to 九 confusion.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `jiu.py`-style anchor plan (like 几 with 撇 through);
strong belly curve on wan_gou; interior 点 tucked into the crotch.

## p3_char_0046_久 (FAIL)
**Failure mode**: short pie + long spine pie + na — likely apex not
shared (X-cross fragmentation, same failure as 火/攴).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: force shared-pixel P at apex (compute intersection first,
place both stroke chords through it). Per joint_atlas.md P rule.

## p3_char_0047_也 (FAIL)
**Failure mode**: 3 strokes with s1 crossing s2 & s3 — but s3 drawn
inline as curved bend, and the bend geometry likely wrong (should be
竖弯钩 with hook UP at the end, not just a curve).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `shu_wan_gou.py` primitive for s3 with proper up-flick;
ensure s1 (short pie) sits UPPER-LEFT and crosses s2 body cleanly.

## p3_char_0056_亾 (FAIL)
**Failure mode**: inline strokes with N-class gaps preserved — but 亾
requires the 亡+人 composition to read as one character, not two
disjoint pieces. Fragmentation.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: consult form_catalog for 亡 composition; bottom 人 must share
the base with 亡's bottom-right corner (T-weld, not N-gap).

## p3_char_0058_兀 (FAIL)
**Failure mode**: reused `wu_lame.py` — but that primitive doesn't
match 兀's canonical shape (兀 = 一 + 儿). Wrong bank primitive.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: compose as heng (top) + er_legs.py (儿 body). Reuse `er_legs.py`
with 一 above per TR1. Cool-down 50 items.

## p3_char_0059_么 (FAIL)
**Failure mode**: 3 strokes with N-gap at BR + s2 as pie sweep — but
么 needs the 幺-loop pattern (like `yao_small.py`), not scattered strokes.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `yao_small.py` pattern (pie_zhe loop) + top dot;
ensure loop closes visually.

## p3_char_0060_卂 (FAIL)
**Failure mode**: MMH-verbatim anchors, N + P joints. Drawer flagged
TR10 exception for 几-family style — but the character's silhouette
came out as scattered pieces rather than the 卂 compound-hook shape.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 卂 requires ONE continuous compound stroke (like 飞's top piece).
Inline as one variable-width polyline (per Pattern E in sandbox).
Cool-down 50 items.

## p3_char_0061_与 (FAIL)
**Failure mode**: 3 strokes with s1 tick, s2 compound spine, s3 bottom
heng — revised with hook flick added, but the character's characteristic
"tick + zigzag + horizontal" pattern didn't cohere. Compound spine likely
misjoined.
**SELF_CHECK vs human**: DISAGREE despite revision.
**Fix**: compose as small top tick + heng_zhe_zhe_gou spine + bottom heng.
Reuse `heng_zhe_zhe_zhe_gou.py` for spine.

## p3_char_0064_叉 (FAIL)
**Failure mode**: 撇 + 捺 + 点 with P at BC — but the P-weld apex not
shared-pixel (fragmentation). Interior 点 also placed too high.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: compute apex intersection first; place 点 BELOW the apex in
the crotch (per 寸 lesson from B1). Reuse `you.py` (又) or `p3_char_bank.draw_p3_you`
pattern.

## p3_char_0065_及 (FAIL)
**Failure mode**: revised once with s2 simplified to 横+竖+撇 (3
sub-segments). But 及 requires a proper 横折折撇 compound stroke, not
three separate pieces. Same failure as B2 stroke 29.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `heng_zhe_zhe_zhe.py` primitive for s2 (compound stroke);
do NOT decompose into pieces. Reference B2 stroke 29 errata.

## p3_char_0070_夂 (FAIL)
**Failure mode**: MMH verbatim — s1.mid ⇆ s2.head N-gap ≈57px (way
over 25px TR10 threshold). Drawer's own SELF_CHECK notes flagged this
but overall_pass=True anyway. Rubber-stamp.
**SELF_CHECK vs human**: DISAGREE despite explicit numeric warning
in notes.
**Fix**: same derived-anchor technique as p2_081_夂 retry fix —
precompute s2 pie body pixel at t=0.35, place s3.head there.

## p3_char_0072_夊 (FAIL)
**Failure mode**: same as p3_070 — 3-stroke ク+X composition, but ク
top piece rendered as near-straight; T-weld to s1 body missed.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: s1 must be a real curl (quad_bezier with belly outside chord);
s3.head derived from s1 body pixel via inverse anchor_to_xy.

## p3_char_0073_飞 (FAIL)
**Failure mode**: revised for flatter horizontal opening + wan-curved
descent + up-flick — but STILL chained bezier segments, not ONE
polyline. Chronic — same failure as p2_047_飞 retry_2.
**SELF_CHECK vs human**: DISAGREE.
**Fix (LITERAL)**: single `stroke_variable_width` polyline call with
5-6 points describing the compound sweep. NO bezier chaining. Marks
placed INSIDE the arc envelope, not overlapping the arc line.
Cool-down 50 items.

## p3_char_0076_孓 (FAIL)
**Failure mode**: revised once with heng_pie curl + wan_gou body + ti
crossing at BC — but the ti direction is wrong (孓's flick is TOP-right
extension, not standard ti). Also body geometry may not match.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: study GT; use heng_pie for top curl, wan_gou for main body,
horizontal 提 crossing at upper mid (not bottom).

## p3_char_0081_女 (FAIL)
**Failure mode**: reused `draw_nv` (mastered radical) but Phase-3 char
context differs — the pie 撇 slightly straighter and the composition
compressed. Char-vs-radical distinction not applied.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: for Phase-3 char 女, expand horizontal 横 span to full ML→MR
(not the tighter radical span); allow 撇 pie curve=0.13; lift the
撇点 head slightly further.

## p3_char_0083_才 (FAIL)
**Failure mode**: 3 strokes 横 + 竖钩 + 撇 with P-weld at C — but the
撇 head placement (near C, N-gap ~15px) may have been too high or too
right; 才's 撇 comes off the crossing point going down-left prominently.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 撇 head shares anchor with 竖钩 body at ~C(0.5, 0.55) via
T-weld (not N-gap). Then 撇 sweeps to BL(0.10, 0.85) with strong curve.

---

# Batch B5 — retry outcomes (B4 retry-failures + new-retry set)

## Chronic cluster — SUPPLANTED at position 300

The 5 items below reached retry_n=3 in B5. Free-form retries have
failed for 4 batches. Their errata fixes were literally applied by
compliant drawers and still lost the panel test (see 马 retry_2). At
position 300 the curator promoted hand-written canonical primitives
to `success_bank/code/chronic/`. These items are NO LONGER on the
active retry list — future attempts should call the canonical
primitive rather than re-render from anchors.

### p2_radical_003_丿 (retry_n=3, SUPPLANTED)
**Retry-3 attempt**: drawer QUOTED the errata anti-diagonal fix in
docstring, then wrote `head=('TC',0.65,0.10) tail=('BL',0.55,0.90)`
with the comment "GT shows a more vertical sweep." Willful override.
**Supplanted by**: `chronic/pie_radical.py` — call `draw_pie_radical(draw)`
with the anchors baked in. No drawer tuning window.

### p2_radical_015_刀 (retry_n=3, SUPPLANTED)
**Retry-2 attempt in B5**: T-weld held but 横 still too long / 撇 sweep
still too extreme. **Supplanted by**: `chronic/dao_char.py`.

### p2_radical_024_冂 (retry_n=3, SUPPLANTED)
**Retry-2 attempt in B5**: frame proportion still not canonical;
top-left corner alignment still off. **Supplanted by**:
`chronic/jiong_frame.py` (230×210 frame, TR9 span, strict verticals).

### p2_radical_050_弓 (retry_n=3, SUPPLANTED)
**Retry-2 attempt in B5**: 3-tier separation attempted with distinct
rows but bottom-tier bowl still misjoined. **Supplanted by**:
`chronic/gong_bow.py` (bottom tier hand-written with leftward sweep
+ up-right hook; stock `shu_zhe_zhe_gou.py` cannot be reused because
it asserts heng goes right, wrong for 弓).

### p2_radical_058_马 (retry_n=3, SUPPLANTED)
**Retry-2 attempt in B5**: mechanically perfect — TR8 col-share, TR9
span, 9 pre-render asserts, shu_zhe_zhe_gou reuse. Still FAILed panel.
Best evidence that mechanical compliance can hit the synthesis
ceiling. **Supplanted by**: `chronic/ma_horse.py`.

## New-retry set (retry_n=1 → retry_n=2, active)

### p2_radical_088_长 (retry_n=2)
**B5 retry_1 attempt**: s3 rendered as curved zigzag again, not
strict 竖提 (straight vertical + 提 flick). Drawer noted the errata
fix but tuned the 提 curve.
**Fix (literal for retry_2)**: s3 head=('C', 0.55, 0.30), s3
knee=('BC', 0.55, 0.85), s3 tip=('BR', 0.35, 0.55). Column-share
head→knee, then flick up-right. Use `shu_ti.py` VERBATIM (no local
tuning). Cool-down 50 items.

### p2_radical_093_方 (retry_n=2)
**B5 retry_1 attempt**: 横折钩 still compressed to right column;
descent too short. Drawer added its own belly to the 横折钩 body.
**Fix (literal for retry_2)**: heng_zhe_gou corner=('MR', 0.65,
0.55), tail=('BR', 0.65, 0.75), tip=('BC', 0.65, 0.55). NO added
belly; use `heng_zhe_gou.py` as-is. Cool-down 50 items.

### p2_radical_100_见 (retry_n=2)
**B5 retry_1 attempt**: eye-box enlarged per errata, but s4 竖弯钩
head positioned at C(0.40, 0.80) — inside box, not on right wall.
GT clearly shows s4 head anchored to right side of box interior.
**Fix (literal for retry_2)**: s4 head=('MR', 0.30, 0.80) (right
side of box); s4 hook_pt=('BR', 0.30, 0.60); s4 tip=('BR', 0.25,
0.25) up-flick. Cool-down 50 items.

### p2_radical_111_气 (retry_n=2)
**B5 retry_1 attempt**: horizontal stack (s2/s3/s4) still overlapping
at same y. Compound 横折弯钩 still chained beziers not one polyline.
**Fix (literal for retry_2)**: distinct y-bands: s2 y=0.35, s3 y=0.55,
s4 y=0.15. Compound spine as ONE `stroke_variable_width` polyline.
Cool-down 50 items.

### p2_radical_124_文 (retry_n=2)
**B5 retry_1 attempt**: apex P still not shared-pixel (fragmentation
at X-cross). Drawer computed anchors independently instead of shared
tuple.
**Fix (literal for retry_2)**: define `APEX = ('BC', 0.50, 0.30)`;
pass IDENTICAL tuple to both pie head and na head. Bezier controls
also derived from apex. Cool-down 50 items.

### p2_radical_135_无 (retry_n=2)
**B5 retry_1 attempt**: 尢-base 竖弯钩 body direction still wrong;
top 一 tilted (TR8 rule 5 violation).
**Fix (literal for retry_2)**: reuse `wang_lame.py` UNCHANGED for the
尢 base + `heng.py` with row-lock for top 一. NO customization of
the base. Cool-down 50 items.

---

# Batch B5 — main-item FAILs (24 items)

Format: item, human FAIL diagnosis, calibration, fix idea.

## p3_char_0085_马 (FAIL)
**Attempt**: heng_zhe top-box + shu_zhe_zhe_gou spine + heng bottom
(3 strokes as spec). Drawer flagged near-weld override at j1.
**Failure mode**: same chronic 马 pattern — top-box proportion off,
spine descent leans, bottom heng overlaps hook_pt zone.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `chronic/ma_horse.py` — call `draw_ma_horse(draw)` for
the character-level 马 too. Char and radical share the same
canonical shape. Cool-down 50 items.

## p3_char_0086_巛 (FAIL)
**Attempt**: 3 stroke variable-width curves ("chuan-family"). Cited
`chuan_river.py` from B1.
**Failure mode**: curves rendered too vertical; three strokes read as
parallel commas not the flowing 巛 signature (each stroke should hook
distinctly at head + sweep down-right with belly bowing left).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: increase curve to 0.20, ensure heads all in T-row with
spacing 0.25 x_frac apart; tails in B-row with SAME 0.25 x_frac
spacing (parallel offsets). Widen head_w=8 for prominent 顿笔.

## p3_char_0091_乡 (FAIL)
**Attempt**: 3 folds (pie_zhe stacked). Same family as 幺/纟.
**Failure mode**: three folds run together vertically without the
distinct 3-tier stagger 乡 needs.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: force distinct y-bands per fold (top at y=0.20, mid at
y=0.55, bottom at y=0.85). Model after `si_silk.py` but with a THIRD
fold instead of terminal 提.

## p3_char_0096_为 (FAIL)
**Attempt**: 4-stroke composition (点 + 撇 + 横折钩 + 点).
**Failure mode**: 横折钩 body not descending far enough; inner 点
placement scattered.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 为 has 横折钩 with LONG descent (top-third to bottom-third);
inner dot in the belly cavity near BC. Use `heng_zhe_gou.py` with
tail=('BR', 0.30, 0.80).

## p3_char_0097_乌 (FAIL)
**Attempt**: pie + heng_zhe_gou-ish body + horizontal.
**Failure mode**: same chronic 马-family — compound descender body
lacks canonical proportion; middle bar disconnected from spine.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 乌 is similar to 鸟 without the dot — mimic `ma_horse.py`
anchor plan with top-box slightly wider, no bottom horizontal. If
still failing at retry_n=3, promote to canonical.

## p3_char_0098_以 (FAIL)
**Attempt**: 4 strokes for the two-part 以 = 㠯 + 人.
**Failure mode**: right 人 (pie + na) apex not shared-pixel;
fragmentation. Left 㠯 misjoined.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `ren.py` for right half with shared APEX tuple; left
half = short shu + dot. Component composition per B4 lesson.

## p3_char_0099_予 (FAIL)
**Attempt**: 4 strokes — top curl + middle short + shu_gou hook +
horizontal-ish crossbar.
**Failure mode**: 予 needs 3-stroke compound spine (like 子) with
crossbar; drawer split it into 4 pieces losing the compound feel.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: reuse `zi_char.py` (子) shape as base; add crossbar for the
予 mid-heng. Not scattered strokes.

## p3_char_0101_亓 (FAIL)
**Attempt**: 2 heng + 2 shu = 4 strokes.
**Failure mode**: shu spacing wrong — legs too close; heng too short
above 二.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: TR2 top-radical span for 二 (full ML→MR); legs at x_frac
0.30 and 0.70 (well-separated); shu heads T-weld into 二 lower heng.

## p3_char_0103_亢 (FAIL)
**Attempt**: dot + heng + 撇 + 竖弯钩.
**Failure mode**: 竖弯钩 hook flick direction wrong (should be up-right
prominently for 亢); dot placement too high.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `shu_wan_gou.py` with tip explicitly UP-RIGHT of
hook_pt (tip.x > hook_pt.x). Top structure = 亠 (dot + heng).

## p3_char_0104_方 (FAIL)
**Attempt**: dot + heng + inline heng_zhe_gou + pie. Drawer revised
once (added belly).
**Failure mode**: revision made it worse — 横折钩 gained a body
belly, breaking the primitive contract. Descent still short.
**SELF_CHECK vs human**: DISAGREE despite revision.
**Fix**: LITERAL errata — heng_zhe_gou corner=('MR', 0.65, 0.55),
tail=('BR', 0.65, 0.75), tip=('BC', 0.65, 0.55). No added belly. See
retry entry above; on to retry_n=2.

## p3_char_0110_分 (FAIL)
**Attempt**: 4 strokes for 八 + 刀. Top pie + na apex-shared; bottom
刀 as heng_zhe_gou + pie.
**Failure mode**: 八 apex too wide (splayed); 刀 bottom-half compressed.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: apex at TC(0.50, 0.30); 刀 base uses `chronic/dao_char.py`
UNCHANGED for the bottom half.

## p3_char_0111_仇 (FAIL)
**Attempt**: 亻 (ren_side) + 九.
**Failure mode**: 九 compound stroke direction wrong; body slants
where it should curve.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 九 base = short pie + 横折弯钩. Use B4 errata for 九 body
direction (like 几 with 撇 through).

## p3_char_0113_仉 (FAIL)
**Attempt**: 亻 + 几.
**Failure mode**: 几 top gap fused (drawer welded to satisfy TR10,
against the 几-family exception in joint_atlas).
**SELF_CHECK vs human**: DISAGREE.
**Fix**: joint_atlas 几-family exception — keep top gap 15-20 px
VISIBLE. Do NOT weld.

## p3_char_0114_见 (FAIL)
**Attempt**: shu + heng_zhe + pie + shu_wan_gou (4 strokes).
Cited errata + 100_见 fix.
**Failure mode**: eye-box enlarged per errata BUT s4 head positioned
inside box mid (C(0.40, 0.80)) instead of right wall.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: same as 100_见 retry above — s4 head=('MR', 0.30, 0.80).

## p3_char_0118_从 (FAIL)
**Attempt**: 2 × 人 = 4 strokes.
**Failure mode**: two 人 sub-units bunched together; apex-shares not
both P-welded.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: two `ren.py` calls with distinct x_frac bands (left at
0.20-0.45, right at 0.55-0.80); both apex-P-welded independently.

## p3_char_0119_仓 (FAIL)
**Attempt**: 4 strokes — 亽 top (pie + na + heng) + 巴-like bottom.
**Failure mode**: bottom 巴-like piece rendered as scattered strokes,
no enclosing frame feel.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: bottom = mini enclosing frame (short shu + heng_zhe with
hook flicking right). TR9 span for the enclosure per position-150
lesson.

## p3_char_0120_气 (FAIL)
**Attempt**: 4 strokes matching 气 canonical (top pie + two heng +
compound 横折弯钩). Cited errata + p2_radical_111_气 fix.
**Failure mode**: same as p2_111 — horizontals overlap; compound
spine chained beziers.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: same as p2_111 retry_2 — distinct y-bands; ONE polyline
spine.

## p3_char_0121_內 (FAIL)
**Attempt**: 4 strokes — 冂 frame + 入 inside.
**Failure mode**: frame under-spanned; 入 sub-unit apex not
shared-pixel.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: reuse `chronic/jiong_frame.py` for the frame; 入 uses
apex-share tuple.

## p3_char_0122_五 (FAIL)
**Attempt**: 4 strokes — three heng + slanted shu. Drawer cited
verified NOT-a-兀 (correct primitive-pick discipline).
**Failure mode**: slanted s2 doesn't cross s3 at P; the "5" reads as
two disconnected halves stacked.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: shared-pixel P at s2/s3 intersection (see joint_atlas P
rule); enforce s2 chord passes through s3 body.

## p3_char_0123_兮 (FAIL)
**Attempt**: 4 strokes — 八 top + 亅 middle + 一 base.
**Failure mode**: 八 too wide and dropped too low; hook body compressed.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: 八 apex at TC(0.50, 0.20); hook body spans C→BC vertically;
base 一 at y=0.85 spanning ML→MR.

## p3_char_0125_円 (FAIL)
**Attempt**: 4 strokes — enclosing frame + middle short shu.
**Failure mode**: frame proportion off (too tall); middle shu
disconnected from top bar.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: reuse `chronic/jiong_frame.py` scaled slightly narrower
(currently baked); add middle shu with T-weld to top bar.

## p3_char_0130_切 (FAIL)
**Attempt**: 4 strokes — 七 left + 刀 right. Drawer revised once
(increased 竖弯 curvature).
**Failure mode**: 七 sub-unit and 刀 sub-unit both compressed;
overall silhouette lopsided.
**SELF_CHECK vs human**: DISAGREE despite revision.
**Fix**: 刀 sub-unit = `chronic/dao_char.py` UNCHANGED; 七 sub-unit
in left half with heng full-width in ML.

## p3_char_0132_内 (FAIL)
**Attempt**: 4 strokes — 冂 frame + 人-like inner. Drawer revised
once (inner apex moved).
**Failure mode**: same as 内 group — frame under-spanned; inner
apex not shared-pixel.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: `chronic/jiong_frame.py` for frame; `ren.py` for inner with
shared APEX tuple.

## p3_char_0133_冘 (FAIL)
**Attempt**: 4 strokes — 冖 top + 儿-like bottom.
**Failure mode**: 冖 cover misjoined; 儿 legs splayed too far.
**SELF_CHECK vs human**: DISAGREE.
**Fix**: use `mi_cover_char.py` for top; `er_legs.py` for bottom
with tighter x-frac span.

---

# Batch B6 (positions 134-183) — retry outcomes and main FAILs

**Context**: FIRST batch under v8 unlock at position 350. All B6 attempts
happened BEFORE the v8 unlock (drawer prompts had not yet gained the
free-form drawer_memory.md). Retry outcomes are therefore still on the
v7 mechanism.

## Retry outcomes (10 retries; 0 PASS, 4 STALL_DNC, 6 rendered-and-failed)

### p2_radical_086_比 (RETRY FAIL — retry_n=1)
**Attempt**: split 比 into 卜 (left) + 匕 (right). Left half read as an
"H"-shape (two verticals + short crossbar); right became a 乙-like curl.
**Failure mode**: drawer did not reuse the mastered `bi.py` primitive
(promoted at position 43) which already encodes 匕 = 撇 + 竖弯钩. Instead
drew fresh. Also fell into the "compose sub-radicals" trap: 比 is TWO
匕 side-by-side (mirrored), not 卜+匕.
**Fix (LITERAL)**: two calls to `bi.py`, left mirrored. Left half x∈[0.1,
0.45] mirrored; right half x∈[0.55, 0.9] normal orientation. Cool-down
50 items. If retry_n=3 still FAILs → CANONICAL primitive candidate.

### p2_radical_094_风 (RETRY FAIL — retry_n=1)
**Attempt**: pie left wall + horizontal + inner marks. 几-family frame
under-spanned; inner X-mark disconnected from frame.
**Failure mode**: joint_atlas 几-family exception noted, but the OUTER
frame + INNER cross composition never gets both halves talking. Similar
failure mode to 用/内 in this batch.
**Fix**: outer frame = one continuous compound stroke (like flying's
top piece) reaching full canvas span; inner marks INSIDE frame envelope.
Cool-down 50 items.

### p2_radical_116_礻 (RETRY FAIL — retry_n=1)
**Attempt**: 4 strokes attempted but bottom dots absent in final render;
stem short.
**Failure mode**: SELF_CHECK flagged overall_pass=False but drawer
submitted anyway (per rules, only one revision allowed). Chronic
stem-too-short failure — same as B3 diagnosis.
**Fix (LITERAL)**: stem head=('C', 0.55, 0.35), tail=('BC', 0.55, 0.95);
two dots at BC(0.35, 0.65) and BC(0.75, 0.65). Cool-down 50 items.

### p2_radical_119_水 (RETRY FAIL — retry_n=1)
**Attempt**: only 3 strokes rendered; right 捺 missing entirely.
**Failure mode**: stroke count off by one (4 expected, 3 delivered).
Chronic 水 pattern — the right 捺 keeps getting dropped.
**Fix (LITERAL)**: enforce 4-stroke plan: spine 竖钩 center + left 撇 +
right 撇 + right 捺 (na, not another pie). Assert `len(strokes) == 4`
before rendering. Cool-down 50 items.

### p2_radical_045_寸 (RETRY FAIL — retry_n=1)
**Attempt**: 3 strokes 一+亅+丶. Dot landed upper-right corner instead
of the crotch between hook and heng.
**Failure mode**: same as B1 bootstrap diagnosis — 点 placement wrong.
Errata fix (dot at C 0.60, 0.55 → C 0.80, 0.75) was named in the drawer
comment but NOT applied to the anchors.
**Fix**: LITERAL apply of the C(0.60, 0.55)→C(0.80, 0.75) anchor pair.
Cool-down 50 items.

### p2_radical_075_夕 (RETRY FAIL — retry_n=1)
**Attempt**: pie + heng_pie + dot. Heng shoulder still too long relative
to pie sweep. Same failure mode as B2 bootstrap.
**Fix (LITERAL)**: s2 corner=('C', 0.55, 0.35); s2 tail=('BL', 0.20,
0.75). NO extension of the heng shoulder past x_frac 0.55 in C. Cool-down
50 items.

### p2_radical_088_长 (RETRY FAIL — retry_n=3) — CANONICAL PROMOTION CANDIDATE
**Attempt**: 3 strokes merged into an unrecognizable blob — center-heavy,
lost the 长 signature entirely.
**Failure mode**: 3 attempts have failed with different fix chains.
Retrieval-application gap saturated. Promote to `chronic/chang_long.py`
next batch under v8 canonical-promotion permission. Freeze retry_n at 3.

### p2_radical_124_文 (RETRY FAIL — retry_n=2)
**Attempt**: apex X-cross still fragmented (not shared-pixel).
**Failure mode**: literal APEX tuple pattern from B5 errata not applied.
Drawer computed anchors independently.
**Fix (LITERAL)**: `APEX = ('BC', 0.50, 0.30)`; pass IDENTICAL tuple to
both pie head and na head. Cool-down 50 items. If retry_n=3 fails →
CANONICAL.

### p2_radical_081_夂 (RETRY FAIL — retry_n=3) — CANONICAL PROMOTION CANDIDATE
**Failure mode**: X-cross topology still wrong. 3 retries; derived-anchor
pattern was named in errata every time and never applied literally.
**Action**: promote to `chronic/zhi_dive.py` next batch under v8.

### p2_radical_084_夊 (RETRY FAIL — retry_n=3) — CANONICAL PROMOTION CANDIDATE
**Failure mode**: ク top piece still near-straight; T-weld off by 60px.
Same as B4 retry_2. Retrieval-application ceiling reached.
**Action**: promote to `chronic/sui_slow.py` next batch under v8.

## Main-item FAILs (24 items)

### p3_char_0135_刅 (FAIL)
**Attempt**: rendered as X + dot. 刀 body absent.
**Diagnosis**: drawer treated 刅 as "刀 + 丶 + tick" but did not call
`chronic/dao_char.py` for the 刀 base — reinvented it and failed.
**Fix**: call `chronic/dao_char.py` for 刀 base; add tick above at
TR(0.65, 0.30) and dot at TR(0.85, 0.55).

### p3_char_0136_比 (FAIL — main att3)
Same as retry above. Reuse `bi.py` mirrored.

### p3_char_0138_水 (FAIL)
See retry above. 4-stroke enforcement required.

### p3_char_0139_礻 (FAIL)
See retry above. Stem + bottom-dots enforcement required.

### p3_char_0140_反 (FAIL)
**Attempt**: 厂 top + 又 base rendered as two disjoint pieces.
**Diagnosis**: 又 base not sharing anchors with 厂 body — fragmentation.
**Fix**: use `chang.py` (厂 mastered) with T-weld override; then `you_again.py`
(又 mastered) with head sharing 厂 body pixel.

### p3_char_0141_办 (FAIL — main att3)
**Attempt**: 力 + 两点 scattered.
**Diagnosis**: 力 not composed via `li.py`; dots misplaced.
**Fix**: call `li.py` for 力; add two dots at ML(0.30, 0.45) and MR(0.30,
0.45) flanking the descent.

### p3_char_0142_区 (FAIL)
**Attempt**: 匚 frame open + inner X. Frame's top-right corner detached.
**Fix**: use `xi_box.py` (匸 mastered) with clean N at TR corner; inner
乂 via `fu.py`-like apex-share pattern. TR9 span for the frame.

### p3_char_0143_勻 (FAIL — main att3)
**Attempt**: outer 勹 became "7"; inner 二 shifted right.
**Fix**: call `bao_char.py` (mastered) for 勹 outer; center inner 二 at
x_frac 0.45-0.65 within the belly. Do NOT reinvent 勹.

### p3_char_0144_风 (FAIL)
See retry above.

### p3_char_0146_队 (FAIL — main att3)
**Attempt**: left 阝 unrecognizable; right 人 too tall.
**Fix**: call `fu_right.py` (阝-right, promoted at B1) MIRRORED for
left 阝 — or promote a new `fu_left.py` primitive; then `ren.py` for
the right 人 with x∈[0.55, 0.95].

### p3_char_0148_书 (FAIL — main att2)
**Attempt**: 十 + tiny hook + dot; lost compound spine.
**Fix**: use `shu_zhe_zhe_gou.py` (mastered) for the compound spine;
add heng crossing + dot. Reference `xi_practice.py` composition.

### p3_char_0150_引 (FAIL)
**Attempt**: left 弓 collapsed to zigzag.
**Diagnosis**: `chronic/gong_bow.py` was mentioned in the drawer's
comment but NOT imported/called. Fatal — CHRONIC MECHANISM NOT WORKING.
**Fix (LITERAL)**: `from chronic.gong_bow import draw_gong_bow` then
`draw_gong_bow(draw)` for left half; then centered 丨 for the right.

### p3_char_0153_卬 (FAIL — main att2)
**Attempt**: left half 卩-mirror missing; right 卩 stretched.
**Fix**: no mastered 卩; needs new promotion. For now: hand-derive left
half as short 撇 + hook composition; right half as 卩 (short 横折 + 竖).

### p3_char_0155_必 (FAIL)
**Attempt**: dots scattered outside body; reads as 心 with tail.
**Fix**: 必 = 心 body + slanted 撇 through center. Use `xin.py` (心
mastered) + one 撇 crossing.

### p3_char_0156_们 (FAIL)
**Attempt**: 亻 ok; 门 right collapsed to two verticals.
**Diagnosis**: `chronic/jiong_frame.py` mentioned in comments but not
called — same failure mode as p3_char_0150 引.
**Fix (LITERAL)**: `from chronic.jiong_frame import draw_jiong_frame`
then `draw_jiong_frame(draw, offset_x=+50)` for the 门 half; `ren_side.py`
for 亻 in left column.

### p3_char_0158_出 (FAIL — main att1)
**Attempt**: 山 tier structure lost; reads as 廿 with extra vertical.
**Fix**: stack two `shan.py` (山 mastered) instances vertically —
upper 山 y∈[0.15, 0.50], lower 山 y∈[0.55, 0.90]. Column-share centers.

### p3_char_0163_丱 (FAIL — main att1)
**Attempt**: 4 strokes but symmetry broken.
**Fix**: force perfect mirror — left cluster x∈[0.1, 0.45], right cluster
x∈[0.55, 0.9], both using the same anchor plan MIRRORED via x_frac
`1 - x`.

### p3_char_0164_对 (FAIL — main att3)
**Attempt**: 又 became sticks; 寸 dot missing.
**Fix**: call `you_again.py` (又 mastered) for left; then heng + shu_gou
+ dot for 寸 on right.

### p3_char_0166_去 (FAIL — main att2)
**Attempt**: top 土 crammed; bottom 厶 opens right (wrong direction).
**Fix**: call `tu.py` (土 mastered) for top; `si_private.py` (厶
mastered) for bottom; enforce 厶 opens LEFT (its canonical direction).

### p3_char_0168_用 (FAIL — main att2)
**Diagnosis**: frame not calling `chronic/jiong_frame.py`; same failure
family as 156_们, 150_引.
**Fix (LITERAL)**: `from chronic.jiong_frame import draw_jiong_frame`;
add inner spine 丨 + two inner heng (all ML→MR span).

### p3_char_0169_疋 (FAIL — main att2)
**Attempt**: proportions off; base X-cross fragmented.
**Fix**: 疋 = 龰 base + 一 top; enforce base 人-cross uses shared APEX
tuple (per B5 文 pattern).

### p3_char_0170_发 (FAIL)
**Attempt**: no 又 base — top pieces only. Wrong stroke count (5 expected).
**Fix**: force 5-stroke plan; base 又 via `you_again.py`; top mark via
compound 撇折 primitive. Assert stroke count before rendering.

### p3_char_0177_仗 (FAIL — main att3)
**Attempt**: 亻 ok; 丈 base heng too short + 捺 direction wrong.
**Fix**: call `ren_side.py` for 亻; 丈 body = wide heng + 撇 (down-left)
+ 捺 (down-right). Both slanted strokes must share BC apex pixel.

### p3_char_0183_仞 (FAIL — main att1)
**Attempt**: 亻 ok; 刃 has wrong hook direction and misplaced dot.
**Fix**: call `chronic/dao_char.py` for 刃 (刃 = 刀 + inner dot); place
dot at inner (MR, 0.30, 0.50) after the 刀 primitive.

---

# B6 top-level observations (NEW under v8)

**Chronic mechanism is failing silently.** `chronic/pie_radical.py`,
`chronic/dao_char.py`, `chronic/jiong_frame.py`, `chronic/gong_bow.py`,
`chronic/ma_horse.py` were promoted at position 300 as callable
primitives specifically to bypass the retrieval-application gap.
Across ALL batches since (B6): **0 imports, 18 mentions in comments.**
Drawers cite the primitive by name in the comment header and then
write fresh anchors. The mechanism named "no drawer tuning window"
has failed because the drawer prompt does not force an import; it
only makes the file available.

**Fix for B7 under v8**: put the exact import line in `drawer_memory.md`
as a MANDATORY snippet the drawer must include verbatim. See
`drawer_memory.md`.

**Compositional-primitive under-use.** B6 has ~15 items composed of
mastered radicals (仔, 付, 打, 化, 他, 仝, 仕 PASSed via reuse; 反, 队,
去, 对, 仗 FAILed by NOT reusing). The bank's ~90 non-basic primitives
have essentially zero uptake — drawers redraw sub-components from
scratch. See `drawer_memory.md` for the shortlist.

**Multi-part characters remain the failure mode.** All 24 main FAILs
are 3+-part characters where the sub-components don't visually cohere.
Basic strokes (heng/shu/pie/dian) are all fine on their own; joining
them into readable radicals is where B6 breaks.

**Chronic-cluster canonical-promotion candidates for position 400**:
- 长 (retry_n=3 saturated)
- 夂 (retry_n=3 saturated)
- 夊 (retry_n=3 saturated)

Under v8 rule "any retry_n≥2 fail may be promoted to canonical", 比
and 124_文 also qualify at retry_n=2.

---

# Batch B7 (positions 184-233) — 25 main FAILs + retry outcomes

**Context**: BEST G4 batch on mains yet (25/50 = 50%). B7 retries all
FAILed under the v8 prompt (12/12 FAIL), but the SAME 12 items re-run
under the v9 visual-diff prompt produced 2 PASSes (比, 文). See
`evolution.md` position-400 for the v9-prompt rationale and evidence.

## Retry PASSes graduated

### p2_radical_086_比 (RERUN PASS at retry_n=1 v9) — GRADUATED
Fix that worked: MMH-verbatim anchors + explicit LEFT/RIGHT half
decomposition. The v8-prompt retry drew halves too far apart (x=55
and x=250). v9 rerun surfaced this via visual diff, then trusted MMH
anchors verbatim (which are properly centered at x∈[55,145] and
x∈[145,265]). No chronic 匕-mirror primitive was needed — direct
draw_heng + draw_shu_ti + draw_pie + draw_shu_wan_gou at MMH anchors.
Removed from active errata.

### p2_radical_124_文 (RERUN PASS at retry_n=2 v9) — GRADUATED
Fix that worked: shared `CROSS_ANCHOR = ('BC', 0.385, 0.225)` passed
as the MID (not head) for both 撇 and 捺, so the P-weld is pixel-
shared BELOW the heng. Prior retry_2 apex was `('C', 0.50, 0.55)`
right ON the heng, which forced the 人 shape. Visual-diff prompt made
the drawer read prior PNG and see this topology bug. Removed from
active errata.

## Both-fail retries (v8 AND v9) — CANONICAL escalation

### p2_radical_088_长 (retry_n=3 SATURATED, v9 rerun FAIL) — CANONICAL NEXT
Fourth attempt failed. v9 visual diff did not help. Under v8/v9 policy,
promote to `chronic/chang_long.py` in B8. Freeze retry_n at 3.

### p2_radical_081_夂 (retry_n=3 SATURATED, v9 FAIL) — CANONICAL NEXT
X-cross topology fault persists after visual diff. Promote to
`chronic/zhi_dive.py` in B8. Note: this is now the SAME topology-bug
pattern as B7r 文 PASS — a `CROSS_ANCHOR` mid-tuple approach may work
as the canonical anchor plan.

### p2_radical_084_夊 (retry_n=3 SATURATED, v9 FAIL) — CANONICAL NEXT
ク top piece still near-straight; T-weld off ~60 px. Promote to
`chronic/sui_slow.py` in B8.

### p2_radical_119_水 (retry_n=2, v9 FAIL) — CANONICAL NEXT (5th chronic)
Stroke-count assertion STILL not applied — right 捺 still missing.
This is a mechanism failure not a rendering one. Promote to
`chronic/shui_water.py` in B8 with a hard 4-stroke plan baked in.

### p2_radical_116_礻 (retry_n=2, v9 FAIL) — CANONICAL NEXT
Chronic stem-too-short + bottom-dots-missing pattern. Promote to
`chronic/shi_altar.py` in B8.

### p2_radical_094_风 (retry_n=2, v9 FAIL) — CANONICAL CANDIDATE
几-family frame under-spanned again. Promote to `chronic/feng_wind.py`
if it fails a 4th time; for B8, one more retry with explicit-frame-span
literal fix in errata.

### p2_radical_135_无 (retry_n=3, v9 FAIL) — CANONICAL NEXT
Fragmented top piece + curve. Promote to `chronic/wu_none.py`.

### p2_radical_111_气 (retry_n=3, v9 FAIL) — CANONICAL NEXT
Stroke stacking overlap. Promote to `chronic/qi_air.py`.

### p2_radical_045_寸 (retry_n=2, v9 FAIL)
Dot still misplaced (upper-right instead of crotch). Cool-down 50 items.
If retry_n=3 fails → canonical.

### p2_radical_075_夕 (retry_n=2, v9 FAIL)
Heng shoulder still too long. Cool-down 50 items. If retry_n=3 fails →
canonical.

## Main FAILs (25) — one-line diagnoses

### p3_char_0187_仡 (FAIL)
亻 fine; 乞 right-half fragmented. No bank primitive for 乞. Fix: hand
compose 乞 = 𠂉 top + 乙-family hook; keep in right half x∈[0.55, 0.95].

### p3_char_0188_边 (FAIL)
辶 walk-radical present but 力 sub-part misplaced inside the 辶
enclosure. Fix: call `li.py` for 力 inside x∈[0.30, 0.65] first, then
draw 辶 sweeping around it.

### p3_char_0191_仫 (FAIL)
亻 fine; 么 right-half unrecognizable. Fix: call `yao_small.py`
(promoted at B2 for radical 幺) but note the char 么 has an added
initial 撇 above the 幺 body.

### p3_char_0193_癶 (FAIL)
Opposing-legs radical. X-cross topology failure — legs read as
disconnected. Fix: use CROSS_ANCHOR pattern (see drawer_memory.md v9
addendum): both inner strokes routed through a shared BC pixel.

### p3_char_0196_东 (FAIL)
Compound top + 木-base. Top piece not aligned with 木 spine. Fix:
column-share spine — top's centerline x == 木 spine x.

### p3_char_0200_市 (FAIL)
亠 top + 巾 base. 巾 frame too narrow. Fix: 巾 body width = 60% of
canvas, spine centered.

### p3_char_0203_冊 (FAIL)
Two 冂 frames side-by-side. Neither imported `chronic/jiong_frame.py`.
Fix (LITERAL): `from chronic.jiong_frame import draw_jiong_frame`;
call twice with left_offset_x=-40 and right_offset_x=+40 (assuming
chronic supports offset; if not, add support).

### p3_char_0205_冋 (FAIL)
冂 frame + inner 口. Frame not called from chronic (comment said "MMH
narrower than chronic"). Fix: override — trust chronic width; inner
口 via `kou.py` at C x∈[0.30, 0.70].

### p3_char_0207_册 (FAIL)
Same as 冊 (0203). Two-frame layout failing without chronic import.
Fix: same as 0203.

### p3_char_0209_冎 (FAIL)
冂 frame + inner cross. Frame not imported. Fix: `chronic/jiong_frame`
+ inner heng + inner shu shared at C.

### p3_char_0211_冯 (FAIL)
冫 + 马. `chronic/ma_horse.py` not called ("full-canvas primitive
can't host right-half"). Fix: modify chronic/ma_horse to accept an
offset_x/scale param and call it scaled to x∈[0.30, 0.95].

### p3_char_0212_处 (FAIL)
处 = 夂 + 卜. X-cross topology on 夂 head. Fix: CROSS_ANCHOR pattern.

### p3_char_0213_処 (FAIL)
処 = 几 + 夂 variant. Compound composition off. Fix: use `ji.py` (几)
+ inner 夂 with CROSS_ANCHOR pattern.

### p3_char_0214_记 (FAIL)
讠 + 己. `yan_speech.py` fine on left; 己 right-half not in bank and
fragmented. Fix: hand compose 己 as 3-tier per B1 errata fix.

### p3_char_0216_失 (FAIL)
Top 丿 + 天. 丿 not welded to 天's top heng. Fix: T-weld the pie head
to heng's top edge.

### p3_char_0217_凹 (FAIL)
Concave frame. Highly irregular shape. Fix: 5-stroke plan with left
wall + top-U + right wall + bottom heng; enforce concavity via
computed offsets.

### p3_char_0218_刍 (FAIL)
⺈ + 彐 stack. Compositional coherence lost. Fix: reuse
`xue_broom.py` (彐 mastered) for bottom; hand compose ⺈ (short 撇 +
横折) on top.

### p3_char_0220_丢 (FAIL)
丿 + 去. 去 = 土 + 厶. Sub-parts not composed via bank. Fix: pie +
`tu.py` (土) + `si_private.py` (厶).

### p3_char_0221_有 (FAIL)
𠂇 + 月. 月 frame fragmented. Fix: hand 𠂇 (pie + heng crossing) +
inline 月 frame (jiong-like but taller, with 2 inner heng).

### p3_char_0225_而 (FAIL)
Frame + 4 legs. Frame proportion off; legs stagger. Fix: TR9-span
frame + 4 legs column-shared at x∈{0.20, 0.40, 0.60, 0.80}.

### p3_char_0228_乩 (FAIL)
占 + 乚. X-cross-like right side. Fix: CROSS_ANCHOR pattern on the
乚 hook + 占's descending stroke.

### p3_char_0230_亘 (FAIL)
一 top + 日 middle + 一 bottom (bracketed stack). Middle collapsed.
Fix: enforce y-alignment of top/bottom heng; middle 日 fits in
y∈[0.30, 0.70].

### p3_char_0231_会 (FAIL)
人 top + 云 base. 人 apex not welded; 云 base fragmented. Fix:
`ren.py` (人 mastered) with shared APEX tuple + inline 云 base.

### p3_char_0232_亙 (FAIL)
Same family as 亘 (0230). Same fix.

### p3_char_0233_那 (FAIL)
compound-left + 阝-right. 阝-right primitive `fu_right.py` should
have been imported. Fix: `from fu_right import draw_fu_right` +
compose left-half of 那.


---

# B8 (positions 401-450) — 30 main FAILs + 7 retry FAILs

**Batch summary**: 20/50 = 40% mains (down from B7's 50%); 0/7 retries.
Item pool shifted heavily to 亻+X compositional pattern (25 of 50 items
share the 亻 left-radical prefix), producing a synthesis-heavy failure
mode. Chronic import rate on B8 mains: 0/50 imports; 19/50 comment
mentions. Same citation-without-import pathology as B6/B7. The 7 retry
FAILs share a distinct root cause described below.

## Retry FAILs (7) — TERMINAL_FROZEN — root cause: canonical file gap

At position 400, the previous curator QUEUED 7 canonical primitives
(chang_long.py, zhi_dive.py, sui_slow.py, shui_water.py, shi_altar.py,
wu_none.py, qi_air.py) — see scans/scan_position_400.md — but **never
hand-wrote the primitive files**. The `success_bank/code/chronic/`
directory still contains only the original 5 files (dao_char,
gong_bow, jiong_frame, ma_horse, pie_radical).

Retry drawers for 长/夂/夊/水/礻/无/气 had no new primitive to import.
Each fell back to v9 visual-diff + MMH-verbatim + inlined base
primitives (pie, shu, na, heng). Zero PASSes. This is NOT the "AI
cannot follow its own memory pointer" pathology — it is the more
basic "curator queued a canonical promotion and forgot to deliver
the file" pathology. Root cause: curator's own compliance failure at
the previous cycle boundary.

Actions:
- All 7 items marked TERMINAL_FROZEN.
- Removed from B9 retry queue.
- Historical note: to re-attempt, a future curator would need to
  hand-write the 7 canonical primitives (not just queue them) and
  update `drawer_memory.md`'s chronic-imports section to list them.
- Rationale for freeze: after 4 batches of escalation (v7 discipline
  → v8 slim + snippets → v9 visual-diff → v10 trajectory-view) plus
  a queued-but-undelivered canonical promotion, marginal ROI on
  another attempt with the SAME memory state is near zero.

---

## Main FAILs (30) — per-item diagnosis

### p3_char_0236_亥 (亥, 6画)
7 draw calls (over-count by 1). All N-joints — no welding at the
X-cross. Fix: 6 strokes only (亠 + X-cross-below); CROSS_ANCHOR
pattern at ('C', 0.5, 0.55) for the pie+na X in the middle.

### p3_char_0237_行 (行, 6画)
Imports pie/heng/shu; 8 draw calls. 彳 left needs `chi_step.py`
(exists in bank — not imported). Fix: `from chi_step import
draw_chi_step` for left half; right 亍 as heng+heng+shu-hook.

### p3_char_0238_亦 (亦, 6画)
Only 2 draw_calls — most strokes must be inlined or missed. N-gap
at C preserved but body underdrawn. Fix: use dedicated primitives
for each stroke; 亠 top + X-cross-below + flanking dots (4 strokes
in the bottom band).

### p3_char_0239_过 (过, 6画)
Zero bank draw calls (all inline PIL). 辶 走之 is very hard to inline;
should use compound-heng-fold-fold-fold pattern. Fix: promote a
`zou_zhi.py` primitive (走之 as: top-dot + horizontal-fold-fold +
long swooping na). Meanwhile: hand-derive 寸 (inline) + 辶 (careful
compound).

### p3_char_0240_仰 (仰, 6画)
Only 3 draws (needs 6). Imports ren_side + pie/shu/heng. Right side
卬 dropped strokes. Fix: 6-stroke plan: 亻 (2 via ren_side) + 卬 (4
strokes: 撇 + 竖折 + 竖 + hook).

### p3_char_0241_如 (如, 6画)
Imports nv + kou; only 2 draw calls. Left 女 too compressed; right
口 not sitting right. Fix: enforce 女 fills x∈[0.05, 0.45], 口 fills
x∈[0.50, 0.95], y∈[0.30, 0.75]. Both primitives OK — placement wrong.

### p3_char_0242_仲 (仲, 6画)
Imports ren_side only; 1 draw call. Right 中 inlined but likely off.
Fix: also import mastered 口 (`kou`) for the 中-frame; add shu
through center.

### p3_char_0243_成 (成, 6画)
Zero draw_calls (all inline). Note claims P-joints welded at C and
BC. Fix: use `xie_gou` for the ヽ + hook cluster; use `heng` for the
short top-heng; explicit CROSS_ANCHOR for the pie+na inside.

### p3_char_0247_军 (军, 6画)
2 draw calls; note says "冖 top + 车 body". Body severely under-
drawn. Fix: use `mi_cover` for 冖 top; hand 车 as heng+shu+heng-shu-
zhe with center vertical.

### p3_char_0248_伄 (伄, 6画)
Zero draws. Right 刁-like part missed. Fix: 亻 + 刁 (compound
heng-zhe with dot). Consider promoting `diao.py` (刁 primitive).

### p3_char_0249_同 (同, 6画)
冂 mentioned in notes as "chronic" but 0 imports (`chronic/jiong_frame`
missed AGAIN). Fix mandatory: `from chronic.jiong_frame import
draw_jiong_frame` — do not inline.

### p3_char_0250_伉 (伉, 6画)
Imports pie/shu/heng/dian; 7 draws. Right 亢 top-dot dropped.
Fix: enforce 6 strokes; top-dot LAST (defensive from drawer_memory
"top-dot dropped" note).

### p3_char_0252_伊 (伊, 6画)
Zero draws; explicit note "does not import ren_side because default
anchors sit in TC/C/BC — this item wants TL/ML/BL". This IS an
anchor-override problem the never-tune-anchors rule addresses. Fix:
use ren_side WITH the offset feature OR add a `ren_side_TL.py`
variant.

### p3_char_0253_好 (好, 6画)
Imports pie_dian, pie, heng, heng_pie, wan_gou; 8 draws. Left 女
did not use `nv.py`. Right 子 fragmented. Fix: import nv + zi (both
mastered).

### p3_char_0254_伎 (伎, 6画)
Imports pie/shu/heng/na; 8 draws. Right 支 topology off. Fix: 支 =
十 top + 又 bottom; use `you_again.py` for the 又 half.

### p3_char_0258_伕 (伕, 6画)
10 draws (over-count). Right 夫 has extra strokes. Fix: 夫 = 二 +
人 = heng + heng + pie + na (4 strokes); total with 亻 = 6.

### p3_char_0263_她 (她, 6画)
Imports nv + heng_zhe_gou + shu + shu_wan_gou; 4 draws. Right 也
loose. Fix: 也 = heng-zhe-gou + shu-wan-gou + inner shu = 3 strokes;
composition should be 3 (nv) + 3 (also) = 6.

### p3_char_0264_伢 (伢, 6画)
Imports pie/shu/heng/shu_gou; 10 draws (over-count). Right 牙 has
X-cross. Fix: CROSS_ANCHOR at pie+shu-gou intersection.

### p3_char_0265_名 (名, 6画)
Zero draws. Note: "名 = 夕 + 口. Long s2 diagonal". Fix: import
`kou.py` (mastered) for the bottom-right 口; 夕 = pie + heng-zhe-
gou + inner dian (3 strokes).

### p3_char_0266_伥 (伥, 6画)
Zero draws. Note explicitly says "长 half rendered fresh (no chronic
promoted yet)". This IS the retry-terminal cluster leaking into
mains. Fix: N/A unless chang_long.py is actually written.

### p3_char_0267_西 (西, 6画)
Zero draws. Note: "6 strokes: heng, shu(left), heng-zhe(top+right),
inner-pie...". Fix: 西 = top-heng + LEFT-shu + RIGHT-heng-zhe +
inner two-pies (or 儿-like) + closing-heng at bottom. Frame closure
often missed.

### p3_char_0270_伧 (伧, 6画)
Zero draws. Right 仑 = 人 apex + 匕 base. Fix: `ren.py` (mastered)
+ `bi.py` (mastered).

### p3_char_0272_伪 (伪, 6画)
Imports pie/shu/dian/heng_zhe_gou; 6 draws. Right 为 has 4-stroke
compound including the outer 撇 + inner dot-cluster. Structure
matches the note but panel rejected — likely stroke-weight or dot
placement. Fix: rebalance for panel visual weight; place inner dots
higher.

### p3_char_0273_次 (次, 6画)
Zero draws. Note: "6 N-joints natural gaps". Fix: right 欠 needs
hard structure — use `pie` + `heng_gou` + `pie` + `na` for the 4
strokes; import when available.

### p3_char_0274_伫 (伫, 6画)
Imports pie/shu/dian/heng; 6 draws. Right 宁 collapsed. Fix: import
`mian.py` (宀 roof) for the top; 亍 base as heng+dian+shu-gou.

### p3_char_0276_佤 (佤, 6画)
Zero draws. Note: 5-stroke 瓦. Fix: 瓦 requires compound heng-zhe-
wan-gou; either promote `wa.py` primitive or hand-craft with a single
`stroke_variable_width` for the compound.

### p3_char_0279_色 (色, 6画)
Only 2 draws. Note: "s2 & s3 rendered as 2-segment". Fix: 色 = 刀
top + 巴 base; use `chronic/dao_char.py` for the 刀 top (mandatory
import per drawer_memory).

### p3_char_0280_兆 (兆, 6画)
Zero draws. Fix: 兆 = 儿-widened base + 2 flanking dot-groups; use
`er_legs.py` for the base; place 2 pie+dian clusters left and right.

### p3_char_0281_设 (设, 6画)
Zero draws. Note: "讠 + 殳; s5-s6 P joint welded". Fix: promote a
`yan_side.py` primitive for 讠 (currently missing bank entry — this
is a B9 prereq); 殳 as compound.

### p3_char_0283_传 (传, 6画)
Zero draws, no notes. Fix: 传 = 亻 + 专. import ren_side; 专 as
heng+heng+shu-zhe-hook+dian.

---

## Cross-batch pattern from B8 mains

**Bank import rate cratered**: only 6 of 30 FAILs import ANY bank
primitive; 4 of 20 PASSes do. The v8/v9 mechanism to lift bank
reuse has not held; drawers overwhelmingly prefer to inline via
`_anchor + fat_line` primitives when the target is a 6-stroke char.
The passing 20 are simple enough (亚, 后, 多, 此, 伐, 问, 回, 再,
问, 齐, ...) that inlining works. The failing 30 are compositional
6-stroke chars where inlining a compound right-half from scratch
loses coherence.

This suggests the "high-value component" shortlist in
`drawer_memory.md` is not reaching drawers, OR drawers are reading
it and rejecting it because they perceive per-item MMH anchors as
authoritative over primitive-default anchors. Ongoing investigation.

---

## Batch 9 (positions 451-500) — 30 main FAILs

Landmark batch: G4 posted 10 A verdicts on mains + 1 A on retry (亚) +
10 PASSes on mains + 5 PASSes on retries = 26/66 successful (39%).
Retry recovery jumped from 0/22 in B7/B8 combined to 5/16 in B9.

BANK_DEVIATION channel usage this batch: 0/66. The v13 channel is
available but no drawer invoked it. Chronic-import rate on mains
containing 丿/刀/冂/弓/马 as sub-components (rough scan: 两/甸/丽/甹/冱,
~5 candidates): 0/5. Comment mention only in `p3_char_0324_但`.
Three negative batches on the chronic-mandatory-import mechanism
(B7=0, B8=0, B9=0) — mechanism is dead.

### p3_char_0284_龹 (龹, 12画)
Complex compound rarely-used char. Drawer produced fragmented sub-parts;
top 龹 outer shape has no bank primitive. Fix idea: split into 半+豕
form; hand-derive using `_anchor + fat_line` per MMH.

### p3_char_0285_师 (师, 6画)
师 = 丿 + 巾-form + top curl. FAIL mode: top short pie + heng combo
misaligned; right 巾 baseline too shallow. Fix: use MMH-verbatim; s1
short pie at TL; ensure s3 竖 anchors align with the top-heng right
end.

### p3_char_0286_冱 (冱, 6画)
冫 + 互. 冫 dots misplaced (too close together). Fix: import base 冫
dot pattern; 互 as heng+heng-zhe-heng+heng per MMH.

### p3_char_0288_凫 (凫, 8画)
凫 = 鸟-simplified top + 几 base. Right side of 几 tail under-extended.
Fix: hand-derive top 鸟-like using MMH; 几 base with wide MR anchor.

### p3_char_0290_甸 (甸, 7画)
勹 outer + 田 inner. 田 grid misaligned. Fix: import base `bao_char.py`
for 勹 outer, then 田 as tight 4-stroke box in inner cell. (chronic
component candidate: none — 勹 is not chronic.)

### p3_char_0292_甹 (甹, 9画)
甹 = 由 + 丂. Rare char; sub-parts fragmented. Fix: hand-derive using
MMH literally; consider promoting a `you_from.py` for 由 pattern.

### p3_char_0295_时 (时, 7画)
日 + 寸. Right 寸 dot floats too far. Fix: import `ri.py` for 日 left;
hand 寸 = heng + shu-gou + dian, anchor dot near shu-gou body.

### p3_char_0296_串 (串, 7画)
Two 口 vertically stacked on 竖. FAIL: upper and lower 口 too far apart;
central 竖 misaligned. Fix: enforce s1(shu) at ('C',0.5,0.05)→('BC',0.5,0.95),
then two 口 boxes centered on it at y∈[0.15,0.45] and y∈[0.55,0.85].

### p3_char_0297_你 (你, 7画)
亻 + 尔. Right 尔 fragmented. Fix: import `ren_side.py` for 亻;
hand 尔 = pie + shu-gou + 2 dots per MMH.

### p3_char_0298_丽 (丽, 7画)
一 + 冂 + 冂. Two 冂 frames side by side under top heng. Chronic
`jiong_frame` NOT imported (comment-only in prior batches). Fix:
MANDATORY `from chronic.jiong_frame import draw_jiong_frame`; call
TWICE with offset_x for left/right positioning.

### p3_char_0302_疔 (疔, 7画)
疒 outer + 丁 inner. 疒 left column strokes disconnected. Fix: promote
a `chuang_sick.py` primitive for 疒 (5 strokes: dot+heng+pie+dot+dot);
inner 丁 = heng + shu-gou.

### p3_char_0303_进 (进, 7画)
辶 + 井. Both parts inline; 辶 sweep too short, 井 crossed wrong. Fix:
use `chuo_walk.py` for 辶 (mastered radical primitive); hand 井 as
2 heng + 2 shu-pie crossing in center.

### p3_char_0306_亨 (亨, 7画)
亠 + 口 + 了. Top 亠 dot+heng OK; middle 口 too large; bottom 了 hook
missing. Fix: import `tou.py` for 亠 top; `kou.py` for middle 口
(constrain x∈[0.30,0.70], y∈[0.30,0.55]); hand 了 = short heng-gou +
shu-gou with hook.

### p3_char_0307_没 (没, 7画)
氵 + 殳. 氵 3-dots row misaligned; 殳 top 几-form fragmented. Fix:
promote a `shui_side.py` (氵 3-dot column primitive); hand 殳.

### p3_char_0309_两 (两, 7画)
一 + 冂 + 人 + 人. Chronic `jiong_frame` NOT imported (0/5 chronic
candidates imported this batch). Fix: MANDATORY jiong_frame import
for the 冂; two inner 人 as pie+na pairs.

### p3_char_0311_身 (身, 7画)
Single compound char with 撇+竖折+3-hengs+pie. Under-drawn; missing
right pie tail. Fix: MMH-verbatim all 7 strokes; s7 pie must extend
from mid-right to bottom-right (x∈[0.55,0.95]).

### p3_char_0312_伲 (伲, 7画)
亻 + 尼. 尼 = 尸 + 匕. Fix: import `ren_side` + `shi_corpse.py` (户 form)
+ `bi.py` for 匕 tail.

### p3_char_0314_伶 (伶, 7画)
亻 + 令. 令 = 人 + 一 + 卩-simplified. Fix: import `ren_side`; hand 令
per MMH (5 strokes).

### p3_char_0315_声 (声, 7画)
士 + 尸. Fix: import `shi_scholar.py` for 士 top; `shi_corpse.py` for
尸 wrapper.

### p3_char_0316_伺 (伺, 7画)
亻 + 司. 司 outer sweep + inner 一+口 all inline. Fix: import
`ren_side`; hand 司 as heng-zhe-gou wrapper + inner heng+kou.

### p3_char_0317_员 (员, 7画)
口 + 贝. Top 口 too wide; bottom 贝 4-stroke box + 2 legs fragmented.
Fix: import `kou.py` for both (constrain top 口 x∈[0.30,0.70],
y∈[0.05,0.30]).

### p3_char_0318_伽 (伽, 7画)
亻 + 加. 加 = 力 + 口. Fix: import `ren_side` + `li.py` + `kou.py`.

### p3_char_0319_听 (听, 7画)
口 + 斤. 口 too tall; 斤 pie under-slanted. Fix: import `kou.py`;
hand 斤 = short pie + heng-zhe + heng + shu.

### p3_char_0321_把 (把, 7画)
扌 + 巴. Fix: import `shou_side.py` (mastered); hand 巴 as heng-zhe +
shu + heng + shu-wan-gou.

### p3_char_0325_状 (状, 7画)
丬 + 犬. 丬 left column bad; 犬 X-cross topology bug — pie/na apex not
shared. Fix: hand 丬 (dot+heng+heng+shu); use X-cross CROSS_ANCHOR
snippet for 犬's pie+na.

### p3_char_0326_佇 (佇, 7画)
亻 + 宁-simplified. Fix: import `ren_side` + `mian.py` for top; inner
丁 as heng+shu-gou.

### p3_char_0328_佈 (佈, 7画)
亻 + 布. 布 = 丿 + 十 + 冂-like frame. Fix: import `ren_side`; hand 布
per MMH; consider chronic `jiong_frame` for frame.

### p3_char_0329_运 (运, 7画)
辶 + 云. Fix: use `chuo_walk.py`; hand 云 = 二 + 厶 per MMH.

### p3_char_0331_更 (更, 7画)
一 + 曰 + 又/攴-tail. Under-drawn; bottom tail missing. Fix: MMH-
verbatim all 7 strokes; ensure bottom pie tail reaches BR.

### p3_char_0333_条 (条, 7画)
夂-like top + 木 base. 夂 top is TERMINAL_FROZEN canonical — inline
per MMH; base 木 as heng+shu+pie+na. Fix: enforce top+base vertical
alignment.

---

## Cross-batch pattern from B9 mains

**Bank-import rate**: ~11 of 50 mains import a named bank primitive
beyond `_anchor`. All 10 A-verdict items either import a primitive
correctly OR inline via MMH-verbatim anchors with an explicit
decomposition comment + SELF_CHECK block declaring stroke count +
joint class. **The A-recipe is not "import more"; it is "trust MMH
literally and structure the code with an explicit decomposition
comment naming the sub-radicals."**

**BANK_DEVIATION channel (v13, new)**: 0/66 usage. Drawers did not
signal any deviations. This may mean (a) drawers didn't read the v13
addendum, or (b) all deviations that happened were considered
implicit under "trust GT over memory". Insufficient signal to
promote any variants this batch.

**Chronic-mandatory-import mechanism**: 0/5 imports across chronic-
candidate mains. This is the 3rd negative batch (B7=0, B8=0, B9=0).
The mechanism as currently implemented (comment snippet in
`drawer_memory.md` + INDEX pointer) is dead. Either escalate to
dispatcher-level pre-check, or retire the mandate.
