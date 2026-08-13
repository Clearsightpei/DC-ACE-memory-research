# BANK_DEVIATION
# skipped: ne_sick.py + jie_radical.py — replaced with inline compact renders
# reason: ne_sick's heng runs to x=245 (full width) and its 撇 tail at x=85 leaves no
#   right-interior room for 卩; jie_radical's shu is centred at canvas mid, way too far
#   left when 疒 already occupies the left half. Need both compressed for L-R composition.
# fresh_component: ne_envelope_LR (compressed to x<=205) + jie_inside_small_v2
#                  (tighter rect at right, shu clearly descending past envelope base)
#
# RETRY MEMORY CHECKLIST (B4-B5 v7 evolution)
# Q1 (errata): errata says "疒 in left 40%, 卩 in right 40%, both thin".
#   retry_1 drew 泸, retry_2 the envelope was OK but the lower 冫 (提) and 卩 shu
#   read as faint/missing. Fix: strengthen those two lines specifically.
# Q2 (form_catalog): envelope + interior_right composition; MMH-thin ~5px widths.
# Q3 (helpers): No helpers — mirror_dian_pair is horizontal; 疒's 冫 is vertical stack.
#
# TRAJECTORY DIFF
# GT (疖): 疒 envelope on left+top (top dot ~x=185, heng from x~90 to x~215 at y~105,
#   long pie sweeping to ~(45, 250), two clearly-separated 冫 marks in left-middle);
#   卩 INSIDE at right: small horizontal-corner-hook top rectangle (x~155..215, y~118..175)
#   and a long shu on the LEFT edge of that rectangle descending to y~285.
# main FAIL: drew 府 (no 卩).
# retry_1 FAIL: drew 泸 (三点水 + 户).
# retry_2 FAIL: envelope + right hook OK but (a) only upper 冫 shows, lower 提 lost;
#   (b) 卩's long shu at x=156 got visually swallowed by pie's descend.
# THIS ATTEMPT fixes:
#   1. Move 卩 shu right to x=165 so it is clearly separated from pie.
#   2. Fatten the lower 冫 提 (w_head=8) and shift it into cleaner left-interior air.
#   3. Draw 卩's 横折 corner sharply (heng + explicit right-vertical + explicit hook tick).
#   4. Keep envelope compressed (heng ends x=205; pie tail x=48).

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


def draw_ne_envelope_LR(draw):
    """疒 envelope compressed for L-R composition; heng ends at x=205."""
    # Stroke 1: top 点 — small tapered slash upper-left of heng.
    _tapered_line(draw, (170, 55), (188, 82), w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng — thin horizontal roof from x=92 to x=208.
    _tapered_line(draw, (92, 108), (208, 105), w_head=5.0, w_tail=5.0, n=30)

    # Stroke 3: 撇 (long left-falling sweep) welded at heng's left end.
    _tapered_bezier(
        draw,
        p0=(92, 108),
        p1=(38, 278),
        ctrl=(58, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # Stroke 4: 冫 upper mark — 点 (short slash), left-interior, clear of pie.
    _tapered_line(draw, (60, 140), (82, 162), w_head=3.0, w_tail=7.0, n=18)

    # Stroke 5: 冫 lower mark — 提 (rising flick), THICKER and lower,
    #           clearly separated from upper 点.
    _tapered_line(draw, (48, 225), (92, 208), w_head=8.5, w_tail=2.5, n=22)


def draw_jie_inside_small_v2(draw):
    """卩 tucked INSIDE the 疒 envelope, right side. 横折钩 + 竖.

    Positioning fix: shu moved right to x=165 (was 156) so it stands clear
    of the pie descent. Right-vertical of 横折 sharper (near-straight).
    """
    # Stroke 1: 横折钩
    # Top-heng of 卩 rectangle:
    p_h_start = (163, 122)
    p_corner = (215, 118)
    # heng
    _tapered_line(draw, p_h_start, p_corner, w_head=5.0, w_tail=6.0, n=22)

    # Right vertical (short, almost straight down with tiny inward curve)
    p_v_end = (206, 175)
    prev = p_corner
    ctrl = (218, 148)
    steps = 24
    for i in range(1, steps + 1):
        u = i / steps
        omu = 1 - u
        x = omu * omu * p_corner[0] + 2 * omu * u * ctrl[0] + u * u * p_v_end[0]
        y = omu * omu * p_corner[1] + 2 * omu * u * ctrl[1] + u * u * p_v_end[1]
        w = max(2, int(round(6.5 - 1.0 * u)))
        draw.line([prev, (x, y)], fill=(0, 0, 0), width=w)
        prev = (x, y)

    # small hook tick at end of 横折
    _tapered_line(draw, (p_v_end[0], p_v_end[1] + 1),
                  (p_v_end[0] - 15, p_v_end[1] + 12),
                  w_head=6.5, w_tail=2.0, n=14)

    # Stroke 2: long 竖 — on the LEFT edge of 卩, from top-heng start descending
    # past envelope base. Thicker and slightly to the right of pie for clarity.
    _tapered_line(draw, (167, 122), (165, 288), w_head=6.5, w_tail=6.5, n=44)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_envelope_LR(draw)
    draw_jie_inside_small_v2(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_疖.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
