"""G1 render of 人 (person) — two strokes: 撇 + 捺.

The GT shows a piě (left-falling) that curves gently, starting near
top-center with a small hook and tapering to a fine tip at lower-left,
and a nà (right-falling) that starts partway down the piě, sweeps to
lower-right and ends with a thickened foot.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def taper_curve(draw, pts, widths, sub=30):
    """Draw a stroke that follows a polyline `pts` with widths at each
    vertex, using overlapping filled discs for a smooth tapered look."""
    assert len(pts) == len(widths)
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(sub + 1):
            t = s / sub
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# --- Stroke 1: 撇 (piě), left-falling with gentle curve ---
pie_pts = [
    (152, 68),    # small hook start (top)
    (150, 82),
    (145, 105),
    (133, 140),
    (115, 180),
    (92, 220),
    (65, 258),    # fine tip at lower-left
]
pie_widths = [4, 6, 6, 6, 5, 4, 2]
taper_curve(d, pie_pts, pie_widths)

# --- Stroke 2: 捺 (nà), right-falling, thickens to foot ---
# In GT, the nà begins partway down the piě (below the top).
na_pts = [
    (150, 130),   # joint below the piě's top
    (168, 158),
    (190, 190),
    (215, 220),
    (245, 250),   # foot (thickened)
    (260, 258),   # small tail lift
]
na_widths = [3, 4, 5, 6, 8, 3]
taper_curve(d, na_pts, na_widths)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_人.png"))
print("wrote", os.path.join(out_dir, "01_人.png"))
