"""
次 — 6 strokes = 冫 (left, 2) + 欠 (right, 4)
Left 冫: 点 upper, 提 lower.
Right 欠: 撇 (short top), 横钩 (top-bar with left-down hook), 撇 (long),
         捺 (long down-right).
Silhouette from GT: 冫 left-column narrow; 欠 wide, top 撇 short,
horizontal bar in middle-upper, big X-shape of 撇+捺 across bottom.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")
    for x, y in pts:
        d.ellipse((x - width/2, y - width/2, x + width/2, y + width/2), fill="black")

def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- 冫 (left column) ---
# 点 upper-left: short down-right stroke, tapered
line([(55, 100), (72, 118)], width=8)
dab(72, 118, 5)
# 提 lower-left: rising stroke from lower-left up to right
line([(50, 190), (85, 168)], width=7)
dab(50, 190, 4)

# --- 欠 (right side) ---
# 1) short 撇 at top (small flick from upper-right going down-left)
line([(175, 65), (160, 90)], width=7)
dab(160, 90, 4)

# 2) 横钩: horizontal bar starting from the base of the short 撇,
#    going right, then a small hook down-left at the right end.
# Horizontal
line([(150, 95), (245, 92)], width=7)
# Small hook: down-left flick at right terminal
line([(245, 92), (238, 108)], width=7)
dab(238, 108, 4)

# 3) long 撇: sweeping from below the top-bar down-and-left to bottom-left
line([(175, 108), (155, 150), (130, 195), (95, 250)], width=7)
dab(95, 250, 4)

# 4) 捺: from around the middle-upper of 欠 (near where the 撇 starts),
#    sweeping down-right with a broadening tail
# Build with several segments increasing width for the 捺 wedge
pts = [(180, 130), (200, 165), (225, 205), (255, 240)]
for i in range(len(pts) - 1):
    w = 5 + i * 2
    d.line([pts[i], pts[i+1]], fill="black", width=w)
# tail flick
dab(255, 240, 6)
d.line([(255, 240), (270, 245)], fill="black", width=4)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0273_次/01_次.png")
print("saved")
