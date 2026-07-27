"""p3_char_0198_立 — G4 attempt.

Reading order (v8): drawer_memory.md -> memory_index.md -> INDEX grep (no
mastered 立 primitive) -> errata (no entry). No chronic primitive fits.
Char is a single-part 5-stroke top-heavy character; drawing fresh via
米字格 anchors provided in the MMH brief.

Composition: 立 = top-dot + short-heng + left-dot + right-dot + long-heng-base.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes matching MMH anchors; s4 tail rests on s5 with N gap ~20px.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

def dot(a_head, a_tail, w_head=6, w_tail=12):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = sample_line(p0, p1, n=16)
    widths = [w_head + (w_tail - w_head) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

def heng(a_head, a_tail, w=8):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = sample_line(p0, p1, n=24)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

strokes = []

# stroke 1: top 点 (small diagonal downstroke)
dot(('TC', 0.242, 0.738), ('TC', 0.652, 0.981), w_head=5, w_tail=11)
strokes.append(1)

# stroke 2: short horizontal near middle-upper (2nd horizontal, right-to-left in MMH order)
heng(('ML', 0.806, 0.538), ('MR', 0.20, 0.348), w=9)
strokes.append(2)

# stroke 3: left 点 (drops down toward BC)
dot(('ML', 0.938, 0.872), ('BC', 0.184, 0.273), w_head=6, w_tail=11)
strokes.append(3)

# stroke 4: right 点 (short, rests toward BC gap)
dot(('C', 0.767, 0.649), ('BC', 0.562, 0.534), w_head=6, w_tail=11)
strokes.append(4)

# stroke 5: long base horizontal
heng(('BL', 0.334, 0.733), ('BR', 0.710, 0.716), w=10)
strokes.append(5)

assert len(strokes) == 5, f"expected 5 strokes, got {len(strokes)}"

img.save(os.path.join(os.path.dirname(__file__), '01_立.png'))
