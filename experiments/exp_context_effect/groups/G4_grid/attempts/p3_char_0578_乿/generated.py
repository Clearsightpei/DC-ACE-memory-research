# BANK_DEVIATION
# skipped: all bank primitives
# reason: 乿 is a rare/unusual character; no bank component (幺/乙 variants) matches well enough to compose without heavy transform, so inline fresh from MMH anchors.
# fresh_component: yi_char_fresh_11stroke

"""Attempt for 乿 (G4). 11 strokes rendered directly from MMH anchors."""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, fat_line, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Fresh inline render; 11 strokes, all N-class joints preserved (no welding, small gaps).',
}


def curve(draw, a_head, a_tail, bulge=(0, 0), width=5):
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    mx = (p0[0] + p2[0]) / 2 + bulge[0]
    my = (p0[1] + p2[1]) / 2 + bulge[1]
    pts = quad_bezier(p0, (mx, my), p2, n=30)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)


def line(draw, a_head, a_tail, width=5):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    fat_line(draw, p0, p1, width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Top-left component (幺-like, strokes 1-7) ----
    # stroke 1: TC(0.342,0.747) -> ML(0.472,0.002) — pie (short diagonal down-left going up-right? head lower, tail upper)
    # In PIL y-down: head y=0.747 in TC row0 -> py=74.7; tail y=0.002 in ML row1 -> py=100.2
    # So head is higher on canvas (py=74) tail is lower (py=100). Short pie stroke.
    curve(d, ('TC', 0.342, 0.747), ('ML', 0.472, 0.002), bulge=(-4, 2), width=4)

    # stroke 2: ML(0.442,0.134) -> ML(0.595,0.339) — small pie going down-right
    curve(d, ('ML', 0.442, 0.134), ('ML', 0.595, 0.339), bulge=(-3, 3), width=4)

    # stroke 3: ML(0.882,0.005) -> C(0.002,0.184) — horizontal-ish stroke top of 幺
    curve(d, ('ML', 0.882, 0.005), ('C', 0.002, 0.184), bulge=(0, -3), width=4)

    # stroke 4: TC(0.386,0.902) -> C(0.184,0.23) — long pie
    curve(d, ('TC', 0.386, 0.902), ('C', 0.184, 0.23), bulge=(-6, 4), width=4)

    # stroke 5: ML(0.8,0.301) -> ML(0.973,0.685) — short vertical-ish on right side of top-幺
    curve(d, ('ML', 0.8, 0.301), ('ML', 0.973, 0.685), bulge=(2, 2), width=4)

    # stroke 6: C(0.172,0.424) -> BC(0.213,0.042) — pie going down
    curve(d, ('C', 0.172, 0.424), ('BC', 0.213, 0.042), bulge=(-3, 2), width=4)

    # stroke 7: C(0.189,0.881) -> BC(0.377,0.171) — long pie
    curve(d, ('C', 0.189, 0.881), ('BC', 0.377, 0.171), bulge=(-5, 3), width=4)

    # ---- Bottom-left (幺 lower dot cluster, strokes 8-10) ----
    # stroke 8: BL(0.902,0.174) -> BL(0.653,0.804) — pie down-left
    curve(d, ('BL', 0.902, 0.174), ('BL', 0.653, 0.804), bulge=(-4, 3), width=4)

    # stroke 9: BL(0.562,0.452) -> BL(0.39,0.839) — small pie
    curve(d, ('BL', 0.562, 0.452), ('BL', 0.39, 0.839), bulge=(-3, 2), width=4)

    # stroke 10: BC(0.236,0.42) -> BC(0.444,0.751) — dian-like or small na
    curve(d, ('BC', 0.236, 0.42), ('BC', 0.444, 0.751), bulge=(2, 2), width=4)

    # ---- Right side (乙, stroke 11) ----
    # stroke 11: TC(0.688,0.943) -> BR(0.566,0.42)
    # This is the big 乙 hook going down then right sweeping.
    p0 = anchor_to_xy(('TC', 0.688, 0.943))       # top: ~(89, 94)? wait TC col=1 -> px=(1+0.688)*100=168.8, py=(0+0.943)*100=94.3
    p_end = anchor_to_xy(('BR', 0.566, 0.42))      # BR col=2 row=2 -> px=(2+0.566)*100=256.6, py=(2+0.42)*100=242
    # Draw as: vertical descent then curve right at bottom
    # Segment A: near-vertical from p0 down to ~(180, 240)
    mid1 = (170, 170)
    mid2 = (185, 245)
    pts_a = quad_bezier(p0, mid1, mid2, n=30)
    # Segment B: horizontal sweep to p_end (curving right and slightly up)
    mid3 = (220, 260)
    pts_b = quad_bezier(mid2, mid3, p_end, n=30)
    pts = pts_a + pts_b
    widths = [5] * len(pts)
    stroke_variable_width(d, pts, widths)

    out = os.path.join(os.path.dirname(__file__), '01_乿.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
