# pie_dian.py — 撇点 (pie dian, pie then dot) coord primitive.
# Extracted from attempts/p1_stroke_17_撇点/generated.py after human PASS.
# Original wrote directly in PIL image coords with an offset origin of
# (155, 145) and scale 1.6. Preserved verbatim, wrapped in the coord API.

CANVAS_SIZE = 300


def draw_pie_dian(t, ox=155, oy=145, scale=1.6):
    """撇点 = tapered 撇 curve + swelling 点 dot at the turn."""
    pie_start = (ox + 55 * scale, oy - 70 * scale)
    pie_mid = (ox + 20 * scale, oy - 20 * scale)
    pie_end = (ox - 40 * scale, oy + 35 * scale)

    def qbez(p0, p1, p2, u):
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        return x, y

    steps = 60
    r_start = 8.0 * scale
    r_end = 1.2 * scale
    for i in range(steps + 1):
        u = i / steps
        x, y = qbez(pie_start, pie_mid, pie_end, u)
        r = r_start + (r_end - r_start) * u
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    dot_start = (ox - 30 * scale, oy + 25 * scale)
    dot_end = (ox + 10 * scale, oy + 65 * scale)
    dot_steps = 30
    r_dot_start = 3.0 * scale
    r_dot_end = 9.0 * scale
    for i in range(dot_steps + 1):
        u = i / dot_steps
        x = dot_start[0] + (dot_end[0] - dot_start[0]) * u
        y = dot_start[1] + (dot_end[1] - dot_start[1]) * u
        r = r_dot_start + (r_dot_end - r_dot_start) * u
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
