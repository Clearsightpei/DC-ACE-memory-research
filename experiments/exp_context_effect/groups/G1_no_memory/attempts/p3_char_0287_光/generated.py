"""G1 render for 光 (p3_char_0287) — 300x300 PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=6):
    d.line([p0, p1], fill="black", width=w)

# 光 has 6 strokes:
# 1) small left dot/short slant on upper-left  ⺌ left
# 2) vertical stroke in the middle top
# 3) small right dot/short slant on upper-right ⺌ right
# 4) horizontal stroke across middle
# 5) left curved leg (piě)
# 6) right hook leg (乚)

# 1) Left upper diagonal (short piě): from ~(100,80) down-left to (80,110)
line((105, 75), (78, 108), 6)

# 2) Middle short vertical: from (150,55) down to (150,105)
line((150, 55), (150, 105), 6)

# 3) Right upper diagonal (short dot/slant): from (195,80) to (220,110)
line((195, 75), (222, 108), 6)

# 4) Horizontal across middle: from (55,140) to (245,140)
line((55, 140), (245, 140), 7)

# 5) Left leg (piě - curving down-left): from (135,140) to (55,270)
# emulate curve with a couple of segments
line((135, 140), (100, 210), 6)
line((100, 210), (55, 270), 6)

# 6) Right leg with hook (shùwāngōu): vertical from ~(180,140) down to (180,255) then hook right to (230,255)
line((180, 140), (180, 255), 6)
line((180, 255), (235, 255), 6)

out = Path(__file__).parent / "01_光.png"
img.save(out)
print("saved", out)
