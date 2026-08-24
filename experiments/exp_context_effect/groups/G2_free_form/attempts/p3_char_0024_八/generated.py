"""Render 八 (bā) — two-stroke character: 撇 (left) + 捺 (right).

Revision 1: after comparing to GT.
  - GT's 撇 is SHORT and sits in the LEFT area; not tall/centered.
  - GT's 捺 starts noticeably right of the 撇's start, with a clear TOP GAP.
  - Both strokes end near the bottom baseline (~y=245) but do NOT span
    the full canvas height — they occupy roughly y=65..245.
  - The 捺 has a broad flat foot with a slight terminal tail-out.
  - The 撇 in GT actually has a slight rightward-then-leftward curve
    and ends with a mild upward hook flick to the left.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_stroke(points, widths):
    for (x, y), r in zip(points, widths):
        bbox = (x - r, y - r, x + r, y + r)
        draw.ellipse(bbox, fill=BLACK)


def sample_bezier(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# --- 撇 (left flick) ---
# Positioned in the LEFT-center of the canvas. Start with a 顿 dab,
# curve slightly rightward-bowing then sweep down-left.
# In GT the 撇 sits in the left half, medium length.
pie_p0 = (115, 110)   # start (upper-left area)
pie_p1 = (105, 175)   # control — gentle bow
pie_p2 = (75, 245)    # end (lower-left)
pie_pts = sample_bezier(pie_p0, pie_p1, pie_p2, n=90)

pie_widths = []
n = len(pie_pts)
for i in range(n):
    t = i / (n - 1)
    if t < 0.06:
        r = 7.0  # 顿 dab
    else:
        r = 6.5 * (1 - t) ** 0.85 + 1.3
    pie_widths.append(r)
brush_stroke(pie_pts, pie_widths)

# --- 捺 (right press) ---
# Starts HIGHER-RIGHT than 撇's top, with a clear TOP GAP horizontally
# between the two starts. Thin apex → thickens → broad foot.
na_p0 = (175, 80)    # start upper (right of 撇 start; gap ~60px)
na_p1 = (210, 165)   # control — gentle bow
na_p2 = (248, 245)   # broad foot on lower-right
na_pts = sample_bezier(na_p0, na_p1, na_p2, n=100)
na_widths = []
n = len(na_pts)
for i in range(n):
    t = i / (n - 1)
    if t < 0.82:
        r = 1.2 + 7.2 * t  # gradually thickens
    else:
        # Foot region — stay thick, then slight taper at tip.
        r = 8.5 - (t - 0.82) * 22
        if r < 2.0:
            r = 2.0
    na_widths.append(r)
brush_stroke(na_pts, na_widths)

# Small horizontal tail-out at the foot of the 捺 (calligraphic release).
tail_start = na_p2
tail_end = (265, 246)
tail_pts = []
for i in range(15):
    t = i / 14
    x = tail_start[0] + (tail_end[0] - tail_start[0]) * t
    y = tail_start[1] + (tail_end[1] - tail_start[1]) * t
    tail_pts.append((x, y))
tail_widths = [max(1.0, 4.0 * (1 - i / 14)) for i in range(15)]
brush_stroke(tail_pts, tail_widths)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0024_八/01_八.png")
print("wrote 01_八.png")
