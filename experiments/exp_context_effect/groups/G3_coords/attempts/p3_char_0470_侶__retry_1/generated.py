# BANK_DEVIATION
# skipped: ren_pang.py
# reason: bank ren_pang renders pie and shu with disjoint offsets that read
#   as two separated strokes at any composition scale (pie floats top-left,
#   shu drops below with no shaft contact — confirmed by main attempt and
#   pass-1 of this retry). GT 亻 needs pie's mid-shaft touched by shu's head.
# fresh_component: inline_ren_pang_for_侶

# TRAJECTORY DIFF
# GT (gt/phase3/侶.png): 亻 on left (proper pie sweeping down-left + touching
#   shu dropping from mid-shaft) + 呂 on right (two 口 stacked vertically, with
#   tiny connecting stroke).
# FAIL main attempt: 亻 broken (pie floated, shu disconnected). Right 呂 boxes
#   sized too big, no connector, gap too wide.
# FAIL retry pass 1: 亻 STILL broken with bank ren_pang — pie floated top-left,
#   shu dropped separately below with no shaft contact. 呂 side looked ok.
# FIXES pass 2 (this render):
#   A) DEVIATE from bank ren_pang: inline a proper 亻 where the shu explicitly
#      starts from a computed point on the pie shaft (~35% down the pie).
#   B) Keep 呂 side (bank kou × 2 + connector) — it rendered acceptably.

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): "bank ren_pang + 2 stacked bank kou at kou_scale ≈ 0.55" —
#   partly adopted: kou-stack kept; ren_pang REJECTED per B5 trust-GT posture
#   (bank primitive disconnects pie/shu in this composition).
# Q2 (form_catalog): 亻+X pattern; bank ren_pang used before, but v13
#   deviation channel explicitly says skip when primitive geometry doesn't
#   fit. Inline is warranted here.
# Q3 (helpers): No X-crossing / mirror-dot / apex-kiss family. Pure L-R
#   composition with a shaft-contact inline for 亻.

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from kou import draw_kou  # noqa: E402


def m2p(x, y):
    """math (center-origin, +y up) → pixel (top-left origin, +y down)."""
    return (150 + x, 150 - y)


def draw_inline_ren_pang(d, cx=-70, cy=0):
    """Inline 亻: pie top-right to bottom-left, then shu drops from mid-shaft.

    All coords in math convention, relative to (cx, cy) = radical center.
    """
    # Pie: from top-right (a bit right of center, high) sweeping down-left
    # (well left, low). Slight bow curve via polyline.
    p_top = (cx + 15, cy + 75)   # top-right head
    p_mid = (cx - 12, cy + 20)   # curve control (roughly on shaft)
    p_bot = (cx - 40, cy - 70)   # bottom-left tail
    d.line([m2p(*p_top), m2p(*p_mid), m2p(*p_bot)],
           fill=(0, 0, 0), width=6, joint="curve")

    # Shu: starts ON the pie shaft at ~35% down (near p_mid) and drops straight.
    shu_head = (cx - 10, cy + 25)
    shu_tail = (cx - 10, cy - 75)
    d.line([m2p(*shu_head), m2p(*shu_tail)], fill=(0, 0, 0), width=6)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left (inline, deviating from bank ren_pang).
    draw_inline_ren_pang(d, cx=-70, cy=0)

    # 呂 on right: two 口 stacked. Upper slightly smaller than lower.
    draw_kou(d, ox=55.0, oy=45.0, scale=0.48)
    draw_kou(d, ox=55.0, oy=-45.0, scale=0.55)

    # Tiny connector between the two 口 (呂's linking mark).
    x_pix = 150 + 55
    d.line([(x_pix, 150 - 18), (x_pix, 150 - (-15))], fill=(0, 0, 0), width=4)

    out = os.path.join(os.path.dirname(__file__), "01_侶.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
