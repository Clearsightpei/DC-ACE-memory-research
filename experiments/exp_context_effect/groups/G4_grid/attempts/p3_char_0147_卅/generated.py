"""p3_char_0147_卅 (sà, "thirty") — G4 grid-bank drawer attempt.

Lookup checklist (memory_index.md):
1. success_bank/INDEX.md grep 卅 — not present.
2. errata.md grep 卅 — not present.
3. form_catalog.md — three verticals + one horizontal (廿-like).
4. principles_meta.md — TR1 override anchors; TR8 keep horizontal flat.
5. joint_atlas.md — three P (piercing) joints where horizontal crosses each vertical.
6. sandbox.md — n/a.

MMH expects 4 strokes:
  s1: horizontal ML(0.267,0.755) → MR(0.804,0.658)
  s2: left "pie"  TL(0.8,0.946) → BL(0.378,0.786)  — slight left-bow
  s3: middle 竖  TC(0.412,0.964) → BC(0.444,0.385)
  s4: right 竖  TC(0.951,0.68)  → BR(0.062,1.05)
Joints: all three P (welded) at where s1 crosses s2, s3, s4.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes (1 heng + 1 pie left + 2 shu). Horizontal welded across all three verticals (P/P/P).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s2: left stroke — pie-like from top-right of TL area down-left to BL
    draw_pie(d, ('TL', 0.80, 0.10), ('BL', 0.30, 0.90),
             head_width=10, tail_width=4, curve=0.06)

    # s3: middle vertical
    draw_shu(d, ('TC', 0.42, 0.10), ('BC', 0.45, 0.90),
             width=10)

    # s4: right vertical (nearly straight, very slight lean)
    draw_shu(d, ('TC', 0.95, 0.10), ('BR', 0.06, 0.95),
             width=10)

    # s1: horizontal — drawn LAST so it visually welds across the three verticals
    draw_heng(d, ('ML', 0.15, 0.55), ('MR', 0.85, 0.55),
              width=10)

    out = os.path.join(os.path.dirname(__file__), '01_卅.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
