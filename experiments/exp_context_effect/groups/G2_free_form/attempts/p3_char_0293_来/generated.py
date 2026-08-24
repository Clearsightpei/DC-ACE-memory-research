"""
来 — p3_char_0293
Structure: 一 (short top) + two tiny strokes flanking 竖 (left 撇 + right 丶)
         + 一 (long middle) + 竖 (through both horizontals)
         + 撇 + 捺 (from middle 一 down like 木-body)
7 strokes total.

Reference: passed 术 attempt uses same 木-body geometry.
Difference from 木/术: 来 has an extra small top 一 + two flanking dots
between the top 一 and the middle 一.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def taper(p1, p2, w_start, w_end, steps=40):
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        r = (w_start + (w_end - w_start) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# --- Stroke 1: short top 一 (upper horizontal), ~y=62 ---
taper((105, 62), (200, 60), w_start=7, w_end=9)

# --- Stroke 2 & 3: two small flanking strokes below top 一 ---
# left: small 撇 (down-left flick)
taper((135, 85), (115, 115), w_start=8, w_end=4)
# right: small 丶 (dot/short stroke down-right)
taper((170, 85), (190, 115), w_start=5, w_end=10)

# --- Stroke 4: main middle 一 (longer horizontal), ~y=150 ---
taper((50, 152), (250, 148), w_start=8, w_end=10)

# --- Stroke 5: 竖 (vertical) through top-1, middle-1, down to bottom ---
taper((153, 55), (153, 275), w_start=7, w_end=9)

# --- Stroke 6: 撇 (left-falling from middle 一 area) ---
taper((153, 155), (105, 215), w_start=9, w_end=7)
taper((105, 215), (55, 275), w_start=7, w_end=4)

# --- Stroke 7: 捺 (right-falling from middle 一 area) ---
taper((153, 155), (200, 215), w_start=8, w_end=9)
taper((200, 215), (255, 270), w_start=9, w_end=11)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0293_来/01_来.png"
img.save(out)
print("saved", out)
