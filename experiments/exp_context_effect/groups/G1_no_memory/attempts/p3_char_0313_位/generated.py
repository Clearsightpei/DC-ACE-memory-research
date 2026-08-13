"""G1 draw 位 (亻+立) — PIL 300x300."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# --- 亻 (person radical) left ---
# 撇 slanting from upper to lower-left
d.line([(105, 70), (55, 210)], fill="black", width=5)
# 竖 vertical
d.line([(100, 120), (100, 260)], fill="black", width=5)

# --- 立 on right ---
# top 点 (small diagonal dot)
d.line([(190, 55), (200, 75)], fill="black", width=5)
# upper horizontal 一
d.line([(155, 105), (245, 105)], fill="black", width=5)
# left 点 (short diag under upper horizontal)
d.line([(170, 130), (162, 165)], fill="black", width=5)
# right 点 (short diag mirror)
d.line([(230, 130), (238, 165)], fill="black", width=5)
# short vertical center
d.line([(200, 110), (200, 175)], fill="black", width=5)
# bottom horizontal 一 (long, under 立 only)
d.line([(140, 220), (265, 220)], fill="black", width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0313_位/01_位.png")
