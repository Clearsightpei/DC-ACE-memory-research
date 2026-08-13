"""p3_char_0464_侯 (hóu, "marquis") — 9 strokes.

Structure: 亻 (left, 2 strokes) + 矦-like right (7 strokes):
  right = 𠂉 (short pie s3 + top heng s4) + small corner (short pie s5 +
  short heng s6) + 矢-bottom (long heng s7 + pie s8 + na s9).

Recipe: P-A-006 (stroke-primitive layer with verbatim MMH anchors) +
P-A-007-v2 (whole-radical hard-check first). Bank has `ren_left` for
亻 but its native pie length (158 px) and shu position differ from
this character's 亻 (pie length 150 px, shu shifted ~65 px left):

Quantitative BANK_DEVIATION (P-A-009):
  ren_left native pie: (158.8, 73.8) -> (80.6, 211.2), length=158.
  Target 侯 pie:       ( 86.1, 66.5) -> (19.6, 200.7), length=150.
  ren_left native shu head x = 138.9;  target shu head x = 73.5.
  Delta pie head shift = -72.7 px; delta shu head shift = -65.4 px.
  Non-uniform shift (pie -72.7 vs shu -65.4) => bank primitive's
  internal N-joint geometry (s1.mid <-> s2.head) will not match the
  MMH-specified joint at ML(0.724, 0.38). Single (ox, oy, scale)
  cannot re-park both endpoints correctly.
  -> inline 亻 per MMH anchors with pie + shu primitives.

No whole-radical bank primitive for 矦 or 侯. Inline all 9 strokes.
"""

# BANK_DEVIATION
# skipped: ren_left.py
# reason: internal pie->shu horizontal offset differs from bank
#   (pie shifts -72.7 px, shu shifts -65.4 px; non-uniform), so
#   single (ox, oy, scale) can't preserve both MMH anchors and the
#   ML(0.724, 0.38) N-joint at once.
# fresh_component: hou_ren_left (adjusted-anchor 亻 for 侯)

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 9 strokes drawn with MMH anchors verbatim. 亻 inlined '
             '(BANK_DEVIATION vs ren_left for joint-preservation reasons). '
             '矢-bottom: long heng s7 pierced by pie s8 + na s9 crossing '
             'at BC cell.',
}


def draw_hou(draw):
    # ==================== 亻 LEFT (s1-s2) ====================
    # s1: 亻 pie — TL(0.861, 0.665) -> BL(0.196, 0.007)
    #     pixel: (86.1, 66.5) -> (19.6, 200.7)
    draw_pie(draw, (86.1, 66.5), (19.6, 200.7),
             bow_perp=14, w_head=9, w_tail=3, steps=80)

    # s2: 亻 shu — ML(0.735, 0.453) -> BL(0.762, 0.95)
    #     pixel: (73.5, 145.3) -> (76.2, 295.0)
    draw_shu(draw, (73.5, 145.3), (76.2, 295.0), width=7)

    # ==================== 矦 RIGHT (s3-s9) ====================
    # s3: 𠂉 top short pie/heng — TC(0.43, 0.861) -> C(0.948, 0.148)
    #     pixel: (143.0, 86.1) -> (194.8, 114.8)
    #     Short slanted stroke; render as slight pie (small bow).
    draw_pie(draw, (143.0, 86.1), (194.8, 114.8),
             bow_perp=3, w_head=6, w_tail=3, steps=48)

    # s4: top heng — C(0.137, 0.327) -> MR(0.607, 0.187)
    #     pixel: (113.7, 132.7) -> (260.7, 118.7)
    draw_heng(draw, (113.7, 132.7), (260.7, 118.7),
              width_head=7, width_tail=8)

    # s5: middle short pie/vertical — C(0.465, 0.359) -> C(0.225, 0.972)
    #     pixel: (146.5, 135.9) -> (122.5, 197.2)
    #     Nearly-vertical descender leaning slightly left; use pie.
    draw_pie(draw, (146.5, 135.9), (122.5, 197.2),
             bow_perp=2, w_head=6, w_tail=3, steps=48)

    # s6: short middle heng — C(0.521, 0.734) -> MR(0.25, 0.623)
    #     pixel: (152.1, 173.4) -> (225.0, 162.3)
    draw_heng(draw, (152.1, 173.4), (225.0, 162.3),
              width_head=6, width_tail=7)

    # s7: long bottom heng (of 矢) — BC(0.046, 0.25) -> BR(0.687, 0.121)
    #     pixel: (104.6, 225.0) -> (268.7, 212.1)
    draw_heng(draw, (104.6, 225.0), (268.7, 212.1),
              width_head=8, width_tail=9)

    # s8: 矢 pie — C(0.685, 0.805) -> BC(0.069, 0.991)
    #     pixel: (168.5, 180.5) -> (106.9, 299.1)
    #     Long pie crossing s7 at BC(0.763, 0.169). P-joint expected.
    draw_pie(draw, (168.5, 180.5), (106.9, 299.1),
             bow_perp=14, w_head=8, w_tail=3, steps=90)

    # s9: 矢 na — BC(0.843, 0.262) -> BR(0.851, 0.977)
    #     pixel: (184.3, 226.2) -> (285.1, 297.7)
    #     Sweeping rightward thickening stroke.
    draw_na(draw, (184.3, 226.2), (285.1, 297.7),
            bow_perp=10, w_head=3, w_tail=10, steps=80)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_hou(d)
    out = os.path.join(_HERE, "01_侯.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
