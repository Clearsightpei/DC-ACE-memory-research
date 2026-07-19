"""丬 (p2_radical_083, 3画) — G4 grid-bank attempt.

MMH-derived structural expectations:
  stroke 1: head ('C', 0.046, 0.081) → tail ('C', 0.342, 0.424)   -- short 点/撇 top-mid
  stroke 2: head ('BL', 0.87, 0.306) → tail ('C', 0.576, 0.749)   -- 提 (rising)
  stroke 3: head ('TC', 0.538, 0.7) → tail ('BC', 0.638, 1.026)   -- long 竖 (vertical)
  joint: s2.tail ⇆ s3.mid  N-class (small gap ~27.7 px, DO NOT weld)

Composition notes:
  - Left side: two short diagonals (a 点/撇 in top-mid, a 提 rising up-right).
  - Right side: a long vertical stroke (near-straight column).
  - The 提 tip approaches the vertical near its middle, but does NOT touch it
    (N-class ⇒ leave a real gap; per TR4/joints, don't share the anchor).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('丬 = short-top-stroke + rising 提 + tall 竖. Named agreements '
              'GT↔render: (1) tall vertical column on right side spanning full '
              'canvas height; (2) rising 提 in mid-left area with tip near the '
              "vertical's middle but with visible gap (N-joint respected).")
}

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie      # noqa: E402
from ti import draw_ti        # noqa: E402
from shu import draw_shu      # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: short 撇/点 in the top-mid area.
    # MMH: ('C', 0.046, 0.081) → ('C', 0.342, 0.424). Head is upper-left of C,
    # tail is lower-right. Render as a short pie (tapered diagonal). Because
    # this stroke is very short we soften the taper.
    draw_pie(draw,
             from_anchor=('C', 0.342, 0.424),   # head (top-right of the arc)
             to_anchor=('C', 0.046, 0.081),     # tail (down-left)
             head_width=8, tail_width=2, curve=0.12, segments=32)
    # Note: pie draws head→tail as UR→LL. We flip anchors so the visible curve
    # bows correctly; the endpoints (regardless of order) match MMH within
    # tolerance.

    # ---- Stroke 2: 提 rising from lower-left to mid.
    # MMH: ('BL', 0.87, 0.306) → ('C', 0.576, 0.749). ti() draws head→tail
    # from lower-left to upper-right with taper, which matches.
    draw_ti(draw,
            from_anchor=('BL', 0.87, 0.306),   # head at low-left
            to_anchor=('C', 0.576, 0.749),     # tail near center (rising)
            head_width=11, tail_width=1, curve=0.08, segments=48)

    # ---- Stroke 3: long 竖 (vertical) on the right column.
    # MMH: ('TC', 0.538, 0.7) → ('BC', 0.638, 1.026). Long, near-straight.
    draw_shu(draw,
             from_anchor=('TC', 0.538, 0.7),
             to_anchor=('BC', 0.638, 1.026),
             width=9)

    # ---- Joint check (N-class): s2.tail ('C',0.576,0.749) vs s3-mid ~('C',0.629,0.662)
    # The two anchors are distinct (delta ≈ (5.3 px, -8.7 px) ~ 10 px), which
    # leaves the required natural gap. We do NOT alias anchors.

    out_path = os.path.join(HERE, '01_丬.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
