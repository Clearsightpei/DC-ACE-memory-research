from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def wavy_stroke(x_top, x_bot_shift=10):
    """Draw a curved stroke: small hook at top, curves down and to the right slightly."""
    # top small hook (short diagonal)
    hook_start = (x_top - 6, 105)
    hook_end = (x_top + 2, 115)
    draw.line([hook_start, hook_end], fill="black", width=3)
    # main body - S curve going down (like a "<" then straight down-right)
    pts = []
    import math
    for i in range(61):
        t = i / 60.0
        # y from ~115 to ~240
        y = 115 + t * 125
        # x: curves left (bulging out to left) in upper-mid, straightens and slightly right at bottom
        # Approx: cubic-like — left bulge peak around t=0.35
        x = x_top + 2 - 22 * math.sin(t * math.pi * 0.75) + t * 14
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill="black", width=3)

# Three strokes evenly spaced
wavy_stroke(110)
wavy_stroke(160)
wavy_stroke(210)

out = os.path.join(os.path.dirname(__file__), "01_巛.png")
img.save(out)
print(out)
