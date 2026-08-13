# p3_char_0324_但 — 但 (dàn), 7 strokes.
# Decomposition: 亻 (left radical, 2 strokes: 撇 + 竖) + 旦 (right, 5 strokes).
# 旦 = 日 (4 strokes) + 一 (1 long horizontal underneath).
# Composition: 亻 hugs the left third; 旦 fills the right two-thirds — 日 sits
# in the upper-middle band, then a long 一 spans nearly the full right span.
# GT is MMH-style thin uniform strokes — keep widths ~4-5 px (P12).
# Inline fresh (v8 posture): trust GT over bank; bank 日 has its own bounding
# box that doesn't fit the right-side slot of 但.

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=45):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        cur = (bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r],
                         fill=(0, 0, 0))
        prev = cur


def line_stroke(draw, p0, p1, w_head, w_tail, n=25):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r],
                         fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亻 (left radical) ----------
    # Stroke 1: 撇 — head upper-mid-left, sweeps down-left.
    bezier_stroke(d,
                  to_px(-55, 100),
                  to_px(-80, 15),
                  to_px(-105, -80),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft, tail low.
    line_stroke(d,
                to_px(-58, 30),
                to_px(-58, -105),
                w_head=5, w_tail=5, n=40)

    # ---------- 旦 (right side) ----------
    # 日 box — compact, upper-mid right band.
    # Box bounds (math coords): x_left=-5, x_right=80, y_top=100, y_bot=-25
    XL, XR = -5, 80
    YT, YB = 100, -25
    YM = int((YT + YB) / 2)  # middle heng row
    W = 5

    # Stroke 3: left 竖 of 日
    line_stroke(d, to_px(XL, YT), to_px(XL, YB), W, W, n=30)
    # Stroke 4: 横折 — top heng + right shu (drawn as two segments, one stroke)
    line_stroke(d, to_px(XL, YT), to_px(XR, YT), W, W, n=30)
    line_stroke(d, to_px(XR, YT), to_px(XR, YB), W, W, n=30)
    # Stroke 5: 横 (middle) — slightly inset on right per GT
    line_stroke(d, to_px(XL + 2, YM), to_px(XR - 4, YM),
                max(1, W - 1), max(1, W - 1), n=25)
    # Stroke 6: 横 (bottom of 日)
    line_stroke(d, to_px(XL, YB), to_px(XR, YB), W, W, n=30)

    # Stroke 7: 一 — long bottom heng of 旦, spans wider than 日 (GT shows
    # the underline extending well past the 日 box on both sides).
    line_stroke(d,
                to_px(-45, -80),
                to_px(120, -80),
                w_head=5, w_tail=5, n=50)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_但.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
