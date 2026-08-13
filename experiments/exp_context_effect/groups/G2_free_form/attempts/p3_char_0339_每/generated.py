"""Draw 每 (7画) at 300x300, white bg, black ink.

Structure = 𠂉 (top) + 母 (bottom).

Strokes (7):
  1. 撇  — short flick top-left, from ~(155,40) down-left to ~(100,105)
  2. 横  — short horizontal across top of body ~(110,88)→(200,88)
  3. 竖折 — left wall of 母: down then turn right at bottom
  4. 横折钩 — top+right wall of 母 with small up-left hook at base
  5. 点  — upper inside dot
  6. 长横 — long horizontal crossing right through body (extends both sides)
  7. 点  — lower inside dot
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")
    r = width / 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# --- 1. 撇 (top): starts upper, sweeps diagonally down-left ---
stroke([(165, 38), (145, 62), (120, 92), (95, 118)], width=5)

# --- 2. 横 (top short): meets the 撇 near its lower end ---
stroke([(115, 88), (205, 92)], width=5)

# Body of 母 sits below y~100
LEFT_X = 108
RIGHT_X = 205
TOP_Y = 100
MID_Y = 175
BOT_Y = 250

# --- 3. 竖折 : left wall down then short right along bottom ---
stroke([(LEFT_X + 4, TOP_Y + 2),
        (LEFT_X, MID_Y),
        (LEFT_X + 4, BOT_Y),
        (LEFT_X + 60, BOT_Y - 4)], width=5)

# --- 4. 横折钩 : top+right wall + small up-left hook flick ---
stroke([(LEFT_X + 6, TOP_Y - 4),
        (RIGHT_X - 2, TOP_Y + 2),   # short top 横 of the box
        (RIGHT_X + 6, TOP_Y + 16),  # shoulder dab
        (RIGHT_X - 4, BOT_Y - 6),   # right wall down
        (RIGHT_X - 25, BOT_Y - 22)],# UP-and-LEFT hook flick
       width=5)

# --- 5. 点 (upper inside) ---
stroke([(148, 145), (162, 158)], width=6)

# --- 6. 长横 : long horizontal that crosses through the whole body ---
stroke([(55, MID_Y + 2), (245, MID_Y - 4)], width=5)

# --- 7. 点 (lower inside) ---
stroke([(150, 205), (164, 218)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0339_每/01_每.png")
