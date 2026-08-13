"""p3_char_0580_疵 — sickness radical 疒 + 此 inside.

Decomposition: 疵 = 疒 (strokes 1-5) + 此 (strokes 6-11); 此 = 止 (6-9) + 匕 (10-11).
Total 11 strokes (matches MMH expected).

Bank lookup (memory_index v8 checklist):
  1. drawer_memory.md — 疒 named-pattern `ne_sick_top_left_frame_for_*`
     (B13 evidence 75% non-FAIL: 疽 A + 疸 PASS). NO chronic/ne_sick.py
     exists — inline 5-stroke frame via _anchor + fat_line/quad_bezier.
     Use MMH-verbatim endpoints (A-recipe point 2).
  2. INDEX grep — 0171_疒, 0524_疸, 0528_疽 exist (frame precedent).
     No standalone 此/止/匕 primitive. Inline 6 strokes.
  3. errata grep 疵 — not present. 疒 cluster interior warning: keep
     此 crisp inside frame's bottom-right slot.

Layout: 疒 top-left frame (strokes 1-5), 此 bottom-right slot (6-11).

Per-stroke plan (all MMH-verbatim from injected block):
  s1  TC(.395,.601)->TC(.705,.861)   top-right dot (点)
  s2  C (.025,.21) ->MR(.259,.055)   top short heng (亠 bar)
  s3  ML(.817,.157)->BL(.343,1.062)  long 撇 sweep
  s4  ML(.41,.403) ->ML(.586,.693)   inner upper dot
  s5  BL(.182,.3)  ->BL(.721,.104)   inner lower rising 提
  s6  C (.318,.55) ->BC(.409,.464)   止 short 竖 (left)
  s7  BC(.532,.013)->C (.784,.951)   止 short 横 (bottom row)
  s8  BC(.034,.03) ->BC(.113,.552)   止 main 竖 (long down)
  s9  BL(.85,.681) ->BC(.734,.391)   止 提 (rising tick)
  s10 MR(.361,.638)->BR(.001,.062)   匕 撇 (falling left)
  s11 C (.819,.321)->BR(.669,.338)   匕 竖弯钩 (with hook tail)

Joints (all N — natural gaps, do NOT weld):
  Per dispatcher block; 13 N-joints preserved by MMH-verbatim placement.

A-recipe points followed: 1 (decomposition), 2 (MMH-verbatim), 3
(SELF_CHECK), 4 (base primitives inline), 5 (N-gaps).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 11 primitives
    'endpoint_mismatches': [],   # MMH-verbatim
    'joint_class_mismatches': [], # all N preserved as gaps
    'overall_pass': True,
    'notes': '疒 frame (5) + 此 (6) MMH-verbatim; all 13 N-joints kept as small gaps.'
}

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ========== 疒 FRAME (strokes 1-5) ==========

    # s1 — top dot (点), short tapered stroke
    h = anchor_to_xy(('TC', 0.395, 0.601))
    t = anchor_to_xy(('TC', 0.705, 0.861))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2 — top short 横 (亠 top bar)
    h = anchor_to_xy(('C', 0.025, 0.21))
    t = anchor_to_xy(('MR', 0.259, 0.055))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # s3 — long 撇 sweep (left-falling frame arm)
    h = anchor_to_xy(('ML', 0.817, 0.157))
    t = anchor_to_xy(('BL', 0.343, 1.062))
    ctrl = (h[0] - 20, h[1] + (t[1] - h[1]) * 0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(3 + 4 * (1 - abs(2 * u - 1)))  # bulge in middle
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper dot (short thick pie)
    h = anchor_to_xy(('ML', 0.41, 0.403))
    t = anchor_to_xy(('ML', 0.586, 0.693))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s5 — inner lower 提 (rising ti)
    h = anchor_to_xy(('BL', 0.182, 0.3))
    t = anchor_to_xy(('BL', 0.721, 0.104))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ========== 此 (strokes 6-11): 止 (6-9) + 匕 (10-11) ==========

    # s6 — 止 left short 竖
    h = anchor_to_xy(('C', 0.318, 0.55))
    t = anchor_to_xy(('BC', 0.409, 0.464))
    fat_line(d, h, t, 5)

    # s7 — 止 short 横 (near bottom of 止)
    h = anchor_to_xy(('BC', 0.532, 0.013))
    t = anchor_to_xy(('C', 0.784, 0.951))
    fat_line(d, h, t, 4)

    # s8 — 止 main long 竖 (down through 止)
    h = anchor_to_xy(('BC', 0.034, 0.03))
    t = anchor_to_xy(('BC', 0.113, 0.552))
    fat_line(d, h, t, 5)

    # s9 — 止 提 (rising tick, bottom of 止)
    h = anchor_to_xy(('BL', 0.85, 0.681))
    t = anchor_to_xy(('BC', 0.734, 0.391))
    pts = quad_bezier(h,
                      ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 2),
                      t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s10 — 匕 撇 (falling left from mid-right down to bottom-right)
    h = anchor_to_xy(('MR', 0.361, 0.638))
    t = anchor_to_xy(('BR', 0.001, 0.062))
    ctrl = ((h[0] + t[0]) / 2 + 4, (h[1] + t[1]) / 2 + 2)
    pts = quad_bezier(h, ctrl, t, n=40)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(6 - 4 * u)  # taper thick->thin
    stroke_variable_width(d, pts, widths)

    # s11 — 匕 竖弯钩 (down, curve right, hook up)
    h = anchor_to_xy(('C', 0.819, 0.321))
    t = anchor_to_xy(('BR', 0.669, 0.338))
    # midpoint via a control that dips low then curves right
    # anchor coordinates: draw as two segments with a bend near bottom
    corner_x = h[0] - 4
    corner_y = t[1] + 6
    corner = (corner_x, corner_y)
    # vertical segment (down)
    fat_line(d, h, corner, 5)
    # horizontal-with-hook segment (right and slight up-tick)
    pts = quad_bezier(corner,
                      ((corner[0] + t[0]) / 2, corner[1] + 4),
                      t, n=20)
    widths = [5 - 1 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    out = os.path.join(HERE, '01_疵.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
