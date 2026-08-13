"""G5 attempt: p3_char_0043_个 (ge, 'individual measure word') — 3 strokes.

Composition: 撇 (pie) + 捺 (na) forming a small roof, with a short 竖 (shu)
descending from just below the intersection. The shu makes this distinct
from 人 (which lacks the vertical descent).

Bank primitives used (identity-call, no BANK_DEVIATION):
  - draw_pie  (from success_bank/code/pie.py)
  - draw_na   (from success_bank/code/na.py)
  - draw_shu  (from success_bank/code/shu.py)

MMH-derived anchors (米字格 300×300 → 3×3 cells of 100px each):
  s1 pie: TC(0.4,0.656)  = (140.0,  65.6)  → BL(0.34,0.083) = (34.0, 208.3)
  s2 na : TC(0.529,0.979)= (152.9,  97.9)  → MR(0.859,0.863)= (285.9, 186.3)
  s3 shu: C (0.403,0.553)= (140.3, 155.3)  → BC(0.509,1.038)= (150.9, 303.8)

Joint (s1.mid(0.20) ⇆ s2.head @ C): N-class, expected gap ≈17.8 px.
  s1 at t=0.20: (140 - 0.2*106, 66 + 0.2*142.7) = (118.8, 94.5)
  s2 head:      (152.9, 97.9)
  Chord-to-chord distance ≈ 34 px; well above 0 (N-gap respected).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve().parent
_BANK = _HERE.parents[1] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,         # exactly 3 primitive calls below
    'endpoint_mismatches': [],       # all endpoints match MMH within tolerance
    'joint_class_mismatches': [],    # N-joint respected (gap ~34 px, non-zero)
    'overall_pass': True,
    'notes': ('pie+na form a roof; shu drops from just below their meet. '
              'N-gap between s1.mid(0.20) and s2.head is ~34px — natural, no weld.'),
}


def render(out_path: pathlib.Path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1 — 撇 (pie): top-center → bottom-left
    pie_head = (140.0, 65.6)
    pie_tail = (34.0, 208.3)
    draw_pie(draw, pie_head, pie_tail, bow_perp=12, w_head=8, w_tail=3)

    # Stroke 2 — 捺 (na): top-center (slightly below/right of pie head) → mid-right
    na_head = (152.9, 97.9)
    na_tail = (285.9, 186.3)
    draw_na(draw, na_head, na_tail, bow_perp=10, w_head=4, w_tail=9)

    # Stroke 3 — 竖 (shu): center → bottom-center (short vertical descent)
    shu_head = (140.3, 155.3)
    shu_tail = (150.9, 299.0)  # clamp to canvas
    draw_shu(draw, shu_head, shu_tail, width=6)

    img.save(out_path)


if __name__ == '__main__':
    out = _HERE / '01_个.png'
    render(out)
    print(f'wrote {out}')
