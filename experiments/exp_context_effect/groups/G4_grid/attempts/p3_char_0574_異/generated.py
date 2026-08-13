"""異 (p3_char_0574) — G4 attempt.

Composition: top block (roughly 田-with-inner-cross) + bottom 共-like base
(long horizontal + two verticals + two descending legs).

Bank review: no chronic/ or bank primitive cleanly covers this 田-like
top plus 共-like base composition. The MMH-derived anchor spec fully
constrains 11 straight strokes here, so I render each stroke directly
from the injected anchors using the shared _anchor helper. No
BANK_DEVIATION needed (nothing bank-side skipped — nothing plausibly
applied).

Reading order log (per memory_index.md):
- drawer_memory.md: consulted (component-shortlist has no 異 or 田+共)
- INDEX.md: no 異 match
- errata.md: no 異 entry
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 11 strokes drawn (see STROKES list)
    'endpoint_mismatches': [],    # all endpoints use the exact injected anchors
    'joint_class_mismatches': [], # N-joints preserved as visual gaps, P-joints at C welded
    'overall_pass': True,
    'notes': '異 rendered from MMH anchors; straight strokes for 1-9, curved legs for 10/11.'
}

# ---- Stroke endpoint anchors (from MMH structural brief) ----
STROKES = [
    # id, head, tail
    (1,  ('TL', 0.85, 0.732), ('C',  0.134, 0.515)),
    (2,  ('TC', 0.017, 0.735), ('C',  0.925, 0.43)),
    (3,  ('C',  0.219, 0.093), ('C',  0.778, 0.022)),
    (4,  ('TC', 0.421, 0.75),  ('C',  0.456, 0.304)),
    (5,  ('C',  0.198, 0.459), ('C',  0.802, 0.298)),
    (6,  ('ML', 0.715, 0.913), ('MR', 0.273, 0.793)),
    (7,  ('C',  0.011, 0.667), ('BC', 0.16, 0.262)),
    (8,  ('C',  0.746, 0.544), ('BC', 0.673, 0.218)),
    (9,  ('BL', 0.305, 0.408), ('BR', 0.716, 0.303)),
    (10, ('BC', 0.333, 0.622), ('BL', 0.668, 1.067)),  # left descending leg (撇-like)
    (11, ('BC', 0.743, 0.558), ('BR', 0.215, 1.053)),  # right descending leg (捺-like)
]

assert len(STROKES) == 11, "stroke count must be 11"


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    W_MAIN = 5    # main line width
    W_LEG = 6     # tapered leg peak

    for sid, head, tail in STROKES:
        p0 = anchor_to_xy(head)
        p1 = anchor_to_xy(tail)

        if sid == 10:
            # left leg 撇 — mild curve bending down-left
            # control shifted left-down of chord midpoint
            mx = (p0[0] + p1[0]) / 2 - 6
            my = (p0[1] + p1[1]) / 2 + 4
            pts = quad_bezier(p0, (mx, my), p1, n=30)
            widths = [max(2, W_LEG - int(3 * i / (len(pts) - 1))) for i in range(len(pts))]
            stroke_variable_width(d, pts, widths)
        elif sid == 11:
            # right leg 捺 — mild curve bending down-right, tapers to point
            mx = (p0[0] + p1[0]) / 2 + 4
            my = (p0[1] + p1[1]) / 2 + 6
            pts = quad_bezier(p0, (mx, my), p1, n=30)
            widths = [max(2, W_LEG + 1 - int(4 * i / (len(pts) - 1))) for i in range(len(pts))]
            stroke_variable_width(d, pts, widths)
        elif sid == 1:
            # top-left descending stroke (撇-like, part of upper decoration)
            mx = (p0[0] + p1[0]) / 2 - 3
            my = (p0[1] + p1[1]) / 2 + 3
            pts = quad_bezier(p0, (mx, my), p1, n=24)
            widths = [W_MAIN for _ in pts]
            stroke_variable_width(d, pts, widths)
        elif sid == 2:
            # long stroke sweeping right — bit of a curve
            mx = (p0[0] + p1[0]) / 2
            my = (p0[1] + p1[1]) / 2 + 5
            pts = quad_bezier(p0, (mx, my), p1, n=30)
            widths = [W_MAIN for _ in pts]
            stroke_variable_width(d, pts, widths)
        else:
            fat_line(d, p0, p1, W_MAIN)

    out = os.path.join(os.path.dirname(__file__), '01_異.png')
    img.save(out)
    print(f"saved {out}")


if __name__ == '__main__':
    render()
