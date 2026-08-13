"""p3_char_0124_文 — G5 attempt.

The character 文 is identical to the radical 文 (p2_radical_124_文, PASSed in B3).
Use the promoted whole-glyph bank primitive `wen_text.py` directly with no transform.

MMH stroke count: 4 (dian, heng, pie, na).
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from wen_text import draw_wen  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls inside draw_wen (dian, heng, pie, na)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [
        # s2.mid ⇆ s3.head — N (neighbor gap ~15px); bank uses default rendering,
        # heng ends near (223.8, 118.9), pie starts at (147.1, 136.2) → natural gap OK.
        # s3.mid ⇆ s4.mid — P (welded crossing); pie and na cross in the lower half.
    ],
    'overall_pass': True,
    'notes': 'Whole-glyph reuse of wen_text.py. Radical == character.'
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wen(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_文.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
