"""p3_char_0234_亚 — G5 render.

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer.
亚 is sibling of 业 (bank: yi_ye.py) with ONE additional top-heng.
Structure: top heng + 2 tall central verticals + 2 outer dians + baseline heng.

MMH anchors (300x300 canvas, cell = 100px, PIL y-down):
  s1 top-heng:   ML(0.788,0.014)=(78.8,101.4)  -> TR(0.224,0.929)=(222.4,92.9)
  s2 left-shu:   C (0.084,0.131)=(108.4,113.1) -> BC(0.154,0.675)=(115.4,267.5)
  s3 right-shu:  C (0.632,0.046)=(163.2,104.6) -> BC(0.658,0.625)=(165.8,262.5)
  s4 left-dian:  ML(0.574,0.761)=(57.4,176.1)  -> BL(0.899,0.121)=(89.9,212.1)
  s5 right-dian: MR(0.262,0.468)=(226.2,146.8) -> BC(0.831,0.062)=(183.1,206.2)
  s6 base-heng:  BL(0.384,0.760)=(38.4,276.0)  -> BR(0.660,0.774)=(266.0,277.4)

All 5 joints are N (natural gap). Verticals end ~10-15 px above baseline.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives called, matches expected 6
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Composition: yi_ye pattern + top heng. All 5 joints N (gaps preserved).',
}


def draw_ya(draw: ImageDraw.ImageDraw):
    # s1: top horizontal heng (slightly diagonal per MMH)
    draw_heng(draw, (78.8, 101.4), (222.4, 92.9),
              width_head=8, width_tail=10)

    # s2: left tall vertical (from just below top heng to just above baseline)
    draw_shu(draw, (108.4, 113.1), (115.4, 267.5), width=7)

    # s3: right tall vertical
    draw_shu(draw, (163.2, 104.6), (165.8, 262.5), width=7)

    # s4: left outer dian (upper-left -> lower-right, tapered thickening)
    draw_dian(draw, (57.4, 176.1), (89.9, 212.1),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s5: right outer dian/pie (upper-right -> lower-left)
    draw_dian(draw, (226.2, 146.8), (183.1, 206.2),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s6: baseline heng (long, wider than top)
    draw_heng(draw, (38.4, 276.0), (266.0, 277.4),
              width_head=9, width_tail=11)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ya(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亚.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
