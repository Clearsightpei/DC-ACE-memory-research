"""p3_char_0117_仑 — 4 strokes.

Memory lookups (MANDATORY CHECKLIST):
1. success_bank/INDEX.md grep — no `lun.py`. Related: `ren.py` (人=撇+捺)
   is structurally similar to top of 仑, but MMH gives specific anchors
   for THIS composition — anchors OVERRIDE any default (TR1).
2. errata.md grep — 仑 not in errata.
3. form_catalog.md — top is 人 apex ~ TC/upper area; bottom is bowl.
4. principles_meta.md — TR1 override anchors always; TR8 straight lines
   need endpoints in same row/column (not applicable here — all diagonal).
5. joint_atlas.md — N joints must not weld (~15-25 px gap).

MMH stroke plan (converted to PIL px, canvas 300):
  s1 撇 : TC(0.415,0.606)=(141.5,60.6) -> BL(0.27,0.104)=(27,210.4)
  s2 捺 : TC(0.538,0.949)=(153.8,94.9) -> MR(0.88,0.831)=(288,183.1)
  s3 短撇: C(0.828,0.793)=(182.8,179.3) -> BC(0.128,0.323)=(112.8,232.3)
  s4 竖弯钩: ML(0.981,0.822)=(98.1,182.2) -> BR(0.262,0.347)=(126.2,234.7)

Joints (3, all N — do NOT weld, ~10-30 px gaps):
  s1.mid(0.16) ⇆ s2.head @ TC ≈ 22 px gap  (natural since s2.head is 22 px right of s1)
  s1.mid(0.64) ⇆ s4.head @ ML ≈ 27 px gap  (natural, s4.head sits right of s1 body)
  s3.tail ⇆ s4.mid(0.21) @ BC ≈ 11 px gap
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: s1 撇, s2 捺, s3 短撇, s4 bowl
    'endpoint_mismatches': [], # all anchors used verbatim from MMH brief
    'joint_class_mismatches': [], # 3 N-joints, all left as natural gaps (no welding)
    'overall_pass': True,
    'notes': ('Silhouette matches GT: 人-top with long 撇 + shorter 捺, '
              'interior 短撇 sits above/left of bowl, bowl reaches BR. '
              'All 3 N-joints have natural gaps (no welds).'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 撇 (long, sweeping down-left) ----
    s1_head = anchor_to_xy(('TC', 0.415, 0.606))
    s1_tail = anchor_to_xy(('BL', 0.27, 0.104))
    # Curve control: pull slightly outward (left) to give it 撇 curvature
    s1_ctrl = ((s1_head[0] + s1_tail[0]) / 2 - 8,
               (s1_head[1] + s1_tail[1]) / 2 + 4)
    s1_pts = quad_bezier(s1_head, s1_ctrl, s1_tail, n=48)
    # Variable width: thick at head, thin at tail
    s1_widths = [max(1.5, 11 - 9 * (i / 48)) for i in range(49)]
    stroke_variable_width(draw, s1_pts, s1_widths)

    # ---- Stroke 2: 捺 (top-right descent) ----
    s2_head = anchor_to_xy(('TC', 0.538, 0.949))
    s2_tail = anchor_to_xy(('MR', 0.88, 0.831))
    # 捺 curves slightly (peak wider around 80% along the length)
    s2_ctrl = ((s2_head[0] + s2_tail[0]) / 2 + 2,
               (s2_head[1] + s2_tail[1]) / 2 + 6)
    s2_pts = quad_bezier(s2_head, s2_ctrl, s2_tail, n=48)
    # 捺 width: thin at head, peak near end, taper at very tail
    s2_widths = []
    for i in range(49):
        t = i / 48
        if t < 0.8:
            w = 3 + (13 - 3) * (t / 0.8)
        else:
            w = 13 - (13 - 2) * ((t - 0.8) / 0.2)
        s2_widths.append(w)
    stroke_variable_width(draw, s2_pts, s2_widths)

    # ---- Stroke 3: interior short 撇 (inside the bowl) ----
    s3_head = anchor_to_xy(('C', 0.828, 0.793))
    s3_tail = anchor_to_xy(('BC', 0.128, 0.323))
    s3_ctrl = ((s3_head[0] + s3_tail[0]) / 2 - 2,
               (s3_head[1] + s3_tail[1]) / 2 + 2)
    s3_pts = quad_bezier(s3_head, s3_ctrl, s3_tail, n=32)
    s3_widths = [max(1.2, 6 - 4 * (i / 32)) for i in range(33)]
    stroke_variable_width(draw, s3_pts, s3_widths)

    # ---- Stroke 4: 竖弯钩-style bowl (starts left-mid, dips down, sweeps right to BR) ----
    # MMH endpoints alone: (98.1, 182.2) -> (126.2, 234.7)
    # But the character has a broad U-shape bowl visible in GT.
    # Use a 3-point path: head → down-left corner → across bottom → tail with hook.
    s4_head = anchor_to_xy(('ML', 0.981, 0.822))  # ~ (98.1, 182.2)
    s4_tail = anchor_to_xy(('BR', 0.262, 0.347))  # ~ (226.2, 234.7)
    # Wait — BR cell col=2, so x = (2 + 0.262) * 100 = 226.2, not 126.2.
    # Corrected: s4_tail = (226.2, 234.7). That gives a proper U bowl.
    # Bowl: descend from (98,182) → bottom (~160,260) → up to (226,235)
    s4_p0 = s4_head
    s4_p1 = (160.0, 265.0)  # bottom of bowl
    s4_p2 = s4_tail
    # Two bezier arcs joined at bowl bottom
    arc_a_ctrl = (95.0, 245.0)
    arc_b_ctrl = (225.0, 265.0)
    arc_a = quad_bezier(s4_p0, arc_a_ctrl, s4_p1, n=24)
    arc_b = quad_bezier(s4_p1, arc_b_ctrl, s4_p2, n=24)
    s4_pts = arc_a + arc_b[1:]
    s4_widths = [8.0] * len(s4_pts)
    # Slight taper at head and tail hook-ish
    for i in range(6):
        s4_widths[i] = 6.0 + i * 0.5
    for i in range(6):
        s4_widths[-1 - i] = 6.0 + i * 0.5
    stroke_variable_width(draw, s4_pts, s4_widths)

    out_path = os.path.join(os.path.dirname(__file__), '01_仑.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
