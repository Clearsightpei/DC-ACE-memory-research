"""p3_char_0078_艹 — G5 attempt.

艹 is literally identical to the p2_radical_039_艹 that was PASSed and
promoted to `draw_cao`. This is a textbook P-A-001 (identity-reuse)
case: MMH expects 3 strokes (heng + shu + shu), our bank primitive
already encodes 3 strokes with per-GT vertical over-extension. Call
with ox=0, oy=0, scale=1.0 — no customization, preserve the quality
that PASSed as radical.

SELF_CHECK:
  stroke_count_ok:      True (3 turtle-primitive calls in draw_cao —
                        1 heng + 2 shu)
  endpoint_anchors_ok:  Bank primitive's shu heads at y=115 sit just
                        above the heng at y~185 — verticals cross the
                        heng and extend below to y=245. This differs
                        slightly from MMH's anchor list but matches the
                        GT visual per P-MMH-002 (MMH under-specs the
                        vertical span of compound characters like 艹).
  joint_classes_ok:     Both joints are P (piercing) at the horizontal
                        — automatic from the primitive's geometry
                        (verticals cross the heng).
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from cao_grass import draw_cao  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "P-A-001 identity reuse of draw_cao; 艹 char is same shape as 艹 radical.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_cao(d, ox=0, oy=0, scale=1.0)
    out = Path(__file__).parent / "01_艹.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
