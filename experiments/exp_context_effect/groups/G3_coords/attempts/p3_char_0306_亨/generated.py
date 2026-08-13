"""亨 (hēng) — 7 strokes.

Decomposition:
  1. 点 (top dot)
  2. 横 (long heng — lid of 亠)
  3. 竖 (口 left)
  4. 横折 (口 top-right, top + right vertical)
  5. 横 (口 bottom)
  6. 横 (short-medium heng below 口)
  7. 弯钩/竖钩 (descender: starts from right, curves down-left, hooks left)

Layout follows GT: dot top center, long heng slightly below, small 口 mid,
horizontal below 口, curved hook descender from right-of-center down-left.
v8: direct PIL rendering with tapered lines.
"""
from PIL import Image, ImageDraw
from pathlib import Path


def draw_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def draw_poly(draw, points, widths, steps_per_seg=30):
    for i in range(len(points) - 1):
        draw_line(draw, points[i], points[i + 1], widths[i], widths[i + 1], steps=steps_per_seg)


def render():
    img = Image.new("L", (300, 300), 255)
    d = ImageDraw.Draw(img)

    # --- Stroke 1: 点 (top dot) ---
    draw_poly(d, [(147, 28), (155, 42)], [4, 10])

    # --- Stroke 2: 长横 (long heng, lid) ---
    # Slight rise then dip, subtle 顿笔 at ends.
    draw_poly(d, [(35, 78), (150, 72), (265, 76)], [6, 6, 8])

    # --- Small 口 (strokes 3, 4, 5) ---
    # Box roughly x=110..195, y=100..150
    # Stroke 3: 竖 (left vertical)
    draw_poly(d, [(112, 102), (113, 152)], [6, 6])

    # Stroke 4: 横折 (top + right vertical)
    draw_poly(d, [(109, 100), (155, 97), (198, 102), (196, 152)], [5, 5, 6, 6])

    # Stroke 5: 横 (bottom of 口)
    draw_poly(d, [(110, 150), (155, 148), (198, 151)], [5, 5, 5])

    # --- Stroke 6: 横 (horizontal below 口) ---
    draw_poly(d, [(58, 188), (150, 184), (243, 187)], [5, 6, 7])

    # --- Stroke 7: 弯钩 (curved hook descender) ---
    # Starts at upper right (just below stroke 6), curves down and left,
    # ends with small hook flick to the left.
    pts = [
        (178, 190),
        (170, 215),
        (158, 240),
        (140, 260),
        (120, 268),
        (108, 262),
    ]
    widths = [7, 7, 6, 6, 5, 4]
    draw_poly(d, pts, widths, steps_per_seg=25)

    out = Path(__file__).parent / "01_亨.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
