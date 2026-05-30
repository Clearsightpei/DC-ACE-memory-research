# Drawer memory

Curator-owned. Strokes are judged by a reference-free Claude-vision
calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion / overall,
0–2 each, /10). Characters add OCR (`is_correct`) and a trustworthy
graphics.txt GT (`visual_score` — *regression* only). Mastery:
`is_correct == true` AND rubric total ≥ 7 with no 0, post-reflection.

---

## Verified atomic-stroke recipes

c1+c2 isolation 9–10/10; c4+c6 composition 9/10; c7 generalization
9–10/10 on first attempt for 又, 个, 不, 木.

### Core technique

Cubic-Bézier centerline sampled ~120–200 points; `pensize` per
sample. **peak ≤ ~2× middle; middle ≥ 50% of peak.** Width
modulation across the ENTIRE path of every primitive, including
compound stroke corners.

### Width-profile per atomic stroke

- **点 dian:** thin entry → rounded weighted belly → tapered tail.
- **横 heng:** soft weighted entry → shaft ≥ 50% of peak → weighted
  end press. Faint upward tilt.
- **竖 shu:** weighted bulb top → shaft ≥ 50% of peak → weighted foot.
- **撇 pie:** heavy weighted head at START → gentle bow → fine point
  at END.
- **捺 na:** thin entry → broadening → **heavy pressed tail at END**
  with **flat-kick plateau** (last 10–15% near-peak; c5/c6/c7 入 all
  nailed this).
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

## Compound strokes (verified across c6/c7)

Mastered: 竖弯 (七), 竖折 (山), 横撇 (又).
Draw as ONE continuous brushed path with per-sample pensize across
both arms AND through the corner. Gaussian 顿笔 bump at the turn
(c7 又's corner-boost at factor ~1.55 lifted dunbi to 2 — keep that
approach).

## Canvas conventions

- 800×600 white background, black ink.
- `t.pensize()` varied per Bézier sample.
- `screen.tracer(0,0)` then `screen.update()`; PostScript → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()`.
- Each task starts at (0,0) heading 90°.

## Verified character compositions

**Mastered (Phase 2):**
- 1–2 strokes: 一, 二, 三 (c4), 十 (c4), 人 (c4), 八 (c4),
  又 (c7).
- 3 strokes: 上 (c6), 下 (c6), 个 (c7), 山 (c6), 七 (c6).
- 4 strokes: 不 (c7), 木 (c7).

That's **13 characters mastered** through cycle 7.

**Still failing:**

- **大 (c5/c6/c7).** Topology correct in c7 (apex above heng, heng
  cuts through, 1.55× limb-crossing span) — still reads as "A with
  crossbar". The 1.4–1.6× rule was insufficient. **NEW FIX for c8:**
  - heng length ≥ **2.0×** the limb-crossing span at heng height
    (was 1.55×).
  - pull apex HIGHER so the "stem above heng" is more prominent
    (apex at y ≈ +200, heng at y ≈ +50, limb tails at y ≈ -200).
  - Optional: emphasize the 撇 head extending above the heng (small
    overshoot of the apex past where 撇/捺 meet).

- **入 (c5/c6/c7).** Topology is now visibly correct (c7 junction at
  ~50% down 撇 — the silhouette reads as 入 to a human), but RapidOCR
  still returns 人. This is now an **OCR-recognition wall**, not a
  composition issue. Two diagnostic options for c8:
  - **(a)** Push asymmetry harder: make 撇 head significantly
    heavier and longer than the 捺 entry; have the 撇 fully extend
    past the 捺 on the upper-left and the 捺 dominate the lower-right
    further. This might cross OCR's threshold.
  - **(b)** Accept the OCR-wall finding and document. The rubric
    scored 9/10 (visually correct); the failure is an OCR limitation,
    not a memory failure.

## Soft / completed observations

- 捺 flat-kick plateau: mastered.
- 撇 + 捺 family generalizes well: 又, 个, 不, 木 all mastered first
  attempt with no special instruction beyond memory + brief.
- Compound strokes (竖弯, 竖折, 横撇): brushed sweep + corner boost
  works as a reusable primitive.

## What to do next cycle

c8 should carry only **大 and 入**, plus introduce 4 more characters
to test broader generalization. The 大 numeric push (heng 2.0×) is
the actionable next step. For 入, try option (a) — more asymmetry —
and if it still fails, accept the OCR wall.

Candidate new chars for c8 (testing untested strokes/compositions):
- 工 (3): heng + shu + heng — vertical 工 layout.
- 王 (4): heng + heng + shu + heng — 工-with-middle-heng.
- 火 (4): 点 + 撇 + 撇 + 捺 — uses two 撇.
- 中 (4): shu + 横折 (compound) + heng + shu — first time a 横折
  inside a frame.
