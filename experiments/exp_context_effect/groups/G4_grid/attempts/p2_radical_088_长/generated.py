"""长 (cháng) — 4-stroke radical. Revision 1.

Revised anchor plan after visual comparison with GT:
  - The upper 撇 (s1) is SHORT and lives in the upper-right region.
  - The 横 (s2) is a medium horizontal, slightly tilted up-right,
    crossing the descent about mid-height.
  - The 竖提 (s3) is the long descent — starts upper-mid area,
    goes DOWN AND SLIGHTLY LEFT, ending with a small 提 flick up-right
    near the bottom.
  - The 捺 (s4) is a LONG sweep from near the crossing point out to
    lower-right — the dominant right-hand stroke.

Joint plan:
  s2 crosses s3's body near mid (P — welded by overlap).
  s1's tail lands near/on s3's upper body (N — small gap OK).
  s4's head starts near the s2/s3 crossing (N — near the crossing).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Revision 1. Visual agreements with GT: '
              '(1) long rising/sweeping 捺 as the dominant right-hand stroke, '
              'ending in lower-right; '
              '(2) 横 crosses the descent body around mid-height forming '
              'the characteristic X-like intersection; '
              '(3) short upper 撇 sits in upper-right area, angled '
              'down-left toward the crossing.')
}


def draw_chang_char(draw):
    # --- s3 FIRST (drawn under s2 for a clean crossing) ---
    # Long descent: from upper-mid area straight down to lower-left,
    # then small 提 flick up-right. Both endpoints of descent share column
    # approximately (near center) — TR12-compliant vertical-ish.
    p_head = anchor_to_xy(('TC', 0.65, 0.15))
    # Slight curve control just below and slightly left
    p_mid  = anchor_to_xy(('C',  0.35, 0.55))
    p_bend = anchor_to_xy(('BL', 0.75, 0.80))  # near bottom-center, elbow
    p_flick = anchor_to_xy(('BC', 0.55, 0.50))  # 提 needle-tip up-right

    body_pts = quad_bezier(p_head, p_mid, p_bend, n=48)
    body_widths = [11 - (11 - 7) * (i / 48) for i in range(49)]
    stroke_variable_width(draw, body_pts, body_widths)

    # Rounded elbow
    r = 5
    draw.ellipse([p_bend[0] - r, p_bend[1] - r, p_bend[0] + r, p_bend[1] + r], fill=(0, 0, 0))

    # 提 flick up-right
    dx, dy = p_flick[0] - p_bend[0], p_flick[1] - p_bend[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = 0.05 * length
    fmid = ((p_bend[0] + p_flick[0]) * 0.5, (p_bend[1] + p_flick[1]) * 0.5)
    ctrl = (fmid[0] + perp[0] * bow, fmid[1] + perp[1] * bow)
    flick_pts = quad_bezier(p_bend, ctrl, p_flick, n=30)
    flick_widths = [9 - (9 - 1) * (i / 30) for i in range(31)]
    stroke_variable_width(draw, flick_pts, flick_widths)

    assert p_flick[1] < p_bend[1], "提 flick must rise"
    assert p_flick[0] > p_bend[0], "提 flick must go rightward"

    # --- s2: 横 across the middle, slight up-right tilt ---
    s2_head = ('ML', 0.10, 0.55)
    s2_tail = ('MR', 0.85, 0.45)   # same row (ML/MR) — TR12 OK
    draw_heng(draw, s2_head, s2_tail, width=9)

    # --- s1: short 撇 in upper-right area ---
    # Small piě, from about (200, 70) to (150, 130) — down-and-left.
    s1_head = ('TR', 0.15, 0.55)   # upper right region
    s1_tail = ('C',  0.30, 0.30)   # mid-upper center
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=2, curve=0.10, segments=36)

    # --- s4: long 捺 from near crossing to lower-right ---
    # Starts near where 横 meets descent, sweeps down-right, then extends
    # rightward with a slight upward foot at the end.
    s4_head = ('C',  0.20, 0.30)   # near the s2/s3 intersection zone
    s4_tail = ('BR', 0.95, 0.55)   # long tail out to right-lower
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang_char(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_长.png')
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
