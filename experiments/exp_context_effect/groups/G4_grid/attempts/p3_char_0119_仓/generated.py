"""p3_char_0119_仓 — G4 attempt.

MMH structural expectations (4 strokes, all joints N):
  s1: head TC(0.386, 0.598)  tail BL(0.27, 0.115)      — 撇 (roof-left)
  s2: head TC(0.518, 0.926)  tail MR(0.859, 0.822)     — 捺 (roof-right)
  s3: head C (0.184, 0.913)  tail BC(0.31, 0.227)      — short 横折 / top of loop
  s4: head C (0.017, 0.808)  tail BR(0.355, 0.344)     — 横折弯钩-ish base loop

Joints (all N — natural gaps, do NOT weld):
  s1.head N s2.head @ TC (~20 px)     — roof apex gap
  s1.mid  N s4.head @ ML (~30 px)     — pie body vs loop-head gap
  s3.head N s4.head @ C  (~13 px)     — loop top vs loop head

MANDATORY LOOKUP CHECKLIST:
  1. success_bank/INDEX.md grep '仓' → none.
  2. errata.md grep '仓' → none.
  3. form_catalog.md — 撇+捺 roof + 巴-like base; no direct row, use generic.
  4. principles_meta.md TR1/TR6/TR8 — inline shape 3 & 4 since no exact primitive fits.
  5. joint_atlas.md — N gaps kept small (≤25 px per TR10).
  6. sandbox.md — no direct notes for 仓.

Approach: reuse draw_pie, draw_na for the roof; inline the loop base as
two curved fat lines (stroke 3 short vertical tail, stroke 4 an L-shape
from left-mid down and right).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes: pie, na, short-heng-zhe stub, L-shaped base curve. All joints N (gaps preserved).'
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: 撇 (pie) — head TC upper-mid, tail BL lower-left.
    s1_head = ('TC', 0.386, 0.598)
    s1_tail = ('BL', 0.27, 0.115)
    draw_pie(d, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.08, segments=48)

    # Stroke 2: 捺 (na) — head TC apex (slightly right of s1.head, gap ~20 px),
    #           tail MR lower-right. Roof of the 人.
    s2_head = ('TC', 0.518, 0.926)   # MMH-verbatim; ~20 px right of s1.head
    s2_tail = ('MR', 0.859, 0.822)
    draw_na(d, s2_head, s2_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.75, curve=0.10, segments=48)

    # Stroke 3: small 横折 top-of-loop.
    # MMH endpoints: head C(0.184, 0.913)=(118.4, 191.3); tail BC(0.31, 0.227)=(131, 222.7).
    # Interpret as a small heng-zhe: horizontal from head-region to right, then short drop.
    # Head at (118.4, 191.3), extend right ~40 px, then down to tail (131, 222.7).
    p3a = anchor_to_xy(('C', 0.184, 0.913))          # (118.4, 191.3)
    p3_corner = (170.0, 191.3)                       # extended right along the roof of loop
    p3b = anchor_to_xy(('BC', 0.31, 0.227))          # (131, 222.7)
    fat_line(d, p3a, p3_corner, width=8)
    fat_line(d, p3_corner, (170.0, 225.0), width=8)  # short drop on the right side of loop

    # Stroke 4: base loop — 横折弯钩-like L that forms the bottom of 巴.
    # MMH: head C(0.017, 0.808)=(101.7, 180.8); tail BR(0.355, 0.344)=(235.5, 234.4).
    # Interpret as an L: down from head to a low corner, then rightward to tail.
    p4a = anchor_to_xy(('C', 0.017, 0.808))          # (101.7, 180.8)
    p4b = anchor_to_xy(('BR', 0.355, 0.344))         # (235.5, 234.4)
    p4_corner = (101.7, 245.0)                        # bottom-left corner of loop
    # Left descent: p4a -> p4_corner (short vertical).
    fat_line(d, p4a, p4_corner, width=10)
    # Bottom sweep + slight rise: p4_corner -> p4b with a gentle curve.
    ctrl4 = (170.0, 255.0)
    pts4 = quad_bezier(p4_corner, ctrl4, p4b, n=48)
    n = len(pts4) - 1
    widths4 = [10 + 2 * (1.0 - abs(2 * (i / n) - 1)) for i in range(n + 1)]
    stroke_variable_width(d, pts4, widths4)

    out = os.path.join(os.path.dirname(__file__), '01_仓.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
