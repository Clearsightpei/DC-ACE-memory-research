# p3_char_0557_圆 (yuán, "circle/round") — 10 strokes
#
# Structure: outer 囗 enclosure + inner 员 (口 above, 贝-simplified below).
# The inner 员 = 口 (top) + 冂 rectangle with 2 short inner hengs + 八 splay legs.
#
# Recipe:
#   - outer 囗 via bank wei_radical (scale 1.0)  — same as 回/国
#   - inner 口 small at top (bank kou at scale 0.42, nudged up)
#   - inner 贝-simplified inline below (small 冂 with 2 inner hengs + 八 feet)
#
# BANK_DEVIATION is NOT triggered — bank wei_radical and kou fit fine
# for their sub-roles. The 贝-simplified bottom is inline (no bank
# entry for 贝 exists).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from wei_radical import draw_wei_radical  # noqa: E402
from kou import draw_kou                  # noqa: E402


def draw_bei_simplified(t, cx, top_y, width, height):
    """贝 simplified: 冂 rectangle with 2 inner hengs + 八 splay feet.
    cx = center x, top_y = top of rectangle, width/height = box size.
    Feet splay below the box's bottom-left/bottom-right corners.
    """
    W = 3  # thin uniform stroke width matching MMH
    left = cx - width // 2
    right = cx + width // 2
    bot_y = top_y + height

    # 冂 top-left vertical
    t.line([(left, top_y), (left, bot_y)], fill=(0, 0, 0), width=W)
    # 冂 top + right vertical (as one 横折 shape)
    t.line([(left, top_y), (right, top_y)], fill=(0, 0, 0), width=W)
    t.line([(right, top_y), (right, bot_y)], fill=(0, 0, 0), width=W)
    # bottom heng closing the rectangle
    t.line([(left, bot_y), (right, bot_y)], fill=(0, 0, 0), width=W)

    # 2 inner short hengs (divide box into 3 rows)
    inner_left = left + 3
    inner_right = right - 3
    y1 = top_y + height // 3
    y2 = top_y + 2 * height // 3
    t.line([(inner_left, y1), (inner_right, y1)], fill=(0, 0, 0), width=W)
    t.line([(inner_left, y2), (inner_right, y2)], fill=(0, 0, 0), width=W)

    # 八 splay feet below the box (from bottom corners, splaying outward)
    foot_dx = 14
    foot_dy = 18
    # left foot (撇-like, going down-left)
    t.line([(left, bot_y), (left - foot_dx, bot_y + foot_dy)],
           fill=(0, 0, 0), width=W)
    # right foot (点-like, going down-right)
    t.line([(right, bot_y), (right + foot_dx, bot_y + foot_dy)],
           fill=(0, 0, 0), width=W)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Outer 囗 — fills canvas, standard identity-alias scale.
    draw_wei_radical(t, ox=0, oy=0, scale=1.0)

    # Inside the outer 囗, the usable interior is approximately
    # x ∈ [78, 202], y ∈ [78, 222] in pixel coords (from wei_radical geometry).
    # Center x ≈ 140.

    # Inner 口 (top of 员) — modest, upper portion of interior.
    # kou at scale 0.50 → ~65px wide box. Nudged up.
    draw_kou(t, ox=-10, oy=48, scale=0.50)

    # Inner 贝-simplified — below the 口, filling the lower interior
    # so the composition doesn't look sparse. Box ~85 wide × 68 tall,
    # feet splay 14px past the corners so they read as legs, not stubs.
    draw_bei_simplified(t, cx=140, top_y=138, width=88, height=68)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_圆.png")
    img.save(out_path)


if __name__ == "__main__":
    main()
