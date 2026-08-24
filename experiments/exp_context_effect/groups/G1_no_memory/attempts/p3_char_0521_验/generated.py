"""G1 render of 验 (yàn) — left: 马 (simplified 3-stroke), right: 佥."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=w)

# ---------- Left: 马 (simplified, 3 strokes) ----------
# Stroke 1: 横折 — top: horizontal then down (forms top-right corner)
poly([(55, 85), (130, 85), (130, 155)])

# Stroke 2: 竖折折钩 — the big "S" body:
# starts at top-left of middle, goes right, down, left, down again, right, up-hook
poly([(60, 130), (130, 130)])                       # small horizontal segment
poly([(60, 130), (60, 175), (130, 175),
      (130, 220), (60, 220), (60, 240), (145, 240),
      (145, 215)])                                   # main body + hook

# Stroke 3: 一 — long horizontal across bottom (提)
poly([(35, 240), (155, 240)])

# ---------- Right: 佥 ----------
# Top 人: 撇 + 捺 meeting at apex
poly([(215, 65), (172, 135)])   # 撇
poly([(215, 65), (262, 135)])   # 捺

# Horizontal beneath 人
poly([(178, 145), (255, 145)])

# Two small dots/short strokes 丷 (left dot leans left, right dot leans right)
poly([(195, 158), (188, 178)])
poly([(240, 158), (247, 178)])

# Second horizontal
poly([(178, 190), (255, 190)])

# Bottom: two small slanting strokes (mimicking small 人 pair)
poly([(203, 200), (195, 230)])
poly([(233, 200), (241, 230)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0521_验/01_验.png")
