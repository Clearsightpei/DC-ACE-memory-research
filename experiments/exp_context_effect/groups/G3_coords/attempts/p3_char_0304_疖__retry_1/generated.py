# TRAJECTORY DIFF (p3_char_0304_疖 retry_1)
#
# MAIN attempt (FAIL): 01_疖.png rendered as something reading like 府 —
# it had a top dot + horizontal roof but the LEFT descender (疒's long
# pie) was missing / merged with weird strokes, the two interior 冫
# marks were absent (no left-side small ticks), and the right side had
# a full 付-like inline shape instead of a compact 卩. So two concrete
# gaps:
#   (a) 疒 envelope was botched — no long left-falling pie, no 冫 dots.
#   (b) 卩 was drawn as a wide 付-like inline instead of a small right-
#       side 横折钩 + 竖 pair (bank jie_radical was ignored).
#
# GT (gt/phase3/疖.png):
#   - 疒 envelope: small top dot upper-right of the roof, clean thin
#     heng, long pie curving down to bottom-left ~y=270, two interior
#     冫 marks (small 点 upper + rising 提 lower) tucked in the left
#     interior band.
#   - 卩 on the right: small 横折钩 (top-heng ~y=125 spanning ~x=170-220,
#     hooks down to ~y=200), plus a 竖 dropping from the top-heng's
#     left end down to ~y=255. Compact, fits under the 疒 heng roof.
#
# FIX PLAN this retry:
#   1. Call bank draw_ne_chuang (ne_sick.py) verbatim for the whole 疒
#      envelope + 冫 pair — this graduated in B7 and is exactly right.
#   2. Call bank draw_jie_radical (jie_radical.py) shrunk (scale ~0.55)
#      and shifted right (ox=+50, oy=-25) so 卩 sits inside 疒's roof
#      on the right, not overlapping the pie shaft.
#   3. Errata explicitly says: "Bank ne_sick OK; 卩 (bank jie_radical)
#      not called — drawer inlined." Fix = call both bank entries.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata p3_char_0304_疖: "Bank ne_sick (疒) OK; 卩 (bank
#   jie_radical) not called — drawer inlined." Fix = use jie_radical
#   bank entry, don't inline.
# Q2 (form_catalog): 疒-envelope + right-inner 卩 composition. ne_sick
#   holds the envelope geometry; jie_radical holds the 卩 geometry.
#   Scaling jie_radical to 0.55 puts it inside the envelope opening.
# Q3 (helpers): No helpers imported. Both components exist as callable
#   bank primitives — this is a pure bank-composition attempt.

import os
import sys
from PIL import Image, ImageDraw

# Import bank primitives.
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ne_sick import draw_ne_chuang  # noqa: E402
from jie_radical import draw_jie_radical  # noqa: E402

_CANVAS = 300


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 1) 疒 envelope + 冫 (bank ne_sick, verbatim).
    draw_ne_chuang(draw)

    # 2) 卩 (bank jie_radical), shrunk and shifted right to sit inside
    # the 疒 envelope on the right. bank origin is canvas center (150,150);
    # +ox = right, +oy = up (math convention).
    # First revision was scale=0.55 → 卩 too small (横折钩 tiny). Bump to
    # 0.7 so heng-zhe spans ~50 px like GT; shift ox slightly to keep it
    # clear of the pie shaft.
    draw_jie_radical(draw, ox=55, oy=-30, scale=0.72)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_疖.png",
    )
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
