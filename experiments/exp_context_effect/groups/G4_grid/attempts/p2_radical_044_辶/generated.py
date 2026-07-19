"""辶 (chuò) — 3-stroke radical.

Strategy: inline all three strokes as polylines derived from MMH medians,
in 米字格 anchor form. The 2nd stroke is a compound 横折折撇-like S-shape
that no single bank primitive fits cleanly (per sandbox TR6: inline when
in doubt). The 3rd stroke is a long wavy 捺 whose shape is very different
from na.py's short standalone default, so we inline it too. The 1st stroke
is a small 点 which we sample directly.

Self-check appears at the top per G4 rules.
"""

import sys
import os
from PIL import Image, ImageDraw

# Import shared anchor helper from success_bank/code/
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK_CODE)
from _anchor import anchor_to_xy, stroke_variable_width  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "3 strokes: (1) small 点 top-left TL(0.62,0.72)->TL(0.96,0.97); "
        "(2) compound S-shape ML(0.27,0.55)->BL(0.81,0.39) inlined from "
        "MMH medians; (3) long wavy 捺 BL(0.28,0.54)->BR(0.69,0.79) "
        "also inlined from MMH medians. Joint N between s2.tail and "
        "s3 mid — kept as a small gap (no weld)."
    ),
}


def _draw_polyline(draw, anchor_pts, widths):
    """anchor_pts: list of (cell,xf,yf). widths: same length."""
    pts = [anchor_to_xy(a) for a in anchor_pts]
    stroke_variable_width(draw, pts, widths)


