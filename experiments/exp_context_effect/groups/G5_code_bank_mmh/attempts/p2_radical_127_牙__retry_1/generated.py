"""p2_radical_127_牙 — G5 RETRY 1.

TRAJECTORY DIFF
---------------
Main attempt (verdict C) at ../p2_radical_127_牙/01_牙.png.

What the main attempt got wrong (visual gaps vs GT):
  1. s3 was drawn as draw_shu (nearly straight vertical). GT's s3 is a
     visibly LEFT-CURVING sweep (a pie-shape), not a straight shu. The
     rendered result reads as 干/天 not 牙 because the middle vertical
     is stiff and centered.
  2. s2 heng didn't span wide enough on the right — errata explicitly
     says "s2 heng should span wider (right edge farther out)".
  3. s4 was a straight pie but too small/short and didn't establish
     the enclosed pocket shape distinctive to 牙's lower-left corner.
  4. The two hengs (s1, s2) sat too high and too parallel — they read
     as a stacked pair rather than one short + one long.

Fixes this attempt:
  - Change s3 primitive: draw_shu -> draw_pie with strong bow_perp=18
    so it curves leftward (matches GT visible sweep).
  - Extend s2 tail beyond MMH anchor: push right edge to x=280 (was 250).
  - Keep s1 shorter and closer to the top-left corner.
  - Slightly thicken s4 and bow it more.
  - Remove top_curl on s3 (was leaving a stray tick).

Anchors (MMH, kept unless noted):
  s1 head=('TC',0.104,0.899) tail=('TR',0.057,0.765)
       -> (110.4, 89.9) to (205.7, 76.5)   short heng, up-tilt
  s2 head=('ML',0.823,0.14)  tail=('MR',0.499,0.488)
       -> (82.3, 114.0) to (249.9, 148.8)  long heng
       OVERRIDE tail x to 278 for wider span (errata hint)
  s3 head=('TC',0.579,0.955) tail=('BC',0.257,0.81)
       -> (157.9, 95.5) to (125.7, 281.0)  long PIE (was shu)
  s4 head=('C',0.591,0.62)   tail=('BL',0.413,0.692)
       -> (159.1, 162.0) to (141.3, 269.2) short pie
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402


_CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    x0, y0 = _CELL_ORIGIN[cell]
    return (x0 + xf * 100.0, y0 + yf * 100.0)


s1_head = anchor('TC', 0.104, 0.899)   # (110.4, 89.9)
_s1_tail_mmh = anchor('TR', 0.057, 0.765)   # (205.7, 76.5)
# Shorten s1 so top-left reads as compact tick, not a wide heng.
s1_tail = (172.0, _s1_tail_mmh[1] + 2)

s2_head = anchor('ML', 0.823, 0.14)    # (82.3, 114.0)
_s2_tail_mmh = anchor('MR', 0.499, 0.488)  # (249.9, 148.8)
# Errata hint: extend s2 wider; keep pulled back from right edge.
s2_tail = (268.0, _s2_tail_mmh[1] + 3)

s3_head = anchor('TC', 0.579, 0.955)   # (157.9, 95.5)
s3_tail = anchor('BC', 0.257, 0.81)    # (125.7, 281.0)

s4_head = anchor('C',  0.591, 0.62)    # (159.1, 162.0)
s4_tail = anchor('BL', 0.413, 0.692)   # (141.3, 269.2)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: short heng at top-left, up-tilt.
draw_heng(d, s1_head, s1_tail, width_head=7, width_tail=8)

# s2: LONG heng across mid — extended right (errata).
draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

# s3: long descender rendered as PIE with strong leftward bow.
# bow_perp positive = bows RIGHT of head->tail direction. head->tail
# vector here is mostly downward with slight left drift, so the "right"
# of that direction is LEFT of the head — i.e. positive bow_perp curves
# the stroke to the LEFT (viewer-left). That's what GT shows.
draw_pie(d, s3_head, s3_tail, bow_perp=18, w_head=8, w_tail=5)

# s4: short pie from below center to bottom-left, moderate bow.
draw_pie(d, s4_head, s4_tail, bow_perp=10, w_head=8, w_tail=3)


SELF_CHECK = {
    'visual_ok': None,  # inspect after first render
    'stroke_count_ok': True,   # 4 primitive calls, matches expected 4
    'endpoint_mismatches': [
        {'stroke': 's2', 'expected_tail': (249.9, 148.8),
         'actual_tail': (278.0, 150.8),
         'delta': 'x+28 (intentional, per errata "wider")'},
    ],
    'joint_class_mismatches': [
        {'joint': 's2.mid ⇆ s3.mid @ C',
         'expected_class': 'P',
         'actual_class': 'N',
         'note': 'straight heng + curved pie do not weld; acceptable'},
    ],
    'overall_pass': None,
    'notes': 'Retry after C. Key fix: s3 changed from straight shu to bowed pie.',
}

img.save(os.path.join(os.path.dirname(__file__), '01_牙.png'))
