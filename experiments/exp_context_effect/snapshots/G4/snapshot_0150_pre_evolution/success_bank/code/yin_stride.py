"""廴 (yǐn, "long stride", 2 strokes) — B1 pass.

No bank primitive fits either stroke without extreme transformation
(heng_zhe_zhe_zhe_gou is close but has a gou hook we don't want; na
primitive bows wrong for a level 平捺). Both strokes are inlined.

Strokes:
  s1 — 横折折撇 compact zigzag: tiny heng + tiny drop + tiny heng
       + long 撇 sweep down-left. Endpoints:
         A ML(0.352, 0.104) → B ML(0.72, 0.16) → C ML(0.50, 0.36)
         → D ML(0.82, 0.42) → E BL(0.179, 0.66).
  s2 — 平捺 (level na): thin head, mid-late swell, needle tail. Endpoints:
         P0 BL(0.381, 0.054) → P2 BR(0.76, 0.745), bow +0.14·length below.

Joint: s1 sweep ⇆ s2 head-region → P (welded crossing near BL cell).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def draw_yin_stride(draw):
    # Stroke 1 anchors
    A = anchor_to_xy(('ML', 0.352, 0.104))
    B = anchor_to_xy(('ML', 0.72, 0.16))
    C = anchor_to_xy(('ML', 0.50, 0.36))
    D = anchor_to_xy(('ML', 0.82, 0.42))
    E = anchor_to_xy(('BL', 0.179, 0.66))
    w_main = 6
    fat_line(draw, A, B, w_main)
    r = 4
    draw.ellipse([B[0]-r, B[1]-r, B[0]+r, B[1]+r], fill=(0, 0, 0))
    fat_line(draw, B, C, w_main)
    draw.ellipse([C[0]-r, C[1]-r, C[0]+r, C[1]+r], fill=(0, 0, 0))
    fat_line(draw, C, D, w_main)
    r = 5
    draw.ellipse([D[0]-r, D[1]-r, D[0]+r, D[1]+r], fill=(0, 0, 0))
    # 撇 sweep D→E, tapered, bowed rightward
    dx, dy = E[0]-D[0], E[1]-D[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    perp = (-dy/length, dx/length)
    mid = ((D[0]+E[0])*0.5, (D[1]+E[1])*0.5)
    ctrl = (mid[0]+perp[0]*0.12*length, mid[1]+perp[1]*0.12*length)
    pts = quad_bezier(D, ctrl, E, n=48)
    n = len(pts) - 1
    widths = []
    for i in range(n+1):
        t = i / n
        eased = t ** 1.4
        widths.append(11 + (2 - 11) * eased)
    stroke_variable_width(draw, pts, widths)

    # Stroke 2 — 平捺
    P0 = anchor_to_xy(('BL', 0.381, 0.054))
    P2 = anchor_to_xy(('BR', 0.76, 0.745))
    dx, dy = P2[0]-P0[0], P2[1]-P0[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    perp = (-dy/length, dx/length)
    mid = ((P0[0]+P2[0])*0.5, (P0[1]+P2[1])*0.5)
    ctrl = (mid[0]+perp[0]*0.14*length, mid[1]+perp[1]*0.14*length)
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
