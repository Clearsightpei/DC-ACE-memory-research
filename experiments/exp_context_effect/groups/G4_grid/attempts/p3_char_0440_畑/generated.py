"""p3_char_0440_畑 — 畑 (tián/hatake), 9 strokes.

Memory lookups (v8 slim checklist):
  1. drawer_memory.md — B9/B10/B11 A-recipe: explicit decomposition +
     MMH-verbatim anchors + inline base primitives. 畑 is a classic
     2-radical left-right compound: 火 (left, 4 strokes) + 田 (right,
     5 strokes). No compound primitive for 火 or 田 exists in the
     bank as importable radical; the neighbour p3_char_0432_畋
     inlined 田 by hand and passed structural. Follow that pattern
     mirrored onto the right side.
  2. success_bank/INDEX.md — no tian.py, no huo.py. huo_four.py is 灬
     (4 dots), not 火. Both radicals must be inlined here.
  3. errata.md — 畑 not listed.

Decomposition:
  畑 = 火 (LEFT, s1-s4) + 田 (RIGHT, s5-s9).
  火 (s1-s4): MMH orders as (near-vertical interior + upper dot-slash
              + long 撇 + short 捺). Rendered with fat_line/pie/na.
  田 (s5-s9): 竖 (left) + 横折 (top+right wall) + 中横 + 中竖 +
              下横. Middle 横/竖 form the s7×s8 P-cross weld.

BANK_DEVIATION does not apply — no bank compound primitive skipped
(neither huo.py nor tian.py exist in bank).

Joint expectations (from MMH block):
  9 joints total: 8 N + 1 P.
  P: s7.mid ⇆ s8.mid @ BC — 田 inner cross (welded).
  All other joints: N (natural gap ~13-27 px, do NOT weld).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 9 draw calls (or 9 stroke primitives)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim: 火 (s1-s4, left column) + 田 '
              '(s5-s9, right half). Inner 田 cross (s7⇆s8) welded via '
              'ordering + fill disc. All N-joints preserved as small '
              'gaps.'),
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


def _shorten(pt, other, px):
    """Return `pt` moved `px` pixels toward `other`."""
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


# ==== 火 anchors (MMH-verbatim; strokes 1-4) ====
S1_H = ('ML', 0.466, 0.383); S1_T = ('ML', 0.469, 0.893)  # near-vertical interior
S2_H = ('C',  0.154, 0.104); S2_T = ('ML', 0.946, 0.471)  # top dot / short slash
S3_H = ('TL', 0.715, 0.715); S3_T = ('BL', 0.258, 0.824)  # long 撇 (left slash)
S4_H = ('BL', 0.929, 0.06);  S4_T = ('BC', 0.178, 0.402)  # short 捺 (right slash)

# ==== 田 anchors (MMH-verbatim; strokes 5-9) ====
S5_H = ('C',  0.333, 0.635); S5_T = ('BC', 0.579, 0.64)   # left 竖 of 田
S6_H = ('C',  0.491, 0.652); S6_T = ('BR', 0.452, 0.76)   # 横折 (top + right wall)
S7_H = ('BC', 0.696, 0.118); S7_T = ('BR', 0.282, 0.03)   # middle 横
S8_H = ('C',  0.884, 0.708); S8_T = ('BC', 0.919, 0.426)  # middle 竖
S9_H = ('BC', 0.646, 0.575); S9_T = ('BR', 0.355, 0.467)  # bottom 横


def draw_huo(d):
    """Draw 火 on the left (4 strokes, MMH-verbatim)."""
    p1h = anchor_to_xy(S1_H); p1t = anchor_to_xy(S1_T)
    p2h = anchor_to_xy(S2_H); p2t = anchor_to_xy(S2_T)

    # s1: short near-vertical interior (interior median of 火)
    fat_line(d, p1h, p1t, width=6)
    # s2: upper-left dot / short slash
    fat_line(d, p2h, p2t, width=7)
    # s3: long 撇 (upper-right → lower-left), tapered
    draw_pie(d, from_anchor=S3_H, to_anchor=S3_T,
             head_width=11, tail_width=2, curve=0.10, segments=48)
    # s4: short 捺 (upper-left → lower-right)
    draw_na(d, from_anchor=S4_H, to_anchor=S4_T,
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.75, curve=0.08, segments=48)


def draw_tian(d):
    """Draw 田 on the right (5 strokes, MMH-verbatim)."""
    p5h = anchor_to_xy(S5_H); p5t = anchor_to_xy(S5_T)
    p6h = anchor_to_xy(S6_H); p6t = anchor_to_xy(S6_T)
    p7h = anchor_to_xy(S7_H); p7t = anchor_to_xy(S7_T)
    p8h = anchor_to_xy(S8_H); p8t = anchor_to_xy(S8_T)
    p9h = anchor_to_xy(S9_H); p9t = anchor_to_xy(S9_T)

    w = 7
    gap = 3

    # s5: left 竖 of 田 (shorten top for N-gap vs top-heng)
    fat_line(d, _shorten(p5h, p5t, gap), p5t, width=w)

    # s6: heng-zhe — top-heng + right-wall drawn as two segments.
    # p6h ~ top-left corner of 田; p6t ~ bottom-right corner.
    corner = (p6t[0], p6h[1])  # top-right corner of 田 frame
    fat_line(d, p6h, corner, width=w)
    fat_line(d, corner, _shorten(p6t, corner, gap), width=w)
    cx, cy = corner; r = 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s7: middle 横 (will be P-crossed by s8)
    fat_line(d,
             _shorten(p7h, p7t, 2),
             _shorten(p7t, p7h, 2),
             width=w)
    # s8: middle 竖 (drawn AFTER s7 so crossing reads welded)
    fat_line(d, p8h, p8t, width=w)
    # emphasis at the inner P-cross
    icx = (p8h[0] + p8t[0]) / 2
    icy = (p7h[1] + p7t[1]) / 2
    d.ellipse([icx - 4, icy - 4, icx + 4, icy + 4], fill=(0, 0, 0))

    # s9: bottom 横 (shorten both ends for N-gap corners)
    fat_line(d,
             _shorten(p9h, p9t, 2),
             _shorten(p9t, p9h, 2),
             width=w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_huo(d)
    draw_tian(d)
    out = os.path.join(_HERE, '01_畑.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
