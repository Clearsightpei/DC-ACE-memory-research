"""
G2 render of 学 (xue2) — 8 strokes.

Structure:
  Top:  three small marks (⺍) — left 点/撇, center small 丨, right 丶
        (rendered as 3 short strokes; center leans slightly right)
  Mid:  秃宝盖 冖 — long horizontal with tiny left drop on the left,
        tiny hook on the right (drawn as one horizontal with small
        left down-tick and right terminal down-tick)
  Bot:  子 — 乛 (横折 with flick), 亅 (long central 竖钩 going down
        with UP-LEFT flick per TIER-0 B), 一 (crossbar mid-way)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    # round the joints
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# ---- Top three marks (⺍) ----
# Left small 撇 (short diagonal, top-right to bottom-left)
stroke([(95, 55), (78, 82)], width=7)
# Center small mark — short vertical/right-leaning
stroke([(150, 45), (158, 82)], width=7)
# Right small 点 (short diagonal, top-left to bottom-right)
stroke([(200, 55), (215, 82)], width=7)

# ---- 秃宝盖 冖 (horizontal cover) ----
# small left downward drop
stroke([(60, 100), (65, 115)], width=6)
# long horizontal top, terminates with small down flick on right
stroke([(60, 110), (240, 115), (238, 130)], width=8)

# ---- 子 bottom ----
# 乛 : horizontal from left going right, then turning sharply down-left (short flick)
stroke([(95, 145), (200, 148), (180, 175)], width=8)

# 亅 : long central vertical hook, ends with UP-LEFT flick
stroke([(155, 130), (155, 250), (135, 240)], width=9)

# 一 : horizontal crossbar mid-child, long, spans wide
stroke([(70, 205), (245, 210)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0379_学/01_学.png")
print("wrote 01_学.png")
