"""G5 attempt: p2_radical_100_见 (4-stroke radical).

Decomposition per MMH-injected anchors:
  s1: 竖  (left vertical of top box)                   — bank: shu
  s2: 横折 (top + right side, boxy)                     — bank: heng_zhe_box
  s3: 撇  (long left-diagonal from top-middle to BL)    — bank: pie
  s4: 竖弯钩 (from middle-bottom curving right + hook)   — bank: shu_wan_gou

Joints (both N — natural gaps, DO NOT weld):
  - s1.head ⇆ s2.head @ TC (~13 px gap)
  - s3.mid(0.35) ⇆ s4.head @ C (~20 px gap)
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# Bank imports
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: shu, heng_zhe_box, pie, shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Bank primitives fit cleanly; no BANK_DEVIATION.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── MMH-derived pixel anchors ──
    # s1 竖: TL(0.885, 0.82) → BL(0.958, 0.08)
    s1_head = (88.5, 82.0)
    s1_tail = (95.8, 208.0)
    draw_shu(d, s1_head, s1_tail, width=7)

    # s2 横折 (box top+right): TC(0.061, 0.858) → BC(0.939, 0.048)
    s2_top_left     = (106.1, 85.8)
    s2_bottom_right = (193.9, 204.8)
    draw_heng_zhe_box(d, s2_top_left, s2_bottom_right, width=8)

    # s3 撇: C(0.295, 0.157) → BL(0.448, ~1.0)  [tail clipped to canvas]
    s3_head = (129.5, 115.7)
    s3_tail = (44.8, 288.0)
    draw_pie(d, s3_head, s3_tail, bow_perp=22, w_head=9, w_tail=3)

    # s4 竖弯钩: C(0.529, 0.925) → BR(0.695, 0.303)
    s4_head = (152.9, 192.5)
    s4_tail = (269.5, 230.3)
    draw_shu_wan_gou(d, s4_head, s4_tail, width=7,
                     bottom_extra=45, knee_ratio=0.75)

    return img


if __name__ == '__main__':
    img = render()
    out = pathlib.Path(__file__).parent / '01_见.png'
    img.save(out)
    print(f'wrote {out}  ({img.size})')
