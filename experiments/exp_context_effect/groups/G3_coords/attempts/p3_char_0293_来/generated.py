# p3_char_0293_来 (lái) — 7 strokes
# Composition:
#   1. short top heng
#   2. left 丷-dot (small pie going outer-down)
#   3. right 丷-dot (small na going outer-down)
#   4. long middle heng
#   5. central shu (vertical from above top-heng to bottom)
#   6. long pie from middle-heng center to lower-left
#   7. long na  from middle-heng center to lower-right
# Reuses mu.py stroke primitives (bank REFERENCE, v8) since 来 lower
# half is essentially 木.

import os
import sys

sys.path.insert(0, '<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code')

from PIL import Image, ImageDraw
from mu import _inline_heng, _inline_shu, _inline_pie, _inline_na


def draw_lai(t, ox=0.0, oy=0.0, scale=1.0):
    s = scale
    # 1. Top short heng
    _inline_heng(t, ox + 0, oy + 92 * s, 30 * s, thickness=max(1, int(round(7 * s))))

    # 2. Left 丷-dot (small pie, upper-inner -> lower-outer)
    _inline_pie(
        t,
        x0=ox + (-8) * s, y0=oy + 78 * s,
        x1=ox + (-28) * s, y1=oy + 50 * s,
        w_head=6.0 * s, w_tail=1.5 * s, bow_perp=-2.0 * s,
    )

    # 3. Right 丷-dot (small na, upper-inner -> lower-outer)
    _inline_na(
        t,
        x0=ox + 8 * s, y0=oy + 78 * s,
        x1=ox + 28 * s, y1=oy + 50 * s,
        w_head=2.0 * s, w_belly=6.0 * s, w_tail=2.0 * s, bow_perp=2.0 * s,
    )

    # 4. Long middle heng
    _inline_heng(t, ox + 0, oy + 25 * s, 100 * s, thickness=max(1, int(round(7 * s))))

    # 5. Central shu — extends from above top heng down to bottom
    _inline_shu(t, ox + 0, oy + 0 * s, 118 * s, thickness=max(1, int(round(7 * s))))

    # 6. Bottom pie (long, from center of middle heng to lower-left) — thin per P12
    _inline_pie(
        t,
        x0=ox + 0, y0=oy + 25 * s,
        x1=ox + (-95) * s, y1=oy + (-115) * s,
        w_head=5.0 * s, w_tail=2.0 * s, bow_perp=-4.0 * s,
    )

    # 7. Bottom na  (long, from center of middle heng to lower-right) — thin per P12
    _inline_na(
        t,
        x0=ox + 0, y0=oy + 25 * s,
        x1=ox + 95 * s, y1=oy + (-115) * s,
        w_head=3.0 * s, w_belly=5.0 * s, w_tail=3.0 * s, bow_perp=4.0 * s,
    )


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    t = ImageDraw.Draw(img)
    draw_lai(t)
    out_path = os.path.join(os.path.dirname(__file__), '01_来.png')
    img.save(out_path)
    print(f'wrote {out_path}')
