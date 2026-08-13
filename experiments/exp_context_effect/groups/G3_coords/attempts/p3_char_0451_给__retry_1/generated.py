# BANK_DEVIATION
# skipped: si_zi_pang.py
# reason: bank 纟 has wide 提 (native span -65..+60) that intrudes into
#         the right column in an L-R composition; retry needs scoops
#         with more visible curvature (main attempt looked like flat L-shapes).
# fresh_component: si_zi_pang_LR_left_v2 (rounder scoops, short 提 in left col)
#
# TRAJECTORY DIFF (retry_1 vs main)
# GT (phase3/给.png):
#   - Left 纟: two small CURLED scoops stacked (upper smaller), long 提 rising
#     from below-left to right, 提 stays mostly in left half.
#   - Right 合: 人-roof at top (apex ~y=+75, splayed wide), horizontal 一
#     below apex, 口 rectangle below (fills lower right), all vertically stacked.
# Main attempt (verdict C):
#   FAIL-1: Left hooks looked ANGULAR (like L-shapes ㄴ), not the rounded
#           scoop-with-hook shape of 撇折. → Increase bezier bow, larger scoop size.
#   FAIL-2: Right 亼 roof read as JUST a triangle — the 一 horizontal was too
#           close to apex and merged visually. → drop 一 lower, keep gap.
#   FAIL-3: Right 口 was too SMALL and floated in mid-column. → scale up 0.42→0.55.
#   FAIL-4: Overall right column FELT LOW — top of 亼 apex was mid-canvas.
#           → Move right column UP so apex sits near y=+90.
# Fixes: bigger curls on 纟; larger 合 with roof higher and 口 bigger/tighter.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.normpath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ji_meet_char import draw_ji_meet_char   # noqa: E402
from kou_char import draw_kou_char           # noqa: E402


CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _draw_curled_scoop(draw, cx, cy, size, ink=6):
    """Rounded 撇折-style scoop: dive-down bezier with pronounced bow,
    then hook right/down. cx,cy is the hinge point (top of scoop)."""
    # Down-scoop (pie): from hinge (top) curving down-left then back to hinge
    # More bow than main attempt so it reads as a curl, not an L.
    p0_top = (cx + size * 0.55, cy + size * 1.10)  # upper-right start
    p2_bot = (cx - size * 0.15, cy)               # hinge (bottom-left)
    # Push control point far to the RIGHT-DOWN of midline so curve bulges right
    p1 = ((p0_top[0] + p2_bot[0]) / 2 + size * 0.35,
          (p0_top[1] + p2_bot[1]) / 2 + size * 0.05)
    _tapered_bezier(draw, p0_top, p1, p2_bot,
                    w_head=ink, w_tail=max(2, ink - 2), n=36, head_ramp=0.05)
    # Little hook out (heng-zhe-like) — short bar to the right
    h0 = (cx - size * 0.15, cy)
    h2 = (cx + size * 1.20, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.05)
    _tapered_bezier(draw, h0, h1, h2,
                    w_head=ink + 1, w_tail=1.5, n=36, head_ramp=0.05)


def draw_si_zi_pang_LR_left(draw):
    """Fresh 纟 for LR-left column: curled scoops + short 提."""
    # Upper small scoop
    _draw_curled_scoop(draw, cx=-95, cy=+65, size=18, ink=5)
    # Middle slightly bigger scoop
    _draw_curled_scoop(draw, cx=-100, cy=+15, size=22, ink=6)
    # Short 提 (rising stroke) — confined to left column
    p0 = (-120, -55)
    p2 = (-10, -30)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 6)
    _tapered_bezier(draw, p0, p1, p2, w_head=12, w_tail=1.5,
                    n=50, head_ramp=0.08)


img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)

# Left: fresh compressed 纟 with rounder scoops
draw_si_zi_pang_LR_left(d)

# Right column: 合 = 亼 top + 口 bottom.
# Tighten vertical spacing: ji_meet_char at scale 0.50 with oy=+35 so roof
# apex ~y=+72 and 一 base ~y=-12. Kou at oy=-45 scale 0.55 → top ~y=-18,
# bottom ~y=-72. Small gap between 一 and 口 top matches GT.
draw_ji_meet_char(d, ox=+55, oy=+35, scale=0.50)

# 口 bottom: tucked close under 一 base.
draw_kou_char(d, ox=+55, oy=-45, scale=0.55)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "01_给.png")
img.save(out_path)
print("wrote", out_path)
