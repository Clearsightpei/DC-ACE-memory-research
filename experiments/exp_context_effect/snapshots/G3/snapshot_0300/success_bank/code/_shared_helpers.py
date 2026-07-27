# _shared_helpers.py — helpers reused across B2+ bank entries.
#
# B2 curator note: bank entries increasingly need short tapered-bezier
# inline recipes because the underlying (ox, oy, scale) signature only
# permits uniform rescaling — it cannot vary stroke angle, taper, or
# width profile independently. To keep entries compact, common helpers
# live here and are imported by each bank entry.
#
# Math coord convention (P5): center origin at (150, 150), +y up.
# All helpers accept a PIL ImageDraw and math-coord endpoints.

CANVAS = 300


def to_px(ox, oy):
    """Math coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=48, head_ramp=0.0):
    """Quadratic bezier drawn as tapered stamped-line + circle caps.
    p0, p1, p2 are math coords. w_head, w_tail in pixels."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = to_px(bx, by)
        if head_ramp > 0 and u < head_ramp:
            w = w_head
        else:
            u2 = u if head_ramp == 0 else (u - head_ramp) / (1 - head_ramp)
            w = w_head + (w_tail - w_head) * u2
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def tapered_line(draw, p0, p1, w0, w1, n=32):
    """Tapered straight segment between math-coord endpoints."""
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        px, py = to_px(x, y)
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def variant_pie(draw, head, tail, bow_perp=-6.0, w_head=9.0, w_tail=1.5, n=48):
    """Adaptive 撇 primitive: bezier from (head math) to (tail math)
    with configurable perpendicular bow, head/tail widths.

    Addresses B2 diagnosis: 撇 in different contexts needs different
    angle/curvature/taper. This is a callable Python primitive that
    exposes those knobs (v7 memory-evolution addition — see
    principles_stroke_family.md P11)."""
    import math
    x0, y0 = head
    x1, y1 = tail
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    p1 = (mx0 + perp_x * bow_perp, my0 + perp_y * bow_perp)
    tapered_bezier(draw, head, p1, tail, w_head, w_tail, n=n)


def variant_na(draw, head, tail, bow_perp=8.0, w_head=2.0, w_belly=15.0,
               w_tail=3.0, belly_u=0.7, n=60):
    """Adaptive 捺: bezier head→belly→tail with belly at u=belly_u.
    B2 addition per user diagnosis (different 捺s need different taper)."""
    import math
    x0, y0 = head
    x1, y1 = tail
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    p1 = (mx0 + perp_x * bow_perp, my0 + perp_y * bow_perp)
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * p1[0] + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * p1[1] + u ** 2 * y1
        if u <= belly_u:
            t = u / belly_u
            w = w_head + (w_belly - w_head) * t
        else:
            t = (u - belly_u) / (1 - belly_u)
            w = w_belly + (w_tail - w_belly) * t
        wi = max(1, int(round(w)))
        px, py = to_px(bx, by)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def variant_dian(draw, head, tail, w_head=3.0, w_tail=13.0, bow_perp=-3.0, n=36):
    """Adaptive 点: small tapered bezier from thin head to heavy tail.
    Configurable to draw left-dot, right-dot, or standard dot by
    swapping head/tail positions."""
    import math
    x0, y0 = head
    x1, y1 = tail
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    p1 = (mx0 + perp_x * bow_perp, my0 + perp_y * bow_perp)
    tapered_bezier(draw, head, p1, tail, w_head, w_tail, n=n)


# ---- B3 addition (2026-07-22): joint/weld helpers ----
#
# B3 evidence: 7 of 13 retries used variant_pie/na/dian; only 5 of those
# showed fail-mode SHIFT (per-stroke improved, composition still off);
# 0 PASSed. Root cause of the composition failures (人, 入, 大, 犬, 力,
# 刀): the drawer knows which variant to call, but doesn't compute the
# exact pixel where the second stroke should weld to the first. These
# helpers make weld/kiss geometry explicit.


def bezier_point(p0, p1, p2, u):
    """Sample a quadratic bezier at parameter u∈[0,1]. Returns (x,y)."""
    x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
    y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
    return (x, y)


def line_point(p0, p1, u):
    """Sample a straight line at parameter u∈[0,1]. Returns (x,y)."""
    return (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)


def pie_point(head, tail, u, bow_perp=-6.0):
    """Return the (math-coord) point at parameter u along a variant_pie
    bezier from `head` to `tail` with the given `bow_perp`. Use to
    compute the exact pixel where a crossing/welding stroke should meet.

    Example (人):
        head_pie = (+35, +90); tail_pie = (-60, -95)
        apex = pie_point(head_pie, tail_pie, u=0.0, bow_perp=-6)  # = head_pie
        # For 人 kiss-at-apex: both 撇 head and 捺 head land at head_pie.
        head_na = head_pie  # explicit shared pixel

    Example (入, na starts mid-shaft on pie):
        weld = pie_point(head_pie, tail_pie, u=0.3, bow_perp=-6)
        # then variant_na(head=weld, tail=(+60, -95), ...)
    """
    import math
    x0, y0 = head
    x1, y1 = tail
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    p1 = (mx0 + perp_x * bow_perp, my0 + perp_y * bow_perp)
    return bezier_point(head, p1, tail, u)


def kiss_apex(pie_head, pie_tail, na_tail, u_pie=0.0, bow_pie=-6.0):
    """Return the (pie_head_used, na_head) tuple where pie and na share
    an apex/weld pixel.

    - `u_pie=0.0` → 人-style (both heads at pie_head, kissing at apex).
    - `u_pie=0.3` → 入-style (na starts mid-shaft on pie).
    - `u_pie=0.5` → 大-style (crossing at midpoint).

    Returns two (x, y) math-coord tuples: use the first as pie_head,
    the second as na_head. Guarantees the strokes share an exact pixel.
    """
    if u_pie == 0.0:
        return pie_head, pie_head
    weld = pie_point(pie_head, pie_tail, u_pie, bow_perp=bow_pie)
    return pie_head, weld


def mirror_dian_pair(shaft_x, y_center, spread=25.0, w_head=2.0,
                     w_tail=7.0, tilt=8.0):
    """Return two dian specs (left_dot_kwargs, right_dot_kwargs) for a
    mirror-pair like 忄, 丷, 火 side dots. Both dots have the same
    width profile; head/tail positions are mirrored around `shaft_x`.

    B3 addition: 忄, 丷, 丬 all failed on retry because the drawer had
    to hand-compute the mirror and got the bow sign wrong. This helper
    encapsulates the mirror geometry.

    Returns two dicts you spread into variant_dian:
        left, right = mirror_dian_pair(0, y_center=0, spread=25)
        variant_dian(draw, **left)
        variant_dian(draw, **right)
    """
    # Left dot: head upper-right, tail lower-left (tilt into shaft).
    left = dict(
        head=(shaft_x - spread + tilt, y_center + tilt),
        tail=(shaft_x - spread - tilt, y_center - tilt),
        w_head=w_head, w_tail=w_tail, bow_perp=+2.0,
    )
    # Right dot: head upper-left, tail lower-right (mirror of left).
    right = dict(
        head=(shaft_x + spread - tilt, y_center + tilt),
        tail=(shaft_x + spread + tilt, y_center - tilt),
        w_head=w_head, w_tail=w_tail, bow_perp=-2.0,
    )
    return left, right
