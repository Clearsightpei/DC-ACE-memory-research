"""p2_radical_011_匕 (bǐ) — retry_4. G3 coord-bank render.

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata says 撇 must terminate EXACTLY on the shu-wan-gou
#   shaft, not float above/across it. Prior retries had the 撇 slanting
#   across the whole figure or the crossing point wrong.
# Q2 (form_catalog): 撇 in top-of-envelope role (short, near-vertical),
#   shu_wan_gou as body envelope. Also 匕's 2nd stroke starts with a
#   small right-down slant at the top before descending.
# Q3 (helpers): Under v8, trust GT over helpers. GT contradicts the
#   bank shu_wan_gou (which is a big envelope). Inline both strokes
#   with hand-tuned PIL polylines to match GT exactly.

GT observation (pixels, 300x300):
  Stroke 1 (撇): from ~(118, 88) down-left to ~(88, 195). Short, mostly
    vertical, slight left lean.
  Stroke 2 (竖弯钩): starts top at ~(130, 130), goes right-and-down
    slightly to ~(185, 148) [top intro segment], then curves down and
    left into a vertical shaft descending to ~(120, 255), then curves
    right along bottom to ~(215, 258), then hooks up to ~(215, 215).

  The 撇 CROSSES the top intro segment of stroke 2 around (128, 130).
"""

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300
OUT = Path(__file__).parent / "01_匕.png"


def stroke_polyline(d, points, width=6, fill=(0, 0, 0)):
    d.line(points, fill=fill, width=width, joint="curve")
    # rounded caps
    r = width / 2
    for (x, y) in (points[0], points[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def draw_pie_inline(d):
    """Stroke 1: short 撇 down-left, near vertical."""
    pts = [(120, 88), (112, 118), (102, 155), (90, 195)]
    stroke_polyline(d, pts, width=6)


def draw_shu_wan_gou_inline(d):
    """Stroke 2: top intro slant → vertical shaft → bottom curve → hook up."""
    # top intro: starts at (132, 130) slanting slightly down-right to (185, 148)
    intro = [(132, 130), (150, 137), (168, 143), (185, 148)]
    # BUT — after the intro tip, the stroke continues down forming a shaft.
    # In 匕, the second stroke is actually one continuous stroke that starts
    # at top, then IMMEDIATELY curves down/left into the shaft. The intro
    # segment IS the top of the shaft (a slight right-lean at top).
    # Body: continues from ~intro-mid down into the vertical shaft.
    body_top_x = 128  # shaft x position
    body = [
        (185, 148),   # end of intro
        (170, 155),
        (152, 175),
        (140, 200),
        (132, 225),
        (128, 250),   # bottom of shaft
    ]
    # Actually re-read GT: the top intro extends right, then the shaft is on
    # the LEFT side (around x=118). The intro is short — the shaft starts
    # at the left end of intro. Rewrite:
    # Stroke 2 is one continuous line. It starts at top-right at (185, 148),
    # curves smoothly down-left into the vertical shaft, descends, then
    # curves right along the bottom, then hooks up. No sharp peak at top.
    full = [
        (185, 148),   # top-right start
        (170, 152),
        (150, 158),
        (135, 168),   # smooth curve into shaft
        (125, 185),
        (118, 210),
        (116, 240),   # bottom of vertical shaft
        (122, 258),
        (145, 268),
        (180, 270),
        (210, 268),
        (220, 258),   # right side of bottom curve
        (222, 240),
        (218, 218),   # hook tip going up
    ]
    stroke_polyline(d, full, width=6)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shu_wan_gou_inline(d)
    draw_pie_inline(d)
    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
