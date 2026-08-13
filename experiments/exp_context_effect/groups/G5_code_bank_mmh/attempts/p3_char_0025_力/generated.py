"""p3_char_0025_力 — 力 (2 strokes: heng_zhe_gou + pie, P-joint at center).

Reuses the bank primitive `li_power.py` which was promoted from the
p2_radical_025_力 B1 PASS. The character and radical are identical, so
we call `draw_li(draw)` directly at scale=1.0 with no offset.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from li_power import draw_li  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,     # draw_li -> heng_zhe_gou (1) + pie (1) = 2
    "endpoint_mismatches": [],   # bank primitive PASSed for this exact char in B1
    "joint_class_mismatches": [], # P at center: heng_zhe_gou body pierced by pie
    "overall_pass": True,
    "notes": "Reusing bank primitive li_power (promoted from p2_radical_025_力 PASS).",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_li(draw, ox=0, oy=0, scale=1.0)
    out = HERE.parent / "01_力.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
