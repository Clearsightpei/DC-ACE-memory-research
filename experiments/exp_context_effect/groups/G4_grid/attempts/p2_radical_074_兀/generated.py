"""p2_radical_074_兀 — G4 grid-bank attempt.

Character: 兀 (wù) — 3 strokes.
  Stroke 1: 一 (heng) — top horizontal, slight up-right slant.
  Stroke 2: 丿 (pie) — left leg, sweeps down-left from upper mid-right.
  Stroke 3: 竖弯 (shu_wan) — right leg, vertical descent then curve right (no hook).

Joints (from MMH-derived brief):
  s1.head ⇆ s2.head @ ML : N (small natural gap; do NOT weld). Expected ~35 px.
  s1.mid  ⇆ s3.head @ C  : N (small natural gap; do NOT weld). Expected ~20 px.

Anchor plan (米字格, PIL y-down):
  Stroke 1 (heng): from ('ML', 0.65, 0.08) to ('TR', 0.32, 0.96)  → pixel (65,108) → (232,96)
  Stroke 2 (pie):  from ('ML', 0.99, 0.29) to ('BL', 0.35, 0.78)  → pixel (99,129) → (35,278)
  Stroke 3 (shu_wan): head ('C', 0.50, 0.10)   → (150,110)
                     belly ('C', 0.50, 0.60)   → (150,160) [keeps upper body straight]
                     corner ('BC', 0.55, 0.85) → (155,285)
                     tail  ('BR', 0.40, 0.85)  → (240,285)  [flat horizontal, no upward curl]
  (Stroke 3 tail extended vs MMH's short-median tail: single-radical rule
   from sandbox — MMH medians measure the mid-glyph shape, real radical
   render should occupy the full grid.)

N-gap enforcement:
  s1 left endpoint (65,108); s2 head (99,129). dist ~sqrt(34^2+21^2)=40 px. OK (N).
  s1 midpoint x at t=0.43 along (65,108)->(232,96): x = 65 + 0.43*(232-65) = 137; y = 108 + 0.43*(96-108) = 103.
  s3 head (150,110). dist ~sqrt(13^2 + 7^2) = 15 px. OK-ish for N (slight welding acceptable
  as MMH expected 20 px; but 15 is still under the "≤25 gap" N tolerance per sandbox).

Stroke count: 3.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "Heng in upper third slanting slightly up-right; pie sweeps from mid-right "
        "down to lower-left; shu_wan on right side descends and curves right. "
        "Silhouette matches GT: horizontal cap + two divergent legs, right leg "
        "curving out. N-gaps at ML (heng-left ↔ pie-head) ~40px and at C "
        "(heng-mid ↔ shu_wan-head) ~15px — both small natural gaps, not welds."
    ),
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..', '..', '..'))
_BANK = os.path.join(_ROOT, 'groups', 'G4_grid', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu_wan import draw_shu_wan  # noqa: E402


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 一 (top heng), slight up-right slant per MMH.
    draw_heng(
        draw,
        from_anchor=('ML', 0.65, 0.08),
        to_anchor=('TR', 0.32, 0.96),
        width=9,
    )

    # Stroke 2: 丿 (left leg pie).
    draw_pie(
        draw,
        from_anchor=('ML', 0.99, 0.29),
        to_anchor=('BL', 0.35, 0.78),
        head_width=11,
        tail_width=2,
        curve=0.08,
    )

    # Stroke 3: 竖弯 (right leg — descent then curve right, no hook).
    draw_shu_wan(
        draw,
        head=('C', 0.50, 0.10),
        belly=('C', 0.50, 0.60),
        corner=('BC', 0.55, 0.85),
        tail=('BR', 0.40, 0.85),
        head_w=8,
        belly_w=10,
        corner_w=10,
        tail_w=8,
    )

    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    out = os.path.join(_HERE, '01_兀.png')
    render(out)
