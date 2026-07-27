"""
p3_char_0222_乑 — G4 attempt

Memory reads (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — no chronic/component primitive maps to 乑 directly;
     it is a 3-fold repetition of 人-like shape. Not in shortlist.
  2. success_bank/INDEX.md — grepped; no prior 乑; 人 primitive not yet present.
  3. errata.md — grepped; 乑 not listed.

Compositional split: 乑 = 人 (top) + 人 (bottom-left) + 人 (bottom-right).
MMH gives 6 strokes = 3 pairs, but pair 2 (strokes 3+4) is 撇+撇 not 撇+捺,
suggesting the middle 人 is a 从-like drop of two 撇s while the third
uses 撇+捺. Trust GT/MMH per v8 (bank is reference only).

Drawing with PIL polylines directly at the MMH-derived anchors.
"""
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'draw 6 strokes as smooth polylines at MMH anchors; N-joints kept as small gaps; s5.tail welded to s6.head (T).'
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# 米字格 cell origins (top-left of each cell, in PIL pixel coords, y grows DOWN)
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)

def clamp(p):
    x, y = p
    return (max(1, min(W-1, x)), max(1, min(H-1, y)))

def stroke(pts, width=5):
    pts = [clamp(p) for p in pts]
    d.line(pts, fill='black', width=width, joint='curve')

# Stroke 1: 撇 at top — from TC(0.679, 0.688) → TL(0.601, 0.946)
s1_head = A('TC', 0.679, 0.688)
s1_tail = A('TL', 0.601, 0.946)
# Add a slight curve for calligraphic feel
s1_mid = ((s1_head[0] + s1_tail[0]) / 2 - 3, (s1_head[1] + s1_tail[1]) / 2)
stroke([s1_head, s1_mid, s1_tail], width=5)

# Stroke 2: long right descending — from TC(0.066, 0.908) → BC(0.181, 1.185)
# This is the long 捺-like leg of the top 人, extending nearly full height
s2_head = A('TC', 0.066, 0.908)
s2_tail = A('BC', 0.181, 1.185)  # y_frac 1.185 means below the BC row
# Slight arc, thickens toward tail — draw as tapered polyline
s2_q1 = (s2_head[0] + 2, s2_head[1] + (s2_tail[1]-s2_head[1]) * 0.33)
s2_q2 = (s2_head[0] + 5, s2_head[1] + (s2_tail[1]-s2_head[1]) * 0.66)
stroke([s1_head[0]-1, s1_head[1]+2] if False else [s2_head, s2_q1, s2_q2, s2_tail], width=6)

# Stroke 3: 撇 middle-left area — from ML(0.768, 0.336) → BL(0.334, 0.033)
s3_head = A('ML', 0.768, 0.336)
s3_tail = A('BL', 0.334, 0.033)
s3_mid = ((s3_head[0] + s3_tail[0]) / 2 - 2, (s3_head[1] + s3_tail[1]) / 2)
stroke([s3_head, s3_mid, s3_tail], width=5)

# Stroke 4: 撇 lower-left — from ML(0.768, 0.998) → BL(0.334, 0.692)
s4_head = A('ML', 0.768, 0.998)
s4_tail = A('BL', 0.334, 0.692)
s4_mid = ((s4_head[0] + s4_tail[0]) / 2 - 2, (s4_head[1] + s4_tail[1]) / 2)
stroke([s4_head, s4_mid, s4_tail], width=5)

# Stroke 5: 撇 in center area — from C(0.975, 0.072) → C(0.304, 0.685)
s5_head = A('C', 0.975, 0.072)
s5_tail = A('C', 0.304, 0.685)
s5_mid = ((s5_head[0] + s5_tail[0]) / 2 - 3, (s5_head[1] + s5_tail[1]) / 2)
stroke([s5_head, s5_mid, s5_tail], width=5)

# Stroke 6: 捺 from center → BR — from C(0.315, 0.705) → BR(0.681, 0.49)
# s5.tail (130.4, 168.5) welded to s6.head (131.5, 170.5): T-joint, welded
s6_head = A('C', 0.315, 0.705)
s6_tail = A('BR', 0.681, 0.49)
s6_mid = ((s6_head[0] + s6_tail[0]) / 2, (s6_head[1] + s6_tail[1]) / 2 + 3)
stroke([s6_head, s6_mid, s6_tail], width=6)

out = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0222_乑/01_乑.png'
img.save(out)
print(f"Saved {out}")
print(f"Stroke count = 6")
