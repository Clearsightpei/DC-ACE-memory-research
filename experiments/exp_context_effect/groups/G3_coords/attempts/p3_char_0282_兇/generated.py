# p3_char_0282_兇 — G3 attempt
# 兇 = 凶 (top: 乂 inside 凵) + 儿 (bottom).
# Fresh inline rendering — GT shows thin uniform strokes (MMH style).
# The er_ren bank primitive uses calligraphic widths that are too heavy
# vs the GT's thin lines; per v8 "trust GT" we hand-render with thin ink.

from PIL import Image, ImageDraw

CANVAS = 300
INK = 5  # thin, MMH-like
CX = CY = CANVAS / 2


def M(x, y):
    """Math coords (center origin, y up) -> pixel coords."""
    return (CX + x, CY - y)


def line(d, p1, p2, w=INK):
    d.line([M(*p1), M(*p2)], fill=(0, 0, 0), width=w)
    # end caps
    for (x, y) in (p1, p2):
        px, py = M(x, y)
        r = w / 2
        d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def poly(d, pts, w=INK):
    px_pts = [M(*p) for p in pts]
    d.line(px_pts, fill=(0, 0, 0), width=w, joint="curve")
    for (x, y) in (pts[0], pts[-1]):
        px, py = M(x, y)
        r = w / 2
        d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_xiong(d):
    """Top: 凶 = 乂 inside 凵. Bottom: 儿."""

    # ---- 凶 (top half, y roughly +130 down to +5) ----
    # 乂 crossing strokes centered near (0, +75), spans y +130 to +20
    # 撇: from top-right to bottom-left
    line(d, (35, 130), (-40, 25))
    # 捺-like: from top-left to bottom-right
    line(d, (-30, 130), (45, 25))

    # 凵 U-shape enclosing the 乂. Opens upward. Sits around y +100 down to +5
    # Left vertical
    line(d, (-70, 105), (-70, 5))
    # Bottom horizontal
    line(d, (-70, 5), (70, 5))
    # Right vertical
    line(d, (70, 105), (70, 5))

    # ---- 儿 (bottom half, y +0 down to -125) ----
    # 撇 left leg: from top (around x=-30, y=0) curving down-left to (-95, -125)
    poly(d, [(-30, 0), (-45, -50), (-70, -90), (-95, -125)])

    # 竖弯钩 right leg: from top (x=30, y=0) down then curving right, ending with tick up
    # shaft down
    poly(d, [(35, 0), (35, -80),
             # bottom curve to the right
             (45, -110), (75, -125), (105, -125),
             # small hook tick up
             (105, -105)])


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_xiong(d)
    img.save("01_兇.png")


if __name__ == "__main__":
    main()
