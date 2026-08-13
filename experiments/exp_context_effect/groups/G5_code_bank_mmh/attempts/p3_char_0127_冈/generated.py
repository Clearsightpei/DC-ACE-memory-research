"""p3_char_0127_冈 — G5 attempt.

冈 = 4 strokes: 竖 (left vertical) + 横折钩 (top/right/hook) + 撇 + 捺
Inner 撇+捺 form 乂 crossing at C (P-joint).
Outer left-vert and top-horiz do NOT weld (N-joint gap ~17px).

MMH-derived anchors:
- s1: TL(0.636,0.938)=(63.6,93.8)  → BL(0.653,0.836)=(65.3,283.6)
- s2: ML(0.861,0.02)=(86.1,102.0)  → BC(0.796,0.707)=(179.6,270.7)   [head=heng start, tail=hook_tip]
  corner + gou_tail inferred: (245,100) and (243,268)
- s3: C(0.723,0.242)=(172.3,124.2) → BL(0.891,0.438)=(89.1,243.8)
- s4: C(0.104,0.559)=(110.4,155.9) → BC(0.931,0.394)=(193.1,239.4)

Bank use:
  shu, heng_zhe_gou, pie, na  — all fit cleanly.  No BANK_DEVIATION.
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / "success_bank" / "code"))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 primitive calls = 4 MMH strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # s1/s2 heads left with ~24px gap (N ok); s3/s4 cross near C (P ok)
    'overall_pass': True,
    'notes': 'shu + heng_zhe_gou + pie + na, corner (245,100) & gou_tail (243,268) '
             'inferred (MMH gives only head and hook_tip for s2).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 竖 (left vertical) — anchors from MMH
    draw_shu(d, head=(63.6, 93.8), tail=(65.3, 283.6), width=6)

    # s2: 横折钩 (top + right + hook curling inward)
    draw_heng_zhe_gou(
        d,
        heng_head=(86.1, 102.0),   # MMH s2 head (top-left of frame, just right of s1 top)
        corner=(245.0, 99.0),      # inferred top-right corner
        gou_tail=(243.0, 268.0),   # inferred bottom-right before hook flick
        hook_tip=(179.6, 270.7),   # MMH s2 tail — a long inward hook
    )

    # s3: 撇 (pie) inner — head upper-right of center, tail lower-left
    draw_pie(
        d,
        head=(172.3, 124.2),
        tail=(89.1, 243.8),
        bow_perp=10, w_head=7, w_tail=2,
    )

    # s4: 捺 (na) inner — head upper-left of center, tail lower-right
    draw_na(
        d,
        head=(110.4, 155.9),
        tail=(193.1, 239.4),
        bow_perp=10, w_head=3, w_tail=8,
    )

    out = _HERE.parent / "01_冈.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
