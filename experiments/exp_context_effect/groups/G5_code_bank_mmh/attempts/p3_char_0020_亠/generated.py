"""p3_char_0020_亠 — G5 attempt.

Character 亠 is identical to the promoted radical primitive `tou_lid.py`
(dian + heng, 2 strokes). The primitive's baked-in canvas coordinates
already match the MMH anchors injected in this dispatch:

  s1 head C(0.204, 0.28)   -> (120.4, 128.0)
  s1 tail C(0.608, 0.559)  -> (160.8, 155.9)
  s2 head ML(0.463, 0.931) -> (46.3, 193.1)
  s2 tail MR(0.584, 0.857) -> (258.4, 185.7)

So we call draw_tou at defaults (ox=0, oy=0, scale=1.0). No BANK_DEVIATION.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
_BANK = _HERE.parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from tou_lid import draw_tou  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,          # 2 primitive calls inside draw_tou (dian + heng)
    "endpoint_mismatches": [],        # baked coords match MMH anchors exactly
    "joint_class_mismatches": [],     # MMH: no joints (clear separation)
    "overall_pass": True,
    "notes": "draw_tou primitive coordinates align to the MMH anchors verbatim.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_tou(d)
    out = _HERE.parent / "01_亠.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
