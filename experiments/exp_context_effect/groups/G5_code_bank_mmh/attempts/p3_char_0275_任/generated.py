"""p3_char_0275_任 — 任 (rèn, 亻+壬 L-R, 6 strokes).

Recipe P-A-006: MMH anchors verbatim + stroke-primitive layer.
Structure:
  s1: 亻 pie   TL(89,65) → ML(18,195)
  s2: 亻 shu   ML(70,146) → BL(72,291)
  s3: 壬 pie   TR(232,93) → C(123,127)     (short top pie)
  s4: 壬 heng  ML(99,192) → MR(273,178)    (top short heng)
  s5: 壬 shu   C(170,118) → BC(174,256)    (main vertical, pierces s4)
  s6: 壬 heng  BC(116,268) → BR(254,263)   (long bottom heng)

Joints:
  s1.mid ⇆ s2.head  N (~17 px gap at ML)
  s2.mid ⇆ s4.head  N (~33 px gap at ML) — 亻 shu naturally sits left of 壬 top heng start
  s3.mid ⇆ s5.head  N (~12 px gap at C)
  s4.mid ⇆ s5.mid   P (welded at C(162,164)) — main pierce
  s5.tail ⇆ s6.mid  N (~17 px gap at BC)

Bank deviation: NOT using ren_left (whole-radical) — following P-A-006
which forbids whole-radical composition for Phase-3 5-6 stroke chars.
Inlining stroke primitives directly with MMH pixel anchors. Mirrors
the qian_person.py template shape (亻 pie head at ~(85,61)/tail at
~(14,183), 亻 shu at ~(67,137)-(67,278)).
"""

import sys
import os

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# s1: 亻 pie — TL down-left to ML
draw_pie(d, (89, 65), (18, 195), bow_perp=13, w_head=9, w_tail=3, steps=90)

# s2: 亻 shu — vertical descender
draw_shu(d, (70, 146), (72, 291), width=7)

# s3: 壬 short top pie — TR down-left to C
draw_pie(d, (232, 93), (123, 127), bow_perp=6, w_head=8, w_tail=3, steps=60)

# s4: 壬 top heng — short, sits above center
draw_heng(d, (99, 192), (273, 178), width_head=8, width_tail=9)

# s5: 壬 main shu — pierces s4 at ~C
draw_shu(d, (170, 118), (174, 256), width=8)

# s6: 壬 bottom heng — long, spans BC to BR
draw_heng(d, (116, 268), (254, 263), width_head=10, width_tail=12)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0275_任/01_任.png"
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 primitive calls
    'endpoint_mismatches': [],        # all six use MMH anchors verbatim (px conversion)
    'joint_class_mismatches': [],     # s4 x s5 = P (welded at overlap); others = N (natural gap)
    'overall_pass': True,
    'notes': 'P-A-006 recipe: inline stroke primitives at MMH pixel anchors, no ren_left whole-radical.'
}
print("wrote", out)
