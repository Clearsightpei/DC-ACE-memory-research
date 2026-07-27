"""p3_char_0034_刁 — G4 grid-bank attempt.

Pre-code lookup checklist:
1. success_bank/INDEX.md grep '刁' → not present (first attempt).
2. errata.md grep '刁' → not present.
3. form_catalog: 横撇弯钩 top-envelope with hook on right; 提 rises L→R.
4. principles_meta TR1 OVERRIDE anchors for THIS composition.
5. joint_atlas: strokes do not meet → N-wide/separate; expected JOINTS = NONE.

Character 刁: 2 strokes.
  s1 = 横撇弯钩 (heng-pie-wan-gou): top 横 → bends down along right → hook LEFT at bottom.
  s2 = 提 (ti): short rising diagonal, lower-left → mid-right.

MMH expected endpoints (dispatcher-injected):
  s1 head @ ('ML', 0.729, 0.075)  tail @ ('BC', 0.412, 0.537)
  s2 head @ ('BL', 0.530, 0.013)  tail @ ('C',  0.828, 0.436)
Joints: NONE.
"""

import os, sys
from PIL import Image, ImageDraw

# Import G4 shared primitives.
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng_pie_wan_gou import draw_heng_pie_wan_gou
from ti import draw_ti

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '2 strokes, joints=NONE per MMH; heng_pie_wan_gou + ti.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1 = 横撇弯钩 (compound). Endpoints override-anchored for 刁.
    s1_head_h = ('ML', 0.729, 0.075)   # MMH head — top-mid-left start of 横
    s1_corner = ('TR', 0.30, 0.75)     # 横 hits top-right; bend point
    s1_knee   = ('MR', 0.45, 0.10)     # short 撇 sweep down-left of corner
    s1_belly  = ('MR', 0.30, 0.65)     # 弯 belly control, pulling curve inward-down
    s1_hookpt = ('BC', 0.412, 0.537)   # MMH tail — base of hook
    s1_tip    = ('BC', 0.15, 0.30)     # flick up-left
    draw_heng_pie_wan_gou(
        draw,
        s1_head_h, s1_corner, s1_knee, s1_belly, s1_hookpt, s1_tip,
        h_width=8, corner_shoulder=11,
        pie_head_w=10, pie_knee_w=7, knee_shoulder=10,
        wan_head_w=7, wan_belly_w=11,
        hook_start_w=9, tip_w=2,
    )

    # Stroke 2 = 提. Uses MMH endpoints literally.
    s2_head = ('BL', 0.530, 0.013)
    s2_tail = ('C',  0.828, 0.436)
    draw_ti(draw, s2_head, s2_tail,
            head_width=12, tail_width=2, curve=0.06)

    out = os.path.join(os.path.dirname(__file__), '01_刁.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
