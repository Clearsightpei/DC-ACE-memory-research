"""G1 render of 痄 (illness radical 疒 + 乍 inside)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- 疒 radical (illness) - left/top wrapping ----
# 1) top dot (small diagonal)
line([(108, 45), (118, 58)], w=5)

# 2) top horizontal of 疒 (long, gentle downward slant, ends up near top-right)
line([(78, 78), (240, 72)], w=4)

# 3) two small dots on the left side (short diagonals)
line([(85, 100), (75, 118)], w=4)
line([(102, 122), (92, 140)], w=4)

# 4) long sweeping left-falling stroke (the leg of 疒)
line([(108, 78), (55, 265)], w=5)

# ---- 乍 inside (right portion) ----
# 5) tiny slanted stroke at top of 乍
line([(165, 105), (180, 98)], w=4)

# 6) top horizontal of 乍
line([(140, 130), (230, 124)], w=4)

# 7) vertical stroke of 乍 (comes down through, slightly left of center of horizontals)
line([(168, 124), (163, 255)], w=5)

# 8) middle short horizontal
line([(163, 175), (215, 172)], w=4)

# 9) bottom horizontal
line([(150, 220), (220, 216)], w=4)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_痄.png")
img.save(out_path)
print(f"Saved {out_path}")
