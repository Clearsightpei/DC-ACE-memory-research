"""西 (xi) — 6 strokes.

Stroke plan (from GT decomposition):
  1. 一 top horizontal (separate, above the box)
  2. 丨 left vertical of box (down from top of box)
  3. 𠃍 top+right of box (横折, one continuous stroke)
  4. 丿 inner-left short pie
  5. 竖弯 inner-right short vertical with rightward bend at bottom
  6. 一 bottom horizontal (closes the box)

Reference-only note: bank has thin-line renderers; GT uses uniform
thin ~3px lines (per P12), so we render straight PIL lines width=3.
"""
from PIL import Image, ImageDraw
import os

W = 300
H = 300
INK = 0
BG = 255
LW = 3

def draw_xi(draw):
    # Box bounds
    box_left = 60
    box_right = 240
    box_top = 90
    box_bottom = 250

    # 1. Top horizontal (above the box, wider than box)
    draw.line([(55, 55), (245, 60)], fill=INK, width=LW)

    # 2. Left vertical of box
    draw.line([(box_left, box_top), (box_left, box_bottom)],
              fill=INK, width=LW)

    # 3. 横折 — top of box then right vertical
    draw.line([(box_left - 2, box_top), (box_right, box_top)],
              fill=INK, width=LW)
    draw.line([(box_right, box_top), (box_right, box_bottom)],
              fill=INK, width=LW)

    # 4. Inner-left 丿 (short pie leaning left)
    draw.line([(120, 130), (108, 215)], fill=INK, width=LW)

    # 5. Inner-right 竖弯 (short vertical curving right at bottom)
    # approximate with a polyline
    pts = [(185, 130), (188, 190), (195, 210), (210, 218)]
    draw.line(pts, fill=INK, width=LW, joint="curve")

    # 6. Bottom horizontal (closes box)
    draw.line([(box_left, box_bottom), (box_right, box_bottom)],
              fill=INK, width=LW)


def main():
    img = Image.new("L", (W, H), BG)
    d = ImageDraw.Draw(img)
    draw_xi(d)
    out = os.path.join(os.path.dirname(__file__), "01_西.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
