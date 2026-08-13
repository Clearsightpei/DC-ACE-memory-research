# p3_char_0173_仔__retry_1__rerun — 仔 (zǐ), 6 strokes: 亻(2) + 子(3).
#
# VISUAL DIFF — prior retry_1 vs GT (per rerun MANDATORY STEP 0)
# Observations from opening both PNGs:
#   1. HEAVY BLOB at top of 子 in prior. The prior render used `liao`
#      whose `_hengou` helper paints a 7-radius filled ellipse at the
#      横钩 shoulder. GT shows uniform-thin ink with NO shoulder blob.
#      Under v8 "trust GT" — drop the blob entirely.
#   2. 亻 top-撇 also has a small thick head in prior (from bank pie
#      taper). GT's 亻 pie is uniform thin, no bulge at the head.
#   3. Prior's 子 crossing 横 is TOO SHORT (~120px, x=145..265) AND
#      too high (y~165). GT's 横 spans wider (x≈140..280) and sits
#      slightly higher-left / lower-right — the whole char reads
#      wider because of this long crossbar.
#   4. Prior's 亻 shu appears fine but slightly short; GT's shu
#      descends noticeably below the crossbar-heng level.
#
# Fix strategy — inline fresh with uniform thin ink (~5px) matching
# GT's MMH-thin aesthetic; NO shoulder ellipses; long crossbar for 子.
# This is a v8 "trust GT over bank" rewrite (per B5 lesson: helpers
# with baked-in calligraphic embellishments override GT if used blindly).
#
# RETRY MEMORY CHECKLIST
# Q1 (errata): errata says "use zi_char (bank #122) verbatim at
#   scale 0.65, ox=+40". But zi_char calls liao → _hengou → blob
#   ellipse. That's what produced the prior fail. Fix idea is
#   correct in spirit (reuse 子 structure) but wrong in mechanism
#   (bank primitives carry the blob). Trust-GT posture: inline thin.
# Q2 (form_catalog): 亻-family rows say ren_pang identity on left;
#   right component is the fail. Right is 子 — 3 strokes: 横撇,
#   弯钩, 长横. Inline them thin.
# Q3 (helpers): fail is embellishment-mismatch (blob vs no-blob), not
#   a weld/kiss geometry gap. No adaptive helper applies. Under v8,
#   inline fresh with thin uniform lines.

import os
from PIL import Image, ImageDraw


INK = 5  # uniform thin stroke width to match GT MMH aesthetic


def _line(draw, p0, p1, w=INK):
    draw.line([p0, p1], fill="black", width=w)


def _bezier(draw, p0, p1, p2, w=INK, steps=28):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps

        def bez(u):
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
            return (x, y)
        draw.line([bez(u0), bez(u1)], fill="black", width=w)


def draw_ren_pang_thin(draw):
    """Left 亻: uniform thin 撇 + shu. No calligraphic taper/blob."""
    # 撇: from upper-right sweeping down-left, slight bow
    _bezier(draw, (98, 62), (75, 130), (40, 210), w=INK)
    # 竖: short vertical from mid-撇 shaft, descending
    _line(draw, (82, 118), (82, 235), w=INK)


def draw_zi_thin(draw):
    """Right 子: 横撇 + 弯钩 + long 横. Thin uniform."""
    # 1. 横撇 top: horizontal segment then a small turn down-left
    #    horizontal part
    _line(draw, (148, 75), (232, 72), w=INK)
    #    turn: sharp diagonal down-left from right end
    _line(draw, (232, 72), (216, 96), w=INK)

    # 2. 弯钩 descender: curves from just below 横撇 turn, gently
    #    bowing right then sweeping back left with a small hook tail.
    #    Main body — S-ish curve via two beziers
    _bezier(draw, (218, 92), (222, 155), (210, 215), w=INK)
    #    small hook back to the left at tail
    _bezier(draw, (210, 215), (198, 225), (180, 222), w=INK)

    # 3. 长横 crossing: LONG horizontal that spans well past the
    #    弯钩 shaft on both sides. GT shows it sits at mid-height
    #    with a very slight upward tilt to the right (or nearly flat).
    _line(draw, (140, 158), (283, 152), w=INK)


def draw(draw_obj):
    draw_ren_pang_thin(draw_obj)
    draw_zi_thin(draw_obj)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), "01_仔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
