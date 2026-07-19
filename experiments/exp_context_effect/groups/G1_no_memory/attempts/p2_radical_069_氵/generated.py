"""G1 attempt: 氵 (three-drops-of-water radical, 3 strokes).

Layout (from GT):
  - Stroke 1: upper dot (点) — small comma-like stroke top-right area
  - Stroke 2: middle dot (点) — small comma-like stroke, slightly left
    and below the first
  - Stroke 3: bottom rising stroke (提) — starts lower-left, rises up
    to the right

All strokes sit on the LEFT half of a character-cell (radicals occupy
left side). We render into a 300x300 PNG, white bg, black ink.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
OUT = os.path.join(os.path.dirname(__file__), "01_氵.png")


def draw_dot(draw, path_points, widths):
    """Draw a tapered comma-like dot along path_points with per-segment widths."""
    for i in range(len(path_points) - 1):
        x1, y1 = path_points[i]
        x2, y2 = path_points[i + 1]
        w = widths[i]
        draw.line([(x1, y1), (x2, y2)], fill="black", width=w)
    # cap start/end with small circles
    x, y = path_points[0]
    r = max(widths[0] // 2, 2)
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
    x, y = path_points[-1]
    r = max(widths[-1] // 2, 2)
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def main():
    img = Image.new("RGB", (SIZE, SIZE), "white")
    draw = ImageDraw.Draw(img)

    # Stroke 1: upper dot (点) — top-right of the radical column
    # A downward-curving comma from upper-left to lower-right, then
    # a tiny hook. Position: around x=140..175, y=70..105.
    s1 = [(140, 70), (155, 82), (170, 98), (175, 108)]
    w1 = [5, 6, 7]
    draw_dot(draw, s1, w1)

    # Stroke 2: middle dot (点) — slightly left of s1, lower
    # Position: around x=110..145, y=125..160.
    s2 = [(115, 130), (128, 142), (142, 155)]
    w2 = [5, 6]
    draw_dot(draw, s2, w2)

    # Stroke 3: rising stroke (提) — bottom. Starts as a short downward
    # curve on the lower-left, then rises up to the right (like a
    # comma flipped, or a check-mark). Matches GT shape.
    s3 = [(115, 205), (112, 220), (115, 235), (125, 250), (140, 255),
          (155, 245), (170, 230)]
    w3 = [5, 6, 7, 8, 7, 5]
    draw_dot(draw, s3, w3)

    img.save(OUT)
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
