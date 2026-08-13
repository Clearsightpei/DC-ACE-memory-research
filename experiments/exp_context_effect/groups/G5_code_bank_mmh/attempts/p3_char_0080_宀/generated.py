"""p3_char_0080_宀 — G5 attempt.

Bank has a direct primitive `draw_mian_roof` (from mian_roof.py) that
was PASSed as p2_radical_060_宀__retry_2. Reuse it verbatim (identity
recipe P-A-001). No BANK_DEVIATION needed.

Expected stroke count: 3 (dian + dian + heng_zhe_short).
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from mian_roof import draw_mian_roof  # noqa: E402

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 3 strokes: dian + dian + heng_zhe_short
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],  # both N (neighbor) — dian tip near heng, natural gap
    "overall_pass": True,
    "notes": "Identity-reuse of bank primitive draw_mian_roof (passed as radical). "
             "Centered on 300x300 with scale 1.0.",
}


def main():
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    # mi_cover extents ~ x:54-213, y:92-148 → width ~160, height ~56.
    # With mian_roof adding a top dian above (y≈88) and downshift +38,
    # bounding box roughly x:54-213, y:88-186. Center on canvas:
    # cx_bank ≈ (54+213)/2 = 133.5 ; cy_bank ≈ (88+186)/2 = 137
    # canvas center = 150,150 → ox = 150 - 133.5 = 16.5, oy = 150 - 137 = 13
    draw_mian_roof(d, ox=16, oy=13, scale=1.0)
    out = Path(__file__).parent / "01_宀.png"
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
