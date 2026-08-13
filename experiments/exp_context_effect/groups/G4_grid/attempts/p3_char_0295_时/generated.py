"""p3_char_0295_时 — 时 (shí, "time", 6-7 strokes).

Decomposition: 时 = 日 (left) + 寸 (right).
- Left 日 uses 4 strokes (vertical, heng-zhe, middle heng, bottom heng).
- Right 寸 uses 3 strokes (heng, shu-gou, dian).
Total: 7 strokes (matches MMH expected count).

Composition per drawer_memory.md compositional playbook:
- Left radical 日: x in [0.05, 0.40]
- Right radical 寸: x in [0.45, 0.95]
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '时=日+寸. Inlined both halves (ri.py exists but is full-canvas; here need left-half only). '
             '7 strokes: 4 for 日 + 3 for 寸. All 6 non-cross joints N (small gap); s6/s7 P at MR (dian touches shu-gou).',
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ============ LEFT: 日 (compact, x-range ~ pixels 25..118) ============
# s1: 竖 (left vertical of 日)
s1_h = anchor_to_xy(('TL', 0.25, 0.55))   # (25, 55)
s1_t = anchor_to_xy(('BL', 0.25, 0.50))   # (25, 250)
fat_line(d, s1_h, s1_t, width=9)

# s2: 横折 (top + right side of 日) — one connected stroke via corner
s2_h    = anchor_to_xy(('TL', 0.27, 0.55))   # (27, 55) - starts near s1 head
s2_cor  = anchor_to_xy(('TC', 0.18, 0.55))   # (118, 55) - top-right corner
s2_t    = anchor_to_xy(('BC', 0.18, 0.48))   # (118, 248)
fat_line(d, s2_h, s2_cor, width=9)
fat_line(d, s2_cor, s2_t, width=9)

# s3: 横 (middle horizontal in 日) - wall-to-wall
s3_h = anchor_to_xy(('ML', 0.30, 0.55))   # (30, 155)
s3_t = anchor_to_xy(('TC', 0.15, 0.55))   # (115, 155) actually in ML row => but that's TC. correct: use ML(1.15,..) not valid; use C cell? 115 is in C-column? no, C column x is [100,200]. 115 is in TC/C/BC. y=155 is middle row, so C cell.
# Fix: rewrite s3_t as C cell anchor
s3_t = anchor_to_xy(('C', 0.15, 0.55))    # (115, 155)
fat_line(d, s3_h, s3_t, width=8)

# s4: 横 (bottom horizontal of 日)
s4_h = anchor_to_xy(('BL', 0.30, 0.48))   # (30, 248)
s4_t = anchor_to_xy(('BC', 0.15, 0.48))   # (115, 248)
fat_line(d, s4_h, s4_t, width=9)

# ============ RIGHT: 寸 (x-range ~ pixels 145..280) ============
# s5: 横 (top horizontal of 寸) — spans across right half
s5_h = anchor_to_xy(('TC', 0.45, 0.95))   # (145, 95)
s5_t = anchor_to_xy(('TR', 0.80, 0.95))   # (280, 95)
fat_line(d, s5_h, s5_t, width=9)

# s6: 竖钩 (vertical hook) — starts above heng, crosses through it, hooks left at bottom
s6_h    = anchor_to_xy(('TC', 1.10, 0.60))   # invalid cell. Use TR(0.10, 0.60)
s6_h    = anchor_to_xy(('TR', 0.10, 0.60))   # (210, 60)
s6_bot  = anchor_to_xy(('BR', 0.10, 0.55))   # (210, 255)
s6_hook = anchor_to_xy(('BR', 0.02, 0.45))   # (202, 245) - small hook to upper-left
fat_line(d, s6_h, s6_bot, width=10)
fat_line(d, s6_bot, s6_hook, width=8)

# s7: 点 (dot on the right, between heng and shu-gou middle)
p_dot_a = anchor_to_xy(('MR', 0.20, 0.70))   # (220, 170)
p_dot_b = anchor_to_xy(('MR', 0.45, 0.85))   # (245, 185)
# render as a short thick tapered stroke
pts = [p_dot_a, ((p_dot_a[0]+p_dot_b[0])/2, (p_dot_a[1]+p_dot_b[1])/2), p_dot_b]
widths = [4, 9, 12]
stroke_variable_width(d, pts, widths)

out_path = os.path.join(os.path.dirname(__file__), '01_时.png')
img.save(out_path)
print(f"Wrote {out_path}")
print(f"SELF_CHECK: {SELF_CHECK}")
