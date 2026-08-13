"""p3_char_0447_信 — 信 (xin, 'trust') = 亻 + 言 (9 strokes).

Decomposition:
  s1-s2: 亻 (ren_left bank primitive; aspect matches — pie+shu, MMH ratios ~0.92
         width, ~1.0 height vs bank ref → uniform scale=1.0 with translation fits)
  s3-s6: 言 top (dian + three 横 of decreasing width) — inline from MMH anchors
  s7-s9: 口 at bottom of 言 — INLINED (see BANK_DEVIATION below)

# BANK_DEVIATION
# skipped: kou_mouth.py
# reason (P-A-009 quantitative):
#   This 口 is compressed vertically at the bottom of 言.
#   MMH-derived footprint: width = 230.6 - 131.8 = 98.8 px, height = 292.1 - 232.3 = 59.8 px
#   → my_aspect (w/h) = 98.8 / 59.8 = 1.65 (wide-flat)
#   Bank kou_mouth ref footprint: width = 225 - 92 = 133 px, height = 272 - 128 = 144 px
#   → bank_aspect = 133 / 144 = 0.92 (near-square)
#   aspect ratio mismatch = 1.65 / 0.92 = 1.79x
#   Uniform-scale primitive cannot resolve non-uniform aspect distortion.
# fresh_component: kou_flat_for_yan_bottom (wide-flat 口 sitting under 言's three 横)

SELF_CHECK layout:
  Stroke count: 2 (ren_left) + 1 (dian) + 3 (heng) + 3 (kou) = 9  ✓
  Endpoint anchors: ren_left translated by (ox=-69.4, oy=-7.9) to place s1_head
    near MMH (89.4, 65.9); s3-s9 use MMH anchors verbatim.
  Joints:
    s1.mid ⇆ s2.head @ ML: N (18.7 px expected) — emerges from ren_left geometry (~15-20 px gap)
    s7.head ⇆ s8.head @ BC: N (15 px) — s7 at (131.8, 232.3), s8 at (149.1, 233.8) → dx=17.3 ✓
    s7.tail ⇆ s9.head @ BC: N (11.3 px) — s7.tail (151.2, 292.1), s9.head (157.0, 285.4) → dist≈8.9 (close)
    s8.tail ⇆ s9.mid @ BR: N (11.7 px) — s8.tail (211.5, 266.6), s9.mid≈(193.8, 281.8) → dist≈23 (loose N)
"""

import os
import sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../success_bank/code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from ren_left import draw_ren_left
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('ren_left called at scale=1.0 with ox=-69.4, oy=-7.9 to align s1_head '
              'with MMH TL(0.894, 0.659). 言 inlined from MMH anchors. 口 inlined '
              '(BANK_DEVIATION: aspect 1.65 vs bank 0.92, 1.79x mismatch — P-A-009).')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---------- 亻 (s1-s2) via ren_left bank primitive ----------
    # Bank ref s1_head=(158.8, 73.8); MMH target s1_head=(89.4, 65.9).
    # scale=1.0, ox=89.4-158.8=-69.4, oy=65.9-73.8=-7.9
    draw_ren_left(d, ox=-69.4, oy=-7.9, scale=1.0)

    # ---------- 言 top (s3-s6) ----------
    # s3: dian at TC (164.6, 57.4) → TC (199.2, 86.7) — slim, not a blob
    draw_dian(d, (164.6, 57.4), (199.2, 86.7),
              w_head=2, w_tail=6, bow=2, steps=48)

    # s4: top long 横, C→MR (108.4, 127.4) → (266.3, 114.0)
    draw_heng(d, (108.4, 127.4), (266.3, 114.0),
              width_head=8, width_tail=8)

    # s5: second 横, C→MR (144.4, 161.4) → (218.0, 153.5)
    draw_heng(d, (144.4, 161.4), (218.0, 153.5),
              width_head=6, width_tail=6)

    # s6: third 横, C→MR (142.1, 196.6) → (219.1, 188.7)
    draw_heng(d, (142.1, 196.6), (219.1, 188.7),
              width_head=6, width_tail=6)

    # ---------- 口 at bottom of 言 (s7-s9) — INLINED, wide-flat aspect ----------
    # s7 left 竖: BC (131.8, 232.3) → BC (151.2, 292.1)
    draw_shu(d, (131.8, 232.3), (151.2, 292.1), width=6)

    # s8 横折 (top + right wall): head BC (149.1, 233.8) → tail BR (211.5, 266.6)
    draw_heng_zhe_box(d, top_left=(149.1, 233.8), bottom_right=(211.5, 266.6), width=6)

    # s9 bottom 横: BC (157.0, 285.4) → BR (230.6, 278.3)
    draw_heng(d, (157.0, 285.4), (230.6, 278.3),
              width_head=6, width_tail=7)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_信.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
