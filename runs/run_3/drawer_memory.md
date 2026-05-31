# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.

---

## Verified atomic-stroke recipes

Cubic-Bézier centerline ~120–200 points; per-sample pensize;
middle ≥ 50% of peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick) | start |
| 提     | start | end |
| 点     | belly | tail |

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩.
One continuous brushed path; corner Gaussian thickening; hooks are
short tail-arms (15–20% main length).

## Canvas conventions

- 800×600 white; per-sample pensize on Bézier.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (22 mastered through c11)

- 1–2 strokes: 一, 二, 十, 人, 八, 又.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已.
- 4 strokes: 不, 木, 王, 中, 日, 月.

## NOT mastered — UN-RETIRED after Teacher-skill rule update

Earlier cycles labeled these "OCR-wall" and stopped drilling, but
that was a rationalization. Per the updated Teacher hard no-skip
rule (quality > coverage), these are active carry-overs and must
keep being attempted until the silhouette is correct enough that
even biased RapidOCR recognizes them. Status:

- **大** (failed c5/c6/c7/c8 = 4 attempts): the silhouette has been
  "A with crossbar" — not a 大 shape. The 撇 and 捺 are too narrow
  and don't extend wide enough below the heng; the heng could be even
  longer; the apex stem too tall relative to the limbs. **NEXT FIX:**
  make the 撇/捺 tails much wider apart at the bottom (limb tails at
  x ≈ ±260, not ±200); shorten the apex stub so the heng dominates;
  consider drawing the heng with a slight downward dip in the middle
  (real calligraphic 大 has a gentle V-shape to the heng).
- **入** (failed c5/c6/c7/c8 = 4 attempts): silhouettes have been
  close to 人. **NEXT FIX:** the 撇 should be SHORTER and the 捺
  should LEAN further right and be the dominant stroke (in 入 the
  right side is heavier and longer). Junction at 50% is correct.
- **火** (failed c8/c9/c10/c11 = 4 attempts): the 点 placement
  improved progressively but the overall character still doesn't OCR.
  **NEXT FIX:** look closely at standard 火 — the two 点 are not
  ABOVE the apex, they are at roughly the same height as the apex on
  either side, like ears (left 点 slopes down-and-right from upper-
  left of the apex; right 点 slopes down-and-left from upper-right
  of the apex). Place the 点 OUTSIDE the apex's horizontal extent,
  not hovering above it.

## OCR mis-recognitions to overcome (NOT "OCR-wall")

Earlier cycles recorded these as "OCR-bias" and used that as
permission to lower effort. That was wrong. The mis-recognitions
indicate the silhouette is too close to a neighbor character — the
fix is to draw the *distinguishing feature* more prominently, not
to declare the OCR broken. Active failure modes with concrete next
moves:

| char drawn | OCR reads | distinguishing feature to amplify next attempt |
|------------|-----------|-----------------------------------------------|
| 也 | 卫 | 竖弯钩 must wrap UNDER both other strokes (form a clear floor) and hook UP-RIGHT at the end. 卫 has no such hook. Make the up-right hook longer and sharper. |
| 力 | 刀 | The horizontal top of 力's 横折钩 must extend WELL TO THE LEFT of the corner (a real heng). 刀 has no such extension. Push the heng start to x ≈ −150 while the corner sits at x ≈ +80. |
| 巴 | 已 | 巴 is taller and has a CLOSED upper rectangle with a middle heng dividing it into two stacked compartments. 已 has only a single-corner top. Make the upper portion a tall double-decker, not a single open corner. |
| 见 | 月 | 见's LEFT side is a 撇 leg (diagonal sweeping down-LEFT past the bottom of the frame). 月's left side is straight. Push the 撇 to clearly diverge from the frame at the bottom-left. |

## What WOULD help these characters cross OCR (if we keep trying)

- 力: extend the top heng of 横折钩 far to the LEFT of the corner,
  so the heng dominates the upper silhouette and clearly differs
  from 刀.
- 巴: make the upper double-decker frame visibly taller and contain
  multiple horizontal bars to distinguish from 已's single-corner top.
- 见: keep top frame compact, make the LEFT leg (撇) clearly diagonal
  going down-left out from the frame's bottom-left — the 撇 leg is
  the distinguishing feature vs 月.
- 也: hard. The character's signature shape is hard to compose from
  primitives; even when correct, the result is unusual relative to
  printed-font 也 that OCR was trained on.

## State through c11 (post no-skip-rule update)

- **22 characters mastered**: 一二十人八又三上下个山七工口子习已不木王中日月.
- **7 active carry-overs** (un-mastered, MUST be drilled until they
  pass): 大, 入, 火, 也, 力, 巴, 见. None retire as "OCR-wall" —
  per the updated Teacher hard no-skip rule, these stay in the
  rotation. The "OCR-bias" notes above are diagnostic, not exit
  criteria.

## What to do next cycle

Active backlog is 7 carry-overs. The Teacher's next batch should be
6 of those 7 carry-overs (per the "no new chars while backlog ≥ 6"
rule). Pick the 6 with the freshest diagnoses and most-targeted
prescriptions in this memory file:
- 大 (next-fix: wider limb tails ±260, shorter apex stub, dipped heng).
- 入 (next-fix: shorter 撇, longer/dominant 捺 leaning further right).
- 火 (next-fix: 点 outside apex horizontal extent, at apex height — not above).
- 也 (next-fix: sharpen 竖弯钩's up-right hook).
- 力 (next-fix: top heng of 横折钩 extends far left of corner).
- 巴 (next-fix: double-decker upper rectangle with middle heng inside).

Defer 见 by one cycle (it was c11's freshest non-mastered, but with
6 older carry-overs the rule forces the 6 above).
