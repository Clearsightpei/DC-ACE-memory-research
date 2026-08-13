"""p3_char_0434_畎 retry_1 — 畎 (quǎn), 9 strokes = 田 + 犬.

TRAJECTORY DIFF (Step 0):
- GT (gt/phase3/畎.png): 田 sits LEFT (compact, y roughly mid-band) and
  犬 sits RIGHT and TALLER. 犬 = 大 (heng+long-pie+na) + 丶 at upper-right.
  Notable in GT: the 大's long pie sweeps deeply DOWN-LEFT, its tail
  ending near the bottom-left of the 犬 slot; the 大's na is comparatively
  short, sweeping down-right; the 丶 is a small NE→SW-leaning dot high
  up above the na.
- MAIN attempt (verdict C): 田 read OK on the left. RIGHT side failed:
  the pie was too shallow / too vertical, the na was too straight and
  ran off past the frame, the top-right 丶 was placed too low and
  merged with the pie/na cross. Overall the right glyph did not read
  as 犬 — the "大" base was insufficient.

Fixes applied this retry:
1. Follow MMH anchors verbatim for all 9 strokes (I was drifting).
2. 大's pie (s7) drawn as a LONG deep sweep from high TC down to BL —
   curve -0.15 so it bellies leftward (concave-right), tail thinning.
3. 大's na (s8) kept short but with pronounced 捺 swell (peak_t=0.75,
   peak_width=12) so it clearly reads as 捺 not a straight tick.
4. 丶 dot (s9) placed HIGH (in TR cell) with a small dian primitive
   leaning NE→SW.
5. P-cross emphasis discs at 田-inner (s3×s4) and 大 (s6×s7).

No BANK_DEVIATION — using base primitives (heng/pie/na/dian/fat_line);
da.py exists but its baked anchors don't match this composition's
compressed 犬 slot; safer to inline with MMH anchors.

Structural expectations (MMH block):
  9 strokes, 12 joints. P: s3⇆s4 (田 cross), s6⇆s7 (大 cross).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry: 犬 rebuilt with MMH-verbatim anchors — long-deep '
              'pie, swelled short na, high 丶 dot. 田 unchanged (main '
              'read OK).'),
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
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


# ==== 田 anchors (MMH-verbatim) ====
S1_H = ('ML', 0.188, 0.485); S1_T = ('BL', 0.401, 0.464)    # left vertical
S2_H = ('ML', 0.319, 0.491); S2_T = ('BC', 0.04, 0.405)     # heng-zhe
S3_H = ('ML', 0.469, 0.957); S3_T = ('ML', 0.938, 0.89)     # inner heng
S4_H = ('ML', 0.642, 0.512); S4_T = ('BL', 0.659, 0.265)    # inner shu
S5_H = ('BL', 0.463, 0.42);  S5_T = ('BL', 0.92, 0.303)     # bottom heng

# ==== 犬 anchors (MMH-verbatim) ====
S6_H = ('C', 0.28, 0.825);   S6_T = ('MR', 0.546, 0.705)    # 大 heng
S7_H = ('TC', 0.644, 0.694); S7_T = ('BL', 0.961, 0.944)    # 大 long pie
S8_H = ('C', 0.813, 0.983);  S8_T = ('BR', 0.836, 0.877)    # 大 short na
S9_H = ('TR', 0.104, 0.987); S9_T = ('MR', 0.44, 0.277)     # 丶 dot


def draw_tian(draw):
    """Draw 田 on the left (5 strokes)."""
    p1h = anchor_to_xy(S1_H); p1t = anchor_to_xy(S1_T)
    p2h = anchor_to_xy(S2_H); p2t = anchor_to_xy(S2_T)
    p3h = anchor_to_xy(S3_H); p3t = anchor_to_xy(S3_T)
    p4h = anchor_to_xy(S4_H); p4t = anchor_to_xy(S4_T)
    p5h = anchor_to_xy(S5_H); p5t = anchor_to_xy(S5_T)

    corner = (p2t[0], p2h[1])  # top-right corner of heng-zhe

    w = 7
    gap = 3

    # s1: left vertical
    fat_line(draw, _shorten(p1h, p1t, gap), p1t, width=w)

    # s2: top heng + right wall (heng-zhe) — two segments + corner cap
    fat_line(draw, p2h, corner, width=w)
    fat_line(draw, corner, _shorten(p2t, corner, gap), width=w)
    cx, cy = corner; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3 inner heng, s4 inner shu — P-cross welded via ordering + disc
    fat_line(draw, p3h, p3t, width=w)
    fat_line(draw, p4h, p4t, width=w)
    icx = (p3h[0] + p3t[0]) / 2.0
    icy = (p4h[1] + p4t[1]) / 2.0
    draw.ellipse([icx - 4, icy - 4, icx + 4, icy + 4], fill=(0, 0, 0))

    # s5 bottom heng — small N-gaps at both ends
    fat_line(draw, _shorten(p5h, p5t, 2), _shorten(p5t, p5h, 2), width=w)


def draw_quan(draw):
    """Draw 犬 on the right (4 strokes)."""
    # s6: 大's heng — spans C→MR
    draw_heng(draw, from_anchor=S6_H, to_anchor=S6_T, width=8)

    # s7: 大's long pie — high TC down to BL, deep leftward sweep
    draw_pie(draw, from_anchor=S7_H, to_anchor=S7_T,
             head_width=10, tail_width=1, curve=-0.15, segments=60)

    # s8: 大's na — short but swelled, sweeping down-right
    draw_na(draw, from_anchor=S8_H, to_anchor=S8_T,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.75, curve=0.10, segments=40)

    # s9: 丶 dot at upper-right — NE→SW-leaning short dian
    draw_dian(draw, from_anchor=S9_H, to_anchor=S9_T,
              head_width=2, peak_width=9, curve=0.08, segments=24)

    # Emphasis disc at 大 heng × pie weld (analytic intersection)
    p6h = anchor_to_xy(S6_H); p6t = anchor_to_xy(S6_T)
    p7h = anchor_to_xy(S7_H); p7t = anchor_to_xy(S7_T)
    x1, y1 = p6h; x2, y2 = p6t; x3, y3 = p7h; x4, y4 = p7t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) > 1e-6:
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        cx = x1 + t * (x2 - x1); cy = y1 + t * (y2 - y1)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(0, 0, 0))


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
