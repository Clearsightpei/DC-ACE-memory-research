# BANK_DEVIATION
# skipped: fang.py  (fang.py encodes 匚, not 方; entirely different shape)
# reason: 方 (radical 093 and char 0104) is in terminal errata — no bank
#         entry exists for the 方 shape (dian+heng+heng_zhe_gou+pie).
#         Similarly 攵 (radical 110) is in errata — no bank entry.
#         Building 放 fully fresh inline, reusing the 攵 recipe pattern
#         from p3_char_0349_改's successful-shape composition.
# fresh_component: fang_left_for_LR, pu_right_for_LR
#
# 放 = 方 (LEFT, ~x 20..140) + 攵 (RIGHT, ~x 150..295)
#   方 = 点 + 横 + 横折钩 (box outline) + 撇 (inside sweeping down-left)
#   攵 = 短撇 + 横 + 长撇 + 捺 (crossing X below the heng)

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


def draw_fang_left(d):
    # 方 fitted to left of 放 (x ~20..140, y ~50..270)
    # Stroke 1: 点 (dian) — small dot upper-left, angled down-right
    _tapered_bezier(d, (55, 58), (60, 68), (68, 82), 3, 8)
    # Stroke 2: 横 — long heng below the dian, spans full radical width
    _tapered_line(d, (22, 108), (140, 108), 6, 8)
    _dot_blob(d, 140, 108, 5)
    # Stroke 3: 横折钩 — heng starts near mid, turns down at right, hook left
    # heng segment
    _tapered_line(d, (48, 140), (128, 140), 7, 8)
    _dot_blob(d, 128, 140, 5)
    # shu going down
    _tapered_line(d, (128, 140), (125, 245), 8, 10)
    # gou (hook) at bottom — curls left-up
    _tapered_bezier(d, (125, 245), (117, 258), (95, 250), 10, 4)
    # Stroke 4: 撇 — starts inside top of the box, sweeps down-left to bottom
    _tapered_bezier(d, (72, 138), (55, 200), (20, 270), 5, 11)


def draw_pu_right(d):
    # 攵 fitted to right of 放 (x ~150..295, y ~55..285)
    # Stroke 1: short 撇 at top-right
    _tapered_bezier(d, (218, 62), (208, 88), (192, 118), 4, 8)
    # Stroke 2: 横 — long crossing bar through pie tail
    _tapered_line(d, (160, 118), (285, 115), 7, 9)
    # Stroke 3: long 撇 — starts just below heng near right, sweeps to bottom-left
    _tapered_bezier(d, (228, 130), (198, 200), (152, 285), 5, 11)
    # Stroke 4: 捺 — starts from mid of 撇, sweeps down-right with heavy tail
    _tapered_bezier(d, (202, 178), (245, 225), (293, 282), 5, 13)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_fang_left(d)
    draw_pu_right(d)
    img.save("01_放.png")


if __name__ == "__main__":
    main()
