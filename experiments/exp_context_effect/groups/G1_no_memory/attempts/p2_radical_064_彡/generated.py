"""Render 彡 (radical, 3 strokes) at 300x300 using PIL.

彡 is three descending 撇 (pie) strokes with pronounced curvature —
each has a small hook/head at upper-right, curves down and to the
left, and tapers at the tail. The three strokes stack top-to-bottom
with the bottom stroke being the longest.
"""

from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def curved_pie(draw, x0, y0, x1, y1, head_size=5, mid_width=6, bulge=30):
    """A calligraphic 撇: small head hook at (x0,y0), sweeping curved
    body ending at (x1,y1) with tapered tail. Curve bulges to the
    right (outward from an S-like bow)."""
    # Draw a small head hook (small filled shape at start)
    r = head_size
    draw.ellipse([x0 - r, y0 - r * 0.6, x0 + r * 0.6, y0 + r], fill="black")

    # Quadratic Bezier control point pushed to right of chord
    dx = x1 - x0
    dy = y1 - y0
    length = math.hypot(dx, dy)
    if length == 0:
        return
    # Normal pointing to the "right" of down-left travel direction
    # For a stroke going down-left (dx<0, dy>0), right-normal is (-dy, dx) direction
    # which points down-right — we want bulge to the RIGHT side (outer arc)
    nx = -dy / length
    ny = dx / length
    # We want the curve to bow to the right (upper-right side), so push
    # control point along +normal
    cx = (x0 + x1) / 2 + nx * bulge
    cy = (y0 + y1) / 2 + ny * bulge

    segments = 60
    prev = (x0, y0)
    for i in range(1, segments + 1):
        t = i / segments
        bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
        by = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
        # Taper: thick just after head, thin at tail
        # Width profile: rises to peak around t=0.15, tapers to ~1 at t=1
        if t < 0.15:
            w = mid_width * (0.5 + t / 0.15 * 0.5)
        else:
            w = mid_width * (1.0 - (t - 0.15) / 0.85 * 0.85)
        w = max(1.2, w)
        draw.line([prev, (bx, by)], fill="black", width=int(round(w)))
        rr = w / 2
        draw.ellipse([bx - rr, by - rr, bx + rr, by + rr], fill="black")
        prev = (bx, by)


# Three curved 撇 stacked vertically. From GT:
# - Strokes are fairly steep (more vertical than 45 deg)
# - Each has a visible head hook at top-right
# - Body curves noticeably (bows to the right)
# - Bottom stroke is the longest and reaches lowest

# Stroke 1 (top-right small)
curved_pie(draw, x0=185, y0=65, x1=145, y1=125, head_size=5, mid_width=6, bulge=18)

# Stroke 2 (middle)
curved_pie(draw, x0=180, y0=125, x1=130, y1=185, head_size=5, mid_width=6, bulge=20)

# Stroke 3 (bottom, longest)
curved_pie(draw, x0=180, y0=175, x1=100, y1=255, head_size=6, mid_width=7, bulge=28)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_彡.png")
img.save(out_path)
print(f"Saved {out_path}")
