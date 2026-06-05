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
- 4 strokes: 不, 木, 王, 中, 日, 月, 火, 天, 见, 太.

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

## c18 update — width floors WORK (太 10/10 mastered) but cause OCR tradeoffs

c18 width floors restored brushwork: 太 mastered 10/10 (canonical
大-shape + 点), 万 rubric jumped to 8/10. But OCR became more
sensitive to silhouette shape — 万 read as 九 (撇 head not visibly
above heng), 几 read as 门 (no visible 钩), 巴 read as 日 (弯钩
absent in render). **Lesson:** width floors are correct; the
remaining gap is composition precision — strokes must end where
the character demands, not just be brushed.

## Active carry-overs after c18 (5)

- **也 (10 attempts).** c17 OCR-passed but rubric 4. c18 lost the
  竖弯钩 sweep entirely — only upper two heng + small hook remained.
  **Next:** the 竖弯钩 must dominate the bottom half of the
  character (sweep from y≈+100 down to y≈-100 then right to x≈+150
  with a 50px up-hook). The c17 layout was structurally correct;
  c18 dropped the long sweep. Restore c17 layout WITH width floors.

- **巴 (9 attempts).** c18 read as 日 conf 0.86. The 竖弯钩 below
  was supposed to be there but appears absent in the render.
  **Next:** verify the 竖弯钩 actually renders — extend it well
  below the frame (frame bottom y=-150, 弯钩 bottom y=-280, hook
  tip y=-260 x=+200). Visually unmistakable.

- **寸 (3 attempts).** c18 OCR'd 于 conf 0.25. Still ambiguous.
  **Next:** make 竖钩 hook MORE pronounced (longer leftward hook
  arm) so it can't be confused with a straight 竖. Move 点 to upper-
  right area above the heng to differentiate from 于's structure.

- **万 (3 attempts).** c18 brushwork 8/10 but OCR 九 conf 0.81 —
  撇 head was at heng level, not above. **Next:** push 撇 head HIGHER
  — head y = heng_y + 80 (not just +30); the 撇 must START in the
  empty space ABOVE the heng top, then sweep DOWN through the heng,
  exiting at lower-left.

- **几 (2 attempts).** c18 brushwork 6/10 but OCR 门 conf 0.83 —
  no visible 钩 at bottom-right. **Next:** make the 钩 (up-hook at
  end of 横折弯钩) PROMINENT — hook arm length 60+ px, tip clearly
  pointing up-and-left. Without the hook 几 reads as 门.

- **(太 MASTERED c18 at 10/10 — removed from carry-overs.)**

## What to do next cycle

c19 backlog = 5 (也, 巴, 寸, 万, 几). Backlog < 6 → 1 new char
allowed. Recommended c19: [也, 巴, 寸, 万, 几, + 1 new].
For the new char, pick something far from any OCR-confusing
silhouette — e.g. **公** (4-stroke 八+厶, distinct from anything
on the failure list).
