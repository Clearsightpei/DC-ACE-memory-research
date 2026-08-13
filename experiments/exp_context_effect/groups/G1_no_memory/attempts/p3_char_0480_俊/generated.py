"""G1 render of 俊 (jun) — 亻 (left) + 夋 (right, top厶 / middle八 / bottom夂)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ============ 亻 (left radical) ============
# 撇 (long left-falling)
stroke([(90, 65), (60, 155), (45, 220)], width=5)
# 竖 (vertical, meets 撇 at upper-mid)
stroke([(78, 115), (78, 265)], width=5)

# ============ 夋 (right) ============
# --- Top 厶 ---
# left downward-slant
stroke([(175, 60), (160, 95)], width=4)
# short horizontal + tiny hook
stroke([(160, 95), (210, 90), (215, 105)], width=4)

# --- Middle 八 (two diverging small strokes) ---
# left 撇
stroke([(170, 115), (155, 145)], width=4)
# right 捺
stroke([(210, 115), (230, 145)], width=4)

# --- Bottom 夂 ---
# 横撇: short horizontal, then down-left long 撇
stroke([(155, 165), (225, 160)], width=4)
stroke([(215, 155), (200, 180), (140, 275)], width=5)
# 捺: from mid going down-right sweeping wide
stroke([(180, 195), (225, 240), (270, 275)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0480_俊/01_俊.png")
