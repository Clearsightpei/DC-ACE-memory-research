# Cycle 8 — 3 tasks (carry-over of 一/二/三 with wider-uniform-variant heng)

## Hard gate
OCR conf > 0.95 AND visual_score > 0.9 AND Claude vision unambiguous. ALL THREE.

## Findings from c6 + c7

The MMH GT rasterized through postscript ends up as ~20-31 px wide stroke bands. The c6 brushed heng (width 11-19) under-painted (visual ≤ 0.88); the c7 thin variant (width 3) under-painted even more (visual ≤ 0.87). The pixel-overlap (Dice) is the bottleneck.

## Tasks (same characters, third attempt)

1. 一 → `attempts/cycle_8/01_一.png` (GT `ground_truths/cycle_8/01_一.png`)
2. 二 → `attempts/cycle_8/02_二.png`
3. 三 → `attempts/cycle_8/03_三.png`

## Approach — uniform width matched to GT band

Define `draw_heng_wide(t, ox, oy, scale)` inline that uses a **constant pensize ~25** (matching the median GT band width of ~25 px). Same Bezier centerline as `heng.py`. Place centerlines at the GT band centers (c6/c7 measured these — reuse).

The brushed `heng.py` keeps its place in the bank for calligraphic uses. `draw_heng_wide` is a NEW variant — let the Curator decide whether to promote it.

## Renderer

**Do NOT use `subprocess`.** The c7 audit flagged it. Use turtle's `screen.reset()` between tasks instead, or call `t.reset()` between tasks.

```python
def task_01(t, screen):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)
    draw_heng_wide(t, ox=6, oy=-47, scale=0.81)
    save_canvas_to_png(screen, ...)

def main():
    screen = turtle.Screen(); screen.setup(800,600); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()
    task_02(t, screen); screen.update()
    task_03(t, screen); screen.update()
```

Between tasks `t.reset()` clears the canvas, which is what you want.

## Self-preview budget

Max 2 iterations per task. The c6/c7 positions are known to align centerlines tightly — keep those (ox, oy, scale) values:
- 一: (6, -47, 0.81)
- 二 top: (3, 35, 0.45), bottom: (6, -115, 0.80)
- 三 top: (5, 60, 0.42), mid: (4, -38, 0.38), bottom: (14, -140, 0.84)

## Output

One `attempts/cycle_8/generated.py` defining `draw_heng_wide` inline + 3 tasks. 3 PNG outputs.
