"""p3_char_0288_凫 — 凫 (fú, wild duck).

Structure: simplified bird-head top (small 撇 + closed box with an interior
tick + a top-right dot/tick) sitting above a wide 几 that carries the bottom.

Top is inlined thin strokes (P12 — MMH GT is thin uniform). Bottom uses the
frozen bank `draw_ji` (bank #41) scaled slightly larger and pushed down.
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_G3 = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _G3)

from ji import draw_ji  # noqa: E402

W = H = 300


def _line(draw, p0, p1, width=5):
    draw.line([p0, p1], fill=(0, 0, 0), width=width)
    # round caps
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _bezier(draw, p0, p1, p2, w=5, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
        prev = (bx, by)


def draw_fu_duck(draw):
    # --- Top half: simplified bird head, occupying roughly y=25..140 ---

    # 1. Slanted 撇 forming the head's crown, from upper-right down to
    #    the top-left of the box.
    _bezier(draw, (150, 28), (128, 52), (108, 78), w=5, steps=30)

    # 2. Closed box (bird-head shape).
    box_top, box_bot = 78, 140
    box_l, box_r = 108, 188
    # Top heng (bird-head top).
    _line(draw, (box_l, box_top), (box_r, box_top), width=5)
    # Left shu.
    _line(draw, (box_l, box_top), (box_l + 2, box_bot), width=5)
    # Right shu with slight lean-in.
    _line(draw, (box_r, box_top), (box_r - 3, box_bot), width=5)
    # Bottom heng closing the box.
    _line(draw, (box_l + 2, box_bot), (box_r - 3, box_bot), width=5)
    # Interior horizontal (bird's eye stripe).
    _line(draw, (box_l + 8, 112), (box_r - 8, 112), width=4)

    # 3. Small upward tick on box's top-right (a slight hook).
    _bezier(draw, (box_r, box_top - 2), (box_r + 8, box_top - 12),
            (box_r + 4, box_top - 20), w=4, steps=18)

    # --- Bottom half: 几 (spans below the head, staying on canvas) ---
    # Raw ji: top y=95, bottom y=260; height 165. With scale=0.85,
    # oy=-42 places top ~y=145 and bottom ~y=285 (see _apply: uses cy - oy).
    draw_ji(draw, ox=0, oy=-42, scale=0.85)


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_fu_duck(draw)
    out = os.path.join(_HERE, "01_凫.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
