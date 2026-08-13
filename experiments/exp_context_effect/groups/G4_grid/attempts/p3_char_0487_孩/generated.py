"""孩 (hái, "child") — 9 strokes.

Decomposition: 孩 = 子 (left) + 亥 (right).
  Left (s1-s3): 子 as left radical — 横撇 + 弯钩 + 横 in x∈[0.05, 0.42], y∈[0.35, 0.90].
  Right (s4-s9): 亥 — top 亠 (dian + heng) + inner 撇折 + 3-stroke leg cluster
    (pie + pie + na) in x∈[0.42, 0.98], y∈[0.05, 1.0].

MMH-verbatim anchors per dispatcher block. Base primitives (fat_line +
quad_bezier) rather than compound bank primitives — 子 sits far-left column
compressed, doesn't match zi_char.py's standalone defaults; 亥's leg cluster
is TERMINAL_FROZEN X-cross family so no compound primitive exists.

Reading order (v8 slim): drawer_memory.md → INDEX (子=zi_char; 亥 frozen)
→ errata (亥 chronic, don't reuse).
"""

# BANK_DEVIATION
# skipped: zi_char.py
# reason: 子 sits far-left compressed column in 孩 (x∈[0.05,0.42]); zi_char defaults are
#   standalone-canvas centered — partial anchor override would trigger the伊 anti-pattern.
# fresh_component: zi_left_far_left_for_compound

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; s2.mid × s3.mid welded (P); other joints N with natural gaps.',
}

import os, sys
from PIL import Image, ImageDraw

# Import bank helpers.
BANK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def a(t):
    return anchor_to_xy(t)


# ---------- LEFT: 子 (compressed far-left column) ----------

# s1 — 横撇 : starts short heng down-right, then bends. MMH gives head→tail only
#      (small stroke). Render as a slight downward heng with a small bend into 竖钩.
s1_h = a(('ML', 0.434, 0.069))     # ~ (43, 107)
s1_t = a(('ML', 0.94, 0.395))      # ~ (94, 140)
# Use a quad_bezier to give it the horizontal-then-drop feel.
ctrl1 = ((s1_h[0] + s1_t[0]) / 2 + 4, (s1_h[1] + s1_t[1]) / 2 - 3)
pts1 = quad_bezier(s1_h, ctrl1, s1_t, n=32)
widths1 = [7 - 4 * (i / len(pts1)) for i in range(len(pts1))]
widths1 = [max(3, w) for w in widths1]
stroke_variable_width(d, pts1, widths1)

# s2 — 弯钩 : from top of 子 body, curve down with belly right, hook up-left at tail.
s2_h = a(('ML', 0.797, 0.412))     # ~ (80, 141)
s2_t = a(('BL', 0.612, 0.689))     # ~ (61, 269)
belly2 = (a(('ML', 0.95, 0.85))[0], a(('ML', 0.95, 0.85))[1])   # ~ (95, 185) push right for belly
# Two-segment bezier to describe belly then hook.
mid2 = (belly2[0], (s2_h[1] + s2_t[1]) / 2)
pts2a = quad_bezier(s2_h, belly2, ((belly2[0] + s2_t[0]) / 2, s2_t[1] - 5), n=24)
pts2b = quad_bezier(pts2a[-1], (s2_t[0] + 15, s2_t[1] + 5), s2_t, n=16)
pts2 = pts2a + pts2b[1:]
widths2 = [10 - 5 * (i / len(pts2)) for i in range(len(pts2))]
widths2 = [max(3, w) for w in widths2]
stroke_variable_width(d, pts2, widths2)

# s3 — 横 crossing through 子 body (P weld with s2.mid).
s3_h = a(('BL', 0.217, 0.177))     # ~ (22, 218)
s3_t = a(('C', 0.289, 0.608))      # ~ (129, 261)
fat_line(d, s3_h, s3_t, width=8)

# ---------- RIGHT: 亥 ----------

# s4 — top dian/short pie of 亠 : (179, 62) → (212, 92)
s4_h = a(('TC', 0.796, 0.624))     # (179.6, 62.4)
s4_t = a(('TR', 0.124, 0.92))      # (212.4, 92.0)
# Short dot-like stroke.
pts4 = quad_bezier(s4_h, ((s4_h[0] + s4_t[0]) / 2, s4_h[1] + 8), s4_t, n=16)
widths4 = [4 + 5 * (i / len(pts4)) for i in range(len(pts4))]
stroke_variable_width(d, pts4, widths4)

# s5 — long 横 across upper 亥 : (133, 128) → (255, 115)
s5_h = a(('C', 0.333, 0.28))       # (133.3, 128.0)
s5_t = a(('MR', 0.549, 0.148))     # (254.9, 114.8)
fat_line(d, s5_h, s5_t, width=8)

# s6 — small 撇 or 竖 for 亥 top inner : (176, 132) → (196, 186)
s6_h = a(('C', 0.755, 0.318))      # (175.5, 131.8)
s6_t = a(('C', 0.96, 0.863))       # (196.0, 186.3)
fat_line(d, s6_h, s6_t, width=7)

# s7 — long 撇 spanning from upper-right down to lower-left : (214, 149) → (123, 264)
s7_h = a(('MR', 0.139, 0.491))     # (213.9, 149.1)
s7_t = a(('BC', 0.228, 0.637))     # (122.8, 263.7)
# Curved pie.
ctrl7 = ((s7_h[0] + s7_t[0]) / 2 + 10, (s7_h[1] + s7_t[1]) / 2 - 5)
pts7 = quad_bezier(s7_h, ctrl7, s7_t, n=40)
widths7 = [8 - 6 * (i / len(pts7)) for i in range(len(pts7))]
widths7 = [max(2, w) for w in widths7]
stroke_variable_width(d, pts7, widths7)

# s8 — 撇 in lower-right leg cluster : (245, 209) → (156, 283)
s8_h = a(('BR', 0.446, 0.089))     # (244.6, 208.9)
s8_t = a(('BC', 0.556, 0.827))     # (155.6, 282.7)
ctrl8 = ((s8_h[0] + s8_t[0]) / 2 + 5, (s8_h[1] + s8_t[1]) / 2 - 5)
pts8 = quad_bezier(s8_h, ctrl8, s8_t, n=32)
widths8 = [8 - 5 * (i / len(pts8)) for i in range(len(pts8))]
widths8 = [max(2, w) for w in widths8]
stroke_variable_width(d, pts8, widths8)

# s9 — 捺 leg going right-down : (211, 253) → (261, 296)
s9_h = a(('BR', 0.109, 0.528))     # (210.9, 252.8)
s9_t = a(('BR', 0.607, 0.959))     # (260.7, 295.9)
# Na: thin start → thick tail.
ctrl9 = ((s9_h[0] + s9_t[0]) / 2 - 3, (s9_h[1] + s9_t[1]) / 2 + 5)
pts9 = quad_bezier(s9_h, ctrl9, s9_t, n=32)
widths9 = [3 + 8 * (i / len(pts9)) for i in range(len(pts9))]
stroke_variable_width(d, pts9, widths9)

out = os.path.join(os.path.dirname(__file__), '01_孩.png')
img.save(out)
print('wrote', out)
