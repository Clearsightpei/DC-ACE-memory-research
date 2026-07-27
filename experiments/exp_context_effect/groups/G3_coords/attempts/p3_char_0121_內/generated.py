# p3_char_0121_內 — 内 (nèi, "inside"), 4 strokes.
# Stroke order: 1) 竖 left, 2) 横折钩 (top+right+hook), 3) 撇 inside, 4) 捺 inside (人).
# GT shows a wider envelope than 门, with 人 nested inside.
# Envelope pattern adapted from men_char (tall/narrow) but wider aspect for 内.
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie, variant_na  # noqa: E402


def _tapered_line(D, p0, p1, w0, w1, steps=32):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_nei(D):
    # Envelope corners (PIL px). GT shows a rectangular-ish frame
    # slightly wider than tall, centered near canvas mid, with a small
    # gap between left-竖 top and top-heng start (typical of 内's opening).
    # Left vertical (short 竖) — extends from ~y=60 to y=250
    left_top = (75, 60)
    left_bot = (78, 258)
    _tapered_line(D, left_top, left_bot, w0=6, w1=7, steps=32)
    D.ellipse([left_top[0] - 3, left_top[1] - 3,
               left_top[0] + 3, left_top[1] + 3], fill=(0, 0, 0))
    D.ellipse([left_bot[0] - 4, left_bot[1] - 4,
               left_bot[0] + 4, left_bot[1] + 4], fill=(0, 0, 0))

    # 横折钩: top-heng + right-shu + hook. Starts slightly right of
    # left-竖 top with a small gap; extends across, turns down, hooks left.
    h_left = (95, 62)
    h_right = (238, 60)
    _tapered_line(D, h_left, h_right, w0=6, w1=8, steps=28)

    v_top = (238, 60)
    v_bot = (232, 252)
    _tapered_line(D, v_top, v_bot, w0=8, w1=7, steps=32)
    D.ellipse([v_top[0] - 4, v_top[1] - 4,
               v_top[0] + 4, v_top[1] + 4], fill=(0, 0, 0))

    # Hook at bottom of the shu (leftward)
    hook_end = (v_bot[0] - 18, v_bot[1] - 12)
    _tapered_line(D, (v_bot[0], v_bot[1] + 1), hook_end,
                  w0=7, w1=2, steps=14)

    # Inside 人: 撇 + 捺, meeting at apex high inside the frame.
    # Math coords: center (150,150), +y up. Convert helpers accept math.
    # Apex up near y=+55 (PIL ~95), just below the top-heng.
    apex_math = (-5, 55)
    # 撇 from apex sweeping down-left toward inside-lower-left
    pie_tail_math = (-55, -85)
    variant_pie(D, head=apex_math, tail=pie_tail_math,
                bow_perp=-8.0, w_head=6.0, w_tail=1.8, n=48)
    # 捺 from apex sweeping down-right with a belly, ending
    # lower-right, tapering to a thin tail.
    na_tail_math = (60, -90)
    variant_na(D, head=apex_math, tail=na_tail_math,
               bow_perp=8.0, w_head=2.0, w_belly=11.0, w_tail=2.5,
               belly_u=0.78, n=56)


def main():
    img = Image.new("RGB", (300, 300), "white")
    D = ImageDraw.Draw(img)
    draw_nei(D)
    out = os.path.join(_HERE, "01_內.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
