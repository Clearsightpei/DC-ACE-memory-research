"""p3_char_0092_廾 — G4 attempt.

Memory lookup checklist:
  1. success_bank/INDEX.md grep '廾' → row 78: p2_radical_051_廾 → gong_join.py.
     Reuse draw_gong_join, OVERRIDE anchors per TR1 with the MMH-derived
     anchors from this brief.
  2. errata.md grep '廾' → not in errata (only referenced as a pattern
     example for 艹). No fix idea to follow.
  3. form_catalog / joint_atlas: 廾 has two P joints (s2 crosses s1;
     s3 crosses s1). Both are welded by construction — s2/s3 both start
     above the heng-line and end below it.

Stroke plan (MMH brief, verbatim):
  s1 横 head ('ML', 0.349, 0.86)  tail ('MR', 0.625, 0.86)
  s2 撇 head ('C',  0.014, 0.485) tail ('BL', 0.633, 0.596)
  s3 竖 head ('C',  0.749, 0.377) tail ('BC', 0.863, 0.719)

Joints (both P — welded):
  s1.mid ⇆ s2.mid @ C  (left crossing)
  s1.mid ⇆ s3.mid @ C  (right crossing)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused draw_gong_join from success bank (gong_join.py) with MMH-brief anchors overriding defaults per TR1. Both joints are P by construction because s2 and s3 anchors span across s1 y-line (heng at ML/MR y_frac=0.86 which puts it slightly below the ML/MR band midline, and both s2/s3 tails sit in BL/BC — welding is automatic).',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from gong_join import draw_gong_join

# MMH-brief anchors (override defaults per TR1)
S1_HEAD = ('ML', 0.349, 0.86)
S1_TAIL = ('MR', 0.625, 0.86)
S2_HEAD = ('C',  0.014, 0.485)
S2_TAIL = ('BL', 0.633, 0.596)
S3_HEAD = ('C',  0.749, 0.377)
S3_TAIL = ('BC', 0.863, 0.719)

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

draw_gong_join(draw,
               s1_head=S1_HEAD, s1_tail=S1_TAIL,
               s2_head=S2_HEAD, s2_tail=S2_TAIL,
               s3_head=S3_HEAD, s3_tail=S3_TAIL)

out = os.path.join(os.path.dirname(__file__), '01_廾.png')
img.save(out)
print('wrote', out)
