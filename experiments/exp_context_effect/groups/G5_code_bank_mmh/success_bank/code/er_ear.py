"""Bank primitive: 阝 (er, "ear" left/right position radical — 2 strokes).

Promoted from p2_radical_020_阝__retry_2 (G5 B3 R2 PASS 2026-08-08).
VERY HIGH-REUSE (那/都/阳/院/防/际/陈/阿/隔/etc. — top-10 Phase-3 radical).

s1 = 横撇弯钩 (compact smooth 3-shape ear, inline: no bank primitive covers it).
s2 = 竖 (left vertical shaft).

The ear must stay COMPACT (max belly x ~= 175) with a clear waist cinch
at x ~= 128 — otherwise it reads as "B" not "3".
"""

from PIL import ImageDraw

from shu import draw_shu


def _cubic(p0, p1, p2, p3, steps=56):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] \
            + 3 * (1 - u) * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] \
            + 3 * (1 - u) * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def _ink(d, pts, w_head=6.5, w_tail=6.5):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        w = w_head + (w_tail - w_head) * t
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_er_ear(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — 3-shape ear (compact + smooth)
    upper = _cubic(_tx(128, 108, ox, oy, scale),
                   _tx(172, 95, ox, oy, scale),
                   _tx(175, 145, ox, oy, scale),
                   _tx(128, 152, ox, oy, scale))
    lower = _cubic(_tx(128, 152, ox, oy, scale),
                   _tx(172, 155, ox, oy, scale),
                   _tx(172, 195, ox, oy, scale),
                   _tx(142, 195, ox, oy, scale))
    _ink(draw, upper, w_head=max(2, 6.5 * scale), w_tail=max(2, 6.5 * scale))
    _ink(draw, lower, w_head=max(2, 6.5 * scale), w_tail=max(2, 6.5 * scale))
    # Terminal hook flick
    for i in range(15):
        t = i / 14
        x = _tx(142 + (118 - 142) * t, 195 + (188 - 195) * t, ox, oy, scale)[0]
        y = _tx(142 + (118 - 142) * t, 195 + (188 - 195) * t, ox, oy, scale)[1]
        w = max(1, (5.5 * (1 - t) + 1.2) * scale)
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # s2 — left shu
    draw_shu(draw, _tx(120, 115, ox, oy, scale),
             _tx(115, 290, ox, oy, scale),
             width=max(2, int(7 * scale)),
             top_curl=False)
