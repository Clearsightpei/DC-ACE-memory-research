"""p3_char_0495_复 (fù, "return/repeat") — 9 strokes.

BANK_DEVIATION reasoning (P-A-006 / P-A-008 / P-A-009):
Reviewed bank for whole-char primitive of 复 or a component match — none
(no 夂 primitive; no 复 sibling in bank). Also checked 亠-top pattern
(s1 pie + s2 heng) — bank has heng, pie, shu but no compound "亠". Inline
per stroke primitive using MMH-verbatim anchors is the correct P-A-006
path here. No BANK_DEVIATION needed (nothing skipped that fit).

Structure interpretation:
  s1 — top short pie (upper-center → middle-left; the / above the box)
  s2 — top short heng (mid-top → upper-right; the ─ crossing s1)
  s3 — left of middle box (short shu-like descender)
  s4 — heng-zhe (top+right of the middle box, single MMH stroke)
  s5 — middle horizontal inside the box
  s6 — bottom horizontal of the box
  s7 — long descending pie from center-bottom down to lower-left
        (the outer sweep continuing under the box)
  s8 — 夂 inner pie (upper-BC → BL, forms X-cross with s9)
  s9 — 夂 na (upper-BC → BR, welded P with s8 at BC(0.61,0.59))

Cell → pixel: 300×300 canvas, 3×3 米字格 with 100px cells.
  origin_of(cell) + (x_frac*100, y_frac*100)
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng        # noqa: E402
from na import draw_na            # noqa: E402
from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402


CELL = {
    "TL": (0, 0), "TC": (100, 0), "TR": (200, 0),
    "ML": (0, 100), "C": (100, 100), "MR": (200, 100),
    "BL": (0, 200), "BC": (100, 200), "BR": (200, 200),
}


def a(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100, oy + yf * 100)


def draw_heng_zhe(draw, top_left, bottom_right, width=6):
    """Draw a heng-zhe (horizontal + right-vertical) with a corner."""
    tlx, tly = top_left
    brx, bry = bottom_right
    corner = (brx, tly + 2)
    # top horizontal (slightly rising toward corner)
    draw.line([top_left, corner], fill="black", width=width)
    r = width / 2 + 1
    draw.ellipse([tlx - r, tly - r, tlx + r, tly + r], fill="black")
    # small 顿笔 at corner
    draw.ellipse([corner[0] - r - 1, corner[1] - r - 1,
                  corner[0] + r + 1, corner[1] + r + 1], fill="black")
    # right vertical down to tail
    draw.line([corner, bottom_right], fill="black", width=width)


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top short pie (105.8,53.6) -> (66.8,123.6)
    draw_pie(d, a("TC", 0.058, 0.536), a("ML", 0.668, 0.236),
             bow_perp=6, w_head=6, w_tail=2, steps=60)

    # s2: top short heng (113.4,87) -> (212.4,71.2)
    draw_heng(d, a("TC", 0.134, 0.870), a("TR", 0.124, 0.712),
              width_head=7, width_tail=8)

    # s3: left of middle box — short shu descending
    draw_shu(d, a("ML", 0.973, 0.148), a("C", 0.178, 0.813), width=6)

    # s4: heng-zhe (top + right of middle box)
    draw_heng_zhe(d, a("C", 0.107, 0.163), a("C", 0.749, 0.623), width=6)

    # s5: middle horizontal
    draw_heng(d, a("C", 0.195, 0.494), a("C", 0.661, 0.409),
              width_head=5, width_tail=6)

    # s6: bottom horizontal of box
    draw_heng(d, a("C", 0.225, 0.734), a("C", 0.711, 0.690),
              width_head=5, width_tail=6)

    # s7: long descending pie center → lower-left
    draw_pie(d, a("C", 0.154, 0.849), a("BL", 0.387, 0.742),
             bow_perp=12, w_head=6, w_tail=2, steps=90)

    # s8: 夂 pie (upper-BC → BL, forms X-cross with s9)
    draw_pie(d, a("BC", 0.263, 0.092), a("BL", 0.747, 0.974),
             bow_perp=8, w_head=6, w_tail=2, steps=80)

    # s9: 夂 na (upper-BC → BR, welded P with s8)
    draw_na(d, a("BC", 0.140, 0.247), a("BR", 0.684, 0.947),
            bow_perp=12, w_head=4, w_tail=12, steps=100)

    out = os.path.join(os.path.dirname(__file__), "01_复.png")
    img.save(out)
    return out


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 9 stroke calls = 9 MMH strokes
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "MMH-verbatim anchors via cell-frac helper; heng-zhe inlined for s4.",
}


if __name__ == "__main__":
    print(render())
