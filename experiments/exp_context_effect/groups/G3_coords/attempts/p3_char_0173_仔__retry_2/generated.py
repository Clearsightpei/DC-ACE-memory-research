# p3_char_0173_仔__retry_2 — 仔 (zǐ), 5 strokes: 亻 (2) + 子 (3).
#
# VISUAL DIFF (retry_1 PNG vs GT PNG) — mandatory step 0
# 1. Left 亻: retry_1 rendered the 竖 as a *tiny, detached* vertical bar
#    floating in the mid-left, NOT touching the 撇. GT has 亻 as
#    (a) a long 撇 from upper-mid down-left, and (b) a 竖 that starts
#    from roughly the midpoint of the 撇 and runs straight down to the
#    bottom, both strokes connected at a clear vertex.
# 2. Right 子, top stroke: retry_1 drew a huge C-bracket / left-facing
#    "C" shape at the top of the 子 (looks like a backwards parenthesis).
#    GT top is a short 横 that turns sharply down into a small hook =
#    横撇 — a "7" shape, NOT a "C".
# 3. Right 子, main body: retry_1's 弯钩 hook lands at the top-right
#    and curves up-right instead of dropping to the bottom and hooking
#    up-left. GT has the 竖弯钩 dropping from the top-center of 子, going
#    all the way to the bottom, then curving left-up into a small hook.
# 4. Middle 横 of 子: retry_1 has a stray floating short heng in the
#    left half of the canvas (looks like it belongs to nothing). GT has
#    one clean 横 crossing the vertical shaft of 子 near the vertical
#    midpoint, spanning almost the full width of the right component.
#
# Fix: abandon the bank composition (liao + wan_gou) — they added
# unwanted primitives. Hand-render 5 clean strokes with PIL, thin
# uniform ink (matches GT's MMH style per P12).
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata said "use zi_char verbatim @ scale 0.65". Retry_1
#   tried a variant (liao+custom heng) and produced the C-bracket top.
#   Errata is a HYPOTHESIS — visual diff overrides. The real fail was
#   wrong stroke topology on top of 子 (C-shape vs 7-shape). Bank
#   composition brought in extra shapes; fresh inline is the fix.
# Q2 (form_catalog): 亻-family rows recommend ren_pang identity, but
#   ren_pang in prior attempts produced the detached 竖 seen in
#   retry_1. Inline 亻 as 撇+竖 with the 竖 anchored on the 撇
#   midpoint to guarantee connection.
# Q3 (helpers): fail is stroke-topology (wrong shape for top of 子),
#   not X-crossing/joint-weld. mirror_dian_pair etc do not apply.
#   Trust GT (B5 lesson) — inline fresh with straight lines.

import os
from PIL import Image, ImageDraw


def draw(d, ink=8):
    # ---------- LEFT: 亻 ----------
    # Stroke 1: 撇 — from upper mid-left, angling down-left.
    d.line([(100, 65), (55, 215)], fill="black", width=ink)
    # Stroke 2: 竖 — from a point ON the 撇 (near midpoint), straight down.
    # Midpoint of stroke 1 ~ (77, 140). Start at (82, 140) so the 竖
    # visually meets the 撇 without a gap; run down to y=250.
    d.line([(82, 140), (82, 250)], fill="black", width=ink)

    # ---------- RIGHT: 子 ----------
    # Stroke 3: 横撇 — short heng then a small hook down-left.
    d.line([(150, 70), (240, 70)], fill="black", width=ink)
    d.line([(240, 70), (218, 108)], fill="black", width=ink)

    # Stroke 4: 竖弯钩 — long vertical then a smooth curl at the bottom.
    # Vertical shaft.
    d.line([(200, 90), (200, 230)], fill="black", width=ink)
    # Curl approximated with a short arc: three tiny segments.
    d.line([(200, 230), (215, 245)], fill="black", width=ink)
    d.line([(215, 245), (245, 245)], fill="black", width=ink)
    # Small up-tick hook (弯钩 ends by lifting up-left).
    d.line([(245, 245), (250, 225)], fill="black", width=ink)

    # Stroke 5: middle 横 — long horizontal crossing the shaft.
    d.line([(135, 165), (270, 165)], fill="black", width=ink)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), "01_仔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
