"""
p3_char_0086_巛 — G2 attempt (revised)
Character 巛 = three parallel S-shaped "stream" strokes.

GT re-read:
- Each stroke = a small angled head flick (top-right diagonal tick)
  then a long S-body: swings down-left in the upper half, then
  reverses and swings down-right, ending in a small hooked tail.
- Overall silhouette per stroke: shallow "S" leaning left, tail
  curls right/down-right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def draw_thick(pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def draw_stream(cx, y_top=75, y_bot=250):
    # 1) HEAD FLICK: short diagonal tick going down-left,
    #    starting slightly up-and-right of the body start.
    head_start = (cx + 10, y_top - 5)
    head_end   = (cx - 2,  y_top + 14)
    head_pts = bezier(head_start,
                      (cx + 7, y_top + 2),
                      (cx + 2, y_top + 8),
                      head_end, n=25)
    draw_thick(head_pts, 5, 3)

    # 2) BODY: proper S-curve.
    #    starts near head_end, bulges LEFT in upper 2/3,
    #    then reverses and swings RIGHT at bottom, ending in a small
    #    down-right tail hook.
    body_start = (cx - 2,  y_top + 10)
    ctrl1      = (cx - 28, y_top + 60)   # bulge LEFT upper
    ctrl2      = (cx - 22, y_bot - 30)   # keep left through middle-lower
    body_end_x = cx - 6                  # bottom sits slightly left of center
    body_end   = (body_end_x, y_bot - 8)
    body_pts   = bezier(body_start, ctrl1, ctrl2, body_end, n=80)
    draw_thick(body_pts, 6, 5)

    # 3) TAIL: small right-turning flick at the bottom of the body.
    tail_start = body_end
    tail_ctrl1 = (body_end_x + 4, y_bot - 2)
    tail_ctrl2 = (body_end_x + 10, y_bot + 2)
    tail_end   = (body_end_x + 16, y_bot + 4)
    tail_pts   = bezier(tail_start, tail_ctrl1, tail_ctrl2, tail_end, n=30)
    draw_thick(tail_pts, 5, 2)

# Three streams evenly spaced across the canvas
draw_stream(cx=85)
draw_stream(cx=150)
draw_stream(cx=220)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0086_巛/01_巛.png")
