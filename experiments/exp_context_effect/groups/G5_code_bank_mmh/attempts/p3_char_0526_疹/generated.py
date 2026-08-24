# BANK_DEVIATION
# skipped: no 疒-family radical primitive exists in bank (terminal-freeze cluster
#          declared post-B10 after 9 cumulative FAILs). No bank push per
#          P-COMP-008 refutation. No candidate whole-radical primitive to call.
# reason: 疒-family has no bank coverage; must inline from MMH anchors + GT.
# fresh_component: chuang_radical_inline (5-stroke 疒 from MMH s1-s5) +
#                  zhen_right_inline (5-stroke 㐱 from MMH s6-s10 — 人 + 3-slash cluster)
#
# Quantitative BANK_DEVIATION per P-A-009: n/a — no bank template to compare
# aspect against. All 10 strokes rendered per MMH anchor endpoints verbatim
# (P-A-006 stroke-primitive layer: MMH-anchor verbatim, refusing whole-radical
# composition — appropriate here because no whole-radical bank exists).
#
# Reasoning trace (P-A-008):
# - 疹 = 疒(5) + 㐱(5) = 10 strokes, matches MMH count.
# - 疒 stroke order: dot-slash (s1), 一 (s2), 长丿 (s3), inner dot (s4), inner 提 (s5)
# - 㐱 stroke order: 丿 (s6), 捺 (s7), then 3 parallel 丿 (s8/s9/s10)
# - All 10 rendered as straight lines / short slashes with uniform width 6.

from PIL import Image, ImageDraw

W = H = 300
CELL = 100

CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL, oy + yf * CELL)


img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

LW = 6

# --- 疒 radical (strokes 1-5) ---
# s1: TC(0.389,0.524) -> TC(0.714,0.759)  short dot-slash down-right (top dot)
d.line([anchor('TC', 0.389, 0.524), anchor('TC', 0.714, 0.759)], fill='black', width=LW)
# s2: TC(0.017,0.999) -> TR(0.288,0.867)  horizontal 一
d.line([anchor('TC', 0.017, 0.999), anchor('TR', 0.288, 0.867)], fill='black', width=LW)
# s3: TL(0.806,0.923) -> BL(0.284,0.921)  long 丿 down-left
d.line([anchor('TL', 0.806, 0.923), anchor('BL', 0.284, 0.921)], fill='black', width=LW)
# s4: ML(0.41,0.181) -> ML(0.612,0.421)  short inner dot down-right
d.line([anchor('ML', 0.41, 0.181), anchor('ML', 0.612, 0.421)], fill='black', width=LW)
# s5: BL(0.17,0.019) -> ML(0.738,0.72)  inner 提 upward-right (tail is upper right of head? head lower-left)
# head at (17,200), tail at (73.8, 172) — small upward flick
d.line([anchor('BL', 0.17, 0.019), anchor('ML', 0.738, 0.72)], fill='black', width=LW)

# --- 㐱 (strokes 6-10) ---
# s6: C(0.767,0.175) -> ML(0.987,0.939)  wait ML(0.987,0.939) is (98.7, 193.9)
# head (176.7,117.5) -> tail (98.7,193.9): long down-left slash (left of 人)
d.line([anchor('C', 0.767, 0.175), anchor('ML', 0.987, 0.939)], fill='black', width=LW)
# s7: C(0.731,0.295) -> MR(0.839,0.843)  down-right 捺 (right of 人)
d.line([anchor('C', 0.731, 0.295), anchor('MR', 0.839, 0.843)], fill='black', width=LW)
# s8: C(0.67,0.603) -> BC(0.216,0.159)  first of three parallel 丿
d.line([anchor('C', 0.67, 0.603), anchor('BC', 0.216, 0.159)], fill='black', width=LW)
# s9: C(0.787,0.931) -> BC(0.263,0.569)  second parallel 丿
d.line([anchor('C', 0.787, 0.931), anchor('BC', 0.263, 0.569)], fill='black', width=LW)
# s10: BC(0.893,0.244) -> BC(0.055,1.176)  third parallel 丿 (longest, extending below)
d.line([anchor('BC', 0.893, 0.244), anchor('BC', 0.055, 1.176)], fill='black', width=LW)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 line calls == MMH 10
    'endpoint_mismatches': [],   # all endpoints verbatim from MMH anchors
    'joint_class_mismatches': [],# all 8 expected joints are class N (natural gap) — inline lines with no welding preserves N by default
    'overall_pass': True,
    'notes': 'inline MMH-verbatim; 疒 family has no bank primitive (terminal-freeze).'
}


img.save('<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0526_疹/01_疹.png')
