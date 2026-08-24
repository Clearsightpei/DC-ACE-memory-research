"""町 = 田 (left) + 丁 (right).
Layout: 田 occupies left ~40% (compressed narrow), 丁 occupies right ~55%.
丁 has horizontal top + hooked vertical (竖钩 flicks UP-LEFT).
"""
from PIL import Image, ImageDraw

SZ = 300
img = Image.new("RGB", (SZ, SZ), "white")
d = ImageDraw.Draw(img)

W = 7  # stroke width

def line(p1, p2, w=W):
    d.line([p1, p2], fill="black", width=w)

# ---- 田 (left, roughly x: 40..135, y: 90..215) ----
Lx, Rx = 40, 135
Ty, By = 90, 215
Mx = (Lx + Rx) // 2
My = (Ty + By) // 2

# Outer box: left-vertical, top-horizontal, right-vertical, bottom-horizontal
line((Lx, Ty), (Lx, By))                # left vertical
line((Lx - 2, Ty), (Rx + 2, Ty))        # top horizontal
line((Rx, Ty - 2), (Rx, By + 2))        # right vertical (slight overhang)
line((Lx, By), (Rx, By))                # bottom horizontal
# Middle horizontal
line((Lx, My), (Rx, My))
# Middle vertical
line((Mx, Ty), (Mx, By))

# ---- 丁 (right, roughly x: 150..270, y: 75..245) ----
# Top horizontal: long, slight tilt up
top_l = (150, 88)
top_r = (275, 78)
line(top_l, top_r, w=W)

# Vertical with hook (竖钩): starts near horizontal midpoint, goes down,
# then flicks UP-and-LEFT
v_top = (218, 82)
v_bot = (218, 235)
line(v_top, v_bot, w=W)
# Hook: flick up-and-left
hook_end = (200, 218)
line(v_bot, hook_end, w=W)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0294_町/01_町.png")
print("saved")
