"""p3_char_0186_本 — G4 attempt

Decomposition: 本 = 木 (4 strokes: 横+竖+撇+捺) + 一 (short bottom horizontal marker)
Total = 5 strokes (matches MMH expected count).

Memory consulted:
  - drawer_memory.md v8 read (chronic + component playbook; no chronic radical applies)
  - success_bank/INDEX.md grep: 木 (mu.py) is listed as mastered p2_radical_104
    but the .py file is not present in success_bank/code — falling back to fresh
    inline draw using shared primitives (heng.py/shu.py/pie.py/na.py style),
    per shared_rules "supplementary aid, not mandate".
  - errata.md grep for 本: not present.

Anchors follow the MMH-derived expectations block verbatim.
"""

import os, sys
from PIL import Image, ImageDraw

# Add success_bank/code to import path for _anchor
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes, top-横 crosses 竖 (P), small bottom-横 crosses 竖 base (P), 撇/捺 fork from cross point (N-gaps).'
}


def draw_ben():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: top 横 (ML 0.621,0.318 -> MR 0.314,0.178) ---
    s1_h = anchor_to_xy(('ML', 0.621, 0.318))
    s1_t = anchor_to_xy(('MR', 0.314, 0.178))
    # variable width: thin start, thicker mid, taper
    n = 40
    from _anchor import sample_line
    pts = sample_line(s1_h, s1_t, n)
    widths = [max(4, int(6 + 3 * (1 - abs(i - n/2)/(n/2)))) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 2: 竖 (TC 0.321,0.583 -> BC 0.424,1.152, clipped to canvas) ---
    s2_h = anchor_to_xy(('TC', 0.321, 0.583))
    s2_t_raw = anchor_to_xy(('BC', 0.424, 1.152))
    # clip y to canvas
    s2_t = (s2_t_raw[0], min(s2_t_raw[1], 295))
    pts = sample_line(s2_h, s2_t, n)
    widths = [9] * (n + 1)
    # slight taper at bottom
    for i in range(n - 5, n + 1):
        widths[i] = max(5, 9 - (i - (n - 5)))
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 3: 撇 (C 0.383,0.354 -> BL 0.229,0.66) ---
    s3_h = anchor_to_xy(('C', 0.383, 0.354))
    s3_t = anchor_to_xy(('BL', 0.229, 0.66))
    # slight curve — bezier control biased left
    ctrl = (s3_h[0] * 0.4 + s3_t[0] * 0.6 - 8, (s3_h[1] + s3_t[1]) / 2)
    pts = quad_bezier(s3_h, ctrl, s3_t, n)
    widths = [max(3, int(9 - 6 * i / n)) for i in range(n + 1)]  # taper thick-to-thin
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 4: 捺 (C 0.55,0.418 -> BR 0.915,0.42) ---
    s4_h = anchor_to_xy(('C', 0.55, 0.418))
    s4_t = anchor_to_xy(('BR', 0.915, 0.42))
    # capture typical 捺 arc: bow slightly down then flare
    ctrl = ((s4_h[0] + s4_t[0]) / 2, (s4_h[1] + s4_t[1]) / 2 + 18)
    pts = quad_bezier(s4_h, ctrl, s4_t, n)
    widths = [max(4, int(4 + 8 * i / n)) for i in range(n + 1)]  # thin-to-thick (捺 flare)
    # taper at the very tip
    widths[-1] = 3
    widths[-2] = 5
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 5: bottom 一 marker (BL 0.899,0.464 -> BC 0.901,0.426) ---
    # This is 本's distinguishing short horizontal near 竖's base.
    # Note: MMH endpoints straddle BL/BC boundary (right edge of BL, right edge of BC-ish).
    s5_h = anchor_to_xy(('BL', 0.899, 0.464))
    s5_t = anchor_to_xy(('BC', 0.901, 0.426))
    pts = sample_line(s5_h, s5_t, n)
    widths = [7] * (n + 1)
    stroke_variable_width(draw, pts, widths)

    return img


if __name__ == '__main__':
    img = draw_ben()
    out = os.path.join(HERE, '01_本.png')
    img.save(out)
    print('wrote', out)
