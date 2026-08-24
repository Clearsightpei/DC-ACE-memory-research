"""
Render 入 (rù) — 2 strokes: 撇 + 捺.

Sibling insight (form_catalog.md):
  人 vs 入: 人's strokes meet at same apex; 入's 捺 starts HIGHER on the 撇
           and OVERHANGS to the upper-left (visible short stub).

Revision (v2, against clean GT):
- Widen stance: 撇 foot near (50, 270), 捺 foot near (255, 260).
- 撇 curves noticeably (concave to upper-right), not near-vertical.
- 捺 overhang stub is clearly visible above meeting point.
- Character is slightly wider than tall.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    """Draw a stroke as a chain of circles, width interpolated along path."""
    n = len(points)
    if n < 2:
        return
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dist = max(1, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for t_step in range(dist + 1):
            t = t_step / dist
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ---- Stroke 1: 撇 — starts upper-mid, sweeps down with strong leftward curve.
# Concave to the upper-right (bows out to the left). Ends far lower-left.
pie_pts = [
    (158, 65),
    (152, 95),
    (142, 128),
    (128, 160),
    (108, 195),
    (82, 230),
    (58, 260),
    (48, 275),
]
pie_widths = [13, 13, 12, 11, 10, 8, 5, 3]
brush_stroke(pie_pts, pie_widths)

# ---- Stroke 2: 捺 — overhang stub starts up-left of meeting point,
# then sweeps down-right with broadening foot.
# Meeting on 撇 approximately (145, 118). Stub tip around (128, 90).
na_pts = [
    (128, 88),   # overhang tip, clearly above meeting
    (135, 100),
    (145, 118),  # meeting the 撇
    (165, 145),
    (188, 175),
    (212, 205),
    (235, 232),
    (255, 258),  # broad foot lower-right
    (268, 268),
]
na_widths = [3, 5, 7, 9, 11, 13, 15, 14, 8]
brush_stroke(na_pts, na_widths)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0029_入/01_入.png"
img.save(out_path)
print(f"Wrote {out_path}")
