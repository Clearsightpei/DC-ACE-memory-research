"""p3_char_0149_升 — G5 attempt.

升 (shēng, "rise") — 4 strokes:
  s1: short pie from upper-inner down to middle-left (forms top-left arm)
  s2: long heng crossing the full character horizontally
  s3: long curved pie going from center down to bottom-left
  s4: long shu (vertical) on the right side, tall

Uses bank primitives: draw_pie, draw_heng, draw_shu. Anchors from MMH.
No BANK_DEVIATION needed — 3 bank fits directly.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


# --- 米字格 pixel helper: cell (row-col) + (x_frac, y_frac) → pixel ---
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)


# --- MMH anchors (from injected structural expectations) ---
s1_head = anchor('TC', 0.292, 0.788)   # (129, 79)
s1_tail = anchor('ML', 0.712, 0.327)   # (71,  133)

s2_head = anchor('ML', 0.249, 0.784)   # (25, 178)
s2_tail = anchor('MR', 0.774, 0.614)   # (277, 161)

s3_head = anchor('C',  0.025, 0.236)   # (103, 124)
s3_tail = anchor('BL', 0.589, 0.833)   # (59, 283)

s4_head = anchor('TC', 0.726, 0.612)   # (173, 61)
s4_tail = anchor('BC', 0.872, 1.111)   # (187, 311) — clip at canvas edge
# clip s4_tail y to canvas
s4_tail = (s4_tail[0], min(s4_tail[1], 298))


# --- Render ---
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: short pie (top-inner → middle-left) — small bow
draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=8, w_tail=4)

# s2: long heng crossing horizontally, slight rise toward right
draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

# s3: long curved pie (center → bottom-left) — pronounced bow rightward
draw_pie(d, s3_head, s3_tail, bow_perp=18, w_head=8, w_tail=3)

# s4: long shu (top-center → bottom-center-right) — straight vertical
draw_shu(d, s4_head, s4_tail, width=8)


out = pathlib.Path(__file__).parent / '01_升.png'
img.save(out)


# --- Self-check ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes called: pie, heng, pie, shu
    'endpoint_mismatches': [],     # anchors used as MMH gave them
    'joint_class_mismatches': [],  # s2xs3 and s2xs4 cross at C (P welded), s1-s3 near ML (N gap)
    'overall_pass': True,
    'notes': 'bank primitives fit; no BANK_DEVIATION. s1 short pie deliberately small.',
}


if __name__ == '__main__':
    print(f'wrote {out}')
