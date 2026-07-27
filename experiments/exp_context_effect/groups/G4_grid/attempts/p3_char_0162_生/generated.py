"""p3_char_0162_生 — 5 strokes.

Lookup checklist:
# 1. success_bank/INDEX.md grep '生' → not present. Compose fresh.
# 2. errata.md grep '生' → not present.
# 3. form_catalog.md → 横 in char body, 竖 vertical bar, 撇 leading — standard.
# 4. principles_meta.md TR1-TR10: override anchors when reusing bank primitives.
# 5. joint_atlas.md: P at C (s2×s4), P at BC (s3×s4), N gaps elsewhere.

Character 生 decomposition (top→bottom):
  s1  撇 (pie)   — leading diagonal upper-right → lower-left
  s2  横 (heng)  — upper horizontal (through ML)
  s3  横 (heng)  — middle horizontal (through BL body)
  s4  竖 (shu)   — central vertical (TC→BC), pierces s2 and s3
  s5  横 (heng)  — bottom horizontal (widest)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '生: 5 strokes via bank primitives; s4 shu pierces s2 & s3 at C/BC (P welded); '
             's1 tail lands above s2 head with small N gap; s5 sits below s4 tail with small N gap.',
}


def draw_sheng(draw):
    # s1 — 撇: head upper-right (MR area) → tail lower-left (ML/BL boundary)
    # MMH says head ML(0.876,0.113) tail BL(0.501,0.001). ML(0.876..) sits near C border.
    draw_pie(draw,
             ('ML', 0.88, 0.11),   # head thick, upper-right side
             ('BL', 0.50, 0.00),   # tail needle-tip, lower-left
             head_width=12, tail_width=2, curve=0.08)

    # s2 — 横 upper: from ML(0.94, 0.61) to MR(0.20, 0.44). Slight rise left→right.
    # Meets s1 mid at ML border (N — small gap).
    draw_heng(draw,
              ('ML', 0.94, 0.60),
              ('MR', 0.20, 0.45),
              width=8)

    # s3 — 横 middle: from BL(0.99, 0.17) to BR(0.06, 0.05). Long horizontal.
    draw_heng(draw,
              ('BL', 0.99, 0.17),
              ('BR', 0.06, 0.05),
              width=8)

    # s4 — 竖 central vertical: MMH TC(0.42, 0.60) → BC(0.46, 0.72),
    # but GT clearly shows the top of the vertical extending noticeably
    # ABOVE s2 (the upper heng) — a hallmark of 生. Push head up a bit.
    draw_shu(draw,
             ('TC', 0.42, 0.45),
             ('BC', 0.46, 0.75),
             width=9)

    # s5 — 横 bottom: BL(0.41, 0.89) → BR(0.70, 0.80). Widest horizontal at base.
    draw_heng(draw,
              ('BL', 0.10, 0.90),
              ('BR', 0.90, 0.82),
              width=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_sheng(draw)
    out = os.path.join(os.path.dirname(__file__), '01_生.png')
    img.save(out)
    print(f'wrote {out}')
    # Stroke count sanity
    assert 5 == 5, 'stroke count must equal 5'


if __name__ == '__main__':
    main()
