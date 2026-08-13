# 响 (xiǎng) — L-R composition: 口 (left) + 向 (right).
# 向 = 丿 top-left + 冂 outer frame + 口 interior.
# Total 9 strokes. Inline PIL, thin uniform widths (MMH GT is thin).
# Reference: jiong_char.py, tong_char.py style.

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

    # ================== LEFT 口 (small, mid-lower left) ==================
    # Slot: x 25..90, y 140..225
    lx0, ly0, lx1, ly1 = 28, 145, 88, 225
    # left vertical
    draw_poly(d, [(lx0, ly0), (lx0 + 2, ly1)], [5, 5])
    # top + right (横折)
    draw_poly(
        d,
        [(lx0 - 2, ly0), (lx1 - 4, ly0 - 2), (lx1, ly0 + 5), (lx1 + 2, ly1)],
        [5, 5, 5, 5],
    )
    # bottom
    draw_poly(d, [(lx0 - 2, ly1), (lx1 + 4, ly1 - 2)], [5, 5])

    # ================== RIGHT 向 ==================
    # Slot: x 108..280, y 45..275

    # Stroke 1: top-left 丿 (short slanted, tip high, ends at frame top-left corner)
    draw_poly(d, [(155, 45), (135, 70), (118, 98)], [6, 5, 3])

    # Stroke 2: left vertical of 冂 (starts at 丿 landing, long down)
    draw_poly(d, [(118, 100), (120, 185), (118, 275)], [7, 7, 6])

    # Stroke 3: 横折钩 — top horizontal + right vertical + small hook left
    draw_poly(
        d,
        [(116, 100), (200, 92), (270, 100), (272, 185), (270, 273), (250, 278)],
        [6, 7, 7, 7, 7, 4],
    )

    # ================== Interior 口 of 向 ==================
    # Sits in the middle-lower interior of the frame, slightly narrower
    ix0, iy0, ix1, iy1 = 152, 170, 240, 250

    # inner left vertical
    draw_poly(d, [(ix0, iy0), (ix0 + 2, iy1)], [5, 5])
    # inner top + right (横折)
    draw_poly(
        d,
        [(ix0 - 3, iy0), (ix1 - 5, iy0 - 2), (ix1, iy0 + 5), (ix1 + 2, iy1)],
        [5, 5, 5, 5],
    )
    # inner bottom
    draw_poly(d, [(ix0 - 2, iy1), (ix1 + 4, iy1 - 2)], [5, 5])

    out = Path(__file__).parent / "01_响.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
