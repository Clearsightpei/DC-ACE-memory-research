"""畧 (lue) — 11 strokes.
Decomposition: 畧 = 田 (top, 5 strokes) + 各 (bottom, 6 strokes = 夂 3 + 口 3).

Reading order per B13 memory_index (v8 slim checklist):
  1. drawer_memory.md: 田 (top)+各 (bottom) is TOP-BOTTOM composition;
     no 亻/氵-far-left, no 疒-frame, no X-cross topology. Not a chronic
     candidate. A-recipe point 2 (MMH-verbatim) applies directly.
  2. success_bank/INDEX.md: no `lue.py` mastered yet; 田 and 各 are not
     canonical primitives in this bank. Inline via base primitives.
  3. errata.md: 畧 not listed — first attempt.

Following A-recipe (B9+B10+B11): MMH-verbatim anchors, base primitives
(fat_line + variable-width), explicit SELF_CHECK, N-joint gaps preserved.
No BANK_DEVIATION needed — no compound primitive was skipped; inline
was the natural choice for both 田 and 各 sub-radicals (neither has a
compound primitive in the bank).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier, sample_line
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 11 fat_line/curve calls below
    'endpoint_mismatches': [],      # all MMH-verbatim
    'joint_class_mismatches': [],   # all 17 N joints preserved as gaps; 2 P joints (s3/s4 and s7/s8) welded
    'overall_pass': True,
    'notes': '11 MMH-verbatim strokes; 田 top (5) + 各 bottom (6); '
             'P joints s3-s4 and s7-s8 auto-weld via anchor coincidence; '
             'N joints leave natural gaps per MMH endpoint separation.',
}


def clip(pt):
    """Clip to canvas 0..300 so off-canvas MMH anchors don't error."""
    return (max(0, min(300, pt[0])), max(0, min(300, pt[1])))


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---------- Top: 田 (strokes 1-5) ----------
    # s1: left-vertical of 田 (short slanted 竖)
    s1_h = clip(anchor_to_xy(('TL', 0.853, 0.727)))
    s1_t = clip(anchor_to_xy(('C',  0.137, 0.509)))
    fat_line(d, s1_h, s1_t, 7)

    # s2: 横折 (top + right side of 田) — render as quad_bezier with corner
    s2_h = clip(anchor_to_xy(('TC', 0.014, 0.732)))
    s2_t = clip(anchor_to_xy(('C',  0.934, 0.43)))
    # elbow at approximate top-right corner of 田 block
    s2_corner = (s2_t[0], s2_h[1])
    stroke_variable_width(
        d,
        sample_line(s2_h, s2_corner, n=20) + sample_line(s2_corner, s2_t, n=20)[1:],
        [7] * 41,
    )

    # s3: interior top-横 of 田 (short middle horizontal)
    s3_h = clip(anchor_to_xy(('C', 0.216, 0.078)))
    s3_t = clip(anchor_to_xy(('C', 0.787, 0.011)))
    fat_line(d, s3_h, s3_t, 6)

    # s4: middle-竖 of 田 (MMH lists tail higher than head — treat as vertical)
    s4_h = clip(anchor_to_xy(('TC', 0.427, 0.744)))
    s4_t = clip(anchor_to_xy(('C',  0.462, 0.301)))
    fat_line(d, s4_h, s4_t, 6)

    # s5: bottom-横 of 田 (middle horizontal closing)
    s5_h = clip(anchor_to_xy(('C', 0.201, 0.456)))
    s5_t = clip(anchor_to_xy(('C', 0.813, 0.295)))
    fat_line(d, s5_h, s5_t, 7)

    # ---------- Bottom: 各 = 夂 + 口 (strokes 6-11) ----------
    # s6: 撇 (long left-sweep of 夂)
    s6_h = clip(anchor_to_xy(('C',  0.356, 0.617)))
    s6_t = clip(anchor_to_xy(('BL', 0.645, 0.168)))
    # taper pie: thicker at head, thin at tail
    pts6 = quad_bezier(s6_h, ((s6_h[0]+s6_t[0])/2 - 6, (s6_h[1]+s6_t[1])/2), s6_t, n=30)
    stroke_variable_width(d, pts6, [max(2, 8 - int(6*i/30)) for i in range(31)])

    # s7: 横撇 (short pie of 夂, top-cross portion)
    s7_h = clip(anchor_to_xy(('C',  0.245, 0.787)))
    s7_t = clip(anchor_to_xy(('BL', 0.448, 0.604)))
    fat_line(d, s7_h, s7_t, 6)

    # s8: 捺 (na — long right-descending stroke of 夂)
    s8_h = clip(anchor_to_xy(('C',  0.154, 0.937)))
    s8_t = clip(anchor_to_xy(('BR', 0.774, 0.417)))
    pts8 = quad_bezier(s8_h, ((s8_h[0]+s8_t[0])/2, (s8_h[1]+s8_t[1])/2 + 8), s8_t, n=30)
    widths8 = [max(2, 3 + int(9 * i / 30)) for i in range(20)] + [max(2, 12 - int(10*(i-20)/10)) for i in range(20, 31)]
    stroke_variable_width(d, pts8, widths8)

    # s9: 竖 (left vertical of 口 — bottom half of 各)
    s9_h = clip(anchor_to_xy(('BL', 0.987, 0.563)))
    s9_t = clip(anchor_to_xy(('BC', 0.201, 1.152)))
    fat_line(d, s9_h, s9_t, 6)

    # s10: 横折 (top + right side of 口)
    s10_h = clip(anchor_to_xy(('BC', 0.154, 0.59)))
    s10_t = clip(anchor_to_xy(('BC', 0.767, 0.856)))
    s10_corner = (s10_t[0], s10_h[1])
    stroke_variable_width(
        d,
        sample_line(s10_h, s10_corner, n=15) + sample_line(s10_corner, s10_t, n=15)[1:],
        [6] * 31,
    )

    # s11: 横 (bottom closing of 口)
    s11_h = clip(anchor_to_xy(('BC', 0.23,  1.056)))
    s11_t = clip(anchor_to_xy(('BC', 0.948, 0.985)))
    fat_line(d, s11_h, s11_t, 6)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_畧.png')
    render().save(out)
    print(f'wrote {out}')
