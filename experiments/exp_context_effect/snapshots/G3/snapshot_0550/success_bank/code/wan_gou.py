# wan_gou.py — 弯钩 (wan gou, curved hook) coord primitive.
# Extracted from attempts/p1_stroke_07_弯钩/generated.py after human PASS.
# Note: the passing attempt was drawn with turtle (math coords, +y up).
# We re-express in PIL for consistency with the rest of the bank.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def draw_wan_gou(t, ox=0, oy=0, scale=1.0):
    """弯钩 = long curved arc + short leftward hook flick at bottom."""
    # Main curved body (math coords).
    p_start = (5 * scale, 110 * scale)
    p_ctrl = (40 * scale, 10 * scale)
    p_end = (-10 * scale, -95 * scale)

    body = _qbez(p_start, p_ctrl, p_end, 60)
    n = len(body)
    for i in range(n - 1):
        u = i / (n - 1)
        if u < 0.55:
            w = 6 + (10 - 6) * (u / 0.55)
        else:
            w = 10 - (10 - 5) * ((u - 0.55) / 0.45)
        w_int = max(3, int(round(w * scale)))
        p1 = _to_pixel(ox + body[i][0], oy + body[i][1])
        p2 = _to_pixel(ox + body[i + 1][0], oy + body[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        t.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))

    # Hook flick up-left.
    p_hook_tip = (-38 * scale, -75 * scale)
    p_hook_ctrl = (-22 * scale, -78 * scale)
    hook = _qbez(p_end, p_hook_ctrl, p_hook_tip, 20)
    m = len(hook)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 5 - (5 - 2) * u
        w_int = max(2, int(round(w * scale)))
        p1 = _to_pixel(ox + hook[i][0], oy + hook[i][1])
        p2 = _to_pixel(ox + hook[i + 1][0], oy + hook[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
