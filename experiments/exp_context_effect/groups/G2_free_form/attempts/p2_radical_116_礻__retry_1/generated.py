"""
Render 礻 (radical 116, 4 strokes).

Structure: 4 strokes = 丶 (top dot) + 横撇 (short horizontal + shoulder + long left-flick)
+ 竖 (central vertical) + 丶 (bottom-right dot).

Retry_1 fix (per errata): keep 4 clear strokes, ONE bottom-right dot (not two — that's 衤).
Also make strokes cleaner/less blocky than first attempt.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")

def stroke_line(pts, width_start, width_end):
    # tapered polyline via dabs interpolated along segments
    total_len = 0
    segs = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        seg_len = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        segs.append(seg_len)
        total_len += seg_len
    if total_len == 0:
        return
    covered = 0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        seg_len = segs[i]
        steps = max(2, int(seg_len))
        for s in range(steps + 1):
            t_local = s / steps
            x = x0 + (x1 - x0) * t_local
            y = y0 + (y1 - y0) * t_local
            t_global = (covered + t_local * seg_len) / total_len
            r = width_start * (1 - t_global) + width_end * t_global
            dab(x, y, r / 2)
        covered += seg_len

# --- Stroke 1: top dot 丶 (a short teardrop, slanting down-right) ---
# centered roughly at (150, 55)
stroke_line([(147, 45), (156, 68)], width_start=3, width_end=9)

# --- Stroke 2: 横撇 (horizontal then long left-down flick) ---
# short horizontal from (100, 90) to (170, 88), shoulder, then long 撇 down to (75, 195)
# Do as two connected segments with taper.
# horizontal part
stroke_line([(100, 92), (172, 88)], width_start=8, width_end=9)
# shoulder + 撇 tapering to point
stroke_line([(172, 88), (168, 110), (135, 150), (75, 200)], width_start=10, width_end=2)

# --- Stroke 3: central 竖 (vertical) ---
# from ~(150, 100) down to (150, 260)
stroke_line([(150, 100), (150, 265)], width_start=9, width_end=8)

# --- Stroke 4: bottom-right dot 丶 ---
# to the right of the 竖, around (200, 180)
stroke_line([(175, 170), (215, 205)], width_start=4, width_end=11)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_116_礻__retry_1/01_礻.png")
print("saved")
