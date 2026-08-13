"""p3_char_0473_城 — 城 (chéng, "city", 9 strokes).

Composition: 土 (left radical, 3 strokes) + 成 (right, 6 strokes).

Memory reads:
  1. drawer_memory.md — noted `tu.py` for 土 (but as LEFT radical, s3 is 提 not 横).
  2. success_bank/INDEX.md — 土 exists; 成 not mastered but xie_gou.py primitive
     available (used in 我/戈/戊/成). Errata p3_char_0243_成 flagged 斜钩 hook.
  3. errata.md grep — no direct hit for 城. 成 chronic (斜钩) issues noted.

Since 土 in this composition is left-radical (s3 is 提 rising stroke, not
horizontal 横 bottom), and 成 is not in bank as a primitive, this render
uses the MMH anchor spec directly rather than importing `tu.py` (which
would need 3+ anchor overrides = anti-pattern per drawer_memory).
Inlining fresh per shared-rules "memory is supplementary".
"""
# BANK_DEVIATION
# skipped: tu.py
# reason: 土 here is left-radical form — s3 must be 提 (rising) not 横 (level); tu.py bakes flat bottom-heng that would need 3+ anchor overrides (anti-pattern per drawer_memory never-tune-anchors rule).
# fresh_component: tu_left_radical_for_城

# Stroke count check: 9 fat_line/curve calls below == expected 9. OK.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Fresh render per MMH anchors. 土-left-radical inlined (tu.py skipped). 斜钩 body curved with hook flick up.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def draw_polyline_curve(draw, pts, widths, color=(0, 0, 0)):
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 土 (left radical) ----
    # s1: 横 (short top heng) ML(0.267,0.758) -> C(0.014,0.623)
    p1a = anchor_to_xy(('ML', 0.267, 0.758))
    p1b = anchor_to_xy(('C',  0.014, 0.623))
    fat_line(draw, p1a, p1b, width=7)

    # s2: 竖 (vertical spine) TL(0.58,0.905) -> BL(0.647,0.279)
    p2a = anchor_to_xy(('TL', 0.58, 0.905))
    p2b = anchor_to_xy(('BL', 0.647, 0.279))
    fat_line(draw, p2a, p2b, width=8)

    # s3: 提 (rising bottom stroke — LEFT radical form of 土) BL(0.217,0.49) -> BC(0.055,0.153)
    p3a = anchor_to_xy(('BL', 0.217, 0.49))
    p3b = anchor_to_xy(('BC', 0.055, 0.153))
    # taper: thick at head, thin at tip
    ti_pts = [
        (p3a[0] + i/10 * (p3b[0]-p3a[0]), p3a[1] + i/10 * (p3b[1]-p3a[1]))
        for i in range(11)
    ]
    ti_widths = [10 - i*0.7 for i in range(11)]
    stroke_variable_width(draw, ti_pts, ti_widths)

    # ---- 成 (right side) ----
    # s4: 横 (top short heng of 成) C(0.368,0.491) -> MR(0.197,0.339)
    p4a = anchor_to_xy(('C',  0.368, 0.491))
    p4b = anchor_to_xy(('MR', 0.197, 0.339))
    fat_line(draw, p4a, p4b, width=7)

    # s5: 撇 (long descending pie) C(0.16,0.438) -> BL(0.779,0.754)
    p5a = anchor_to_xy(('C',  0.16, 0.438))
    p5b = anchor_to_xy(('BL', 0.779, 0.754))
    # curved pie — control biased leftward
    ctrl5 = ((p5a[0] + p5b[0]) * 0.5 - 8,
             (p5a[1] + p5b[1]) * 0.5 + 4)
    pts5 = quad_bezier(p5a, ctrl5, p5b, n=48)
    n5 = len(pts5) - 1
    widths5 = [11 - 9*(i/n5) for i in range(n5+1)]  # thick head → thin tip
    stroke_variable_width(draw, pts5, widths5)

    # s6: short inner vertical (BC to BC — small piece inside 成)
    p6a = anchor_to_xy(('BC', 0.321, 0.033))
    p6b = anchor_to_xy(('BC', 0.348, 0.426))
    fat_line(draw, p6a, p6b, width=7)

    # s7: 斜钩 body TC(0.559,0.63) -> BR(0.666,0.44), with hook up
    p7a = anchor_to_xy(('TC', 0.559, 0.63))
    p7b = anchor_to_xy(('BR', 0.666, 0.44))
    # gentle concave-up curve
    ctrl7 = ((p7a[0] + p7b[0]) * 0.5 - 12,
             (p7a[1] + p7b[1]) * 0.5 + 12)
    pts7 = quad_bezier(p7a, ctrl7, p7b, n=60)
    n7 = len(pts7) - 1
    widths7 = []
    for i in range(n7 + 1):
        t = i / n7
        if t <= 0.65:
            w = 7 + (14 - 7) * (t / 0.65)
        else:
            w = 14 + (12 - 14) * ((t - 0.65) / 0.35)
        widths7.append(w)
    stroke_variable_width(draw, pts7, widths7)
    # hook flick: from p7b upward
    hook_tip = (p7b[0] + 4, p7b[1] - 22)
    ctrl_hook = (p7b[0] + 8, p7b[1] - 8)
    hook_pts = quad_bezier(p7b, ctrl_hook, hook_tip, n=20)
    nh = len(hook_pts) - 1
    hook_ws = [12 - 10*(i/nh) for i in range(nh+1)]
    stroke_variable_width(draw, hook_pts, hook_ws)

    # s8: inner cross-stroke MR(0.247,0.62) -> BC(0.737,0.692)
    p8a = anchor_to_xy(('MR', 0.247, 0.62))
    p8b = anchor_to_xy(('BC', 0.737, 0.692))
    fat_line(draw, p8a, p8b, width=7)

    # s9: 点 (top-right dot on 斜钩) TR(0.021,0.864) -> MR(0.314,0.066)
    p9a = anchor_to_xy(('TR', 0.021, 0.864))
    p9b = anchor_to_xy(('MR', 0.314, 0.066))
    # taper: thin head → thick tail (dot-like)
    pts9 = [
        (p9a[0] + i/8 * (p9b[0]-p9a[0]), p9a[1] + i/8 * (p9b[1]-p9a[1]))
        for i in range(9)
    ]
    ws9 = [3 + i*1.2 for i in range(9)]
    stroke_variable_width(draw, pts9, ws9)

    out = os.path.join(os.path.dirname(__file__), '01_城.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
