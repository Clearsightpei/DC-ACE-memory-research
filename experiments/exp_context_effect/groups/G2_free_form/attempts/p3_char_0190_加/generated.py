"""
p3_char_0190_加 (jiā) — G2

Decomposition: 力 (left) + 口 (right). 5 strokes.
  力 (2 strokes):
    S1 横折钩 — horizontal top, folds down, hooks UP-LEFT at bottom.
    S2 撇 — long sweep from upper region down-left through body.
  口 (3 strokes):
    S3 竖 — left vertical
    S4 横折 — top horizontal into right vertical
    S5 横 — bottom horizontal (touches sides)

# SIGNATURE CHECK (Tier-0 hook flick reminder):
#   S1 is 横折钩 — terminal flick UP-and-LEFT (~-105° to -120°).
#   Never down. Flicks back INTO the 力 body.

Layout: 力 occupies roughly left 55%, 口 occupies right 40% (smaller,
sits slightly lower center-of-mass than 力's top). GT shows 口 quite
small relative to 力.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BRUSH = 6

def line(pts, width=BRUSH):
    d.line(pts, fill="black", width=width, joint="curve")
    # end caps
    for (x, y) in [pts[0], pts[-1]]:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def bezier(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

# ===== 力 (left) =====
# S1 横折钩:
#   horizontal top from ~(55, 70) to ~(150, 65)  (slight lift)
#   fold down-left to ~(115, 210) (leftward curve)
#   hook flicks UP-LEFT to ~(95, 195)
h_top = [(55, 72), (100, 68), (150, 65)]
line(h_top, width=7)
# fold + down curve (bezier)
fold = bezier((150, 65), (155, 130), (118, 215), steps=50)
line(fold, width=7)
# hook flick UP-LEFT
line([(118, 215), (95, 198)], width=7)

# S2 撇: sweeps from upper area (~135, 100) down-left to (~35, 275)
pie = bezier((135, 100), (85, 210), (35, 275), steps=50)
line(pie, width=7)

# ===== 口 (right) — smaller, sits slightly below 力's top =====
# occupies roughly x in [190, 265], y in [140, 225]
# S3 竖 (left vertical)
line([(192, 138), (190, 225)], width=7)
# S4 横折 (top horizontal + right vertical)
line([(190, 138), (263, 135)], width=7)   # 横
line([(263, 135), (258, 228)], width=7)   # 折 down (slight inward)
# S5 横 (bottom, closes the box)
line([(188, 227), (262, 226)], width=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0190_加/01_加.png"
)
print("wrote 01_加.png")
