# BANK_DEVIATION
# skipped: ne_sick.py + jie_radical.py (both banks) — replaced with inline compact renders
# reason: retry_1 called-then-drifted: envelope filled full canvas so 卩 had no room and
#   drawer inlined the wrong right side (produced 泸-like three-water-dot shape).
#   For 疖 the 疒 envelope must compress LEFT so 卩 fits INSIDE the heng roof on the right.
# fresh_component: ne_envelope_compressed_for_LR + jie_inside_small
#
# RETRY MEMORY CHECKLIST (B4-B5 v7 evolution)
# Q1 (errata): errata says "疒 in left 40%, 卩 in right 40%, both thin". Prior retry_1
#   drew 三点水 + 户 (wrong recognition) — need to actually render 疒 envelope + 卩 inside.
# Q2 (form_catalog): envelope + interior_right composition; thin MMH widths ~5px.
# Q3 (helpers): No helpers. mirror_dian_pair is horizontal; 疒's 冫 is vertical stack.
#
# TRAJECTORY DIFF
# GT (疖): 疒 envelope on left+top (top dot ~x=185, heng from x~90 to x~220 at y~105,
#   long pie sweeping to ~(45, 250), two small 冫 marks in left-middle);
#   INSIDE the envelope on the RIGHT: a small 卩 (horizontal-hook top-rectangle then
#   long vertical descending past envelope base).
# main FAIL: drew what looks like 府 — no 卩, wrong right-side stroke.
# retry_1 FAIL: drew 泸 (三点水 + 户). The three separated left dots and the 户-like
#   right side are visually a different character. Absent 疒 envelope entirely.
# THIS ATTEMPT fixes:
#   1. Draw the 疒 envelope EXPLICITLY (top dot + heng + long pie + two 冫 interior marks).
#   2. Compress heng right-extent to ~x=200 so 卩 has room INSIDE at right ~x=155..215.
#   3. Draw 卩 inline: small heng-zhe-gou top + long shu descending past envelope.
#   4. Use uniform-thin widths (5-6 px) per MMH-thin trust-GT posture.

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


def draw_ne_envelope_compressed_for_LR(draw):
    """疒 envelope, heng right-end pulled back to x=205 so 卩 fits inside at right."""
    # Stroke 1: top 点 — small tapered slash, above the heng roof.
    _tapered_line(draw, (168, 55), (185, 82), w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng — thin horizontal roof, shorter right-extent than solo 疒 bank.
    _tapered_line(draw, (95, 108), (208, 105), w_head=5.0, w_tail=5.0, n=30)

    # Stroke 3: 撇 (long left-falling sweep) welded at heng's left end.
    _tapered_bezier(
        draw,
        p0=(95, 108),
        p1=(42, 275),
        ctrl=(62, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # Stroke 4: 冫 upper mark — 点 (short slash), left-interior.
    _tapered_line(draw, (58, 138), (80, 158), w_head=3.0, w_tail=6.0, n=18)

    # Stroke 5: 冫 lower mark — 提 (rising flick), left-interior.
    _tapered_line(draw, (42, 218), (78, 202), w_head=7.5, w_tail=2.5, n=20)


def draw_jie_inside_small(draw):
    """卩 tucked INSIDE the 疒 envelope, right side. Two strokes: 横折钩 + 竖."""
    # Stroke 1: 横折钩 — short heng starting inside envelope, corner down,
    # bezier curve into a small hook at bottom.
    # Top rectangle roughly x=155..210, y=118..175.
    p_h_start = (155, 122)
    p_corner = (210, 118)
    p_v_end = (200, 170)

    # heng segment
    _tapered_line(draw, p_h_start, p_corner, w_head=5.0, w_tail=6.0, n=22)

    # right-vertical curving inward with a small hook
    # Use bezier for the descend + inward hook
    prev = p_corner
    ctrl = (215, 145)
    steps = 24
    for i in range(1, steps + 1):
        u = i / steps
        omu = 1 - u
        x = omu * omu * p_corner[0] + 2 * omu * u * ctrl[0] + u * u * p_v_end[0]
        y = omu * omu * p_corner[1] + 2 * omu * u * ctrl[1] + u * u * p_v_end[1]
        w = max(1, int(round(6.0 - 1.0 * u)))
        draw.line([prev, (x, y)], fill=(0, 0, 0), width=w)
        prev = (x, y)

    # small hook tick at the bottom-left of the rectangle
    _tapered_line(draw, (p_v_end[0], p_v_end[1] + 1), (p_v_end[0] - 12, p_v_end[1] + 10),
                  w_head=6.0, w_tail=2.0, n=12)

    # Stroke 2: long 竖 descending from left side of 卩 top rectangle to below envelope.
    # Starts near where the 横 begins, drops straight down.
    _tapered_line(draw, (158, 122), (156, 288), w_head=5.5, w_tail=6.5, n=40)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_envelope_compressed_for_LR(draw)
    draw_jie_inside_small(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_疖.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
