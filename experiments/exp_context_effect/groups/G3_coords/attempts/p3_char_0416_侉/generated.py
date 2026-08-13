# p3_char_0416_侉 — G3 attempt.
# 侉 = 亻 (left, 2 strokes) + 夸 (right, 6 strokes) = 8 strokes.
# 夸 = 大 (top: 撇 + 一 + 捺) + 亏 (bottom: 一 + 横折折弯钩 ...actually 3 strokes).
# We use: 亻 (bank-like inline: pie + shu), 大 (small at top-right),
# 亏 (wide heng + 横折折弯钩 -- two visible strokes below 大).
# BANK_DEVIATION: gt shows 大 with pie+heng+na very compact at top-right,
# and 亏 wider than 大. Inlining fresh — no bank fu/kua entry exists.
# Recipe adapted from zhan_char.py (亻 side) + hand-inlined 夸 (右侧).

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=50):
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
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def line_stroke(draw, p0, p1, w_head, w_tail, n=30):
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
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def polyline_stroke(draw, pts, w_head, w_tail, n_per_seg=25):
    total = 0.0
    lens = []
    for i in range(len(pts) - 1):
        d = ((pts[i+1][0]-pts[i][0])**2 + (pts[i+1][1]-pts[i][1])**2) ** 0.5
        lens.append(d)
        total += d
    covered = 0.0
    for i in range(len(pts) - 1):
        L = lens[i]
        if L <= 0:
            continue
        prev = None
        for s in range(n_per_seg + 1):
            u_local = s / n_per_seg
            u_global = (covered + u_local * L) / max(1e-6, total)
            x = pts[i][0] + (pts[i+1][0]-pts[i][0]) * u_local
            y = pts[i][1] + (pts[i+1][1]-pts[i][1]) * u_local
            cur = (x, y)
            w = w_head + (w_tail - w_head) * u_global
            wi = max(1, int(round(w)))
            if prev is not None:
                draw.line([prev, cur], fill=(0, 0, 0), width=wi)
                r = w / 2.0
                draw.ellipse([cur[0]-r, cur[1]-r, cur[0]+r, cur[1]+r], fill=(0, 0, 0))
            prev = cur
        covered += L


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亻 (left radical) — tall column on left third ----------
    # Stroke 1: 撇 (pie) — sweeps from upper-left area down to lower-left.
    bezier_stroke(d,
                  to_px(-70, 110),
                  to_px(-92, 20),
                  to_px(-115, -110),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 (shu) — vertical column, head touches pie's mid-shaft.
    line_stroke(d,
                to_px(-72, 40),
                to_px(-72, -115),
                w_head=5, w_tail=5, n=40)

    # ---------- 夸 = 大 (top) + 亏 (bottom) — right two-thirds ----------
    # ---- 大 (top of 夸): 撇 + 一 + 捺 (small, at top) ----
    # 撇 of 大 — from upper right area sweeping down-left, one continuous curl.
    bezier_stroke(d,
                  to_px(50, 125),
                  to_px(20, 80),
                  to_px(-15, 50),
                  w_head=5, w_tail=2, n=55)

    # Heng of 大 (short, crosses just below pie apex).
    line_stroke(d,
                to_px(-10, 95),
                to_px(90, 95),
                w_head=4, w_tail=5, n=30)

    # 捺 of 大 — from just right of pie/heng crossing, sweeping down-right.
    bezier_stroke(d,
                  to_px(45, 100),
                  to_px(72, 78),
                  to_px(100, 50),
                  w_head=3, w_tail=6, n=50)

    # ---- 亏 (bottom of 夸): 一 (wide heng) + 横折折弯钩 ----
    # Wide 一 across the upper part of bottom half.
    line_stroke(d,
                to_px(-30, 30),
                to_px(110, 30),
                w_head=4, w_tail=5, n=40)

    # 横折折弯钩 of 亏: horizontal that turns down, sweeps left-down,
    # then curls into a rightward hook.
    # Segment: heng at top, fold down on right, sweep down-left as curve.
    polyline_stroke(d,
                    [to_px(-15, -5),
                     to_px(85, -5),
                     to_px(85, -35)],
                    w_head=5, w_tail=5)

    # Continuous sweeping arc down-left then curling to a bottom hook.
    bezier_stroke(d,
                  to_px(85, -35),
                  to_px(20, -70),
                  to_px(-30, -115),
                  w_head=5, w_tail=4, n=60)

    # Terminal hook flick (short upward tick at the end).
    line_stroke(d,
                to_px(-30, -115),
                to_px(-5, -100),
                w_head=5, w_tail=3, n=15)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_侉.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
