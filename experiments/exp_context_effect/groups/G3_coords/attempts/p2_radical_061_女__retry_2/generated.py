# p2_radical_061_女 (nü) — G3 coord-bank RETRY #2.
#
# Retry_1 diagnosis (from PNG vs GT):
#   The 撇点 V was too shallow / too diagonal — the two legs read as
#   near-parallel rather than a distinct V opening downward. Also the
#   long 撇 crossed BELOW the V-vertex instead of THROUGH it, so the
#   character read as separate strokes.
#
# GT observation (fresh look):
#   Stroke 1: 撇点 (pie-dian) — a deep V with vertex low.
#     Pie leg starts upper-mid (~x=150,y=60), sweeps down-LEFT with a
#     slight belly to vertex (~x=95,y=175). Dot leg starts at same
#     vertex, shoots down-RIGHT to (~x=170,y=225). Legs form a wide
#     V opening downward.
#   Stroke 2: 撇 (long crossing) — starts upper-right (~x=205,y=95),
#     sweeps down-LEFT with belly, passes through / near the pie-dian
#     vertex, tail at lower-left (~x=55,y=250).
#   Stroke 3: 横 — long horizontal near y=170 spanning x=45..245, THIN.
#
# Key fixes vs retry_1:
#   - Make the 撇点 V deeper (vertex lower, ~y=178) and legs more open.
#   - Ensure long 撇 crosses THROUGH the V-vertex (ctrl point pulled
#     toward (95,175)).
#   - Keep strokes thin (per P12 — MMH GT is uniform-thin).
#   - Crossbar just above vertex at y~168.

import os

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _bezier2(draw, p0, p1, p2, r_head, r_tail, steps=70):
    """Quadratic bezier with linearly-varying stamp radius."""
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        r = r_head + (r_tail - r_head) * u
        r = max(0.6, r)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_nü(t, ox=0, oy=0, scale=1.0):
    """女 radical inlined: 撇点 (deep V) + long 撇 crossing through vertex + 横 crossbar."""

    # ----- Stroke 1: 撇点 -----
    # Pie leg: (150,58) -> vertex (95,178). Slight left-bowing curve.
    pd_head   = (150 + ox, 58 + oy)
    pd_ctrl   = (118 + ox, 118 + oy)
    pd_vertex = (95  + ox, 178 + oy)
    _bezier2(t, pd_head, pd_ctrl, pd_vertex,
             r_head=4.5 * scale, r_tail=1.6 * scale, steps=70)

    # Dot leg: vertex (95,178) -> (172,228). Thin at vertex, thickens then
    # tapers at tail.
    dp_start = (95  + ox, 178 + oy)
    dp_ctrl  = (135 + ox, 205 + oy)
    dp_end   = (172 + ox, 228 + oy)
    # Two-pass stroke: first pass swells, second pass tapers.
    steps = 60
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * dp_start[0] + 2 * (1 - u) * u * dp_ctrl[0] + u * u * dp_end[0]
        y = (1 - u) ** 2 * dp_start[1] + 2 * (1 - u) * u * dp_ctrl[1] + u * u * dp_end[1]
        # Thin at vertex(u=0), swell to u~0.65, then taper.
        if u < 0.65:
            r = 1.8 + (5.5 - 1.8) * (u / 0.65)
        else:
            r = 5.5 + (2.0 - 5.5) * ((u - 0.65) / 0.35)
        r = max(0.6, r * scale)
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    # ----- Stroke 2: long 撇 crossing THROUGH the V-vertex -----
    # Head upper-right (208,88), curves down-left through (~100,175),
    # tail lower-left (55,250).
    p_head = (208 + ox, 88 + oy)
    p_ctrl = (128 + ox, 165 + oy)   # pulls curve through vertex area
    p_tail = (55  + ox, 250 + oy)
    _bezier2(t, p_head, p_ctrl, p_tail,
             r_head=4.8 * scale, r_tail=1.0 * scale, steps=90)

    # ----- Stroke 3: 横 crossbar -----
    # Horizontal near y=168, x=45..248. Very slight upward tilt.
    h_x0 = 45  + ox
    h_x1 = 248 + ox
    h_y0 = 170 + oy
    h_y1 = 164 + oy
    n_h = 70
    for i in range(n_h + 1):
        u = i / n_h
        x = h_x0 + (h_x1 - h_x0) * u
        y = h_y0 + (h_y1 - h_y0) * u
        # Slight taper: thicker toward middle, thin at ends.
        r = (2.6 + 0.9 * (1 - abs(2 * u - 1))) * scale
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def main():
    out = os.path.join(os.path.dirname(__file__), "01_女.png")
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_nü(t)
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
