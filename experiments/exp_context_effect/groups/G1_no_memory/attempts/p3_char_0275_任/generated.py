"""G1 render for 任 (p3_char_0275). PIL, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# 亻 (person radical) on the left
# 1. Left slanting stroke (short, upper): from top ~ (95, 75) down-left to (55, 155)
stroke([(95, 75), (78, 110), (58, 155)], width=6)
# 2. Vertical stroke from (95, 100) down to (95, 240)
stroke([(95, 100), (93, 170), (92, 245)], width=6)

# 壬 (right side)
# 1. Short slant top (ノ): from (155, 75) down-left slightly to (135, 90)
stroke([(160, 70), (145, 82), (130, 92)], width=6)
# 2. Top horizontal: from (130, 92) to (230, 88)
stroke([(130, 92), (180, 90), (235, 88)], width=6)
# 3. Middle horizontal (shorter): from (145, 150) to (240, 148)
stroke([(145, 150), (195, 149), (245, 148)], width=6)
# 4. Vertical stroke through middle: from (185, 90) down to (185, 235)
stroke([(185, 92), (186, 160), (188, 235)], width=6)
# 5. Bottom horizontal (longest, slight upward tilt at right): from (115, 240) to (265, 232)
stroke([(115, 240), (190, 236), (270, 230)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0275_任/01_任.png")
print("wrote 01_任.png")
