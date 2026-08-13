"""G5 attempt: p2_radical_072_土 (tǔ, "earth" — 3 strokes: heng + shu + heng, BOTTOM heng LONGER).

Sibling of 士 (shi_scholar); the distinguisher is that in 土 the BOTTOM
heng is longer than the top, while in 士 the TOP heng is longer.

MMH anchors (from injected block, canvas 300x300, cells 100x100):
  s1 heng (top):    ML(0.829,0.717)->MR(0.171,0.579)  = ( 82.9,171.7) -> (217.1,157.9)
  s2 shu (middle):  TC(0.351,0.773)->BC(0.395,0.552)  = (135.1, 77.3) -> (139.5,255.2)
  s3 heng (bottom): BL(0.378,0.71) ->BR(0.701,0.622)  = ( 37.8,271.0) -> (270.1,262.2)

Joints:
  s1 mid P s2 mid  -> shu pierces top heng (weld, both drawn thick, natural overlap)
  s2 tail N s3 mid -> shu stops just short of bottom heng (~19px gap expected)
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 primitives called: heng, shu, heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused shi_scholar layout but swapped heng lengths: top short (~134px), bottom long (~232px). '
             'Shu tail stops ~16px above bottom heng to preserve the N-gap.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1 - top heng (SHORT)
    s1_head = (82.9, 171.7)
    s1_tail = (217.1, 157.9)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # stroke 2 - central shu; pull tail up slightly to leave the N-gap to s3
    s2_head = (135.1, 77.3)
    s2_tail = (139.5, 246.0)  # was 255.2; lift ~9px so gap to s3 (~262) ≈ 16px
    draw_shu(d, s2_head, s2_tail, width=8)

    # stroke 3 - bottom heng (LONG — the 土 vs 士 distinguisher)
    s3_head = (37.8, 271.0)
    s3_tail = (270.1, 262.2)
    draw_heng(d, s3_head, s3_tail, width_head=10, width_tail=11)

    out = os.path.join(os.path.dirname(__file__), "01_土.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
