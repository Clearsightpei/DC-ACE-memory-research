"""
Render 留 (liu2) at 300x300, black ink on white.

Structural read from GT:
  Top-left  (卯 left):  撇 sweeping down-left + a short 折 dab.
  Top-right (卯 right): 横折钩 (open box with UP-LEFT hook) + inner 竖.
  Bottom:              田 — 5 strokes: 竖 / 横折 / 中横 / 中竖 / 底横.

Applies TIER-0 F: bez curves, teardrop taper on 撇/点, shoulder dabs
at every 折, and hook flick UP-and-LEFT into the character body.
Components touch (H rule): top row sits flush on 田's top edge.
"""
from PIL import Image, ImageDraw

W = H = 300
OUT = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0535_留/01_留.png"

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line(a, b, w=6):
    pts = bez(a, ((a[0]+b[0])/2, (a[1]+b[1])/2),
              ((a[0]+b[0])/2, (a[1]+b[1])/2), b, n=40)
    stroke(pts, (w, w))

def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ============================================================
# TOP-LEFT (卯 left half): a diagonal 撇 + a short 折 (elbow dab)
# ============================================================
# main 撇: from upper-center-left down-left
pie = bez((95, 45), (80, 90), (65, 125), (50, 160), n=70)
stroke(pie, (10, 4))
# short elbow / 折 attached mid-height on the 撇
elbow_h = bez((72, 105), (95, 105), (115, 105), (130, 105), n=30)
stroke(elbow_h, (6, 6))
# small 竖 dropping from right end of elbow (the "折" foot)
elbow_v = bez((128, 105), (128, 130), (126, 150), (120, 165), n=30)
stroke(elbow_v, (6, 5))
dab(128, 105, r=5)   # shoulder dab

# ============================================================
# TOP-RIGHT (卯 right half): 横折钩 + inner 竖
# ============================================================
# top 横 of the right box
top_h = bez((145, 55), (175, 53), (205, 53), (225, 58), n=40)
stroke(top_h, (6, 6))
# shoulder dab at fold
dab(225, 58, r=6)
# 竖 down from fold, ending with UP-LEFT hook
vert = bez((225, 58), (225, 95), (223, 130), (218, 160), n=50)
stroke(vert, (7, 6))
# hook flick UP-and-LEFT into the body
hook = bez((218, 160), (212, 155), (206, 150), (198, 146), n=25)
stroke(hook, (7, 3))
# inner 竖 (dividing the top-right box)
inner_v = bez((178, 70), (178, 100), (178, 130), (178, 158), n=40)
stroke(inner_v, (6, 5))

# ============================================================
# BOTTOM: 田 (5 strokes) — components touch top row at y≈170
# ============================================================
BL, BR, BT, BB = 78, 222, 170, 275
MX = (BL + BR) // 2   # 150
MY = (BT + BB) // 2   # ~222

# 1) 左竖
left_v = bez((BL, BT), (BL, BT+35), (BL, BT+70), (BL, BB), n=50)
stroke(left_v, (7, 7))

# 2) 横折 (top edge + right edge)
top_edge = bez((BL, BT), (MX, BT-2), (BR-20, BT-2), (BR, BT), n=50)
stroke(top_edge, (7, 7))
dab(BR, BT, r=6)  # shoulder dab
right_v = bez((BR, BT), (BR, BT+35), (BR, BT+70), (BR, BB), n=50)
stroke(right_v, (7, 7))

# 3) 中横
mid_h = bez((BL, MY), (MX-20, MY-1), (MX+20, MY-1), (BR, MY), n=50)
stroke(mid_h, (6, 6))

# 4) 中竖
mid_v = bez((MX, BT), (MX, MY-10), (MX, MY+10), (MX, BB), n=50)
stroke(mid_v, (6, 6))

# 5) 底横
bot_h = bez((BL, BB), (MX-20, BB+1), (MX+20, BB+1), (BR, BB), n=50)
stroke(bot_h, (7, 7))

img.save(OUT)
print("saved", OUT)
