"""Render 痂 (jiā, scab) — 疒 radical enclosing 加 (力+口)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")


# ============================================================
# 疒 radical
# ============================================================
# Top dot (点) — small slanted above the horizontal
d.line([(95, 45), (108, 60)], fill="black", width=5)

# Horizontal top bar (一) — long, slightly tilted
stroke([(55, 78), (240, 72)], w=4)

# 丿 — the long left-diagonal downward-sweeping stroke
stroke([(110, 78), (95, 130), (75, 195), (45, 260)], w=4)

# 冫 (two dots on the inner-left of the enclosure)
# upper dot: short slanted
d.line([(100, 115), (112, 130)], fill="black", width=5)
# lower dot: short upstroke (提)
d.line([(95, 165), (112, 158)], fill="black", width=5)

# ============================================================
# 加 = 力 + 口, positioned to right of 冫, inside 疒
# ============================================================

# --- 力 (leftish, under the top bar) ---
# 横折钩: horizontal → turn down → hook
stroke([(125, 130), (185, 128), (180, 200)], w=4)
# hook at bottom
stroke([(180, 200), (195, 200)], w=4)
# 撇 (long diagonal down-left starting near top-left of the 横折钩)
stroke([(150, 138), (120, 235)], w=4)

# --- 口 (small box, to the right, inside enclosure lower area) ---
# left vertical
stroke([(205, 160), (205, 235)], w=4)
# top horizontal + right vertical
stroke([(205, 158), (265, 160), (263, 235)], w=4)
# bottom horizontal
stroke([(205, 235), (265, 235)], w=4)

# Save
out = os.path.join(os.path.dirname(__file__), "01_痂.png")
img.save(out)
print("Saved:", out)
