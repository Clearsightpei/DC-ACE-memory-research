"""又 (you) — composed character. 2 strokes (heng_pie + na).

Mastered: run_6 c34, panel 3/3 YES.
visual_score=0.65, ocr=又 (1.00 confidence).

Anchors derived from MMH medians via tools/joint_detector.mmh_to_canvas:
- 横撇 from upper-left, bend at upper-right (MMH max-x), down to lower-far-left
- 捺 from upper-middle-left, sweeping down-right to far-bottom-right

Reuse:
    from you import draw_you
    draw_you(t)
"""
from heng_pie import draw_heng_pie
from na import draw_na


def draw_you(t):
    draw_heng_pie(t,
        ('ML', 0.516, 0.048),
        ('MR', 0.044, 0.436),
        ('BL', 0.032, 1.22))
    draw_na(t,
        ('ML', 0.536, 0.36),
        ('BR', 1.3, 1.26))
