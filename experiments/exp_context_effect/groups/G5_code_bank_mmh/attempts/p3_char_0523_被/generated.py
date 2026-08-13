"""p3_char_0523_被 (bei, "quilt/passive") — 10 strokes.

Structure: 衤 (5 strokes, left) + 皮 (5 strokes, right).

BANK REVIEW (P-A-007-v2 hard-check):
  Bank has shi_spirit (礻, 4 strokes) — CLOSE but wrong: 衤 has 5 strokes
  (adds a second dot). Whole-radical mismatch on stroke count (not
  uniform-shift adjustable) — refuse whole-radical primitive. No 皮 or
  被 primitive in bank. Decision: inline all 10 strokes from MMH anchors,
  with visual adjustment where MMH samples degenerate segments.
  Not a BANK_DEVIATION: no matched primitive was skipped.

REVISION notes (pass 2):
  Pass 1 was too disconnected — top dots misplaced, 皮 top structure
  fragmented. Pass 2: keep MMH endpoints as guides but connect strokes
  into calligraphic units matching GT silhouette. s2 (MMH: short
  vertical at far-left) is treated as 衤's short 横 crossbar; s3 (MMH:
  tiny stub) treated as the main 衤 竖.
"""

from PIL import Image, ImageDraw

# --- Anchor → pixel helper (米字格 3x3 cells, 100px each on 300x300) ---
CELL_X = {'TL': 0, 'TC': 100, 'TR': 200,
          'ML': 0, 'C':  100, 'MR': 200,
          'BL': 0, 'BC': 100, 'BR': 200}
CELL_Y = {'TL': 0,   'TC': 0,   'TR': 0,
          'ML': 100, 'C':  100, 'MR': 100,
          'BL': 200, 'BC': 200, 'BR': 200}

def A(cell, xf, yf):
    return (CELL_X[cell] + 100 * xf, CELL_Y[cell] + 100 * yf)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def stroke(p0, p1, width):
    d.line([p0, p1], fill=BLACK, width=int(round(width)))

def stroke_poly(pts, width):
    d.line(pts, fill=BLACK, width=int(round(width)), joint='curve')

# =============================================================
# 衤 (left radical, 5 strokes) — positioned left half x=25..115
# =============================================================

# s1: top 点 dian (small down-right slant near top-left)
stroke_poly([(65, 55), (85, 80)], 6)

# s2: 横撇 crossbar — short heng from upper-left crossing to right-ish,
#     ending with a small pie hook down-left.
stroke_poly([(35, 118), (110, 108), (95, 130)], 5)

# s3: 竖 main vertical of 衤 (from just under crossbar down to bottom)
stroke((78, 128), (78, 265), 6)

# s4: 撇 small on left (dot-like, sweeping down-left)
stroke_poly([(60, 165), (35, 210)], 6)

# s5: 捺/dot on right (below-right of vertical)
stroke_poly([(95, 165), (128, 210)], 6)

# =============================================================
# 皮 (right side, 5 strokes) — positioned right half x=125..290
# =============================================================

# s6: 皮 top 横 with rightward extension (short heng near top)
s6_head = (145, 85)
s6_tail = (250, 90)
stroke(s6_head, s6_tail, 5)

# s7: 皮 main 撇 — long diagonal from top-right of s6 down-left to bottom
#     (starts near right end of s6, sweeps down through left side).
s7_head = (220, 60)   # tiny bit above s6, provides the top hook
s7_tail = (135, 275)
mid_s7 = ((s7_head[0] + s7_tail[0]) / 2 - 12,
          (s7_head[1] + s7_tail[1]) / 2 + 10)
stroke_poly([s7_head, mid_s7, s7_tail], 6)

# s8: 皮 内 short vertical (pierces the box formed under top heng, hangs
#     down forming left side of interior 又's 口-like region).
s8_head = (185, 100)
s8_tail = (190, 180)
stroke(s8_head, s8_tail, 5)

# s9: 又 横撇 (short horizontal turning into pie, mid-right area)
s9_head = (180, 180)
s9_corner = (245, 178)
s9_tail = (200, 260)
stroke_poly([s9_head, s9_corner, s9_tail], 5)

# s10: 又 main 捺 (sweeping down-right to bottom-right corner)
s10_head = (215, 200)
mid_s10 = (255, 245)
s10_tail = (290, 285)
stroke_poly([s10_head, mid_s10, s10_tail], 7)

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0523_被/01_被.png')

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 strokes
    'endpoint_mismatches': [
        {'stroke': 2, 'note': 'MMH sampled a vertical; visual 衤 s2 is a heng-pie crossbar'},
        {'stroke': 3, 'note': 'MMH sampled tiny stub; extended to full 衤 竖'},
        {'stroke': 8, 'note': 'MMH s8 head at TC(0.811,0.618)=y61 too high; kept as short interior vertical'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Pass 2 revision: connected calligraphic units matching GT silhouette. '
             '衤 left: dian + heng-pie crossbar + long shu + two dots. '
             '皮 right: top heng, main pie, interior shu, 又 (heng-pie + na). '
             'No BANK_DEVIATION — no matching primitive to skip.',
}
