from PIL import Image, ImageDraw
import os, math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6

def stroke(pts, w=W):
    d.line(pts, fill="black", width=w, joint="curve")
    r = w // 2
    for x, y in [pts[0], pts[-1]]:
        d.ellipse([x-r, y-r, x+r, y+r], fill="black")

def curve(ctrl, w=W, steps=60):
    n = len(ctrl) - 1
    prev = ctrl[0]
    for i in range(1, steps + 1):
        t = i / steps
        x = 0.0; y = 0.0
        for k, (px, py) in enumerate(ctrl):
            b = math.comb(n, k) * (t ** k) * ((1 - t) ** (n - k))
            x += px * b; y += py * b
        stroke([prev, (x, y)], w=w)
        prev = (x, y)

# 代 — 亻 (left) + 弋 (right)

# --- 亻 radical ---
# 撇 (piě): from top down-left with slight curve
curve([(110, 70), (100, 110), (85, 155), (60, 220)], w=6, steps=50)
# 竖 (shù): straight vertical from a joint on the piě
stroke([(105, 130), (108, 265)], w=6)

# --- 弋 component ---
# 横 (héng): horizontal near top, slight upslope
stroke([(155, 105), (240, 92)], w=6)

# 斜钩 (xié-gōu): from just below-left of héng's start, gentle curve down-right,
# ending with an upward hook
curve([(170, 118), (185, 165), (210, 220), (245, 268)], w=6, steps=60)
# hook flick upward-right
stroke([(245, 268), (268, 250)], w=6)

# 点 (diǎn): small dot in upper-right, above/right of héng end
stroke([(230, 65), (248, 88)], w=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_代.png"))
print("saved")
