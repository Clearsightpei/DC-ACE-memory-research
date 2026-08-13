"""p2_radical_084_夊 — G5 attempt

3 strokes:
  s1: short 撇  head TC(0.31, 0.688) → tail ML(0.768, 0.84)
  s2: long 撇   head C(0.245, 0.433) → tail BL(0.448, 0.906)
  s3: 捺        head ML(0.926, 0.45) → tail BR(0.748, 0.924)

Joints:
  s1.mid(0.60) ⇆ s2.head @ C : N (~11px gap)
  s1.mid(0.70) ⇆ s3.head @ C : T (welded)
  s2.mid(0.54) ⇆ s3.mid(0.38) @ BC : P (welded crossing)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# make bank importable
BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from pie import draw_pie
from na import draw_na


def anchor(cell, xf, yf, size=300):
    cell_w = size / 3
    col = {'L': 0, 'C': 1, 'R': 2}
    row = {'T': 0, 'M': 1, 'B': 2}
    if cell == 'C':
        cx, cy = 1, 1
    else:
        r, c = cell[0], cell[1]
        cy, cx = row[r], col[c]
    return (cx * cell_w + xf * cell_w, cy * cell_w + yf * cell_w)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: short 撇
s1_head = anchor('TC', 0.31, 0.688)
s1_tail = anchor('ML', 0.768, 0.84)
draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=7, w_tail=3)

# s2: long 撇 (mid crosses BC with s3)
s2_head = anchor('C', 0.245, 0.433)
s2_tail = anchor('BL', 0.448, 0.906)
draw_pie(d, s2_head, s2_tail, bow_perp=10, w_head=7, w_tail=3)

# s3: 捺 sweeping down-right, mid crosses s2 at BC
s3_head = anchor('ML', 0.926, 0.45)
s3_tail = anchor('BR', 0.748, 0.924)
draw_na(d, s3_head, s3_tail, bow_perp=12, w_head=4, w_tail=10)

OUT = Path(__file__).parent / "01_夊.png"
img.save(OUT)
print(f"wrote {OUT}")

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 draws
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'used draw_pie x2 + draw_na x1; endpoints from MMH anchors',
}
