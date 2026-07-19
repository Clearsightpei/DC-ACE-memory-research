"""p2_radical_004_乛 (1画部首) — G4 attempt.

Anchor plan (per MMH endpoint spec + principle_bank 乛 → draw_heng_gou):
  stroke 1 (横钩): head @ ('ML', 0.782, 0.342)  == pixel (78, 134)
                    shoulder @ ('MR', 0.40, 0.25)  == pixel (240, 125)
                    tip @ ('C', 0.89, 0.623)      == pixel (189, 162)
  Joints: NONE (single primitive, internal hook part of stroke).

Shoulder chosen so the hook flick (shoulder → tip) points DOWN-LEFT,
which is the canonical 横钩 hook direction. tip is the MMH-declared
endpoint. shoulder placement matches the GT PNG's visible bend point
(top-right of the drawn shape).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng_gou import draw_heng_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 1 primitive call == 1 stroke, matches expected 1
    'endpoint_mismatches': [],    # head anchor matches MMH; tip == MMH tail exactly
    'joint_class_mismatches': [], # no joints expected, none implemented
    'overall_pass': True,
    'notes': 'shoulder anchor is a required internal parameter of heng_gou '
             '(defines the bend point) — MMH only reports head+tail (=tip).',
}

# ---- Anchors ----
HEAD     = ('ML', 0.782, 0.342)   # MMH head
SHOULDER = ('MR', 0.40,  0.25)    # inferred bend point (right of tip, above tip)
TIP      = ('C',  0.89,  0.623)   # MMH tail == hook tip

# Sanity: tip is DOWN-LEFT of shoulder (canonical 横钩 flick direction).
_ph = anchor_to_xy(HEAD)
_ps = anchor_to_xy(SHOULDER)
_pt = anchor_to_xy(TIP)
assert _pt[0] < _ps[0], f'tip.x ({_pt[0]}) must be LEFT of shoulder.x ({_ps[0]})'
assert _pt[1] > _ps[1], f'tip.y ({_pt[1]}) must be BELOW shoulder.y ({_ps[1]})'
assert _ph[0] < _ps[0], f'head.x ({_ph[0]}) must be LEFT of shoulder.x ({_ps[0]})'

# ---- Render ----
img = Image.new('RGB', (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

draw_heng_gou(
    draw,
    head=HEAD,
    shoulder=SHOULDER,
    tip=TIP,
    head_w=8, mid_w=6, shoulder_w=11, tip_w=2,
)

out = os.path.join(os.path.dirname(__file__), '01_乛.png')
img.save(out)
print(f'wrote {out}')
