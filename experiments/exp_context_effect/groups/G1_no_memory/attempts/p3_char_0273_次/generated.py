"""G1 render of 次 (cì) — 6 strokes, PIL at 300x300."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# Left radical: 冫 (two dots)
# Upper dot (short slanting stroke)
line([(65, 110), (88, 130)], width=6)
# Lower 提 (rising stroke)
line([(55, 195), (95, 175)], width=6)

# Right side: 欠 (qiàn)
# Stroke 1: 撇 — short slanting top of 欠
line([(170, 60), (150, 105)], width=6)
# Stroke 2: 横钩 — horizontal then hook down
line([(150, 105), (235, 100), (228, 125)], width=6)
# Stroke 3: 撇 — long left-slanting from upper mid down to lower left
line([(195, 130), (115, 260)], width=6)
# Stroke 4: 捺 — long right-slanting ending flare
line([(170, 175), (255, 265)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0273_次/01_次.png")
