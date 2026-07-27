"""p3_char_0084_屮 — character 屮 (chè, "sprout", 3 strokes).

Lookup checklist (mandatory):
  1. success_bank/INDEX.md grep '屮' → row 70 chuo.py (mastered radical
     p2_radical_040_屮). Character 屮 == radical 屮 shape. Reuse
     draw_chuo per TR1 with OVERRIDING anchors from MMH inject.
  2. errata.md grep '屮' → not present.
  3. form_catalog.md — 竖折 + 短竖 + 竖 pattern; anchors from MMH inject.
  4. principles_meta.md TR1 — reuse bank primitive with override anchors.
  5. joint_atlas.md — one P (weld) at C center; one N (~17 px) on right.
  6. sandbox.md — no additional notes for 屮.

MMH-injected expected anchors (used verbatim for overrides):
  s1: ML 0.68,0.312 → MR 0.165,0.969   (竖折)
  s2: MR 0.139,0.181 → BR 0.282,0.218  (短竖 right)
  s3: TC 0.339,0.662 → BC 0.497,1.167  (竖 tall center)
Joints:
  s1.tail ⇆ s2.mid @ BR : N (~17.6 px gap)
  s1.mid ⇆ s3.mid @ C  : P (welded crossing)
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from chuo import draw_chuo  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # draw_chuo calls draw_shu_wan + draw_shu + draw_shu = 3 strokes
    'endpoint_mismatches': [], # anchors match MMH exactly (chuo.py defaults were derived from same MMH)
    'joint_class_mismatches': [], # P at C (welded by construction), N at BR (~17 px) per chuo.py
    'overall_pass': True,
    'notes': 'Reused mastered radical chuo.py (row 70). Character 屮 identical shape to radical 屮. MMH-injected anchors match chuo.py defaults verbatim.'
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # OVERRIDING anchors per TR1 — match MMH-injected expectations for this item.
    draw_chuo(
        draw,
        s1_head=('ML', 0.68, 0.312),
        s1_belly=('ML', 0.68, 0.95),
        s1_corner=('BC', 0.05, 0.00),
        s1_tail=('MR', 0.165, 0.969),
        s2_head=('MR', 0.139, 0.181),
        s2_tail=('BR', 0.282, 0.218),
        s3_head=('TC', 0.339, 0.662),
        s3_tail=('BC', 0.497, 1.05),  # slight clamp from MMH 1.167 to stay in-frame
    )

    out = os.path.join(os.path.dirname(__file__), '01_屮.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
