from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 俉 = 亻 (left) + 吾 (right, 五 over 口)

# --- 亻 (person radical, left) ---
# 撇 (long slanting stroke down-left)
stroke([(85, 75), (35, 210)], width=5)
# 竖 (vertical from mid of pie downward)
stroke([(65, 145), (68, 260)], width=5)

# --- 吾 right side ---
# 五 (top part)
# 1. top short horizontal
stroke([(165, 80), (245, 82)], width=5)
# 2. left short pie down from top-left
stroke([(180, 82), (155, 145)], width=5)
# 3. middle horizontal + right-turn-down (forms the S/Z)
stroke([(150, 130), (235, 132)], width=5)
stroke([(235, 132), (232, 170)], width=5)
# 4. bottom horizontal of 五 (long)
stroke([(140, 172), (255, 175)], width=5)

# 口 (bottom)
# left vertical
stroke([(165, 195), (165, 262)], width=5)
# top horizontal + right vertical (single 横折)
stroke([(165, 195), (248, 197)], width=5)
stroke([(248, 197), (250, 262)], width=5)
# bottom horizontal
stroke([(165, 262), (250, 262)], width=5)

out = os.path.join(os.path.dirname(__file__), "01_俉.png")
img.save(out)
print("saved", out)
