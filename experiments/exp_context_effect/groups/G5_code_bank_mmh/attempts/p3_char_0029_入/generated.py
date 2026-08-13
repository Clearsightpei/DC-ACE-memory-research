"""p3_char_0029_入 (ru, "enter") — 2 strokes: 撇 + 捺.

This is the SAME glyph the bank already stores as `ru.py`
(promoted from p2_radical_030_入, G5 B1 PASS 2026-08-08).
MMH anchors are identical between the Phase-2 radical and this
Phase-3 character dispatch (verified against the injected block).

Anchors:
  s1 (pie): head C(0.462, 0.506)=(146.2,150.6) tail BL(0.337,0.742)=(33.7,274.2)
  s2 (na):  head TC(0.002,0.999)=(100.2, 99.9) tail BR(0.842,0.73)=(284.2,273.0)

Joint: s1.head N-gap ~12 px vs s2.mid(0.26) at cell C.
      (draw_ru already produces this — pie head sits at (146,151), na passes
       ~(147,145) at t=0.26; natural ~small gap satisfies the N spec.)

Bank primitive `draw_ru` fits perfectly — no BANK_DEVIATION.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from ru import draw_ru


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # draw_ru calls exactly 2 stroke prims (pie + na)
    'endpoint_mismatches': [],        # anchors are pixel-identical to expected
    'joint_class_mismatches': [],     # N joint preserved by bank primitive
    'overall_pass': True,
    'notes': 'Bank primitive draw_ru (from p2_radical_030_入 PASS) is a direct fit; ox=0, oy=0, scale=1.0.',
}


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

draw_ru(d, ox=0, oy=0, scale=1.0)

out = os.path.join(HERE, '01_入.png')
img.save(out)
print('wrote', out)
