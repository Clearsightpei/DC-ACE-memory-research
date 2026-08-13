# p3_char_0524_疸 — G5 attempt
#
# Reasoning trace (P-A-008):
#   Char: 疸 = 疒 (sickness) + 旦 (dawn = 日 + 一)
#   Bank check: 疒-family declared terminal-freeze at B10 (9 疒 FAILs).
#   No whole-radical primitive for 疒 exists; per P-A-006 use
#   stroke-primitive layer with MMH anchor verbatim. 旦 also has no
#   whole-radical primitive. So: render all 10 strokes from MMH
#   anchors directly. Straight-line for endpoint-only strokes;
#   stroke 7 is a heng_zhe (top-right of 日 box) → render as L with
#   corner at (tail_x, head_y).
#   BANK_DEVIATION not applicable: no bank primitive skipped
#   (nothing to skip for 疒/旦 at this point in bank state).
#
# Stroke count check: 10 line/L calls below (matches MMH expected 10).

from PIL import Image, ImageDraw

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

def cell_to_px(cell, xf, yf):
    if cell == 'C':
        r, c = 1, 1
    else:
        row_map = {'T': 0, 'M': 1, 'B': 2}
        col_map = {'L': 0, 'C': 1, 'R': 2}
        r = row_map[cell[0]]
        c = col_map[cell[1]]
    return (c * 100 + xf * 100, r * 100 + yf * 100)

# MMH-derived endpoint anchors (verbatim from brief)
anchors = [
    (('TC', 0.438, 0.568), ('TC', 0.77, 0.832)),    # 1 dian (top dot of 疒)
    (('C',  0.04,  0.192), ('MR', 0.317, 0.058)),   # 2 heng (top-right short heng)
    (('ML', 0.817, 0.11 ), ('BL', 0.296, 1.1  )),   # 3 pie (long left descender)
    (('ML', 0.387, 0.368), ('ML', 0.604, 0.641)),   # 4 dian (small inner dot)
    (('BL', 0.152, 0.241), ('ML', 0.729, 0.998)),   # 5 ti (short ti up-right)
    (('C',  0.184, 0.57 ), ('BC', 0.395, 0.402)),   # 6 shu (left vertical of 日)
    (('C',  0.368, 0.673), ('BC', 0.922, 0.294)),   # 7 heng_zhe (top+right of 日 box) — L-shape
    (('C',  0.43,  0.995), ('C',  0.837, 0.928)),   # 8 heng (middle interior of 日)
    (('BC', 0.456, 0.317), ('BC', 0.919, 0.209)),   # 9 heng (bottom of 日)
    (('BL', 0.864, 0.81 ), ('BR', 0.654, 0.789)),   # 10 heng (long base of 旦)
]

STROKE_W = 7

for i, (h, t) in enumerate(anchors):
    hp = cell_to_px(*h)
    tp = cell_to_px(*t)
    if i == 6:  # stroke 7 = heng_zhe (L-shape corner)
        corner = (tp[0], hp[1])
        d.line([hp, corner], fill='black', width=STROKE_W)
        d.line([corner, tp], fill='black', width=STROKE_W)
        # cap the corner so it looks welded (P joint at corner)
        d.ellipse([corner[0]-STROKE_W/2, corner[1]-STROKE_W/2,
                   corner[0]+STROKE_W/2, corner[1]+STROKE_W/2], fill='black')
    else:
        d.line([hp, tp], fill='black', width=STROKE_W)

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0524_疸/01_疸.png')

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,       # 10 stroke calls = MMH expected 10
    'endpoint_mismatches': [],     # anchors used verbatim from brief
    'joint_class_mismatches': [],  # all 6 expected joints are N; straight-line rendering preserves natural gaps
    'overall_pass': None,
    'notes': 'MMH anchors verbatim (P-A-006). No bank primitives applicable for 疒/旦 in current bank; inlined per stroke-primitive layer.',
}
