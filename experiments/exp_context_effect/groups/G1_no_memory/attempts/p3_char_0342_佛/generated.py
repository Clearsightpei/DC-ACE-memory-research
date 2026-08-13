"""G1 render of 佛 (Buddha) — 300x300, black ink on white."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# === Left radical 亻(person) ===
# Slanting piě, meeting the vertical near its top
stroke([(95, 70), (72, 135)], width=6)
# Vertical stroke starts where the piě ends
stroke([(72, 135), (72, 260)], width=6)

# === Right component 弗 ===
# Middle vertical (丨) — the long one that curves through
stroke([(185, 75), (185, 250)], width=5)

# Left "curve" vertical (丿) — starts high, curves down-left with sweep
stroke([(155, 100), (150, 200), (125, 265)], width=5)

# Right "hook" vertical (亅) — starts high, curves down-right with hook
stroke([(228, 100), (232, 235), (250, 270)], width=5)

# Upper horizontal crossing all three verticals
stroke([(135, 125), (250, 118)], width=5)
# Lower horizontal crossing all three verticals
stroke([(125, 180), (255, 175)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0342_佛/01_佛.png")
