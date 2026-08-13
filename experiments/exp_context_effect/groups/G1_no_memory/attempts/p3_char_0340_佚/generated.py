"""Render 佚 (yi4) — person radical 亻 + 失 — 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(pts, width=5):
    draw.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (person radical) — left column ---
# 撇 (piě): diagonal from upper area down-left
line([(95, 70), (60, 175)], width=5)
# 竖 (shù): vertical descending from mid-撇 downward
line([(85, 130), (85, 245)], width=5)

# --- 失 — right side, centered around x=190 ---
# stroke 1: short 撇 at top (small tick going down-left)
line([(185, 60), (165, 90)], width=5)
# stroke 2: upper horizontal 一
line([(140, 105), (255, 100)], width=5)
# stroke 3: long 撇 — from top-right diagonally down-left through the horizontals
line([(220, 75), (140, 260)], width=5)
# stroke 4: middle horizontal 一 (shorter)
line([(150, 155), (250, 152)], width=5)
# stroke 5: 捺 (nà) — from intersection near middle diagonally down-right
line([(190, 160), (270, 260)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_佚.png")
img.save(out_path)
print(f"saved {out_path}")
