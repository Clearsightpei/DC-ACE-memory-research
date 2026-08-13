"""Render 盎 (ang - abundant/dish). Top: 央. Bottom: 皿."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# ===== TOP: 央 (y ~ 30..170) =====
# 1) top-center short horizontal (small bar/dot)
line((135, 45), (170, 45))

# 2) small 冂-frame just below the top bar - narrow box
#    left down
line((120, 60), (118, 100))
#    top of frame
line((120, 60), (185, 60))
#    right down with hook
line((185, 60), (187, 100))
line((187, 100), (180, 105))
#    inner horizontal (bottom of box)
line((123, 90), (183, 90))

# 3) long horizontal (widest) - the 一 of 大
line((60, 125), (245, 125))

# 4) center vertical descending from box down to horizontal
line((152, 100), (152, 145))

# 5) 撇 (down-left diagonal from center down)
line((150, 135), (85, 180))

# 6) 捺 (down-right diagonal from center down)
line((155, 135), (220, 180))

# ===== BOTTOM: 皿 (y ~ 190..280) =====
# left vertical
line((85, 195), (80, 262))
# right vertical
line((220, 195), (225, 262))
# top horizontal
line((85, 195), (220, 195))
# inner vertical 1
line((125, 205), (123, 258))
# inner vertical 2
line((175, 205), (177, 258))
# bottom long horizontal (extends past edges)
line((55, 268), (255, 270))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0550_盎/01_盎.png")
print("done")
