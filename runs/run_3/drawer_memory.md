# Drawer memory

Curator-owned. Strokes are judged by a reference-free Claude-vision
calligraphy rubric (顿笔 / 弧度 / 粗细 taper / proportion / overall,
0–2 each, /10). Characters add OCR (`is_correct`) and a trustworthy
graphics.txt GT (`visual_score` — *regression* only, absolute low is
normal cross-renderer). Mastery: total ≥ 7/10 with no 0 criterion,
post-reflection. For characters add `is_correct == true`.

---

## Verified atomic-stroke recipes

c1+c2 in isolation 9–10/10; c4 in composition for {一二三十人八} 9/10.
**These recipes hold for the six core strokes when drawn at "normal"
sizes (length ≥ ~150–200 px).** Two newer findings from c5:

- they regress to barbell when strokes are *short* (e.g. 上's mid heng,
  下's shu) — keep middle width ≥ 50% of peak regardless of stroke
  length.
- the brushed technique did **not auto-transfer to new compound
  primitives** (七's 竖弯, 山's 竖折). New primitives must inherit the
  same per-sample-pensize sweep along the entire path, including the
  turn.

### Core technique (now with c5 stricter limits)

Cubic-Bézier centerline sampled at ~120–200 points; `pensize` set
per sample.
- **peak ≤ ~2× middle, middle ≥ ~50% of peak** (raised from 30% after
  c5 short-stroke barbell regression).
- Apply width modulation across the ENTIRE path of every primitive,
  including compound strokes' corners and tails.

### Width-profile per atomic stroke

- **点 dian:** thin entry → rounded weighted belly → tapered tail.
- **横 heng:** soft weighted entry → shaft ≥ 50% of peak → weighted
  end press. Faint upward tilt. Continuous brushed; no dumbbell.
- **竖 shu:** weighted bulb top → shaft ≥ 50% of peak → weighted foot.
- **撇 pie:** heavy weighted head at the START → gentle bow → fine
  point at the END.
- **捺 na:** thin entry → broadening body → **HEAVY pressed tail at
  the END**, with a **flat-kick plateau** (hold near-peak width for
  the last 10–15% of arclength then a small horizontal kick taper).
  c4 got the direction right; c5 入 got the flat kick.
- **提 ti:** weighted base at START → gentle rise → fine flicked
  point at END.

### "Which end is heavy?" cheat sheet

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends (entry + end press) |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (with flat kick) | start |
| 提     | start | end |
| 点     | belly | tail |

Key to **stroke identity**, not chord direction.

## Compound strokes (c5 introduction — partial success)

When a stroke contains a **turn** (折 / 弯 / 钩 families), draw it as
**one continuous brushed path** with per-sample pensize across both
arms AND through the corner. The corner is a 顿笔 (a thickening at
the turn), not two disconnected strokes.

- **竖弯 / 横折弯钩 (七 stroke 2):** descend from upper-middle, curl
  into the corner, then a rightward bottom arm with a small flick at
  the right end. **c5 implementation made the turn but lost the
  brushed width** — fix: apply the same heng/shu width profile
  (caps + shaft ≥ 50% of peak) along the entire path.
- **竖折 (山 stroke 2):** vertical descent + 90° turn + horizontal
  bottom. Same fix — keep width modulation continuous across the
  corner; a slightly heavier corner reads as a 折 顿笔.

## Canvas conventions

- 800×600 white background, black ink.
- `t.pensize()` varied per Bézier sample.
- `screen.tracer(0,0)` then `screen.update()`; PostScript → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()`.
- Each task starts at (0,0) heading 90°.

## Verified character compositions

**Mastered (c4):**
- 一: single centered heng.
- 二: top + bottom heng, **bottom longer**.
- 三: bottom longest, middle shortest, top medium.
- 十: heng + shu crossing at center; shu slightly more below.
- 人: 撇 + 捺 sharing top apex; **撇 starts higher and is longer than
  捺**; 捺's heavy end at lower-right.
- 八: 撇 + 捺 with **gap at top** (no shared apex).

**c5 failures with diagnoses — these compositions need fixes:**

- **大 (c5: read as 天).** The Drawer drew 撇/捺 BELOW the heng,
  starting at the heng's middle and going down. That is 天's topology.
  **Correct 大: the 撇/捺 share an apex ABOVE the heng; the heng
  passes horizontally through them (cutting across both limbs ~30–40%
  of the way down from the apex).** The 撇 extends from the apex,
  through the heng, and out the lower-left; the 捺 from the apex,
  through the heng, and out the lower-right. The heng is roughly
  shoulder-height through 撇 and 捺.

- **入 (c5: read as 人).** The Drawer drew the 捺 starting at the
  apex (essentially a sibling to the 撇 — that is 人's topology).
  **Correct 入: only the 撇 has the top apex. The 捺 starts on the
  撇's spine, partway down (around 30–40% from the 撇's head), and
  sweeps to the lower-right.** The two strokes are NOT both at the
  top — 入 is asymmetric, 人 is symmetric.

- **上 / 下:** composition fine; only the brushwork barbell on short
  strokes is the issue (middle width must hold ≥ 50% of peak even on
  short heng/shu).

- **七 / 山:** the new compound primitives must apply the same per-
  sample brushed width across the entire path (see "Compound strokes"
  section above).

## Soft improvement areas

- 捺 flat-kick plateau: c5 入's 捺 had the best version yet
  (`dunbi=2`). Keep that approach.

## What to do next cycle

c6 will carry over all 6 of c5 — **none mastered** (4/6 OCR, but rubric
gate failed everywhere). Specific fixes per task:
- 大: redraw with 撇/捺 sharing an apex ABOVE the heng, heng cutting
  through both limbs.
- 入: redraw with 捺 starting on the 撇's spine partway down (NOT at
  the apex).
- 上, 下: same composition, but enforce ≥50% middle-width on every
  stroke including short ones.
- 七, 山: keep the corner placement, but apply the brushed width
  modulation along the entire compound path (caps + ≥50% shaft).
