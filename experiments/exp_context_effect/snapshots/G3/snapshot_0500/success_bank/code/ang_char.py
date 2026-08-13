# p3_char_0153_卬 (áng) — 4 strokes.
# REVISION 1: better GT match.
#   - Connect 撇 tail to top of 竖提 vertical (left half).
#   - Steepen the 竖提 rising tail.
#   - Right 卩: the 横折钩's vertical drop should end near the long right 竖's
#     upper section, not run parallel far apart. Widen the D and let the
#     long 竖 start from the top-right of the D.
#
# Format: thin uniform lines (MMH-GT style, per principle P12).

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_卬.png")


def _line(draw, pts, w=4):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)


def _bez(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def draw_ang(t, ox=0, oy=0, scale=1.0):
    W = 4

    # ---- LEFT half ----
    # Stroke 1: 撇 — from around (110, 78) curving down-left, joining
    # the top of the 竖提's vertical near (78, 118).
    pie_pts = _bez((110 + ox, 78 + oy), (95 + ox, 100 + oy),
                   (78 + ox, 120 + oy), 24)
    _line(t, pie_pts, W)

    # Stroke 2: 竖提 — long vertical from (78, 118) straight down to
    # about (78, 235), then a rising tail sweeping up-right to (145, 210).
    _line(t, [(78 + ox, 118 + oy), (78 + ox, 235 + oy)], W)
    ti_pts = _bez((78 + ox, 235 + oy), (108 + ox, 232 + oy),
                  (145 + ox, 210 + oy), 20)
    _line(t, ti_pts, W)

    # ---- RIGHT half (卩) ----
    # Stroke 3: 横折钩 — top-right D shape.
    # 横 from (160, 92) to (218, 88), then 折 curving down to (210, 165),
    # then a small 钩 hooking back to (198, 168).
    _line(t, [(160 + ox, 92 + oy), (218 + ox, 88 + oy)], W)
    zhe_pts = _bez((218 + ox, 88 + oy), (222 + ox, 130 + oy),
                   (210 + ox, 165 + oy), 24)
    _line(t, zhe_pts, W)
    _line(t, [(210 + ox, 165 + oy), (198 + ox, 168 + oy)], W)

    # Stroke 4: 竖 — long vertical for 卩's right leg,
    # starting near the 横's right end at (218, 92) going down to (218, 258).
    # Actually GT shows the long vertical is INSIDE/left of the D-hook,
    # descending from the横起笔 area. Place it starting at (180, 108)
    # going down to (180, 260).
    _line(t, [(180 + ox, 108 + oy), (180 + ox, 260 + oy)], W)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ang(draw, ox=0, oy=0, scale=1.0)
    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
