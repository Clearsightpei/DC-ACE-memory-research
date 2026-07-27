"""Render 勹 (bao) at 300x300 PIL, black ink on white.

勹 has 2 strokes:
  1) 撇 — short-medium steep diagonal, upper area, thick→thin taper.
  2) 横折钩 — short horizontal at top-right, shoulder dab, curved
     vertical descending down and bowing right, ending with an
     up-and-left flick (hook).

The 撇 sits above the horizontal shoulder; the horizontal starts near
where the 撇 ends and shoots right, then curves down enclosing the
'wrap' shape. Following form_catalog: 撇 as top-of-radical single
flick (dedicated entry for 勹). Steep 75deg, ~x=155..115 y=75..145.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def taper_line(pts, w_start, w_end):
    """Draw a taper by placing dabs along a piecewise-linear path.
    pts: list of (x, y). Radius interpolated from w_start->w_end over path."""
    # total path length
    total = 0.0
    seg_lens = []
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        L = (dx * dx + dy * dy) ** 0.5
        seg_lens.append(L)
        total += L
    if total <= 0:
        return
    step = 0.7
    acc = 0.0
    for i in range(len(pts) - 1):
        L = seg_lens[i]
        if L <= 0:
            continue
        n = max(1, int(L / step))
        for k in range(n + 1):
            t = k / n
            x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t
            y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t
            u = (acc + t * L) / total
            r = w_start * (1 - u) + w_end * u
            dab(x, y, r)
        acc += L


# ---------- Stroke 1: 撇 (top-left single flick) ----------
# Steeper, longer to match GT: starts (155,55) ends (95,150).
pie_pts = [
    (155, 55),
    (140, 78),
    (125, 102),
    (110, 128),
    (95, 150),
]
taper_line(pie_pts, w_start=4.4, w_end=1.4)
# 顿 dab at start
dab(155, 55, 4.8)


# ---------- Stroke 2: 横折钩 ----------
# Top horizontal spans from near the 撇 crossing (~x=115,y=115) to
# a top-right shoulder (~x=225,y=100). Then curved 竖 descends,
# bowing rightward, reaching (215, 255), then hook flicks up-left
# to (185, 240).

hb_start = (115, 115)
hb_shoulder = (228, 100)
taper_line([hb_start, (150, 110), (190, 103), hb_shoulder], w_start=3.8, w_end=3.6)
# Start dab (顿)
dab(115, 115, 3.8)
# shoulder dab (顿, slightly bigger)
dab(228, 100, 4.6)

# curved vertical down, bowing right, terminating at bottom.
def qbez(P0, P1, P2, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        pts.append((x, y))
    return pts


curve_pts = qbez((228, 100), (250, 185), (212, 258), n=70)
taper_line(curve_pts, w_start=3.6, w_end=3.0)

# hook flick: up-and-left from curve terminal
hook_pts = [(212, 258), (198, 250), (185, 242), (172, 232)]
taper_line(hook_pts, w_start=3.0, w_end=1.2)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0037_勹/01_勹.png"
)
print("wrote 01_勹.png")
