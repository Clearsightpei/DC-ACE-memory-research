# Drawer memory

Curator-owned. Notes for the next Drawer subagent based on what
previous attempts actually produced vs the ground truths. The judge's
`visual_score` is a composite shape-fidelity metric (dice = overlap,
chamfer = fine detail, proportion = relative structure). Mastery gate
is **visual_score ≥ 0.85**.

---

## THE biggest cold-start lesson (cycle 1)

**Draw small and light, not big and heavy.** The ground-truth strokes
are SMALL (~70 px long, a 点 only ~17 px) and THIN (a uniform
pensize-3 line). Cycle-1 attempts drew huge (300–500 px) tapered,
filled brush shapes with heavy blobs — every curved stroke lost
points for this. Recipe that works:

```python
t.pencolor("black"); t.pensize(3)      # thin, uniform — no fill, no taper
# stroke body ~70 px total length (点 ~17 px)
```

Do **not** build filled polygons or variable-width brush shapes. A
plain `t.pensize(3)` pen path that traces the stroke's centerline is
what scores well. Reserve "顿笔/weight" for a *tiny* emphasis only —
the GT's 顿笔 is subtle, not a blob.

---

## Mastered strokes (visual ≥ 0.85) — keep doing this

### 横 heng — horizontal — 0.924
```python
t.penup(); t.goto(-35, 0); t.setheading(4)   # faint upward tilt
t.pendown(); t.forward(70); t.penup()
```
Thin straight line, ~70 px, ~4° upward tilt. Solved — reuse verbatim.

### 竖 shu — vertical — 0.922
```python
t.penup(); t.goto(0, 35); t.setheading(270)  # due south
t.pendown(); t.forward(70); t.penup()
```
Thin straight line, ~70 px, straight down. Solved — reuse verbatim.

---

## Strokes that need refinement (carry-over, < 0.85)

### 撇 pie — 0.706 (dice 0.61)
Direction was right (upper-right → lower-left, convex to the right)
but it was drawn ~5× too long and very thick/tapered. Fix: thin
pensize-3, ~70 px total. Start near (24, 35), heading ~260°, curve
gently with ~50–60° of total clockwise rotation over the length
(e.g. 60 steps of `forward(70/60)` + `t.right(1)`), ending lower-left.
Compact gentle arc, not a long heavy sweep.

### 捺 na — 0.703 (dice 0.60)
Right idea (upper-left → lower-right) but again far too large and
heavy. Fix: thin pensize-3, ~70–75 px. na is a *shallow* descent
(~45° down-right) that bows gently and flattens toward the tail —
front-load a small left-curve then straighten. NOT a deep curve, NOT
a thick wedge. Keep it small.

### 提 ti — 0.662 (proportion 0.65, the lowest)
GT 提 is a SHORT, THIN, straight rising line (~70 px) at ~30–40°
up-and-to-the-right. The attempt was a long spike with a heavy 顿笔
blob at the start — that blob wrecked the proportion term. Fix:
plain pensize-3, start lower-left ~(-30,-20), heading ~30°,
`forward(~70)`, no start blob; only a very slight taper at the very
end if any. Short and clean.

### 点 dian — 0.783 (closest of the four)
GT 点 is tiny (~17 px) and roundish — a small pressed dab, not a
line. Attempt was a bit too large/linear. Fix: keep it ~15–18 px,
compact and blunt. A short `t.dot(9)` or a very short thick-ish dab
works better than a drawn-out tear-drop.

---

## Canvas conventions (confirmed)

- 800×600, white bg, **pensize 3, black, no fill**.
- `screen.tracer(0,0)` then `screen.update()`; save via
  `canvas.postscript()` → PIL → PNG. Do NOT `screen.bye()` between
  tasks; use `t.reset()` via the helper.
- Turtle: x→east, y→north; `setheading(0)`=east, 90=north, 270=south;
  `t.right(d)` = clockwise.

## What to try next cycle

All four carry-overs share ONE root cause: **too big, too heavy**.
Redraw pie/na/ti/dian small (~70 px, 点 ~17 px) and thin (pensize 3),
keeping the directions above. heng/shu are solved — reuse their
recipes if asked again.
