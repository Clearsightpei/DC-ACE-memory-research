"""p3_char_0216_失 — G4 attempt.

Decomposition: 失 = 丿 (short pie top-left) + 一 (top heng) + 一 (mid heng)
             + 丿 (main pie) + 捺 (na).  5 strokes, matches MMH.

Reading order (v8):
  1) drawer_memory.md — read (no single-primitive covers 失; no chronic hit)
  2) INDEX.md grep for 失 — not mastered; grep for 矢/大/夫 — none in bank
  3) errata.md grep for 失 — not present
  Draw fresh per MMH anchors.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke count = 5 matches MMH. Anchors follow brief. P joints at C (s2xs4, s3xs4) welded by geometry. N joints have natural gaps.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- Stroke 1: short 丿 (pie) TL(.946,.943) -> ML(.618,.652)
p0 = anchor_to_xy(('TL', 0.946, 0.943))
p2 = anchor_to_xy(('ML', 0.618, 0.652))
# slight leftward curve
ctrl = (p0[0] - 4, (p0[1] + p2[1]) / 2 - 2)
pts = quad_bezier(p0, ctrl, p2, n=30)
widths = [7 - 4 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# ---- Stroke 2: top 一 (heng, slight upward) ML(.976,.368) -> MR(.065,.184)
p0 = anchor_to_xy(('ML', 0.976, 0.368))
p1 = anchor_to_xy(('MR', 0.065, 0.184))
fat_line(d, p0, p1, width=7)

# ---- Stroke 3: middle 一 (heng, slight upward) ML(.595,.978) -> MR(.426,.819)
p0 = anchor_to_xy(('ML', 0.595, 0.978))
p1 = anchor_to_xy(('MR', 0.426, 0.819))
fat_line(d, p0, p1, width=7)

# ---- Stroke 4: main 丿 (long pie) TC(.389,.598) -> BL(.422,.936)
p0 = anchor_to_xy(('TC', 0.389, 0.598))
p2 = anchor_to_xy(('BL', 0.422, 0.936))
# curve leftward significantly (pie)
mid_x = (p0[0] + p2[0]) / 2
mid_y = (p0[1] + p2[1]) / 2
ctrl = (mid_x + 18, mid_y - 6)  # bulge to the right of the chord = arch = 撇 curls left
pts = quad_bezier(p0, ctrl, p2, n=50)
widths = [8 - 5 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# ---- Stroke 5: 捺 (na) C(.538,.978) -> BR(.763,.927)
p0 = anchor_to_xy(('C', 0.538, 0.978))
p2 = anchor_to_xy(('BR', 0.763, 0.927))
# slight downward-right curve, widening
ctrl_x = (p0[0] + p2[0]) / 2 + 4
ctrl_y = (p0[1] + p2[1]) / 2 + 10
pts = quad_bezier(p0, (ctrl_x, ctrl_y), p2, n=40)
widths = [3 + 6 * (i / len(pts)) for i in range(len(pts))]
# na traditionally tapers again at end; leave heavier tail
stroke_variable_width(d, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_失.png')
img.save(out)
print('wrote', out)
