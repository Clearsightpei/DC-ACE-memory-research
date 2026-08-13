# BANK_DEVIATION
# skipped: tu.py (draw_tu is turtle-based and uses two heng; for 城's
#          LR-left 土 form the bottom stroke is a 提 (rising), not a heng)
# reason: LR-left 土 form uses 提 not 横 for stroke 3, and needs narrow
#         compressed aspect; tu.py bakes a wider bottom heng.
# fresh_component: tu_LR_left_with_ti
#
# 城 (chéng) — 9 strokes. PIL, 300x300, math-not-needed screen coords.
# Left  土 form (compressed, ti-bottom): 横 竖 提
# Right 成: 横 撇 横折 斜钩 撇 点 (7 in some counts; 城 is 9-stroke)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def seg(p, q, w=5):
    d.line([p, q], fill=BLACK, width=w)
    r = w/2 + 0.5
    d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=BLACK)
    d.ellipse([q[0]-r, q[1]-r, q[0]+r, q[1]+r], fill=BLACK)

def bez(p0, p1, p2, w=5, n=40):
    prev = p0
    for i in range(1, n+1):
        t = i/n
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        cur = (x, y)
        seg(prev, cur, w)
        prev = cur

# ---------- LEFT: 土 (compressed, LR-left form with 提) ----------
# Occupies roughly x in [30, 100], y in [110, 210]. Centered around y=160.
# Stroke 1: 横 top
seg((35, 130), (100, 128), 5)
# Stroke 2: 竖 middle-vertical, drops from top-heng center down
seg((68, 130), (68, 200), 5)
# Stroke 3: 提 rising left-to-right (thicker at start, tapers/rises to right)
bez((32, 210), (65, 200), (108, 175), w=5, n=30)

# ---------- RIGHT: 成 ----------
# Occupies roughly x in [115, 280], y in [55, 260]
# Stroke 1: 撇 — long-ish descending pie from upper area down through center
bez((165, 75), (155, 135), (128, 235), w=5, n=48)

# Stroke 2: 横 — the top-central heng of 成
seg((150, 108), (225, 105), 5)

# Stroke 3: 横折(横折钩 without visible hook here) — starts at right end of heng,
#   drops down to form the small enclosed shape's right wall
seg((222, 108), (220, 175), 5)
# little bottom of the enclosure — small heng inside
seg((155, 175), (222, 173), 4)

# Stroke 4: 斜钩 — the DOMINANT stroke: long sweeping curve from top
#   descending to lower-right, ending with hook flick UP
bez((175, 60), (225, 165), (275, 245), w=6, n=56)
# hook at end: short up-flick
seg((275, 245), (285, 220), 5)

# Stroke 5: 撇 — small pie crossing near the 斜钩 upper section
bez((205, 155), (185, 180), (160, 210), w=4, n=24)

# Stroke 6: 点 — small dot upper-right (outside the sweep, top-right corner)
bez((248, 68), (256, 78), (263, 92), w=5, n=16)

img.save("01_城.png")
