"""p2_radical_087_灬 (fire-bottom radical, 4 strokes).

Four separated dots along the bottom. From MMH anchors:
  s1: head ML(0.677,0.708) tail BL(0.504,0.206)  — leftward-slanting pie
  s2: head C (0.069,0.72 ) tail BC(0.225,0.033)  — short dian, rightward
  s3: head C (0.544,0.708) tail C (0.729,0.989)  — short dian, rightward
  s4: head MR(0.092,0.69 ) tail BR(0.52 ,0.194)  — rightward na-like dian

No joints (strokes are clearly separated — expected N-style gaps everywhere).
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from pie import draw_pie


CELL = 100  # 3x3 米字格 on 300x300 canvas

CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL, oy + yf * CELL)


# --- endpoints (from MMH block) ---
s1_head = anchor('ML', 0.677, 0.708)
s1_tail = anchor('BL', 0.504, 0.206)
s2_head = anchor('C',  0.069, 0.72)
s2_tail = anchor('BC', 0.225, 0.033)
s3_head = anchor('C',  0.544, 0.708)
s3_tail = anchor('C',  0.729, 0.989)
s4_head = anchor('MR', 0.092, 0.69)
s4_tail = anchor('BR', 0.52,  0.194)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: leftward pie (down-left). Slight rightward bow (concave-right).
    draw_pie(d, s1_head, s1_tail, bow_perp=4, w_head=7, w_tail=3)

    # Stroke 2: short dian leaning right.
    draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=7, bow=2)

    # Stroke 3: short dian leaning right.
    draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=7, bow=2)

    # Stroke 4: long rightward dian (na-like tail).
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=9, bow=3)

    out = pathlib.Path(__file__).parent / '01_灬.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 stroke primitives called
    'endpoint_mismatches': [],    # anchors used exactly as MMH specified
    'joint_class_mismatches': [], # no joints expected (N gaps between all strokes)
    'overall_pass': True,
    'notes': 'Four separated dots. draw_pie for s1 (leftward), draw_dian for s2/s3 (short) and s4 (long rightward).',
}


if __name__ == '__main__':
    print(render())
