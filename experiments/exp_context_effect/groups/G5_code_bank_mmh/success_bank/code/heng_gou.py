"""Bank primitive: 横钩 (heng-gou — short horizontal + tight downward hook).

Extracted from p2_radical_112_欠 s2 (G5 B2 PASS 2026-08-08 via
BANK_DEVIATION). Distinct from heng_pie (which sweeps far down-left,
tuned for 又); heng_gou's hook is short and mostly downward.

Signature: (head, corner, hook_tip). MMH gives head + corner as the
median endpoints of the horizontal top; hook_tip extends BELOW the
corner (MMH median usually does not capture the hook). Idiomatic for
欠, 买, 家, 尔, 冖-tops that end in a hook.
"""

from PIL import ImageDraw


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_heng_gou(draw: ImageDraw.ImageDraw, head, corner, hook_tip,
                  w_start=3.0, w_corner=5.0, w_tip=1.5):
    """Draw 横钩: horizontal arc head→corner, then quarter-turn hook corner→hook_tip.

    Rendered as a chain of small filled ellipses so the ink can taper
    (calligraphic feel).
    """
    hx, hy = head
    cx, cy = corner
    apex = ((hx + cx) / 2, (hy + cy) / 2 - 3)   # slight lift on the horizontal
    pts_a = _bezier(head, apex, corner, steps=60)
    for i, (x, y) in enumerate(pts_a):
        t = i / (len(pts_a) - 1)
        w = w_start + (w_corner - w_start) * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    tx, ty = hook_tip
    mx, my = (cx + tx) / 2, (cy + ty) / 2
    dx, dy = tx - cx, ty - cy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular right-of-travel (image y-down) — pulls the hook inward
    px, py = -dy / L, dx / L
    ctrl = (mx + px * 6, my + py * 6)
    pts_b = _bezier(corner, ctrl, hook_tip, steps=50)
    for i, (x, y) in enumerate(pts_b):
        t = i / (len(pts_b) - 1)
        w = w_corner - (w_corner - w_tip) * t
        if w < 1.5:
            w = 1.5
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')
