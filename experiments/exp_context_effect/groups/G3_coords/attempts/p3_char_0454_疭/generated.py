# BANK_DEVIATION
# skipped: ne_sick.py + bing_ren.py (helpers from _shared_helpers not reused here)
# reason: 疭 embeds 从 tightly INSIDE the 疒 envelope; both components need
#         hand-tuned positions/scales that don't match either bank's fixed
#         geometry (envelope descender must clear the interior 从; 从 must
#         sit compact under the heng roof, smaller than bing_ren's stacked
#         pair). Inline PIL render for both.
# fresh_component: ne_envelope_for_454 + cong_inside_ne

# 疭 (p3_char_0454_疭) — 疒 envelope + 从 inside.
# GT decomposition (from gt/phase3/疭.png):
#   Outer 疒 (5 strokes): top dot upper-right, thin heng roof,
#     long descending 撇 from heng's left end, two small interior 冫 marks
#     tucked against the pie's upper-left interior.
#     WAIT — for 疭, the interior IS 从, not 冫. So the 疒 envelope here is
#     really just: top dot + heng + long descending pie (3 envelope strokes),
#     with the interior 冫 marks REPLACED by 从 (two 人 = 4 strokes).
#   Inner 从 (4 strokes): left 人 (pie + na) + right 人 (pie + na).
#     Both sit under the heng roof, right of the descending pie.
# Total ~7 strokes visible in GT.
# Widths kept thin per drawer_memory "trust GT / MMH is thin" posture.

import os
from PIL import Image, ImageDraw

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


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
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


def draw_ren_pil(draw, apex, pie_tail, na_tail,
                 w_pie_head=5.5, w_pie_tail=3.0,
                 w_na_head=3.0, w_na_belly=5.5, w_na_tail=2.5,
                 bow_pie=-4.0, bow_na=+4.0):
    """Small inline 人 (pie + na) sharing an apex. Coords in PIL space."""
    # pie: apex → pie_tail, slight leftward bow
    mid_pie = ((apex[0] + pie_tail[0]) / 2 + bow_pie,
               (apex[1] + pie_tail[1]) / 2)
    _tapered_bezier(draw, apex, pie_tail, mid_pie,
                    w_head=w_pie_head, w_tail=w_pie_tail, n=40)
    # na: apex → na_tail, slight rightward bow, with belly
    mid_na = ((apex[0] + na_tail[0]) / 2 + bow_na,
              (apex[1] + na_tail[1]) / 2)
    _tapered_bezier(draw, apex, na_tail, mid_na,
                    w_head=w_na_head, w_tail=w_na_tail, n=40)


def draw_zong(draw):
    """Render 疭 directly. PIL pixel coords (y grows DOWN)."""

    # ------------------ 疒 envelope ------------------
    # Stroke 1: top 点 (small tapered slash, upper-right of the envelope)
    _tapered_line(draw, (198, 55), (215, 78), w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng roof (thin horizontal)
    _tapered_line(draw, (145, 108), (245, 105), w_head=4.5, w_tail=4.5, n=30)

    # Stroke 3: long descending 撇 from heng's left end
    _tapered_bezier(
        draw,
        p0=(145, 108),
        p1=(85, 278),
        ctrl=(108, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # ------------------ 从 inside (two 人, side by side) ------------------
    # Sits under the heng roof, right of the descending pie.
    # Left 人: apex just under heng, tucked right of the descending pie
    draw_ren_pil(draw,
                 apex=(158, 138),
                 pie_tail=(128, 240),
                 na_tail=(190, 250),
                 w_pie_head=5.0, w_pie_tail=2.5,
                 w_na_head=3.0, w_na_belly=5.0, w_na_tail=2.0,
                 bow_pie=-4.0, bow_na=+4.0)

    # Right 人: slightly larger (dominant); pull na tail in so it stays on canvas
    draw_ren_pil(draw,
                 apex=(218, 138),
                 pie_tail=(188, 250),
                 na_tail=(258, 265),
                 w_pie_head=5.5, w_pie_tail=2.5,
                 w_na_head=3.0, w_na_belly=6.0, w_na_tail=2.0,
                 bow_pie=-5.0, bow_na=+6.0)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zong(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疭.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
