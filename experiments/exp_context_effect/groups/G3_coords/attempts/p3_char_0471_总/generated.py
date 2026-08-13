# 总 (zǒng) — 3 components: 丷 (top) + 口 (middle) + 心 (bottom).
# Stacked vertically; 心 spans the widest, 口 is compact middle, 丷 caps top.
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ba_dot import draw_ba_dot   # noqa: E402
from kou import draw_kou         # noqa: E402
from xin import draw_xin         # noqa: E402


CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Top 丷 — slanting dot pair in top ~1/5. ba_dot canonical goes y=0..-50 down.
    draw_ba_dot(d, ox=0, oy=120, scale=0.75)

    # Middle 口 — compact box in upper-middle. Bigger than pass1.
    draw_kou(d, ox=0, oy=35, scale=0.55)

    # Bottom 心 — wide bowl + three dots occupying bottom half. Shift higher so
    # 心 doesn't sink to canvas edge. xin dots don't scale; keep scale ~1.0.
    draw_xin(d, ox=0, oy=-45, scale=1.0)

    out_path = os.path.join(_HERE, "01_总.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
