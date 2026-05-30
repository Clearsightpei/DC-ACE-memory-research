# Drawer memory

Curator-owned. Notes for the next Drawer based on what previous
attempts actually produced. Strokes are judged by a reference-free
Claude-vision calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion
/ overall, 0–2 each, /10). Characters add OCR (`is_correct`) and a
trustworthy graphics.txt GT (`visual_score` — for *regression* only,
absolute low is normal cross-renderer). Mastery for both: total ≥ 7/10
with no 0 criterion, post-reflection. For characters add
`is_correct == true`.

---

## Verified atomic-stroke recipes (proven 9–10/10 in isolation, c1+c2)

The brushed approach scored 9–10 per stroke when each stroke was
rendered alone (cycle 2 avg 9.67). **These recipes are correct
*in isolation* — the cycle-3 character cycle revealed they need two
adjustments when composed into characters.**

### Core technique

Render the centerline as a smooth cubic-Bézier sampled at ~120–200
points and **set `pensize` at every sample**. Width variation is the
single biggest win. Add weighted 顿笔 at start/turn/end.

### Width-profile per stroke (with composition fixes)

- **点 dian:** thin entry → rounded weighted belly → tapered tail,
  slight rightward arc.
- **横 heng:** weighted rounded entry → thinner middle → weighted end
  press, faint upward tilt. **FIX vs cycle 3:** the 顿笔 end discs
  must be a *thickening* (peak ≈ 1.5–2× middle width), not a separate
  blob. Cycle-3 heng all looked like dumbbells (a hairline shaft
  joining two discs). Soften the end-disc radius and raise the
  middle-shaft width floor so the transition reads as one continuous
  brushed stroke.
- **竖 shu:** weighted bulb top → thin middle → weighted foot. Same
  fix — don't let the middle go almost zero.
- **撇 pie:** weighted head at the START (the thicker end) → gentle
  bow → smooth taper to a FINE POINT at the END. Heavy = start;
  hairline = end.
- **捺 na — READ CAREFULLY, the c3 failure mode lives here.** Width
  profile: **THIN entry at the start → broadening through the body →
  HEAVY flat pressed tail (顿笔) at the END.** Cycle-3 drew 捺 with
  the c1 atomic-stroke endpoints flipped under composition: heavy
  start, fine tail. That made it visually a second 撇 (OCR still
  accepted but the rubric scored taper=0). **The thicker end of a 捺
  is always the LOWER-RIGHT tail, regardless of the chord's
  start/end orientation in your code.** The flat tail kick is
  non-negotiable.
- **提 ti:** weighted rounded base at the START (lower-left) →
  gentle rise curve → fine flicked point at the END (upper-right).

### Quick "which end is heavy?" cheat sheet

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends (weighted entry + end press) |
| 竖     | both ends |
| 撇     | start (upper-right head) | end (lower-left tail) |
| 捺     | end (lower-right tail — flat press!) | start (upper-left entry) |
| 提     | start (lower-left base) | end (upper-right flick) |
| 点     | belly (middle-ish) | tail |

If your primitive function takes `(x_start, y_start, x_end, y_end)`
and a `peak` width, ensure the width profile is keyed off **stroke
identity**, not just chord direction. A `stroke_na(start→end)` must
put the press at the END no matter where the chord points.

## Canvas conventions (confirmed twice)

- 800×600 white background, black ink.
- `t.pensize()` varied per Bézier sample.
- `screen.tracer(0,0)` then `screen.update()`; PostScript → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()`.
- Each task starts at (0,0) heading 90°.

## Cycle 3 character cycle — what passed, what failed

Phase 2 entry (一/二/三/十/人/八). **6/6 OCR correct** but **0/6
mastered** because rubric averaged 5.67/10 (gate is 7/10 with no 0).
Two distinct failure modes:

1. **Barbell 顿笔 on heng & shu (一/二/三/十).** The end-cap discs
   were too large relative to a near-zero middle. Fix: peak/middle
   ratio ≤ ~2; never let middle-width go below ~30% of peak.
2. **Inverted 捺 taper (人/八).** Width profile applied wrong end.
   Fix: see the cheat sheet above — 捺's heavy end is the LOWER-RIGHT
   pressed tail.

**Composition rules that DID work (keep doing this):**
- 二: bottom heng longer than top ✓
- 三: bottom longest, middle shortest, top medium ✓
- 十: heng+shu cross at center; shu extends slightly more below ✓
- 人: 撇 starts higher and is longer than 捺 ✓ (silhouette right,
  only the 捺 brushwork wrong)
- 八: gap at top, no shared apex ✓

## What to do next cycle

Cycle 4 will carry over all 6 characters (run_3 mandatory carry-over:
nothing un-mastered retires). Same eval=gt+ocr+vision. Apply the two
fixes above:
- soften 顿笔 disc caps (peak ≤ ~2× middle, middle width floor ~30%
  of peak),
- make 捺's pressed tail at the LOWER-RIGHT end no matter how the
  primitive is parameterized.

The composition rules (lengths/positions/apex structure) were correct
— don't change those. Only fix the brushwork on heng/shu/捺.
