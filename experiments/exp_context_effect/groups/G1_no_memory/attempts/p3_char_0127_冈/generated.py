"""G1 render of 冈 (character p3_char_0127) at 300x300 PNG."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# Frame occupies roughly x=[60,240], y=[45,270]
# Stroke 1: left vertical 丨 (slight slant left, from (60, 60) to (55, 275))
draw.line([(62, 62), (58, 278)], fill=BLACK, width=LW)

# Stroke 2: top horizontal + right vertical hook (橫折鉤)
# horizontal from (62, 55) to (238, 62)
draw.line([(62, 55), (238, 60)], fill=BLACK, width=LW)
# right vertical from (238, 60) down to (232, 268), then small hook left
draw.line([(238, 60), (234, 268)], fill=BLACK, width=LW)
# hook
draw.line([(234, 268), (218, 262)], fill=BLACK, width=LW)

# Inside 乂 (X shape), centered around (150, 175)
# Stroke 3: 撇 (falling left) from upper-right to lower-left
draw.line([(195, 120), (95, 240)], fill=BLACK, width=LW)
# Stroke 4: 捺 (falling right) from upper-left to lower-right
draw.line([(115, 130), (210, 245)], fill=BLACK, width=LW)

out_path = __file__.rsplit("/", 1)[0] + "/01_冈.png"
img.save(out_path)
print(f"Saved {out_path}")
