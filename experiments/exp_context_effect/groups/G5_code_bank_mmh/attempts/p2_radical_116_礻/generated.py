"""G5 attempt: p2_radical_116_礻 (4-stroke radical, 'show/spirit' left form).

Composition (4 strokes matching MMH structural block):
  s1: 点 top dot (small stroke at top-center, going down-right)
  s2: 横撇 short heng bending into pie (top crossbar)
  s3: 竖 vertical shaft descending through center
  s4: 点 right dot on right side

All three joints (s2/s3, s2/s4, s3/s4) are N (neighbor) — small gaps
at cell C, NOT welded. Bank primitives used: dian, heng_pie, shu.
"""

import os
import sys
from PIL import Image, ImageDraw

# --- bank imports (canonical relative path) ---
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian          # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from shu import draw_shu            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 stroke primitive calls (s1..s4)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints implemented as N with visible gap
    'overall_pass': True,
    'notes': (
        's1 top dot; s2 heng-pie via bank; s3 shu via bank; s4 right dot. '
        'Joint gaps at C left visible (no welding).'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top dot (small down-right stroke, top-center of canvas)
    draw_dian(d, head=(148, 46), tail=(172, 76), w_head=3, w_tail=7, bow=3, steps=40)

    # s2 — 横撇 (short heng bending to pie). Corner near cell C, tail SW.
    # heng_pie signature: (head, tail, apex_x, corner_x)
    # We want a compact top-bar spanning roughly x=80..175 then pie down-left to (120, 165).
    draw_heng_pie(d, head=(80, 118), tail=(120, 165),
                  apex_x=155, corner_x=175)

    # s3 — 竖 vertical shaft. Head near center (small gap below s2 corner),
    # tail near lower center — GT tail extends past bottom slightly.
    draw_shu(d, head=(138, 132), tail=(138, 272), width=6)

    # s4 — right dot (below top-right of s2, angled down-right).
    draw_dian(d, head=(163, 148), tail=(198, 200), w_head=3, w_tail=8, bow=5, steps=40)

    out = os.path.join(HERE, '01_礻.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
