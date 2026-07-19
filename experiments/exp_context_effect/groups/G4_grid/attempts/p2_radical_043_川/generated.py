"""川 (chuān) — Phase-2 radical 043. 3 strokes: 撇 + 竖 (short) + 竖 (tall).

Compositional plan:
  stroke 1: 撇 (curved sweep) from upper-mid to lower-left.
    head ('ML', 0.727, 0.102), tail ('BL', 0.352, 0.771)
  stroke 2: 竖 (shorter, middle) — starts below the top row.
    head ('C', 0.386, 0.204), tail ('BC', 0.456, 0.508)
  stroke 3: 竖 (tallest, right) — starts from top row, extends to bottom.
    head ('TC', 0.995, 0.727) ≈ TR left edge, tail ('BR', 0.13, 1.047) ≈ BR bottom.

Joints: NONE. All three strokes are clearly separated.

Bank usage: draw_pie for stroke 1, draw_shu for strokes 2 & 3. Per TR1,
we override every default anchor.
"""
import os
import sys

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Three separate strokes (P + Sh + Sh). Pie curves left; two shu strokes vertical, right one taller.'
}

# Import bank primitives.
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw  # noqa: E402
from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 撇 — curved sweep from upper-middle down to lower-left.
    # Slight extra curve to match GT's leftward-bowing 撇.
    draw_pie(
        draw,
        from_anchor=('ML', 0.727, 0.102),   # head, upper mid-left area
        to_anchor=('BL', 0.352, 0.771),     # tail, lower-left
        head_width=12, tail_width=2, curve=0.14, segments=48,
    )

    # Stroke 2: 竖 (short middle vertical). Slightly bolder than pilot.
    draw_shu(
        draw,
        from_anchor=('C', 0.386, 0.204),    # head, mid area
        to_anchor=('BC', 0.456, 0.508),     # tail, into lower-mid
        width=10,
    )

    # Stroke 3: 竖 (tall right vertical). Clamp tail to canvas edge.
    draw_shu(
        draw,
        from_anchor=('TC', 0.995, 0.727),   # head, near top-right border area
        to_anchor=('BR', 0.13, 1.0),        # tail, bottom
        width=11,
    )

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_川.png')
    render(out)
    print(f'Wrote {out}')
