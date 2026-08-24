"""
亨 (hēng/xiǎng) - 7 strokes
Structure: 亠 (top: dot + long horizontal) + 口 (small mouth) + 了 (bottom hook)

Strokes:
1. 丶 dot on top
2. 一 long horizontal
3. 丨 left vertical of 口
4. ??? top+right of 口 (横折)
5. 一 bottom of 口
6. 横钩 (short horizontal with left-down hook - the 冖 top of 了 element)
7. 竖钩 with curve at bottom (the 了 hook)

Hook rule: hook flicks UP-and-LEFT into the character body.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(pts, width=6):
    """Draw a stroke through a list of points using line segments with round joints."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        draw.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

def bezier(p0, p1, p2, n=30):
    """Quadratic bezier for curves."""
    out = []
    for i in range(n+1):
        t = i / n
        x = (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        out.append((x, y))
    return out

# Stroke 1: 丶 (dot at top) - short slanting dot
stroke([(158, 22), (168, 40)], width=7)

# Stroke 2: 一 (long horizontal) - top of 亠
stroke([(40, 62), (260, 60)], width=6)

# ---- 口 (small mouth) in middle-upper ----
# Small square roughly centered horizontally
L, R = 118, 190
T, B = 82, 122

# Stroke 3: left vertical of 口
stroke([(L, T), (L, B)], width=6)

# Stroke 4: 横折 (top + right side of 口) - one stroke
stroke([(L, T), (R, T), (R, B)], width=6)

# Stroke 5: bottom horizontal of 口 (小 slightly wider closing)
stroke([(L-2, B), (R+2, B)], width=6)

# ---- 冖-like 横钩 (roof with hook) below 口 ----
# Stroke 6: long horizontal, then small hook down-left at right end
h_pts = [(38, 152), (260, 148)]
stroke(h_pts, width=6)
# small hook flicking down-left from right end
stroke([(260, 148), (252, 168)], width=6)

# ---- Stroke 7: 了-like 竖钩 with big curve at bottom ----
# vertical descending from top center, curves left near bottom, then hooks up-left
curve = bezier((155, 152), (155, 240), (95, 275), n=40)
pts = [(int(x), int(y)) for x, y in curve]
stroke(pts, width=6)
# Hook: flick UP-and-LEFT at the end of the curve
end = pts[-1]
hook_end = (end[0] - 15, end[1] - 22)
stroke([end, hook_end], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0306_亨/01_亨.png")
print("wrote 01_亨.png")
