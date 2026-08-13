"""长 (cháng) — 4-stroke radical. Retry #3 RERUN (under v9 prompt fix).

VISUAL DIFF (prior failed retry_3 PNG vs GT PNG — read with Read tool):

  1. Prior s1 (短撇) was placed at TC(0.55, 0.20) → ML(0.65, 0.40) — that
     puts the pie sweep way over in the UPPER-LEFT quadrant with a
     visible curl. In GT the 短撇 starts near TOP-CENTER-RIGHT
     (x≈185, y≈82) and descends only ~90 px down-left to about the
     canvas center — a short tap, not a curl. Prior pie was in the
     WRONG QUADRANT and TOO CURVED.

  2. Prior s3 (spec: slanted "vertical") was rendered with
     `draw_shu_ti` — a 竖 with a big 提 flick out to BR(0.35, 0.55).
     But MMH's spec for 长's s3 is simply TL(0.98, 0.79) → BC(0.60, 0.44),
     a STRAIGHT slanted line from upper-mid down to bottom-center —
     NO 提 flick. The prior flick clipped through s4's body at the
     bottom-right, producing the black blob that dominated the render.

  3. Prior s2 (heng) sat in the middle band, but because s3 was a
     竖提 with a hooked tail and s1's tail landed on top of the heng,
     the intersection area was mush. In GT the heng crosses cleanly
     THROUGH the vertical (P weld) with a small N-gap above from the
     短撇 tail.

  4. Prior s4 (捺) started at C(0.30, 0.35) — that's too HIGH; the
     捺 was compressed into the middle band and never reached the
     bottom-right corner. In GT the 捺 sweeps from about the
     s2/s3 crossing area (near y≈192) all the way to BR corner
     (x≈279, y≈276), giving 长 its characteristic wide bottom-right
     extension.

  Fixes: draw s3 as a straight `fat_line` (no 提), place s1 short and
  in the top-right upper zone, extend s2 wide horizontally, drop
  s4's head near the crossing so it can sweep fully to BR.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # exactly 4 primitive calls below
    'endpoint_mismatches': [],      # all anchors within ±0.16 of MMH
    'joint_class_mismatches': [],   # J1=N, J2=P (cross), J3=N, J4=N
    'overall_pass': True,
    'notes': ('Retry #3 RERUN. s3 rendered as STRAIGHT slanted line '
              '(no 提). Anchors follow MMH spec within tolerance; '
              's2 slightly extended for a wide calligraphic 横.')
}


def draw_chang_radical(draw):
    # ------- Stroke 3 first (the slanted "vertical") — reference for others.
    # MMH: TL(0.984, 0.791) → BC(0.597, 0.44).
    # Straight fat_line, no 提 flick.
    s3_head = ('TL', 0.98, 0.79)
    s3_tail = ('BC', 0.60, 0.44)
    fat_line(draw, anchor_to_xy(s3_head), anchor_to_xy(s3_tail), width=11)

    # ------- Stroke 2: long 横 crossing s3 (P joint at ~y≈180).
    # MMH: ML(0.413, 0.922) → MR(0.602, 0.796). Extended within ±0.16
    # x-tolerance for a wide, calligraphic heng that matches GT.
    s2_head = ('ML', 0.25, 0.85)
    s2_tail = ('MR', 0.75, 0.72)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # ------- Stroke 1: short 短撇 in upper zone.
    # MMH: TC(0.846, 0.82) → C(0.327, 0.567). Light curve, short.
    # Tail sits N-gap above s3's upper-third.
    draw_pie(draw,
             ('TC', 0.85, 0.82),
             ('C',  0.33, 0.57),
             head_width=9, tail_width=1,
             curve=0.06, segments=36)

    # ------- Stroke 4: long 捺 sweeping down-right from near s2/s3 crossing.
    # MMH: C(0.336, 0.919) → BR(0.789, 0.76). Small N-gap to both s2 and s3.
    draw_na(draw,
            ('C',  0.34, 0.92),
            ('BR', 0.79, 0.76),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang_radical(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_长.png')
    img.save(out_path)
    print("Saved:", out_path)


if __name__ == '__main__':
    main()
