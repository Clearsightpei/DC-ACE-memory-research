"""
幺 - character p3_char_0090
3 strokes: 撇折 + 撇折 + 点

Revision: previous attempt was too disconnected. Make strokes smoother
by sampling curves densely; extend top stroke taller (GT shows it
starting from upper-right area with a long diagonal); make each
撇折 read as one continuous flowing curve.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def bezier(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def stroke_curve(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=width)
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x-r, y-r, x+r, y+r), fill=INK)

# --- Stroke 1: upper 撇折 ---
# Diagonal down-left from top area, then flatten and hook slightly right/up
seg1a = bezier((170, 45), (155, 75), (130, 100), (110, 125))   # 撇 part
seg1b = bezier((110, 125), (120, 135), (145, 130), (165, 115))  # 折 + small flick
stroke_curve(seg1a + seg1b, width=6)

# --- Stroke 2: lower 撇折 (larger, sits under first) ---
seg2a = bezier((155, 135), (135, 165), (110, 195), (95, 220))   # 撇
seg2b = bezier((95, 220), (115, 230), (150, 225), (180, 205))   # 折 curving right-up
stroke_curve(seg2a + seg2b, width=6)

# --- Stroke 3: 点 (dot) at bottom-right ---
# Diagonal dab going down-right
dot = bezier((180, 225), (188, 235), (195, 248), (208, 262))
stroke_curve(dot, width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0090_幺/01_幺.png")
print("saved")
