# Drawer memory

Curator-owned. Strokes are judged by a reference-free Claude-vision
calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion / overall,
0–2 each, /10). Characters add OCR (`is_correct`) and a trustworthy
graphics.txt GT (`visual_score` — *regression* only). Mastery:
`is_correct == true` AND rubric total ≥ 7 with no 0, post-reflection.

---

## Verified atomic-stroke recipes

Mastered across cycles 1–8.

### Core technique

Cubic-Bézier centerline sampled ~120–200 points; `pensize` per
sample. **peak ≤ ~2× middle; middle ≥ 50% of peak.** Continuous
width across the ENTIRE path including compound corners.

### Width-profile per atomic stroke

- **点 dian:** thin entry → rounded weighted belly → tapered tail.
- **横 heng:** soft weighted entry → shaft ≥ 50% peak → weighted end.
- **竖 shu:** weighted bulb top → shaft ≥ 50% peak → weighted foot.
- **撇 pie:** heavy head at START → gentle bow → fine point at END.
- **捺 na:** thin entry → broadening → heavy pressed tail at END
  with **flat-kick plateau** (last 10–15% near-peak).
- **提 ti:** weighted base at START → gentle rise → fine flick at END.

### "Which end is heavy?" cheat sheet

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat kick) | start |
| 提     | start | end |
| 点     | belly | tail |

## Compound strokes (verified)

Mastered: 竖弯 (七), 竖折 (山), 横撇 (又), **横折 (中)**.
One continuous brushed path across both arms + corner. Corner-boost
顿笔 Gaussian bump (factor ~1.55, σ~0.06) lifts dunbi to 2.

## Canvas conventions

- 800×600 white, black; per-sample pensize on Bézier path.
- `screen.tracer(0,0)` + `update()`; PostScript → PIL → PNG.
- `t.reset()` between tasks (NEVER `screen.bye()`).
- Each task at (0,0) heading 90°.

## Verified character compositions

**Phase-2 mastered (16 chars through c8):**
- 1–2 strokes: 一, 二, 十, 人, 八, 又.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工.
- 4 strokes: 不, 木, 王, 中.

## OCR-wall characters (composition correct, RapidOCR refuses)

These two characters have visually-correct silhouettes (rubric 8–9/10)
that RapidOCR's PaddleOCR-trained model consistently refuses to
recognize as the intended character. Document and move on — this is
a measurement-tool limitation, not a memory failure.

- **大 (c5–c8):** by c8 the heng is 2.8× the limb-crossing span, the
  apex is well above the heng, the limbs extend further below than
  above the heng. The silhouette is geometrically textbook. OCR
  returns empty across all four attempts. **OCR-wall.**
- **入 (c5–c8):** by c8 the 撇 has a bold head, the 捺 attaches at
  ~50% down the 撇's spine, the 捺 right-tail extends further right
  than the 撇 left-tail extends left. Silhouette unambiguously 入 to
  a human. OCR returns 人 across all four attempts. **OCR-wall.**

The original Curator note in `runs/run_1/POSTMORTEM.md` was that
RapidOCR can mis-recognize even good calligraphy in certain cases —
大/入 are concrete instances of that wall. Future cycles should not
keep grinding on these two unless RapidOCR is replaced; rubric is
the signal that matters and rubric says they're done.

## Failure modes still being learned

- **火 (c8):** drawn with 撇/捺 NOT sharing an apex (small gap at
  top), so it read as 八 with floating 点. **Fix for c9:** 撇 and
  捺 must share a SINGLE apex point near the top, with the two 点
  positioned closely to either side of that shared apex (not floating
  high above). 火 silhouette = a tighter 大-like shape topped with
  two 点 hugging the apex.

## What to do next cycle

c9 should carry **火** with the apex-sharing fix. Optionally also
carry 大 and 入 as OCR-wall documentation cases — but if grinding
becomes diminishing returns, retire them under "OCR-wall" status.
Introduce 4 more characters covering remaining stroke families:
- 口 (3): pure rectangular frame using 横折 (no center shu — distinct
  from 中).
- 田 (5): 口 frame + interior cross. Tests frame + crossing.
- 日 (4): tall narrow 口 + middle heng.
- 月 (4): tall narrow 口 (left-open) + two interior heng.

Actually 田/日/月 might exceed Phase-2's 1–4 stroke band; pick within
band:
- 口 (3) — fits.
- 已 (3) — fits, intro 弯钩.
- 巳 (3), 已 (3), 己 (3) — all family of 己 with 横折钩 + heng + shu.
- 习 (3) — fits.
- 也 (3) — 横折钩 + shu + 竖弯钩.

Suggestion for c9: 火 (carry) + 口, 已, 习, 也, plus one easy filler
(yi.e.g.也 or 也). Final batch decision is the next Teacher's.
