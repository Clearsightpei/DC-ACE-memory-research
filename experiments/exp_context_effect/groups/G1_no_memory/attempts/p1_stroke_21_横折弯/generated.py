"""
G1 no-memory attempt: p1_stroke_21_横折弯
Stroke: 横折弯 (horizontal, corner drop, then curves right)
Rendered with PIL to guarantee exact 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw
import math
import os

SIZE = 300
INK = (0, 0, 0)
BG = (255, 255, 255)
WIDTH = 10  # brush thickness for a strong ink stroke


def draw_thick_line(draw, x1, y1, x2, y2, width):
    draw.line((x1, y1, x2, y2), fill=INK, width=width)
    # round-cap the endpoints
    r = width / 2
    draw.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), fill=INK)
    draw.ellipse((x2 - r, y2 - r, x2 + r, y2 + r), fill=INK)


def draw_arc_thick(draw, cx, cy, r, start_deg, end_deg, width, steps=48):
    # Sample points along the arc and connect with short thick segments
    pts = []
    for i in range(steps + 1):
        t = start_deg + (end_deg - start_deg) * i / steps
        rad = math.radians(t)
        pts.append((cx + r * math.cos(rad), cy + r * math.sin(rad)))
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        draw_thick_line(draw, x1, y1, x2, y2, width)


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    # 横折弯 shape:
    #   1) horizontal stroke going right (横)
    #   2) sharp corner turning down (折 — vertical drop)
    #   3) smooth curve sweeping to the right (弯), ending horizontal
    #
    # Layout in a 300x300 canvas:
    #   - 横 starts near upper-left, ends upper-right
    #   - drop from that corner down
    #   - curve arcs from the bottom of the drop to the right

    # 1) horizontal (横) — top bar
    x1_h, y_h = 70, 90
    x2_h = 220
    draw_thick_line(draw, x1_h, y_h, x2_h, y_h, WIDTH)

    # 2) vertical drop (折) — from end of 横 straight down
    x_v = x2_h
    y_v_top = y_h
    y_v_bot = 170
    draw_thick_line(draw, x_v, y_v_top, x_v, y_v_bot, WIDTH)

    # 3) curve (弯) — sweeping down-and-right, ending flat to the right
    # Arc: center to the left of the drop's bottom, radius carries the
    # ink from a downward tangent (matching the vertical) around to a
    # rightward tangent. Using a quarter-arc from angle 180° -> 90°
    # around a center placed at (x_v + r, y_v_bot) sweeps from the
    # drop's bottom rightward and downward, finishing horizontal.
    r = 55
    cx = x_v + r  # center to the right of the drop bottom
    cy = y_v_bot
    # Start at 180° (leftmost point of circle == the drop bottom),
    # sweep to 90° (bottom of circle), i.e. going clockwise from left
    # down to bottom. In PIL image coords y grows down, so angle 90°
    # is below the center — that's the bottom of the curve.
    draw_arc_thick(draw, cx, cy, r, 180, 90, WIDTH, steps=60)

    out_path = os.path.join(os.path.dirname(__file__), "01_横折弯.png")
    img.save(out_path, "PNG")
    print(f"wrote {out_path} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
