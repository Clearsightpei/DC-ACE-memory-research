"""p3_char_0432_畋 retry_1 — 畋 (tián), 9 strokes.

TRAJECTORY DIFF (Step 0):
- GT (gt/phase3/畋.png): 田 (compact left column) + 攵 on the right.
  攵 has FOUR visible marks: (a) a short curved 撇 hanging off the top,
  (b) a short 横 crossbar under it, (c) a long 撇 sweeping down-left,
  (d) a long 捺 sweeping down-right; (c) and (d) welded near BC.
- MAIN attempt (verdict C): 田 read OK, but the 攵 collapsed. The
  short 横 (s7) was invisible — swallowed by fat s6 pie and s8 head.
  The top 撇 (s6) was too straight/steep, so it merged with the long
  撇 (s8) and the whole right side read like 又 (two-stroke) rather
  than 攵 (four-stroke). Also the s9 long捺 tail flew past the frame
  making the right half feel loose/oversized.

Fixes applied this retry:
1. Give s7 (short 横) real weight and a small BC-cap so it doesn't
   drown at the crossing with s6 / s8 heads.
2. Draw s6 (short 撇) with a stronger curve so its head sits clearly
   ABOVE-right and its body arcs DOWN-LEFT — visually distinct from
   the long 撇 s8 which starts lower.
3. Draw ordering: s6 first (top pie), s7 second (horizontal), s8
   third (long pie), s9 last (long捺). Emphasis disc at s8×s9 weld.
4. Tighten s9's peak_t / peak swell so the 捺 has an obvious swell
   before hitting BR — makes the 捺 read as a 捺 not a straight line.

No BANK_DEVIATION — no bank primitive for 田 or 攵 exists to skip.
Base primitives (pie/heng/na/fat_line) used as-is.

Structural expectations (MMH block):
  9 strokes, 12 joints. P-joints: s3⇆s4 (田 inner cross), s8⇆s9 (攵 X).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry with articulated 攵: s7 heng thickened + cap; '
              's6 curved harder to separate from s8 long pie; '
              's8/s9 X-cross weld emphasized. 田 unchanged (main '
              'attempt read OK on left).'),
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

    corner = (p2t[0], p2h[1])  # top-right corner of heng-zhe

    w = 7
    gap = 4

    # s1: left vertical
    fat_line(draw, _shorten(p1h, p1t, gap), p1t, width=w)
    # s2: top heng + right wall (heng-zhe), two segments + corner cap
    fat_line(draw, p2h, corner, width=w)
    fat_line(draw, corner, _shorten(p2t, corner, gap), width=w)
    cx, cy = corner; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3 inner heng, s4 inner shu — P-cross welded via ordering + disc
    fat_line(draw, p3h, p3t, width=w)
    fat_line(draw, p4h, p4t, width=w)
    icx = (p3h[0] + p3t[0]) / 2
    icy = (p4h[1] + p4t[1]) / 2
    draw.ellipse([icx - 4, icy - 4, icx + 4, icy + 4], fill=(0, 0, 0))

    # s5 bottom heng — small N-gaps
    fat_line(draw, _shorten(p5h, p5t, 2), _shorten(p5t, p5h, 2), width=w)


def draw_pu(draw):
    """Draw 攵 on the right (4 strokes)."""
    # s6: short 撇 — strong curve so head sits UP-RIGHT, body arcs DOWN-LEFT
    #      distinct from s8's long 撇 which starts to its right & lower.
    draw_pie(draw, from_anchor=S6_H, to_anchor=S6_T,
             head_width=10, tail_width=2, curve=0.18, segments=52)

    # s7: short 横 — thickened & capped so it survives the s6/s8 crossings
    p7h = anchor_to_xy(S7_H); p7t = anchor_to_xy(S7_T)
    draw_heng(draw, from_anchor=S7_H, to_anchor=S7_T, width=8)
    # emphasize the heng tips
    for x, y in (p7h, p7t):
        draw.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(0, 0, 0))

    # s8: long 撇 — full sweep, moderate curve
    draw_pie(draw, from_anchor=S8_H, to_anchor=S8_T,
             head_width=10, tail_width=2, curve=0.10, segments=56)

    # s9: long 捺 — pronounced swell before BR tail
    draw_na(draw, from_anchor=S9_H, to_anchor=S9_T,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.72, curve=0.10, segments=56)

    # Emphasis disc at s8 x s9 weld (analytic line-line intersection).
    p8h = anchor_to_xy(S8_H); p8t = anchor_to_xy(S8_T)
    p9h = anchor_to_xy(S9_H); p9t = anchor_to_xy(S9_T)
    x1, y1 = p8h; x2, y2 = p8t; x3, y3 = p9h; x4, y4 = p9t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) > 1e-6:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        cx = x1 + t * (x2 - x1); cy = y1 + t * (y2 - y1)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(0, 0, 0))


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
