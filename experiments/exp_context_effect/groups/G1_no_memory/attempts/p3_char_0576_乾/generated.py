"""G1 render of 乾 (qian) — left: 龺 (十+日+long horiz + 十 running through), right: 乞."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# ==== LEFT COMPONENT: 龺 (like 卓 upper) ====
# occupies x in [45, 165], y in [50, 275]

# Top: small stroke going down-left (like left dot/丿 above the box)
line([(112, 55), (100, 78)], 4)
# Top short horizontal
line([(90, 78), (135, 72)], 4)

# Box (日-like)
line([(70, 95), (155, 90)], 4)   # top
line([(72, 95), (75, 160)], 4)   # left
line([(155, 90), (152, 160)], 4) # right
line([(75, 128), (153, 125)], 4) # middle horizontal
line([(72, 160), (153, 160)], 4) # bottom

# Long horizontal below the box (the 一)
line([(45, 195), (172, 188)], 4)

# Long vertical going down through center (from top, through box, past bottom horiz)
line([(108, 78), (110, 278)], 4)

# ==== RIGHT COMPONENT: 乞 ====
# occupies x in [175, 288], y in [100, 265]

# Top slanted 撇
line([(210, 110), (188, 138)], 4)
# Horizontal short (top of 乞)
line([(185, 138), (250, 132)], 4)
# The big 乙-like sweeping stroke — smoother curve, ending with rightward hook
sweep = [
    (255, 138),
    (245, 160),
    (225, 180),
    (205, 200),
    (192, 225),
    (198, 250),
    (225, 262),
    (260, 263),
    (285, 250),
]
line(sweep, 4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0576_乾/01_乾.png")
print("saved")
