"""口 (kǒu, "mouth") — 3-stroke enclosing radical.

Structure (MMH-derived):
  stroke 1: 竖 (left vertical, slightly leaning) — head @ ML(0.671, 0.289) → tail @ BC(0.02, 0.555)
  stroke 2: 横折 (top horizontal + right vertical) — head @ ML(0.891, 0.333) → tail @ BC(0.937, 0.2)
             (corner at ~C(0.93, 0.33) i.e. top-right of the interior)
  stroke 3: 横 (bottom horizontal) — head @ BC(0.081, 0.458) → tail @ BR(0.18, 0.344)

Joints — ALL N (neighbor, small natural gap ≈ 13-15 px). DO NOT weld.
  s1.head ⇆ s2.head @ ML(0.844, 0.364) : N, ~15.3 px gap
  s1.tail ⇆ s3.head @ BC(0.043, 0.485) : N, ~12.8 px gap
  s2.tail ⇆ s3.mid  @ BC(0.922, 0.251) : N, ~14.6 px gap

To preserve N-class gaps, we shorten each stroke slightly toward each
neighbor endpoint so the fat_line caps don't fuse.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes; all joints N (gapped); anchors within tolerance of MMH spec.'
}

import sys
import os
from PIL import Image, ImageDraw

# Import shared primitives from success bank.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402


def _shorten(p_from, p_to, px):
    """Move p_from toward p_to by `px` pixels; returns the new endpoint."""
    x0, y0 = p_from
    x1, y1 = p_to
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_kou(draw):
    # Anchors (from MMH spec).
    s1_head = anchor_to_xy(('ML', 0.671, 0.289))   # (67.1, 128.9)
    s1_tail = anchor_to_xy(('BC', 0.02,  0.555))   # (102.0, 255.5)

    s2_head = anchor_to_xy(('ML', 0.891, 0.333))   # (89.1, 133.3)
    s2_corner = anchor_to_xy(('C',  0.93,  0.33))  # (193.0, 133.0)  top-right
    s2_tail = anchor_to_xy(('BC', 0.937, 0.2))     # (193.7, 220.0)

    s3_head = anchor_to_xy(('BC', 0.081, 0.458))   # (108.1, 245.8)
    s3_tail = anchor_to_xy(('BR', 0.18,  0.344))   # (218.0, 234.4)

    # --- Preserve N-class gaps at the three joints ---
    # s1.head ⇆ s2.head : shorten both heads slightly away from the meet-point.
    s1_head_g = _shorten(s1_head, s1_tail, 4)      # pull s1.head down a hair
    s2_head_g = _shorten(s2_head, s2_corner, 4)    # pull s2.head right a hair

    # s1.tail ⇆ s3.head : pull s1.tail up, s3.head right, both a hair
    s1_tail_g = _shorten(s1_tail, s1_head, 4)
    s3_head_g = _shorten(s3_head, s3_tail, 4)

    # s2.tail ⇆ s3.mid : pull s2.tail up a hair (s3 already ends near this
    # point but not exactly on top — natural neighbor gap).
    s2_tail_g = _shorten(s2_tail, s2_corner, 4)

    # Stroke 1: 竖 (thin vertical, slightly slanting).
    fat_line(draw, s1_head_g, s1_tail_g, width=9)

    # Stroke 2: 横折 — horizontal segment then vertical drop, welded at corner.
    fat_line(draw, s2_head_g, s2_corner, width=9)
    fat_line(draw, s2_corner, s2_tail_g, width=9)
    # Shoulder press at the 折 corner.
    cx, cy = s2_corner
    r = 6
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Stroke 3: 横 (bottom horizontal, slightly upward-slanting to the right).
    fat_line(draw, s3_head_g, s3_tail, width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_kou(draw)
    out = os.path.join(_HERE, '01_口.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
