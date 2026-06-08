"""
Cycle 17 — 十 (shi, ten) — BRUSHWORK phase.

Phase B: compose mastered Success Bank components per §5.2/§2.1.
十 = heng + shu, intersecting near the top of the shu.

Endpoints (from approved skeleton):
  - Heng: (-150, +20) → (+150, +20).
  - Shu : (+15, +160) → (+15, -180).

Composition (per task brief):
  draw_heng(t, ox=0,  oy=+20, scale=0.75)   # 0.75 * 200 = 150 → (-150,+20)..(+150,+20) ✓
  draw_shu (t, ox=+15, oy=-10, scale=0.85)  # 0.85 * 200 = 170; +oy=-10 → (+15,+160)..(+15,-180) ✓

No skeleton-endpoint change; brushwork inherited verbatim from c1 (heng) and c2 (shu).
"""

import sys
import os
import turtle

# Allow importing the mastered Success Bank primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_SUCCESS_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _SUCCESS_BANK)

from heng import draw as draw_heng  # noqa: E402
from shu import draw as draw_shu    # noqa: E402


def setup():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    return screen, t


def main():
    screen, t = setup()

    # ── Task 01 | 十 | shi
    draw_heng(t, ox=0, oy=+20, scale=0.75)
    draw_shu(t, ox=+15, oy=-10, scale=0.85)

    screen.update()

    canvas = screen.getcanvas()
    ps_path = "01_shi.ps"
    canvas.postscript(file=ps_path, colormode="color")

    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.save("01_十.png", "png")
    except Exception as e:
        print(f"PIL conversion failed: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
