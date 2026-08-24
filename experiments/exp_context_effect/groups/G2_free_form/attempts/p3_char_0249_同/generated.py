"""
p3_char_0249_同 — G2 attempt
Character: 同 (tóng, "same"). 6 strokes.
Structure: 冂 enclosure + 一 (upper horizontal inside) + 口 (bottom inside).
Not on sibling-risk list. No 钩-family hook except the 冂's terminal is
a subtle 竖钩 in some fonts; GT shows a clean 竖 (no flick). We'll
keep the enclosure right side ending straight to match GT.

Stroke order:
1. 竖  (left of 冂)
2. 横折钩 or plain 横折 (top + right of 冂) — GT: right side ends straight
3. 一  (upper horizontal inside)
4. 竖  (口 left)
5. 横折 (口 top + right)
6. 一  (口 bottom)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
w_thick = 8
w_thin = 7


def stroke(points, width=w_thick):
    d.line(points, fill=INK, width=width, joint="curve")
    # dab endpoints
    r = width // 2
    for (x, y) in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- 冂 enclosure ---
# 1. Left vertical (slight lean; slightly shorter than right)
stroke([(70, 78), (72, 258)], width=w_thick)

# 2. Top horizontal + right vertical (one stroke: 横折)
# top goes from ~(66, 76) rightward to ~(232, 72), then down to ~(238, 262)
stroke([(60, 76), (232, 70), (238, 262)], width=w_thick)

# 3. Upper inside 横 (一)
stroke([(96, 140), (216, 138)], width=w_thin)

# --- 口 (inside bottom) ---
# 4. Left vertical
stroke([(108, 178), (110, 250)], width=w_thin)

# 5. Top + right (横折)
stroke([(104, 178), (206, 176), (208, 252)], width=w_thin)

# 6. Bottom horizontal
stroke([(108, 250), (208, 250)], width=w_thin)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0249_同/01_同.png")
