# p3_char_0353_找 — 找 (zhǎo, "seek"), 7 strokes.
# Left: 扌 (shou_pang, 3 strokes) — bank primitive.
# Right: 戈 (4 strokes) — inlined, adapted from yi_ge (弋) + extra 撇.
# 戈 is not in bank; 弋 (yi_ge) is close but only 3 strokes.
# BANK_DEVIATION
# skipped: yi_ge.py
# reason: yi_ge is 弋 (3 strokes); 戈 needs an added 撇 crossing the 横,
#         and the composition sits on the right half of a L-R char,
#         so proportions/anchor differ from a standalone 弋.
# fresh_component: ge_variant_for_找

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
from _shared_helpers import tapered_bezier, tapered_line  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
t = ImageDraw.Draw(img)


def draw_ge_right(t, ox=0.0, oy=0.0, scale=1.0):
    """戈 sized for the right side of a L-R char.
    4 strokes: 横, 斜钩(belly bezier + hook), 撇 crossing, 点 upper-right.
    Math coords (+y up)."""
    def _sh(mx, my):
        return (mx * scale + ox, my * scale + oy)

    # Stroke 1: 横 — short-medium horizontal, upper area.
    tapered_line(t, _sh(-55, 25), _sh(45, 30), 4, 4)

    # Stroke 2: 斜钩 — long diagonal from left-of-heng down-right with belly,
    # then small upward hook.
    tapered_bezier(
        t,
        _sh(-30, 60),   # head near top-left of the shape
        _sh(30, -25),   # belly control (bulge to lower-right)
        _sh(60, -95),   # tail bottom-right
        w_head=4, w_tail=5,
        n=64,
    )
    tapered_line(t, _sh(60, -95), _sh(80, -78), 5, 3)  # hook up-right

    # Stroke 3: 撇 — SHORT, from just above heng down-left through heng.
    tapered_bezier(
        t,
        _sh(-5, 55),    # head above heng (near left of shape)
        _sh(-20, 30),   # gentle bow
        _sh(-40, 0),    # tail — short, ends near heng-left
        w_head=4, w_tail=3,
        n=40,
    )

    # Stroke 4: 点 — small dot upper-right corner (above heng).
    tapered_line(t, _sh(35, 60), _sh(52, 42), 3, 6)


# Left: 扌 — centered around x≈-75, slightly smaller so 戈 has room.
draw_shou_pang(t, ox=-75, oy=-5, scale=0.75)

# Right: 戈 — centered around x≈+25.
draw_ge_right(t, ox=25, oy=5, scale=0.90)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_找.png")
img.save(out_path)
print("saved", out_path)
