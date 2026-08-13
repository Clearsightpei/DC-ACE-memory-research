"""Render 定 (dìng) at 300x300, black ink on white, PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(pts, w=6):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# ---- 宀 roof ----
# 1. top dot (点) — small right-leaning dot at top center
line([(148, 28), (160, 50)], w=8)

# 2. left dot of the roof (short slanted)
line([(78, 70), (92, 82)], w=6)

# 3. Main roof: horizontal then curves down-right with hook
# start at left, go right, then bend down for the right side of 宀
line([(70, 88), (215, 82), (232, 96), (234, 118)], w=6)

# ---- 疋 bottom component ----
# 4. horizontal (top of 疋)
line([(100, 138), (208, 138)], w=6)

# 5. small vertical drop on left
line([(128, 138), (128, 168)], w=6)

# 6. short horizontal closing the little box
line([(128, 168), (180, 168)], w=6)

# 7. slight vertical on right of the little box
line([(180, 156), (180, 172)], w=5)

# 8. pie (丿) — left-falling diagonal from mid down to lower-left
line([(150, 172), (100, 240)], w=6)

# 9. long na (乀) horizontal sweep with slight upturn at right
line([(95, 250), (240, 248), (258, 235)], w=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_定.png"))
print("saved")
