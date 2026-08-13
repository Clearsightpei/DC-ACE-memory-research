# BANK_DEVIATION
# skipped: yi_radical.py (乙 primitive)
# reason: 乙 here is the character's right/bottom envelope (tall + wide sweep
#   from top-right around to bottom-left), not the compact standalone 乙.
#   Bank 乙 is compact; this needs an elongated right-side hook that
#   spans full character height.
# fresh_component: yi_envelope_right_for_乹
#
# 乹 = 卓 (left, stacked) + 乙 (right envelope sweep).
# Left: top 十 (short heng + shu) + 日 body + shu extending down + bottom heng.
# Right: elongated 乙 hook wrapping down the right side.

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def draw_left_zhuo(t, ink=4):
    """卓-like left component: 十 on top + 日 body + long shu + short bottom heng."""
    # 1. top short heng
    t.line([(50, 50), (135, 50)], fill=(0, 0, 0), width=ink)
    # 2. top shu crossing the top heng
    t.line([(92, 28), (92, 92)], fill=(0, 0, 0), width=ink)
    # 3. 日 body — left shu
    t.line([(65, 95), (65, 175)], fill=(0, 0, 0), width=ink)
    # 4. 日 body — top heng + right shu (横折)
    t.line([(65, 95), (130, 95)], fill=(0, 0, 0), width=ink)
    t.line([(130, 95), (130, 175)], fill=(0, 0, 0), width=ink)
    # 5. 日 body — middle heng
    t.line([(65, 135), (130, 135)], fill=(0, 0, 0), width=ink)
    # 6. 日 body — bottom heng
    t.line([(65, 175), (130, 175)], fill=(0, 0, 0), width=ink)
    # 7. long central shu extending downward from 日
    t.line([(92, 92), (92, 240)], fill=(0, 0, 0), width=ink)
    # 8. bottom heng (medium-wide, sits below 日)
    t.line([(35, 240), (155, 240)], fill=(0, 0, 0), width=ink)


def draw_right_yi_envelope(t, ink=5):
    """Elongated 乙 envelope on the right — stamped-circle path for a
    smooth heavy curve from top-right, down the right side, hooking
    back to a bottom-right endpoint."""
    def stamp(x, y, r):
        t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))

    # Path: 乙 as right-side envelope — short heng at top, down the right
    # with a gentle bow, wide sweep across bottom, small up-tick at end.
    path = [
        (180, 50),
        (215, 48),
        (240, 55),
        (238, 90),
        (232, 140),
        (225, 195),
        (215, 235),
        (200, 255),
        (185, 260),
        (170, 258),
        (172, 245),  # small up-tick hook
    ]
    widths = [3.0, 4.5, 5.5, 6.0, 6.5, 7.0, 7.5, 7.5, 6.5, 5.0, 2.5]

    steps_per_seg = 60
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(steps_per_seg + 1):
            u = s / steps_per_seg
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            w = w0 + (w1 - w0) * u
            stamp(x, y, w / 2.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_left_zhuo(t, ink=4)
    draw_right_yi_envelope(t, ink=5)
    out = Path(__file__).parent / "01_乹.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
