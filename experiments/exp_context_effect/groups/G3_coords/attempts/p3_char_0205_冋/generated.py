"""冋 (jiong) — a 冂 frame enclosing a small 口 at the upper interior.

Stroke plan (5 strokes):
  1. Left vertical (long, slight lean, calligraphic width)
  2. 横折钩 — top horizontal + right vertical with small hook at bottom
  3. Inner 口 — left vertical (small)
  4. Inner 口 — top + right (横折)
  5. Inner 口 — bottom horizontal

Uses PIL directly per v8 signature freedom.
"""
from PIL import Image, ImageDraw
from pathlib import Path


def draw_line(draw, p0, p1, w0, w1, steps=40):
    """Tapered stroke from p0 (width w0) to p1 (width w1)."""
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
    """Sequential tapered segments through a polyline."""
    for i in range(len(points) - 1):
        draw_line(draw, points[i], points[i + 1], widths[i], widths[i + 1], steps=steps_per_seg)


def render():
    img = Image.new("L", (300, 300), 255)
    d = ImageDraw.Draw(img)

    # --- Outer frame 冂 ---
    # Stroke 1: left vertical — starts high-left, ends bottom-left with slight bend outward
    draw_poly(d, [(70, 60), (72, 170), (70, 260)], [7, 7, 6])

    # Stroke 2: 横折钩 — top horizontal from ~(68,60) to (230,55), turn down to (232,255),
    # small hook to the left at the bottom.
    # Use three segments: top horizontal, right vertical, hook.
    draw_poly(
        d,
        [(66, 58), (150, 52), (232, 58), (234, 165), (232, 258), (215, 265)],
        [6, 7, 7, 7, 7, 4],
    )

    # --- Inner 口 (small, upper-middle interior) ---
    # Roughly a small rectangle around (110..190) x (120..180)
    ix0, iy0, ix1, iy1 = 115, 130, 195, 185

    # Stroke 3: inner-left vertical
    draw_poly(d, [(ix0, iy0), (ix0 + 2, iy1)], [5, 5])

    # Stroke 4: inner top + right (横折) — starts at ix0, iy0, across to ix1, down to iy1
    draw_poly(
        d,
        [(ix0 - 3, iy0), (ix1 - 5, iy0 - 2), (ix1, iy0 + 5), (ix1 + 2, iy1)],
        [5, 5, 5, 5],
    )

    # Stroke 5: inner bottom horizontal
    draw_poly(d, [(ix0 - 2, iy1), (ix1 + 4, iy1 - 2)], [5, 5])

    out = Path(__file__).parent / "01_冋.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
