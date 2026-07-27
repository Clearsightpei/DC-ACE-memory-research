"""忄 (shù xīn, "heart-side", 3 strokes) — B2 pass.

Left-side radical. LEFT dot bows RIGHTWARD (opposite of standard dian),
so it's inlined here rather than reusing draw_dian.

Strokes:
  s1 — left 点 (inlined, bows right).
  s2 — right 点 (standard, bows down-right).
  s3 — 竖 (inlined with a top-curl press; center-column spine).

Joints:
  s2.head ⇆ s3.mid(0.25) @ C — N (~19 px).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line
from dian import draw_dian


def _left_dot(draw, head, tail, head_w=3, peak_w=10, curve=0.12,
              segments=24, color=(0, 0, 0)):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    dx, dy = p2[0]-p0[0], p2[1]-p0[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    # Reverse the perpendicular so belly lands on the RIGHT.
    perp = (-dy/length, dx/length)
    bow = -curve * length
    mid = ((p0[0]+p2[0])*0.5, (p0[1]+p2[1])*0.5)
    ctrl = (mid[0]+perp[0]*bow, mid[1]+perp[1]*bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments+1):
        t = i/segments
        # Bump: thin head → peak → thin tail
        w = head_w + (peak_w - head_w) * (4*t*(1-t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths, color=color)
    r = peak_w/2.0
    draw.ellipse([p2[0]-r, p2[1]-r, p2[0]+r, p2[1]+r], fill=color)


def _spine(draw, head, tail, color=(0, 0, 0)):
    # Curl-press top + straight body.
    p_head = anchor_to_xy(head)
    p_tail = anchor_to_xy(tail)
    ctrl1 = (p_head[0]-6, p_head[1]-4)
    ctrl2 = (p_head[0]-10, p_head[1]+4)
    pts_curl = quad_bezier(p_head, ctrl1, ctrl2, n=16)
    widths_curl = [3 + (11-3)*(i/16) for i in range(17)]
    stroke_variable_width(draw, pts_curl, widths_curl, color=color)
    pts_body = sample_line(ctrl2, p_tail, n=40)
    widths_body = [11 + (9-11)*(i/40) for i in range(41)]
    stroke_variable_width(draw, pts_body, widths_body, color=color)


def draw_xin_side(draw,
                  s1_head=('C', 0.125, 0.468), s1_tail=('BC', 0.014, 0.051),
                  s2_head=('C', 0.6, 0.371),   s2_tail=('C', 0.89, 0.632),
                  s3_head=('TC', 0.371, 0.697), s3_tail=('BC', 0.447, 1.073)):
    _left_dot(draw, s1_head, s1_tail, head_w=3, peak_w=10, curve=0.12)
    draw_dian(draw, s2_head, s2_tail, head_width=3, peak_width=10, curve=0.08)
    _spine(draw, s3_head, s3_tail)
