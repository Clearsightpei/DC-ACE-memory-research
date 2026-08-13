"""p3_char_0019_儿 — G5 retry_1.

TRAJECTORY DIFF (from PNG inspection of main + GT):

Main attempt FAIL — concrete visual gaps:
  1. Pie was OVER-CURVED (bow_perp=14). The rendered left stroke reads
     like a fat "C"/banana rather than a gentle 撇. GT's pie is much
     straighter — a gentle sweep with only mild rightward bow.
  2. Pie head was pushed too far RIGHT (main used x=140 vs MMH x≈93).
     This moved the pie's top into center canvas and made both strokes
     visually crowd each other at the top. GT clearly shows the pie
     starting near the LEFT of the top-center area (x≈95).
  3. Shu-wan-gou HOOK barely visible in main render: bottom_extra=55 +
     knee_ratio=0.88 gave a shallow bottom sweep with no clear upward
     hook tip. GT shows a definite bottom shoulder and a short but
     visible upward hook at the tail.

Fixes this attempt:
  - Trust MMH pie head (~93, 100) instead of the over-shifted (140,95).
    Small y-nudge up (y=95) matches GT better than MMH's y=109.
  - Drop bow_perp to 8 (gentle sweep, not banana).
  - Shu-wan-gou: use head near MMH TC (157, 85), tail near MMH BR
    (272, 220), bump bottom_extra to 70 for a fuller shoulder, keep
    knee_ratio at 0.80 so the bottom curve reaches ~x=245 before the
    hook lifts to the tail. This should make the hook read clearly.

Bank primitives used: draw_pie, draw_shu_wan_gou (no BANK_DEVIATION —
the primitives fit; the previous failure was parameter tuning, not
primitive mismatch).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def render() -> Image.Image:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 撇 (pie). MMH head ML(0.929,0.093)=(93,109); GT shows the
    # pie top a bit higher, ~y=95, so nudge up slightly. Gentle bow.
    draw_pie(d, head=(95, 95), tail=(50, 285),
             bow_perp=8, w_head=9, w_tail=3)

    # s2 — 竖弯钩. MMH head TC(0.567,0.838)=(157,84); tail BR(0.71,0.227)=(271,223).
    # Bigger bottom_extra so the shoulder sweeps low, then hook lifts up
    # to the tail near BR.
    draw_shu_wan_gou(d, head=(158, 88), tail=(272, 222),
                     width=8, bottom_extra=70, knee_ratio=0.80)

    return img


SELF_CHECK = {
    'visual_ok': None,           # set after inspection
    'stroke_count_ok': True,     # 2 primitives, matches expected 2
    'endpoint_mismatches': [
        # s1 head: MMH (93,109), actual (95,95). Δ=(+2,-14).
        # y-nudge is deliberate (GT top of pie sits above MMH y).
        {'stroke': 1, 'expected': 'ML(0.929,0.093)', 'actual': '(95,95)',
         'delta': '+2x -14y (deliberate — GT top of pie above MMH y)'},
        {'stroke': 1, 'expected': 'BL(0.393,0.827)', 'actual': '(50,285)',
         'delta': '+11x +2y (within tolerance)'},
        {'stroke': 2, 'expected': 'TC(0.567,0.838)', 'actual': '(158,88)',
         'delta': '+1x +4y (within tolerance)'},
        {'stroke': 2, 'expected': 'BR(0.71,0.227)', 'actual': '(272,222)',
         'delta': '+1x -1y (within tolerance)'},
    ],
    'joint_class_mismatches': [],  # no joints expected (strokes separate)
    'overall_pass': None,
    'notes': 'retry_1: reverted over-shifted pie head, dropped bow to 8, '
             'extended shu_wan_gou bottom_extra to 70 for visible hook.',
}


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_儿.png'
    render().save(out)
    print(f'wrote {out}')
