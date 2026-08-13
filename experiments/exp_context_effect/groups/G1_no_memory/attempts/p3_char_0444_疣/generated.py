"""Render 疣 (character) as 300x300 PNG using PIL. Revision 2."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
W = 4


def stroke(pts, width=W):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# ============================================================
# 疒 radical (sickness) — encloses top and left
# ============================================================

# 1) Top dot (点) on top-center
stroke([(122, 55), (138, 72)], width=5)

# 2) Top horizontal 一 — long across upper part
stroke([(75, 92), (205, 86)])

# 3) Left vertical-curving downward stroke of 疒
# Starts at left end of horizontal, comes down and curves down-left
stroke([(100, 86), (92, 140), (78, 200), (65, 250)])

# 4) Upper little dot on left interior of 疒 (丶)
stroke([(80, 118), (95, 138)], width=5)

# 5) Lower little dot on left interior of 疒 (丶)
stroke([(72, 158), (88, 178)], width=5)

# ============================================================
# 尤 inside (right-lower quadrant)
# ============================================================

# 6) Short top tick (丿) — small slanted stroke top-right
stroke([(198, 118), (215, 138)], width=4)

# 7) Horizontal of 尤 (一)
stroke([(125, 145), (220, 140)])

# 8) Left downward slanted stroke (丿) of 尤
stroke([(155, 145), (135, 200), (118, 245)])

# 9) 乚 vertical + right hook up (main body of 尤)
# down from horizontal, curve right along bottom, then up
stroke([(180, 145), (180, 215), (195, 245), (240, 250), (245, 220)])

# 10) small dot inside 尤 (丶) — top-right accent
stroke([(222, 158), (238, 175)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_疣.png")
img.save(out_path)
print(f"wrote {out_path}")
