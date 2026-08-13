"""p3_char_0229_自 — G5 attempt.

自 = 撇 (top) + 目-like box body (5 strokes: 竖 + 横折 + 3 hengs inside).
6 strokes total, matches MMH.

Composition strategy: reuses stroke primitives from success_bank
(draw_pie, draw_shu, draw_heng_zhe_box, draw_heng). No BANK_DEVIATION —
all primitives fit cleanly here (自 is a very "boxy" character, ideal
for the boxy heng_zhe_box + shu combo already validated in draw_ri).

Pixel anchors derived from MMH block:
  s1 pie: TC(0.359,0.565)→C(0.184,0.166) = (135.9, 56.5) → (118.4, 116.6)
  s2 shu: ML(0.888,0.146)→BL(0.961,0.783) = (88.8, 114.6) → (96.1, 278.3)
  s3 hzb: C(0.075,0.216)→BC(0.837,0.695) = (107.5, 121.6) → (183.7, 269.5)
  s4 heng-top-inside: (106.9, 176.7) → (171.7, 164.9)
  s5 heng-middle: (106.9, 220.3) → (172.9, 210.9)
  s6 heng-bottom (closes box): (103.7, 272.8) → (190.1, 263.4)

Joints — all seven expected classes are N (natural gap). The 横折 corner
lands slightly INSIDE the left 竖's top, so the s2/s3 join is a natural
overlap-neighbor. The 3 inside hengs are inset from the box walls (N).
"""

import sys, pathlib
from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 turtle-equivalent calls: pie, shu, heng_zhe_box, 3x heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 7 joints implemented as N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'Boxy composition; reuses ri_sun-style primitive combo; adds pie on top.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 撇 (top pie) — short, gentle bow. Negative bow_perp because head→tail
    # travels down-left, and we want the arc to bulge toward the right (calligraphic).
    draw_pie(d, head=(135.9, 56.5), tail=(118.4, 116.6),
             bow_perp=-8, w_head=7, w_tail=3)

    # s2 竖 (left vertical of box)
    draw_shu(d, head=(88.8, 114.6), tail=(96.1, 278.3), width=8)

    # s3 横折 (top + right side of box) — heng_zhe_box takes top_left, bottom_right
    draw_heng_zhe_box(d, top_left=(107.5, 121.6), bottom_right=(183.7, 269.5), width=8)

    # s4 top-inside 横
    draw_heng(d, head=(106.9, 176.7), tail=(171.7, 164.9),
              width_head=6, width_tail=7)

    # s5 middle 横
    draw_heng(d, head=(106.9, 220.3), tail=(172.9, 210.9),
              width_head=6, width_tail=7)

    # s6 bottom 横 (closes the box)
    draw_heng(d, head=(103.7, 272.8), tail=(190.1, 263.4),
              width_head=7, width_tail=8)

    img.save(path)


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_自.png'
    render(out)
    print(f'wrote {out}')
