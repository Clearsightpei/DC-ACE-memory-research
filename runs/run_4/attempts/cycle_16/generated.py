"""Cycle 16 brushwork phase — 三 (san).

Composes the mastered 横 (c1) three times via translate+scale per §2.1/§5.2.
NO endpoint changes from the approved skeleton:

  Top    heng: target (-90, +90)  → (+50, +90)
      center_x = -20, scale = 140/400 = 0.35
      → draw_heng(t, ox=-20, oy=+90, scale=0.35)

  Middle heng: target (-100, -10) → (+50, -10)
      center_x = -25, scale = 150/400 = 0.375 ≈ 0.38
      → draw_heng(t, ox=-25, oy=-10, scale=0.38)

  Bottom heng: target (-130, -120) → (+150, -120)
      center_x = +10, scale = 280/400 = 0.70
      → draw_heng(t, ox=+10, oy=-120, scale=0.70)

The canonical heng has its own ±3 px tilt; the center y aligns with
target ±3 (acceptable since tilt is inherited).
"""

import os
import sys
import turtle

# Import the mastered 横 from success_bank.
_HERE = os.path.dirname(os.path.abspath(__file__))
_SUCCESS_BANK_CODE = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
sys.path.insert(0, _SUCCESS_BANK_CODE)
from heng import draw as draw_heng  # noqa: E402


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    # ── Task 01 | 三 | san ──
    # Top heng — short (scale 0.35), shifted left to center on -20.
    draw_heng(t, ox=-20, oy=+90, scale=0.35)

    # Middle heng — slightly longer (scale 0.38), centered on -25.
    draw_heng(t, ox=-25, oy=-10, scale=0.38)

    # Bottom heng — longest (scale 0.70), centered on +10.
    draw_heng(t, ox=+10, oy=-120, scale=0.70)

    screen.update()
    canvas = screen.getcanvas()
    canvas.postscript(file="01_三.eps")

    try:
        from PIL import Image
        img = Image.open("01_三.eps")
        img.load(scale=2)
        img.save("01_三.png", "PNG")
    except Exception as e:
        print(f"PNG conversion fallback: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
