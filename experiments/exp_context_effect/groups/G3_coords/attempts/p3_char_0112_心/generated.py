# p3_char_0112_心 — first attempt.
# Identity alias: the Phase-3 character 心 has the same shape as the
# Phase-2 radical 心 already in the Success Bank (xin.py, entry #86).
# Per memory_index.md read-order step 3 (Phase-3 char + Phase-2 radical
# same shape → try IDENTITY alias first), call draw_xin with the
# defaults that PASSed the radical (center origin, scale=1.0).
import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from xin import draw_xin  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    # Identity alias — same (ox, oy, scale) used by the radical PASS.
    draw_xin(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_心.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
