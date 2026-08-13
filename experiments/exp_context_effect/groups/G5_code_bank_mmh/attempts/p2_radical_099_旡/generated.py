"""Render 旡 (p2_radical_099) — 4 strokes.

Uses G5 bank primitives (heng, pie, shu_wan_gou).

MMH-derived plan (y-down convention, verified by joint-anchor cross-check):
  s1 heng (top-right short tick):  (103, 90)  -> (211, 78)
  s2 heng (main horizontal):       (78, 114)  -> (231, 147)
  s3 pie  (left leg):              (130, 100) -> (42, 288)
  s4 shu-wan-gou (right hook):     (154, 169) -> (268, 235)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank/code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls, 4 strokes
    'endpoint_mismatches': [
        {'stroke': 3, 'expected': 'BL(0.419,0.883)=(42,288)', 'actual': '(85,262)',
         'delta': 'pie shortened ~40 px — MMH gives median extending past visible ink'},
        {'stroke': 4, 'expected': 'C(0.541,0.69)=(154,169)', 'actual': '(200,150)',
         'delta': 'head shifted right-up ~45 px to attach to s2 tail (visible in GT).'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('MMH y-down decoded via joint-anchor cross-check. Revision 1 '
              'shortens pie tail and attaches s4 head to s2 tail per GT silhouette; '
              'reduces heng tail width to remove oversized end-dot dab.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1: small top-right heng — tapered thin, no tail dab bulge
    draw_heng(d, (108, 88), (218, 78), width_head=6, width_tail=6)

    # stroke 2: main heng, slight down-right tilt per MMH
    draw_heng(d, (78, 116), (238, 143), width_head=8, width_tail=8)

    # stroke 3: pie sweeping down-left from top-center. Anchor override:
    # MMH tail BL(42,288) puts the tip off-character; GT visible ink ends
    # around (85, 262). Shortened accordingly.
    draw_pie(d, (130, 100), (85, 262), bow_perp=14, w_head=8, w_tail=3)

    # stroke 4: shu-wan-gou. Anchor override: MMH head C(154,169) leaves a
    # gap from s2 tail; GT shows the vertical attaching to the heng near
    # (200, 148). Tail (268, 235) kept per MMH (hook curls up-right).
    draw_shu_wan_gou(d, (200, 150), (268, 235),
                     width=7, bottom_extra=45, knee_ratio=0.7)

    out = Path(__file__).with_name('01_旡.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
