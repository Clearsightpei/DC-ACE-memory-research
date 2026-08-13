"""
难 (nan) — LR composition: 又 (left) + 隹 (right).
- Left 又: two strokes — 横撇 (top→right→down-left sweep) + 捺 (down-right).
- Right 隹: 亻 (撇+竖) + top 丶 + right vertical + 3 short 横 across right stem + 底横.
- Components MUST touch (Tier-0 H): left 又's 捺 tail meets right 亻's 撇/竖 area.
- Hook rule N/A (no hooks in 难).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- LEFT: 又 (spanning x ~ 20..150, y ~ 70..255) ----
# S1: 横撇 — short horizontal then long sweep down-left
stroke([(35, 95), (135, 95), (30, 250)], width=8)
# S2: 捺 — from mid of S1 down-right to lower-right, ending at meeting with right component
stroke([(70, 140), (100, 180), (150, 240), (170, 255)], width=9)

# ---- RIGHT: 隹 (spanning x ~ 150..280, y ~ 55..260) ----
# 亻 撇 — long sweep from top down-left
stroke([(200, 55), (180, 95), (155, 145)], width=8)
# 亻 竖 — inside the 撇 sweep
stroke([(178, 115), (178, 258)], width=8)
# top 丶 — tick above right stem
stroke([(220, 75), (232, 92)], width=8)
# right tall 竖 (main vertical of 隹's right stem)
stroke([(245, 105), (245, 258)], width=8)
# 3 short 横 crossing between the two verticals (top, middle, lower)
stroke([(180, 130), (248, 130)], width=6)
stroke([(180, 170), (248, 170)], width=6)
stroke([(180, 208), (248, 208)], width=6)
# 底横 (bottom horizontal — extends across whole right component)
stroke([(160, 253), (283, 253)], width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0545_难/01_难.png")
