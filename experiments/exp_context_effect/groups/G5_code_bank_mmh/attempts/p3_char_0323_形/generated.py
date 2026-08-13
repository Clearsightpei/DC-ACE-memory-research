"""p3_char_0323_形 (xíng, 'form/shape') — G5 attempt.

Decomposition: 开 (left, 4 strokes) + 彡 (right, 3 pies).

Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer
(no whole-radical bank primitive exists for 开 or 彡).

Strokes (from MMH):
  s1: short heng near top-left of 开
  s2: long heng crossing both verticals of 开
  s3: 丿 (long leftward pie — left "vertical" of 开)
  s4: 丨 (right vertical of 开, slight rightward drift)
  s5-s7: three pies of 彡 (top-right → bottom, increasing length)
"""

import sys
import os

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitives called (2 heng + 1 shu + 4 pie)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors direct from MMH block; joint s2×s4 is a natural P-cross (long heng through vertical). 开-left uses pie (curved 丿). 彡 uses 3 pies of increasing length; s7 tail extends slightly below canvas per MMH y_frac=1.067.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 开 (left half, 4 strokes) ----
    # s1: short heng, top-left dab
    draw_heng(d, (56.2, 91.4), (162.0, 84.1), width_head=8, width_tail=9)

    # s2: long main heng, crosses through both verticals
    draw_heng(d, (21.4, 164.6), (166.1, 150.0), width_head=9, width_tail=10)

    # s3: 丿 — long leftward pie (the "left vertical" of 开 is actually a pie)
    # bow_perp positive → curves right of travel; head is upper, tail lower-left
    draw_pie(d, (70.3, 102.2), (29.6, 262.5),
             bow_perp=14, w_head=9, w_tail=4)

    # s4: 丨 — right vertical of 开 (slight rightward drift)
    draw_shu(d, (124.5, 93.2), (134.5, 266.6), width=8)

    # ---- 彡 (right half, 3 pies) ----
    # s5: short-top pie
    draw_pie(d, (226.2, 65.0), (178.1, 138.0),
             bow_perp=10, w_head=8, w_tail=3)

    # s6: medium pie (middle)
    draw_pie(d, (224.4, 137.7), (169.3, 206.2),
             bow_perp=11, w_head=8, w_tail=3)

    # s7: long pie (bottom, extends below canvas)
    draw_pie(d, (237.6, 194.5), (128.3, 306.7),
             bow_perp=16, w_head=9, w_tail=3)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_形.png')
    render(out)
    print(f'wrote {out}')
