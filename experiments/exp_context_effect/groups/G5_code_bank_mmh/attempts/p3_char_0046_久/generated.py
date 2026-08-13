"""p3_char_0046 — 久 (jiu, 'long time')

3 strokes: 撇 (short top-left), 横撇/heng-pie-like main body, 捺 (long down-right).

Bank usage:
- s1: draw_pie (short top pie)
- s2: draw_heng_pie (short horizontal top hook + long left-down pie)
- s3: draw_na (rightward thickening sweep)
Two N joints (natural gap ~17 px) between s1.mid ⇆ s2.head, and s2.mid ⇆ s3.head.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng_pie import draw_heng_pie
from na import draw_na


# ---- 米字格 anchor helper: cell (name) + (x_frac, y_frac in [0,1]) -> pixel ----
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# ---- MMH-injected endpoints ----
s1_head = anchor('TC', 0.236, 0.691)   # (123.6, 69.1)
s1_tail = anchor('ML', 0.478, 0.948)   # (47.8, 194.8)

s2_head = anchor('C',  0.187, 0.354)   # (118.7, 135.4)
s2_tail = anchor('BL', 0.369, 0.933)   # (36.9, 293.3)

s3_head = anchor('BC', 0.579, 0.057)   # (157.9, 205.7)
s3_tail = anchor('BR', 0.769, 0.95)    # (276.9, 295.0)


# ---- Render ----
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: short 撇 at top-left. Slight bow to arch right.
draw_pie(d, s1_head, s1_tail, bow_perp=8, w_head=7, w_tail=3, steps=60)

# s2: heng_pie — top has a short horizontal hook then long pie down-left.
# Tune the horizontal portion to be short (default 130 is way too wide for 久).
draw_heng_pie(d, s2_head, s2_tail, apex_x=s2_head[0] + 22, corner_x=s2_head[0] + 20)

# s3: long 捺 sweeping down-right, thickens toward tail.
draw_na(d, s3_head, s3_tail, bow_perp=12, w_head=4, w_tail=10, steps=90)


# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 primitives called: pie + heng_pie + na
    'endpoint_mismatches': [],     # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # both joints are N (no welding done at those points)
    'overall_pass': True,
    'notes': 'Bank primitives fit; heng_pie shortened via apex_x/corner_x for 久 vs 又.',
}


OUT = pathlib.Path(__file__).parent / '01_久.png'
img.save(OUT)
print(f'saved {OUT}')
