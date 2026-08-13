# p3_char_0180_打 — 打 (dǎ, "hit"), 5 strokes.
# Left radical: 扌 (shou_pang, 3 strokes) — bank primitive.
# Right component: 丁 (ding_char, 2 strokes) — bank primitive.
# Math-coord composition (center origin, +y up).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shou_pang import draw_shou_pang  # noqa: E402
from ding_char import draw_ding_char  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
t = ImageDraw.Draw(img)

# Left: 扌 — centered around x≈-60, slightly smaller than full char
draw_shou_pang(t, ox=-60, oy=0, scale=0.80)

# Right: 丁 — centered around x≈+50, slightly smaller for balance
draw_ding_char(t, ox=50, oy=-5, scale=0.75)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_打.png")
img.save(out_path)
print("saved", out_path)
