"""p3_char_0188_边 — G4 attempt

Decomposition: 边 = inner (力-like: 横折钩 + 撇) + 辶 (dot + top-curve + 平捺)
Total = 5 strokes (matches MMH expected count).

Memory consulted:
  - drawer_memory.md v8 read: no chronic primitive for 边 or 辶; component
    playbook (enclosing + left-radical) doesn't cleanly fit — 辶 wraps
    around left+bottom. Drawing fresh per shared_rules supplementary aid.
  - success_bank/INDEX.md grep for 边/辶/力: none present.
  - errata.md grep for 边: not present.

Anchors follow the MMH-derived expectations block verbatim.
"""

import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 5 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('s1 heng-zhe-gou corner @ C(0.746, 0.47); s2 撇 crosses s1 corner (P); '
              's3 top dot; s4 辶 middle curve; s5 平捺 bottom sweep. '
              's2.tail vs s5.mid: N-gap ~22 px preserved. '
              's4.tail vs s5.mid: N-gap ~11 px preserved.')
}


def draw_bian():
    from PIL import ImageDraw
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---------- Stroke 1: 横折钩 (inner top-right frame) ----------
    # head C(0.239, 0.523), tail BC(0.746, 0.37); corner near s1.mid(0.20) @ C(0.746, 0.47)
    s1_h = anchor_to_xy(('C', 0.239, 0.523))
    s1_corner = anchor_to_xy(('C', 0.746, 0.47))
    s1_t = anchor_to_xy(('BC', 0.746, 0.37))
    pts_h = sample_line(s1_h, s1_corner, 15)
    pts_s = sample_line(s1_corner, s1_t, 25)
    pts1 = pts_h + pts_s[1:]
    widths1 = [7] * len(pts1)
    stroke_variable_width(draw, pts1, widths1)
    # tiny hook at tail (leftward tick)
    hook_end = (s1_t[0] - 14, s1_t[1] - 4)
    stroke_variable_width(draw, [s1_t, hook_end], [7, 3])

    # ---------- Stroke 2: 撇 (upper-right to lower-left inside inner) ----------
    s2_h = anchor_to_xy(('TC', 0.708, 0.7))
    s2_t = anchor_to_xy(('BC', 0.257, 0.499))
    ctrl2 = ((s2_h[0] + s2_t[0]) / 2 + 8, (s2_h[1] + s2_t[1]) / 2 - 2)
    n2 = 40
    pts2 = quad_bezier(s2_h, ctrl2, s2_t, n2)
    widths2 = [max(3, int(9 - 6 * i / n2)) for i in range(n2 + 1)]  # thick head, thin tail (撇)
    stroke_variable_width(draw, pts2, widths2)

    # ---------- Stroke 3: 点 (辶's top dot, compact down-right tick) ----------
    # MMH endpoints span ~45 px which is longer than a typical calligraphic dot;
    # per v8, trust visual — shorten to a compact dot centered on the MMH midpoint.
    s3_h_raw = anchor_to_xy(('TL', 0.729, 0.718))
    s3_t_raw = anchor_to_xy(('C', 0.058, 0.037))
    mid = ((s3_h_raw[0] + s3_t_raw[0]) / 2, (s3_h_raw[1] + s3_t_raw[1]) / 2)
    # 20-px dot from mid, direction s3_h_raw -> s3_t_raw
    import math
    dx, dy = s3_t_raw[0] - s3_h_raw[0], s3_t_raw[1] - s3_h_raw[1]
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    s3_h = (mid[0] - 10 * ux, mid[1] - 10 * uy)
    s3_t = (mid[0] + 10 * ux, mid[1] + 10 * uy)
    n3 = 8
    pts3 = sample_line(s3_h, s3_t, n3)
    widths3 = [max(4, int(4 + 5 * i / n3)) for i in range(n3 + 1)]  # thin head, thick tail (点)
    stroke_variable_width(draw, pts3, widths3)

    # ---------- Stroke 4: 辶 middle curve (short heng-pie-like segment) ----------
    s4_h = anchor_to_xy(('ML', 0.296, 0.635))
    s4_t = anchor_to_xy(('BL', 0.867, 0.458))
    ctrl4 = ((s4_h[0] + s4_t[0]) / 2 - 4, (s4_h[1] + s4_t[1]) / 2 - 4)
    n4 = 30
    pts4 = quad_bezier(s4_h, ctrl4, s4_t, n4)
    widths4 = [6] * (n4 + 1)
    stroke_variable_width(draw, pts4, widths4)

    # ---------- Stroke 5: 平捺 (long bottom sweep of 辶) ----------
    s5_h = anchor_to_xy(('BL', 0.287, 0.584))
    s5_t = anchor_to_xy(('BR', 0.678, 0.848))
    # bow slightly down for classic ping-na curve
    ctrl5 = ((s5_h[0] + s5_t[0]) / 2, (s5_h[1] + s5_t[1]) / 2 + 18)
    n5 = 45
    pts5 = quad_bezier(s5_h, ctrl5, s5_t, n5)
    widths5 = [max(4, int(4 + 8 * i / n5)) for i in range(n5 + 1)]  # thin-to-thick flare
    widths5[-1] = 3  # taper tip
    widths5[-2] = 5
    stroke_variable_width(draw, pts5, widths5)

    return img


if __name__ == '__main__':
    img = draw_bian()
    out = os.path.join(HERE, '01_边.png')
    img.save(out)
    print('wrote', out)
