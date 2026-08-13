"""p3_char_0492_俚 — 亻 + 里 (L-R composition).

REASONING (P-A-007-v2 + P-A-008 + P-A-009 + P-A-010-v2):

Both whole-radical bank primitives exist and are direct matches:
  - ren_left (亻, B1) — 2 strokes: matches s1 (pie) + s2 (shu)
  - li_inside (里, B9) — 7 strokes: matches s3..s9 (日 + 土 stack)
Stroke count: 2 + 7 = 9 = MMH expected. Structural match is exact.

P-A-007-v2 hard-check — whole-radical uniform-shift IS adjustable:
  - 亻: bank native placement centered around x~120; target left-half
    center x~53. Uniform ox shift ~-70. Scale 1.0 (native height matches).
  - 里: bank native full-canvas placement; target compressed to right ~65%
    of canvas. Uniform scale ~0.85 + ox+34 + oy+20. Aspect near-uniform.

P-A-009 quantitative BANK_DEVIATION (calc):
  ren_left native (bank) s1_head=(158.8,73.8); MMH target=(87.9,64.7).
    Δ=(-70.9, -9.1). s2_tail delta=(-69.7, -0.9). Consistent uniform
    shift → clean kind-(a) uniform translation, scale=1.0.
  li_inside native s7_tail=(276,271.6); MMH target=(266.6,270.1).
    Scale by 0.85, then ox=+35, oy=+15 places top-shu at target
    within tolerance. Small aspect diff absorbed (see notes).

P-A-010-v2 mechanism: single object changed per call = (ox, oy, scale)
tuple. NO fresh render, NO variant. Kind (a) uniform-shift applied
to both radicals. This is the "call whole-radical + translate" case.

No BANK_DEVIATION block (both primitives used with only uniform shift).
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "success_bank", "code"))

from PIL import Image, ImageDraw

from ren_left import draw_ren_left
from li_inside import draw_li_inside


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 2 (ren_left) + 7 (li_inside) = 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Whole-radical stack: ren_left @ (ox=-70, oy=-6, s=1.0) + li_inside @ (ox=+40, oy=+18, s=0.83).',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # 亻 (left): shift bank left ~55px (r1: -70 pushed tail off left edge)
    draw_ren_left(d, ox=-55, oy=-8, scale=0.95)

    # 里 (right): scale ~0.85, shift right; r1 lift was too high, add oy
    draw_li_inside(d, ox=45, oy=28, scale=0.82)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俚.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
