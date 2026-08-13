"""Bank primitive: 韦 (wei, 'leather' — 4 strokes:
heng + heng + bottom-hook-compound + long-central-shu).

Promoted from p2_radical_123_韦__retry_1 (G5 B4 R1 PASS, 2026-08-08).
Medium-high reuse — appears in 伟/违/苇/纬/韩/围 (traditional variants).

BANK_DEVIATION note: s3 (bottom-hook) is an inline compound
(wider-than-heng_zhe_gou, softer descending curl, back-left hook) —
it does not fit any promoted stroke primitive cleanly. The compound
is inlined inside this whole-radical primitive; no separate stroke
primitive is extracted (insufficient reuse evidence: only 1 attempt).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _draw_wei_bottom_hook(draw, heng_head, corner, curl_tail, hook_tip):
    """Bottom compound of 韦: horizontal → soft corner → descending curl → back-left hook."""
    # Segment A: horizontal, slight downward drift
    steps_a = 80
    x0, y0 = heng_head
    x1, y1 = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 4.5 + 1.3 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    cx, cy = corner
    draw.ellipse((cx - 6.5, cy - 6.0, cx + 6.5, cy + 6.0), fill='black')
    # Segment B: descending curl (leftward)
    steps_b = 50
    x2, y2 = curl_tail
    ctrl_x = cx - 8
    ctrl_y = (cy + y2) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        w = 5.5 - 1.8 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Segment C: back-left hook, tapered
    steps_c = 26
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 4.2 * (1 - t) + 0.6
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def draw_wei_leather(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top heng, upward slant right
    draw_heng(draw,
              _tx(80, 125, ox, oy, scale), _tx(220, 108, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2: middle heng, upward slant right
    draw_heng(draw,
              _tx(82, 170, ox, oy, scale), _tx(218, 152, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s3: bottom hook compound (inline)
    _draw_wei_bottom_hook(draw,
                          heng_head=_tx(48, 218, ox, oy, scale),
                          corner=_tx(210, 225, ox, oy, scale),
                          curl_tail=_tx(200, 280, ox, oy, scale),
                          hook_tip=_tx(168, 268, ox, oy, scale))
    # s4: long central shu, top-curl entry, extends past canvas bottom
    draw_shu(draw,
             _tx(138, 62, ox, oy, scale), _tx(148, 310, ox, oy, scale),
             width=max(2, int(7 * scale)), top_curl=True)
