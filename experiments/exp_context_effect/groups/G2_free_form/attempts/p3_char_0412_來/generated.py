"""
Render 來 to 300x300 PNG.

Structure (from GT):
- Top horizontal: high, centered, moderate length
- A central vertical spine going from just below the top horizontal down to near bottom
- Two small 人-like shapes: one on the left half, one on the right half,
  attached near the upper-middle of the spine (their apexes meet the spine
  slightly below top horizontal)
- A long horizontal near lower-middle crossing the spine
- Bottom 撇 (left flare) and bottom 捺 (right flare) from the intersection
  of the long horizontal and the spine.

Not a sibling-risk target per TIER-0 list; drawing fresh from GT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 5  # brush width

def line(p0, p1, w=BW):
    d.line([p0, p1], fill=INK, width=w)

def bezier(pts, w=BW, steps=60):
    # quadratic bezier
    (x0,y0),(x1,y1),(x2,y2) = pts
    last = (x0,y0)
    for i in range(1, steps+1):
        t = i/steps
        u = 1-t
        x = u*u*x0 + 2*u*t*x1 + t*t*x2
        y = u*u*y0 + 2*u*t*y1 + t*t*y2
        d.line([last,(x,y)], fill=INK, width=w)
        last = (x,y)

# 1) Top horizontal — slight downward slope then curl right
bezier([(75, 65), (150, 60), (225, 72)], w=6)

# 2) Central vertical spine
line((150, 72), (152, 260), w=6)

# 3) Left small 人: apex on spine at y~100
# 撇 (long, down-left flare)
bezier([(151, 100), (115, 135), (78, 180)], w=5)
# 短捺/点 (small dot flare inward-down)
bezier([(151, 105), (140, 135), (135, 165)], w=5)

# 4) Right small 人: apex on spine at y~100
bezier([(151, 105), (162, 135), (167, 165)], w=5)
bezier([(151, 100), (187, 135), (222, 180)], w=5)

# 5) Long horizontal near lower middle
bezier([(60, 205), (150, 200), (245, 210)], w=6)

# 6) Bottom 撇 from spine/horizontal intersection curving down-left
bezier([(148, 208), (120, 240), (85, 275)], w=6)

# 7) Bottom 捺 from spine/horizontal intersection sweeping down-right
bezier([(154, 208), (200, 240), (250, 265)], w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0412_來/01_來.png")
print("saved")
