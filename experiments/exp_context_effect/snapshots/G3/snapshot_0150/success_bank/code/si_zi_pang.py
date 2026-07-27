# si_zi_pang.py — 纟 (sī, silk radical), 3 strokes.
# Batch B2 (position 102) — human PASSed.
#
# Composition: two small angular 撇折 hooks stacked (upper smaller,
# middle slightly larger) + long 提 spanning bottom.
# Fully inline-fresh (TR8): pie_zhe primitive is too wide and standalone-
# centered; ti primitive spans too wide. Hand-tuned tapered beziers.
#
# NOTE (v7 curator): frozen concrete instance. Only uniform (ox,oy,scale)
# is respected; angle/taper are baked in. Future adaptive-signature
# entries should expose per-stroke width/angle knobs — see
# form_catalog.md and _shared_helpers.variant_pie.

from PIL import Image, ImageDraw  # noqa: F401

CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=7):
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    h0 = (cx, cy)
    h2 = (cx + size * 1.7, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    r = ink * 0.75
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_si_zi_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """纟 radical (3 strokes). Frozen concrete instance from B2 PASS."""
    _draw_pie_zhe_hook(t, cx=-15, cy=55, size=22, ink=6)
    _draw_pie_zhe_hook(t, cx=-20, cy=5, size=26, ink=7)
    p0 = (-65, -70)
    p2 = (60, -45)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 6)
    _tapered_bezier(t, p0, p1, p2, w_head=14, w_tail=1.5, n=60, head_ramp=0.08)
