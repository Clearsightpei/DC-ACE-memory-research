"""G1 render of 常 (cháng) - 11 strokes.
Structure (top→bottom): 小 (3 dots) + 冖 (crown) + 口 (small mouth) + 巾 (cloth)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# --- Top 小 cluster (3 dots) ---
# Center vertical short tick
stroke([(150, 25), (150, 60)], width=5)
# Left dot (slanting down-left)
stroke([(122, 45), (105, 72)], width=5)
# Right dot (slanting down-right)
stroke([(180, 45), (200, 72)], width=5)

# --- 冖 crown ---
# small left tick
stroke([(65, 75), (58, 92)], width=5)
# long horizontal top, gentle arc, small right-hook down
stroke([(58, 92), (100, 87), (170, 87), (235, 92), (240, 108)], width=5)

# --- 口 small square (centered, under crown) ---
# left vertical
stroke([(115, 115), (115, 150)], width=4)
# top horizontal
stroke([(115, 115), (190, 115)], width=4)
# right vertical
stroke([(190, 115), (190, 150)], width=4)
# bottom horizontal
stroke([(115, 150), (190, 150)], width=4)

# --- 巾 bottom ---
# Top horizontal of 巾 (wider than 口, sits below 口)
stroke([(75, 175), (225, 175)], width=5)
# Left descending stroke (down + slight outward)
stroke([(95, 175), (82, 275)], width=5)
# Right side: vertical then hook
stroke([(210, 175), (210, 260), (188, 275)], width=5)
# Center long vertical of 巾 (goes from just under 口 to bottom)
stroke([(150, 152), (150, 285)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0577_常/01_常.png")
print("saved")
