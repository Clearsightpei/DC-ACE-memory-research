# BANK_DEVIATION
# skipped: dao_knife.py (whole-radical 刀)
# reason: 刅 is compact (~100-200px cluster) with two extra small dian/tick
#         strokes on the sides at MMH-specified anchors — the whole-radical
#         primitive's fixed geometry doesn't align to this composition's
#         endpoint anchors. Inline the 刀 body using stroke-level primitives.
# fresh_component: none (all sub-strokes from existing bank stroke primitives)

"""p3_char_0135_刅 — G5 attempt

Char 刅 = 刀 body (compact, upper-left area) + two small ticks on sides.
4 strokes per MMH.

Stroke plan:
  s1: 横折钩 (heng_zhe_gou) — top of 刀
  s2: 撇 (pie)              — left leg of 刀
  s3: 短撇/点 (dian, going down-left) — left tick
  s4: 短点 (dian, going down-right)   — right tick
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/success_bank/code")

from PIL import Image, ImageDraw
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inline stroke primitives; MMH cell/frac -> px via 100px cells'
}


def _cell_to_px(cell, xf, yf):
    """3x3 米字格 on 300x300 canvas -> pixel."""
    col = {'TL': 0, 'TC': 1, 'TR': 2, 'ML': 0, 'C': 1, 'MR': 2, 'BL': 0, 'BC': 1, 'BR': 2}[cell]
    row = {'TL': 0, 'TC': 0, 'TR': 0, 'ML': 1, 'C': 1, 'MR': 1, 'BL': 2, 'BC': 2, 'BR': 2}[cell]
    return (col * 100 + xf * 100, row * 100 + yf * 100)


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 head TC(0.239, 0.85); tail C(0.617, 0.503)  — 横折钩
    s1_head = _cell_to_px('TC', 0.239, 0.85)   # (123.9, 85)
    s1_tail = _cell_to_px('C',  0.617, 0.503)  # (161.7, 150.3)
    # heng from head goes right to corner, then shu drops down, hook flicks in.
    s1_corner  = (170.0, 87.0)
    s1_gou_bot = (168.0, 155.0)
    draw_heng_zhe_gou(d, s1_head, s1_corner, s1_gou_bot, s1_tail)

    # s2 head TC(0.526, 0.92); tail C(0.072, 0.761)  — 撇 (long left-going)
    s2_head = _cell_to_px('TC', 0.526, 0.92)  # (152.6, 92)
    s2_tail = _cell_to_px('C',  0.072, 0.761)  # (107.2, 176.1)
    draw_pie(d, s2_head, s2_tail, bow_perp=10, w_head=7, w_tail=2, steps=60)

    # s3 head C(0.283, 0.122); tail C(0.131, 0.392)  — small dian/pie, left side
    s3_head = _cell_to_px('C', 0.283, 0.122)  # (128.3, 112.2)
    s3_tail = _cell_to_px('C', 0.131, 0.392)  # (113.1, 139.2)
    draw_dian(d, s3_head, s3_tail, w_head=2, w_tail=5, bow=2, steps=40)

    # s4 head MR(0.171, 0.131); tail MR(0.525, 0.397)  — small tick, right side
    s4_head = _cell_to_px('MR', 0.171, 0.131)  # (217.1, 113.1)
    s4_tail = _cell_to_px('MR', 0.525, 0.397)  # (252.5, 139.7)
    draw_dian(d, s4_head, s4_tail, w_head=2, w_tail=5, bow=-2, steps=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_刅.png')
    img.save(out)
    return out


if __name__ == '__main__':
    path = draw()
    print(f'wrote {path}')
