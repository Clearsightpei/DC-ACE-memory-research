# p3_char_0027_七 (qi, "seven") — G3 attempt (revised against clean GT)
#
# Decomposition: 2 strokes.
#   1) Top stroke: a short pie/heng that starts high-left and descends
#      slightly to the right (left end higher than right end). It reads
#      like a short 横 with mild pie tilt.
#   2) 竖弯钩: vertical shaft descending from just above the horizontal,
#      curving right along the bottom, ending in an upward hook.
#
# The horizontal crosses the vertical shaft roughly at 40% from left end.

import sys, os
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
t = ImageDraw.Draw(img)


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


# --- Stroke 1: top 横 with slight downward tilt to the right (like GT).
# Left end higher (~y=40), right end lower (~y=20). Length ~170 px.
# Positioned so the shaft crosses at ~40% from left.
x_left, y_left = _to_pixel(-95.0, 40.0)    # left end (higher)
x_right, y_right = _to_pixel(75.0, 20.0)   # right end (lower)
t.line([(x_left, y_left), (x_right, y_right)], fill=(0, 0, 0), width=12)

# --- Stroke 2: 竖弯钩 (bank primitive)
# Shaft at ox=-25 crosses the horizontal ~40% from left (which spans -95..75).
# scale=1.0: shaft top at oy+70 (=55), shaft bottom at oy-30 (=-45),
# tail extends to (55, -85), hook to (50, -63).
draw_shu_wan_gou(t, ox=-25.0, oy=-15.0, scale=1.0)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0027_七/01_七.png"
img.save(out_path)
print("saved:", out_path)
