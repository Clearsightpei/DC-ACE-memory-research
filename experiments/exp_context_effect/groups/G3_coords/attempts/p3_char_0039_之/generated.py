"""p3_char_0039_之 — 之 (3 strokes: 点, 横撇, 平捺)

Math coords: center (150,150), +y up. 300x300 canvas.
Decomposition from GT:
  S1 点: small heavy dot near top center-right, slight tilt.
  S2 横撇: short horizontal from upper-left, then a diagonal 撇
     sweeping down-left. Rendered as two tapered pieces sharing
     the corner pixel (weld).
  S3 平捺: the base wave — starts slim upper-left, dips down to a
     valley, then swells belly, tapers out horizontally to the right.
"""
import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "groups", "G3_coords", "success_bank", "code"))

from _shared_helpers import (
    variant_dian, variant_na, tapered_line, tapered_bezier, to_px,
)


def draw_zhi(draw, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # ---- S1: 点 (top dot) ----
    # Tilted right-dot near top-center. Thin head upper-left, heavy tail lower-right.
    variant_dian(
        draw,
        head=P(+2, +112),
        tail=P(+22, +92),
        w_head=2.5, w_tail=9.0, bow_perp=-2.0,
    )

    # ---- S2: 横撇 ----
    # Horizontal segment at upper-mid, then a 撇 sweeping down-left.
    # Corner (weld) is the shared pixel.
    heng_left = P(-80, +40)
    corner    = P(+40, +50)   # slight rise to the right for the 横
    pie_tail  = P(-30, -35)   # 撇 sweeps down-left, ends closer to 捺 start

    # 横 piece: thin start, thicker at corner (small taper).
    tapered_line(draw, heng_left, corner, w0=4.0, w1=8.0, n=32)

    # small "顿笔" thickening at the corner
    cx, cy = to_px(*corner)
    r = 5.0
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # 撇 piece: bezier from corner going down-left, tapered thick→thin.
    mid = ((corner[0] + pie_tail[0]) / 2 - 4,
           (corner[1] + pie_tail[1]) / 2 + 4)
    tapered_bezier(draw, corner, mid, pie_tail, w_head=8.0, w_tail=2.0, n=48)

    # ---- S3: 平捺 (bottom wave) ----
    # Starts at a small dip on the left, wave gently down then rises with
    # a broad tapered exit to the right. Near-horizontal.
    #
    # Small dip/hook on the left (start of 捺):
    dip_head = P(-105, -55)
    dip_tail = P(-70, -70)
    tapered_line(draw, dip_head, dip_tail, w0=2.0, w1=6.0, n=16)

    # Main 平捺 body: gentle sag, belly then tapered horizontal tail.
    na_head  = P(-70, -70)
    na_tail  = P(+120, -55)
    variant_na(
        draw,
        head=na_head,
        tail=na_tail,
        bow_perp=-10.0,   # gentle sag downward
        w_head=3.0,
        w_belly=13.0,
        w_tail=2.0,
        belly_u=0.75,
        n=72,
    )


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zhi(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(HERE, "01_之.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
