"""p3_char_0453_度 — 9 strokes: 广 (3) + 廿-like inner (4) + 又 (2).

# Decomp: 度 = 广(top-left frame: 点+横+撇) + 廿-inner (horiz+2 vert+horiz) + 又(横撇+捺).
# Sub-radicals reviewed: guang.py (not present in bank), you_again.py (available
# but its default anchors are top-of-canvas oriented, not fit for the small 又
# tucked under 广 in 度) → inline fresh via MMH anchors.
#
# BANK_DEVIATION
# skipped: you_again.py
# reason: bank's 又 uses TL/TR/BR anchors sized as a standalone char; here 又
#         sits in the bottom-left slot of 度 with BC/BL/BR anchors — scale +
#         position mismatch too extreme to reuse.
# fresh_component: you_bottom_slot_for_度

Strokes follow MMH-injected anchors verbatim.  P-joints welded via
shared cell overlap; N-joints preserved as natural gaps.
"""

import os, sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; P-joints (s4/s5, s4/s6, s8/s9) rely on cell C/BC overlap; N-joints (all others) preserved as gaps by anchor distance.',
}


def tapered_stroke(draw, p0, p1, w_head, w_tail):
    """Straight line with tapered width — head thick to tail thin (or vice versa)."""
    n = 24
    pts = []
    widths = []
    for i in range(n + 1):
        t = i / n
        x = p0[0] * (1 - t) + p1[0] * t
        y = p0[1] * (1 - t) + p1[1] * t
        pts.append((x, y))
        widths.append(w_head * (1 - t) + w_tail * t)
    stroke_variable_width(draw, pts, widths)


def curved_stroke(draw, p0, p1, ctrl_bias, w_head, w_tail):
    """Quadratic bezier with control point offset perpendicular to p0->p1."""
    mx = (p0[0] + p1[0]) / 2.0
    my = (p0[1] + p1[1]) / 2.0
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    # perpendicular vector
    px, py = -dy, dx
    length = max(1.0, (px * px + py * py) ** 0.5)
    px, py = px / length, py / length
    ctrl = (mx + px * ctrl_bias, my + py * ctrl_bias)
    pts = quad_bezier(p0, ctrl, p1, n=40)
    widths = [w_head * (1 - i / len(pts)) + w_tail * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 9 strokes: MMH anchors verbatim ----

    # s1 — 点 (top dot of 广), TC → TC, short diagonal
    p = anchor_to_xy(('TC', 0.424, 0.527))
    q = anchor_to_xy(('TC', 0.717, 0.753))
    tapered_stroke(draw, p, q, w_head=4, w_tail=9)

    # s2 — top 横 of 广, ML → TR, long nearly-horizontal slight rise
    p = anchor_to_xy(('ML', 0.932, 0.028))
    q = anchor_to_xy(('TR', 0.253, 0.879))
    tapered_stroke(draw, p, q, w_head=7, w_tail=6)

    # s3 — long 撇 of 广, TL → BL, sweeping down-left with slight curve
    p = anchor_to_xy(('TL', 0.744, 0.981))
    q = anchor_to_xy(('BL', 0.199, 0.994))
    curved_stroke(draw, p, q, ctrl_bias=-18, w_head=7, w_tail=2)

    # s4 — top 横 of inner 廿, ML → MR
    p = anchor_to_xy(('ML', 0.961, 0.562))
    q = anchor_to_xy(('MR', 0.396, 0.409))
    tapered_stroke(draw, p, q, w_head=6, w_tail=5)

    # s5 — left 竖 of inner 廿, C → C
    p = anchor_to_xy(('C', 0.254, 0.201))
    q = anchor_to_xy(('C', 0.397, 0.913))
    tapered_stroke(draw, p, q, w_head=6, w_tail=6)

    # s6 — right 竖 of inner 廿, C → C
    p = anchor_to_xy(('C', 0.799, 0.096))
    q = anchor_to_xy(('C', 0.772, 0.699))
    tapered_stroke(draw, p, q, w_head=6, w_tail=6)

    # s7 — bottom 横 of inner 廿, C → C, slight rise
    p = anchor_to_xy(('C', 0.462, 0.875))
    q = anchor_to_xy(('C', 0.928, 0.808))
    tapered_stroke(draw, p, q, w_head=5, w_tail=5)

    # s8 — 横撇 of 又 (starts near BC top, sweeps down-left to BL bottom)
    p = anchor_to_xy(('BC', 0.204, 0.153))
    q = anchor_to_xy(('BL', 0.782, 0.985))
    curved_stroke(draw, p, q, ctrl_bias=-10, w_head=7, w_tail=2)

    # s9 — 捺 of 又 (from BC to BR, swelling then tapering)
    p = anchor_to_xy(('BC', 0.154, 0.335))
    q = anchor_to_xy(('BR', 0.766, 0.977))
    # bezier with slight downward bow for na peak
    mx = (p[0] + q[0]) / 2.0
    my = (p[1] + q[1]) / 2.0
    ctrl = (mx - 6, my + 8)
    pts = quad_bezier(p, ctrl, q, n=48)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        # peak swell around t=0.7
        if t < 0.7:
            w = 3 + (12 - 3) * (t / 0.7)
        else:
            w = 12 - (12 - 2) * ((t - 0.7) / 0.3)
        widths.append(w)
    stroke_variable_width(draw, pts, widths)

    # ---- save ----
    out = os.path.join(os.path.dirname(__file__), '01_度.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
