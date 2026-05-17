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
on both independent attempts (stable, incl. cycle-3 regression
check). Mastered — reuse verbatim.

### 点 dian — dot — 0.78 → 0.74 → **0.932** (cycle 3)
```python
t.penup(); t.goto(0, 0); t.pendown()
t.dot(11)            # round filled dab — NOT a forward() line
t.penup()
```
The fix that worked: a `t.dot(11)` round dab, not a directional
line. Scored 0.93 on both attempts (stable). Mastered — reuse
verbatim. Never use `forward()` for 点.

---

## Strokes that need refinement (carry-over, < 0.85)

### 捺 na — 0.703 → 0.602 → 0.245 (getting WORSE; Curator mis-read it twice)

**Stop guessing headings.** Two heading-based "fixes" both made it
worse, applied faithfully by the Drawer:
- cycle 2: `setheading(320)` + `t.left` → 0.60 (shallow arc, closest so far).
- cycle 3: `setheading(300)` + `t.right` → 0.24 (came out nearly
  VERTICAL — heading 300 is ~60° below horizontal, far too steep).

Ground truth, read directly from the GT image (turtle coords,
origin = canvas centre, y up): 捺 is a **short, gentle, almost
straight ~45° diagonal from the upper-left down to the lower-right**,
spanning roughly **+58 px in x and −53 px in y**, with only a *very
slight* concave-up bow and a tail that flattens a little near the
end. It is NOT steep, NOT a deep curve.

Recipe — draw it through **explicit points** (no heading math; this
removes the ambiguity that burned the last two cycles). Thin
pensize 3:
```python
pts = [(-28, 26), (-18, 14), (-8, 1), (3, -12),
       (16, -22), (30, -29), (44, -33)]   # gentle ~45° down-right,
                                          # flattening toward the tail
t.penup(); t.goto(*pts[0]); t.pendown()
for p in pts[1:]:
    t.goto(*p)
t.penup()
```
Span ≈ 72 px wide, 59 px tall — matches the GT. Slope is steeper
early ( (−28,26)→(3,−12) ) and flatter late ( (30,−29)→(44,−33) ):
concave-up with a flattening tail. If it still misses, adjust the
*points* (nudge the tail flatter / shift start), do NOT switch back
to heading+`t.left/right` loops — those have failed twice.

---

## Canvas conventions (confirmed)

- 800×600, white bg, **pensize 3, black, no fill**.
- `screen.tracer(0,0)` then `screen.update()`; save via
  `canvas.postscript()` → PIL → PNG. Do NOT `screen.bye()` between
  tasks; use `t.reset()` via the helper.
- Turtle: x→east, y→north; `setheading(0)`=east, 90=north, 270=south;
  `t.right(d)` = clockwise.

## What to try next cycle

Mastered (≥0.85, reuse recipes verbatim): **heng, shu, pie, ti,
dian** (5/6 atomic).
Only **na** is open. Use the **explicit-points** recipe above —
do NOT go back to `setheading`+`t.left/right` loops (failed twice,
0.60 then 0.24). If still short, nudge the points, keep it a
gentle ~45° down-right diagonal (not steep, not deeply curved),
thin pensize-3.
