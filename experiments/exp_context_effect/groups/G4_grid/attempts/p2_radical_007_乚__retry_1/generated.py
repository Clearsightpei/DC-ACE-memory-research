"""p2_radical_007_乚 — G4 grid-bank render — RETRY #1.

Target: 乚 (1画部首) — a single compound stroke: 竖弯 (shù wān) with a
small UPWARD TICK at the tail.

Errata fix (from groups/G4_grid/errata.md, 2nd entry for this item):
  Prior attempt (retry 0) used draw_shu_wan (no hook) — tail
  terminated ABRUPT/FLAT at mid-right. GT clearly shows a small
  upward tick at the tail terminus. Fix: use draw_shu_wan_gou with a
  short up-tick tip so the ending reads intentional, not truncated.

MMH-expected stroke count: 1
  stroke 1: head @ ('TL', 0.636, 0.867)  tail @ ('BR', 0.552, 0.124)
  joints: NONE (single compound stroke, no meeting).

Pixel translations (300x300, PIL y grows DOWN):
  head  ('TL', 0.636, 0.867) -> (63.6,  86.7)   — top of vertical
  tail  ('BR', 0.552, 0.124) -> (255.2, 212.4)  — TIP of upward tick

Since MMH's endpoint tuple gives (head_of_stroke, tail_of_stroke),
and this stroke ends with an upward tick, the MMH "tail" == the tip
of that tick. So I map tail directly to `tip` in draw_shu_wan_gou,
and place hook_pt (the base of the tick) DIRECTLY BELOW tip at the
end of the horizontal sweep:

  belly    = ('ML', 0.65, 0.90)  ~ (65, 190)  — Bezier control on
             vertical column, keeps upper body straight
  corner   = ('BL', 0.75, 0.30)  ~ (75, 230)  — bend point, bottom-left
  hook_pt  = ('BR', 0.55, 0.30)  ~ (255, 230) — base of tick, right end
             of horizontal sweep (same y as corner for level bottom)
  tip      = ('BR', 0.552, 0.124) ~ (255.2, 212.4) — MMH tail, tick tip

Bank use: draw_shu_wan_gou (batch2 stroke23 pass). Anchors overridden
for THIS composition (not primitive defaults).
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 1 primitive call -> 1 compound stroke
    'endpoint_mismatches': [],    # head=TL(0.636,0.867) matches;
                                  # tail (=tip) = BR(0.552,0.124) matches MMH exactly
    'joint_class_mismatches': [], # no joints declared for 乚
    'overall_pass': True,
    'notes': 'shu_wan_gou primitive with tick. head=MMH head, tip=MMH tail. '
             'Fix applied per errata: added upward tick so tail is not '
             'abrupt/flat. Base of tick placed at BR(0.55,0.30), tick '
             'rises ~18 px to tip at BR(0.552,0.124).',
}

import os
import sys
from PIL import Image, ImageDraw

# Import the shared primitives (success_bank/code/).
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 乚 = single 竖弯(钩) compound stroke.
    #   head    top of vertical, TL cell near bottom (matches MMH head)
    #   belly   control on vertical column, keeps upper body straight
    #   corner  bend at bottom-left
    #   hook_pt base of upward tick (right end of horizontal sweep)
    #   tip     upward tick terminus (matches MMH tail exactly)
    draw_shu_wan_gou(
        draw,
        head=('TL',   0.636, 0.867),
        belly=('ML',  0.65,  0.90),
        corner=('BL', 0.75,  0.30),
        hook_pt=('BR', 0.55, 0.30),
        tip=('BR',    0.552, 0.124),
        head_w=8, belly_w=11, corner_w=11,
        hook_start_w=9, tip_w=2,
    )

    out = os.path.join(os.path.dirname(__file__), '01_乚.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
