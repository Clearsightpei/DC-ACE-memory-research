"""p3_char_0409_油 — G5 attempt.

油 = 氵 (left, 3 strokes) + 由 (right, 5 strokes) = 8 strokes total.

Composition strategy (P-A-007-v2: whole-radical bank primitives match well):
  - Left: draw_sanshui (bank primitive) — 氵 water radical, 3 strokes
  - Right: draw_you_by (bank primitive) — 由, 5 strokes

Both primitives are HIGH-REUSE bank entries. 由 was itself PASSed at B7
with 5 strokes matching MMH structure. 氵 was PASSed at B2 (bootstrap).

BANK_DEVIATION analysis (P-A-009 quantitative):
  - Native 氵 spans (x:92-174, y:77-294) = 82w x 217h. Aspect (h/w) = 2.65.
  - Native 由 spans (x:51-210, y:63-289) = 159w x 226h. Aspect (h/w) = 1.42.
  - Target composition in 300x300: 氵 in left ~1/4 (x:20-90), 由 in right ~2/3 (x:105-260).
  - 氵 target: width ~62 → scale ≈ 62/82 = 0.76. Height ~163 (77-260 target).
  - 由 target: width ~155 → scale ≈ 155/159 = 0.97. Height ~217.
  - Both scales in [0.55, 1.2] range → P-A-007-v2 says USE whole-radical.
  - No BANK_DEVIATION needed — both bank entries fit target aspects.

MMH anchor cross-check (8 strokes):
  s1-s3: 氵 (top-dian, middle-dian, bottom-ti)
  s4-s8: 由 (heng_zhe, left-shu, bottom-heng, central-shu, middle-heng)

Joints (7 total): all internal to each sub-radical (s4-s8 are 由 internal).
  s4/s5 in C: box top-left corner (N, gap ~14)
  s4/s6 in BC: bottom-left corner (N, gap ~29)
  s4/s8 in BC: bottom-right corner (N, gap ~9)
  s5/s7 in C: central shaft crosses top of box (P, welded)
  s5/s8 in BR: bottom-right corner (N, gap ~20)
  s6/s7 in BC: middle heng crossed by shaft (P, welded)
  s7/s8 in BC: shaft ends above bottom (N, gap ~14)
"""

import os
import sys

# Add bank code directory to path
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK_CODE)

from PIL import Image, ImageDraw

from sanshui import draw_sanshui
from you_by import draw_you_by


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 (sanshui) + 5 (you_by) = 8 ✓
    'endpoint_mismatches': [],    # bank primitives use MMH-derived positions internally
    'joint_class_mismatches': [], # all 7 joints internal to bank primitives (validated at B7 PASS for 由)
    'overall_pass': True,
    'notes': 'Composition of two high-reuse bank primitives (氵 + 由). Both bank scales in [0.55, 1.2] range per P-A-007-v2.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # 氵 on the left: shift left and shrink slightly
    # Native 氵 center ~(133, 185); target center ~(55, 165)
    # scale 0.76: ox = 55 - 133*0.76 = -46. oy = 165 - 185*0.76 = 24.
    draw_sanshui(draw, ox=-46, oy=24, scale=0.76)

    # 由 on the right: mostly full-size, shifted right
    # Native 由 center ~(131, 176); target center ~(180, 155)
    # scale 0.95: ox = 180 - 131*0.95 = 55. oy = 155 - 176*0.95 = -12.
    draw_you_by(draw, ox=55, oy=-12, scale=0.95)

    out = os.path.join(_HERE, "01_油.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
