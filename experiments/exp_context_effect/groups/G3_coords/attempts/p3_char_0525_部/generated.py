# BANK_DEVIATION
# skipped: (no 阝 or 立 primitive in bank; kou.py is turtle-based and would clash with PIL inline)
# reason: 部 = 咅 (立+口) left + 阝 right; GT shows thin uniform strokes; no bank fit
# fresh_component: bu_char_inline (咅 left compressed + 阝 right using heng_pie_wan_gou + long shu)
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5  # thin uniform line width (matches MMH GT)

def line(a, b, w=LW):
    d.line([a, b], fill="black", width=w)

# ============ LEFT: 咅 (立 on top of 口), occupying ~x 20..135 ============

# ---- 立 (top part), roughly y 30..135 ----
# 1) top dian (short slanted stroke)
line((72, 40), (82, 55), w=LW)

# 2) upper heng (short)
line((45, 70), (110, 70))

# 3) left small pie (short slanted /)
line((55, 85), (48, 100))

# 4) right small dian (short slanted \)
line((100, 85), (108, 100))

# 5) bottom heng of 立 (wide baseline)
line((28, 130), (135, 130))

# ---- 口 (bottom-left), roughly x 40..120, y 150..215 ----
# left shu
line((45, 150), (45, 210))
# top heng-zhe: heng then shu down
line((45, 150), (118, 150))
line((118, 150), (118, 210))
# bottom heng
line((45, 210), (118, 210))

# ============ RIGHT: 阝 (right ear), occupying x ~170..250 ============
# 阝 = 横撇弯钩 (top loop) + 竖 (long vertical below)

# 1) 横撇弯钩 (heng-pie-wan-gou): starts with short heng, then diagonal pie down,
#    then curves right-down to form a loop closing back to a horizontal-ish base
# Draw as a series of connected line segments approximating the loop
# Start: top-left of loop
pts = [
    (175, 75),   # top-left start of heng
    (215, 75),   # short heng right
    (240, 100),  # pie down-right
    (235, 135),  # curve down (wan)
    (215, 150),  # curve back left (gou-like bottom)
    (180, 150),  # close to left
]
for i in range(len(pts) - 1):
    line(pts[i], pts[i+1])

# 2) 竖 (long vertical shu), passes from top through to bottom on the right side
# The vertical anchor for 阝 is at the "hinge" of the loop (around x=180)
line((180, 75), (180, 275))

out_path = os.path.join(os.path.dirname(__file__), "01_部.png")
img.save(out_path)
print("wrote", out_path)
