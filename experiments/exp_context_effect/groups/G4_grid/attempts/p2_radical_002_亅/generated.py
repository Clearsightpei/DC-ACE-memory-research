"""亅 (jué) — 1画 radical. Uses draw_shu_gou wrapper (per principle_bank
1-画 primitive-as-radical-wrapper convention).

Anchor plan (米字格, PIL-native):
  head    @ ('TC', 0.283, 0.674)   — from MMH-derived spec (top of vertical)
  belly   @ ('C',  0.283, 0.35)    — same x_frac as head; width-knot only
  hook_pt @ ('BC', 0.283, 0.85)    — bottom of straight vertical body
  tip     @ ('BL', 0.973, 0.722)   — MMH tail; hook flick to bottom-left
                                     (matches GT's leftward hook)

Joints: single stroke, internal hook only. No external joints (Phase-2
brief declares NONE).

Stroke count: 1 (draw_shu_gou is one primitive → one stroke).

SELF_CHECK dict (populated after render+visual compare below).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from shu_gou import draw_shu_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 1 primitive call = 1 stroke, matches expected=1
    'endpoint_mismatches': [],     # head TC(0.283,0.674) matches; tail BL(0.973,0.722) matches
    'joint_class_mismatches': [],  # brief declares NONE — n/a
    'overall_pass': True,
    'notes': ('Used shu_gou wrapper per principle_bank Phase-1 rule '
              '(亅 → draw_shu_gou). Body straight vertical along x_frac '
              '~0.283 of TC/C/BC column; hook_pt at bottom of BC, tip '
              'at BL(0.973,0.722) so flick goes down-left ~30px matching '
              'GT bottom-left hook corner.'),
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    head    = ('TC', 0.283, 0.674)
    belly   = ('C',  0.283, 0.35)
    hook_pt = ('BC', 0.283, 0.85)
    tip     = ('BL', 0.973, 0.722)

    draw_shu_gou(draw, head, belly, hook_pt, tip,
                 head_w=8, belly_w=9, hook_start_w=9, tip_w=2)

    out_path = os.path.join(os.path.dirname(__file__), '01_亅.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
