"""G1 render of 是 (p3_char_0429)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts):
    d.line(pts, fill="black", width=LW)

# 是 structure: top 日 + bottom 疋 (一 + 龰)

# --- Top 日 (roughly x 110-190, y 40-115) ---
# Left vertical
line([(112, 42), (114, 118)])
# Top horizontal
line([(112, 42), (190, 46)])
# Right vertical (slight hook at bottom)
line([(190, 46), (188, 118)])
# Middle horizontal
line([(114, 80), (189, 82)])
# Bottom horizontal
line([(114, 118), (188, 118)])

# --- Long horizontal (top of 疋) ---
line([(70, 148), (230, 152)])

# --- Small horizontal above 龰 body ---
line([(120, 178), (180, 180)])

# --- Small vertical connecting the two horizontals ---
line([(150, 152), (150, 180)])

# --- 撇 (left downward stroke of 龰) ---
line([(130, 180), (75, 268)])

# --- Short horizontal in middle of 龰 (the "一" inside) ---
line([(95, 232), (160, 235)])

# --- 捺 (right downward stroke, going down-right) ---
line([(160, 195), (255, 270)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0429_是/01_是.png")
