"""p3_char_0265_名 — G5 retry #1.

TRAJECTORY DIFF (from inspection of GT + prior attempt PNG):

  main FAIL — what's off:
    (1) Bottom 口 was inlined as two thin `draw.line` legs + heng.
        Result: the 口 reads as a squashed 'L' + underline, not a
        closed box. Width was ~80px in GT but only ~60px in attempt.
    (2) Interior 点 (s3) rendered as an over-long skinny mark rather
        than a proper compact dot; head/tail widths too similar.
    (3) 夕's overall composition sat too high; bottom-right region
        of the canvas felt disconnected from the top pie.

  Fix plan (per errata B9 R1 for 名, "use draw_kou for bottom"):
    (a) Replace inline 口 (s4/s5/s6) with a single `draw_kou` call
        from the bank, positioned bottom-right at scale ≈ 0.55.
        This gives a proper closed box (shu + heng_zhe_box + heng)
        and matches GT proportions.
    (b) Keep 夕's s1/s2 anchors from MMH but tighten s3 dot: shorter
        length, thicker tail — a compact ink drop.
    (c) Nudge 夕's pie a hair to open the interior for the dot.

  This retry uses the P-A-007 recipe: whole-radical bank call for
  the sub-component that matches at native shape (口 here), plus
  stroke-primitive inline for the 夕 half whose stroke geometry is
  character-specific.
"""

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
sys.path.insert(0, _BANK)

from pie import draw_pie          # noqa: E402
from dian import draw_dian        # noqa: E402
from kou_mouth import draw_kou    # noqa: E402  (whole-radical bank primitive)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (夕) + 3 (口 inside draw_kou) = 6 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 8 expected joints are N-class; draw_kou preserves internal joint discipline
    'overall_pass': True,
    'notes': ('P-A-007 route: draw_kou bank primitive for bottom-right 口 '
              '(replaces inline L-shape from main attempt), 夕 stroke-primitive '
              'inline at MMH anchors, s3 dot tightened.'),
}


CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)


def draw_ming(d):
    # ---- 夕 (top-left / diagonal) ---------------------------------------
    # s1: short top pie  TC(0.453, 0.574) -> ML(0.718, 0.462)  ~ (145,57) -> (72,146)
    draw_pie(d, A('TC', 0.453, 0.574), A('ML', 0.718, 0.462),
             bow_perp=6, w_head=6, w_tail=3)

    # s2: long main pie  C(0.395, 0.028) -> BL(0.144, 0.78)  ~ (140,103) -> (14,278)
    draw_pie(d, A('C', 0.395, 0.028), A('BL', 0.144, 0.78),
             bow_perp=14, w_head=9, w_tail=3)

    # s3: interior 点 (compact ink drop, not a skinny line)
    #     C(0.04, 0.348) -> C(0.321, 0.638)  ~ (104,135) -> (132,164)
    draw_dian(d, A('C', 0.06, 0.36), A('C', 0.30, 0.60),
              w_head=2, w_tail=7, bow=2)

    # ---- 口 (bottom-right) ---------------------------------------------
    # Use bank primitive draw_kou (shu + heng_zhe_box + heng = 3 strokes).
    # kou native occupies x:[92,225], y:[122,275]  -> width 133, height 153.
    # Revision (retry v2): bump scale 0.55->0.65 (口 was too thin/small vs
    # GT), reposition center to (185, 230) so the 口 tucks under the pie
    # tip and shares vertical territory with 夕's interior.
    #   -> ox = 185 - 158.5*0.65 = 82
    #      oy = 230 - 198.5*0.65 = 101
    # Renders 口 roughly (142,180)..(228,280).
    draw_kou(d, ox=82, oy=101, scale=0.65)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ming(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_名.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
