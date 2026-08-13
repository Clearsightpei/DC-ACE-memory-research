"""Render 伎 (person radical + 支) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left: 亻 (person radical) ----
# Slanted top stroke (short diagonal 撇)
stroke([(85, 75), (60, 120)], width=5)
# Long vertical
stroke([(72, 110), (72, 250)], width=5)

# ---- Right: 支 ----
# Top horizontal (十 top)
stroke([(130, 85), (250, 85)], width=5)
# Vertical of 十
stroke([(190, 70), (190, 150)], width=5)
# Small horizontal in middle (part of 又/support)
stroke([(150, 155), (230, 155)], width=5)
# Left falling stroke (撇) from top of 又
stroke([(180, 150), (135, 260)], width=5)
# Right stroke (捺) crossing over
stroke([(170, 185), (255, 265)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_伎.png")
img.save(out_path)
print(f"Saved {out_path}")
