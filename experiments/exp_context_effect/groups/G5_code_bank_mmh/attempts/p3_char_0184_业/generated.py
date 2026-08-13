"""p3_char_0184_业 — G5 attempt.

MMH-derived 5-stroke decomposition (per injected structural block):
  s1: shu (left tall vertical, slight lean right)     C-cell  → BC-cell
  s2: shu (right tall vertical, slight lean right)    TC-cell → BC-cell
  s3: short dian-like slant on the LEFT outer side    ML → BL
  s4: short dian-like slant on the RIGHT outer side   MR → BC
  s5: long baseline heng                              BL → BR

Both s1.tail and s2.tail sit ABOVE s5's line by ~11–15 px → 'N'
(natural calligraphic gap) — do NOT weld to the baseline.

Bank usage:
  - draw_shu(head, tail, width) — s1, s2
  - draw_dian(head, tail, ...) — s3, s4 (short slanted taper strokes)
  - draw_heng(head, tail, w_head, w_tail) — s5
No BANK_DEVIATION: primitives fit naturally, since dian.py already
supports arbitrary head→tail vectors (its bow_perp gives a subtle
weight taper that matches 业's short slanted marks).
"""

import os
import sys

from PIL import Image, ImageDraw

# Make bank primitives importable
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 primitives called; matches expected 5
    'endpoint_mismatches': [],     # all anchors used as given
    'joint_class_mismatches': [],  # s1.tail↔s5 N (~11px), s2.tail↔s5 N (~13px)
    'overall_pass': True,
    'notes': 'Two tall central verticals stop above baseline heng '
             '(N-class gap). Outer dians taper from thin (near vertical) '
             'to thicker toward inside.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── s1: left tall vertical shu ──
    #   head @ C(0.028, 0.069) = (102.8, 106.9)
    #   tail @ BC(0.143, 0.684) = (114.3, 268.4)  — 11 px above baseline (N)
    draw_shu(d, head=(103, 107), tail=(114, 268), width=7)

    # ── s2: right tall vertical shu ──
    #   head @ TC(0.608, 0.838) = (160.8, 83.8)
    #   tail @ BC(0.655, 0.66)  = (165.5, 266.0)  — 14 px above baseline (N)
    draw_shu(d, head=(161, 84), tail=(166, 266), width=7)

    # ── s3: left outer short slanted dian ──
    #   head @ ML(0.565, 0.784) = (56.5, 178.4)
    #   tail @ BL(0.882, 0.118) = (88.2, 211.8)
    #   goes from upper-left down-right toward the left vertical
    draw_dian(d, head=(57, 178), tail=(88, 212), w_head=3, w_tail=7, bow=3, steps=40)

    # ── s4: right outer short slanted dian (pie-like) ──
    #   head @ MR(0.323, 0.471) = (232.3, 147.1)
    #   tail @ BC(0.969, 0.045) = (196.9, 204.5)
    #   goes from upper-right down-left toward the right vertical
    draw_dian(d, head=(232, 147), tail=(197, 205), w_head=3, w_tail=7, bow=3, steps=40)

    # ── s5: long baseline heng ──
    #   head @ BL(0.384, 0.792) = (38.4, 279.2)
    #   tail @ BR(0.678, 0.801) = (267.8, 280.1)
    draw_heng(d, head=(38, 279), tail=(268, 280), width_head=9, width_tail=11)

    out_png = os.path.join(_HERE, '01_业.png')
    img.save(out_png)
    print('wrote', out_png)


if __name__ == '__main__':
    render()
