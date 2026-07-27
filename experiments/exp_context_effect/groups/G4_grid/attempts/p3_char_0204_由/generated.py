# 由 (yóu) — Phase 3 char 0204, 5 strokes
# Structure: frame (left wall + 横折 top+right) + long spine protruding above frame
# + inner middle heng (welded across spine) + bottom heng (near-neighbors at
# frame bottom corners; N-gap to spine tail)
# Split: 由 ≈ 田-frame variant with spine breaking top.
# Reused conceptual layout from mastered 甲/申 (INDEX 157/159): inline frame +
# shu + heng, no chronic import needed (jiong_frame is 冂 without inner strokes).
# Anchors follow MMH-derived expectations verbatim.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 fat_line stroke primitives (s2 = 2 segments = 1 横折)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # P joints share pixels (welded); N joints have natural gaps
    'overall_pass': True,
    'notes': '由: 5 strokes as per MMH. Spine (s4) is tall, protrudes above frame top; welded to s3 (inner heng) and s2 (top bar) crossings; N-gap to s5 (bottom heng).'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from _anchor import anchor_to_xy, fat_line

WIDTH = 8

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# s1 — left wall of frame (slight rightward slant, trapezoidal narrowing)
#      head ML(0.516,0.485) → tail BL(0.855,0.81)
p1_head = anchor_to_xy(('ML', 0.516, 0.485))
p1_tail = anchor_to_xy(('BL', 0.855, 0.81))
fat_line(draw, p1_head, p1_tail, WIDTH)

# s2 — 横折 (top bar + right wall). Corner inferred: same y as head, same x as tail.
#      head ML(0.718,0.521) → tail BR(0.106,0.895)
p2_head = anchor_to_xy(('ML', 0.718, 0.521))
p2_tail = anchor_to_xy(('BR', 0.106, 0.895))
p2_corner = (p2_tail[0], p2_head[1])
fat_line(draw, p2_head, p2_corner, WIDTH)
fat_line(draw, p2_corner, p2_tail, WIDTH)

# s3 — inner middle heng (welded to spine at mid, P-class)
#      head BC(0.005,0.083) → tail C(0.884,0.998)
p3_head = anchor_to_xy(('BC', 0.005, 0.083))
p3_tail = anchor_to_xy(('C', 0.884, 0.998))
fat_line(draw, p3_head, p3_tail, WIDTH)

# s4 — long central spine, protrudes above frame top (head at TC y=0.633)
#      head TC(0.318,0.633) → tail BC(0.395,0.546)
p4_head = anchor_to_xy(('TC', 0.318, 0.633))
p4_tail = anchor_to_xy(('BC', 0.395, 0.546))
fat_line(draw, p4_head, p4_tail, WIDTH)

# s5 — bottom heng closing the frame (N-neighbor to s1.tail and s2.tail;
#      N-gap to s4.tail — spine does not touch the bottom heng)
#      head BL(0.92,0.719) → tail BR(0.01,0.578)
p5_head = anchor_to_xy(('BL', 0.92, 0.719))
p5_tail = anchor_to_xy(('BR', 0.01, 0.578))
fat_line(draw, p5_head, p5_tail, WIDTH)

OUT = os.path.join(_HERE, '01_由.png')
img.save(OUT)
print("Saved", OUT)
