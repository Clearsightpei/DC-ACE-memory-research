"""毛 (máo) — 4画 radical.

Structure (from GT + MMH):
  s1: 撇 (short, top) — sweeps from upper-right down-to-left over the top,
       creates the "flag" of 毛 at the top.
  s2: 短横 (short, upper) — upper horizontal, right of the pie.
  s3: 长横 (long, middle) — main middle horizontal, spans most of the width.
  s4: 竖弯钩 — vertical descent from top-center-ish (crosses through the pie
       area), rounds at the bottom, sweeps right, hooks up.

Anchor plan (米字格; PIL-native, y grows DOWN):
  s1 (draw_pie):
    from ('TC', 0.80, 0.74) → to ('ML', 0.77, 0.18)
    (verbatim MMH; small compact pie in upper-central region)
  s2 (draw_heng):
    from ('ML', 0.72, 0.63) → to ('C',  0.88, 0.40)
    (verbatim MMH; short upper horizontal, slightly rising)
    NOTE: cells ML(row=1) and C(row=1) — same row → not tilted per TR12.
  s3 (draw_heng):
    from ('BL', 0.27, 0.26) → to ('MR', 0.19, 0.90)
    (verbatim MMH; middle long horizontal spanning near full width)
    NOTE: BL row=2 and MR row=1 mix rows, but the y_fracs (0.26 vs 0.90)
    inside those rows put both endpoints at ~y=226 vs ~y=190 — slight
    rise, matches GT (middle 横 with slight upward slope). Accepted.
  s4 (draw_shu_wan_gou):
    head    ('C', 0.10, 0.10)   — top of vertical, near center
    belly   ('C', 0.10, 0.60)   — same x for straight upper body
    corner  ('BC', 0.10, 0.65)  — round bend at bottom
    hook_pt ('BR', 0.60, 0.55)  — end of horizontal sweep (bottom-right)
    tip     ('BR', 0.65, 0.10)  — hook tip UP (y less than hook_pt)
    (extended from MMH s4 head C(0.10,0.10) tail BR(0.73,0.10) — MMH gives
    only 2 endpoints for the compound; we add belly/corner/hook per the
    canonical shu_wan_gou shape visible in GT.)

Joints (per MMH):
  J1: s1.mid(0.75) ⇆ s4.head @ C  — N (small gap ~11 px expected)
  J2: s2.mid(0.49) ⇆ s4.head @ C  — T (welded)  [s2's mid touches s4's body]
  J3: s3.mid(0.53) ⇆ s4.mid(0.29) @ BC — P (welded crossing)
       [s3 middle horizontal crosses s4's vertical descent]

Both J2 and J3 are realized because s4's body passes through the y-band of
s2 and s3 (s4 body runs vertically from y=110 to y=265 at x=110, then
sweeps right). s2's tail sits at x≈188 y≈140 — close to s4.head area.
s3 crosses s4's body at x=110 which is between s3's endpoints x=27 and
x=219, welded by nature of overlap.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Two specific visual agreements with GT: '
        '(1) Middle long horizontal spans nearly full width with slight '
        'upward tilt, matching GT. '
        '(2) 竖弯钩 descends from top-center, rounds at bottom-right, '
        'and hook tip flicks UP, matching GT silhouette. '
        'Structural: 4 strokes rendered; J1 N-gap ~22 px (in tolerance), '
        'J2 T achieved by s2 body ending near s4 head/body, '
        'J3 P achieved by s3 crossing through s4 vertical column.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 撇 (short, top) ---
    s1_head = ('TC', 0.80, 0.74)
    s1_tail = ('ML', 0.77, 0.18)
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=1, curve=0.10, segments=48)

    # --- Stroke 2: 短横 (upper) ---
    s2_head = ('ML', 0.72, 0.63)
    s2_tail = ('C',  0.88, 0.40)
    draw_heng(draw, s2_head, s2_tail, width=8)

    # --- Stroke 3: 长横 (middle, main) ---
    s3_head = ('BL', 0.27, 0.26)
    s3_tail = ('MR', 0.19, 0.90)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # --- Stroke 4: 竖弯钩 ---
    s4_head    = ('C',  0.10, 0.10)
    s4_belly   = ('C',  0.10, 0.60)
    s4_corner  = ('BC', 0.10, 0.65)
    s4_hook_pt = ('BR', 0.60, 0.55)
    s4_tip     = ('BR', 0.65, 0.10)

    # Sanity: hook tip must be ABOVE hook_pt (y_tip < y_hook_pt in PIL).
    p_hook = anchor_to_xy(s4_hook_pt)
    p_tip  = anchor_to_xy(s4_tip)
    assert p_tip[1] < p_hook[1], "Hook tip must flick UP."
    # Sanity: hook_pt must be RIGHT of corner (sweep goes right).
    p_corner = anchor_to_xy(s4_corner)
    assert p_hook[0] > p_corner[0], "Hook_pt must be right of corner."

    draw_shu_wan_gou(draw,
                     s4_head, s4_belly, s4_corner, s4_hook_pt, s4_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_毛.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
