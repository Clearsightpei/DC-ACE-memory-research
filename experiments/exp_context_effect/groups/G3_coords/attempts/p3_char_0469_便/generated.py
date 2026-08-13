# p3_char_0469_便 — G3 attempt (revision after self-check)
# 便 = 亻 (left) + 更 (right).
#
# Composition plan:
#   - Left: inline "tall ren_pang" recipe (copied from bank kang_char.py) —
#     bank ren_pang's shu is too short for a 9-stroke tall char. This is
#     the same helper kang_char / zhang_ren use for tall-亻 compounds.
#     Reuses bank draw_pie for the pie stroke.
#   - Right: inline 更 (7 strokes: 一 + 曰 + 撇 + 捺) in the right ~60%.
#     No bank entry exists for 更 (X-crossing family flagged TERMINAL in
#     drawer_memory B9/B11; still worth a clean inline attempt).
#
# NOT a BANK_DEVIATION: tall-ren_pang is an established inline pattern
# from kang_char/zhang_ren (bank rows 154, 208) not a skip of ren_pang.py.

import os
import sys
from PIL import Image, ImageDraw

# --- bootstrap bank imports ---
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402


_CANVAS = 300


def _to_pixel(mx, my, canvas=_CANVAS):
    return canvas / 2 + mx, canvas / 2 - my


def _draw_tall_ren_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """亻 tuned for compound-character composition — tall shu.
    (Recipe from bank kang_char.py, row 208 PASS.)"""
    draw_pie(t, ox=ox + (-8) * scale, oy=oy + 25 * scale, scale=0.85 * scale)
    top_x, top_y = _to_pixel(ox + 5 * scale, oy + 30 * scale)
    bot_x, bot_y = _to_pixel(ox + 5 * scale, oy + (-95) * scale)
    thickness = max(1, int(round(9 * scale)))
    t.line([(top_x, top_y), (bot_x, bot_y)], fill=(0, 0, 0), width=thickness)


W, H = _CANVAS, _CANVAS
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# ---------------- LEFT: 亻 (tall) ---------------- #
_draw_tall_ren_pang(draw, ox=-75.0, oy=0.0, scale=0.90)

# ---------------- RIGHT: 更 inline ------------------ #
INK = 6           # main stroke width (MMH-thin per P12)
INK_THIN = 5      # for interior heng


def _line(p0, p1, w=INK):
    draw.line([p0, p1], fill=(0, 0, 0), width=w)


# Right column occupies roughly x=130..285.
# Stroke 1: top 一 (heng)
_line((130, 68), (285, 68), w=INK)

# 曰 box (strokes 2–5): left shu + 横折 + interior heng + bottom heng
box_x_left = 155
box_x_right = 262
box_y_top = 100
box_y_bot = 182
box_y_mid = 144

# Stroke 2: left 竖 of 曰
_line((box_x_left, box_y_top), (box_x_left, box_y_bot), w=INK)
# Stroke 3: 横折 — top heng + right shu
_line((box_x_left, box_y_top), (box_x_right, box_y_top), w=INK)
_line((box_x_right, box_y_top), (box_x_right, box_y_bot), w=INK)
# Stroke 4: interior heng inside 曰
_line((box_x_left + 3, box_y_mid), (box_x_right - 6, box_y_mid), w=INK_THIN)
# Stroke 5: bottom heng of 曰
_line((box_x_left, box_y_bot), (box_x_right, box_y_bot), w=INK)

# Stroke 6: 撇 — leaves from lower-left area of 曰-box, sweeps down-left.
pie_head = (box_x_left + 32, box_y_bot)
pie_tail = (130, 278)
_line(pie_head, pie_tail, w=INK)

# Stroke 7: 捺 — leaves from middle-lower of 曰-base, sweeps down-right.
na_head = (box_x_left + 45, box_y_bot - 1)
na_tail = (290, 270)
_line(na_head, na_tail, w=INK)


out_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "01_便.png",
)
img.save(out_path)
print(f"wrote {out_path}")
