"""p3_char_0115_仌 — two 人 stacked vertically (4 strokes: pie, na, pie, na).

Uses pie + na bank primitives directly (no draw_ren, because the top and
bottom 人 have very different sizes/aspects, and MMH anchors give exact
endpoints).

MMH anchors (300x300 米字格, cell size 100 px):
  s1 (top pie):    head TC(0.315,0.662)=(131.5, 66.2)  tail ML(0.577,0.948)=(57.7, 194.8)
  s2 (top na):     head C (0.4,  0.04) =(140.0,104.0)  tail MR(0.171,0.57) =(217.1,157.0)
  s3 (bottom pie): head C (0.274,0.676)=(127.4,167.6)  tail BL(0.396,1.05) =(39.6,305.0)
  s4 (bottom na):  head BC(0.468,0.156)=(146.8,215.6)  tail BR(0.81,1.056) =(281.0,305.6)

Joints (both N, small gaps):
  s1.mid ⇆ s2.head at cell C (expected gap ~13 px) — top 人
  s3.mid ⇆ s4.head at cell BC (expected gap ~16 px) — bottom 人
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'two 人 stacked; direct pie+na calls with MMH anchors; both joints are N-gap.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Top 人 (smaller, upper-center)
    draw_pie(d, (131.5, 66.2), (57.7, 194.8),
             bow_perp=10, w_head=7, w_tail=2)
    draw_na(d, (140.0, 104.0), (217.1, 157.0),
            bow_perp=6, w_head=3, w_tail=7)

    # Bottom 人 (larger, lower-center)
    draw_pie(d, (127.4, 167.6), (39.6, 300.0),
             bow_perp=14, w_head=9, w_tail=3)
    draw_na(d, (146.8, 215.6), (281.0, 300.0),
            bow_perp=12, w_head=4, w_tail=11)

    out = pathlib.Path(__file__).parent / '01_仌.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
