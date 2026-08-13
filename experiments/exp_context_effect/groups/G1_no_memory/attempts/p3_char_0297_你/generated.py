"""G1 render of 你 (nǐ). Revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=6):
    d.line(points, fill="black", width=width, joint="curve")

# --- LEFT RADICAL: 亻 ---
# 撇 (starts upper, sweeps down-left)
stroke([(90, 70), (85, 100), (75, 140), (60, 190), (48, 240)], width=6)
# 竖 (vertical) starts from the 撇 body (~ mid) going straight down
stroke([(80, 125), (80, 170), (80, 220), (80, 265)], width=6)

# --- RIGHT COMPONENT: 尔 ---
# Top 撇 (small down-left slant, top-center)
stroke([(180, 60), (170, 80), (162, 100)], width=6)
# Top 点/short right slant (top-right of the roof)
stroke([(195, 70), (210, 90), (220, 110)], width=6)

# 横钩 : long horizontal with hook going down-left at the right end
stroke([(130, 130), (170, 128), (215, 126), (245, 128)], width=6)
stroke([(245, 128), (238, 148)], width=6)

# Central 竖钩 (vertical hook)
stroke([(190, 130), (190, 180), (190, 230), (190, 265)], width=6)
stroke([(190, 265), (175, 258)], width=6)  # hook to the left

# Left 撇 (from top-left of 尔 body, going down-left)
stroke([(155, 155), (140, 190), (125, 225)], width=6)

# Right 点 (dot, from mid-right going down-right)
stroke([(220, 160), (240, 195), (255, 225)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_你.png"))
print("saved 01_你.png")
