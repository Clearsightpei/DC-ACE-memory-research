# p3_char_0314_伶 — G3 attempt.
# 伶 = 亻 (left person radical, 2 strokes: pie + shu)
#    + 令 (right, 5 strokes: pie + na roof + short dot/heng + heng-pie hook + dian).
# 7 strokes total. GT shows thin MMH-style ink (~4-6 px).
# Structural playbook: 亻+X L-R composition (drawer_memory.md 亻+right playbook).

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=40):
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
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亻 (left radical) ----------
    # Compressed to left third; MMH thin ink.
    # Stroke 1: 撇 — pie sweep from upper-center down-left to lower-left.
    bezier_stroke(d,
                  to_px(-70, 95),
                  to_px(-90, 10),
                  to_px(-110, -95),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft, tail low.
    line_stroke(d,
                to_px(-72, 30),
                to_px(-72, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 令 (right side, 5 strokes) ----------
    # Roof: 人 (pie + na). WIDE apex spanning right two-thirds of canvas.
    # Stroke 3: 撇 (roof pie) — from apex high, sweeps down-left long.
    bezier_stroke(d,
                  to_px(40, 120),
                  to_px(0, 60),
                  to_px(-40, -5),
                  w_head=5, w_tail=2, n=55)

    # Stroke 4: 捺 (roof na) — from same apex, sweeps down-right long with belly.
    bezier_stroke(d,
                  to_px(45, 115),
                  to_px(90, 50),
                  to_px(125, -15),
                  w_head=4, w_tail=3, n=55)

    # Stroke 5: 丶 (dot below roof, small — the middle mark).
    bezier_stroke(d,
                  to_px(30, 30),
                  to_px(40, 20),
                  to_px(52, 10),
                  w_head=3, w_tail=6, n=25)

    # Stroke 6: 龴 (heng-pie/heng-zhe with pie descent) — sits under middle dot.
    # Short heng segment then curves down-left as pie.
    line_stroke(d,
                to_px(15, -25),
                to_px(75, -25),
                w_head=5, w_tail=5, n=30)
    # Pie descent from right end of heng down-left, long tail:
    bezier_stroke(d,
                  to_px(75, -25),
                  to_px(55, -60),
                  to_px(20, -115),
                  w_head=6, w_tail=2, n=45)

    # Stroke 7: 丶 (final dian) — dot in the pocket right of the pie.
    bezier_stroke(d,
                  to_px(55, -80),
                  to_px(68, -90),
                  to_px(82, -100),
                  w_head=3, w_tail=7, n=25)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伶.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
