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

### 撇 pie — left-falling — 0.706 → **0.936** (cycle 2)
```python
t.penup(); t.goto(24, 35); t.setheading(260)
t.pendown()
steps = 60
for _ in range(steps):
    t.forward(70.0 / steps)
    t.right(55.0 / steps)   # gentle ~55° clockwise arc over the length
t.penup()
```
Small thin gentle arc, upper-right → lower-left. Mastered — reuse
verbatim.

### 提 ti — rising flick — 0.662 → **0.932** (cycle 2)
```python
t.penup(); t.goto(-30, -20); t.setheading(33)
t.pendown(); t.forward(70); t.penup()
```
Short thin straight rising line at 33°, no start blob. Scored 0.93
on both independent attempts (stable). Mastered — reuse verbatim.

---

## Strokes that need refinement (carry-over, < 0.85)

### 捺 na — 0.703 → 0.602 (cycle 2, WORSE; consistent on both attempts)
Size/weight is now fine, but the **curve bows the wrong way**. The
cycle-2 attempt used `setheading(-40)` (≈320°, down-right) with
`t.left(...)`, which produced a curve that humps **upward**
(concave-DOWN, like a frown). The GT 捺 is the opposite: it descends
from upper-left and is **concave-UP (a valley/smile)** — steeper near
the top, then the tail flattens out toward the lower-right.

Fix — start steeper and curve the OTHER way (clockwise, `t.right`),
not `t.left`:
```python
t.penup(); t.goto(-28, 30); t.setheading(300)   # down-right, fairly steep
t.pendown()
steps = 60
for i in range(steps):
    t.forward(74.0 / steps)
    t.right(0.7 if i < steps*0.55 else 0.18)     # bow early, flatten tail
t.penup()
```
Key correction vs last cycle: **`t.right` (clockwise), not `t.left`**,
and a steeper start heading (~300°, not ~320°). This makes it
concave-up like the GT. Keep it thin pensize-3, ~74 px.

### 点 dian — 0.783 → 0.739 (cycle 2, still short)
The attempt drew a short *line* (16 px, pensize 5, a directional
dash). GT 点 is a small **round dab**, not a line. Stop drawing a
line — use a filled dot centered at origin:
```python
t.penup(); t.goto(0, 0); t.pendown()
t.dot(11)            # round filled dab, ~11 px
t.penup()
```
Do not use `forward()` for 点. A `t.dot()` of ~10–12 px is the
shape; tune only the diameter if it carries over again.

---

## Canvas conventions (confirmed)

- 800×600, white bg, **pensize 3, black, no fill**.
- `screen.tracer(0,0)` then `screen.update()`; save via
  `canvas.postscript()` → PIL → PNG. Do NOT `screen.bye()` between
  tasks; use `t.reset()` via the helper.
- Turtle: x→east, y→north; `setheading(0)`=east, 90=north, 270=south;
  `t.right(d)` = clockwise.

## What to try next cycle

Mastered (≥0.85, reuse recipes verbatim): **heng, shu, pie, ti**.
Still open:
- **na**: flip the curve — `t.right` not `t.left`, start steeper
  (~300°), concave-UP like a valley. (Last 2 cycles bowed the wrong
  way → 0.70 then 0.60.)
- **dian**: use `t.dot(11)` at origin — a round dab, NOT a line.
The "small + thin pensize-3, no fill/blob" rule still applies to
both.
