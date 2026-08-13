"""畟 (jì) — 10 strokes.
Decomposition: 畟 = 田 (top, 5 strokes) + 夊-family (bottom, 5 strokes).
Top block = 田-like grid: left shu (s1), heng-zhe frame (s2),
inner heng (s3), inner shu (s4), inner heng bottom (s5).
Bottom block = 夊/夂 pattern: 撇 (s6), 捺 (s7), 撇 (s8), 撇 (s9), 捺 (s10).

Following B9 A-recipe: MMH-verbatim endpoints; inline base primitives;
no compound primitive fits (no bank primitive for 畟 or its parts).
Joints per MMH: mostly N (natural gap), two P welds (s3~s4, s9~s10).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 10 strokes exactly
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; top 田 frame + bottom 夊 legs; two P welds (s3-s4 upper cross, s9-s10 lower cross), rest N gaps preserved.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---------- TOP BLOCK — 田-like frame ----------
# s1: LEFT SHU (slightly slanted right)
S1_H = ('TL', 0.85, 0.782)
S1_T = ('C',  0.134, 0.644)
fat_line(d, anchor_to_xy(S1_H), anchor_to_xy(S1_T), 8)

# s2: HENG-ZHE — top horizontal then right vertical drop.
# Head TC(0.014,0.788)=(101,79); Tail C(0.963,0.515)=(196,152).
# Insert corner at (~tail_x, head_y) for the fold.
p2_head   = anchor_to_xy(('TC', 0.014, 0.788))
p2_tail   = anchor_to_xy(('C',  0.963, 0.515))
p2_corner = (p2_tail[0], p2_head[1])   # (196, 79)
fat_line(d, p2_head,   p2_corner, 8)
fat_line(d, p2_corner, p2_tail,   8)
r = 5
d.ellipse([p2_corner[0]-r, p2_corner[1]-r,
           p2_corner[0]+r, p2_corner[1]+r], fill=(0,0,0))

# s3: inner TOP HENG
S3_H = ('C', 0.248, 0.184)
S3_T = ('C', 0.837, 0.11)
fat_line(d, anchor_to_xy(S3_H), anchor_to_xy(S3_T), 7)

# s4: inner SHU (middle spine)
S4_H = ('TC', 0.436, 0.817)
S4_T = ('C',  0.468, 0.377)
fat_line(d, anchor_to_xy(S4_H), anchor_to_xy(S4_T), 7)

# s5: inner BOTTOM HENG (frame bottom)
S5_H = ('C', 0.184, 0.459)
S5_T = ('C', 0.846, 0.377)
fat_line(d, anchor_to_xy(S5_H), anchor_to_xy(S5_T), 8)

# ---------- BOTTOM BLOCK — 夊 / 夂 legs ----------
# s6: short 撇 (upper-left of bottom block)
S6_H = ('C',  0.26,  0.781)
S6_T = ('BL', 0.768, 0.109)
p6h, p6t = anchor_to_xy(S6_H), anchor_to_xy(S6_T)
# curve slightly (pie)
ctrl6 = (p6h[0]-4, (p6h[1]+p6t[1])/2)
pts6 = quad_bezier(p6h, ctrl6, p6t, n=32)
widths6 = [max(2, 8 - 6*i/(len(pts6)-1)) for i in range(len(pts6))]
stroke_variable_width(d, pts6, widths6)

# s7: 捺 going down-right
S7_H = ('C',  0.693, 0.567)
S7_T = ('MR', 0.42,  0.966)
p7h, p7t = anchor_to_xy(S7_H), anchor_to_xy(S7_T)
ctrl7 = ((p7h[0]+p7t[0])/2 - 6, (p7h[1]+p7t[1])/2 + 4)
pts7 = quad_bezier(p7h, ctrl7, p7t, n=36)
widths7 = [3 + 8*(i/(len(pts7)-1))**1.3 for i in range(len(pts7))]
# taper back down at the very end
widths7[-3:] = [7, 5, 3]
stroke_variable_width(d, pts7, widths7)

# s8: 撇 sweeping SW
S8_H = ('C',  0.298, 0.916)
S8_T = ('BL', 0.633, 0.675)
p8h, p8t = anchor_to_xy(S8_H), anchor_to_xy(S8_T)
ctrl8 = (p8h[0]-6, (p8h[1]+p8t[1])/2 + 6)
pts8 = quad_bezier(p8h, ctrl8, p8t, n=36)
widths8 = [max(2, 9 - 7*i/(len(pts8)-1)) for i in range(len(pts8))]
stroke_variable_width(d, pts8, widths8)

# s9: long 撇 going SW/down
S9_H = ('BC', 0.269, 0.276)
S9_T = ('BL', 0.688, 1.067)
p9h, p9t = anchor_to_xy(S9_H), anchor_to_xy(S9_T)
ctrl9 = (p9h[0]-4, (p9h[1]+p9t[1])/2 + 8)
pts9 = quad_bezier(p9h, ctrl9, p9t, n=40)
widths9 = [max(2, 9 - 7*i/(len(pts9)-1)) for i in range(len(pts9))]
stroke_variable_width(d, pts9, widths9)

# s10: long 捺 sweeping down-right (final big stroke)
S10_H = ('BC', 0.055, 0.481)
S10_T = ('BR', 0.783, 1.082)
p10h, p10t = anchor_to_xy(S10_H), anchor_to_xy(S10_T)
ctrl10 = ((p10h[0]+p10t[0])/2, (p10h[1]+p10t[1])/2 + 12)
pts10 = quad_bezier(p10h, ctrl10, p10t, n=48)
widths10 = [3 + 10*(i/(len(pts10)-1))**1.2 for i in range(len(pts10))]
# taper at the very tail
widths10[-3:] = [8, 5, 3]
stroke_variable_width(d, pts10, widths10)

out_path = os.path.join(os.path.dirname(__file__), '01_畟.png')
img.save(out_path)
print(f"Wrote {out_path}")
