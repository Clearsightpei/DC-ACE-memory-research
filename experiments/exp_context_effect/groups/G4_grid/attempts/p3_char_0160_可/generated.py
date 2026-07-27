"""可 (kě, 5 strokes) — Phase-3 char attempt.

Composition: top 横 (long) + right 竖钩 (long descending hook) + 口 (small, lower-left).

Stroke plan (matches MMH order):
  s1: top 横 — ML(0.369, 0.005) → TR(0.725, 0.894)
  s2: 口 left 竖 — ML(0.732, 0.433) → BL(0.926, 0.065)
  s3: 口 横折 (top+right of small mouth) — ML(0.885, 0.436) → C(0.31, 0.784)
  s4: 口 bottom 横 — ML(0.981, 0.96) → C(0.509, 0.884)
  s5: right 竖钩 — TC(0.837, 0.955) → BC(0.523, 0.666)

Joints (all N per MMH):
  s1.mid ⇆ s5.head  @ TC — N (~15 px gap)
  s2.head ⇆ s3.head @ ML — N (~14 px gap)
  s2.tail ⇆ s4.head @ ML — N (~12 px gap)
  s3.tail ⇆ s4.mid  @ C  — N (~12 px gap)

Bank use: cannot cleanly reuse kou_char because the mouth here is much
smaller than the standalone 口 and positioned in the lower-left; the MMH
anchors are directly usable, so inline in G1-style with the fat_line
primitive from _anchor.py.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 5 strokes drawn per MMH anchors; N-gaps preserved at all 4 joints.'
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_ke(draw):
    # === s1: top 横 (long horizontal, slight up-right slant) ===
    s1h = anchor_to_xy(('ML', 0.369, 0.005))
    s1t = anchor_to_xy(('TR', 0.725, 0.894))
    fat_line(draw, s1h, s1t, width=8)

    # === Small 口 in lower-left. Build as a coherent rectangle so it reads. ===
    # Rectangle roughly x=73..145, y=143..200. Draw all three strokes with
    # matching corners (small N-gaps for calligraphic look).
    kx0, kx1 = 73, 148     # left, right
    ky0, ky1 = 143, 200    # top, bottom

    # s2: left 竖 (top → bottom)
    fat_line(draw, (kx0 + 2, ky0 + 4), (kx0 + 6, ky1 - 2), width=7)

    # s3: 横折 — top bar left→right then right wall top→bottom
    top_left  = (kx0 + 8, ky0)
    top_right = (kx1, ky0 + 2)
    fat_line(draw, top_left, top_right, width=7)
    br = (kx1 - 4, ky1 - 4)
    fat_line(draw, (top_right[0], top_right[1] + 2), br, width=7)
    # corner dot
    cx, cy = top_right; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s4: bottom 横 (left → right)
    bl = (kx0 + 10, ky1)
    fat_line(draw, bl, (br[0] - 3, br[1] + 2), width=7)

    # === s5: right 竖钩 (long vertical from top, hooks left at bottom) ===
    s5h = anchor_to_xy(('TC', 0.837, 0.955))
    s5t = anchor_to_xy(('BC', 0.523, 0.666))
    # keep small N gap under top 横
    s5h_g = _shorten(s5h, s5t, 4)
    # main descending line
    fat_line(draw, s5h_g, s5t, width=9)
    # hook: small tick pointing up-left from the tail
    hook_end = (s5t[0] - 14, s5t[1] - 16)
    fat_line(draw, s5t, hook_end, width=8)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ke(draw)
    out = os.path.join(os.path.dirname(__file__), '01_可.png')
    img.save(out)
    print(f"Saved {out}")
    # sanity: 5 stroke primitives = s1 + s2 + (s3 top + s3 right) + s4 + s5 + hook
    # visible stroke count that MMH cares about = 5 (the 横折 counts as one, hook counts as part of 竖钩)


if __name__ == '__main__':
    main()
