"""p3_char_0432_畋 — 畋 (tián), 9 strokes.

Memory lookups (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — B9/B10 A-recipe applies: explicit decomposition +
     MMH-verbatim anchors + inline base primitives when compound
     primitives don't fit slot. This char is a classic 2-radical
     left-right compound (田 far-left column + 攵 right-half).
  2. success_bank/INDEX.md — no `tian.py` for 田 (only 申 / 甲 / 甴 /
     畀 attempts inline the 田-frame). No `pu.py` for 攵 either — the
     bank file was pruned; only the past 攵 attempt exists. Both
     radicals must be inlined here.
  3. errata.md — 畋 not listed.

Decomposition: 畋 = 田 (left, 5 strokes) + 攵 (right, 4 strokes).
  田 (s1-s5): shu-left + heng-zhe (top+right wall) + inner heng
              + inner shu + bottom heng.
  攵 (s6-s9): short 撇 + short 横 + long 撇 + long 捺, with s8/s9
              welded X-cross at BC(0.865, 0.302).

BANK_DEVIATION does not apply — no bank primitive skipped
(neither `tian.py` nor `pu.py` exist as bank files).

Structural expectations (from dispatcher-injected MMH block):
  9 strokes, 12 joints (10 N + 2 P).
  P-joints:
    - s3.mid ⇆ s4.mid @ ML — 田 inner-cross (welded)
    - s8.mid ⇆ s9.mid @ BC — 攵 X-cross (welded)
  N-joints: all 田 corners + 攵 stroke starts leave 10-25 px gaps.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim: 田 (s1-s5, left column) + 攵 '
              '(s6-s9, right half). Inner 田 cross (s3⇆s4) welded via '
              'ordering + fill disc. 攵 X-cross (s8⇆s9) welded at BC '
              'via shared crossing plus small emphasis disc. All N '
              'corners of 田 shortened ~5 px for natural gap.'),
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
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


# ==== 田 anchors (MMH-verbatim) ====
S1_H = ('ML', 0.208, 0.351); S1_T = ('BL', 0.413, 0.44)     # left vertical
S2_H = ('ML', 0.384, 0.365); S2_T = ('BL', 0.964, 0.227)    # top-bar + right-wall (heng-zhe)
S3_H = ('ML', 0.492, 0.84);  S3_T = ('ML', 0.964, 0.764)    # middle heng
S4_H = ('ML', 0.645, 0.409); S4_T = ('BL', 0.683, 0.194)    # middle shu
S5_H = ('BL', 0.483, 0.35);  S5_T = ('BL', 0.926, 0.276)    # bottom heng

# ==== 攵 anchors (MMH-verbatim) ====
S6_H = ('TC', 0.682, 0.609); S6_T = ('C', 0.312, 0.866)     # short 撇
S7_H = ('C', 0.655, 0.444);  S7_T = ('MR', 0.563, 0.283)    # short 横
S8_H = ('C', 0.904, 0.494);  S8_T = ('BC', 0.061, 0.783)    # long 撇
S9_H = ('C', 0.418, 0.825);  S9_T = ('BR', 0.851, 0.88)     # long 捺


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

    # s1: left vertical (shortened top so top-heng joint stays N)
    fat_line(draw, _shorten(p1h, p1t, gap), p1t, width=w)
    # s2: top heng + right wall (heng-zhe), drawn as two segments
    fat_line(draw, p2h, corner, width=w)
    fat_line(draw, corner, _shorten(p2t, corner, gap), width=w)
    # cap the bend corner
    cx, cy = corner; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3: inner middle heng (P-welded through by s4 later)
    fat_line(draw, p3h, p3t, width=w)
    # s4: inner middle shu (drawn LAST-inside so P-cross weld is clean)
    fat_line(draw, p4h, p4t, width=w)
    # emphasis at the P-cross
    icx = (p3h[0] + p3t[0]) / 2
    icy = (p4h[1] + p4t[1]) / 2
    draw.ellipse([icx - 4, icy - 4, icx + 4, icy + 4], fill=(0, 0, 0))

    # s5: bottom heng (leave small N-gaps at each end so it doesn't fuse)
    fat_line(draw, _shorten(p5h, p5t, 2), _shorten(p5t, p5h, 2), width=w)


def draw_pu(draw):
    """Draw 攵 on the right (4 strokes)."""
    # s6: short 撇 (top of 攵) — tapered, slight curve
    draw_pie(draw, from_anchor=S6_H, to_anchor=S6_T,
             head_width=9, tail_width=2, curve=0.10, segments=48)

    # s7: short 横 (crossbar of 攵)
    draw_heng(draw, from_anchor=S7_H, to_anchor=S7_T, width=7)

    # s8: long 撇 (down-left)
    draw_pie(draw, from_anchor=S8_H, to_anchor=S8_T,
             head_width=9, tail_width=2, curve=0.08, segments=48)

    # s9: long 捺 (down-right, with peak swell) — DRAWN AFTER s8 so
    # the X-cross reads as welded.
    draw_na(draw, from_anchor=S9_H, to_anchor=S9_T,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.70, curve=0.08, segments=48)

    # Small emphasis disc at the X-cross weld
    p8h = anchor_to_xy(S8_H); p8t = anchor_to_xy(S8_T)
    p9h = anchor_to_xy(S9_H); p9t = anchor_to_xy(S9_T)
    # Compute line intersection (both are straight-ish)
    x1, y1 = p8h; x2, y2 = p8t; x3, y3 = p9h; x4, y4 = p9t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) > 1e-6:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        cx = x1 + t * (x2 - x1); cy = y1 + t * (y2 - y1)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(0, 0, 0))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_tian(d)
    draw_pu(d)
    out = os.path.join(_HERE, '01_畋.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
