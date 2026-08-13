"""p2_radical_102_耂 — G5 attempt.

耂 (4 strokes, 老字头):
  s1: short heng at top-right of the middle band
  s2: shu descending from above s1, piercing s1 (P-joint at C)
  s3: long heng crossing the full width, slightly rising left→right
  s4: long pie sweeping from upper-right down to lower-left,
      piercing s3 (P-joint at C)

MMH anchors (cell, x_frac, y_frac) → pixel (cell_origin + frac*100).
Cell origins on the 3x3 米字格 (300x300):
  TL(0,0)   TC(100,0)   TR(200,0)
  ML(0,100) MC/C(100,100) MR(200,100)
  BL(0,200) BC(100,200)   BR(200,200)

  s1 head ('ML', 0.984, 0.172) = ( 98.4, 117.2)
  s1 tail ('C' , 0.887, 0.093) = (188.7, 109.3)
  s2 head ('TC', 0.333, 0.507) = (133.3,  50.7)
  s2 tail ('C' , 0.392, 0.573) = (139.2, 157.3)
  s3 head ('ML', 0.217, 0.787) = ( 21.7, 178.7)
  s3 tail ('MR', 0.742, 0.547) = (274.2, 154.7)
  s4 head ('TR', 0.121, 0.712) = (212.1,  71.2)
  s4 tail ('BL', 0.378, 0.733) = ( 37.8, 273.3)

Bank use: heng.py (s1 short & s3 long), shu.py (s2), pie.py (s4).
No BANK_DEVIATION — all four bank primitives fit naturally.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from pie import draw_pie     # noqa: E402


CELL_ORIGINS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'MC': (100, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def cell_to_px(cell, xf, yf):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — short top heng
    s1_head = cell_to_px('ML', 0.984, 0.172)
    s1_tail = cell_to_px('C',  0.887, 0.093)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2 — shu piercing s1 (P-joint at C)
    s2_head = cell_to_px('TC', 0.333, 0.507)
    s2_tail = cell_to_px('C',  0.392, 0.573)
    draw_shu(d, s2_head, s2_tail, width=7)

    # s3 — long middle heng
    s3_head = cell_to_px('ML', 0.217, 0.787)
    s3_tail = cell_to_px('MR', 0.742, 0.547)
    draw_heng(d, s3_head, s3_tail, width_head=9, width_tail=10)

    # s4 — long pie from upper-right down to lower-left (P with s3)
    s4_head = cell_to_px('TR', 0.121, 0.712)
    s4_tail = cell_to_px('BL', 0.378, 0.733)
    # pie widths are RADII of filled ellipses per step — keep small for thin ink
    draw_pie(d, s4_head, s4_tail, bow_perp=20, w_head=5, w_tail=1, steps=120)

    out = Path(__file__).with_name("01_耂.png")
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 stroke calls: heng, shu, heng, pie
    'endpoint_mismatches': [],   # anchors used directly from MMH
    'joint_class_mismatches': [],# s1×s2 P (shu crosses heng at ~mid), s3×s4 P
    'overall_pass': True,
    'notes': 'All four strokes covered by bank primitives; no BANK_DEVIATION.',
}


if __name__ == '__main__':
    p = render()
    print(f"wrote {p}")
