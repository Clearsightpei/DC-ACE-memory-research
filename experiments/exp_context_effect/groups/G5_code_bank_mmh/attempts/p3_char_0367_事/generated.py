"""G5 attempt: p3_char_0367_事 (8 strokes).

DECOMPOSITION (per MMH anchors + GT):
- s1 top wide heng
- s2 short vertical descender (left side of upper compartment)
- s3 short heng (top of upper compartment interior)
- s4 heng (middle interior of compartment)
- s5 heng-zhe compound (long heng turning down on right — forms the
  right-side spine of the middle group). Inlined as heng + short shu
  since bank's heng_zhe primitives don't quite match this aspect.
- s6 wide bottom heng
- s7 short heng inside bottom compartment
- s8 CENTRAL shu-gou piercing everything (drawn last)

P-A-006 recipe: MMH-anchor-verbatim endpoints + stroke-primitive layer.
No whole-radical primitive fits 事 (unique 龶+口+亅 layout), so P-A-007
whole-radical hard-check doesn't trigger.

# BANK_DEVIATION
# skipped: none whole-radical; s5 uses inline heng+shu instead of
#   heng_zhe_gou / heng_zhe_wide primitives
# reason: s5's aspect (78..202 x-span, 180→156→200 with slight up-then-down)
#   is a long heng-zhe with modest descent — bank heng_zhe_gou expects
#   a proper leftward hook (absent here) and heng_zhe_wide expects a
#   near-box aspect. Inline two-segment better matches the MMH mids.
# fresh_component: inline_heng_zhe_no_hook_for_事

SELF_CHECK filled in after render below.
"""

import os
import sys

# make bank importable
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw  # noqa: E402

from heng import draw_heng          # noqa: E402
from shu import draw_shu            # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top wide heng: TL(0.44,0.97) → TR(0.53,0.86)
    draw_heng(d, (44, 97), (253, 86), width_head=9, width_tail=10)

    # s2 — short vertical descender: ML(0.82,0.18) → C(0.01,0.62)
    draw_shu(d, (82, 118), (101, 162), width=7)

    # s3 — short heng (top of upper compartment): ML(0.96,0.18) → C(0.84,0.34)
    draw_heng(d, (96, 118), (184, 134), width_head=7, width_tail=8)

    # s4 — middle heng: C(0.055,0.506) → C(0.995,0.436)
    draw_heng(d, (105, 151), (200, 144), width_head=7, width_tail=8)

    # s5 — heng-zhe compound (long heng turning down):
    #   head ML(0.782,0.805)=(78,180), through mids
    #   (103,171)->(147,173)->(199,156) turn to tail welded near s6.mid(0.73)=(202,200)
    # inline as heng from (78,180) to (200,160) then shu from (200,160) to (202,200)
    draw_heng(d, (78, 180), (200, 160), width_head=8, width_tail=9)
    draw_shu(d, (200, 160), (202, 200), width=8)

    # s6 — wide bottom heng: BL(0.404,0.142) → BR(0.619,0.01)
    draw_heng(d, (40, 214), (262, 201), width_head=10, width_tail=11)

    # s7 — inside-bottom heng: BL(0.826,0.408) → BR(0.068,0.329)
    draw_heng(d, (83, 241), (207, 233), width_head=7, width_tail=8)

    # s8 — central shu-gou piercing everything:
    #   head TC(0.362,0.521)=(136,52), tail BC(0.025,0.804)=(102,280)
    draw_shu_gou(d, (136, 52), (102, 280), width=8, hook_start_offset=32)

    out = os.path.join(os.path.dirname(__file__), '01_事.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,          # filled after visual comparison
    'stroke_count_ok': True,    # 8 primitive calls counted (s5 is 2 segments but represents 1 MMH stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': (
        's5 rendered as inline heng+shu = 1 MMH stroke (compound). '
        'Primitive-call count = 9 draw_* calls but MMH stroke count = 8.'
    ),
}


if __name__ == '__main__':
    print(render())
