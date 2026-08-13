# p3_char_0530_痂 — 痂 (jiā, scab), 疒 (envelope) + 加 (interior).
#
# Composition:
#   - Envelope: 疒 via bank primitive `ne_sick.draw_ne_chuang`.
#     (V9 graduate — thin uniform widths, matches GT posture.)
#   - Interior: 加 = 力 (left of interior) + 口 (right of interior).
#     No 加 bank entry — inline fresh. 力 rendered similar to ban_char
#     but compressed into the envelope's interior band (right of pie).
#     口 rendered inline as a small box in the lower-right.
#
# Bank fit check:
#   - ne_sick envelope shape matches GT 痂 envelope. Use as-is.
#   - ban_char has full-size 办 (力+八 sides) — geometry doesn't slot
#     into 疒's interior at correct scale; inline the 力 portion fresh
#     with adjusted anchor. kou_char is a full-canvas box; too big.
#
# Not a BANK_DEVIATION (no bank primitive was intended-then-skipped;
# just inline where no bank fit exists, standard practice for 加).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
import ne_sick

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_jia_inside(draw):
    """Inline 加 (力 + 口) sitting inside the 疒 envelope's right band.

    Interior bounding roughly x=140..285, y=115..280.
    力 sits upper-left of interior; 口 sits lower-right.
    """
    # --- 力 component ---
    # Stroke 1: 横折钩 — heng across top → 折 down → small hook up-left
    hzg_heng_start = (155, 138)
    hzg_corner = (215, 133)
    hzg_bot = (213, 225)
    _tapered_line(draw, hzg_heng_start, hzg_corner, 5.0, 5.5, n=24)
    _tapered_line(draw, hzg_corner, hzg_bot, 5.5, 4.5, n=32)
    # hook — short up-left flick
    _tapered_line(draw, hzg_bot, (195, 213), 4.5, 2.5, n=14)

    # Stroke 2: 撇 — starts just above the heng, sweeps down-left
    # Shortened tail vs first pass (was y=275, now y=258) to stay
    # within envelope belly.
    _tapered_bezier(
        draw,
        p0=(178, 120),
        p1=(148, 258),
        ctrl=(160, 195),
        w_head=6.5,
        w_tail=3.0,
        n=60,
    )

    # --- 口 component (small box, right of 力 inside envelope) ---
    # Revised: moved UP and slightly LEFT vs first pass so 口 sits at
    # 力's level (mid-interior), not down in the corner.
    k_left = 228
    k_right = 278
    k_top = 165
    k_bot = 240
    # Stroke 3: 竖 (left vertical of box)
    _tapered_line(draw, (k_left, k_top + 2), (k_left, k_bot), 5.0, 4.5, n=28)
    # Stroke 4: 横折 (top heng + right shu)
    _tapered_line(draw, (k_left - 2, k_top), (k_right, k_top), 4.5, 5.5, n=24)
    _tapered_line(draw, (k_right, k_top), (k_right - 2, k_bot), 5.5, 4.5, n=28)
    # Stroke 5: 横 (bottom closing heng)
    _tapered_line(draw, (k_left - 2, k_bot), (k_right + 1, k_bot), 4.5, 5.0, n=24)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Left/envelope: 疒 from bank primitive.
    ne_sick.draw_ne_chuang(draw)

    # Interior: 加 inline.
    draw_jia_inside(draw)

    out = os.path.join(_HERE, "01_痂.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
