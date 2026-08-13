"""Bank primitive: 横折提 (heng-zhe-ti compound: horizontal + corner + descend + rising ti).

Promoted from p2_radical_035_讠__retry_2 (G5 B3 PASS 2026-08-08).
Two independent BANK_DEVIATIONs saw this class: 讠 (retry_2 PASS) and
several unsuccessful attempts. High-reuse for speech-radical family
(说/话/记/让/请/让/词/许/该/etc.).

Endpoint signature. head = top-left start of horizontal;
tail = end of rising ti flick (up-right).
"""

from PIL import ImageDraw

from ti import draw_ti


def _stamp(draw, pts, width):
    for x, y in pts:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def _polyline(draw, pts, width):
    for a, b in zip(pts, pts[1:]):
        draw.line([a, b], fill='black', width=width)
    _stamp(draw, pts, width)


def draw_heng_zhe_ti(draw: ImageDraw.ImageDraw, head, tail,
                     corner=None, descend_mid=None, ti_head=None,
                     width=6):
    """Compose heng + corner-drop + rising ti.

    head:        (x, y) start of horizontal top segment
    tail:        (x, y) endpoint of rising ti flick
    corner:      optional (x, y) top-right corner where heng turns down;
                 defaults to point slightly right of head with same y
    descend_mid: optional intermediate (x, y) on the descending body
    ti_head:     optional (x, y) where the body ends and rising ti starts
    """
    hx, hy = head
    tx, ty = tail
    if corner is None:
        corner = (hx + max(50, (tx - hx) * 0.6), hy + 8)
    cx, cy = corner
    if ti_head is None:
        # ti_head near bottom-left of the descending body
        ti_head = (cx - abs(cx - hx) * 0.4, ty + 5)
    tih_x, tih_y = ti_head
    if descend_mid is None:
        descend_mid = ((cx + tih_x) * 0.5, (cy + tih_y) * 0.5)

    _polyline(draw, [head, (cx - 5, cy), corner, descend_mid, ti_head], width=width)

    # Rising ti flick (bank primitive)
    draw_ti(draw, ti_head, tail, w_head=max(3, int(width * 1.4)),
            w_tail=2, steps=50)
