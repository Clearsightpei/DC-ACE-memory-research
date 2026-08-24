"""p1_stroke_28_竖折折 — vertical, turn right, turn down again.

Coordinate format (G3): origin at canvas center (150,150), math coords
(y grows UP). Rendered with PIL for pixel-perfect 300x300 output.

Stroke design (three segments, two right-angle corners, brush 顿笔 at
each vertex per P6):
  Segment 1  竖 (down)      : (-55, +90)  -> (-55, +10)     length 80
  Segment 2  折 (rightward) : (-55, +10)  -> (+55, +10)     length 110
  Segment 3  折 (down again): (+55, +10)  -> (+55, -80)     length 90

Ink weight: 10 px (matches 竖 / 竖折 primitives).

No import from success_bank/code — the shu_zhe primitive only draws
one turn, and 竖折折 needs a second one that is part of the same ink
trace. Coordinates chosen to fit a roughly square envelope centered
on the canvas, slightly biased left/up so the second vertical segment
lands centrally after the second turn.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
CX, CY = W // 2, H // 2


def m2p(x, y):
    """math coords (center origin, +y up) -> PIL pixel coords."""
    return (CX + x, CY - y)


def draw_shu_zhe_zhe(draw, ox=0, oy=0, scale=1.0, ink=10):
    # Three joined tapered segments with 顿笔 blobs at every vertex.
    p1 = (ox + -55 * scale, oy + 90 * scale)   # top of first vertical
    p2 = (ox + -55 * scale, oy + 10 * scale)   # first corner (bottom-left)
    p3 = (ox + 55 * scale, oy + 10 * scale)    # second corner (top-right)
    p4 = (ox + 55 * scale, oy + -80 * scale)   # bottom of second vertical

    w = max(1, int(ink * scale))
    draw.line([m2p(*p1), m2p(*p2)], fill="black", width=w)  # 竖
    draw.line([m2p(*p2), m2p(*p3)], fill="black", width=w)  # 折 (rightward)
    draw.line([m2p(*p3), m2p(*p4)], fill="black", width=w)  # 折 (downward)

    r = w // 2
    for pt in (p1, p2, p3, p4):
        px, py = m2p(*pt)
        draw.ellipse([px - r, py - r, px + r, py + r], fill="black")


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_shu_zhe_zhe(draw, ox=0, oy=0, scale=1.0, ink=10)
    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_28_竖折折/01_竖折折.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
