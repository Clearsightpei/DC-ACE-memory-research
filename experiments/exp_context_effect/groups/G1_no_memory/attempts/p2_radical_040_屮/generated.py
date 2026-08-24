"""G1 draw of 屮 (radical, 3 strokes).

Structure per GT:
  Stroke 1 (竖): long vertical center line, top to bottom.
  Stroke 2 (竖折): left short vertical dropping, then a horizontal
                    running rightward crossing the center (like a low
                    bowl on the left side).
  Stroke 3 (short 竖): right short vertical dropping down (mirror of
                        left top part), no bottom bar.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 6  # line thickness

# Stroke 1: long vertical center 竖 (top ~y=60 down to y=270)
cx = 150
d.line([(cx, 60), (cx, 270)], fill=INK, width=TH)

# Stroke 2: 竖折 — left short vertical from (~85, 110) down to (~85, 205),
# then horizontal from (~85, 205) rightward to (~215, 205), crossing the center.
# This forms the low "cup" under the middle.
d.line([(85, 110), (85, 205)], fill=INK, width=TH)
d.line([(85, 205), (215, 205)], fill=INK, width=TH)

# Stroke 3: right short vertical from (~215, 110) down to (~215, 200)
d.line([(215, 110), (215, 200)], fill=INK, width=TH)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_040_屮/01_屮.png"
)
