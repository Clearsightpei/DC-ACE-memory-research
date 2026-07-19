"""p2_radical_055_彑 — G3 (coord-bank) first attempt.

彑 is a 3-stroke radical (pinyin: jì). Structure inferred from GT PNG:
  1. Upper-right piece: a small 撇 that descends from top-right, curving
     slightly down-left — reads as the compact top of the radical.
  2. Middle 横折: starts at mid-left, horizontal right, then bends down
     to a short vertical (forms the middle staircase).
  3. Bottom 横: long horizontal spanning the width, slightly rising
     right — the base of the radical.

Design approach (per TR5/P7 guidance): the shapes are simple enough
that inlining tapered lines with PIL is cleaner than bank primitive
transforms — no bank primitive is a good match for the small "hook"
top-piece of 彑 without extreme scale. Draw fresh.

Canvas: 300x300, white bg, black ink. Math coords converted to PIL.
"""

from PIL import Image, ImageDraw

CANVAS = 300
CX = CANVAS / 2
CY = CANVAS / 2


def to_px(x, y):
    """math-coord (center origin, +y up) -> PIL pixel."""
    return (CX + x, CY - y)


def draw_tapered_line(t, p0, p1, w0, w1, steps=40):
    """Stamped-circle taper from width w0 at p0 to w1 at p1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = max(0.5, w / 2.0)
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_polyline(t, pts, width):
    """Straight lines with rounded joints."""
    for i in range(len(pts) - 1):
        t.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=width)
    r = width // 2
    for (x, y) in pts:
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # ---- Stroke 1: upper 撇-like drop from top-right ----
    # In GT: a longer descending piece from top curving slightly left.
    # From about (+10, +75) down to (-2, +20). Tapered.
    s1_head = to_px(+12, +75)
    s1_tail = to_px(-2, +20)
    draw_tapered_line(t, s1_head, s1_tail, w0=10, w1=5, steps=40)

    # ---- Stroke 2: 横折 middle staircase (compact, centered) ----
    # Left-middle horizontal → down → short left stub to make inner tick.
    # Compact so it sits inside the character silhouette.
    p2a = to_px(-55, +18)
    p2b = to_px(+22, +18)
    p2c = to_px(+22, -18)
    p2d = to_px(-25, -18)
    draw_polyline(t, [p2a, p2b, p2c, p2d], width=8)

    # ---- Stroke 3: long bottom 横 (slightly rising toward right) ----
    # Spans nearly full width; slight upward tilt (right end higher).
    s3_left = to_px(-110, -55)
    s3_right = to_px(+115, -48)
    draw_tapered_line(t, s3_left, s3_right, w0=8, w1=8, steps=60)
    # end caps
    r = 4
    for (x, y) in (s3_left, s3_right):
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    return img


if __name__ == "__main__":
    img = render()
    out = __file__.rsplit("/", 1)[0] + "/01_彑.png"
    img.save(out)
    print("wrote", out)