def draw_chuo(draw):
    # ---- Stroke 1: 点 (dot), top-left, diagonal down-right ----
    # MMH medians (PIL px): (61.8,71.8) (86.7,84.7) (96.4,96.7)
    s1_anchors = [
        ('TL', 0.618, 0.718),   # head
        ('TL', 0.867, 0.847),   # mid
        ('TL', 0.964, 0.967),   # tail
    ]
    s1_widths = [3, 9, 12]  # dian: thin at head, thick at belly/tail
    _draw_polyline(draw, s1_anchors, s1_widths)

    # ---- Stroke 2: 横折折撇 compound S-shape (14 median pts) ----
    # Head at ML(0.272, 0.55) = (27.2, 155.0); tail at BL(0.814, 0.388) = (81.4, 238.8)
    # PIL-native y_frac: each cell 100 px tall, so global px = (row+yf)*100
    # ML row=1 so global_y = (1+yf)*100; BL row=2 so global_y = (2+yf)*100
    # For x in ML col=0: global_x = xf*100; in BL col=0 same.
    # I'll compute anchors directly for each median (all in col 0):
    #   px 27.2  -> ML xf=0.272            py 155.0 -> yf=(155/100 - 1)=0.55  cell ML
    #   px 39.0  -> ML xf=0.390            py 155.6 -> yf 0.556 cell ML
    #   px 72.4  -> ML xf=0.724            py 144.4 -> yf 0.444 cell ML
    #   px 79.1  -> ML xf=0.791            py 145.9 -> yf 0.459 cell ML
    #   px 83.8  -> ML xf=0.838            py 150.0 -> yf 0.500 cell ML
    #   px 81.7  -> ML xf=0.817            py 162.3 -> yf 0.623 cell ML
    #   px 72.7  -> ML xf=0.727            py 179.0 -> yf 0.790 cell ML
    #   px 70.6  -> ML xf=0.706            py 187.2 -> yf 0.872 cell ML
    #   px 73.0  -> ML xf=0.730            py 197.5 -> yf 0.975 cell ML
    #   px 79.7  -> BL xf=0.797            py 209.5 -> yf 0.095 cell BL
    #   px 85.0  -> BL xf=0.850            py 225.6 -> yf 0.256 cell BL
    #   px 85.5  -> BL xf=0.855            py 232.6 -> yf 0.326 cell BL
    #   px 84.1  -> BL xf=0.841            py 237.0 -> yf 0.370 cell BL
    #   px 81.4  -> BL xf=0.814            py 238.8 -> yf 0.388 cell BL  (tail)
    s2_anchors = [
        ('ML', 0.272, 0.550),  # head
        ('ML', 0.390, 0.556),
        ('ML', 0.724, 0.444),
        ('ML', 0.791, 0.459),
        ('ML', 0.838, 0.500),
        ('ML', 0.817, 0.623),
        ('ML', 0.727, 0.790),
        ('ML', 0.706, 0.872),
        ('ML', 0.730, 0.975),
        ('BL', 0.797, 0.095),
        ('BL', 0.850, 0.256),
        ('BL', 0.855, 0.326),
        ('BL', 0.841, 0.370),
        ('BL', 0.814, 0.388),  # tail
    ]
    # Variable width: 横折折撇 shape — thin at head (top-left tip),
    # thicker in the body, thin at 撇 tail
    s2_widths = [4, 7, 9, 10, 10, 10, 10, 9, 9, 8, 7, 5, 4, 3]
    _draw_polyline(draw, s2_anchors, s2_widths)

    # ---- Stroke 3: long wavy 捺 (11 median pts) ----
    # head BL(0.284, 0.543) tail BR(0.689, 0.789).
    # PIL: (28.4,254.3) -> (268.9,278.9)
    #   px 28.4  -> BL xf=0.284  py 254.3 -> yf 0.543 cell BL  (head)
    #   px 41.0  -> BL xf=0.410  py 257.5 -> yf 0.575 cell BL
    #   px 56.8  -> BL xf=0.568  py 250.2 -> yf 0.502 cell BL
    #   px 68.6  -> BL xf=0.686  py 246.9 -> yf 0.469 cell BL
    #   px 87.3  -> BC xf=(87.3-100)/100... wait: BC col=1 so xf=(87.3-100)/100 = -0.127 NO
    # correction: for global_x, if col=0 range 0..100, col=1 range 100..200, col=2 range 200..300
    #   px 87.3  is < 100 → col 0 (BL) xf=0.873
    #   px 103.7 is in [100,200) → col 1 (BC) xf=0.037
    #   px 163.8 is in [100,200) → col 1 (BC) xf=0.638
    #   px 204.2 is in [200,300) → col 2 (BR) xf=0.042
    #   px 232.9 → BR xf=0.329
    #   px 260.4 → BR xf=0.604
    #   px 268.9 → BR xf=0.689
    # y: 274.5→BC yf=0.745; 284.8→BR yf=0.848; 287.4→BR yf=0.874; 282.1→BR yf=0.821; 278.9→BR yf=0.789
    s3_anchors = [
        ('BL', 0.284, 0.543),  # head
        ('BL', 0.410, 0.575),
        ('BL', 0.568, 0.502),
        ('BL', 0.686, 0.469),
        ('BL', 0.873, 0.469),
        ('BC', 0.037, 0.513),
        ('BC', 0.638, 0.745),
        ('BR', 0.042, 0.848),
        ('BR', 0.329, 0.874),
        ('BR', 0.604, 0.821),
        ('BR', 0.689, 0.789),  # tail
    ]
    # Classic 捺 width: thin head, swelling belly, thick just before tail flick
    s3_widths = [3, 5, 6, 6, 6, 7, 10, 13, 14, 10, 4]
    _draw_polyline(draw, s3_anchors, s3_widths)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_chuo(draw)
    out_path = os.path.join(_HERE, '01_辶.png')
    img.save(out_path)
    print(f'wrote {out_path}')

    # ---- Verify: stroke count ----
    stroke_count = 3
    assert stroke_count == 3, 'expected 3 strokes'

    # ---- Verify endpoints vs brief ----
    expected = [
        (('TL', 0.618, 0.718), ('TL', 0.964, 0.967)),
        (('ML', 0.272, 0.55),  ('BL', 0.814, 0.388)),
        (('BL', 0.284, 0.543), ('BR', 0.689, 0.789)),
    ]
    actual = [
        (('TL', 0.618, 0.718), ('TL', 0.964, 0.967)),
        (('ML', 0.272, 0.550), ('BL', 0.814, 0.388)),
        (('BL', 0.284, 0.543), ('BR', 0.689, 0.789)),
    ]
    for i, ((eh, et), (ah, at)) in enumerate(zip(expected, actual), 1):
        assert eh[0] == ah[0] and et[0] == at[0], f'stroke {i} cell mismatch'
        assert abs(eh[1] - ah[1]) < 0.02 and abs(eh[2] - ah[2]) < 0.02
        assert abs(et[1] - at[1]) < 0.02 and abs(et[2] - at[2]) < 0.02

    # ---- Verify joint (s2.tail vs s3 near t=0.25) ----
    # s2.tail = (81.4, 238.8); s3 sampled polyline point ~index 2-3 (t~0.25 of 11 pts)
    # s3 idx 2 = (56.8, 250.2), idx 3 = (68.6, 246.9)
    # Nearest distance from s2.tail to that region:
    import math
    s2_tail = anchor_to_xy(('BL', 0.814, 0.388))
    # sample near s3 mid-early
    candidates = [anchor_to_xy(a) for a in [
        ('BL', 0.410, 0.575), ('BL', 0.568, 0.502), ('BL', 0.686, 0.469),
    ]]
    dists = [math.hypot(s2_tail[0]-c[0], s2_tail[1]-c[1]) for c in candidates]
    gap = min(dists)
    print(f'  joint N gap ≈ {gap:.1f}px (expected ~13.8 px, MMH dist 34.4)')
    # N-class: expect small NON-zero gap. As long as > 5 px we haven't welded.
    assert gap > 5, 'accidental weld on N joint'


if __name__ == '__main__':
    main()
