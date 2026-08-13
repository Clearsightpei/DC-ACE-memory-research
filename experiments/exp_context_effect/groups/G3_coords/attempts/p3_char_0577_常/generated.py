# BANK_DEVIATION
# skipped: shang_char.py (that's 上, not 尚), no 尚/巾 primitives exist
# reason: 常 = 尚 (top: 小+冖+口) + 巾 (bottom). No bank primitives match
#         the top-piece 尚 or bottom-piece 巾 at required scales;
#         inlining fresh keeps proportions faithful to GT.
# fresh_component: shang_top_for_chang, jin_bottom_for_chang

import os
from PIL import Image, ImageDraw


def _tapered_line(draw, p0, p1, w0, w1, n=32):
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = p0[0] + u0 * (p1[0] - p0[0])
        y0 = p0[1] + u0 * (p1[1] - p0[1])
        x1 = p0[0] + u1 * (p1[0] - p0[0])
        y1 = p0[1] + u1 * (p1[1] - p0[1])
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0),
                  width=max(1, int(round(w))))


def _bez(draw, p0, pc, p1, w0, w1, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
        prev = (bx, by)


def _dot(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))


def draw_chang(draw):
    # ===== TOP: 尚 upper part (小-like 3 strokes) =====
    # Center: short dian/vertical dot at top
    _bez(draw, (150, 50), (150, 60), (150, 78), 4.5, 6.5)
    _dot(draw, 150, 78, 4)
    # Left short 撇 (small)
    _bez(draw, (128, 62), (118, 74), (108, 88), 5.5, 2.0)
    # Right dot going down-right
    _bez(draw, (172, 58), (183, 68), (192, 82), 3.0, 5.5)
    _dot(draw, 192, 82, 3.5)

    # ===== 冖-like broad cap =====
    # left short slanting dian at cap's TL start
    _bez(draw, (60, 100), (65, 108), (72, 118), 3.0, 5.0)
    # top horizontal (long heng across cap)
    _tapered_line(draw, (58, 108), (240, 105), 5.5, 5.5)
    # right shu descending — the 横折 of cap
    _tapered_line(draw, (240, 105), (236, 135), 5.5, 5.0)

    # ===== Small 口 (roughly square, sits under cap centrally) =====
    L, R, T, B = 108, 192, 122, 160
    # left shu
    _tapered_line(draw, (L, T), (L, B), 4.5, 4.0)
    # top heng + right shu (横折)
    _tapered_line(draw, (L, T), (R, T), 4.5, 4.5)
    _tapered_line(draw, (R, T), (R, B), 4.5, 4.0)
    # bottom heng
    _tapered_line(draw, (L, B), (R, B), 4.5, 4.5)

    # ===== BOTTOM: 巾 =====
    # Left short 撇 (starting stroke of 巾, curves down-left)
    _bez(draw, (88, 178), (82, 205), (72, 240), 5.5, 3.0)
    # Top heng of 巾
    _tapered_line(draw, (88, 178), (215, 175), 5.5, 5.5)
    # Right shu going down (from 横折)
    _tapered_line(draw, (215, 175), (212, 250), 5.5, 5.0)
    # Hook at bottom of right shu (curls left)
    _bez(draw, (212, 250), (206, 251), (196, 244), 5.0, 2.0)
    # Central long shu (descender all the way down)
    _tapered_line(draw, (150, 165), (150, 282), 6.5, 5.5)


def main():
    W, H = 300, 300
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_chang(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_常.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
