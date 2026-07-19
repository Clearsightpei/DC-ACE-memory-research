# p1_stroke_09_横撇 — G3 (coord-bank)
# 横撇 = 横 (horizontal, slight rise) then sharp turn down-left as 撇 (slanting sweep).
# Coordinate-only format. 300x300, white bg, black ink.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# --- 横 segment ---
# Start upper-left area, sweep right with subtle rise; slight thickening toward the turn.
heng_start = (70, 110)
heng_end   = (215, 100)   # ends slightly higher than start (rise)
# taper: thin -> slightly thicker (calligraphic 横 ends with a 顿笔 hook into 撇 turn)
for i, w in enumerate([7, 7, 8, 8, 9]):
    # draw overlapping segments for smoothness
    t = i / 4.0
    x = heng_start[0] + (heng_end[0] - heng_start[0]) * t
    y = heng_start[1] + (heng_end[1] - heng_start[1]) * t
    d.ellipse([x - w/2, y - w/2, x + w/2, y + w/2], fill="black")

# main heng shaft
d.line([heng_start, heng_end], fill="black", width=8)

# small 顿笔 (pause/press) at the corner before turning
corner = (218, 103)
d.ellipse([corner[0]-7, corner[1]-6, corner[0]+8, corner[1]+9], fill="black")

# --- 撇 segment ---
# Turn sharply down-left, tapering to a fine tip.
pie_start = (218, 108)
pie_end   = (135, 235)   # sweeps down and to the left
# taper via decreasing-width overlapping strokes
steps = 24
for i in range(steps):
    t0 = i / steps
    t1 = (i + 1) / steps
    x0 = pie_start[0] + (pie_end[0] - pie_start[0]) * t0
    y0 = pie_start[1] + (pie_end[1] - pie_start[1]) * t0
    x1 = pie_start[0] + (pie_end[0] - pie_start[0]) * t1
    y1 = pie_start[1] + (pie_end[1] - pie_start[1]) * t1
    # width: 10 near top, tapering to 1 at tip
    w = max(1, int(round(10 - 9 * t0)))
    d.line([(x0, y0), (x1, y1)], fill="black", width=w)

img.save("01_横撇.png")
print("saved 01_横撇.png", img.size)
