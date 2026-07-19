"""G1 render of 扌 (提手旁, 3 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 6  # stroke thickness

# Layout: character centered roughly x=110..180 (radicals often occupy left column,
# but GT shows it centered). GT ranges roughly y=80..230, x=105..190.

# Stroke 1: 横 (short horizontal), slightly rising left-to-right
# From GT: horizontal top segment, small
s1_start = (115, 105)
s1_end   = (175, 95)
draw.line([s1_start, s1_end], fill=INK, width=TH)

# Stroke 2: 竖钩 (vertical hook) - long vertical from top, ending in a hook to the left
# Vertical part
v_top = (150, 85)
v_bot = (150, 240)
draw.line([v_top, v_bot], fill=INK, width=TH)
# Hook: at bottom, curve to the left and up slightly
hook_pts = [(150, 240), (148, 248), (140, 252), (128, 248)]
for i in range(len(hook_pts) - 1):
    draw.line([hook_pts[i], hook_pts[i+1]], fill=INK, width=TH)

# Stroke 3: 提 (rising stroke) - from lower-left rising up to the right, crossing vertical
s3_start = (105, 180)
s3_end   = (185, 160)
draw.line([s3_start, s3_end], fill=INK, width=TH)

out = os.path.join(os.path.dirname(__file__), "01_扌.png")
img.save(out)
print(f"saved {out}")
