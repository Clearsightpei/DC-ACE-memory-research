# p3_char_0092_廾 (nian, "clasped hands"), 4 strokes based on GT visual:
#   1. short 横 top-left cap
#   2. long 撇 curving from upper-mid down to lower-left
#   3. long 横 crossbar spanning left-right below middle
#   4. 竖 right vertical from mid-upper down to bottom
# Inline PIL rendering (no bank primitive fits without heavy transform).
import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_廾.png")

W, H = 300, 300


def _P(bx, by, ox, oy, scale):
    # math-convention -> PIL pixel
    return (150 + ox + bx * scale, 150 - oy - by * scale)


def _curve(t, p0, p1, p2, width, steps=40):
    # quadratic Bezier polyline
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    t.line(pts, fill=(0, 0, 0), width=width)


def draw_nian2(t, ox=0, oy=0, scale=1.0):
    w = max(1, int(round(6 * scale)))

    # Stroke 1: short 横 cap top-left, joins near the top of the 撇
    t.line([_P(-55, +40, ox, oy, scale), _P(-18, +40, ox, oy, scale)],
           fill=(0, 0, 0), width=w)

    # Stroke 2: long 撇 — starts high near cap end, curves down-left
    _curve(t,
           _P(-20, +45, ox, oy, scale),
           _P(-40, -25, ox, oy, scale),
           _P(-72, -85, ox, oy, scale),
           width=w)

    # Stroke 3: long horizontal crossbar (通横), spans across at ~ mid-low
    t.line([_P(-95, -15, ox, oy, scale), _P(+90, -15, ox, oy, scale)],
           fill=(0, 0, 0), width=w)

    # Stroke 4: right 竖 — vertical from upper-mid down to bottom
    t.line([_P(+40, +50, ox, oy, scale), _P(+45, -90, ox, oy, scale)],
           fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_nian2(t, ox=0, oy=0, scale=1.0)
    img.save(OUT_PNG)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
