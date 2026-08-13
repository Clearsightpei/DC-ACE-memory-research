"""
如 = 女 (left) + 口 (right). 6 strokes.
女: 撇点 (curved down-left then flick right), 撇 (long down-left sweep), 横 (horizontal)
口: 竖, 横折, 横
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=(0,0,0), width=width)
    for p in pts:
        r = width // 2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=(0,0,0))

# ----- 女 on left, roughly x in [25,140], y in [70,240] -----
# Stroke 1: 撇点 - starts upper (around 85,80), curves down-left to ~(55,175), then flicks right/down to ~(95,205)
stroke([(88, 82), (78, 115), (65, 150), (55, 175), (70, 195), (98, 208)])

# Stroke 2: 撇 - long sweep from upper-right (135,95) crossing down to lower-left (30,240)
stroke([(135, 95), (110, 145), (75, 195), (30, 240)])

# Stroke 3: 横 - horizontal near middle, slightly rising
stroke([(30, 178), (140, 170)])

# ----- 口 on right, box roughly x [175,260], y [125,210] -----
# Stroke 4: 竖 (left vertical)
stroke([(178, 125), (176, 210)])

# Stroke 5: 横折 (top horizontal then right vertical)
stroke([(178, 125), (260, 128), (258, 213)])

# Stroke 6: 横 (bottom close)
stroke([(176, 210), (260, 213)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0241_如/01_如.png")
