# p3_char_0519_候 — G3 attempt.
# 候 = 亻 (left, 2 strokes) + right cluster (8 strokes: 𠂉 top + short shu
#     + long heng + 矢-arrow bottom).
# GT shows thin MMH-style ink (~4-5 px). Left third for 亻, right two-thirds
# for the tall right cluster.
# Using inline PIL rendering rather than bank ren_pang because tall 亻
# is needed to span full character height alongside the 8-stroke right column.

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

    # ---------- 亻 (left radical, tall) ----------
    # Stroke 1: 撇 — head upper, sweep down-left. Pulled inward.
    bezier_stroke(d,
                  to_px(-55, 110),
                  to_px(-72, 20),
                  to_px(-92, -85),
                  w_head=5, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft.
    line_stroke(d,
                to_px(-58, 45),
                to_px(-58, -105),
                w_head=5, w_tail=4, n=40)

    # ---------- Right cluster (8 strokes) ----------
    # Right column spans roughly x = -20 to +115.

    # Stroke 3: 短撇 at top-right (small pie sloping down-left)
    bezier_stroke(d,
                  to_px(30, 115),
                  to_px(22, 100),
                  to_px(10, 85),
                  w_head=4, w_tail=2, n=25)

    # Stroke 4: 短横 top (short horizontal starting near end of pie).
    line_stroke(d,
                to_px(15, 95),
                to_px(90, 95),
                w_head=4, w_tail=4, n=25)

    # Stroke 5: 短竖 short vertical dropping from left of the top heng.
    line_stroke(d,
                to_px(30, 95),
                to_px(30, 45),
                w_head=4, w_tail=4, n=25)

    # Stroke 6: 长横 long horizontal (mid-line of right cluster).
    line_stroke(d,
                to_px(-18, 45),
                to_px(110, 45),
                w_head=4, w_tail=4, n=40)

    # ---------- 矢-like bottom (4 strokes) ----------
    # Stroke 7: 短撇 inside 矢 top (from just below long heng, sloping down-left).
    bezier_stroke(d,
                  to_px(50, 30),
                  to_px(35, 15),
                  to_px(18, 0),
                  w_head=4, w_tail=2, n=25)

    # Stroke 8: 短横 (small horizontal beneath the pie, forming 大-top).
    line_stroke(d,
                to_px(5, -5),
                to_px(85, -5),
                w_head=4, w_tail=4, n=25)

    # Stroke 9: 撇 (long left leg of 矢). Tighter angle.
    bezier_stroke(d,
                  to_px(48, 15),
                  to_px(25, -45),
                  to_px(-5, -110),
                  w_head=5, w_tail=2, n=40)

    # Stroke 10: 捺 (right leg of 矢, tapering thick to thin tail).
    bezier_stroke(d,
                  to_px(48, 15),
                  to_px(72, -40),
                  to_px(108, -105),
                  w_head=4, w_tail=8, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_候.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
