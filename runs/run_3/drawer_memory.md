# Drawer memory

Curator-owned. Calligraphy rubric (0–2 × 5 / 10). Mastery:
`is_correct` AND total ≥ 7, no 0, post-reflection.
**Hard no-skip**: `is_correct == false` OR `ocr_confidence < 0.4`
→ MUST carry over. Quality > coverage.

---

## "OCR-wall" was rationalization (proven c12–c16)

All previously "OCR-wall" chars mastered: 大 (c12), 入 (c12), 火 (c14).
Same principle holds for ongoing failures (also, 巴).

## Verified atomic-stroke recipes

Smooth cubic Bézier centerline ~120–200 points; **per-sample
pensize with `t.pensize(w); t.goto(x,y)`** — NOT `t.dot(w, ...)`
stamps. Middle ≥ 50% peak.

| stroke | heavy end | fine end |
|--------|-----------|----------|
| 横     | both ends |
| 竖     | both ends |
| 撇     | start | end |
| 捺     | end (flat horizontal kick) | start |
| 提     | start | end |
| 点     | belly (heavy outer for radiating 点 in 小/火); tilted ~45° | tail (inward) |

## Brush rendering — smooth Bézier, NOT dot stamps (c15 lesson, c16 fix)

Render strokes as `t.pensize(w); t.goto(x,y)` along sampled
Bézier — continuous fluid line. NEVER as `for p in pts:
t.dot(w, p)` stamps; that leaves "beads on a wire" joint artifacts
that hurt OCR and rubric.

## Compound strokes (mastered)

竖弯, 竖折, 横撇, 横折, 竖钩, 横折钩, 竖弯钩, 横钩.
横折弯钩 attempted c16 in 万 — first attempt fail; needs iteration.

## Canvas conventions

- 800×600 white; smooth per-sample pensize.
- `t.reset()` between tasks. Each task at (0,0) heading 90°.

## Verified character compositions (30 mastered through c16)

- 1–2 strokes: 一, 二, 十, 人, 八, 又, 入, 力, 了.
- 3 strokes: 三, 上, 下, 个, 山, 七, 工, 口, 子, 习, 已, 大, 小.
- 4 strokes: 不, 木, 王, 中, 日, 月, 火, 天, 见.

**见 (c16 fix):** 撇 as LONG diagonal (>200 px) sweeping from
upper-right area through frame to lower-left.
**小 (c16 fix):** tilted 点 (~45°), teardrop, outer-end heavy,
tail-toward-center.

## CRITICAL — brushwork regression in c17 (撇 hairline; uniform widths)

c17 introduced a serious regression: many strokes rendered as
near-uniform thin lines, and 撇 in 太 was almost invisible (hairline).
The OCR was permissive (3/6 passed including 也, 太, 几) but the
calligraphy rubric correctly scored them 4–5/10 (taper=0 on all
three). **OCR-pass without brushwork is NOT mastery.**

**Required brushwork (re-asserted, MUST NOT regress):**

```python
def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=160):
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1-s)**3*P0[0] + 3*(1-s)**2*s*P1[0] + 3*(1-s)*s*s*P2[0] + s**3*P3[0]
        y = (1-s)**3*P0[1] + 3*(1-s)**2*s*P1[1] + 3*(1-s)*s*s*P2[1] + s**3*P3[1]
        t.pensize(max(3, w_profile(s)))   # NEVER below 3 anywhere
        t.goto(x, y)
```

Width profiles MUST have peak ≥ 14 and middle ≥ 7 (50% of peak).
The c1–c16 widths were e.g. heng peaks 16–18 with middle 9–11. If
your `w_profile` returns 2 or 3 anywhere except for the very tip
of a tapered end, the stroke will read as a hairline and rubric
taper goes to 0.

**Per-stroke width floor:**

| stroke | peak | middle (shaft) | tip |
|--------|------|----------------|-----|
| 横     | 16   | 10             | 6 at both ends-of-taper (not at the very tips, which are weighted) |
| 竖     | 16   | 10             | 6 |
| 撇     | 17 at head | 11 shaft | 2 only at the very last 5% |
| 捺     | 18 at tail | 10 shaft | 4 at head |
| 提     | 14 at base | 9 shaft | 2 only at very last 5% |
| 点     | 14 at belly | n/a | 2 at tail |

Compound strokes follow whichever atomic they currently embody; never
let the whole stroke uniform-thin out.

## Active carry-overs after c17 (6 — all unmastered or regressed)

- **也 (9 attempts).** c17 finally OCR'd as 也 (conf 0.94)! But
  rubric only 4/10 — taper=0 (uniform lines), composition reads as
  4 disjoint fragments. **Next:** keep the upper-middle 竖弯钩 +
  内嵌 横折钩 layout (it works for OCR), but apply proper widths
  per the cheat sheet — peak 16, middle 10. Integrate the fragments
  with visible brushed continuity.

- **巴 (8 attempts).** c17 read as 电. Frame too small, 弯钩 too
  uniform-thin. **Next:** widen the upper frame (it should be wider
  than tall — currently it's a small square); make 弯钩 brushed
  with proper widths (peak 16, middle 10).

- **寸 (2 attempts).** c17 OCR'd as 卡 (conf 0.31 < threshold).
  Composition vaguely correct but brushwork uniform. **Next:** keep
  the 点 in traditional spot; thicken everything; make the 竖钩 a
  proper brushed stroke (not a uniform line).

- **万 (2 attempts).** c17 OCR'd as 瓦 with confidence 0.97 —
  CONFIDENTLY WRONG. The 撇 needs to start ABOVE the heng and
  dominate. In c17 the 撇 head was at the heng level, so the
  composition reads as 瓦. **Next:** 撇 head at y > heng_y + 30; 撇
  sweeps THROUGH the heng to lower-left. Standard width.

- **太 (1 attempt — REGRESSION).** c17 OCR'd as 太 (conf 0.99) but
  rubric 5/10: 撇 was hairline-thin. **Next:** redraw 大-shape with
  proper widths (this was MASTERED at 10/10 in c12!), then add the
  点 below. Reference c12's 大.

- **几 (1 attempt — REGRESSION).** c17 OCR'd as 几 (conf 0.99) but
  rubric 5/10: 撇 hairline, 横折弯钩 uniform. **Next:** proper
  widths on both strokes.

## What to do next cycle

c17 backlog grew to 6 (the no-skip rule triggered on 太/几 too due
to taper=0). Backlog ≥ 6 forces a carry-overs-only batch. c18 MUST
be exactly [也, 巴, 寸, 万, 太, 几]. NO new characters until
brushwork regression is fixed.

The key fix is RE-ASSERT THE WIDTH FLOORS (see top of this file).
The drawer subagent has shown over c17 that smooth-Bézier alone
isn't sufficient — explicit minimum widths are needed.
