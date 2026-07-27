"""灬 (huǒ, "four-dot fire", 4 strokes) — B2 pass.

Bottom radical. Four slender 点 dots along the B-row. s1 and s4 are the
outer pair (both slant DOWN-LEFT — mirror direction). s2 and s3 are
narrower and more vertical.

Strokes: 4 × 点, peak_w=5–7 (narrower than a standalone 点).

Joints: NONE (all separate, S-class).
"""
from dian import draw_dian


def draw_huo_four(draw,
                  s1_head=('ML', 0.677, 0.708), s1_tail=('BL', 0.504, 0.206),
                  s2_head=('C',  0.069, 0.72),  s2_tail=('BC', 0.225, 0.033),
                  s3_head=('C',  0.544, 0.708), s3_tail=('C',  0.729, 0.989),
                  s4_head=('MR', 0.092, 0.69),  s4_tail=('BR', 0.52, 0.194)):
    draw_dian(draw, s1_head, s1_tail, head_width=1, peak_width=6, curve=0.05)
    draw_dian(draw, s2_head, s2_tail, head_width=1, peak_width=5, curve=0.05)
    draw_dian(draw, s3_head, s3_tail, head_width=1, peak_width=5, curve=0.05)
    draw_dian(draw, s4_head, s4_tail, head_width=1, peak_width=7, curve=0.06)
