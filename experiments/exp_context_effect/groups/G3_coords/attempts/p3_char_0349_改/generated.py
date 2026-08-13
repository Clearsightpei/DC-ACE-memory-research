# BANK_DEVIATION
# skipped: si.py  (the 巳 primitive; sibling of 己 but 己 has an open top-right
#                  and different bottom sweep, and si.py is sized for standalone
#                  radical use — needs shrunk-left version for L-R char)
# reason: 改 needs 己 on the LEFT at ~0.55 scale of a full 300px canvas, and 己
#         differs from 巳 in that its top-横折 does NOT close down into the
#         middle-横 (gap between 横折 tail and 横 left). si.py is closed.
# fresh_component: ji_left_for_gai  (compact 己 for L-R char position)

# 改 = 己 (left, compact upper-mid) + 攵 (right, top short pie + long heng +
# X of pie/na at bottom). No bank hit for 攵 (in terminal errata) nor for 己
# (terminal errata). Fully fresh inline PIL, math-free pixel coords.

from PIL import Image, ImageDraw

INK = (0, 0, 0)


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _dot_blob(draw, cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK)


def draw_ji_left_for_gai(d):
    # 己 fitted to left side of 改 (x ~25..130, y ~95..230)
    # Stroke 1: 横折 — top heng then SHORT 竖 down; leave clear GAP before middle heng
    _tapered_line(d, (28, 105), (120, 105), 8, 10)
    _dot_blob(d, 120, 105, 5)
    _tapered_line(d, (120, 105), (120, 128), 10, 8)   # short down; ends well above mid-heng
    # Stroke 2: 竖弯钩 body — starts at top-left, sweeps down and right with hook up
    _tapered_line(d, (28, 105), (28, 205), 9, 10)
    _tapered_bezier(d, (28, 205), (55, 232), (140, 220), 10, 11)
    # tiny hook up
    _tapered_line(d, (140, 220), (134, 202), 11, 3)


def draw_pu_right_for_gai(d):
    # 攵 fitted to right of 改 (x ~150..295, y ~60..285)
    # Stroke 1: short 撇 at top-right; tail lands near where heng will cross
    _tapered_bezier(d, (218, 65), (208, 90), (195, 118), 4, 8)
    # Stroke 2: 横 — long crossing bar; passes THROUGH the pie tail area
    _tapered_line(d, (162, 118), (285, 115), 7, 9)
    # Stroke 3: long 撇 — starts from just below heng, sweeps down-left to bottom
    _tapered_bezier(d, (225, 128), (195, 200), (152, 285), 5, 11)
    # Stroke 4: 捺 — starts from mid of 撇 (~y=190) sweeps down-right with heavy tail
    _tapered_bezier(d, (200, 175), (245, 225), (292, 282), 5, 13)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_ji_left_for_gai(d)
    draw_pu_right_for_gai(d)
    img.save("01_改.png")


if __name__ == "__main__":
    main()
