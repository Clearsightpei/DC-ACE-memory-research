"""G5 attempt for p3_char_0249_同 (tong, "same" — 6 strokes).

Composition (from MMH anchors):
  s1: LEFT frame 竖         shu       (65.6, 80.6) -> (66.5, 281.5)
  s2: RIGHT frame 横折钩    heng_zhe_gou (85.5, 86.4) corner (215, 86) tail (200, 268) hook (183, 273)
  s3: interior top 一        heng      (110.4, 131) -> (184.0, 123.0)
  s4: 口 left 竖             shu       (105.5, 170.2) -> (123.3, 228.8)
  s5: 口 横折 (top+right)    heng_zhe_box top_left (121.9, 177) bottom_right (164.6, 218)
  s6: 口 bottom 一           heng      (128.9, 218) -> (180.2, 212.1)

Uses bank primitives: shu, heng, heng_zhe_gou, heng_zhe_box.
P-A-006 style: MMH anchors verbatim + stroke primitives, no whole-radical composition.
"""

import os, sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)

from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 primitive calls, matches MMH count
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 4 joints are N (natural gap), preserved by MMH-verbatim coords
    'overall_pass': True,
    'notes': ('MMH anchors used verbatim for s1/s3/s4/s6. s2 heng_zhe_gou corner extrapolated '
              'to (215,86) to reach right frame; hook at MMH tail. s5 heng_zhe_box bottom_right y '
              'extended from 202 -> 218 so the interior 口 closes with s6 bottom bar.')
}


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: LEFT frame vertical shu
    draw_shu(d, (65.6, 80.6), (66.5, 281.5), width=7)

    # s2: RIGHT frame 横折钩
    draw_heng_zhe_gou(d,
                      heng_head=(85.5, 86.4),
                      corner=(215.0, 86.0),
                      gou_tail=(210.0, 268.0),
                      hook_tip=(183.1, 273.0))

    # s3: interior top short 一
    draw_heng(d, (110.4, 131.0), (184.0, 123.0), width_head=6, width_tail=7)

    # s4: 口 left short 竖
    draw_shu(d, (105.5, 170.2), (123.3, 228.8), width=5)

    # s5: 口 横折 (top+right) — extend bottom_right y so the box closes with s6
    draw_heng_zhe_box(d, top_left=(121.9, 177.0), bottom_right=(164.6, 218.0), width=5)

    # s6: 口 bottom 一
    draw_heng(d, (128.9, 218.0), (180.2, 212.1), width_head=5, width_tail=6)

    img.save(path)
    print("wrote", path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_同.png")
    render(out)
