# p2_radical_001_丨 — 1画部首 竖 radical.
#
# GT observation: the radical form of 丨 shows a slight rightward-scooping
# head at the top (~10-15 px arc down-right) and then a long straight
# vertical descent. This is NOT identical to shu (pure straight vertical);
# per P7 caveat + P10 analogue, when the radical form has a softer
# head than the mastered stroke, build a variant rather than default-
# calling the primitive.
#
# Strategy: inline a shu-like vertical shaft with a small curved head.
# Draw as a spine + width (per P3, P4) with uniform ~12 px thickness.
#
# Placement (canvas 300x300, center origin, +y up per P5):
#   head start ≈ (0, +80)  scoop right-down to (+3, +65)
#   shaft continues straight down to (+3, -100)
# Convert to PIL pixels: (px, py) = (150 + ox, 150 - oy)

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_丨.png")


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_radical_shu(draw):
    # Revised: GT shows a pronounced rightward-curving head — extend the
    # arc further right (~10 px) and start the head higher up. Shaft
    # thickness bumped from 8 to 10 to better match GT ink weight.
    #
    # Head arc: from (-6, +85) scooping down-right to (+4, +60)
    head_pts = [
        _to_pixel(-6, 85),
        _to_pixel(-3, 80),
        _to_pixel(0, 74),
        _to_pixel(3, 68),
        _to_pixel(4, 60),
    ]
    # Straight vertical shaft: from (+4, +60) down to (+4, -100)
    shaft_top = _to_pixel(4, 60)
    shaft_bot = _to_pixel(4, -100)

    thickness = 10  # radical stroke ink weight matches GT better at 10
    # Draw head arc
    draw.line(head_pts, fill=(0, 0, 0), width=thickness, joint="curve")
    # Draw shaft
    draw.line([shaft_top, shaft_bot], fill=(0, 0, 0), width=thickness)
    # Round the top cap
    r = thickness / 2
    hx, hy = head_pts[0]
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))
    # Round the bottom (soft foot)
    bx, by = shaft_bot
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_radical_shu(draw)
    img.save(OUT_PNG)


if __name__ == "__main__":
    main()
