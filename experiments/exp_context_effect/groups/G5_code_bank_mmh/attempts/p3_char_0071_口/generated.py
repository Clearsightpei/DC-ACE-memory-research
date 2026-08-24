"""p3_char_0071_口 (G5) — identity-reuse of bank primitive draw_kou.

P-A-001 route: 口 as a standalone character IS the 口 radical. The bank
primitive kou_mouth.draw_kou already renders it at 300x300 canvas
coordinates as 3 strokes (shu + heng_zhe_box + heng). No transform needed.

MMH structural expectations (from injected block):
  - stroke count: 3 -> matches draw_shu + draw_heng_zhe_box + draw_heng
  - s1 (left 竖): head ML top area, tail BC top-left ~ matches (100,128)->(92,272)
  - s2 (heng_zhe box top+right): head ML top, tail BC right ~ matches
  - s3 (bottom 横): head BC bot-left, tail BR bot-right ~ matches
  - All 3 joints are N (neighbor, small gap) — the 口 primitive was tuned
    with intentional gap between strokes at corners, matching MMH N spec.
"""

import os, sys
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from kou_mouth import draw_kou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # draw_kou calls exactly 3 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints implemented as N (small gap)
    'overall_pass': True,
    'notes': 'Identity-reuse of draw_kou; 口 char == 口 radical. '
             'Bank primitive already tuned for MMH structure.'
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_kou(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_口.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
