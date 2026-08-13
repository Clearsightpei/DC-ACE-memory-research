# p3_char_0382_疠 — 疠 = 疒 envelope (bank: ne_sick) + 万 inside lower-right.
#
# Composition:
#   - 疒 envelope (5 strokes) inlined from bank ne_sick.py — the bank
#     entry preserves module-level PIL rendering, so we reuse its
#     _tapered_line / _tapered_bezier helpers here.
#   - 万 inside: 3 strokes (heng, heng-zhe-gou, pie). Kept thin per
#     drawer_memory "trust GT (MMH-thin)" posture. Tucked into the
#     lower-right belly so it clears the pie descender.
#
# GT read: envelope sits upper-left with a long descending pie; 万
# occupies the lower-right, its pie sweeping down-left toward the
# envelope pie but not touching it, and its heng-zhe-gou anchoring
# the right edge with a small leftward hook.

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


def draw_ne_envelope(draw):
    """疒 envelope — inlined from success_bank/code/ne_sick.py."""
    # Stroke 1: top 点 (small slash, upper-right of envelope).
    _tapered_line(draw, (160, 45), (177, 68), w_head=3.0, w_tail=6.5, n=18)
    # Stroke 2: heng — thin horizontal roof.
    _tapered_line(draw, (108, 98), (208, 95), w_head=4.5, w_tail=4.5, n=30)
    # Stroke 3: long 撇 welded at heng's left end.
    _tapered_bezier(
        draw,
        p0=(108, 98),
        p1=(48, 268),
        ctrl=(71, 190),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )
    # Stroke 4: 冫 upper 点 — short slash tucked in belly.
    _tapered_line(draw, (41, 128), (63, 148), w_head=3.0, w_tail=6.0, n=18)
    # Stroke 5: 冫 lower 提 — rising flick, thick→thin.
    _tapered_line(draw, (21, 208), (58, 192), w_head=7.5, w_tail=2.5, n=20)


def draw_wan_inside(draw):
    """万 (three strokes) tucked into the lower-right belly of 疒."""
    # Stroke 1: heng — thin top bar of 万.
    _tapered_line(draw, (128, 138), (238, 138), w_head=4.5, w_tail=4.5, n=30)
    # Stroke 2: 横折钩 — starts at right end of heng, descends, hooks left.
    # Descending shaft (vertical, slightly leaning right→left).
    _tapered_line(draw, (232, 138), (222, 258), w_head=5.0, w_tail=4.5, n=40)
    # Hook: short leftward flick at the bottom.
    _tapered_line(draw, (222, 258), (204, 244), w_head=5.0, w_tail=2.5, n=15)
    # Stroke 3: 撇 — sweeps down-left from top bar into lower-left interior.
    _tapered_bezier(
        draw,
        p0=(178, 138),
        p1=(112, 275),
        ctrl=(140, 210),
        w_head=6.0,
        w_tail=3.5,
        n=80,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_envelope(draw)
    draw_wan_inside(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疠.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
