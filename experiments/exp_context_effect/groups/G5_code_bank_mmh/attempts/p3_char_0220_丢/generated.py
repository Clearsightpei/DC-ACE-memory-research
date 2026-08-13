"""p3_char_0220_丢 — G5 attempt.

Composition: 6 strokes.
  s1: pie (top slash)        — TR head → ML tail
  s2: short heng (upper mid) — ML → MR
  s3: shu (central vertical) — C → C (top to lower-mid)
  s4: long heng (mid-lower)  — BL → MR
  s5: pie_zhe (ム left)      — BC head → BR tail (with corner low-left)
  s6: dian (ム dot / na)     — BC → BR

Bank reuse: pie, heng, shu, pie_zhe, dian (all present).
No BANK_DEVIATION.
"""

import os
import sys

# Add bank code to path
_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw  # noqa: E402
from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: pie, heng, shu, heng, pie_zhe, dian
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors from MMH block, decoded PIL y-down within each cell.',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top pie (TR→ML). Anchors: (202,84)→(90,108).
    draw_pie(d, (202, 84), (90, 108),
             bow_perp=10, w_head=9, w_tail=3, steps=90)

    # s2: short heng in upper-middle (ML→MR). (79,151)→(212,137).
    draw_heng(d, (79, 151), (212, 137),
              width_head=8, width_tail=9)

    # s3: central shu (C→C top-to-lower-mid). (137,103)→(146,190).
    draw_shu(d, (137, 103), (146, 190), width=7)

    # s4: long heng across mid-lower (BL→MR). (36,208)→(274,197).
    draw_heng(d, (36, 208), (274, 197),
              width_head=10, width_tail=12)

    # s5: ム pie_zhe (BC head → BR tail).
    # head (158, 212) sweeps down-left to corner ≈ (108, 268),
    # then folds right to tail (200, 266).
    draw_pie_zhe(d,
                 head=(158, 212),
                 corner=(108, 268),
                 tail=(200, 266),
                 pie_bow=6, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4, steps=70)

    # s6: dian on right of ム (BC→BR). (185, 234)→(227, 293).
    draw_dian(d, (185, 234), (227, 293),
              w_head=3, w_tail=7, bow=4, steps=48)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_丢.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
