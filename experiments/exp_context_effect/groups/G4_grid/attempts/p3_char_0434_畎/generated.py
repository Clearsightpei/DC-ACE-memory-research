"""p3_char_0434_畎 — 畎 (quǎn), 9 strokes.

Memory lookups (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — B9/B10/B11 A-recipe: explicit decomposition +
     MMH-verbatim anchors + inline base primitives when compound
     primitives don't fit slot. Classic 2-radical left-right compound:
     田 far-left column + 犬 right-half. Sibling 畋 (also 田+X-right)
     used inline; follow that pattern.
  2. success_bank/INDEX.md — no `tian.py` (bank has only 申/甴/畀/果/畋
     which all INLINE 田). `quan.py` exists for standalone 犬 but its
     defaults are full-canvas — MMH here compresses 犬 into right-half
     with 撇 sweeping down-left across canvas. Compound-slot embedding
     ⇒ SKIP quan.py, inline via base primitives (BANK_DEVIATION below).
  3. errata.md — 畎 not listed.

Decomposition: 畎 = 田 (left, 5 strokes) + 犬 (right, 4 strokes).
  田 (s1-s5): shu-left + heng-zhe (top+right wall) + inner heng
              + inner shu + bottom heng. (Note: MMH gives s3=inner
              heng, s5=bottom heng.)
  犬 (s6-s9): heng + long-pie + na + top-right dian, with s6/s7
              welded P-cross at C(0.747, 0.764).
"""

# BANK_DEVIATION
# skipped: quan.py
# reason: 犬 sits in right-half slot with pie sweeping across canvas
#   (head TC, tail BL) — quan.py bakes standalone full-canvas 犬 anchors.
#   Per B10/B11 A-recipe point 4/7: inline via base primitives with
#   MMH-verbatim anchors preserves compositional proportion.
# fresh_component: quan_right_half_for_田-compound

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim: 田 (s1-s5, left column) + 犬 '
              '(s6-s9, right half). Inner 田 cross (s3⇆s4) welded via '
              'draw-order + emphasis disc. 犬 heng×pie (s6⇆s7) welded '
              'at C via computed intersection. N-gaps preserved at all '
              '田 corners and 犬 non-welded joints.'),
}

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian


def _shorten(pt, other, px):
    """Return `pt` moved `px` pixels toward `other`."""
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


# ==== 田 anchors (MMH-verbatim) ====
S1_H = ('ML', 0.188, 0.485); S1_T = ('BL', 0.401, 0.464)   # left vertical
S2_H = ('ML', 0.319, 0.491); S2_T = ('BC', 0.04,  0.405)   # top-heng + right-wall (heng-zhe)
S3_H = ('ML', 0.469, 0.957); S3_T = ('ML', 0.938, 0.89)    # inner middle heng
S4_H = ('ML', 0.642, 0.512); S4_T = ('BL', 0.659, 0.265)   # inner middle shu
S5_H = ('BL', 0.463, 0.42);  S5_T = ('BL', 0.92,  0.303)   # bottom heng

# ==== 犬 anchors (MMH-verbatim) ====
S6_H = ('C',  0.28,  0.825); S6_T = ('MR', 0.546, 0.705)   # heng of 大
S7_H = ('TC', 0.644, 0.694); S7_T = ('BL', 0.961, 0.944)   # long pie sweeping down-left
S8_H = ('C',  0.813, 0.983); S8_T = ('BR', 0.836, 0.877)   # na down-right
S9_H = ('TR', 0.104, 0.987); S9_T = ('MR', 0.44,  0.277)   # dian at top-right


def draw_tian(draw):
    """Draw 田 on the left (5 strokes)."""
    p1h = anchor_to_xy(S1_H); p1t = anchor_to_xy(S1_T)
    p2h = anchor_to_xy(S2_H); p2t = anchor_to_xy(S2_T)
    p3h = anchor_to_xy(S3_H); p3t = anchor_to_xy(S3_T)
    p4h = anchor_to_xy(S4_H); p4t = anchor_to_xy(S4_T)
    p5h = anchor_to_xy(S5_H); p5t = anchor_to_xy(S5_T)

    # Corner for heng-zhe (top-right of 田 frame)
    corner = (p2t[0], p2h[1])

    w = 7
    gap = 4

    # s1: left vertical
    fat_line(draw, _shorten(p1h, p1t, gap), p1t, width=w)
    # s2: top heng + right wall (heng-zhe), drawn as two segments
    fat_line(draw, p2h, corner, width=w)
    fat_line(draw, corner, _shorten(p2t, corner, gap), width=w)
    cx, cy = corner; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3: inner middle heng (P-welded through by s4 later)
    fat_line(draw, p3h, p3t, width=w)
    # s4: inner middle shu (drawn after s3 so P-cross weld is clean)
    fat_line(draw, p4h, p4t, width=w)
    # emphasis at the P-cross
    icx = (p3h[0] + p3t[0]) / 2
    icy = (p4h[1] + p4t[1]) / 2
    draw.ellipse([icx - 4, icy - 4, icx + 4, icy + 4], fill=(0, 0, 0))

    # s5: bottom heng
    fat_line(draw, _shorten(p5h, p5t, 2), _shorten(p5t, p5h, 2), width=w)


def draw_quan(draw):
    """Draw 犬 on the right (4 strokes)."""
    # s6: heng (top horizontal of 大)
    draw_heng(draw, from_anchor=S6_H, to_anchor=S6_T, width=7)

    # s7: long pie (down-left sweep) — DRAWN AFTER heng so P-weld reads clean
    draw_pie(draw, from_anchor=S7_H, to_anchor=S7_T,
             head_width=11, tail_width=2, curve=0.10, segments=56)

    # s8: na (down-right sweep)
    draw_na(draw, from_anchor=S8_H, to_anchor=S8_T,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.75, curve=0.08, segments=48)

    # Emphasis at the P-cross of s6 × s7 (~ C(0.747, 0.764))
    p6h = anchor_to_xy(S6_H); p6t = anchor_to_xy(S6_T)
    p7h = anchor_to_xy(S7_H); p7t = anchor_to_xy(S7_T)
    x1, y1 = p6h; x2, y2 = p6t; x3, y3 = p7h; x4, y4 = p7t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) > 1e-6:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        cx = x1 + t * (x2 - x1); cy = y1 + t * (y2 - y1)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(0, 0, 0))

    # s9: dian at top-right — draw LAST (per drawer_memory: dots dropped
    # first are drawn last defensively)
    draw_dian(draw, from_anchor=S9_H, to_anchor=S9_T,
              head_width=2, peak_width=10, curve=0.08, segments=24)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_tian(d)
    draw_quan(d)
    out = os.path.join(_HERE, '01_畎.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
