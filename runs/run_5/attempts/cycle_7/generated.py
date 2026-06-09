"""
Cycle 7 — thin-variant heng applied to 一 / 二 / 三.

c6 used the brushed run_4 heng.py (width 11→19). MMH GT skeleton is ~3 px,
so brushed over-paints and visual caps at ~0.88. Hard gate is > 0.9.

Strategy: same centerline (Bezier endpoints, same tilt), uniform pensize 3.
Reuse `brushed_bezier` from success_bank heng.py — it's just the per-sample
walker; passing a constant `lambda s: 3.0` makes the stroke uniform.

Positioning measured from GT pixel bands (numpy dark<100 row clusters),
matching c6's approach. Turtle canvas 800x600, center (400,300), y-up.

Each task runs in its own subprocess so the turtle module state is fresh.
"""

import os
import subprocess
import sys
import turtle

from PIL import Image

_HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(_HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

# Reuse brushed_bezier from the mastered heng entry — uniform width by passing constant lambda.
from heng import brushed_bezier  # noqa: E402


def draw_heng_thin(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Thin 横 — uniform pensize 3, matches MMH skeleton width exactly.

    Same canonical endpoints as the brushed heng: P0=(-200,-3), P3=(+200,+3),
    a gentle ~6 px upward tilt. The only difference is the width profile —
    constant 3 instead of the 16→11→19 brushed profile. This is the variant
    to use when targeting MMH GT visual_score > 0.9.
    """
    P0 = (-200.0 * scale + ox, -3.0 * scale + oy)
    P3 = (200.0 * scale + ox, 3.0 * scale + oy)
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: 3.0, samples=220)


# (ox, oy, scale) measured from GTs.
TASKS = {
    "01_一.png": [(6.0, -47.0, 0.81)],
    "02_二.png": [(3.0, 35.0, 0.45),
                  (6.0, -115.0, 0.80)],
    "03_三.png": [(5.0, 60.0, 0.42),
                  (4.0, -38.0, 0.38),
                  (14.0, -140.0, 0.84)],
}


def render_one(out_name, strokes):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.setworldcoordinates(-400, -300, 400, 300)
    screen.tracer(0, 0)
    screen.bgcolor("white")

    t = turtle.Turtle(visible=False)
    t.speed(0)
    t.pencolor("black")

    for (ox, oy, scale) in strokes:
        draw_heng_thin(t, ox=ox, oy=oy, scale=scale)

    screen.update()

    out_path = os.path.join(_HERE, out_name)
    ps_path = out_path.replace(".png", ".ps")
    canvas = screen.getcanvas()
    canvas.postscript(file=ps_path, colormode="color",
                      x=-400, y=-300, width=800, height=600)

    img = Image.open(ps_path)
    img.load(scale=4)
    img = img.convert("RGB").resize((800, 600), Image.LANCZOS)
    img.save(out_path, "PNG")
    os.remove(ps_path)


def main():
    if len(sys.argv) > 1:
        # subprocess invocation: render the one task whose name was given
        out_name = sys.argv[1]
        render_one(out_name, TASKS[out_name])
        return

    # parent: fan out one subprocess per task for clean turtle state
    for out_name in TASKS:
        result = subprocess.run(
            [sys.executable, __file__, out_name],
            cwd=_HERE,
        )
        if result.returncode != 0:
            sys.exit(f"render failed for {out_name}")


if __name__ == "__main__":
    main()
