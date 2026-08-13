# ren_pang_pil_for_LR_left.py — promoted from p3_char_0492_俚 (B13 main PASS)
# Curator B13 (2026-08-05, position ~651).
#
# 亻 (person radical) for the LEFT slot of L-R compositions, rendered in
# PIL pixel coords (NOT turtle math-coords). Complements the frozen
# `ren_pang.py` (turtle-based). Provides a canonical thin-MMH-ink 亻 so
# drawers that build the right-side in PIL don't have to re-derive the
# bezier + shu every time.
#
# Motivating context: 俚 (亻+里) B13 PASS. Reuse targets: 伧 (亻+仓),
# 佝 (亻+句), 债 (亻+责), 侏 (亻+朱), 借 (亻+昔), 傍 (亻+旁), 值 (亻+直),
# 傲 (亻+敖), 侪 (亻+齐), 佩 (亻+佩-body) — any L-R with 亻 on the left
# that composes in PIL. The 亻 recipe has repeatedly appeared across
# B7-B13 PASSes (作, 但, 佐, 伯, 佃, 佇, 仲, 伉, 伛, 保, 侑, 俚) — this
# canonical form crystallizes what worked.
#
# Why fresh (v13 BANK_DEVIATION rationale): frozen `ren_pang.py` is
# turtle math-coord (y grows UP, origin at canvas center). PIL right-slot
# radicals (曰, 里, 田, 田-family) use pixel coords (y grows DOWN, origin
# at top-left). Mixing the two coord systems in one attempt is a fresh
# source of position bugs; drawers therefore keep re-inlining the 亻.
# This variant is the PIL-native canonical.
#
# Signature: (d, cx=75, y_top=90, y_bot=225, w_pie_head=6, w_pie_tail=2,
#             w_shu=5)
# cx is the x-center of the 亻; typically 60-80 for a left ~40% slot on
# 300x300. y_top/y_bot bracket the shu (vertical) endpoints. The 撇
# starts up-and-right of cx (offset +25) at y_top-5 and sweeps to the
# lower-left (cx-40, y_bot). Widths default to MMH thin ~5px uniform;
# override for heavier ink.
#
# The recipe: 2-stroke 亻 = 撇 (quadratic bezier, tapered head→tail) +
# 竖 (straight tapered line, head at pie mid-shaft, tail at y_bot-10).

import math
from PIL import Image, ImageDraw


def _bezier_stroke(d, p0, p1, p2, w_head, w_tail, n=45, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def _tapered_line(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def draw_ren_pang_pil_for_LR_left(d, cx=75, y_top=90, y_bot=225,
                                   w_pie_head=6, w_pie_tail=2, w_shu=5,
                                   black=(0, 0, 0)):
    """亻 in PIL pixel coords for LR-left slot.

    d = PIL ImageDraw. cx = shu-column center x. y_top / y_bot bracket
    the shu endpoints. Weights default to MMH thin ~5px.
    """
    # S1: 撇 — starts up-and-right of cx, sweeps down-left past cx.
    _bezier_stroke(
        d,
        (cx + 25, y_top - 5),   # head, upper-right
        (cx + 5, y_top + 55),   # control
        (cx - 35, y_bot),       # tail, lower-left
        w_head=w_pie_head, w_tail=w_pie_tail, n=55, black=black,
    )
    # S2: 竖 — vertical, head touches pie mid-shaft, tail ends above y_bot.
    _tapered_line(
        d,
        (cx + 3, y_top + 50),   # head near pie mid-shaft
        (cx + 3, y_bot - 15),   # tail above bottom
        w_head=w_shu + 1, w_tail=w_shu, n=40, black=black,
    )


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ren_pang_pil_for_LR_left(d)
    import os
    out = os.path.join(os.path.dirname(__file__),
                       "01_ren_pang_pil_for_LR_left.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
