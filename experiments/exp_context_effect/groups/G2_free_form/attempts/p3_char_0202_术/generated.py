"""
术 — p3_char_0202
# SIGNATURE CHECK (from sibling_signature_checklist.md row 术):
#   术 = 木 + interior 点 upper-right
#   木 body = 一 (horizontal) + 竖 (vertical) + 人-body (撇+捺, apex ON the 一)
#   Plus: an interior 丶 (dot) placed in the upper-right quadrant
#         (between the top of the 竖 and the right end of the 一).
# Distinguish from 木 (no dot), 未 (short-over-long horizontals),
# 末 (long-over-short horizontals).
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BRUSH = 9

def line(p1, p2, width=BRUSH):
    d.line([p1, p2], fill=INK, width=width)

def taper(p1, p2, w_start, w_end, steps=40):
    """Draw a tapered stroke by stacking small circles from p1 to p2."""
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        r = (w_start + (w_end - w_start) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# --- 一 (top horizontal), slightly wavy, crosses the 竖 near y~130 ---
# Extend from ~x=55 to ~x=245
taper((55, 132), (245, 128), w_start=8, w_end=10)

# --- 竖 (vertical), from top (~y=80) down to bottom (~y=275), through the 一 ---
taper((150, 78), (150, 278), w_start=8, w_end=9)

# --- 撇 (left-falling stroke), starting from the 一/竖 intersection area, sweeping down-left ---
# Apex on the 一 near (150, 132). Curve to lower-left corner.
# Use a two-segment curve to give it a natural sweep.
taper((150, 135), (100, 200), w_start=9, w_end=7)
taper((100, 200), (55, 275), w_start=7, w_end=4)

# --- 捺 (right-falling stroke), same apex, sweeping down-right ---
# Slight arc toward lower-right with a broader foot.
taper((150, 135), (200, 210), w_start=8, w_end=9)
taper((200, 210), (255, 270), w_start=9, w_end=11)

# --- 丶 (interior dot), upper-right quadrant, between top of 竖 and right end of 一 ---
# Small teardrop-ish dot slanting down-right
taper((185, 100), (205, 118), w_start=5, w_end=10)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0202_术/01_术.png"
img.save(out)
print("saved", out)
