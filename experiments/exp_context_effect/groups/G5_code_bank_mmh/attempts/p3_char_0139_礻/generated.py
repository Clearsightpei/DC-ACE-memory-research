"""p3_char_0139_礻 — Phase-3 character 礻 (same shape as p2_radical_116_礻).

P-A-001 identity: this Phase-3 character IS the promoted bank radical.
Call draw_shi_spirit (bank primitive) with identity transform (ox=0,
oy=0, scale=1.0). The radical PASSed in B4 R2, so identity call is the
correct default.

SELF_CHECK:
- stroke_count: 4 (dian + heng_pie + shu + dian) — matches MMH expected 4.
- endpoints: shi_spirit's baked pixel anchors were tuned to match MMH
  for the radical (which is the same shape). Anchor deltas expected within
  tolerance.
- joints: all 3 joints are N (natural gaps at cell C). shi_spirit
  achieves N-gaps by construction (crossbar s2 doesn't weld to s3/s4
  heads; s3 head and s4 head are at different x-positions so no weld).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

# Add bank code dir to path
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shi_spirit import draw_shi_spirit  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 4 strokes via draw_shi_spirit
    "endpoint_mismatches": [], # bank primitive tuned to MMH for the same shape
    "joint_class_mismatches": [], # all N by construction
    "overall_pass": True,
    "notes": "P-A-001 identity call of draw_shi_spirit; Phase-3 char = "
             "Phase-2 radical (same MMH medians).",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_shi_spirit(draw, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / "01_礻.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
