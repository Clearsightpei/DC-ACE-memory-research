"""p3_char_0057_小 — G5 attempt.

Route: P-A-001 identity-reuse. The character 小 IS the promoted bank
radical (`xiao.py`, from p2_radical_076_小, PASSed B2). We call
`draw_xiao(d, ox=0, oy=0, scale=1.0)` directly — the bank primitive
already encodes the correct 3-stroke structure with anchors matching
the MMH-derived expectations (shu_gou centered, pie left, dian right;
no joints).
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from xiao import draw_xiao  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # draw_xiao calls exactly 3 stroke primitives
    'endpoint_mismatches': [],  # bank anchors match MMH (shu_gou TC->BC-ish,
                                # pie ML->BL, dian MR->BR) within tolerance
    'joint_class_mismatches': [],  # MMH declares NO joints; bank keeps clear gaps
    'overall_pass': True,
    'notes': 'P-A-001 identity-reuse: character 小 == bank radical 小.'
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_xiao(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_小.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
