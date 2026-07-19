"""飞 (fēi, 3画) — Phase-2 radical, G4 attempt.

Anchor plan (per MMH-derived brief):
  stroke 1 (long 横折弯钩-like body): head @ ('ML', 0.369, 0.318),
     tail @ ('BR', 0.651, 0.484). It sweeps from the mid-left across
     the top and curves down through cell C toward the lower-right.
  stroke 2 (short 撇 inside): head @ ('MR', 0.168, 0.26),
     tail @ ('C', 0.849, 0.77). A short diagonal descending from
     upper-right area down into cell C.
  stroke 3 (small hook/点 near cell C): head @ ('C', 0.767, 0.863),
     tail @ ('BR', 0.367, 0.291). Short up-right sweep.

Joints (all N — small natural gaps at cell C):
  s1.mid ⇆ s2.tail @ C — N (gap ~26 px)
  s1.mid ⇆ s3.head @ C — N (gap ~15 px)
  s2.tail ⇆ s3.head @ C — N (gap ~17 px)

Bank primitive fit: none cleanly fits — s1 is a compound curve that no
existing primitive spans in this shape. Inlining per TR6.
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line)

SELF_CHECK = {
    'visual_ok': True,  # (1) both have long leftward horizontal at top,
                        # (2) both have descending curved hook on right
                        # reaching bottom of canvas, (3) both have a
                        # short inner tick near cell C.
    'stroke_count_ok': True,  # 3 strokes drawn, matches MMH.
    'endpoint_mismatches': [
        {'stroke': 1, 'expected_tail': ('BR', 0.651, 0.484),
         'actual_tail': ('BR', 0.85, 0.90),
         'delta': 'per TR9 — standalone radical expanded from MMH'},
        {'stroke': 3, 'expected_tail': ('BR', 0.367, 0.291),
         'actual_tail': ('C', 0.95, 0.55),
         'delta': 'shortened tick — GT shows small mark, not long stroke'},
    ],
    'joint_class_mismatches': [],  # all 3 joints N-class, small gaps
                                   # near cell C — verified by anchor
                                   # proximity but not welded.
    'overall_pass': True,
    'notes': 'Revised once: extended stroke 1 tail to reach bottom-right '
             '(GT shows deep descent). Stroke 3 shortened to a small tick '
             'per GT visual.',
}


def draw_fei(draw):
    # ---- Stroke 1: long compound sweep (横折弯钩-like body of 飞) ----
    # Extended toward bottom of canvas to match GT descent depth.
    s1_head = anchor_to_xy(('ML', 0.369, 0.318))
    # Extend tail: MMH gives BR(0.651,0.484) but standalone radical
    # (TR9) — expand toward BR corner to fill more of the frame.
    s1_tail = anchor_to_xy(('BR', 0.85, 0.90))
    # Control 1: at top-right — creates the flat top then bend down.
    ctrl1 = anchor_to_xy(('TR', 0.55, 0.85))
    # Mid: through cell C going down (per MMH s1.mid @ ('C', 0.755, 0.799))
    mid = anchor_to_xy(('C', 0.755, 0.799))
    # Control 2: bows the descending body leftward, then curls back right.
    ctrl2 = anchor_to_xy(('MR', 0.05, 0.95))

    pts_a = quad_bezier(s1_head, ctrl1, mid, n=48)
    pts_b = quad_bezier(mid, ctrl2, s1_tail, n=48)
    pts1 = pts_a + pts_b[1:]
    n1 = len(pts1) - 1
    widths1 = []
    for i in range(len(pts1)):
        t = i / n1
        if t < 0.35:
            w = 10 - (10 - 7) * (t / 0.35)
        elif t < 0.75:
            w = 7 - (7 - 5) * ((t - 0.35) / 0.40)
        else:
            w = 5 + (8 - 5) * ((t - 0.75) / 0.25)
        widths1.append(w)
    stroke_variable_width(draw, pts1, widths1)

    # ---- Stroke 2: short 撇-like inner sweep ----
    # Keep close to MMH: from upper-right area diagonally down into cell C.
    s2_head = anchor_to_xy(('MR', 0.168, 0.26))
    s2_tail = anchor_to_xy(('C', 0.849, 0.77))
    dx = s2_tail[0] - s2_head[0]
    dy = s2_tail[1] - s2_head[1]
    length2 = (dx * dx + dy * dy) ** 0.5
    perp = (-dy / length2, dx / length2)
    bow = 0.06 * length2
    midp = ((s2_head[0] + s2_tail[0]) / 2, (s2_head[1] + s2_tail[1]) / 2)
    ctrl_s2 = (midp[0] + perp[0] * bow, midp[1] + perp[1] * bow)
    pts2 = quad_bezier(s2_head, ctrl_s2, s2_tail, n=36)
    widths2 = [10 - 7 * (i / 36) for i in range(37)]  # taper 10 -> 3
    stroke_variable_width(draw, pts2, widths2)

    # ---- Stroke 3: small tail/tick near cell C (dot-like) ----
    # A short mark ending upward-right from near cell C — the small
    # "点/tick" that appears above/right of the curve's belly.
    s3_head = anchor_to_xy(('C', 0.767, 0.863))
    s3_tail = anchor_to_xy(('C', 0.95, 0.55))  # short up-right tick
    dx3 = s3_tail[0] - s3_head[0]
    dy3 = s3_tail[1] - s3_head[1]
    length3 = (dx3 * dx3 + dy3 * dy3) ** 0.5
    perp3 = (-dy3 / length3, dx3 / length3)
    bow3 = 0.04 * length3
    midp3 = ((s3_head[0] + s3_tail[0]) / 2,
             (s3_head[1] + s3_tail[1]) / 2)
    ctrl_s3 = (midp3[0] + perp3[0] * bow3, midp3[1] + perp3[1] * bow3)
    pts3 = quad_bezier(s3_head, ctrl_s3, s3_tail, n=24)
    widths3 = [9 - 6 * (i / 24) for i in range(25)]  # taper 9 -> 3
    stroke_variable_width(draw, pts3, widths3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_fei(draw)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '01_飞.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
