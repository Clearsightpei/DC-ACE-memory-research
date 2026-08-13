from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 5

# 过 = 辶 (walk radical, wraps left/bottom) + 寸 (right-upper component)

# --- Right component: 寸 ---
# Horizontal stroke (top of 寸)
d.line([(150, 90), (250, 90)], fill=BLACK, width=LW)
# Vertical hook stroke going down from horizontal, with left hook at bottom
d.line([(200, 75), (200, 175)], fill=BLACK, width=LW)
# Little hook at bottom
d.line([(200, 175), (185, 170)], fill=BLACK, width=LW)
# Dot (点) on the right side
d.line([(215, 130), (235, 145)], fill=BLACK, width=LW)

# --- Left/bottom: 辶 (walk radical) ---
# Top dot
d.line([(85, 70), (100, 85)], fill=BLACK, width=LW)
# Middle short stroke (like a small hook / horizontal-turn)
d.line([(60, 115), (110, 115)], fill=BLACK, width=LW)
d.line([(110, 115), (95, 145)], fill=BLACK, width=LW)
# The long horizontal 捺 sweep at bottom (rises to right)
# small curve down on left, then long sweep bottom-right
d.line([(70, 175), (85, 205)], fill=BLACK, width=LW)
d.line([(85, 205), (75, 235)], fill=BLACK, width=LW)
# Long horizontal sweep
d.line([(50, 245), (260, 245)], fill=BLACK, width=LW)
# Slight upward tick at right end
d.line([(260, 245), (275, 235)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_过.png")
img.save(out)
print(f"wrote {out}")
