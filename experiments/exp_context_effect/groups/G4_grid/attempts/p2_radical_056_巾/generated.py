"""巾 (jīn) — 3 strokes, radical p2_radical_056.

MMH-derived structural expectations:
  s1: head ML(0.724, 0.356) tail BL(0.788, 0.353)  — short left 竖
  s2: head ML(0.899, 0.389) tail BC(0.805, 0.095)  — 横折 (top bar → right descender)
  s3: head TC(0.336, 0.647) tail BC(0.474, 1.108)  — long center 竖 (extends past bottom)

Joints:
  s1.head ⇆ s2.head @ ML(0.853, 0.406)  N — small natural gap (do NOT weld)
  s2.mid  ⇆ s3.mid  @ C(0.496, 0.333)   P — welded crossing

TR guidance: primitives called with explicit override anchors (TR1).
"""

import os, sys
_CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _CODE_DIR)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from shu import draw_shu
from heng_zhe import draw_heng_zhe

# ---- SELF_CHECK (populated after visual inspection of first render) ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: short left 竖, 横折 top-right bracket, long center 竖. '
             's1/s2 heads separated by ~10-15px (N-gap). s2 horizontal crosses '
             's3 vertical at C cell (P-weld by shared geometry).'
}


def draw_jin(draw):
    # --- Stroke 1: short left 竖 --------------------------------------
    # head ML(0.724, 0.356) -> pixel (72.4, 135.6)
    # tail BL(0.788, 0.353) -> pixel (78.8, 235.3)
    # Nearly straight vertical drop, slight rightward drift.
    draw_shu(draw,
             from_anchor=('ML', 0.724, 0.356),
             to_anchor=('BL', 0.788, 0.353),
             width=9)

    # --- Stroke 2: 横折 (top bar + right descender) -------------------
    # head ML(0.899, 0.389) -> pixel (89.9, 138.9)     start of top horizontal
    # corner @ MR area, roughly TC/MR border at y ≈ 140    (the folding corner)
    # tail BC(0.805, 0.095) -> pixel (180.5, 209.5)    end of vertical drop
    #
    # Corner anchor placement: horizontal spans from x≈90 to x≈181 at
    # y≈140, then descends to (181, 209). So corner is roughly at
    # ('MR', 0.805, 0.389) → pixel (280.5, 138.9) -- NO, that overshoots
    # to right column. Actual right edge is around x=181, which is
    # inside the C cell not MR. But since MMH tail is 'BC' at x≈181,
    # the corner sits above the tail: ('C', 0.805, 0.389) → (180.5, 138.9).
    draw_heng_zhe(draw,
                  head=('ML', 0.899, 0.389),
                  corner=('C', 0.805, 0.389),
                  tail=('BC', 0.805, 0.095),
                  h_width=9, v_width=9, shoulder=11)

    # --- Stroke 3: long center 竖 -------------------------------------
    # head TC(0.336, 0.647) -> pixel (133.6, 64.7)
    # tail BC(0.474, 1.108) -> pixel (147.4, 310.8)  (past canvas bottom)
    # Clip tail y_frac to stay within canvas (1.0 max).
    draw_shu(draw,
             from_anchor=('TC', 0.336, 0.647),
             to_anchor=('BC', 0.474, 1.0),
             width=10)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jin(draw)
    out = os.path.join(os.path.dirname(__file__), '01_巾.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
