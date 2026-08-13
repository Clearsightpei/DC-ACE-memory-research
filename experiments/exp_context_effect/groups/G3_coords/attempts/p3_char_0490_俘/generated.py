# BANK_DEVIATION
# skipped: zi_char.py
# reason: zi_char depends on liao.py's pixel-coord frame which doesn't cleanly compose in a math-coord L-R slot at reduced scale; inlining lets me size the 子 to a bottom-right slot of 孚.
# fresh_component: zi_inline_for_LR_bottom
"""
俘 (fú) — 亻 (left) + 孚 (right = 爫 top + 子 bottom).
L-R structure: narrow 亻 on the left, wider 孚 stack on the right.
"""
import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang           # noqa: E402
from zhao_top import draw_zhao_top           # noqa: E402
from _shared_helpers import (                # noqa: E402
    variant_pie, tapered_bezier, tapered_line, to_px,
)

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


# ---------------- Left 亻 (compressed, shifted left) ----------------
draw_ren_pang(d, ox=-70, oy=5, scale=0.75)


# ---------------- Right top 爫 (compact, upper) ---------------------
draw_zhao_top(d, ox=45, oy=25, scale=0.65)


# ---------------- Right bottom 子 (inline, fits bottom slot) --------
# 子 has 3 strokes: (1) 横撇 hook on top (short), (2) 竖弯钩 descending
# hook with left-curving belly, (3) crossing 横 through the middle.
# Slot: centered around (45, -40) in math coords, width ~70, height ~85.
def draw_zi_inline_for_LR_bottom(draw, cx=45, cy=-40, w=70, h=85):
    # 1) 横撇 top: short heng that turns down-left into a pie tip.
    #    Head at upper-left of slot; corner at upper-right; tip below.
    heng_L = (cx - w * 0.42, cy + h * 0.42)
    heng_R = (cx + w * 0.42, cy + h * 0.38)
    pie_tip = (cx + w * 0.20, cy + h * 0.08)
    # heng segment (thin, slight taper)
    tapered_line(draw, heng_L, heng_R, w0=4, w1=6, n=24)
    # corner + short pie
    tapered_bezier(draw, heng_R,
                   (cx + w * 0.42, cy + h * 0.20),
                   pie_tip,
                   w_head=6, w_tail=3, n=24)

    # 2) 竖弯钩 descender: starts at upper-mid, curves down, hooks up-left
    #    (this is the vertical spine of 子, curving at the bottom).
    top_pt = (cx + w * 0.05, cy + h * 0.30)
    mid_pt = (cx + w * 0.05, cy - h * 0.20)
    bot_ctrl = (cx + w * 0.00, cy - h * 0.48)
    hook_end = (cx - w * 0.35, cy - h * 0.42)
    # spine (top -> mid) straight vertical thin line
    tapered_line(draw, top_pt, mid_pt, w0=5, w1=5, n=20)
    # curve from mid down and left to hook end
    tapered_bezier(draw, mid_pt, bot_ctrl, hook_end,
                   w_head=5, w_tail=6, n=40)
    # small hook cap at end
    hx, hy = to_px(hook_end[0], hook_end[1])
    r = 4
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))

    # 3) crossing 横: long horizontal near the middle of 子.
    heng2_L = (cx - w * 0.48, cy - h * 0.02)
    heng2_R = (cx + w * 0.48, cy - h * 0.05)
    tapered_line(draw, heng2_L, heng2_R, w0=4, w1=5, n=28)


draw_zi_inline_for_LR_bottom(d)


out = os.path.join(os.path.dirname(__file__), "01_俘.png")
img.save(out)
print(f"wrote {out}")
