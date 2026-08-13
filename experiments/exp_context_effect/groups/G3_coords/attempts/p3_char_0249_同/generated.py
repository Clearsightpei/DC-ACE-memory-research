"""同 (tóng) — 冂 frame with interior 一 near top and interior 口 at bottom.

Adapted from jiong_char.py (冋), which is 冂 + interior 口 at top.
For 同: keep outer frame, replace top-interior 口 with a single 一 (heng),
add a full 口 at the bottom interior.

Stroke plan (6 strokes):
  1. Outer left vertical (long)
  2. Outer 横折钩 — top horizontal + right vertical + small left-hook
  3. Interior 一 (heng, upper-middle)
  4. Inner-口 left vertical
  5. Inner-口 横折 (top + right)
  6. Inner-口 bottom horizontal

v8 signature freedom: direct PIL rendering.
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

    # --- Outer frame 冂 ---
    # Stroke 1: left vertical, slight lean outward at bottom
    draw_poly(d, [(65, 58), (67, 170), (65, 265)], [7, 7, 6])

    # Stroke 2: 横折钩 — top horizontal, right vertical, small hook left at bottom
    draw_poly(
        d,
        [(62, 55), (150, 50), (238, 56), (240, 165), (238, 262), (218, 268)],
        [6, 7, 7, 7, 7, 4],
    )

    # --- Interior 一 (upper-middle horizontal) ---
    # Sits roughly y~118, spans x~110 to x~200 (inside the frame)
    draw_poly(d, [(108, 122), (155, 118), (205, 122)], [5, 5, 5])

    # --- Inner 口 (bottom interior) ---
    ix0, iy0, ix1, iy1 = 112, 175, 205, 240

    # Stroke 4: inner-left vertical
    draw_poly(d, [(ix0, iy0), (ix0 + 2, iy1)], [5, 5])

    # Stroke 5: inner top + right (横折)
    draw_poly(
        d,
        [(ix0 - 3, iy0), (ix1 - 5, iy0 - 2), (ix1, iy0 + 5), (ix1 + 2, iy1)],
        [5, 5, 5, 5],
    )

    # Stroke 6: inner bottom horizontal
    draw_poly(d, [(ix0 - 2, iy1), (ix1 + 4, iy1 - 2)], [5, 5])

    out = Path(__file__).parent / "01_同.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
