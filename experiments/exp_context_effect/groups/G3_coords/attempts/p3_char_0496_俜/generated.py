# p3_char_0496_俜 — G3 attempt.
# 俜 (pīng) = 亻 (left person radical, 2 strokes) + 甹 (right, ~7 strokes).
# 甹 structure (from GT): 由-like small box on top (vertical crossing through
#   top of box, top heng, right side with 横折, middle heng inside box),
#   then a long heng under the box, then a 横折弯钩-like curve with a
#   downward-left tail ending in a hook at bottom.
# Following the fu_pay / qian_thousand inline PIL recipe (thin ~4-6 px lines).
# Chose to inline 亻 rather than call bank ren_pang: same L-R layout family
# as fu_pay which also inlines — not a compositional mismatch, just staying
# consistent with the sibling recipe.

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
    # Stroke 1: 撇 — deeper sweep, head near top, tail far down-left.
    bezier_stroke(d,
                  to_px(-50, 115),
                  to_px(-85, 15),
                  to_px(-120, -120),
                  w_head=6, w_tail=2, n=60)
    # Stroke 2: 竖 — vertical from pie mid-shaft down.
    line_stroke(d,
                to_px(-55, 45),
                to_px(-55, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 甹 (right side) ----------
    # Box roughly x=[5, 90], y=[35, 110]. Central vertical extends up above.
    # Stroke 3: 竖 — central vertical extending above box down to inner-heng level.
    line_stroke(d,
                to_px(48, 125),
                to_px(48, 55),
                w_head=5, w_tail=5, n=30)
    # Stroke 4: 竖 — left vertical of box
    line_stroke(d,
                to_px(5, 110),
                to_px(5, 35),
                w_head=5, w_tail=5, n=30)
    # Stroke 5: 横折 — top horizontal + right vertical of box (one stroke)
    line_stroke(d,
                to_px(5, 110),
                to_px(90, 110),
                w_head=5, w_tail=5, n=30)
    line_stroke(d,
                to_px(90, 110),
                to_px(90, 35),
                w_head=5, w_tail=5, n=30)
    # Stroke 6: inner 横 — middle horizontal inside box
    line_stroke(d,
                to_px(5, 70),
                to_px(90, 70),
                w_head=5, w_tail=5, n=25)
    # Stroke 7: bottom 横 of box
    line_stroke(d,
                to_px(5, 35),
                to_px(90, 35),
                w_head=5, w_tail=5, n=25)
    # Stroke 8: long 横 spanning wider under the box.
    line_stroke(d,
                to_px(-18, 5),
                to_px(115, 5),
                w_head=5, w_tail=5, n=35)

    # ---------- Bottom of 甹 (乙-like 横折弯钩) ----------
    # Stroke 9: top heng of the hook-shape
    line_stroke(d,
                to_px(-5, -30),
                to_px(100, -30),
                w_head=5, w_tail=5, n=30)
    # Stroke 10: curve down-then-sweeping-left forming the belly of the hook
    bezier_stroke(d,
                  to_px(100, -30),
                  to_px(105, -85),
                  to_px(30, -115),
                  w_head=5, w_tail=5, n=50)
    # Stroke 11: sweep continuing left to tail
    bezier_stroke(d,
                  to_px(30, -115),
                  to_px(0, -118),
                  to_px(-35, -115),
                  w_head=5, w_tail=5, n=35)
    # Stroke 12: small upward hook flick at the tail
    bezier_stroke(d,
                  to_px(-35, -115),
                  to_px(-42, -108),
                  to_px(-48, -95),
                  w_head=5, w_tail=1, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_俜.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
