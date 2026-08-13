"""
伽 = 亻 (left ~30%) + 加 (力 middle + 口 right)
Layout on 300x300:
  - 亻 column ~ x 45..95
  - 力 column ~ x 105..185
  - 口 column ~ x 195..265
Strokes 8 total: 亻(2) + 力(2: 横折钩 + 撇) + 口(3: 竖, 横折, 横)
Renderer: PIL brush-dabs for tapered strokes; polylines with round-cap for 口.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab_stroke(pts, r_start, r_end, steps=None):
    """Poly-line brush-dab stroke through control points (linear segments).
    pts: list of (x,y). r ramps from r_start at pts[0] to r_end at pts[-1]."""
    # compute total length for even-radius interpolation
    seglens = []
    total = 0.0
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        L = (dx * dx + dy * dy) ** 0.5
        seglens.append(L)
        total += L
    if total == 0:
        return
    N = steps or max(60, int(total * 2))
    for k in range(N + 1):
        t = k / N
        # distance along path
        dist = t * total
        # find segment
        acc = 0.0
        for i, L in enumerate(seglens):
            if acc + L >= dist or i == len(seglens) - 1:
                u = (dist - acc) / L if L > 0 else 0
                x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u
                y = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u
                break
            acc += L
        r = r_start + (r_end - r_start) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------- 亻 (left radical) ----------
# 撇 (pie): from top ~(78, 70) descending-left to ~(45, 175). Ends higher (radical
# 撇 doesn't reach baseline), pressed head, taper.
dab_stroke([(78, 68), (70, 105), (58, 145), (45, 185)], r_start=5.2, r_end=1.6)

# 竖 (vertical): starts at 撇 mid-point, straight down to baseline.
dab_stroke([(76, 110), (76, 235)], r_start=4.2, r_end=3.8)


# ---------- 力 (middle component) ----------
# 横折钩: horizontal top from ~(110, 100) to ~(178, 100), fold down to ~(176, 210),
# then hook flick UP-LEFT (~-115°).
dab_stroke(
    [(110, 100), (178, 102), (178, 155), (176, 210)],
    r_start=4.2, r_end=3.6,
)
# Hook flick up-and-left INTO body
dab_stroke([(176, 210), (168, 202), (156, 194)], r_start=3.6, r_end=1.4)

# 撇 (pie) crossing the top-bar at ~x=135, sweeping down-left to (100, 235).
dab_stroke([(138, 118), (128, 155), (115, 195), (100, 235)], r_start=4.6, r_end=1.8)


# ---------- 口 (right component) ----------
# Small square, slightly wider at top. Baseline aligns with 力.
# Left 竖
dab_stroke([(200, 120), (202, 215)], r_start=3.6, r_end=3.4)
# 横折 (top horizontal + right vertical)
dab_stroke([(200, 120), (262, 118), (260, 215)], r_start=3.8, r_end=3.4)
# Bottom 横 closing
dab_stroke([(202, 215), (260, 215)], r_start=3.6, r_end=3.4)


img.save("01_伽.png")
print("wrote 01_伽.png")
