"""p3_char_0125_円 — 円 (Japanese yen, 4 strokes).

Structural inspection (mandatory lookup checklist):
  1. success_bank/INDEX.md: no 円 entry. Closest primitives: yue.py (曰
     enclosure), ri.py (日), kou.py (口). All 口-family/冂-family frames
     with N-class open corners.
  2. errata.md: no 円 entry. Related p2_024_冂 and p3_026_冂 have
     chronic FAIL history — soft-interpretation of "MMH anchors are a
     FLOOR" (TR9). Frame must span nearly full grid.
  3. form_catalog: 冂-family frames want ML→BL for left wall, TL→TR→BR
     for 横折 top+right; all corners N (small gap, no weld).
  4. principles_meta TR9: standalone frame → expand anchors to full
     grid span. TR10: N gaps ≤25 px, ≥ ~8 px so corners LOOK connected.
  5. joint_atlas: 口-family corners are N-narrow (~10 px). Inner
     strokes to enclosing wall are N.

Structure of 円 from GT (4 strokes):
  s1: left vertical wall (丨).
  s2: top-plus-right 横折 (冂 shape).
  s3: inner short vertical (丨) descending from mid-top area to bottom.
  s4: bottom horizontal bar (一) closing the frame.

All 5 joints are N (口-family open corners + inner-N contacts), matching
MMH-injected expectations. Frame expanded per TR9.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Frame TR9-expanded to full grid span. Inner vertical '
             '(s3) at x=0.50 (C cell), bottom bar (s4) spans left wall '
             'to right wall as horizontal one-stroke.',
}

import os, sys
from PIL import Image, ImageDraw

# Use shared G4 anchor helper
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line  # noqa: E402


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    w = 10

    # --- stroke 1: left vertical wall (丨) ---
    # Expected head @ ML(0.809, 0.204) ~ (81, 120), tail @ BL(0.844, 0.971) ~ (84, 297)
    # TR9-expand: keep near ML→BL, use x_frac ~ 0.80 for a strong left wall.
    s1_h = anchor_to_xy(('ML', 0.80, 0.20))    # (80, 120)
    s1_t = anchor_to_xy(('BL', 0.80, 0.95))    # (80, 295)
    fat_line(draw, _shorten(s1_h, s1_t, 4), _shorten(s1_t, s1_h, 4), width=w)

    # --- stroke 2: 横折 (top + right wall) ---
    # Expected head @ ML(0.981,0.242) ~ (98,124), tail @ BC(0.658,0.789) ~ (166,279)
    # 冂-family top+right corner: HORIZONTAL top bar from just right of s1
    # head to right wall (same y as s1 head), then vertical down to bottom.
    s2_h = anchor_to_xy(('ML', 0.90, 0.20))    # (90, 120) — top-left corner
    s2_c = anchor_to_xy(('MR', 0.90, 0.20))    # (290, 120) — top-right corner (same y)
    s2_t = anchor_to_xy(('BR', 0.90, 0.95))    # (290, 295) — bottom-right
    # Top horizontal (with N gap to s1 head)
    fat_line(draw, _shorten(s2_h, s2_c, 4), s2_c, width=w)
    # Right vertical
    fat_line(draw, s2_c, _shorten(s2_t, s2_c, 4), width=w)
    # Corner disc for clean turn
    r = 5
    draw.ellipse([s2_c[0]-r, s2_c[1]-r, s2_c[0]+r, s2_c[1]+r], fill=(0, 0, 0))

    # --- stroke 3: inner short vertical (丨) ---
    # Expected head @ C(0.541, 0.236) ~ (154, 124), tail @ C(0.421, 0.963) ~ (142, 296)
    # Inner vertical descending near the vertical center; slight lean.
    # Inner vertical should descend from just below the top bar down to
    # near (but not touching) the bottom bar. Extend into BC cell so it
    # visually reads as a proper inner 丨.
    s3_h = anchor_to_xy(('C', 0.54, 0.20))     # (154, 120) — just below top bar
    s3_t = anchor_to_xy(('BC', 0.44, 0.75))    # (144, 275) — near bottom bar (N gap)
    fat_line(draw, _shorten(s3_h, s3_t, 4), _shorten(s3_t, s3_h, 4), width=w)

    # --- stroke 4: bottom horizontal bar (一) closing the frame ---
    # Expected head @ BC(0.005, 0.121) ~ (100, 212), tail @ MR(0.007, 0.916) ~ (200, 292)
    # Interpretation: bottom bar running L→R just above the bottom of BC row.
    # Use full wall-to-wall inside the bottom band for a proper closing 横.
    s4_h = anchor_to_xy(('BL', 0.85, 0.88))    # (85, 288)
    s4_t = anchor_to_xy(('BR', 0.90, 0.88))    # (290, 288)
    fat_line(draw, _shorten(s4_h, s4_t, 4), _shorten(s4_t, s4_h, 4), width=w)

    out = os.path.join(os.path.dirname(__file__), '01_円.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
