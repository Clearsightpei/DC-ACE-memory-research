"""
p3_char_0161_甴 — 5 strokes
Structure (from GT):
  1. 竖 vertical stalk emerging from top-center, extending up above the box
  2. 竖 left side of the box (vertical, from top-left down)
  3. 横折 top-horizontal + right-vertical (single stroke: top edge, then turns down)
  4. 横 middle horizontal inside the box
  5. 横 bottom horizontal (closes the box)

Canvas 300x300, black ink on white.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # line width

# Box coords
box_left = 70
box_right = 230
box_top = 110
box_bot = 260
box_mid_y = (box_top + box_bot) // 2  # centered horizontal

# 1. 竖 top stalk (vertical from above box into top edge, roughly centered)
stalk_x = 145
stalk_top = 50
d.line([(stalk_x, stalk_top), (stalk_x, box_top + 5)], fill=BLACK, width=LW)

# 2. 竖 left side of box
d.line([(box_left, box_top), (box_left, box_bot)], fill=BLACK, width=LW)

# 3. 横折 top edge + right side (single stroke with fold)
d.line([(box_left - 2, box_top), (box_right, box_top)], fill=BLACK, width=LW)
d.line([(box_right, box_top - 2), (box_right, box_bot)], fill=BLACK, width=LW)

# 4. 横 middle horizontal
d.line([(box_left + 4, box_mid_y), (box_right - 4, box_mid_y)], fill=BLACK, width=LW)

# 5. 横 bottom horizontal
d.line([(box_left - 2, box_bot), (box_right + 2, box_bot)], fill=BLACK, width=LW)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0161_甴/01_甴.png"
img.save(out_path)
print(f"Wrote {out_path}")
