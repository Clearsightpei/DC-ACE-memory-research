"""p2_radical_087_灬 — four fire-dots along the bottom.

灬 is four small dots in a row occupying roughly the lower third of the
canvas. From the GT:
  - Dot 1 (leftmost): a 左点/反点 — head at upper-right, tail at lower-left.
  - Dots 2, 3 (middle): small, nearly vertical dots slightly leaning right.
  - Dot 4 (rightmost): a larger standard 点 — head at upper-left, tail at
    lower-right; the tallest of the four.

Bank dian is tuned for standalone size (~40 px) and only draws the
upper-left→lower-right direction. For 灬 we need one mirrored dot plus
three smaller dots at very small scale, so per TR5 (extreme scale/
mirroring) we INLINE small tapered beziers instead of stretching the
primitive. Coords are pixel PIL (top-left origin, +y down).
"""

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _dot(t, head, tail, ctrl, w_head, w_tail, n=30):
    """Small tapered bezier stroke from head to tail.

    Thickness grows from w_head at the head to w_tail at the tail
    (dots are heavier at the tail side, like 点)."""
    x0, y0 = head
    x1, y1 = tail
    mx, my = ctrl
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head * (1 - u) + w_tail * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def render():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Baseline (bottom of the dots) around y=225; heads sit around y=195.
    # Four dots spaced across roughly x=90 .. x=225.

    # Dot 1: 左点 (reversed) — head upper-RIGHT, tail lower-LEFT.
    # Head at (108, 195), tail at (92, 225). Slight left-down bow.
    _dot(t,
         head=(108, 195),
         tail=(92, 225),
         ctrl=(104, 212),
         w_head=2.0, w_tail=6.5,
         n=30)

    # Dot 2: small near-vertical dot, slight right lean.
    # Head (139, 200), tail (144, 224).
    _dot(t,
         head=(139, 200),
         tail=(146, 224),
         ctrl=(141, 213),
         w_head=2.0, w_tail=5.5,
         n=30)

    # Dot 3: mirror pair of dot 2, slightly right of center.
    _dot(t,
         head=(170, 200),
         tail=(178, 224),
         ctrl=(173, 213),
         w_head=2.0, w_tail=5.5,
         n=30)

    # Dot 4: rightmost, tallest — proper 点 shape (upper-left → lower-right).
    # Head (200, 192), tail (228, 226). Slight lower-left bow.
    _dot(t,
         head=(200, 192),
         tail=(228, 226),
         ctrl=(210, 214),
         w_head=2.0, w_tail=8.0,
         n=40)

    return img


if __name__ == "__main__":
    import os
    img = render()
    out = os.path.join(os.path.dirname(__file__), "01_灬.png")
    img.save(out)
    print(f"wrote {out}")
