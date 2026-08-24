"""Render 军 (jūn, army) — 6 strokes.

Structure: 冖 (top cover: 点 + 横钩) over 车-like body (横, 横折,
横, 长竖 extending down through the cover).

Hook rule (memory_index Tier-0 B): 横钩 flicks UP-and-LEFT at the
terminal — never DOWN. The long central 竖 has no hook (straight).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=INK, width=width, joint="curve")
    r = width // 2
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---- 冖 (top cover) ----
# 1. 点 (small dot at top-left of the cover)
stroke([(78, 68), (92, 82)], width=8)

# 2. 横钩 (horizontal with UP-LEFT flick hook on right end)
#    long horizontal sweep, then hook down-then-up-left
stroke([(72, 92), (240, 90)], width=7)
# hook: downstroke then flick UP-and-LEFT
stroke([(240, 90), (233, 108)], width=7)
stroke([(233, 108), (222, 100)], width=6)  # up-and-left flick

# ---- 车 body inside ----
# 3. 横 (upper horizontal of 车, inside the cover)
stroke([(108, 128), (208, 128)], width=7)

# 4. 横折 (short horizontal + turn down — right side of 车 body)
stroke([(115, 155), (198, 155)], width=7)   # short mid horizontal
stroke([(198, 155), (198, 195)], width=7)   # turn down (right side)
# left side downstroke (part of the 车 body enclosure)
stroke([(115, 155), (115, 195)], width=7)

# 5. 横 (long middle-bottom horizontal — wider than the cover)
stroke([(58, 210), (250, 210)], width=8)

# 6. 长竖 (central vertical: starts just under cover, extends well below)
stroke([(152, 118), (152, 275)], width=8)

img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0247_军/01_军.png"
)
print("wrote 01_军.png", img.size)
