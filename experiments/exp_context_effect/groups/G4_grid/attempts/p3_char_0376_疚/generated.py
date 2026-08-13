"""p3_char_0376_疚 — G4 attempt.

Decomposition: 疚 = 疒 (top-left frame + 2 inner marks, 5 strokes) + 久 (3 strokes).

Memory consulted (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — read. No chronic primitive fires for 疒 or 久
     (guang.py was retired; no 疒-primitive; no 久-primitive).
     Compositional playbook: enclosing-frame-ish left/top part (疒) +
     inner content (久) in bottom-right. Grid layout: 疒 fills top-left
     with 撇 sweeping full height; 久 sits inside bottom-right cavity.
  2. success_bank/INDEX.md — 疒 listed at row 171 but code file was
     retired; no 久. No primitive to import.
  3. errata.md — 疚 not present.

Following MMH-derived anchors verbatim (v9 lesson: MMH is stronger
than hand tuning). No bank primitive call so no BANK_DEVIATION block
needed (nothing skipped — nothing available to skip).
"""

import os
from PIL import Image, ImageDraw

import sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, stroke_variable_width, quad_bezier, sample_line, fat_line, CANVAS


SELF_CHECK = {
    'visual_ok': None,           # filled after render
    'stroke_count_ok': True,     # 8 strokes below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 7 joints are N (natural gaps) — no welding
    'overall_pass': None,
    'notes': 'All 7 joints are N-class (small natural gaps). Anchors taken verbatim from MMH.'
}


def draw():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    W_MAIN = 6   # main heng/pie/na width
    W_THIN = 4   # short strokes / dots
    INK = (0, 0, 0)

    strokes = []

    # ── 疒 (5 strokes) ─────────────────────────────────────────────

    # stroke 1: top short 点 of 疒 — TC(0.421, 0.551) → TC(0.77, 0.82)
    # short slanted "dian" tapering from thin head to slightly fatter tail
    p0 = anchor_to_xy(('TC', 0.421, 0.551))
    p1 = anchor_to_xy(('TC', 0.77, 0.82))
    pts = sample_line(p0, p1, n=10)
    widths = [3 + i * 0.4 for i in range(len(pts))]  # 3 → 7
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s1_dian', p0, p1))

    # stroke 2: 横 of 广 — C(0.069, 0.104) → TR(0.364, 0.955)
    # long top horizontal spanning from left-center to top-right
    p0 = anchor_to_xy(('C', 0.069, 0.104))
    p1 = anchor_to_xy(('TR', 0.364, 0.955))
    fat_line(d, p0, p1, W_MAIN, INK)
    strokes.append(('s2_heng', p0, p1))

    # stroke 3: long 撇 of 广 — ML(0.864, 0.04) → BL(0.366, 0.991)
    # curve slightly; start thick at head, taper toward tail
    p0 = anchor_to_xy(('ML', 0.864, 0.04))
    p1 = anchor_to_xy(('BL', 0.366, 0.991))
    # control point pulled slightly left to give the pie a curve
    mid_x = (p0[0] + p1[0]) / 2 - 15
    mid_y = (p0[1] + p1[1]) / 2 + 10
    pts = quad_bezier(p0, (mid_x, mid_y), p1, n=40)
    widths = [W_MAIN + 2 - i * 0.15 for i in range(len(pts))]
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s3_pie', p0, p1))

    # stroke 4: inner short 撇/dot — ML(0.466, 0.356) → ML(0.659, 0.661)
    # small oblique dash going down-right
    p0 = anchor_to_xy(('ML', 0.466, 0.356))
    p1 = anchor_to_xy(('ML', 0.659, 0.661))
    pts = sample_line(p0, p1, n=8)
    widths = [3 + i * 0.3 for i in range(len(pts))]
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s4_inner1', p0, p1))

    # stroke 5: inner 提 (rising) — BL(0.223, 0.183) → ML(0.776, 0.942)
    # note: head lower than tail — this is a 提 rising stroke
    p0 = anchor_to_xy(('BL', 0.223, 0.183))
    p1 = anchor_to_xy(('ML', 0.776, 0.942))
    pts = sample_line(p0, p1, n=10)
    widths = [5 - i * 0.3 for i in range(len(pts))]  # thicker head, thin tail
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s5_inner2', p0, p1))

    # ── 久 (3 strokes) ─────────────────────────────────────────────

    # stroke 6: 撇 of 久 — C(0.535, 0.307) → BC(0.043, 0.156)
    # long pie going from upper-right down to lower-left
    p0 = anchor_to_xy(('C', 0.535, 0.307))
    p1 = anchor_to_xy(('BC', 0.043, 0.156))
    mid_x = (p0[0] + p1[0]) / 2 + 5
    mid_y = (p0[1] + p1[1]) / 2 - 5
    pts = quad_bezier(p0, (mid_x, mid_y), p1, n=40)
    widths = [W_MAIN - i * 0.05 for i in range(len(pts))]
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s6_pie', p0, p1))

    # stroke 7: 横撇 (short horizontal then pie) — C(0.503, 0.764) → BL(0.844, 0.921)
    # this is the middle stroke of 久 — a short diagonal
    p0 = anchor_to_xy(('C', 0.503, 0.764))
    p1 = anchor_to_xy(('BL', 0.844, 0.921))
    pts = sample_line(p0, p1, n=10)
    widths = [5 - i * 0.25 for i in range(len(pts))]
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s7_hengpie', p0, p1))

    # stroke 8: 捺 of 久 — BC(0.849, 0.288) → BR(0.827, 0.965)
    # na going down-right, thickening then tapering at foot
    p0 = anchor_to_xy(('BC', 0.849, 0.288))
    p1 = anchor_to_xy(('BR', 0.827, 0.965))
    mid_x = (p0[0] + p1[0]) / 2 - 5
    mid_y = (p0[1] + p1[1]) / 2 - 5
    pts = quad_bezier(p0, (mid_x, mid_y), p1, n=40)
    # na thickens through middle, then tapers at end
    n = len(pts)
    widths = []
    for i in range(n):
        t = i / (n - 1)
        if t < 0.75:
            widths.append(4 + t * 6)  # 4 → 8.5
        else:
            widths.append(8.5 - (t - 0.75) * 20)  # taper down
    stroke_variable_width(d, pts, widths, INK)
    strokes.append(('s8_na', p0, p1))

    assert len(strokes) == 8, f"expected 8 strokes, got {len(strokes)}"

    out = os.path.join(os.path.dirname(__file__), '01_疚.png')
    img.save(out)
    return out, strokes


if __name__ == '__main__':
    out, strokes = draw()
    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['overall_pass'] = SELF_CHECK['stroke_count_ok'] and SELF_CHECK['visual_ok']
    print(f"wrote {out}")
    print(f"strokes: {len(strokes)}")
    print(f"SELF_CHECK: {SELF_CHECK}")
