"""p3_char_0445_点 — G5 attempt.

Structure (MMH → 9 strokes):
  s1-s2 : 卜 (top of 占)          — vertical + horizontal-ish dian
  s3-s5 : 口 (bottom of 占)       — left shu + heng_zhe_box + bottom heng
  s6-s9 : 灬 (fire-bottom)        — leftward pie + 2 short dians + long right dian

# BANK_DEVIATION
# skipped: bu_divine.py, kou_mouth.py, si_fire_bot.py
# reason: All three native canvases span nearly the full 300-height (卜 y=82→285,
#   口 y=122→275, 灬 y=170→220). In 点 the 占 top-half occupies only y=64→222
#   (~52% of native height, aspect skew) and 灬 shifts down to y=231→290
#   (translation +65 y, near-uniform scale). Composing three whole-radical
#   primitives with distinct affine transforms would compound placement error
#   across 9 strokes. Per P-A-006 + P-A-007-v2 hard-check: use MMH endpoint
#   anchors verbatim with the stroke-primitive layer.
# quantitative (P-A-009):
#   - bu_divine native aspect (卜 body) H/W = 203/48 = 4.23; target 87/8 = 10.9 (2.6× skinnier)
#   - kou_mouth native H/W = 153/133 = 1.15; target 65/94 = 0.69 (0.6× wider-flat)
#   - si_fire_bot native span 202w × 50h; target 201w × 59h (aspect match, +65y shift only)
#     → si_fire_bot would be usable as a whole; inlined here for consistent style
#       across all 9 strokes and to preserve exact MMH endpoint fidelity.
# fresh_component: dian_top_dot_for_bu (卜's near-horizontal dot at top),
#   zhan_compact_kou (口 compressed y-aspect for 占-bottom position),
#   si_fire_bot_shifted (灬 with +65y translation — could motivate a variant later).
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from pie import draw_pie
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 5 expected joints are class N (natural gap)
    'overall_pass': True,
    'notes': 'MMH-verbatim inline; all 5 joints are N-class (natural gaps preserved by using exact MMH endpoint pixels without welding).',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # 占 top-half
    # ------------------------------------------------------------------
    # s1  卜 vertical (head TC 138,63.6 → tail C 145.6,150.9)  — slight R drift
    draw_shu(d, head=(138, 64), tail=(146, 151), width=7)

    # s2  卜 dian (head C 159.7,116.6 → tail MR 215,108.1) — near-horizontal, up-right
    draw_dian(d, head=(160, 117), tail=(215, 108),
              w_head=3, w_tail=7, bow=3, steps=40)

    # s3  口 left-shu (head ML 95.2,157.3 → tail BC 116,221.5)
    draw_shu(d, head=(95, 157), tail=(116, 222), width=6)

    # s4  口 heng_zhe_box (head C 113.4,158.8 → tail C 189.3,193.1)
    draw_heng_zhe_box(d,
                      top_left=(113, 159),
                      bottom_right=(189, 193),
                      width=6)

    # s5  口 bottom heng (head BC 122.5,215 → tail BR 208,206.5)
    draw_heng(d, head=(123, 215), tail=(208, 207),
              width_head=6, width_tail=7)

    # ------------------------------------------------------------------
    # 灬 fire-bottom (4 dots, natural gaps between all)
    # ------------------------------------------------------------------
    # s6  leftmost pie (head BL 80.3,237.3 → tail BL 54.2,290.3)
    draw_pie(d, head=(80, 237), tail=(54, 290),
             bow_perp=4, w_head=7, w_tail=3, steps=50)

    # s7  short dian, right-lean (head BC 114.3,243.2 → tail BC 131.2,277.1)
    draw_dian(d, head=(114, 243), tail=(131, 277),
              w_head=3, w_tail=7, bow=2, steps=40)

    # s8  short dian, right-lean (head BC 163.2,237 → tail BC 182.5,273.6)
    draw_dian(d, head=(163, 237), tail=(183, 274),
              w_head=3, w_tail=7, bow=2, steps=40)

    # s9  long rightward dian, na-like (head BR 209.5,231.4 → tail BR 255.2,287.4)
    draw_dian(d, head=(210, 231), tail=(255, 287),
              w_head=3, w_tail=9, bow=3, steps=50)

    return img


if __name__ == '__main__':
    out = Path(__file__).parent / '01_点.png'
    img = draw()
    img.save(out)
    print(f'wrote {out}')
