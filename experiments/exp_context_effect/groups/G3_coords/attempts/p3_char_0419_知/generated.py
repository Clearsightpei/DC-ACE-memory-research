# BANK_DEVIATION
# skipped: kou.py (turtle-based; whole-char cleaner in PIL for cursive-thin GT)
# reason: GT is thin-uniform hand-drawn strokes; mixing turtle-bank kou with
#         inline PIL 矢 mismatches widths and axis conventions
# fresh_component: zhi_char_inline (矢 + 口 both inline PIL)
#
# 知 = 矢 (left, ~55% width) + 口 (right, ~40% width).
# GT is cursive/thin. Uniform 5px lines throughout.

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

# --- LEFT: 矢 (arrow, 5 strokes) ---
# 1) top small 撇 (pie), from ~(70,35) down-left to (48,72)
d.line([(72, 32), (46, 78)], fill="black", width=LW)

# 2) upper 横 (short heng), from (52, 88) to (135, 85)
d.line([(50, 92), (138, 82)], fill="black", width=LW)

# 3) middle 横 (longer heng), from (30, 148) to (160, 143) — the crossing heng
d.line([(28, 150), (162, 140)], fill="black", width=LW)

# 4) long 撇 (pie), from (105, 100) sweeping down-left to (22, 280)
# use polyline for slight curve
d.line([(108, 100), (95, 145), (75, 195), (48, 240), (22, 280)],
       fill="black", width=LW)

# 5) 捺 (na), from crossing ~(100, 155) down-right to (170, 260)
d.line([(100, 158), (125, 200), (150, 235), (172, 260)],
       fill="black", width=LW)

# --- RIGHT: 口 (mouth), placed middle-right, aligned with heng ---
# Box roughly (185, 122) to (275, 225)
# stroke 1: 竖 (left shu) — from TL down to BL
d.line([(188, 122), (185, 225)], fill="black", width=LW)
# stroke 2: 横折 (top heng into right shu)
d.line([(188, 122), (275, 125)], fill="black", width=LW)
d.line([(275, 125), (278, 225)], fill="black", width=LW)
# stroke 3: 横 (bottom heng, slightly inset for calligraphic feel)
d.line([(188, 225), (282, 228)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_知.png")
img.save(out)
print(f"wrote {out}")
