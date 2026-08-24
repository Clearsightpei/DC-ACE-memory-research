"""
经 (jing) — 8 strokes, left-right layout.
Left: 纟 (silk radical, simplified: 撇折 + 撇折 + 提) — 3 strokes.
Right: 圣 (又 top + 土 bottom) — 5 strokes.

Revision 1: better-connected 撇折 for 纟, tighter 又 with 横撇 joined,
土 with 竖 touching top 横.
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

def bezier(pts, steps=80):
    out = []
    if len(pts) == 3:
        (x0,y0),(x1,y1),(x2,y2) = pts
        for i in range(steps+1):
            t = i/steps
            u = 1-t
            x = u*u*x0 + 2*u*t*x1 + t*t*x2
            y = u*u*y0 + 2*u*t*y1 + t*t*y2
            out.append((x,y))
    elif len(pts) == 4:
        (x0,y0),(x1,y1),(x2,y2),(x3,y3) = pts
        for i in range(steps+1):
            t = i/steps
            u = 1-t
            x = u*u*u*x0 + 3*u*u*t*x1 + 3*u*t*t*x2 + t*t*t*x3
            y = u*u*u*y0 + 3*u*u*t*y1 + 3*u*t*t*y2 + t*t*t*y3
            out.append((x,y))
    return out

def stroke(pts, width=8):
    for i in range(len(pts)-1):
        draw.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        draw.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill="black")

# ---------- LEFT: 纟 (silk radical) ----------
# 撇折 #1: single continuous stroke — down-left curve then折 up-right
s1 = bezier([(95,85),(78,110),(72,128),(102,120)])
stroke(s1, width=6)

# 撇折 #2: same shape below
s2 = bezier([(102,140),(83,163),(77,180),(112,168)])
stroke(s2, width=6)

# 提 (bottom): rising from lower-left to upper-right, with a tip
ti = bezier([(72,215),(90,205),(118,195)])
stroke(ti, width=7)
draw.polygon([(114,192),(122,196),(115,204)], fill="black")

# ---------- RIGHT: 圣 (又 + 土) ----------
# 横撇: horizontal then diagonal-down-left as one continuous stroke
hp1 = [(155,75),(245,75)]  # horizontal part
stroke(hp1, width=8)
hp2 = bezier([(245,75),(220,120),(165,180)])  # 撇 dropping
stroke(hp2, width=8)

# 捺: from area near junction going down-right
na = bezier([(200,110),(230,150),(260,195)])
stroke(na, width=9)
# thickening flare at end of 捺
draw.polygon([(253,188),(268,193),(258,205)], fill="black")

# Bottom 土:
# top short 横
stroke([(175,215),(255,215)], width=8)
# 竖 touching top 横 and extending to bottom
stroke([(215,210),(215,258)], width=9)
# long bottom 横
stroke([(155,262),(275,262)], width=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0375_经/01_经.png")
print("wrote 01_经.png")
