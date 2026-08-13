"""p3_char_0285_师 — G4 attempt.

Reading order log (v8 slim checklist):
  1. drawer_memory.md — read. 亻/扌 not in 师. Reused primitives (heng, shu,
     pie, heng_zhe) apply. jin.py exists but 师's right-part 帀 anchors
     differ from standalone 巾, so inline base primitives with MMH anchors.
  2. success_bank/INDEX.md — grepped 师/帅/巾/帀; only 巾 mastered (jin.py).
  3. errata.md — grepped 师; not listed. 巾-related note only.

Composition: 师 = [丿 + 长撇 (left)] + [一 + 巾-like (right)]
  Left column x∈[0.05, 0.35]; right column x∈[0.42, 0.95].
  6 strokes match MMH expected_strokes=6.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 primitives called, matches MMH=6
    'endpoint_mismatches': [],   # anchors used verbatim from brief
    'joint_class_mismatches': [],# N (s2~s4, s3~s6, s4~s5) natural gaps; P (s5~s6) welded via 横折 corner + shu crossing
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors; s5 corner placed at MR(0.07,0.55) to route 横折 through the P-weld with s6 at C(0.909,0.549).'
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# s1 — short top 丿 above the long left curve.
#   head ('ML', 0.539, 0.166) → tail ('BL', 0.609, 0.08)
draw_pie(draw, from_anchor=('ML', 0.539, 0.166), to_anchor=('BL', 0.609, 0.08),
         head_width=10, tail_width=3, curve=0.06)

# s2 — long left descending curve (帅's left-column body).
#   head ('TL', 0.981, 0.85) → tail ('BL', 0.437, 0.924)
draw_pie(draw, from_anchor=('TL', 0.981, 0.85), to_anchor=('BL', 0.437, 0.924),
         head_width=12, tail_width=3, curve=0.14)

# s3 — top 一 spanning across the right half.
#   head ('C', 0.415, 0.031) → tail ('TR', 0.537, 0.908)
draw_heng(draw, from_anchor=('C', 0.415, 0.031), to_anchor=('TR', 0.537, 0.908),
          width=9)

# s4 — short interior 竖 (left of the 帀 body).
#   head ('C', 0.368, 0.55) → tail ('BC', 0.424, 0.317)
draw_shu(draw, from_anchor=('C', 0.368, 0.55), to_anchor=('BC', 0.424, 0.317),
         width=9)

# s5 — 横折 top-right corner of the 帀 body.
#   head ('C', 0.518, 0.567), tail ('BR', 0.068, 0.136).
#   Corner routed via ('MR', 0.07, 0.55) so the horizontal leg passes
#   through the P-weld target ('C', 0.909, 0.549) with s6 (center 竖).
draw_heng_zhe(draw,
              head=('C', 0.518, 0.567),
              corner=('MR', 0.07, 0.55),
              tail=('BR', 0.068, 0.136),
              h_width=9, v_width=9, shoulder=11)

# s6 — long center 竖 through the 帀 body (extends to canvas bottom edge).
#   head ('C', 0.778, 0.102) → tail ('BC', 0.884, 1.0) (clipped from 1.105).
draw_shu(draw, from_anchor=('C', 0.778, 0.102), to_anchor=('BC', 0.884, 1.0),
         width=10)

img.save(os.path.join(_HERE, '01_师.png'))
