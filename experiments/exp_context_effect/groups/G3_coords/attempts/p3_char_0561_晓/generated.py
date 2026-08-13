# BANK_DEVIATION
# skipped: ri.py, er_ren.py
# reason: 日 must be compressed narrow (LR-left slot ~85px wide, tall aspect);
#         儿 legs must be small in the bottom-right of 尧 with matching scale.
#         Both bank entries have hard-coded x-coords that don't fit here;
#         inlining fresh keeps proportions faithful to the GT.
# fresh_component: ri_LR_left_narrow, er_ren_for_yao_bottom
"""晓 (xiao) — left-right: 日 (left) + 尧 (right). Phase-3 char."""
import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
img = Image.new("RGB", (300, 300), (255, 255, 255))
t = ImageDraw.Draw(img)

# ============================================================
# LEFT: 日 (compressed narrow for LR-left slot)
# ============================================================
xL_left = 35
xL_right = 105
yL_top = 65
yL_bot = 215
yL_mid = 145
wL = 8
# left 竖
t.line([(xL_left, yL_top), (xL_left, yL_bot)], fill=(0, 0, 0), width=wL)
# 横折 (top + right shu)
t.line([(xL_left, yL_top), (xL_right, yL_top)], fill=(0, 0, 0), width=wL)
t.line([(xL_right, yL_top), (xL_right, yL_bot)], fill=(0, 0, 0), width=wL)
# middle 横 (slight right gap)
t.line([(xL_left + 3, yL_mid), (xL_right - 5, yL_mid)], fill=(0, 0, 0), width=6)
# bottom 横
t.line([(xL_left, yL_bot), (xL_right, yL_bot)], fill=(0, 0, 0), width=wL)

# ============================================================
# RIGHT: 尧
# Components (top to bottom):
#   - Small top 撇 + short slash forming the top "戈-ish" area
#   - Short horizontal below the top zone
#   - Long 一 across the middle-lower zone
#   - 兀-bottom (儿 legs: 撇 + 竖弯钩)
# ============================================================

# Top-left 撇 (longer, pointing down-left, forming the top diagonal)
t.line([(200, 45), (155, 130)], fill=(0, 0, 0), width=8)
# Top-right short 点 (small dot-like stroke, upper-right)
t.line([(215, 60), (235, 85)], fill=(0, 0, 0), width=7)
# Small 横 (short, crossing the 撇 mid-way — the little "土"-ish crossbar)
t.line([(165, 105), (215, 105)], fill=(0, 0, 0), width=6)
# Middle-lower long 一 (the top of 兀)
t.line([(130, 170), (275, 170)], fill=(0, 0, 0), width=8)

# 兀-bottom = 儿 legs
# Left leg: 撇 from just under the heng, curving down-left
# Using two segments for a slight curve
t.line([(170, 180), (150, 230)], fill=(0, 0, 0), width=8)
t.line([(150, 230), (140, 280)], fill=(0, 0, 0), width=8)

# Right leg: 竖弯钩 — straight down, then curves right, then hook up
t.line([(230, 180), (232, 245)], fill=(0, 0, 0), width=9)
t.line([(232, 245), (275, 265)], fill=(0, 0, 0), width=9)
# hook up
t.line([(275, 265), (275, 245)], fill=(0, 0, 0), width=8)

out_path = os.path.join(OUT_DIR, "01_晓.png")
img.save(out_path)
print(f"Saved {out_path}")
