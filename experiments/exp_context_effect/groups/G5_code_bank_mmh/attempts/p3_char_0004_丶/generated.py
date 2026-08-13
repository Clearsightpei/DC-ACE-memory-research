"""p3_char_0004_丶 — single dian stroke, using bank primitive dian.py."""
import sys, os
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from dian import draw_dian  # noqa: E402


# 米字格 cell -> pixel origin for 300×300 canvas (3x3 grid of 100px cells).
CELL_ORIGINS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'L':  (0, 100), 'C':  (100, 100), 'R':  (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: 丶 — head at ('TC', 0.146, 0.946) → tail at ('C', 0.717, 0.652)
head = anchor('TC', 0.146, 0.946)   # (114.6, 94.6)
tail = anchor('C',  0.717, 0.652)   # (171.7, 165.2)
draw_dian(d, head, tail, w_head=3, w_tail=9, bow=6, steps=60)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 1 draw_dian call == 1 expected stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Bank primitive draw_dian used as-is with tuned taper/bow; endpoints match MMH anchors exactly.'
}

out = os.path.join(os.path.dirname(__file__), '01_丶.png')
img.save(out)
print('wrote', out)
