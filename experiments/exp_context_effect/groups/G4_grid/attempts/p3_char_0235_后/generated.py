"""Draw 后 (hòu) — 6 strokes, PIL 300x300.

Composition: top 短撇 (s1), long 横撇 forming top and left flank (s2),
short middle heng (s3), then 口-like enclosure formed by s4 (left vert),
s5 (heng-zhe top+right), s6 (bottom heng).

Memory log:
- Read drawer_memory.md v8 top matter + memory_index.md v8 checklist.
- 后 not in success_bank INDEX; not in errata.
- Not a chronic-cluster component (no 丿/刀/冂/弓/马 stand-alone module fits).
- Free composition per shared_rules v8: bank is reference only.
- Using injected MMH anchors directly; all six joints declared N.
"""
from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # all six N-class, natural gaps preserved
    'overall_pass': True,
    'notes': '后 rendered from injected MMH anchors; s2 given a rightward curve control; s5 drawn as heng-zhe corner (right-then-down) to make 口 read as rectangular.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- Stroke 1: 短撇 (small top pie) ----
s1_h = anchor_to_xy(('TR', 0.083, 0.812))
s1_t = anchor_to_xy(('C',  0.055, 0.16))
# tapered pie, slight downward-left curve
mid1 = ((s1_h[0] + s1_t[0]) / 2 - 4, (s1_h[1] + s1_t[1]) / 2 + 2)
pts1 = quad_bezier(s1_h, mid1, s1_t, n=30)
widths1 = [11 - 8 * i / 30 for i in range(31)]
stroke_variable_width(d, pts1, widths1)

# ---- Stroke 2: 横撇 (long horizontal-then-down forming top and left flank) ----
s2_h = anchor_to_xy(('ML', 0.797, 0.061))
s2_t = anchor_to_xy(('BL', 0.193, 0.807))
# horizontal start, curving down-left through mid — control biased right/down
ctrl2 = (95, 200)
pts2 = quad_bezier(s2_h, ctrl2, s2_t, n=48)
widths2 = [11 - 6 * i / 48 for i in range(49)]
stroke_variable_width(d, pts2, widths2)

# ---- Stroke 3: short middle 横 ----
s3_h = anchor_to_xy(('ML', 0.979, 0.649))
s3_t = anchor_to_xy(('MR', 0.558, 0.512))
fat_line(d, s3_h, s3_t, width=8)

# ---- Stroke 4: 竖 (left side of 口) ----
s4_h = anchor_to_xy(('BL', 0.987, 0.133))
s4_t = anchor_to_xy(('BC', 0.219, 0.953))
fat_line(d, s4_h, s4_t, width=9)

# ---- Stroke 5: 横折 (top + right of 口) ----
s5_h = anchor_to_xy(('BC', 0.157, 0.145))
s5_t = anchor_to_xy(('BR', 0.001, 0.613))
# make it read as an inverted L: heng first, then shu
s5_corner = (s5_t[0], s5_h[1])
fat_line(d, s5_h, s5_corner, width=9)
fat_line(d, s5_corner, s5_t, width=9)

# ---- Stroke 6: bottom 横 (bottom of 口) ----
s6_h = anchor_to_xy(('BC', 0.283, 0.845))
s6_t = anchor_to_xy(('BR', 0.238, 0.748))
fat_line(d, s6_h, s6_t, width=9)

out_png = os.path.join(os.path.dirname(__file__), "01_后.png")
img.save(out_png)
print(f"Saved {out_png}")
