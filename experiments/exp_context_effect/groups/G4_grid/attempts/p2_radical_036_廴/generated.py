"""p2_radical_036_廴  (yin, "long stride") — 2-stroke radical.

Structure per MMH:
  stroke 1: 横折折撇 (heng-zhe-zhe-pie) — the compound zigzag at top.
     head @ ('ML', 0.352, 0.104)
     tail @ ('BL', 0.179, 0.66)
  stroke 2: 平捺 (level-na) — the sweeping bottom stroke.
     head @ ('BL', 0.381, 0.054)
     tail @ ('BR', 0.76, 0.745)

Joints: 1 P joint at s1.mid ⇆ s2.mid @ BL (welded crossing).

The top stroke is a compound with no direct bank primitive (heng_zhe_zhe_zhe_gou
is close but has a gou hook we don't want). Drawing inline with variable-width
polyline via sample_line + quad_bezier. The 平捺 is inlined too (na primitive
assumes a diagonal chord and bows the wrong way for a level 平捺).
"""

SELF_CHECK = {
    'visual_ok': True,          # compact Z top-left + pie sweep + level-na — matches GT silhouette
    'stroke_count_ok': True,    # exactly 2 stroke primitives (compound top + na)
    'endpoint_mismatches': [
        # stroke 1 head A used ('ML', 0.352, 0.104) — matches expected exactly.
        # stroke 1 tail E used ('BL', 0.179, 0.66) — matches expected exactly.
        # stroke 2 head used ('BL', 0.381, 0.054) — matches expected exactly.
        # stroke 2 tail used ('BR', 0.76, 0.745) — matches expected exactly.
    ],
    'joint_class_mismatches': [
        # expected: s1.mid(0.73) ⇆ s2.mid(0.17) @ BL (~(80, 217)) : P (welded).
        # s1 sweeps down through the BL region (pie), s2 arcs up through BL near its head.
        # They visibly cross/weld at the lower-left — P satisfied.
    ],
    'overall_pass': True,
    'notes': 'revision 1 applied (compacted top zigzag; first pass had oversized Z).'
}

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, sample_line,
                     stroke_variable_width, fat_line)

CANVAS = 300


def draw_stroke1_heng_zhe_zhe_pie(draw):
    """Compound top stroke: heng → small zhe down → heng → pie sweep down-left.

    Anchors (米字格):
      A head    @ ('ML', 0.352, 0.104)  — start of top 横
      B corner1 @ ('TC', 0.55,  0.32)   — end of top 横 / top of small 竖
      C corner2 @ ('TC', 0.35,  0.72)   — bottom of small 竖 / start of lower 横
      D corner3 @ ('ML', 0.80,  0.35)   — end of lower 横 / start of 撇 sweep
      E tail    @ ('BL', 0.179, 0.66)   — needle tip of 撇
    """
    # Compact Z at top-left; long pie sweep down to (BL, 0.179, 0.66).
    # Joint constraint: s1.mid(0.73) ~ (('BL', 0.796, 0.174)) → (80, 217).
    A = anchor_to_xy(('ML', 0.352, 0.104))   # ~(35, 110) — start of tiny heng
    B = anchor_to_xy(('ML', 0.72,  0.16))    # ~(72, 116) — end of tiny heng
    C = anchor_to_xy(('ML', 0.50,  0.36))    # ~(50, 136) — end of tiny drop
    D = anchor_to_xy(('ML', 0.82,  0.42))    # ~(82, 142) — end of second tiny heng / pie start
    E = anchor_to_xy(('BL', 0.179, 0.66))    # ~(18, 266) — needle tip

    w_main = 6

    # 1a: tiny top 横 A→B
    fat_line(draw, A, B, w_main)
    r = 4
    draw.ellipse([B[0]-r, B[1]-r, B[0]+r, B[1]+r], fill=(0,0,0))

    # 1b: tiny diagonal drop B→C (down-left)
    fat_line(draw, B, C, w_main)
    r = 4
    draw.ellipse([C[0]-r, C[1]-r, C[0]+r, C[1]+r], fill=(0,0,0))

    # 1c: tiny second 横 C→D (right/down-right)
    fat_line(draw, C, D, w_main)
    r = 5
    draw.ellipse([D[0]-r, D[1]-r, D[0]+r, D[1]+r], fill=(0,0,0))

    # 1d: 撇 sweep D→E, tapered thick→needle, gently curved (bow to right)
    dx, dy = E[0]-D[0], E[1]-D[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    # perp choice: we want the sweep to bow OUTWARD (to the right/below)
    # so the pie has a natural leftward-concave arc.
    perp = (-dy/length, dx/length)
    mid = ((D[0]+E[0])*0.5, (D[1]+E[1])*0.5)
    bow = 0.12 * length
    ctrl = (mid[0]+perp[0]*bow, mid[1]+perp[1]*bow)
    pts = quad_bezier(D, ctrl, E, n=48)
    n = len(pts) - 1
    widths = []
    for i in range(n+1):
        t = i / n
        eased = t ** 1.4
        widths.append(11 + (2 - 11) * eased)  # 11 → 2 (needle)
    stroke_variable_width(draw, pts, widths)


def draw_stroke2_ping_na(draw):
    """Level 平捺 — the sweeping bottom stroke of 廴.

    Anchors:
      head @ ('BL', 0.381, 0.054)  — starts in upper-BL cell, mid-upper area
      tail @ ('BR', 0.76,  0.745)  — sweeps down to BR needle 出锋

    Shape: gentle S — dips down and to the right, thin head, swell mid-late,
    needle tip. Bows downward (below chord).
    """
    P0 = anchor_to_xy(('BL', 0.381, 0.054))
    P2 = anchor_to_xy(('BR', 0.76,  0.745))
    dx, dy = P2[0]-P0[0], P2[1]-P0[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    # bow downward (positive y in PIL): use +perp with sign so control goes below chord
    perp = (dy/length, -dx/length)  # this is one perp
    # We want ctrl BELOW chord midpoint → larger y. Test: if dx>0, dy>0, perp=(dy/L,-dx/L)
    # gives ctrl at +dy/L in x and -dx/L in y (up-right). We want DOWN so flip:
    perp = (-dy/length, dx/length)
    mid = ((P0[0]+P2[0])*0.5, (P0[1]+P2[1])*0.5)
    bow = 0.14 * length
    ctrl = (mid[0]+perp[0]*bow, mid[1]+perp[1]*bow)
    pts = quad_bezier(P0, ctrl, P2, n=56)
    n = len(pts) - 1
    widths = []
    peak_t = 0.78
    head_w, peak_w, tail_w = 4, 15, 1
    for i in range(n+1):
        t = i / n
        if t <= peak_t:
            u = t / peak_t
            w = head_w + (peak_w - head_w) * u
        else:
            u = (t - peak_t) / max(1e-6, 1.0 - peak_t)
            w = peak_w + (tail_w - peak_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)
    draw_stroke1_heng_zhe_zhe_pie(draw)
    draw_stroke2_ping_na(draw)
    out = os.path.join(HERE, '01_廴.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
