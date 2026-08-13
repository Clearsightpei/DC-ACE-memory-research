# p3_char_0456_疮 (chuāng) — sore/wound.
# Structure: 疒 envelope (top-left) enclosing 仓 (cāng) interior.
# 疒: 5 strokes (top dian + heng roof + long pie + two 冫 marks).
# 仓 interior (top-right, tucked under heng): pie+na 人-cap + short heng + 巳-like rounded enclosure with hook.
#
# Bank use:
#   - ne_sick.py structure copied inline (bank fn draws at full-canvas scale;
#     for 疮 the envelope is still full-canvas, but shifted slightly left/up
#     to leave room for the 仓 interior on the right side).
#   - 仓 has no bank entry; inlined fresh with GT-thin uniform widths per
#     drawer_memory "trust GT" posture.

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


def draw_chuang(draw):
    # ---------- 疒 envelope (inline from ne_sick bank) ----------
    # Top dian (right of heng): small slash.
    _tapered_line(draw, (175, 45), (192, 68), w_head=3.0, w_tail=6.5, n=18)

    # Heng roof — thin, spans mid-left to right edge.
    _tapered_line(draw, (125, 92), (240, 90), w_head=4.5, w_tail=4.5, n=30)

    # Long 撇 descending from heng's left end, slight leftward bow.
    _tapered_bezier(
        draw,
        p0=(125, 92),
        p1=(55, 275),
        ctrl=(80, 190),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # Two 冫 interior marks, tucked in the LEFT belly (off pie shaft).
    _tapered_line(draw, (55, 130), (78, 152), w_head=3.0, w_tail=6.0, n=18)   # upper dian
    _tapered_line(draw, (38, 210), (75, 195), w_head=7.5, w_tail=2.5, n=20)   # lower ti

    # ---------- 仓 interior (right side of envelope, inline fresh) ----------
    # Interior occupies roughly x=110..255, y=100..280.

    # 人-cap: pie from apex (185, 110) sweeping down-left.
    _tapered_bezier(
        draw,
        p0=(185, 110),
        p1=(140, 175),
        ctrl=(162, 145),
        w_head=5.0,
        w_tail=3.5,
        n=60,
    )
    # 人-cap: na from apex (185, 110) sweeping down-right.
    _tapered_bezier(
        draw,
        p0=(185, 110),
        p1=(240, 175),
        ctrl=(215, 145),
        w_head=3.5,
        w_tail=6.5,
        n=60,
    )

    # Small middle 点 stroke under the 人 cap (a tiny dot mark inside 仓).
    _tapered_line(draw, (178, 178), (192, 195), w_head=3.0, w_tail=6.0, n=18)

    # 巳-like rounded loop at bottom — compact, rounded, with small hook.
    # Approximate with an ellipse outline for the rounded body + a small
    # hook flick at the top-right closure.
    # Top edge (short heng): (155, 210) → (225, 210).
    _tapered_line(draw, (158, 212), (222, 212), w_head=4.5, w_tail=4.5, n=25)
    # Left side (short shu going down): (158, 212) → (158, 255).
    _tapered_line(draw, (158, 212), (158, 258), w_head=4.5, w_tail=4.5, n=22)
    # Rounded bottom + right rise as 竖弯钩:
    _tapered_bezier(
        draw,
        p0=(158, 258),
        p1=(225, 220),
        ctrl=(225, 265),
        w_head=4.5,
        w_tail=4.5,
        n=70,
    )
    # Small hook flick up at end.
    _tapered_line(draw, (225, 220), (218, 208), w_head=4.5, w_tail=2.5, n=12)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_chuang(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疮.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
