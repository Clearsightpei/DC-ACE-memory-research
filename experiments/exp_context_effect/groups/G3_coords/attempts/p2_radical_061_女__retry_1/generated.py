# p2_radical_061_女 (nü) — G3 coord-bank RETRY #1.
#
# Prior FAIL diagnosis (from errata + comparing prior PNG vs GT):
#   Prior attempt made the strokes thick/bulky and the two diagonals
#   ran roughly parallel — they read as two separate slashes with a
#   heng under them, NOT as the crossing V of 女. Also the dot half
#   of 撇点 was oversized, obscuring structure.
#
# GT observation for 女 (redone):
#   The character is a compact 3-stroke:
#     Stroke 1: 撇点 (pie-dian). Starts around upper-center (~x=155,y=80),
#       sweeps down-LEFT to about (110,155), THEN reverses direction
#       and shoots down-RIGHT to about (170,205) as the "dot" leg.
#       This forms the LEFT-V shape of the character.
#     Stroke 2: 撇 (long diagonal). Starts upper-RIGHT (~x=200,y=70),
#       sweeps down-LEFT crossing through the pie-dian's midpoint
#       (~x=140,y=155), continuing to lower-left tail (~x=70,y=235).
#       It PASSES THROUGH the crossing point of stroke 1.
#     Stroke 3: 横 (crossbar). Long horizontal near y=165, spanning
#       roughly x=45..250. Thin.
#
# Fix idea (from errata): inline all three fresh, keep strokes THIN,
# and ensure the long 撇 crosses through the pie-dian's V-vertex.

import os

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def draw_nü(t, ox=0, oy=0, scale=1.0):
    """女 radical inlined: 撇点 + long 撇 crossing it + 横 crossbar."""

    # ----- Stroke 1: 撇点 (V-shape, left half of char) -----
    # Pie leg: from (155,80) down-left to vertex (108,155).
    pd_head = (155 + ox, 80 + oy)
    pd_ctrl = (128 + ox, 122 + oy)
    pd_vertex = (108 + ox, 158 + oy)

    steps = 60
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * pd_head[0] + 2 * (1 - u) * u * pd_ctrl[0] + u * u * pd_vertex[0]
        y = (1 - u) ** 2 * pd_head[1] + 2 * (1 - u) * u * pd_ctrl[1] + u * u * pd_vertex[1]
        # Head thick (~5px), thinning slightly toward vertex.
        r = (4.0 - 1.5 * u) * scale
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    # Dot leg: from vertex (108,158) down-RIGHT crossing UNDER the heng
    # and continuing to (195,235). Longer than a typical dot — this is
    # the pie-dian's assertive right leg forming the character's base.
    dp_start = (108 + ox, 158 + oy)
    dp_ctrl  = (150 + ox, 195 + oy)
    dp_end   = (198 + ox, 240 + oy)
    d_steps = 60
    for i in range(d_steps + 1):
        u = i / d_steps
        x = (1 - u) ** 2 * dp_start[0] + 2 * (1 - u) * u * dp_ctrl[0] + u * u * dp_end[0]
        y = (1 - u) ** 2 * dp_start[1] + 2 * (1 - u) * u * dp_ctrl[1] + u * u * dp_end[1]
        # Thin at vertex, swelling slightly then tapering at tail.
        r = (2.5 + 1.8 * u) * scale
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    # ----- Stroke 2: long 撇, crosses through the V-vertex -----
    # From upper-right (205,70) sweeping down-left through (~135,160)
    # (near pie-dian vertex) to tail (65,240). Thin, tapering.
    p_head = (205 + ox, 70 + oy)
    p_ctrl = (135 + ox, 165 + oy)
    p_tail = (62  + ox, 240 + oy)

    n_seg = 80
    prev = None
    for i in range(n_seg + 1):
        u = i / n_seg
        x = (1 - u) ** 2 * p_head[0] + 2 * (1 - u) * u * p_ctrl[0] + u * u * p_tail[0]
        y = (1 - u) ** 2 * p_head[1] + 2 * (1 - u) * u * p_ctrl[1] + u * u * p_tail[1]
        # Head thicker, thin tail (per pie primitive P10).
        r = (4.5 - 3.5 * u) * scale
        r = max(0.6, r)
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)

    # ----- Stroke 3: 横 crossbar, long thin horizontal -----
    # y ~ 165, x from 45 to 250. Slight upward tilt at right (calligraphic).
    h_x0 = 45 + ox
    h_x1 = 250 + ox
    h_y0 = 168 + oy
    h_y1 = 162 + oy   # tilts up slightly to the right
    n_h = 60
    prev = None
    for i in range(n_h + 1):
        u = i / n_h
        x = h_x0 + (h_x1 - h_x0) * u
        y = h_y0 + (h_y1 - h_y0) * u
        r = 3.5 * scale
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
