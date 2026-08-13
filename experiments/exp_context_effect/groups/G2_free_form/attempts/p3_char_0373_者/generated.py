"""者 (zhě) — 8 strokes.
Structure: 老字头 (top): 横 + 竖 + 横 + long 撇 (sweeping across)
           bottom: 日 (竖, 横折, 横, 横)
Consulted memory_index TIER-0: 者 is not a sibling-risk target.
No hooks. Standard PIL brush-dabs approach.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=8):
    d.line(pts, fill=INK, width=width, joint="curve")
    # cap the endpoints
    for (x, y) in (pts[0], pts[-1]):
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Top: 老字头 ---
# Stroke 1: top short 横 (near center-top)
stroke([(110, 55), (185, 55)], width=8)

# Stroke 2: 竖 through it, slightly leaning
stroke([(145, 40), (145, 115)], width=8)

# Stroke 3: long slanting 横 (main horizontal), spans wide
stroke([(50, 125), (250, 118)], width=9)

# Stroke 4: long 撇 (sweeping from upper-right down to lower-left)
# starts near top-right of 横, arcs down-left
stroke([(200, 70), (175, 130), (130, 200), (70, 275)], width=9)

# --- Bottom: 日 (positioned to right of 撇 tail) ---
# 日 box approx: left=140 right=210 top=170 bot=270
LX, RX = 145, 215
TY, BY = 175, 270

# Stroke 5: 竖 (left of 日)
stroke([(LX, TY), (LX, BY)], width=8)

# Stroke 6: 横折 (top + right side of 日)
stroke([(LX, TY), (RX, TY), (RX, BY)], width=8)

# Stroke 7: middle 横 of 日
stroke([(LX + 4, 220), (RX - 4, 220)], width=6)

# Stroke 8: bottom 横 of 日
stroke([(LX, BY), (RX, BY)], width=8)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0373_者/01_者.png"
)
print("saved")
