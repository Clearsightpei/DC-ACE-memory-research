# Drawer memory

Curator-owned. Notes for the next Drawer based on what previous
attempts actually produced. This run judges **strokes by a
reference-free Claude-vision calligraphy rubric** (顿笔 / 弧度 /
粗细 taper / proportion / overall, 0–2 each, /10). There is **no
stroke ground truth** — do NOT try to match a template; produce
genuinely brush-formed strokes. Mastery = total ≥ 7/10, no 0
criterion, confirmed post-reflection.

---

## Cycle 1 — what worked (KEEP doing this)

Cold start, vision-judged: all six atomic strokes scored **9–10/10**.
The brushed approach is correct and must be preserved:

- **Render the centerline as a smooth path (Bézier-ish) and vary
  `pensize` point-by-point** to get real width modulation. A uniform
  `pensize(3)` pen line scores ~3–4 (that was run_1's failure). Width
  variation is the single biggest win.
- **顿笔 (pause/weight):** give a *weighted, rounded entry* and a
  weighted press at the end/turn. Every stroke below has a deliberate
  heavy node at start and finish.
- **Taper to a real point** where the stroke should end fine
  (撇 tail, 提 flick): width → near zero.

### Per-stroke recipes that scored well

- **点 dian (10/10):** short teardrop — thin entry broadening to a
  rounded weighted belly, slight curve. Compact.
- **横 heng (9/10):** weighted rounded entry → thinner middle →
  weighted end press; faint upward tilt. (弧度 only scored 1 — heng
  is near-straight so that is fine.)
- **竖 shu (10/10):** weighted bulb at top and foot, thinner middle,
  straight true spine.
- **撇 pie (9/10):** strong weighted head upper-right → smooth taper
  to a fine point lower-left. 弧度=1: give it a touch more natural
  bow next time (not a ruler-straight diagonal).
- **捺 na (10/10):** thin entry → broadening → a flattened pressed
  tail (顿笔) at lower-right. The flat tail kick is essential.
- **提 ti (9/10):** weighted rounded base lower-left → strong taper to
  a fine flicked point upper-right. 弧度=1: a slightly more natural
  rise-curve would make it 10.

## Only soft improvement areas (everything is already ≥9)

`hudu` (curvature) scored 1 on heng/pie/ti — a little too straight.
For 撇 and 提 add a *gentle* natural bow (large-radius, small-arc
curvature — not a tight curve). heng/shu are meant to be near-straight;
that is correct, don't over-curve them.

## Canvas conventions (confirmed)

- 800×600 white, black; vary `t.pensize()` along the path for taper.
- `screen.tracer(0,0)` then `screen.update()`; save via
  `canvas.postscript()` → PIL → PNG. Do NOT `screen.bye()` between
  tasks; use the `reset_turtle` helper.
- Each task starts at (0,0) heading 90°.

## What to do next cycle

Reuse the cycle-1 brushed recipes verbatim — they are near-perfect.
If carried over for the post-reflection confirmation, just reproduce
the same approach; optionally nudge 撇/提 with a slightly richer
弧度. Do not regress to thin uniform lines.
