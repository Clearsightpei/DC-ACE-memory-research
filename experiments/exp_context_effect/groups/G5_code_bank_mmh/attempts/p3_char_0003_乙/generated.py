"""p3_char_0003_乙 — Phase-3 character 乙.

Single-stroke character; identical shape to the Phase-2 radical 乙
already promoted to the bank as `yi_second.py`. Use the bank primitive
as-is (PASSed as a radical in bootstrap; the character form is the
same S/hook curve occupying the full canvas).

MMH structural expectations:
  - stroke count: 1
  - stroke 1 head @ ('TL', 0.715, 0.955)  → pixel ~(71.5, 95.5)
  - stroke 1 tail @ ('BR', 0.49, 0.083)   → pixel ~(249, 208.3)
  - joints: none

Bank primitive endpoints (reference canvas 300x300):
  - top_start (head) = (95, 125)  → ML cell (adjacent to expected TL)
  - hook_end  (tail) = (222, 240) → BR cell (same cell as expected)

Both endpoints land in the same-or-adjacent cell vs MMH expectation,
which meets the self-check tolerance ("±0.20 x_frac/y_frac OR
same/adjacent cell"). We proceed with the bank primitive un-modified.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"),
)
from yi_second import draw_yi_second  # noqa: E402

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 1 continuous S-curve, matches expected 1
    "endpoint_mismatches": [
        {
            "stroke": 1,
            "endpoint": "head",
            "expected": ("TL", 0.715, 0.955),
            "actual_pixel": (95, 125),
            "note": "in ML cell (adjacent to TL) — within tolerance",
        },
        {
            "stroke": 1,
            "endpoint": "tail",
            "expected": ("BR", 0.49, 0.083),
            "actual_pixel": (222, 240),
            "note": "in BR cell (same cell) — within tolerance",
        },
    ],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "Reused bootstrap-PASS bank primitive yi_second.py; same shape.",
}


def main() -> None:
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_yi_second(draw, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / "01_乙.png"
    img.save(out)


if __name__ == "__main__":
    main()
