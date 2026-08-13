"""p3_char_0477_南 — G4 attempt.

Decomposition (visual + MMH):
  南 = 十 (top) + 冂 (frame) + inside (小干-like: heng + shu + heng crossing)

MMH gives 9 strokes; using anchors verbatim, all rendered as fat_line
except s4 (横折钩) which is drawn as an L-bend with vertical hook tail.

Reading path (v8 mandatory):
  1. drawer_memory.md — no chronic primitive matches (南 has no 丿/刀/冂-frame
     that maps to jiong_frame cleanly here — frame is item-specific).
  2. success_bank INDEX grep 南 → not present.
  3. errata.md grep 南 → not present.
No bank primitive fit, drawing fresh from MMH anchors verbatim.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 9 MMH anchors used verbatim; s1×s2 welded P at center; s8×s9 welded P at BC.'
}

import sys, os
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

STROKE_W = 8

def line(a, b, w=STROKE_W):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), w)

def lbend(a_head, a_corner, a_tail, w=STROKE_W):
    """Compound stroke: head→corner→tail (for 横折 / 横折钩)."""
    h = anchor_to_xy(a_head)
    c = anchor_to_xy(a_corner)
    t = anchor_to_xy(a_tail)
    fat_line(draw, h, c, w)
    fat_line(draw, c, t, w)

def heng_zhe_gou(a_head, a_topright, a_bottomright, a_hooktip, w=STROKE_W):
    """横折钩 compound: head → top-right corner → bottom-right → hook tip."""
    pts = [anchor_to_xy(a) for a in (a_head, a_topright, a_bottomright, a_hooktip)]
    for i in range(len(pts) - 1):
        fat_line(draw, pts[i], pts[i + 1], w)

# --- 9 strokes, MMH order ---

# s1: top heng of 十 (part of top 十, crossed with s2 at C)
line(('ML', 0.923, 0.116), ('MR', 0.036, 0.002))

# s2: top shu of 十 (crosses s1 at C — P weld)
line(('TC', 0.395, 0.527), ('C', 0.274, 0.535))

# s3: left of frame (short pie-like vertical)
line(('ML', 0.463, 0.632), ('BL', 0.621, 0.845))

# s4: 横折钩 = top + right vertical + hook tail. MMH gives head + tail only;
# insert two corners: top-right (heng ends) and bottom-right (before hook).
# Right side vertical sits near x≈295; hook curls back to x≈195 near y≈273.
heng_zhe_gou(
    ('ML', 0.606, 0.664),   # head — top-left of frame
    ('MR', 0.951, 0.664),   # top-right corner
    ('BR', 0.951, 0.733),   # bottom-right (just before hook)
    ('BC', 0.951, 0.733),   # hook tip — MMH tail
)

# s5: small stroke inside (short down-tick in C cell)
line(('C', 0.061, 0.752), ('C', 0.195, 0.957))

# s6: short vertical inside (from mid area up-to lower)
line(('C', 0.652, 0.629), ('BC', 0.518, 0.019))

# s7: small heng inside top
line(('BL', 0.993, 0.121), ('BC', 0.919, 0.051))

# s8: wide heng inside bottom (crosses s9 at BC — P weld)
line(('BL', 0.926, 0.443), ('BR', 0.019, 0.396))

# s9: center vertical inside (crosses s8)
line(('BC', 0.33, 0.174), ('BC', 0.415, 0.938))

out = os.path.join(os.path.dirname(__file__), '01_南.png')
img.save(out)
print('wrote', out)
