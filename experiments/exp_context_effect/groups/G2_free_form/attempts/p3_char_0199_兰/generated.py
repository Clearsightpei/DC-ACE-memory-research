"""Render 兰 (lán) — 5 strokes total.

Layout (top-to-bottom):
  1. 丶 (dot) — left top, slight downward-inward slant
  2. 丶 (dot) — right top, slight downward-inward slant (mirrored)
  3. 一 (short horizontal) — upper
  4. 一 (medium horizontal) — middle
  5. 一 (long horizontal) — bottom (longest, foot of the char)

Increasing width top-down for the 3 横. Two top dots form 丷 pattern.
Standard 3-horizontal stacked layout beneath.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def brush_line(p0, p1, width=10):
    """Draw a smooth thick line with rounded ends."""
    d.line([p0, p1], fill=INK, width=width)
    # rounded end caps
    r = width / 2
    d.ellipse([p0[0]-r, p0[1]-r, p0[0]+r, p0[1]+r], fill=INK)
    d.ellipse([p1[0]-r, p1[1]-r, p1[0]+r, p1[1]+r], fill=INK)

# --- Two top dots (丷) ---
# Left dot: slants down-right (like a small 撇 that goes down-right? Actually
# in 兰 the left dot is 点 slanting down-inward toward center)
# Looking at GT: left mark slants down-right, right mark slants down-left,
# forming a small V-like opening at top center.
brush_line((115, 70), (135, 100), width=9)   # left dot: down-right
brush_line((190, 70), (170, 100), width=9)   # right dot: down-left

# --- Three horizontals (increasing width) ---
# Upper 横: shortest, ~120px
brush_line((90, 135), (215, 135), width=9)

# Middle 横: medium, ~140px
brush_line((80, 180), (225, 180), width=9)

# Bottom 横: longest, ~220px, sits at foot of grid
brush_line((45, 235), (265, 235), width=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0199_兰/01_兰.png")
