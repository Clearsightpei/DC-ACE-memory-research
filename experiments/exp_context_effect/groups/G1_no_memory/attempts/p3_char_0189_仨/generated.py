"""Render 仨 (sān) — 亻 radical on left, 三 on right."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def stroke(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # round caps
    r = width / 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# --- 亻 (person radical) on the left ---
# 撇 (piě): downward diagonal from upper area sweeping left-down
pie = [(105, 70), (100, 100), (90, 140), (75, 185), (60, 220)]
stroke(pie)

# 竖 (shù): vertical stroke starting from mid of piě
shu = [(100, 130), (100, 260)]
stroke(shu)

# --- 三 (three) on the right ---
# Top 横 (short-ish)
h1 = [(165, 95), (240, 88)]
stroke(h1)

# Middle 横 (shorter)
h2 = [(160, 155), (235, 152)]
stroke(h2)

# Bottom 横 (longest)
h3 = [(140, 235), (265, 228)]
stroke(h3)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0189_仨/01_仨.png")
print("saved")
