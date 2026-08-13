"""G1 render of 伊 (character). PIL, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 伊 = 亻 (left) + 尹 (right)

# --- Left radical 亻 ---
# slanted top stroke
line([(85, 75), (55, 130)], width=5)
# vertical
line([(75, 115), (75, 250)], width=5)

# --- Right 尹 (4 strokes) ---
# 1. short slash top-left of 尹
line([(155, 80), (140, 115)], width=5)
# 2. top horizontal (slight rightward downtick as a small hook)
line([(140, 110), (250, 105)], width=5)
line([(250, 105), (245, 118)], width=4)  # tiny hook
# 3. middle horizontal (a bit shorter, positioned below top)
line([(150, 155), (240, 150)], width=5)
# 4. long descending stroke: starts upper-right, goes down then curves down-left
line([(215, 90), (210, 165)], width=5)
line([(210, 165), (150, 265)], width=5)

img.save(os.path.join(os.path.dirname(__file__), "01_伊.png"))
print("saved 01_伊.png")
