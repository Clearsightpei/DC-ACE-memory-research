"""Render 师 (shī) at 300x300, white background, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# ---- LEFT component (like a small 丨 + long 丿) ----
# Short vertical dot/stroke upper-left
d.line([(85, 100), (85, 155)], fill=BLACK, width=LW)

# Long left-sweeping curve (丿) starting upper-right of left component
pts = []
for t in range(0, 101):
    tt = t / 100.0
    x = 115 - 55 * tt - 10 * (tt ** 2)  # sweep from x=115 down to ~50
    y = 90 + 175 * tt                   # sweep from y=90 to y=265
    pts.append((x, y))
d.line(pts, fill=BLACK, width=LW)

# ---- RIGHT component (帀-like: top-heng, short vert, then 巾-like frame) ----
# Top horizontal (long, slightly rising)
d.line([(140, 95), (260, 90)], fill=BLACK, width=LW)

# Short vertical from top horizontal downward (top-right)
d.line([(220, 90), (220, 130)], fill=BLACK, width=LW)

# Middle horizontal (top of the 巾-frame)
d.line([(160, 135), (255, 135)], fill=BLACK, width=LW)

# Left vertical of frame (short, angled slightly inward at top)
d.line([(160, 135), (160, 215)], fill=BLACK, width=LW)

# Right vertical of frame with hook at bottom
d.line([(255, 135), (255, 220)], fill=BLACK, width=LW)
# small hook to the left at bottom of right vertical
d.line([(255, 220), (243, 213)], fill=BLACK, width=LW)

# Long central descender (巾's central vertical) going down past the frame
d.line([(205, 135), (205, 270)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0285_师/01_师.png")
print("saved")
