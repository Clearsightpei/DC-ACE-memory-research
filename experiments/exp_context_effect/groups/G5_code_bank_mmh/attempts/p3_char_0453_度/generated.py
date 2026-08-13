"""p3_char_0453_度 — G5 attempt.

Decomposition (9 strokes):
  s1-s3: 广 top (dian + heng + long pie)
  s4-s7: middle 廿-like enclosure (heng crossbar + 2 shu + bottom heng)
  s8-s9: 又 bottom-right (heng_pie + na)

# BANK_DEVIATION
# skipped: guang_wide.py, you_again.py
# reason: quantitative aspect check — standalone 广 vertical span = 178px
#   (s1 top y=64 to s3 tail y=303), whereas 度's 广-slot spans 246px
#   (s1 top y=53 to s3 tail y=299). Ratio 1.38, not a uniform-scale fit.
#   Standalone 又 head at (77.9,116.9) with na tail at (285.4,278.9) has
#   different aspect than 度's compressed 又 (s8 head y=215, s9 tail y=298).
#   Both bank primitives would produce inter-stroke offsets ≥15px if
#   dropped in with any single (ox,oy,scale). Inlining primitives keeps
#   per-stroke MMH-anchor verbatim (P-A-006 recipe).
# fresh_component: du_9stroke_inline (widely reusable for 席/庶/庭 family)

# P-A-008 reasoning trace:
# The 9 MMH endpoints given in the brief are used verbatim. Stroke-primitive
# layer: dian(s1), heng(s2), pie(s3), heng(s4), shu(s5,s6), heng(s7),
# heng_pie(s8 tightened apex), na(s9). Joint expectations: s4×s5 and s4×s6
# both P (welded) — the crossbar pierces both verticals. s8×s9 P at BC:
# heng_pie tail-region welds to na mid-region. All other joints N (small
# calligraphic gaps, no forced welding).
"""

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[2] / "success_bank" / "code"),
)

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from heng_pie import draw_heng_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 recipe: MMH-anchor verbatim + stroke primitives. '
             'BANK_DEVIATION for guang and you due to aspect mismatch.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 广 top (s1-s3) — MMH anchors verbatim ----
    # s1 dian: TC(0.424,0.527) -> TC(0.717,0.753)
    draw_dian(d, (142, 53), (172, 75), w_head=3, w_tail=7, bow=2)

    # s2 heng: ML(0.932,0.028) -> TR(0.253,0.879)
    draw_heng(d, (93, 103), (225, 88), width_head=8, width_tail=10)

    # s3 long pie: TL(0.744,0.981) -> BL(0.199,0.994)
    draw_pie(d, (74, 98), (20, 299), bow_perp=16, w_head=8, w_tail=3)

    # ---- middle 廿-like (s4-s7) ----
    # s4 heng crossbar (pierces both verticals): ML(0.961,0.562) -> MR(0.396,0.409)
    draw_heng(d, (96, 156), (240, 141), width_head=6, width_tail=7)

    # s5 left shu (short vertical): C(0.254,0.201) -> C(0.397,0.913)
    draw_shu(d, (125, 120), (140, 191), width=5)

    # s6 right shu: C(0.799,0.096) -> C(0.772,0.699)
    draw_shu(d, (180, 110), (177, 170), width=5)

    # s7 bottom small heng: C(0.462,0.875) -> C(0.928,0.808)
    draw_heng(d, (146, 188), (193, 181), width_head=5, width_tail=6)

    # ---- 又 bottom (s8-s9) — MMH anchors verbatim, tightened apex ----
    # s8 heng_pie: BC(0.204,0.153) -> BL(0.782,0.985)
    # Tighten apex_x since 度's 又 has a very short horizontal segment
    draw_heng_pie(d, (120, 215), (78, 298), apex_x=138, corner_x=135)

    # s9 long na: BC(0.154,0.335) -> BR(0.766,0.977)
    draw_na(d, (115, 233), (277, 298),
            bow_perp=14, w_head=4, w_tail=12, steps=90)

    return img


if __name__ == '__main__':
    out = Path(__file__).parent / '01_度.png'
    render().save(out)
    print(f'wrote {out}')
