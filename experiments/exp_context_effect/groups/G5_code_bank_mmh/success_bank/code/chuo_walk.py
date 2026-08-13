"""Bank primitive: 辶 (chuo, 'walk' — 3 strokes: dian + zigzag + ping_na).

Promoted from p2_radical_044_辶 (G5 B1 PASS, 2026-08-08). HIGH-REUSE:
enclosing radical for 这/进/远/近/道/... The bottom flat-捺 sweeps under the
enclosed component.

Uses ping_na.py (also promoted). Middle 横折折撇 is inlined here (no
suitable standalone primitive).
"""

from PIL import ImageDraw

from dian import draw_dian
from ping_na import draw_ping_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _line_thickened(draw, p0, p1, w0, w1, steps=40):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = w0 + (w1 - w0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _bezier_thickened(draw, pts_ctrl, w_head, w_tail, steps=60):
    p0, p1, p2 = pts_ctrl
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _draw_zigzag_zzp(draw, head, tail, w=5):
    """Inlined 横折折撇 (mid stroke of 辶): 3-segment zigzag."""
    hx, hy = head
    p_top_right = (hx + 30, hy - 3)
    p_mid_left = (hx + 4, hy + 32)
    p_low_mid = (hx + 20, hy + 55)
    _line_thickened(draw, head, p_top_right, w, w)
    _bezier_thickened(draw, (p_top_right, (hx + 34, hy + 14), p_mid_left), w, w)
    _bezier_thickened(draw, (p_mid_left, p_low_mid, tail), w, w - 1)


def draw_chuo(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(61.8, 71.8, ox, oy, scale)
    s1_tail = _tx(96.4, 96.7, ox, oy, scale)
    s2_head = _tx(27.2, 155.0, ox, oy, scale)
    s2_tail = _tx(81.4, 238.8, ox, oy, scale)
    s3_head = _tx(28.4, 254.3, ox, oy, scale)
    s3_tail = _tx(268.9, 278.9, ox, oy, scale)
    draw_dian(draw, s1_head, s1_tail,
              w_head=3 * scale, w_tail=8 * scale, bow=3 * scale)
    _draw_zigzag_zzp(draw, s2_head, s2_tail, w=max(2, int(5 * scale)))
    draw_ping_na(draw, s3_head, s3_tail)
