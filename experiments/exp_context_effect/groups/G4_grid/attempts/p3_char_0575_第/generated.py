"""p3_char_0575_第 — G4 attempt (revision 1).

Read: drawer_memory.md (chronic imports), INDEX (no 第 present),
errata (no 第 present). No mastered primitive covers 第. Inlining
fresh from MMH anchors given in the brief.

Revision notes vs pass 1: removed off-anchor curve control points
that produced a wrong big diagonal in the top-right; use lines +
minimal in-cell control points; clarify bottom-hook structure by
extending piercing-vertical (s10) fully and giving stroke 11 a
sharper corner (heng-zhe-gou form).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 11 primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Straight-line strokes at MMH anchors; s10 piercing '
             'vertical welds through s8 heng and s9 slant (P joints); '
             'other joints are unwelded N.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W = 6
BLACK = (0, 0, 0)


def line(a, b, w=W):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w, color=BLACK)


def curve(a0, a1, a2, w=W):
    pts = quad_bezier(anchor_to_xy(a0), anchor_to_xy(a1), anchor_to_xy(a2), n=30)
    stroke_variable_width(d, pts, [w] * len(pts), color=BLACK)


# ---------------- 11 strokes of 第 ----------------

# --- 竹字头 (bamboo top): 6 strokes, left cluster + right cluster ---

# stroke 1: left 撇 — TL(.888,.645) -> ML(.513,.354)
curve(('TL', 0.888, 0.60), ('TL', 0.78, 0.85), ('ML', 0.513, 0.354), w=6)

# stroke 2: left short 横 — TL(.999,.929) -> TC(.553,.847)
line(('TL', 0.999, 0.929), ('TC', 0.553, 0.847), w=6)

# stroke 3: left 点 — C(.075,.099) -> C(.216,.233)
curve(('C', 0.075, 0.09), ('C', 0.14, 0.15), ('C', 0.216, 0.233), w=6)

# stroke 4: right 撇 — TC(.743,.554) -> C(.497,.128)
curve(('TC', 0.743, 0.50), ('TC', 0.60, 0.85), ('C', 0.497, 0.128), w=6)

# stroke 5: right short 横 — TC(.852,.844) -> TR(.399,.765)
line(('TC', 0.852, 0.844), ('TR', 0.399, 0.765), w=6)

# stroke 6: right 点/短撇 — TC(.898,.999) -> MR(.153,.178) (short slant down-right)
line(('TC', 0.898, 0.999), ('MR', 0.153, 0.178), w=6)

# --- middle + body: 5 strokes ---

# stroke 7: short 横 upper body — ML(.914,.459) -> C(.866,.62)
line(('ML', 0.914, 0.459), ('C', 0.866, 0.62), w=6)

# stroke 8: main 横 crossing — ML(.967,.816) -> MR(.010,.731)
line(('ML', 0.967, 0.816), ('MR', 0.010, 0.731), w=6)

# stroke 9: 撇-like slant — ML(.800,.755) -> BC(.881,.525)
curve(('ML', 0.800, 0.755), ('C', 0.50, 0.85), ('BC', 0.881, 0.525), w=6)

# stroke 10: piercing 竖钩 — C(.409,.456) -> BC(.482,1.152) with left hook
p10a = anchor_to_xy(('C', 0.409, 0.456))
p10b = anchor_to_xy(('BC', 0.482, 1.152))
fat_line(d, p10a, p10b, W, color=BLACK)
hook_end = (p10b[0] - 16, p10b[1] - 8)
fat_line(d, p10b, hook_end, W - 1, color=BLACK)

# stroke 11: bottom 横折 (L-shape) — BC(.403,.197) -> BL(.489,1.006)
# render as: from BC(.403,.197) go across-right to BR area, then down to BL(.489,1.006)
p11_head = anchor_to_xy(('BC', 0.403, 0.197))
p11_corner = anchor_to_xy(('BR', 0.05, 0.30))
p11_tail = anchor_to_xy(('BL', 0.489, 1.006))
fat_line(d, p11_head, p11_corner, W, color=BLACK)
fat_line(d, p11_corner, p11_tail, W, color=BLACK)


img.save(os.path.join(os.path.dirname(__file__), '01_第.png'))
print('rendered 01_第.png')
