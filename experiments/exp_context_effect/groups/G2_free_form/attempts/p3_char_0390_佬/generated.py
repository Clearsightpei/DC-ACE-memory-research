"""
佬 = 亻 (left) + 老 (right, 耂 top + 匕 bottom)
Stroke count: 8. Layout: left-right, left ~30%, right ~70%.

# SIGNATURE CHECK (component 匕 in bottom-right):
# 匕 top stroke is a 撇 (upper-right -> lower-left);
# terminal hook flicks UP-and-LEFT (NEVER down, NEVER right).

Strokes (in canonical order):
  1. 亻 撇 (top-left slanting down-left)
  2. 亻 竖 (vertical from apex of 撇 going down)
  3. 耂 横 (top horizontal, right side)
  4. 耂 竖 (short vertical crossing 横 midway)
  5. 耂 长撇 (long slanting stroke from top-right down to lower-left)
  6. 耂 second 横 (short horizontal crossing 长撇 partway)
  -- above four form 耂 (土 with a 丿 through it)
  7. 匕 撇 (short slanting stroke, upper-right to lower-left inside 匕)
  8. 匕 竖弯钩 (vertical bending right and hooking up-left)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# ---------- 亻 (left, ~x 30-90) ----------
# 撇: from around (78, 70) down-left to (45, 165)
line([(82, 68), (72, 100), (60, 135), (48, 168)], width=6)
# 竖: from apex of 撇 (~72, 95) straight down to (72, 240)
line([(72, 95), (72, 170), (72, 240)], width=6)

# ---------- 耂 (top-right, ~x 120-260, y 55-180) ----------
# 横 (top horizontal): (135, 100) to (255, 100)
line([(135, 100), (195, 98), (255, 102)], width=6)
# 竖 (short vertical crossing 横): from (200, 70) to (200, 130)
line([(200, 72), (200, 100), (200, 132)], width=6)
# 长撇 (long left-falling stroke): from top-right (245, 70) sweeping down-left to (115, 220)
line([(245, 68), (215, 110), (180, 155), (145, 190), (115, 222)], width=6)
# 第二横 (shorter horizontal crossing 长撇 lower): (130, 145) to (240, 148)
line([(132, 148), (185, 145), (240, 150)], width=6)

# ---------- 匕 (bottom-right, ~x 145-260, y 175-260) ----------
# 撇: short slanting from (200, 175) to (155, 240)
line([(202, 178), (185, 200), (168, 225), (155, 245)], width=6)
# 竖弯钩: from (175, 200) down to (175, 250), sweep right to (250, 255), hook UP-and-LEFT
line([(178, 200), (178, 232), (178, 255), (205, 262), (240, 260), (255, 252), (250, 240)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0390_佬/01_佬.png")
print("wrote 01_佬.png")
