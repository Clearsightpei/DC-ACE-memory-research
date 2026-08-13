"""Render 空 (kong - empty). 8 strokes: 宀 (roof w/ dot) + 八 (two dots) + 工 (bottom)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def polyline(pts, width=5):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)

# --- 宀 radical (roof) ---
# Stroke 1: top dot (short diagonal, upper center)
polyline([(148, 40), (156, 58)], width=6)

# Stroke 2: left short diagonal (start of roof, upper-left)
polyline([(85, 80), (75, 105)], width=5)

# Stroke 3: horizontal with right-side hook down (roof top + right side)
polyline([(75, 105), (230, 100), (228, 138)], width=5)

# --- 八 (two dots inside roof) ---
# Stroke 4: left dot (short slash \)
polyline([(120, 135), (108, 160)], width=6)

# Stroke 5: right dot (short slash /)
polyline([(192, 135), (204, 160)], width=6)

# --- 工 (bottom) ---
# Stroke 6: top horizontal
polyline([(100, 200), (210, 198)], width=5)

# Stroke 7: middle vertical
polyline([(155, 200), (155, 250)], width=5)

# Stroke 8: bottom horizontal (longer)
polyline([(70, 252), (240, 250)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_空.png"))
print("saved")
