"""
G1 no-memory drawer: 竖钩 (vertical stroke with hook flicking left at the bottom).
Renders a 300x300 white PNG with a black ink stroke using PIL only.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
OUT = os.path.join(os.path.dirname(__file__), "01_竖钩.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# 竖钩: a vertical stroke that starts near the top, runs downward,
# then hooks (flicks) to the upper-left at the bottom.
# Ink: black. Stroke width tapers slightly by drawing a couple of
# overlapping segments; PIL doesn't taper natively so we approximate.

# Vertical shaft: from (150, 55) down to (150, 235)
shaft_top = (150, 55)
shaft_bottom = (150, 235)

# Hook: from shaft_bottom curving up-left, ending around (110, 205)
hook_end = (110, 200)

# Draw main vertical
draw.line([shaft_top, shaft_bottom], fill="black", width=12)

# Small entry "顿笔" (a slightly thicker top): draw an ellipse blob at top
draw.ellipse([shaft_top[0]-7, shaft_top[1]-4, shaft_top[0]+7, shaft_top[1]+8], fill="black")

# Draw hook as a short curved segment approximated by two lines
mid_hook = (135, 225)
draw.line([shaft_bottom, mid_hook], fill="black", width=12)
draw.line([mid_hook, hook_end], fill="black", width=11)

# Taper the hook tip
draw.ellipse([hook_end[0]-4, hook_end[1]-4, hook_end[0]+4, hook_end[1]+4], fill="black")

img.save(OUT)
print(f"Saved: {OUT}")
