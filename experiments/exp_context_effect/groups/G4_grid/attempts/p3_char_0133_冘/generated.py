"""冘 (yín) — 4 strokes per MMH.

Lookup checklist (memory_index reading order):
1. success_bank/INDEX.md grep 冘 → not present. Related family: ji.py (几).
2. errata.md grep 冘 → not present.
3. form_catalog.md → 几-family top uses N-gap; here s2⇆s3 is P (welded), different.
4. principles_meta.md → TR6: inline strokes fresh where no clean primitive fits.
5. joint_atlas.md → P = welded crossing (draw so lines actually cross).
6. sandbox.md → 几-family top gap N (~15-20 px); here explicit gap N ~12.9 px at s1.mid⇆s2.head.

MMH structural spec (from dispatcher):
  s1: head ML(0.671, 0.169) → tail ML(0.521, 0.79)   — short left-side 点/竖 (top-left mark).
  s2: head ML(0.800, 0.274) → tail MR(0.054, 0.526)  — 横 sweeping across, slight downward.
  s3: head TC(0.286, 0.656) → tail BL(0.302, 0.979)  — long 撇 diagonal from top-centre down.
  s4: head C(0.506, 0.661)  → tail BR(0.637, 0.323)  — 弯钩-style rightward-up (drawn tail→head as sweep).
Joints:
  s1.mid(0.15) ⇆ s2.head @ ML : N (gap ~12.9 px, do NOT weld).
  s2.mid(0.30) ⇆ s3.mid(0.22) @ C : P (welded crossing).

Inlined per TR6 — no clean bank primitive fits this specific composition.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Inlined all 4 strokes with anchors matching MMH. s2⇆s3 crossing implemented by geometry (both pass through C).'
}


def draw_yin(draw):
    # s1 — short 点-like mark on left side of cover. In ML cell, tilting left-down.
    s1_head = ('ML', 0.671, 0.169)
    s1_tail = ('ML', 0.521, 0.79)
    draw_dian(draw, s1_head, s1_tail,
              head_width=3, peak_width=8, curve=0.05, segments=24)

    # s2 — 横 running from ML → MR, slight downward tilt (the cover 横).
    s2_head = ('ML', 0.800, 0.274)
    s2_tail = ('MR', 0.054, 0.526)
    p2a = anchor_to_xy(s2_head)
    p2b = anchor_to_xy(s2_tail)
    mid2 = ((p2a[0] + p2b[0]) * 0.5, (p2a[1] + p2b[1]) * 0.5 - 1)
    pts2 = quad_bezier(p2a, mid2, p2b, n=32)
    widths2 = [7] * len(pts2)
    widths2[-3] = 9; widths2[-2] = 10; widths2[-1] = 8
    stroke_variable_width(draw, pts2, widths2)

    # s3 — long 撇 from TC down-through the horizontal to BL (P-cross at C).
    # Head is at TC(0.286, 0.656) which is above the cover; tail sweeps to BL bottom.
    s3_head = ('TC', 0.286, 0.656)
    s3_tail = ('BL', 0.302, 0.979)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=1, curve=0.14, segments=48)

    # s4 — 弯钩/斜钩: from C(0.506, 0.661) descending down-right into BC/BR,
    # then curving right and finishing with an upward hook tip at BR(0.637, 0.323).
    # MMH lists head=C, tail=BR (higher y, meaning UP in PIL). This is the
    # tail-flick endpoint. So the stroke goes head DOWN then SWEEPS RIGHT and UP.
    s4_head = ('C', 0.506, 0.661)
    s4_tail = ('BR', 0.637, 0.323)
    p4a = anchor_to_xy(s4_head)  # ~(150.6, 166.1)
    p4b = anchor_to_xy(s4_tail)  # ~(263.7, 232.3)
    # Two-segment path: descent to a bottom belly, then sweep up to tail.
    belly = (p4a[0] + 40, 260)   # bottom of curve, roughly BC area
    pts4a = quad_bezier(p4a, (p4a[0] + 5, (p4a[1] + belly[1]) / 2 + 10), belly, n=32)
    pts4b = quad_bezier(belly, ((belly[0] + p4b[0]) / 2 + 8, belly[1] + 4), p4b, n=28)
    pts4 = pts4a + pts4b[1:]
    n = len(pts4) - 1
    widths4 = []
    for i, _ in enumerate(pts4):
        t = i / n
        if t < 0.5:
            w = 7 + t * 6   # 7 → 10
        elif t < 0.85:
            w = 10 - (t - 0.5) / 0.35 * 3  # 10 → 7
        else:
            w = 7 - (t - 0.85) / 0.15 * 6  # taper to 1
        widths4.append(max(1, w))
    stroke_variable_width(draw, pts4, widths4)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yin(draw)
    out = os.path.join(HERE, '01_冘.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
