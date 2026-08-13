# BANK_DEVIATION
# skipped: bao_gai_tou.py
# reason: bao_gai_tou's ox/oy convention is inconsistent between its dian
#         (math coords, +y up) and its henggou (PIL coords, +y down); safe
#         only at defaults, so shifting the roof up for 家 desynchronizes
#         chimney and roof.  Inline fresh 宀 lets me place it cleanly at
#         the top ~30% of the canvas while the 豕 body owns the rest.
# fresh_component: mian_roof_for_家 + shi_pig_body_for_家
#
# 家 (jiā) — "home/family", 10 strokes.
# 300x300, white bg, black ink, PIL.

import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
CANVAS = 300
OUT = os.path.join(_HERE, "01_家.png")


def _tapered(draw, p_head, p_tail, w_head, w_tail, steps=30, bow_perp=0.0):
    """Draw a tapered line with optional perpendicular quadratic bow."""
    xh, yh = p_head
    xt, yt = p_tail
    dx, dy = xt - xh, yt - yh
    L = (dx * dx + dy * dy) ** 0.5
    if L < 1e-6:
        return
    px, py = -dy / L, dx / L
    bow = bow_perp * L
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bfac = 4 * u * (1 - u) * bow
        x = xh + dx * u + px * bfac
        y = yh + dy * u + py * bfac
        if prev is not None:
            w = max(1, int(round(w_head + (w_tail - w_head) * u)))
            draw.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)


def _dot(draw, cx, cy, w_head=3, w_tail=10):
    """Short 点 stroke ~ 18 px diagonal."""
    _tapered(draw, (cx - 6, cy - 8), (cx + 6, cy + 6), w_head, w_tail,
             steps=16, bow_perp=0.10)


def draw_roof(draw):
    """宀 roof at top ~30% of canvas."""
    # chimney dot (top)
    _dot(draw, 150, 42, 3, 10)
    # left short slanted 点/竖点
    _tapered(draw, (78, 60), (68, 92), 5, 9, steps=18)
    # 横钩: wide horizontal ending in small down-left hook
    _tapered(draw, (62, 82), (238, 88), 6, 8, steps=28)
    # hook: short downward-left tick at end of henggou
    _tapered(draw, (238, 88), (228, 108), 8, 3, steps=10, bow_perp=-0.15)


def draw_shi_body(draw):
    """豕 body sitting below the roof."""
    # S1: short top 撇 — just under the roof, tiny slanted head bar
    _tapered(draw, (155, 108), (140, 128), 5, 3, steps=14)

    # S2: 弯钩 — the main curved spine; starts high center, curves down
    #     and slightly right, ending with tiny right hook near bottom.
    #     Two sub-arcs so the curvature isn't a single flat bow.
    _tapered(draw, (152, 115), (175, 240), 4, 6, steps=36, bow_perp=0.09)
    # tail hook of 弯钩 at the bottom of spine
    _tapered(draw, (175, 240), (192, 246), 6, 4, steps=8)

    # S3: middle short 撇 — leftmost belly rib
    _tapered(draw, (128, 168), (108, 198), 4, 2, steps=16, bow_perp=0.05)

    # S4: middle short 撇 — center belly rib
    _tapered(draw, (152, 168), (132, 198), 4, 2, steps=16, bow_perp=0.05)

    # S5: middle short 撇 — right belly rib (attaches to spine)
    _tapered(draw, (172, 172), (152, 202), 4, 2, steps=16, bow_perp=0.05)

    # S6: long 撇 — left leg sweeping to lower-left corner
    _tapered(draw, (145, 155), (50, 268), 5, 2, steps=44, bow_perp=0.07)

    # S7: 捺 — big sweep to lower-right corner, wide foot at end
    _tapered(draw, (162, 168), (262, 262), 3, 11, steps=44, bow_perp=0.08)
    # small horizontal flat foot at end of 捺
    _tapered(draw, (252, 262), (278, 266), 11, 3, steps=8)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_roof(draw)
    draw_shi_body(draw)
    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
