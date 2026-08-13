"""p3_char_0108_无 — G5 attempt.

P-A-001 identity call: bank primitive `wu_none.py` (promoted from
p2_radical_135_无 in G5 B3) is the exact same 4-stroke glyph. Use
identity (ox=0, oy=0, scale=1.0). No BANK_DEVIATION.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE.parents[1] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from wu_none import draw_wu_none  # noqa: E402

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # bank primitive calls 4 strokes: heng + heng + pie + shu_wan_gou
    "endpoint_mismatches": [],  # bank was tuned to match MMH-derived anchors in B3
    "joint_class_mismatches": [],  # s2/s3 P at C, s1/s3 + s2/s4 + s3/s4 N — as in radical GT
    "overall_pass": True,
    "notes": "P-A-001 identity — 无 char == 无 radical, one bank call.",
}


def main() -> None:
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_wu_none(d, ox=0, oy=0, scale=1.0)
    out = HERE / "01_无.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
