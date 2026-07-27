"""Render 以 (yǐ) at 300x300, white background, black ink.

以 has 4 strokes:
  1. Short 撇 (left-falling) — upper left
  2. 竖提 (vertical-then-rising-hook) — long stroke going down then hooking up-right
  3. Small 点 (dot) — upper right area (small short slanted mark)
  4. Long 捺 (right-falling sweep) — from middle-upper sweeping down-right
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5

def quad_bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

def stroke(pts, width=LW):
    draw.line(pts, fill=INK, width=width, joint="curve")

# --- Left component (like a 竖 with 提, plus a short 撇 dot on top) ---

# Stroke 1: short 撇 in upper-left — slants down-left slightly
s1 = quad_bezier((105, 100), (100, 125), (92, 150), n=20)
stroke(s1)

# Stroke 2: 竖提 — vertical stroke down, curving slightly, then hook up to right
# Start upper-mid-left, go down, then flick up-right
s2_down = quad_bezier((115, 130), (100, 190), (115, 225), n=40)
s2_hook = quad_bezier((115, 225), (135, 225), (155, 205), n=25)
stroke(s2_down + s2_hook)

# --- Right component (人-like) ---

# Stroke 3: small dot / short slanted stroke — upper right, short
s3 = quad_bezier((180, 115), (183, 128), (188, 145), n=15)
stroke(s3)

# Stroke 4: long 捺 sweeping from middle-upper down and right to bottom-right
s4 = quad_bezier((175, 130), (205, 195), (250, 245), n=50)
stroke(s4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0098_以/01_以.png")
print("saved")
