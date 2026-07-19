"""Render radical 广 (yǎn) to a 300x300 PNG.

广 has 3 strokes:
  1) 点 (dot) — short diagonal stroke at top
  2) 横 (heng) — horizontal stroke below the dot
  3) 撇 (pie) — long left-falling stroke from the top-left of the horizontal

Uses PIL for clean anti-aliased strokes.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = (0, 0, 0)
BG = (255, 255, 255)


def draw_stroke(draw, points, width_start, width_end=None, steps=40):
    """Draw a variable-width stroke by interpolating circles along a polyline."""
    if width_end is None:
        width_end = width_start
    # Interpolate points along the polyline
    total_len = 0
    seg_lens = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        seg_lens.append(d)
        total_len += d
    if total_len == 0:
        return
    for s in range(steps + 1):
        t = s / steps
        target = t * total_len
        acc = 0
        for i, d in enumerate(seg_lens):
            if acc + d >= target or i == len(seg_lens) - 1:
                local_t = (target - acc) / d if d > 0 else 0
                x0, y0 = points[i]
                x1, y1 = points[i + 1]
                x = x0 + local_t * (x1 - x0)
                y = y0 + local_t * (y1 - y0)
                break
            acc += d
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Stroke 1: 点 (dot) — short diagonal from upper-left going down-right
    # Positioned in upper-middle area
    dot_pts = [(120, 65), (145, 85)]
    draw_stroke(draw, dot_pts, width_start=5, width_end=8, steps=20)

    # Stroke 2: 横 (horizontal) — from left near dot, extending right
    # Starts around x=110, ends around x=225, y around 110
    heng_pts = [(110, 115), (225, 108)]
    draw_stroke(draw, heng_pts, width_start=6, width_end=5, steps=30)

    # Stroke 3: 撇 (pie / left-falling) — starts at top-left corner of the 横,
    # curves down and to the left, ending near bottom-left.
    # Anchored at ~ (115, 110), curving to ~ (65, 260)
    pie_pts = [
        (118, 108),
        (110, 140),
        (100, 175),
        (88, 210),
        (75, 240),
        (62, 265),
    ]
    draw_stroke(draw, pie_pts, width_start=7, width_end=4, steps=60)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_广.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
