"""
G3 (coord-bank) — p1_stroke_17_撇点 (pie-dian)
Stroke shape: a 撇 (left-falling curve from upper-right to lower-left,
tapering) that turns and becomes a 点 (short right-down dot) at its
tail. This is a compound stroke used e.g. in 女, 巛.

Coordinate format: raw numeric (ox, oy, scale) offsets, no anchors.
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

CANVAS = 300
OUT = "01_撇点.png"


def draw_pie_dian(img_draw, ox=150, oy=150, scale=1.0):
    # --- 撇 portion: a curve from upper-right down to lower-left,
    # tapering from thick to thin. Rendered as a series of overlapping
    # circles whose radius shrinks along the path.
    # Path anchor points (in canvas coords, y grows DOWN like PIL):
    pie_start = (ox + 55 * scale, oy - 70 * scale)    # upper right
    pie_mid   = (ox + 20 * scale, oy - 20 * scale)    # bending down-left
    pie_end   = (ox - 40 * scale, oy + 35 * scale)    # lower left (tail tip)

    # Quadratic-bezier sampling for the 撇 curve
    def qbez(p0, p1, p2, t):
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        return x, y

    steps = 60
    r_start = 8.0 * scale   # thick head
    r_end = 1.2 * scale     # thin tail
    for i in range(steps + 1):
        t = i / steps
        x, y = qbez(pie_start, pie_mid, pie_end, t)
        r = r_start + (r_end - r_start) * t
        img_draw.ellipse(
            [x - r, y - r, x + r, y + r], fill="black"
        )

    # --- 点 portion: at the pivot near the tail, a short thick dot
    # heading down-right. It starts where the 撇 ends its curve and
    # goes to the lower-right.
    dot_start = (ox - 30 * scale, oy + 25 * scale)  # slightly inside pie tail
    dot_end   = (ox + 10 * scale, oy + 65 * scale)  # lower-right end

    dot_steps = 30
    r_dot_start = 3.0 * scale
    r_dot_end = 9.0 * scale  # dot swells toward its tail (typical 点)
    for i in range(dot_steps + 1):
        t = i / dot_steps
        x = dot_start[0] + (dot_end[0] - dot_start[0]) * t
        y = dot_start[1] + (dot_end[1] - dot_start[1]) * t
        r = r_dot_start + (r_dot_end - r_dot_start) * t
        img_draw.ellipse(
            [x - r, y - r, x + r, y + r], fill="black"
        )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_pie_dian(d, ox=155, oy=145, scale=1.6)
    img.save(OUT)
    print(f"wrote {OUT} ({CANVAS}x{CANVAS})")


if __name__ == "__main__":
    main()
