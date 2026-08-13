"""两 (liǎng, "two") — 7 strokes.

Structure (from GT):
  1. Small top 一 (short horizontal at very top, wider than initial guess)
  2. Left long vertical (frame left)
  3. 横折钩 (top horizontal + right vertical + small hook)
  4. Inner horizontal (splits enclosed area high — around y=115)
  5. Inner-left  丿 (pie curving down-left)
  6. Inner-left  丨/丶 (short vertical inside left half)
  7. Inner-right 丿 + 丨/丶 collapsed here into two more strokes:
     right pie + right short vertical.

Total: 7 marks. No central divider — that visual line is the inner-right
short vertical touching the middle-inner horizontal.

Inline PIL per v8 signature freedom (jiong_char pattern).
Thin widths ~ MMH GT.
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

    # --- Stroke 1: top small 一 (wider, centered) ---
    draw_poly(d, [(95, 42), (205, 44)], [5, 5])

    # --- Stroke 2: left long vertical (frame left) ---
    draw_poly(d, [(60, 78), (62, 175), (58, 275)], [6, 6, 5])

    # --- Stroke 3: 横折钩 (top horizontal + right vertical + hook) ---
    draw_poly(
        d,
        [(58, 78), (150, 72), (245, 78), (247, 175), (245, 270), (225, 275)],
        [5, 6, 6, 6, 6, 3],
    )

    # --- Stroke 4: inner horizontal (splits, HIGH ~y=115) ---
    draw_poly(d, [(65, 118), (150, 115), (242, 118)], [4, 4, 4])

    # --- Stroke 5: inner-left 丿 (pie down-left) ---
    draw_poly(d, [(105, 125), (92, 190), (78, 265)], [5, 4, 3])

    # --- Stroke 6: inner-left 丨/丶 (short vertical/dot inside left half) ---
    draw_poly(d, [(138, 135), (140, 200), (140, 258)], [4, 4, 4])

    # --- Stroke 7 (split into two for visual): inner-right pie + inner-right vertical ---
    # inner-right 丿
    draw_poly(d, [(200, 125), (185, 190), (168, 265)], [5, 4, 3])
    # inner-right 丨/丶 (this is what LOOKS like a central divider in some renders)
    draw_poly(d, [(220, 135), (222, 200), (222, 258)], [4, 4, 4])

    out = Path(__file__).parent / "01_两.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
