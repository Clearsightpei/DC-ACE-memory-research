"""p3_char_0567_桌 — G2 free-form render, revision 2.

Structure (10 strokes): top 卜 (短横 + 短竖) → 日 → 木 (横 竖 撇 捺).
Applying TIER-0.F 4-move (tapered strokes, shoulder dabs, bezier).
TIER-0.H (touching): 日 bottom sits on 木's 横; 木 竖 comes out of 日.

Rev 2 fixes: denser dab spacing, closer component packing.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")

def stroke(pts, widths):
    if len(pts) < 2:
        return
    if isinstance(widths, (int, float)):
        widths = [widths] * len(pts)
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        seg_len = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        n_seg = max(int(seg_len * 3), 20)
        for j in range(n_seg + 1):
            t = j / n_seg
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            dab(x, y, w / 2)

def bez(p0, p1, p2, p3, n=80):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3 * p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        out.append((x, y))
    return out

# --- TOP: 卜 (a 短横 with a small 点/hook, plus a 短竖) ---
stroke([(122, 55), (178, 52)], [4.5, 6])       # 短横
stroke([(178, 52), (180, 62)], [6, 2])         # tiny hook at right end
stroke([(150, 55), (150, 88)], [5.5, 6])       # 短竖 into 日 top

# --- MIDDLE: 日 box (compact, centered) ---
# top edge
stroke([(112, 88), (188, 88)], [6, 6])
# left 竖
stroke([(112, 88), (112, 158)], [6, 6])
# right side (横折竖) with shoulder dab at corner
dab(188, 88, 4)
stroke([(188, 88), (188, 158)], [6, 6])
# middle 横
stroke([(112, 123), (188, 123)], [5, 5])
# bottom 横 of 日 — placed to sit right on top of 木's 横
stroke([(112, 158), (188, 158)], [6, 6])

# --- BOTTOM: 木 (touches 日) ---
# 横 of 木 — wide, slightly below 日 bottom (touching)
stroke([(45, 175), (255, 175)], [6.5, 7])
# 竖 of 木 — from 日's interior down through 横, long descender
stroke([(150, 130), (150, 265)], [6, 7])
# 撇 — bezier taper thick→thin, springing from junction of 木's 横 and 竖
pie = bez((150, 178), (128, 205), (95, 235), (55, 272), n=80)
for i, (x, y) in enumerate(pie):
    t = i / (len(pie) - 1)
    w = 7.0 * (1 - t) + 1.4 * t
    dab(x, y, w / 2)
# 捺 — S-curve, thin start, swell, slight flare
na = bez((150, 178), (178, 210), (215, 240), (250, 272), n=80)
for i, (x, y) in enumerate(na):
    t = i / (len(na) - 1)
    if t < 0.75:
        w = 2.0 + 6.0 * (t / 0.75)
    else:
        w = 8.0 - 3.0 * ((t - 0.75) / 0.25)
    dab(x, y, w / 2)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0567_桌/01_桌.png")
print("saved")
