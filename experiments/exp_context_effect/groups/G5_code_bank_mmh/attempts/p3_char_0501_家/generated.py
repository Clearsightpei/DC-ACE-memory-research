"""p3_char_0501_家 — G5 attempt.

家 = 宀 (roof, 3 strokes) + 豕 (pig, 7 strokes) = 10 strokes total.

Reasoning trace (P-A-008):
- Bank has draw_mian_roof (3 strokes) — very high-reuse top radical.
  MMH s1-s3 match mian_roof layout: top dian (TC), left dian (TL/ML),
  heng-zhe (ML→MR). Use it with uniform shift/scale (P-A-007-v2:
  uniform shift IS adjustable).
- Bank does NOT have 豕. 豕 = short heng + long-pie + heng + 3 short pies
  + na. Inline the 7 strokes using bank pie/na/heng primitives.

BANK_DEVIATION analysis:
- mian_roof: used as-is with ox/oy uniform shift + scale. No deviation.
- 豕: no bank primitive; inline using pie + na + heng components.
  Not a deviation — bank has no whole-radical for 豕.
"""

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from mian_roof import draw_mian_roof
from pie import draw_pie
from na import draw_na
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 3 (mian_roof) + 7 (inline 豕) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Using mian_roof for 宀 (s1-s3), inline 豕 for s4-s10.',
}


def render(path: str) -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------------------------------------------------------------
    # 宀 (roof) — s1, s2, s3 via bank mian_roof
    # Shifted up (oy=-38) so roof sits at top ~y=50-120.
    # Slight ox=15 to center-right (GT roof spans ~x=60-260).
    # ------------------------------------------------------------
    draw_mian_roof(d, ox=15, oy=-38, scale=1.05)

    # ------------------------------------------------------------
    # 豕 (7 strokes) below the roof
    # From MMH anchors:
    #   s4: short heng — head (198,139)→ tail (188,130)  [tiny — treat
    #       as the top-center short heng of 豕 spanning ~ (110,135)→(200,135)]
    #   s5: pie — head C(138,153) → tail ML(66,197)  (long left pie)
    #   s6: pie — head C(121,173) → tail BC(113,287) (vertical-ish pie)
    #   s7: pie — head C(126,180) → tail BL(70,231)  (mid pie left)
    #   s8: pie — head BC(149,202) → tail BL(55,280) (long lower pie)
    #   s9: pie — head C(195,154) → tail C(165,199)  (right pie short)
    #   s10: na — head BC(163,201) → tail BR(286,267) (final na)
    # ------------------------------------------------------------

    # s4: wide heng of 豕 (across middle, just below roof)
    #  GT shows the heng spans roughly x=55 to x=245 at y~145
    draw_heng(d, head=(60, 148), tail=(245, 143),
              width_head=6, width_tail=7)

    # s5: long left pie from mid-heng going down-left (main left of 豕)
    draw_pie(d, head=(150, 145), tail=(50, 245),
             bow_perp=18, w_head=8, w_tail=3)

    # s6: small pie hook top of 豕 body (short mark on upper-mid)
    draw_pie(d, head=(155, 160), tail=(135, 195),
             bow_perp=4, w_head=5, w_tail=3)

    # s7: mid pie (second slanted stroke)
    draw_pie(d, head=(160, 185), tail=(105, 235),
             bow_perp=8, w_head=6, w_tail=3)

    # s8: long lower pie down-left
    draw_pie(d, head=(165, 200), tail=(70, 285),
             bow_perp=12, w_head=7, w_tail=3)

    # s9: short right pie
    draw_pie(d, head=(175, 175), tail=(160, 210),
             bow_perp=4, w_head=5, w_tail=3)

    # s10: final na (down-right, thick tail)
    draw_na(d, head=(165, 200), tail=(280, 275),
            bow_perp=16, w_head=4, w_tail=12)

    img.save(path)


if __name__ == "__main__":
    out = Path(__file__).parent / "01_家.png"
    render(str(out))
    print(f"wrote {out}")
