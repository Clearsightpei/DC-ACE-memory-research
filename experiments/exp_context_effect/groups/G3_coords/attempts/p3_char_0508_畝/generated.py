# p3_char_0508_畝 — 畝 (mǔ, "Chinese acre") — 10 strokes
# Structure: 亠 (top spanning left+mid) over 田 (bottom-left, compressed)
# with 攵/夂 on the right (top-right horizontal + upper pie + lower na).
# Uses the v13 bank variant quan_tian_for_LR_left.py (explicitly named
# in its docstring as a template for 畝). Right side inlined fresh.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # noqa: E402


def draw_mu(d):
    black = (0, 0, 0)
    w = 3   # GT uses thin uniform ink
    wm = 3

    # --- 亠 on top (spans left+middle, over 田) ---
    # dian (small slanted stroke at top-center of 亠)
    d.line([(95, 32), (108, 48)], fill=black, width=w)
    # heng (long horizontal spanning across, over 田 column)
    d.line([(28, 78), (185, 78)], fill=black, width=w)

    # --- 田 compressed on the bottom-left ---
    draw_quan_tian_for_LR_left(d,
                               x_left=38, x_right=130,
                               y_top=115, y_bot=225,
                               w=w, wm=wm)

    # --- 攵/夂 on the right ---
    # short horizontal near top-right (the 攵 top heng)
    d.line([(195, 92), (240, 92)], fill=black, width=wm)
    # small dian above-right of that heng (attaches near top-right)
    d.line([(228, 72), (238, 88)], fill=black, width=w)
    # upper pie: sweeps from upper-right down-left into 田's right-middle area
    for seg in range(28):
        t0 = seg / 28.0
        t1 = (seg + 1) / 28.0
        def pt(t):
            # curve from (232,100) -> (200,170) -> (165,240)
            x = (1 - t) * (1 - t) * 232 + 2 * (1 - t) * t * 200 + t * t * 165
            y = (1 - t) * (1 - t) * 100 + 2 * (1 - t) * t * 170 + t * t * 240
            return (x, y)
        d.line([pt(t0), pt(t1)], fill=black, width=wm)
    # na: sweeps from upper-mid heading down-right, ending near lower-right
    for seg in range(30):
        t0 = seg / 30.0
        t1 = (seg + 1) / 30.0
        def pt2(t):
            # curve from (198,130) -> (235,190) -> (280,252)
            x = (1 - t) * (1 - t) * 198 + 2 * (1 - t) * t * 235 + t * t * 280
            y = (1 - t) * (1 - t) * 130 + 2 * (1 - t) * t * 190 + t * t * 252
            return (x, y)
        d.line([pt2(t0), pt2(t1)], fill=black, width=wm)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_mu(d)
    out = os.path.join(os.path.dirname(__file__), "01_畝.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
