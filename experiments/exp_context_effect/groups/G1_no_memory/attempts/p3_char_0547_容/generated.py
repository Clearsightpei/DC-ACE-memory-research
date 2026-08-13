"""G1 attempt for 容 (róng) - 宀 + 八 + 人 + 口."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# --- 宀 (roof radical, 3 strokes) ---
# 1. top dot (点)
stroke([(148, 25), (158, 42)], w=5)
# 2. 横钩: left tick down + long horizontal + hook down at end
stroke([(65, 68), (75, 60), (235, 60), (228, 82)], w=5)
# The 宀 left side descends
stroke([(75, 60), (72, 95)], w=5)

# --- middle row: 八 (two dots) + 人 (small 撇捺) ---
# left dot of 八
stroke([(95, 100), (82, 128)], w=5)
# right dot of 八
stroke([(215, 100), (228, 128)], w=5)

# 人 in center
stroke([(150, 108), (115, 165)], w=5)   # 撇
stroke([(150, 108), (188, 165)], w=5)   # 捺

# --- 口 at bottom (3 strokes) ---
# left vertical
stroke([(112, 200), (112, 268)], w=5)
# top horizontal + right vertical (横折)
stroke([(112, 200), (195, 200), (195, 268)], w=5)
# bottom horizontal
stroke([(112, 268), (195, 268)], w=5)

out_path = os.path.join(os.path.dirname(__file__), "01_容.png")
img.save(out_path)
print(f"Saved {out_path}")
