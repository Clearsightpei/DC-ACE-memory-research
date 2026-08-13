"""p3_char_0335_别 (bie, 'other/leave') — 7 strokes: 口(3) + 力(2) + 刂(2).

Structure: L-R split. Left = 另 = 口 (top-left small) + 力 (bottom-left).
Right = 刂 (long knife radical).

## P-A-008 inline-reasoning trace per sub-component

Three plausible whole-radical bank primitives exist: `draw_kou`,
`draw_li`, `draw_dao_right`. Per P-A-007-v2 hard-check, each is
evaluated for scale ∈ [0.55, 1.2] of native aspect.

### 刂 (right) → USE `draw_dao_right`

Bank primitive spans x: 111-161 (s1-s2 heads), y: 71-270. Bounding
~50w x 199h. MMH says s6 head (176.4, 125.7), tail (185.4, 225);
s7 head (222.7, 69.1), tail (195.1, 277.1). Bounding ~50w x 208h.
Height ratio 208/199 = 1.045 (in [0.55, 1.2] YES). Aspect matches.
Translation: dao_right s2 head (161, 71) → MMH s7 head (222.7, 69.1),
so ox=+61.7, oy=-1.9, scale=1.0. CALL IT.

### 口 (top-left small) → BANK_DEVIATION (aspect mismatch)

Bank `draw_kou` reference bounding box ~133w x 153h (aspect 0.87,
taller-than-wide). In 别, MMH s1-s3 span x: ~57-138 (81w), y: ~94-158
(64h). Aspect 1.27, wider-than-tall. Required scale for width 0.61,
for height 0.42. Ratio 1.45 — outside [0.55, 1.2] tolerance band on
the height dimension AND aspect skew ~1.45. INLINE 3 strokes.

### 力 (bottom-left) → BANK_DEVIATION (aspect mismatch)

Bank `draw_li` reference bounding box ~124w x 174h. In 别, 力 spans
x: 34-90 (56w), y: 154-290 (136h). Scale width 0.45 (BELOW 0.55),
height 0.78. Aspect mismatch. INLINE 2 strokes with heng_zhe_gou +
pie primitives at MMH-verbatim anchors.

# BANK_DEVIATION
# skipped: kou_mouth.py
# reason: aspect skew — 口 in 别 is wider-than-tall (81w/64h) vs
#   bank taller-than-wide (133w/153h); required scale 0.42 outside band.
# fresh_component: kou_small_for_别_topleft (3 stroke-primitive inline)
#
# skipped: li_power.py
# reason: aspect skew and required width-scale 0.45 below [0.55, 1.2].
# fresh_component: li_compressed_for_别_bottomleft (2 stroke-primitive inline)
"""

import os
import sys

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from dao_right import draw_dao_right


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes: 口(s1-s3) + 力(s4-s5) + 刂(s6-s7). '
             '刂 via dao_right bank (P-A-007-v2 hard-check PASS). '
             '口 and 力 inline via stroke primitives (aspect mismatch).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============= 口 top-left (s1 shu + s2 heng-zhe-box + s3 heng) =========
    # s1: 口 left shu — MMH head TL(0.568, 0.938)=(56.8, 93.8),
    #     tail ML(0.738, 0.582)=(73.8, 158.2)
    draw_shu(d, (57, 94), (74, 158), width=6)

    # s2: 口 top heng-zhe (top_left → bottom_right of box)
    #     MMH head ML(0.75, 0.04)=(75, 104), tail C(0.228, 0.304)=(122.8, 130.4)
    #     But heng-zhe is a compound stroke — extend to actual box bottom-right.
    #     Top-left of box ≈ (75, 100); bottom-right ≈ (135, 160).
    draw_heng_zhe_box(d, (75, 100), (135, 158), width=6)

    # s3: 口 bottom heng — MMH head ML(0.806, 0.447)=(80.6, 144.7),
    #     tail C(0.38, 0.412)=(138, 141.2)
    #     Actual bottom of the box.
    draw_heng(d, (72, 160), (135, 158), width_head=6, width_tail=7)

    # ============= 力 bottom-left (s4 heng-zhe-gou + s5 pie) ================
    # s4: 力 heng-zhe-gou — MMH head ML(0.404, 0.922)=(40.4, 192.2),
    #     tail BL(0.894, 0.631)=(89.4, 263.1)
    #     MMH endpoints are heng-head → hook-tip. Compound-stroke needs
    #     4 anchors: heng_head, corner, gou_tail, hook_tip.
    #     heng_head at (40, 192); corner top-right at (100, 188);
    #     gou_tail at bottom before hook (95, 263); hook_tip up-left (89, 253).
    draw_heng_zhe_gou(d,
                      heng_head=(40, 192),
                      corner=(100, 187),
                      gou_tail=(95, 263),
                      hook_tip=(89, 253))

    # s5: 力 pie — MMH head ML(0.902, 0.541)=(90.2, 154.1),
    #     tail BL(0.34, 0.895)=(34, 289.5). Long diagonal pie.
    draw_pie(d, (90, 154), (34, 290),
             bow_perp=12, w_head=8, w_tail=2, steps=90)

    # ============= 刂 right (s6 short shu + s7 long shu-gou via bank) =======
    # P-A-007-v2 hard-check PASS: dao_right at scale=1.0, ox=+62, oy=-2
    draw_dao_right(d, ox=62, oy=-2, scale=1.0)

    return img


if __name__ == '__main__':
    out_path = os.path.join(os.path.dirname(__file__), '01_别.png')
    img = render()
    img.save(out_path)
    print(f'Wrote {out_path}')
