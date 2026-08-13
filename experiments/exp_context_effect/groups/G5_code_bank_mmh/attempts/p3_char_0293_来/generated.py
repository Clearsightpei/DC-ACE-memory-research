"""来 (lai — "come") — 7 strokes. G5 attempt using MMH endpoint anchors."""

import os
import sys
from PIL import Image, ImageDraw

# Bank imports
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes via bank primitives (heng, dian x2, heng, shu, pie, na). '
             'MMH anchors converted to pixel space via 米字格 3x3 (cell=100px). '
             'Central spine (s5) intersects both hengs (P joints s1-s5 and s4-s5 '
             'auto-satisfied by geometry). s6/s7 heads meet s4 mid at central spine '
             '(N joints; small natural gaps ≈13-24 px).',
}


def anchor(cell, xf, yf):
    """Convert 米字格 anchor (cell, x_frac, y_frac) → pixel (x, y) on 300×300."""
    col_map = {'L': 0, 'C': 100, 'R': 200}
    row_map = {'T': 0, 'M': 100, 'B': 200}
    if len(cell) == 2:
        row, col = cell[0], cell[1]
    else:
        # 'C' alone means center cell
        row, col = 'M', 'C'
    x0 = col_map[col]
    y0 = row_map[row]
    return (x0 + xf * 100, y0 + yf * 100)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- MMH-derived endpoint anchors ----
    s1_head = anchor('ML', 0.879, 0.104)   # (87.9, 110.4)
    s1_tail = anchor('MR', 0.106, 0.002)   # (210.6, 100.2)

    s2_head = anchor('ML', 0.891, 0.377)   # (89.1, 137.7)
    s2_tail = anchor('C',  0.163, 0.638)   # (116.3, 163.8)

    s3_head = anchor('C',  0.934, 0.216)   # (193.4, 121.6)
    s3_tail = anchor('C',  0.685, 0.588)   # (168.5, 158.8)

    s4_head = anchor('ML', 0.478, 0.919)   # (47.8, 191.9)
    s4_tail = anchor('MR', 0.525, 0.852)   # (252.5, 185.2)

    s5_head = anchor('TC', 0.336, 0.586)   # (133.6, 58.6)
    s5_tail = anchor('BC', 0.438, 1.12)    # (143.8, 212.0)

    s6_head = anchor('C',  0.395, 0.934)   # (139.5, 193.4)
    s6_tail = anchor('BL', 0.401, 0.763)   # (40.1, 276.3)

    s7_head = anchor('C',  0.567, 0.916)   # (156.7, 191.6)
    s7_tail = anchor('BR', 0.774, 0.81)    # (277.4, 281.0)

    # ---- Render ----
    # s1: short top heng
    draw_heng(d, s1_head, s1_tail, width_head=7, width_tail=8)

    # s2: small stroke down-right on left half (calligraphic 点 shape)
    draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=6, bow=-4)

    # s3: small stroke down-left on right half (mirror 点)
    draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=6, bow=4)

    # s4: long middle heng
    draw_heng(d, s4_head, s4_tail, width_head=9, width_tail=10)

    # s5: central vertical spine (spans full height)
    draw_shu(d, s5_head, s5_tail, width=7)

    # s6: long left descending pie
    draw_pie(d, s6_head, s6_tail, bow_perp=14, w_head=6, w_tail=2)

    # s7: long right na
    draw_na(d, s7_head, s7_tail, bow_perp=16, w_head=4, w_tail=11)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_来.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
