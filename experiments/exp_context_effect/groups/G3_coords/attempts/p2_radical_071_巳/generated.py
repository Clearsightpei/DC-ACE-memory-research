# generated.py — 巳 (sì) radical, 3 strokes.
# G3 coord-format attempt. Following TR8 (inline-fresh test): 巳 is
# close in shape to 己 (which FAILed in B1), so the sandbox lesson is
# to INLINE fresh with hand-tuned tapered polylines rather than
# force-fit heng_zhe / shu_wan_gou primitives.
#
# Stroke plan (300x300 canvas, PIL, math-coord convention via center):
#   S1 横折  : top horizontal from TL(85, 90)→TR(185, 90), then a
#              short shoulder turning down to (185, 130).
#   S2 横    : middle horizontal from (85, 130) → (185, 130),
#              closing the top box.
#   S3 竖弯钩: from TL(85, 90) descending to (85, 210), then
#              sweeping right to (205, 210), tiny hook flick up.
#
# Widths follow P4: heng-like ~11 px, shu-like ~11 px, hook taper
# to ~2 px.

import os
from PIL import Image, ImageDraw

W, H = 300, 300
INK = (0, 0, 0)
BG = (255, 255, 255)


def tapered_line(draw, p0, p1, w0, w1, steps=40):
    """Draw a straight tapered line as a series of overlapping circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    """Quadratic bezier with a width ramp."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def dot_blob(draw, cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK)


def draw_si(img):
    d = ImageDraw.Draw(img)

    # ---- S1: 横折 (top horizontal + shoulder down) ----
    # Wider than v1: TL(70, 85) → TR(200, 85), shoulder to (200, 130).
    tapered_line(d, (70, 85), (200, 85), 9, 12)
    # Small 顿笔 blob at the corner (P6).
    dot_blob(d, 200, 87, 7)
    # Shoulder going down.
    tapered_line(d, (200, 87), (200, 130), 12, 10)

    # ---- S2: 横 (middle closing horizontal) ----
    # From (95, 130) → (200, 130). Starts slightly inside the left
    # descender (matches GT — GT's middle horizontal doesn't fully
    # reach the left edge).
    tapered_bezier(d, (95, 130), (145, 128), (200, 130), 9, 11)

    # ---- S3: 竖弯钩 (long descender + horizontal sweep + hook) ----
    # Vertical descender from top-left: (70, 85) → (70, 210).
    tapered_line(d, (70, 85), (70, 210), 11, 12)
    # 弯 sweep: bezier arcing from (70, 210) around through
    # (95, 225) out to (200, 220), then continue straight.
    tapered_bezier(d, (70, 210), (95, 228), (180, 220), 12, 11)
    tapered_line(d, (180, 220), (215, 217), 11, 9)
    # 顿笔 at hook root.
    dot_blob(d, 215, 217, 6)
    # Hook flick UP (slightly left) per P1.
    tapered_line(d, (215, 217), (208, 197), 9, 2)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw_si(img)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_巳.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
