"""G1 render of 盍 (he) — 去 (士 + ム) over 皿 dish."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w)

# ---- Top: 士 ----
# top short horizontal (shorter)
line([(120, 45), (180, 43)], 4)
# vertical stem
line([(150, 45), (150, 100)], 4)
# long horizontal (wider than top)
line([(100, 100), (200, 97)], 5)

# ---- Middle: ム (private) shape — triangular ----
# left-down diagonal 撇
line([(148, 108), (120, 150)], 4)
# top-right short horizontal / dot region
line([(148, 108), (178, 115)], 4)
# right side down
line([(178, 115), (168, 148)], 4)
# closing curve/horizontal
line([(120, 150), (168, 148)], 4)

# ---- 皿 top big horizontal ----
line([(55, 170), (245, 167)], 5)

# ---- Bottom: 皿 (dish) ----
# left vertical (leans out)
line([(80, 175), (72, 250)], 4)
# right vertical (leans out)
line([(220, 175), (228, 250)], 4)
# inner left vertical
line([(125, 178), (122, 240)], 4)
# inner right vertical
line([(175, 178), (178, 240)], 4)
# bottom long horizontal (base of 皿)
line([(50, 253), (250, 250)], 5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0548_盍/01_盍.png")
print("saved")
