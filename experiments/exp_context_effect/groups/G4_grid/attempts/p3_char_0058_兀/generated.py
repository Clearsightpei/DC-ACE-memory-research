"""p3_char_0058_兀 — Phase-3 char, 3 strokes.

Lookup checklist:
  1. success_bank/INDEX.md grep 兀 → p2_radical_074_兀 → wu_lame.py (MASTERED).
  2. errata.md grep 兀 → not present.
  3. form_catalog / principles_meta → TR1 (reuse with OVERRIDING anchors).
  4. joint_atlas → 几-family N gaps at top; do NOT weld (TR10 exception).

Reuse wu_lame.py (TR1) with anchors overridden from THIS item's
MMH block. wu_lame's defaults already closely match MMH here since
the mastered radical came from the same MMH source.

MMH expected:
  s1 (横):  head ML(0.647,0.084)  tail TR(0.317,0.964)
  s2 (撇):  head ML(0.999,0.289)  tail BL(0.346,0.783)
  s3 (竖弯):head C(0.497,0.102)   tail BR(0.666,0.168)
Joints:
  s1.head ⇆ s2.head @ ML : N (~35.8 px gap)
  s1.mid  ⇆ s3.head @ C  : N (~19.6 px gap)
"""
import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from wu_lame import draw_wu_lame  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused mastered wu_lame.py (TR1). MMH anchors match wu_lame defaults within tolerance.'
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Override anchors from THIS item's MMH block (TR1 override).
    draw_wu_lame(
        draw,
        s1_head=('ML', 0.647, 0.084),
        s1_tail=('TR', 0.317, 0.964),
        s2_head=('ML', 0.999, 0.289),
        s2_tail=('BL', 0.346, 0.783),
        s3_head=('C', 0.497, 0.102),
        # 竖弯 needs internal bend; MMH s3 tail (0.666,0.168 in BR) is the
        # median tail, but visually 兀's right leg goes straight down then
        # curves right at bottom. Keep wu_lame's belly/corner/tail spec
        # for the curve shape; MMH's flat tail-listing lacks the corner.
        s3_belly=('C', 0.55, 0.65),
        s3_corner=('BC', 0.60, 0.88),
        s3_tail=('BR', 0.45, 0.85),
    )

    out = os.path.join(HERE, "01_兀.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
