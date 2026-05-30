# Drawer memory

Curator-owned. Strokes are judged by a reference-free Claude-vision
calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion / overall,
0–2 each, /10). Characters add OCR (`is_correct`) and a trustworthy
graphics.txt GT (`visual_score` — *regression* only). Mastery:
`is_correct == true` AND rubric total ≥ 7 with no 0, post-reflection.

---

## Verified atomic-stroke recipes (c1+c2 isolation 9–10/10; c4+c6 composition 9/10)

The brushed approach holds for the six core strokes at any reasonable
size, AND across compound primitives (c6 七/山 mastered).

### Core technique

Cubic-Bézier centerline sampled at ~120–200 points; `pensize` set
per sample. **peak ≤ ~2× middle; middle ≥ ~50% of peak** (raised
from 30% after c5 short-stroke regression — c6 confirmed 50% works).
Apply width modulation across the ENTIRE path of every primitive,
including the corners of compound strokes.

### Width-profile per atomic stroke

- **点 dian:** thin entry → rounded weighted belly → tapered tail.
- **横 heng:** soft weighted entry → shaft ≥ 50% of peak → weighted
  end press. Faint upward tilt.
- **竖 shu:** weighted bulb top → shaft ≥ 50% of peak → weighted foot.
- **撇 pie:** heavy weighted head at START → gentle bow → fine point
  at END.
- **捺 na:** thin entry → broadening → **heavy pressed tail at END**
  with **flat-kick plateau** (hold near-peak width over last
  10–15% of arclength, c5/c6 入 nailed this).
- **提 ti:** weighted base at START → gentle rise → fine flicked
  point at END.

### "Which end is heavy?" cheat sheet

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick) | start |
| 提     | start | end |
| 点     | belly | tail |

Key to stroke identity, not chord direction.

## Compound strokes (c6 mastered: 七 竖弯, 山 竖折)

Draw as ONE continuous brushed path. Per-sample pensize sweep across
both arms AND through the corner. The corner is a 顿笔 — a clear
thickening at the turn that reads as a 折/弯, not a hairline angle.
c6 七 had a subtle corner (dunbi=1); future cycles should make the
corner thickening more pronounced (lift to dunbi=2).

## Canvas conventions

- 800×600 white background, black ink.
- `t.pensize()` varied per Bézier sample.
- `screen.tracer(0,0)` then `screen.update()`; PostScript → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()`.
- Each task starts at (0,0) heading 90°.

## Verified character compositions

**Mastered (c4):** 一, 二, 三, 十, 人, 八.
**Mastered (c6):** 上, 下, 七, 山.

**Still failing — refined diagnoses after c6:**

- **大 (c5: 撇/捺 below heng → 天; c6: heng too short → ambiguous /
  "A"-shape).** Updated recipe:
  - apex of 撇/捺 ABOVE the heng (~150–170 px above center) ✓
  - heng cuts horizontally through both limbs ~30–40% down ✓
  - **NEW FIX: the heng must extend WELL past the crossing points
    on both sides** (≥ 30–40% past each limb, so the heng is the
    widest element of the character). c6 drew heng barely wider
    than the limb-crossing span; that reads as 'A' with a crossbar
    rather than 大. Target heng length ≈ 1.4–1.6 × the horizontal
    distance between the 撇 and 捺 at the crossing height.

- **入 (c5: 捺 at apex → 人; c6: junction too high → still 人).**
  Updated recipe:
  - only 撇 has the top apex ✓
  - 捺 starts ON the 撇's spine, **45–55% down from the head** (c6
    was ~35% — too close to the top to disambiguate). Push the
    junction visibly past the midpoint of the 撇.
  - 捺 ends well below and to the right of where 撇 ends (the right
    extent of 入 is dominated by the 捺's tail; 人 is more
    symmetric).

## Soft / completed observations

- 捺 flat-kick plateau: solidly mastered (c5/c6 入).
- 七 compound: brushed sweep landed; corner thickening could be
  stronger (currently dunbi=1).

## What to do next cycle

c7 should carry **大 and 入** (un-mastered after the c6 refinement).
The other 4 (上, 下, 七, 山) are mastered and retire. Teacher can
either:
- (a) carry over only the 2 un-mastered + introduce 4 new chars
  testing the next set of strokes/compositions, or
- (b) drill 大/入 with 4 chars sharing the same difficulty class
  (more 撇+捺 characters: 木, 火, 个, 又).

Either way, the two specific c7 fixes for 大/入 are:
- 大: heng length ≥ 1.4× the limb-crossing span.
- 入: junction at 45–55% down the 撇's spine, not 35%.
