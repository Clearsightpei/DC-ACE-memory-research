"""Cycle 15 brushwork phase — 二 (er).

Composes the mastered 横 (c1) twice via translate+scale per §2.1/§5.2.
NO endpoint changes from the approved skeleton:

  Top    heng: target (-90, +50)  → (+50, +50)
      center_x = -20, scale = 140/400 = 0.35
      → draw_heng(t, ox=-20, oy=+50, scale=0.35)

  Bottom heng: target (-130, -100) → (+130, -100)
      center_x = 0, scale = 260/400 = 0.65
      → draw_heng(t, ox=0, oy=-100, scale=0.65)

The canonical heng has its own ±3 px tilt; the center y aligns with
target ±3 (acceptable since the brief notes the tilt is inherited).
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

    # ── Task 01 | 二 | er ──
    # Top heng — short (scale 0.35), shifted left to center on -20.
    draw_heng(t, ox=-20, oy=+50, scale=0.35)

    # Bottom heng — long (scale 0.65), centered on 0.
    draw_heng(t, ox=0, oy=-100, scale=0.65)

    screen.update()
    canvas = screen.getcanvas()
    canvas.postscript(file="01_二.eps")

    try:
        from PIL import Image
        img = Image.open("01_二.eps")
        img.load(scale=2)
        img.save("01_二.png", "PNG")
    except Exception as e:
        print(f"PNG conversion fallback: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
