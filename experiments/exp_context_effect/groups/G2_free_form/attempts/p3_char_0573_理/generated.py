"""理 (lǐ) — 11 strokes
Structure: 王字旁 (left, ~1/3 width) + 里 (right, ~2/3 width, main body).

Left radical 王字旁 (4 strokes) — compressed to the LEFT third:
 1. 横 (top short)
 2. 横 (middle shorter)
 3. 竖 (through the three horizontals)
 4. 提 (rising rightward stroke — the "王 → 王字旁" signature;
    replaces the bottom flat 横 of standalone 王)

Right body 里 (7 strokes):
 5. 竖 (left vertical of top 日)
 6. 横折 (top + right vertical of top 日)
 7. 横 (middle horizontal inside 日)
 8. 横 (bottom of 日 / top of 土)
 9. 竖 (central long vertical through into 土)
10. 横 (middle horizontal of lower 土)
11. 横 (bottom horizontal — widest)

# COMPONENT-TOUCH rule (TIER-0 H): the 提's right terminal MUST
# push into (or touch) the left edge of the right 日 body.
# Signature: 王 → 王字旁 last stroke is 提 (rising), not flat 横.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(p0, p1, w_start, w_end, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w_start + (w_end - w_start) * t
        r = w / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def stroke(pts, width=9):
    """Polyline stroke with round dabs at joints."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=INK)


# ---------- LEFT: 王字旁 (compressed vertically too) ----------
# Occupies x ~ 40..115, vertically compressed to sit within the top ~2/3
# of the character so it visually pairs with 里's top 日, not with the
# full 里 height. GT: 王字旁 top ~y=70, 提 tip ~y=155.
LX, RX = 45, 110
Y1, Y2 = 75, 120      # top and middle 横
Y3 = 175              # 提 base

# 1. top 横 (slight up-tilt)
brush_line((LX, Y1+2), (RX, Y1-2), 7, 6, steps=50)
d.ellipse((LX-4, Y1-2, LX+4, Y1+6), fill=INK)  # 顿 dab at start
d.ellipse((RX-4, Y1-6, RX+4, Y1+2), fill=INK)  # end dab

# 2. middle 横 (shortest)
brush_line((LX+5, Y2+1), (RX-5, Y2-1), 6, 5, steps=50)
d.ellipse((LX+1, Y2-3, LX+9, Y2+5), fill=INK)
d.ellipse((RX-9, Y2-5, RX-1, Y2+3), fill=INK)

# 3. 竖 through-axis (slightly left of center of the radical)
CX_L = (LX + RX) // 2 - 2
brush_line((CX_L, Y1-6), (CX_L, Y3-2), 8, 7, steps=60)
d.ellipse((CX_L-6, Y1-10, CX_L+6, Y1+2), fill=INK)  # 顿 dab at top

# 4. 提 — rising rightward (from bottom-left up to right, touching 里)
# Start low-left, end high-right (thicker at start, tapering to thin tip)
p_start = (LX - 3, Y3 + 5)
p_end = (145, Y3 - 20)   # tip pushes into the left edge of 里
brush_line(p_start, p_end, 10, 3, steps=60)
# 顿 dab at start of 提
d.ellipse((p_start[0]-6, p_start[1]-6, p_start[0]+6, p_start[1]+6), fill=INK)


# ---------- RIGHT: 里 body ----------
# Top 日: roughly cols 145..235, rows 50..145
BX_L, BX_R = 150, 235
T = 55
MID = 105
BOT_RI = 150  # bottom of 日 / top-shelf of 土

# 5. 竖: left vertical of 日
stroke([(BX_L, T+3), (BX_L, BOT_RI)], width=9)

# 6. 横折: top horizontal + right vertical
stroke([(BX_L-4, T), (BX_R, T+3), (BX_R, BOT_RI)], width=9)

# 7. 横: middle horizontal inside 日
stroke([(BX_L+3, MID), (BX_R-3, MID)], width=7)

# 8. 横: bottom of 日
stroke([(BX_L-2, BOT_RI), (BX_R+2, BOT_RI)], width=9)

# 9. 竖: central vertical through 日 and 土
CX_R = (BX_L + BX_R) // 2
stroke([(CX_R, T+14), (CX_R, 250)], width=10)

# 10. 横: middle horizontal of lower 土
stroke([(BX_L-5, 205), (BX_R+5, 205)], width=8)

# 11. 横: bottom horizontal — WIDEST stroke of the whole character
stroke([(130, 260), (270, 258)], width=11)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0573_理/01_理.png")
print("saved 理")
