"""
併 = 亻 (left) + 并 (right)
Structure:
  Left: 亻 — top 撇 + tall 竖
  Right (并):
    two short slanted marks at top (丷: 撇 left, 点/short-撇 right)
    long 一 horizontal crossing under them
    a short 一 mid-way + two 竖 descending, right one slightly longer
    (final stroke often 竖 with slight hook)
Sibling note: no sibling-risk radical directly (亻 not in list).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def brush(pts, w0=6, w1=6):
    # taper by drawing multiple lines with decreasing width along path
    n = len(pts) - 1
    for i in range(n):
        t = i / max(n - 1, 1)
        w = int(round(w0 * (1 - t) + w1 * t))
        d.line([pts[i], pts[i + 1]], fill="black", width=max(w, 2))

# --- 亻 (left component) ---
# 撇: from upper area down-left, starts near top of 竖
brush([(85, 65), (72, 105), (52, 160)], w0=7, w1=3)
# 竖: long vertical, starts from where 撇 begins
line([(83, 90), (83, 250)], width=7)

# --- 并 (right component) ---
# Two top 丷: left short 撇, right short 点/撇
brush([(155, 70), (143, 105)], w0=6, w1=3)   # left mark (slants left-down)
brush([(215, 70), (228, 105)], w0=3, w1=6)   # right mark (slants right-down like 点)

# Long horizontal 一 crossing under top marks
line([(128, 125), (260, 122)], width=6)

# Two verticals — extend UP through the top 一 slightly, descend long
line([(163, 115), (163, 250)], width=7)     # left vertical (through top 一)
line([(230, 115), (230, 262)], width=7)     # right vertical (a bit lower)

# Middle small horizontal, crossing both verticals
line([(145, 180), (250, 178)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0398_併/01_併.png")
print("saved")
