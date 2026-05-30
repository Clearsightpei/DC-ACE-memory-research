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

## Verified atomic-stroke recipes (c1+c2 in isolation 9–10/10; c4 in composition 9/10)

The brushed approach scored 9–10 per stroke in isolation. After the
c3 composition failure (barbell heng/shu, inverted 捺) and the c4
repair, **the recipes now hold up under composition (c4 6/6 mastered,
avg 9.00/10).** Reuse verbatim.

### Core technique

Render the centerline as a smooth cubic-Bézier sampled at ~120–200
points and **set `pensize` at every sample**. Add weighted 顿笔 at
start/turn/end. **Width modulation must be continuous** — peak ≤ ~2×
middle, middle ≥ ~30% of peak (preferably ~50%+ for heng/shu so the
shaft holds visible weight between caps).

### Width-profile per stroke

- **点 dian:** thin entry → rounded weighted belly → tapered tail,
  slight rightward arc.
- **横 heng:** soft weighted entry → shaft holds ~55% of peak →
  weighted end press. Faint upward tilt. End-caps must read as a
  *thickening of the stroke*, not as separate discs joined by a
  hairline (the c3 dumbbell artifact).
- **竖 shu:** weighted bulb top → shaft holds width → weighted foot.
  Same continuous-width rule.
- **撇 pie:** weighted head at the START (upper-right) → gentle bow →
  smooth taper to a FINE POINT at the END (lower-left).
- **捺 na:** **THIN entry at the start (upper-left) → broadening
  through the body → HEAVY pressed tail at the END (lower-right).**
  Width key is stroke identity, not chord direction — the press is
  always at the END no matter how the primitive is parameterized.
  The signature flat *kick* (a brief horizontal landing) is still a
  refinement target — c4 had a heavy lower-right press but lacked the
  flat kick (cost 1 point on `dunbi` for 人/八). A future fix is to
  hold near-peak width across the last ~10–15% of arclength rather
  than tapering smoothly.
- **提 ti:** weighted rounded base at the START (lower-left) →
  gentle rise curve → fine flicked point at the END (upper-right).

### "Which end is heavy?" cheat sheet (c3 lesson — keep this front-of-mind)

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends (entry + end press) |
| 竖     | both ends |
| 撇     | start (upper-right head) | end (lower-left tail) |
| 捺     | end (lower-right pressed tail) | start (upper-left entry) |
| 提     | start (lower-left base) | end (upper-right flick) |
| 点     | belly | tail |

Key it to **stroke identity**, not chord orientation.

## Canvas conventions

- 800×600 white background, black ink.
- `t.pensize()` varied per Bézier sample.
- `screen.tracer(0,0)` then `screen.update()`; PostScript → PIL → PNG.
- Do NOT `screen.bye()` between tasks; use `t.reset()`.
- Each task starts at (0,0) heading 90°.

## Verified character compositions (c3 wrong brushwork, c4 mastered)

- 一: single centered heng.
- 二: top heng + bottom heng with **bottom longer**.
- 三: three heng with **bottom longest, middle shortest, top medium**.
- 十: heng + shu crossing at center; shu extends slightly more below
  than above.
- 人: 撇 + 捺 sharing top apex; **撇 starts higher and is longer than
  捺**. The 捺's heavy end goes lower-right (not lower-left).
- 八: 撇 + 捺 with a **gap at the top** (no shared apex). Same 捺
  width-direction rule.

## Soft improvement areas (don't gate but worth nudging)

- 捺's flat tail kick (currently a smooth taper-to-heavy-end). Target:
  hold near-peak width for the last 10–15% of arclength, then a small
  horizontal kick-off taper. This will lift `dunbi` 1→2 on chars with
  捺 (人, 八, future 大, 入, 木 …).

## What to do next cycle (Phase-2 expansion)

Phase 2 starter (一二三十人八) is now mastered. The Teacher will
introduce new 1–4-stroke characters. Likely candidates exercising
strokes not yet stress-tested in composition:
- 七 (heng+鉤 — first compound stroke; needs a 钩 hook turn).
- 上 (heng+shu+heng — vertical composition).
- 下 (heng+shu+dian — uses 点).
- 大 (heng+撇+捺 — adds 撇/捺 over a heng with shared center; the
  捺 flat-tail-kick refinement matters here).
- 小 (shu+撇+点 / a 钩 variant — depending on which list_chars
  returns).
- 子 (compound — uses 横折钩 or 鉤 family + heng).

Apply the verified primitives + the cheat sheet. When a new stroke
appears (钩 family, 折), expect a partial-success first cycle, then
the curator will diagnose what was missing.
