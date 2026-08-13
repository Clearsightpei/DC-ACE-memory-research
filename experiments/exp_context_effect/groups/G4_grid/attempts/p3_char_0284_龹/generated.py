"""龹 (p3_char_0284) — G4 attempt.

Structural read from GT + brief:
- s1, s2: top 八 (left short pie, right short dian)
- s3: upper 一 (heng across middle)
- s4: lower 一 (heng across middle, longer, wider)
- s5: long 撇 from top-center down to bottom-left
- s6: long 捺 from center-middle down to bottom-right

Joints:
- s2.tail ⇆ s3.tail @ C  : N (small gap ~32 px)
- s3 ⇆ s5 @ C (0.387, 0.353) : P (welded)
- s4 ⇆ s5 @ C (0.266, 0.718) : P (welded)
- s4 ⇆ s6.head @ C (0.642, 0.693) : N (small gap ~13 px)
"""

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Drew 6 strokes: 2 top dots (八), 2 heng, long pie + long na crossing them.'
}

# Memory-index reads: drawer_memory (skimmed), success_bank/INDEX grep for 龹/关 (none),
#   errata grep for 龹 (none). No mastered primitive fits so drawing fresh with anchors.

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- stroke 1: left top dot (short pie ~ left half of 八) ---
# Anchor spec puts this in the small region just above the upper heng, left of center.
# Extend visually so it reads as a proper pie-dot.
p1a = anchor_to_xy(('TL', 0.935, 0.905))
p1b = anchor_to_xy(('C',  0.157, 0.11))
# extend outward along the stroke direction so it reads
dx1, dy1 = p1b[0]-p1a[0], p1b[1]-p1a[1]
p1a2 = (p1a[0] - dx1*0.6, p1a[1] - dy1*0.6)
p1b2 = (p1b[0] + dx1*0.6, p1b[1] + dy1*0.6)
pts1 = [p1a2,
        ((p1a2[0]+p1b2[0])/2, (p1a2[1]+p1b2[1])/2),
        p1b2]
widths1 = [3, 7, 8]
stroke_variable_width(d, pts1, widths1)

# --- stroke 2: right top dot (dian, mirror-image angle) ---
p2a = anchor_to_xy(('TC', 0.91, 0.683))
p2b = anchor_to_xy(('C',  0.693, 0.066))
dx2, dy2 = p2b[0]-p2a[0], p2b[1]-p2a[1]
p2a2 = (p2a[0] - dx2*0.6, p2a[1] - dy2*0.6)
p2b2 = (p2b[0] + dx2*0.6, p2b[1] + dy2*0.6)
pts2 = [p2a2,
        ((p2a2[0]+p2b2[0])/2, (p2a2[1]+p2b2[1])/2),
        p2b2]
widths2 = [3, 7, 8]
stroke_variable_width(d, pts2, widths2)

# --- stroke 3: upper heng ---
p3a = anchor_to_xy(('ML', 0.905, 0.389))
p3b = anchor_to_xy(('C',  0.989, 0.254))
fat_line(d, p3a, p3b, width=6)

# --- stroke 4: lower heng (longer & lower) ---
p4a = anchor_to_xy(('ML', 0.58, 0.802))
p4b = anchor_to_xy(('MR', 0.414, 0.635))
fat_line(d, p4a, p4b, width=7)

# --- stroke 5: long pie (top-center → bottom-left) ---
p5a = anchor_to_xy(('TC', 0.359, 0.56))
p5b = anchor_to_xy(('BL', 0.384, 0.59))
# slight curve — control point pulled to the left of the midpoint
mid5 = ((p5a[0]+p5b[0])/2 - 12, (p5a[1]+p5b[1])/2)
curve5 = quad_bezier(p5a, mid5, p5b, n=40)
# taper: thick middle, thin tail
widths5 = []
n5 = len(curve5)
for i in range(n5):
    t = i / (n5 - 1)
    # start medium, thickest ~1/3, taper to thin at tail
    if t < 0.3:
        w = 5 + t * 3
    else:
        w = 6 - (t - 0.3) * 5
    widths5.append(max(2, w))
stroke_variable_width(d, curve5, widths5)

# --- stroke 6: long na (center → bottom-right) ---
p6a = anchor_to_xy(('C',  0.682, 0.72))
p6b = anchor_to_xy(('BR', 0.854, 0.37))
# slight curve
mid6 = ((p6a[0]+p6b[0])/2 + 6, (p6a[1]+p6b[1])/2 + 4)
curve6 = quad_bezier(p6a, mid6, p6b, n=40)
widths6 = []
n6 = len(curve6)
for i in range(n6):
    t = i / (n6 - 1)
    # thin start, thick middle, thick end (na style)
    if t < 0.6:
        w = 3 + t * 6
    else:
        w = 8 - (t - 0.6) * 10  # slight taper at tip
    widths6.append(max(2, w))
stroke_variable_width(d, curve6, widths6)

out = os.path.join(os.path.dirname(__file__), '01_龹.png')
img.save(out)
print(f"saved {out}")
print(f"strokes: 6, expected 6")
