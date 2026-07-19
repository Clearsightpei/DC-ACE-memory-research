"""G1 render for radical 歹 (4 strokes) — 300x300, white bg, black ink.

Stroke breakdown (from GT reference):
  1) 一 (heng): top horizontal, long, with a very slight downward curve
     starting slightly higher on left, dipping and rising to right end.
  2) 短撇 (short pie): a small slash going down-left, sitting below the
     left portion of the top heng.
  3) 横折 (heng-zhe): short horizontal then turning down — inside upper
     body forming the '夕'-like top pocket.
  4) 长撇 (long pie): long sweeping left-falling stroke from top-middle
     of the interior all the way down to lower-left.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 4


def curve(pts, width=TH, steps=60):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill=INK, width=width)
        prev = (x, y)


def line(pts, width=TH):
    d.line(pts, fill=INK, width=width, joint="curve")


# ---- stroke 1: top heng — long, mostly flat with slight sag then rise ----
# Left end higher than middle by a hair; right end tips up
curve([(50, 88), (160, 95), (260, 82)], width=TH + 1)

# ---- stroke 2: short pie under-left of the heng (a small down-left slash) ----
curve([(100, 105), (92, 125), (78, 148)], width=TH)

# ---- stroke 3: horizontal-turn (横折) — small heng then bend down ----
# short heng in mid-upper interior
line([(110, 150), (185, 148)], width=TH)
# turn/hook downward a short distance
curve([(185, 148), (188, 158), (180, 178)], width=TH)

# ---- stroke 4: long pie — sweeps from upper interior down-left to bottom ----
curve([(178, 108), (145, 200), (80, 275)], width=TH + 1)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_090_歹/01_歹.png"
)
print("wrote 01_歹.png")
