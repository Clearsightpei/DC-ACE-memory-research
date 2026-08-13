"""p3_char_0107_仃 (dīng) — 亻 (left) + 丁 (right), 4 strokes.

Composition: inline from stroke bank per drawer_memory.md line 199-204
rule — ren_left bank baked geometry is >30px off from MMH anchors for
this composition, so inline pie+shu for 亻 rather than transforming.
丁 has no whole-radical bank entry; compose from heng + shu_gou.

SELF_CHECK (see bottom).
"""
import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                 'success_bank', 'code'))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_gou import draw_shu_gou

# ---- Anchor helpers: 米字格 3x3 grid on 300x300 canvas ----
CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, fx, fy):
    ox, oy = CELL[cell]
    return (ox + fx * 100, oy + fy * 100)

# ---- Anchors from MMH block ----
s1_head = A('TL', 0.999, 0.615)   # (99.9, 61.5)
s1_tail = A('ML', 0.202, 0.922)   # (20.2, 192.2)
s2_head = A('ML', 0.735, 0.491)   # (73.5, 149.1)
s2_tail = A('BL', 0.773, 0.938)   # (77.3, 293.8)
s3_head = A('C',  0.157, 0.368)   # (115.7, 136.8)
s3_tail = A('MR', 0.698, 0.257)   # (269.8, 125.7)
s4_head = A('C',  0.843, 0.365)   # (184.3, 136.5)
s4_tail = A('BC', 0.562, 0.786)   # (156.2, 278.6)

# ---- Render ----
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# 亻 (strokes 1-2)
# s1: 撇 (pie) from upper-right of TL to lower-left of ML
draw_pie(d, s1_head, s1_tail, bow_perp=20, w_head=9, w_tail=3, steps=80)
# s2: 竖 (shu) — the vertical of 亻, touching s1 mid on the N side
draw_shu(d, s2_head, s2_tail, width=7, top_curl=True)

# 丁 (strokes 3-4)
# s3: 横 (heng) — top horizontal spanning C to MR
draw_heng(d, s3_head, s3_tail, width_head=6, width_tail=7)
# s4: 竖钩 (shu-gou) — vertical with leftward hook at tail
# head at (184.3, 136.5), tail at (156.2, 278.6). Hook curls back-left.
# Larger hook_start_offset + wider tail displacement → more visible hook.
draw_shu_gou(d, s4_head, s4_tail, width=7, hook_start_offset=55)

img.save(os.path.join(os.path.dirname(__file__), '01_仃.png'))

# ---- MANDATORY SELF-CHECK ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke calls: pie, shu, heng, shu_gou
    'endpoint_mismatches': [], # anchors are MMH-verbatim
    'joint_class_mismatches': [],  # both joints N: s1.mid≈s2.head near-touch; s3.mid≈s4.head near-touch (natural stroke ends leave small gap)
    'overall_pass': True,
    'notes': 'Inlined from stroke bank per composition-rule L199-L204 (bank ren_left geometry >30px off from these MMH anchors). Both joints are N (calligraphic gap), no welding.',
}
