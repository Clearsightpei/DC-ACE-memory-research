# p3_char_0141_办 — 4 strokes: 横折钩 + 撇 + 左点 + 右点
# 力 base (横折钩 top-right + long 撇 crossing) with two side dots (八-style).
# Inline PIL. Coords chosen deliberately per TR1-TR3 (no default bank calls).
# GT observed: 力 sits center; hook loop is small at bottom of 折; long pie
# sweeps from top of 横折钩's corner down-left; two dots on either side
# perch high on the character (dots start above pie tail level).

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _tapered_line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_ban(D, ox=0, oy=0, scale=1.0):
    def X(x): return 150 + (x - 150) * scale + ox
    def Y(y): return 150 + (y - 150) * scale + oy

    W = max(2, int(4 * scale))

    # 力 is the central component; two dots flank left & right.
    # 力's horizontal (heng of 横折钩) spans roughly x=120..190 in GT,
    # near y=110. Vertical shaft descends to y~230, then hooks left.
    # The 撇 crosses through the 横 near its LEFT third and sweeps
    # to lower-left, tail near (75, 260).

    # Stroke 1: 横折钩 — 横 across upper mid → 折 down → 钩 up-left
    hzg_start = (X(118), Y(112))
    hzg_corner = (X(190), Y(108))
    hzg_bot = (X(188), Y(225))
    _tapered_line(D, hzg_start, hzg_corner, W, W + 1, 24)
    _tapered_line(D, hzg_corner, hzg_bot, W + 1, W, 32)
    # hook — small up-left flick
    hook_end = (X(168), Y(212))
    _tapered_line(D, hzg_bot, hook_end, W, max(1, W - 2), 14)

    # Stroke 2: 撇 — starts near top of 横 (crossing it), sweeps down-left
    pie_start = (X(138), Y(88))
    pie_end = (X(65), Y(258))
    # Control: bow leftward for the characteristic 撇 arc
    ctrl = (X(90), Y(190))
    _tapered_bezier(D, pie_start, ctrl, pie_end, W + 2, 1, steps=60)

    # Stroke 3: 左点 (short down-left pie-like dot) — perches on left,
    # roughly at mid-height (y~155) just left of the pie
    ld_start = (X(90), Y(150))
    ld_end = (X(65), Y(190))
    ld_ctrl = (X(75), Y(172))
    _tapered_bezier(D, ld_start, ld_ctrl, ld_end, max(2, W - 1), max(1, W - 2), steps=22)

    # Stroke 4: 右点 (na-like) — thin top → heavy tail, on right of 力
    rd_start = (X(205), Y(148))
    rd_end = (X(240), Y(195))
    rd_ctrl = (X(220), Y(168))
    _tapered_bezier(D, rd_start, rd_ctrl, rd_end, max(1, W - 2), W + 2, steps=22)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_ban(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_办.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
