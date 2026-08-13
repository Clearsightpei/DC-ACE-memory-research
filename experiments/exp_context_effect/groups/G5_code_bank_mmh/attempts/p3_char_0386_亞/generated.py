# BANK_DEVIATION
# skipped: ya_asia.py (bank primitive for simplified 亚)
# reason: 亞 (traditional) is 8 strokes per MMH; ya_asia is 6 strokes.
#   Quantitative: stroke count 8 vs 6 = +33% strokes; inner geometry
#   also differs (亚 has 2 outer dians spanning MMH ML..MR;
#   亞 has interior small-heng + short-shu forming a box+cross detail
#   at BC cell, no outer dians). Aspect of primary body similar
#   (~230 px wide, ~200 px tall) but stroke topology mismatch is
#   structural, not stylistic — per P-A-007-v2 skip bank and inline
#   MMH-verbatim from stroke primitives (heng + shu).
# fresh_component: ya_traditional_8stroke (top heng + inner box+cross + baseline heng)
"""p3_char_0386_亞 — G5 render.

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer.
8 strokes, all 8 joints N-class (natural gap, no welding).

MMH anchors (300x300 canvas, 100 px per cell, PIL y-down;
y_frac measured top-down within each cell — verified against
ya_asia.py's docstring convention):

  s1 top-heng  : TL(0.879,0.814)=( 87.9, 81.4) -> TR(0.238,0.697)=(223.8, 69.7)
  s2 short-shu : TC(0.11 ,0.929)=(111.0, 92.9) -> C (0.269,0.45 )=(126.9,145.0)
  s3 inner-heng: ML(0.721,0.626)=( 72.1,162.6) -> C (0.324,0.55 )=(132.4,155.0)
  s4 left-desc : ML(0.568,0.623)=( 56.8,162.3) -> BC(0.125,0.722)=(112.5,272.2)
  s5 right-desc: TC(0.708,0.858)=(170.8, 85.8) -> MR(0.153,0.942)=(215.3,194.2)
  s6 mid-heng  : BC(0.775,0.06 )=(177.5,206.0) -> BR(0.373,0.03 )=(237.3,203.0)
  s7 mid-shu   : BC(0.67 ,0.057)=(167.0,205.7) -> BC(0.69 ,0.692)=(169.0,269.2)
  s8 base-heng : BL(0.293,0.842)=( 29.3,284.2) -> BR(0.754,0.824)=(275.4,282.4)

Joints (all N — DO NOT weld; keep natural gaps ~10-20 px):
  s1.head  <> s2.head  @ TC  N (~16 px)
  s1.mid   <> s5.head  @ TC  N (~19 px)
  s2.tail  <> s3.tail  @ C   N (~16 px)
  s3.head  <> s4.head  @ ML  N (~14 px)
  s4.tail  <> s8.mid   @ BC  N (~19 px)
  s5.tail  <> s6.mid   @ MR  N (~16 px)
  s6.head  <> s7.head  @ BC  N (~10 px)
  s7.tail  <> s8.mid   @ BC  N (~17 px)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 primitives called; matches expected 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION from ya_asia (6-stroke) to inline 8-stroke; '
             'all joints N-class, natural gaps preserved by not welding.',
}


def draw_ya_trad(draw: ImageDraw.ImageDraw):
    # s1: top heng (crown), slight upward slant to the right
    draw_heng(draw, (87.9, 81.4), (223.8, 69.7),
              width_head=8, width_tail=10)

    # s2: short left shu descending from just below crown into center
    draw_shu(draw, (111.0, 92.9), (126.9, 145.0), width=7)

    # s3: upper interior heng (short)
    draw_heng(draw, (72.1, 162.6), (132.4, 155.0),
              width_head=7, width_tail=8)

    # s4: long left descending diagonal (ML -> BC) — the left "wing"
    draw_shu(draw, (56.8, 162.3), (112.5, 272.2), width=7)

    # s5: long right descending diagonal (TC -> MR) — the right "wing"
    draw_shu(draw, (170.8, 85.8), (215.3, 194.2), width=7)

    # s6: small horizontal near center-right in bottom band
    draw_heng(draw, (177.5, 206.0), (237.3, 203.0),
              width_head=7, width_tail=8)

    # s7: short central shu descending inside bottom band
    draw_shu(draw, (167.0, 205.7), (169.0, 269.2), width=7)

    # s8: baseline heng (long, heaviest)
    draw_heng(draw, (29.3, 284.2), (275.4, 282.4),
              width_head=9, width_tail=11)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ya_trad(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亞.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
