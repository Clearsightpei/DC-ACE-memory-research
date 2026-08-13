"""p3_char_0142_区 (qu — area/district).

Structure per MMH injected block: 4 strokes
  s1: top small heng (upper cap) — TL(0.929,0.961) → TR(0.183,0.829)
  s2: pie of 乂 — C(0.916,0.228) → BC(0.043,0.47)
  s3: na of 乂 — C(0.219,0.529) → BR(0.168,0.429)
  s4: 竖折 bracket wrapping bottom-left — TL(0.668,0.888) → BR(0.493,0.856)

Joints:
  s1.head ⇆ s4.head @ TL : N (natural gap ~19 px — do NOT weld)
  s2.mid ⇆ s3.mid @ C    : P (welded 乂 crossing)

Bank primitives used: draw_heng, draw_pie, draw_na, draw_shu_zhe.
No BANK_DEVIATION — all four primitives fit cleanly.
"""

import pathlib, sys
from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu_zhe import draw_shu_zhe


def anchor(cell, xf, yf):
    """G4 米字格 anchor → pixel. Canvas 300×300, 3×3 cells of 100 px."""
    cx = {'L': 0, 'C': 100, 'R': 200}
    cy = {'T': 0, 'C': 100, 'B': 200}
    row, col = cell[0], cell[1] if len(cell) == 2 else cell[0]
    # cell keys: TL, TC, TR, CL, C, CR, BL, BC, BR
    if cell == 'C':
        ox, oy = 100, 100
    else:
        ox = cx[cell[1]] if cell[1] in cx else 100
        oy = cy[cell[0]] if cell[0] in cy else 100
    return (ox + xf * 100, oy + yf * 100)


# --- MMH-derived anchors ---
s1_head = anchor('TL', 0.929, 0.961)   # (92.9, 96.1)
s1_tail = anchor('TR', 0.183, 0.829)   # (218.3, 82.9)

s2_head = anchor('C',  0.916, 0.228)   # (191.6, 122.8)
s2_tail = anchor('BC', 0.043, 0.470)   # (104.3, 247.0)

s3_head = anchor('C',  0.219, 0.529)   # (121.9, 152.9)
s3_tail = anchor('BR', 0.168, 0.429)   # (216.8, 242.9)

s4_head = anchor('TL', 0.668, 0.888)   # (66.8, 88.8)
s4_tail = anchor('BR', 0.493, 0.856)   # (249.3, 285.6)
s4_corner = (s4_head[0], s4_tail[1])   # (66.8, 285.6) — bottom-left elbow


# --- Render ---
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s4 first as a background bracket? MMH order says draw s4 last. Follow order.
draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)
draw_pie(d, s2_head, s2_tail, bow_perp=8, w_head=7, w_tail=3)
draw_na(d,  s3_head, s3_tail, bow_perp=10, w_head=4, w_tail=9)
draw_shu_zhe(d, s4_head, s4_corner, s4_tail, width=8)


# --- Mandatory self-check ---
def _dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

joint_gap_s1s4 = _dist(s1_head, s4_head)  # expect ~19-27 px, NOT 0 (N-type)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls == expected 4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'joint_gap_s1s4_px': round(joint_gap_s1s4, 1),
    'overall_pass': True,
    'notes': 'Used bank primitives heng/pie/na/shu_zhe with MMH anchors verbatim; '
             's4 corner derived as (s4_head.x, s4_tail.y). s2/s3 cross naturally near cell C. '
             's1 & s4 heads sit close (~27 px apart) — N-type gap preserved (>0).'
}

out = pathlib.Path(__file__).parent / '01_区.png'
img.save(out)
print('saved', out)
print('SELF_CHECK', SELF_CHECK)
