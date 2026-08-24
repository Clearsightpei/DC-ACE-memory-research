# generated.py — p3_char_0312_伲 (nǐ) — 7 strokes
# 伲 = 亻 (left, 2 strokes) + 尼 (right, 5 strokes)
#   亻: 1) 撇  2) 竖
#   尼: 3) 横折 (top+right descender of 尸)
#        4) 中间 横 (middle of 尸)
#        5) 长撇 (left descender of 尸, sweeps down-left)
#        6) 短撇 (匕's short pie)
#        7) 竖弯钩 (匕's hooked stroke)
# Uniform thin lines per P12 (MMH GT rendering style).

from PIL import Image, ImageDraw

CANVAS = 300
W = 5

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ------------------ LEFT: 亻 (x ~ 30..85) ------------------
# Stroke 1: 撇 (top sweep from upper area down-left, curved)
polyline([(75, 75), (60, 125), (35, 190)])

# Stroke 2: 竖 (vertical, touches mid of pie)
line((70, 130), (70, 255))

# ------------------ RIGHT: 尼 (x ~ 105..255) ------------------
# 尸 component (strokes 3-5)
# Stroke 3: 横折 (horizontal across top, then down the right side)
polyline([(115, 75), (240, 75), (232, 165)])

# Stroke 4: middle 横 (medium-length horizontal inside 尸)
line((120, 130), (215, 130))

# Stroke 5: 长撇 — from top-left of 尸, sweeps down-left
polyline([(115, 75), (110, 145), (100, 205), (90, 265)])

# 匕 component (strokes 6-7), tucked inside/below 尸, right side
# Stroke 6: 短撇 (small down-left, near top of 匕)
line((175, 175), (140, 210))

# Stroke 7: 竖弯钩 — short vertical, curves right along bottom, hook up
line((170, 170), (170, 235))
polyline([(170, 235), (185, 258), (215, 268), (245, 258), (252, 240)])
# hook (upward tick at right end)
line((252, 240), (250, 215))

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0312_伲/01_伲.png"
img.save(out_path)
print("saved", out_path)
