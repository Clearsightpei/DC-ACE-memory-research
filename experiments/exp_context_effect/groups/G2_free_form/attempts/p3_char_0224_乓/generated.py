"""乓 (ping) — 6 strokes.
丘 top (5 strokes: 丿, 一, 丨-short, 一, 一-long) + downward 丿 bottom-right.
Sibling: 乒 has bottom flick on LEFT, 乓 has it on RIGHT.
"""
from PIL import Image, ImageDraw

W = 300
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)

def bezier(p0, p1, p2, width=6, n=30):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        pts.append((x, y))
    line(pts, width=width)

# --- 丘 top (occupies upper 2/3) ---
# Stroke 1: 丿 short top-left flick
bezier((110, 60), (100, 85), (85, 110), width=6)

# Stroke 2: 一 top-mid horizontal (upper bar of the step)
line([(110, 75), (185, 80)], width=6)

# Stroke 3: 丨 short vertical dropping from right end of top bar
line([(185, 80), (185, 130)], width=6)

# Stroke 4: 一 mid horizontal — the second step, starting from lower position on left, extending to right
line([(90, 145), (215, 140)], width=6)

# Stroke 5: 一 long bottom horizontal (base of 丘 / top of 一 in 乓)
line([(40, 210), (270, 205)], width=7)

# Stroke 6: 丿 downward flick at bottom-right (乓 distinguishing feature)
bezier((215, 215), (230, 245), (250, 275), width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0224_乓/01_乓.png")
print("saved")
