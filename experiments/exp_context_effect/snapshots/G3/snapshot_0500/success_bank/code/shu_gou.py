# shu_gou.py — 竖钩 (shu gou, vertical + hook) coord primitive.
# Reconstructed after Phase-2 restart file surgery. Originally graduated
# from batch-3 retry (p1_stroke_14_竖钩) after batch-1 FAIL. The retry_attempt
# file was deleted in the restart wipe; this reconstruction follows shu.py's
# math-coord convention with an added upward-left hook flick.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_gou(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 竖钩: vertical shaft + short up-left hook.

    Canonical unit: shaft length ~180 px (from y=+90 to y=-90 in math coords),
    thickness 12 px. Hook flicks up-and-left ~30 px from shaft base, tapered.
    """
    half_len = 90.0 * scale
    thickness = max(1, int(round(12.0 * scale)))

    # Vertical shaft
    x_top, y_top = _to_pixel(ox, oy + half_len)
    x_bot, y_bot = _to_pixel(ox, oy - half_len)
    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)

    # Hook: from shaft base up-and-left, tapered via multiple line segments
    # Base at (ox, oy - half_len), tip at (ox - 25*scale, oy - half_len + 22*scale)
    hook_base = (ox, oy - half_len)
    hook_tip = (ox - 25.0 * scale, oy - half_len + 22.0 * scale)
    n_seg = 8
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((thickness - 1) * (1 - (u0 + u1) / 2) + 1)))
        x0, y0 = _to_pixel(*p0)
        x1, y1 = _to_pixel(*p1)
        t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=w)
