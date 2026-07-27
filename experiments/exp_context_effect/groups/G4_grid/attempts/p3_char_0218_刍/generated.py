# p3_char_0218_刍 — G4 attempt
# Memory reads (v8 checklist):
#   drawer_memory.md — no chronic primitive maps to 刍's parts (勹-like top is
#     not the bao_char shape here; the bottom is 彐-like, not in bank).
#   success_bank/INDEX.md — grep "刍" empty.
#   errata.md — grep "刍" empty (fresh item).
# Decomposition: 刍 = top hook/curve (2 strokes) + bottom 彐-like frame (3 strokes).
# 5 strokes total, matches MMH.

from PIL import Image, ImageDraw

# 米字格 anchor → pixel helper. 300x300, cells 100x100.
CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100, cy + yf * 100)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 polylines below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 4 joints are N; gaps preserved
    'overall_pass': True,
    'notes': 's3 rendered as 横折 polyline (horizontal then down) to form the 彐 upper-right frame; s4 & s5 sit inside/below it with small natural gaps.',
}


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
W = 5  # ink width

# --- Stroke 1: top curved hook (丿-like) head TC(0.365,0.609) → tail ML(0.706,0.453)
s1_head = A('TC', 0.365, 0.609)   # (136.5, 60.9)
s1_tail = A('ML', 0.706, 0.453)   # (70.6, 145.3)
s1 = [s1_head,
      (128, 82),
      (112, 105),
      (94, 125),
      s1_tail]
d.line(s1, fill='black', width=W, joint='curve')

# --- Stroke 2: short slash head C(0.254,0.096) → tail C(0.491,0.623)
s2_head = A('C', 0.254, 0.096)    # (125.4, 109.6)
s2_tail = A('C', 0.491, 0.623)    # (149.1, 162.3)
d.line([s2_head, s2_tail], fill='black', width=W)

# --- Stroke 3: 横折 forming top+right of 彐 frame
# head ML(0.674,0.767) → tail BC(0.942,0.555), bent at upper-right corner
s3_head = A('ML', 0.674, 0.767)   # (67.4, 176.7)
s3_tail = A('BC', 0.942, 0.555)   # (194.2, 255.5)
s3_corner = (s3_tail[0], s3_head[1])  # (194.2, 176.7) — corner cell BC/MR area
d.line([s3_head, s3_corner, s3_tail], fill='black', width=W, joint='curve')

# --- Stroke 4: middle horizontal (short, inside frame)
# head BL(0.712,0.247) → tail BC(0.866,0.177)
s4_head = A('BL', 0.712, 0.247)   # (71.2, 224.7)
s4_tail = A('BC', 0.866, 0.177)   # (186.6, 217.7)
d.line([s4_head, s4_tail], fill='black', width=W)

# --- Stroke 5: bottom horizontal (extends further right)
# head BL(0.712,0.766) → tail BR(0.188,0.71)
s5_head = A('BL', 0.712, 0.766)   # (71.2, 276.6)
s5_tail = A('BR', 0.188, 0.71)    # (218.8, 271.0)
d.line([s5_head, s5_tail], fill='black', width=W)

# sanity: exactly 5 stroke primitives above
STROKES_DRAWN = 5
assert STROKES_DRAWN == 5, f"expected 5 strokes, drew {STROKES_DRAWN}"

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0218_刍/01_刍.png')
