"""Render 兇 (xiōng) at 300x300.

Structure: 兇 = 凶 (top) + 儿 (bottom)
  凶 = 丿 (upper-left diagonal) + 丶/short (upper-right) forming 乂 crossing X inside
       + 凵 open-top three-sided frame (left-vertical, bottom-horizontal, right-vertical)
  儿 = 丿 (left short-flick) + 竖弯钩 (right vertical curving to right with UP-LEFT flick)

Notes: 儿's right stroke gets UP-and-LEFT flick per TIER-0 hook rule.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=7):
    # smooth line via segments + rounded joins
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)
    for p in pts:
        d.ellipse([p[0]-w//2, p[1]-w//2, p[0]+w//2, p[1]+w//2], fill="black")

# --- Top: 凶 (occupies roughly y=30..160, x=60..240) ---

# 乂 inside — strokes cross around the frame's top; tips extend well ABOVE the frame.
# Actual 凶 stroke order: 丿, 丶 form 乂; then 凵 (left-vertical, bottom, right-vertical).

# Stroke 1: 丿 of 乂 - starts high center, sweeps down-left across the frame's top
stroke([(155, 40), (135, 80), (115, 115), (95, 150)], w=6)

# Stroke 2: 丶/short-捺 of 乂 - starts high center, sweeps down-right across
stroke([(155, 40), (175, 80), (195, 115), (215, 150)], w=6)

# Stroke 3: left-vertical of 凵 — top starts BELOW the X tips (~y=95), goes down
stroke([(70, 95), (70, 165)], w=7)

# Stroke 4: 凵 bottom + right vertical — continuous 竖折-like path from bottom-left
# across to bottom-right, then up
stroke([(70, 165), (150, 178), (232, 165), (232, 95)], w=7)

# --- Bottom: 儿 (occupies roughly y=160..280, x=50..260) ---

# Stroke 5: 儿 left 丿 - starts under 凶 left, curves down and slightly left
stroke([(115, 175), (100, 210), (80, 245), (60, 275)], w=7)

# Stroke 6: 儿 right 竖弯钩 - down, curves right along bottom, then UP-LEFT flick
stroke([(178, 175), (180, 220), (190, 255), (220, 275), (255, 275)], w=7)
# The hook flick UP-and-slightly-LEFT
stroke([(255, 275), (252, 262)], w=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0282_兇/01_兇.png")
print("wrote 01_兇.png")
