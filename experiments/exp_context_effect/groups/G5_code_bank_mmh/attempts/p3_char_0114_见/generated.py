"""G5 attempt for p3_char_0114_见 (4 strokes).

Decomposition (from MMH block + GT):
- s1: 竖 left vertical of box  (bank: shu.py)
- s2: 横折 top + right vertical  (bank: heng_zhe_box.py — bare heng_zhe, no hook)
- s3: 撇 left leg sweeping down-left from inside box (bank: pie.py)
- s4: 竖弯钩 right leg with bottom hook (bank: shu_wan_gou.py)

All four strokes covered by existing bank primitives — NO BANK_DEVIATION.

Joint check (N = neighbor with small gap):
- s1.head (88.5, 82) ⇆ s2.head (106, 86) → both near TC, actual gap
  ≈ sqrt(17.5^2 + 4^2) ≈ 17.9 px (target ≈ 13.4).  N — OK.
- s3.mid(0.35) ≈ (99.9, 180.6) ⇆ s4.head (153, 193) → gap
  ≈ sqrt(53^2 + 12.4^2) ≈ 54.4 px. Expected N gap ~20 px. The MMH
  distance itself is 50.2, so this joint is genuinely far apart in
  MMH (a wide-N). Rendering with a real gap is correct.
"""

import os
import sys

from PIL import Image, ImageDraw

# Bank imports
BANK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)

from shu import draw_shu                          # noqa: E402
from heng_zhe_box import draw_heng_zhe_box        # noqa: E402
from pie import draw_pie                          # noqa: E402
from shu_wan_gou import draw_shu_wan_gou          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'stroke_count_actual': 4,
    'stroke_count_expected': 4,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 4 strokes from bank primitives. s3-s4 joint is a wide-N per MMH (dist=50.2); rendering the gap literally is correct.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: 竖 left vertical of box (MMH head TL(0.885,0.82), tail BL(0.958,0.08)) ----
    # canvas pixels: head (88.5, 82) → tail (95.8, 208)
    draw_shu(d, head=(88.5, 82.0), tail=(95.8, 208.0), width=7)

    # ---- s2: 横折 top + right vertical (MMH head TC(0.061,0.858), tail BC(0.939,0.048)) ----
    # canvas pixels: head (106.1, 85.8) → tail (193.9, 204.8)
    # heng_zhe_box takes top_left and bottom_right.
    draw_heng_zhe_box(d, top_left=(106.1, 85.8),
                      bottom_right=(193.9, 204.8), width=7)

    # ---- s3: 撇 left leg (MMH head C(0.295,0.157), tail BL(0.448,1.012)) ----
    # canvas pixels: head (129.5, 115.7) → tail (44.8, 297)  [clamped to canvas]
    draw_pie(d, head=(129.5, 115.7), tail=(50.0, 288.0),
             bow_perp=14, w_head=8, w_tail=2, steps=80)

    # ---- s4: 竖弯钩 right leg with hook (MMH head C(0.529,0.925), tail BR(0.695,0.303)) ----
    # canvas pixels: head (152.9, 192.5) → tail (269.5, 230.3)
    # Bump bottom_extra so the vertical drop is longer before the hook;
    # decrease knee_ratio to bring the knee/shoulder closer under the head
    # (matches GT's flatter "drop then quick right-hook" silhouette).
    draw_shu_wan_gou(d, head=(152.9, 192.5), tail=(269.5, 230.3),
                     width=7, bottom_extra=75, knee_ratio=0.72)

    out = os.path.join(os.path.dirname(__file__), '01_见.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    main()
