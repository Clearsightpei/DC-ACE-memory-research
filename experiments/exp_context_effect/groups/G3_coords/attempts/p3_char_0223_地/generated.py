# p3_char_0223_地 (dì, "earth/ground") — L-R compound: 土 (left) + 也 (right)
#
# Revision 2: tighter 土 (bank primitive was too spread at scale 0.5),
# and inline 也 with proper 横折 top + central shu + 竖弯钩 envelope,
# all three strokes touching where they should. drawer_memory says
# do NOT compose 3 primitives horizontally for 也 — inline as an
# integrated shape.

import os
import math
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = 150


def m2p(x, y):
    return (CX + x, CY - y)


def draw_tu_left(draw, ox=0.0, oy=0.0, w=6):
    """Inline 土 as left radical: two hengs + a shu, compact."""
    # top heng (short)
    draw.line([m2p(ox - 20, oy + 32), m2p(ox + 20, oy + 32)], fill="black", width=w)
    # central shu, connects top heng to bottom heng
    draw.line([m2p(ox, oy + 32), m2p(ox, oy - 32)], fill="black", width=w)
    # bottom heng (提 style — slight rise toward right; wider than top)
    draw.line([m2p(ox - 26, oy - 32), m2p(ox + 26, oy - 26)], fill="black", width=w)


def draw_ye_inline(draw, ox=0.0, oy=0.0, scale=1.0, w=6):
    """Inline 也 (yě). Three strokes:
      1) 横折钩: top horizontal + short downward-hook segment on the right
      2) 竖: central vertical piercing down through the interior
      3) 竖弯钩: left-descent + bottom rightward curve + tiny upward hook
    """
    s = scale

    # --- 1) 横折钩 (top): horizontal from upper-left to upper-right,
    # then a short drop on the right end
    top_l = m2p(ox - 45 * s, oy + 40 * s)
    top_r = m2p(ox + 50 * s, oy + 40 * s)
    top_drop_end = m2p(ox + 50 * s, oy + 15 * s)
    draw.line([top_l, top_r, top_drop_end], fill="black", width=w, joint="curve")

    # --- 2) central 竖 piercing top heng down into interior
    shu_top = m2p(ox + 10 * s, oy + 55 * s)
    shu_bot = m2p(ox + 10 * s, oy - 25 * s)
    draw.line([shu_top, shu_bot], fill="black", width=w)

    # --- 3) 竖弯钩 envelope: start upper-left, drop, curve right, small hook up
    env_pts = []
    # vertical descent
    xL = ox - 30 * s
    yTop = oy + 30 * s
    yBot = oy - 40 * s
    env_pts.append(m2p(xL, yTop))
    env_pts.append(m2p(xL, yBot))
    # arc from (xL, yBot) sweeping right and up-tangent, radius r
    r = 50 * s
    cx_a = xL + r
    cy_a = yBot
    steps = 24
    for i in range(1, steps + 1):
        theta = math.pi + (math.pi / 2) * (i / steps)  # pi -> 3pi/2
        px = cx_a + r * math.cos(theta)
        py = cy_a + r * math.sin(theta)
        env_pts.append(m2p(px, py))
    # tiny hook up
    last_x, last_y = env_pts[-1]
    env_pts.append((last_x, last_y - 12))  # pixel-up = math-up
    draw.line(env_pts, fill="black", width=w, joint="curve")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # LEFT: 土 radical — narrow, at ox=-80
    draw_tu_left(draw, ox=-80, oy=0, w=6)

    # RIGHT: 也 inline at ox=+55, slight downshift
    draw_ye_inline(draw, ox=55, oy=-5, scale=1.0, w=6)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_地.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
