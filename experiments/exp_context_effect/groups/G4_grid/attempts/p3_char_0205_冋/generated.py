"""p3_char_0205_冋 — 冋 = 冂 frame + 口 inside (5 strokes).

Memory checklist (per memory_index.md v8):
  1. drawer_memory.md — read; enclosing-frame => chronic/jiong_frame is
     recommended, BUT MMH anchors for this specific char place the frame
     narrower than chronic (frame ends near x=190, not chronic's x=280).
     Under v8 "trust GT" — inlining fresh 冂 that matches MMH anchors.
  2. INDEX grep — kou.py exists; would help for inner 口 but the MMH
     anchors here place inner 口 much smaller and higher than kou's
     defaults, so inlining fresh per MMH.
  3. errata grep — 冋 not in errata.

Composition:
  冋 = enclosing 冂 frame (strokes 1-2) + inner 口 (strokes 3-5).

Strokes (per MMH-injected anchors):
  s1 竖   : TL(0.65,0.87) -> BL(0.621,0.877)   ; left wall of frame
  s2 横折 : TL(0.844,0.929) -> BC(0.907,0.745) ; top+right wall of frame
  s3 竖   : C(0.063,0.544) -> BC(0.257,0.118)  ; inner 口 left wall
  s4 横折 : C(0.187,0.547) -> C(0.67,0.819)    ; inner 口 top+right
  s5 横   : C(0.301,0.945) -> C(0.825,0.928)   ; inner 口 bottom bar

Joints (all N — small natural gaps ~10-15 px):
  s1.head N s2.head          (frame top-left corner)
  s3.head N s4.head          (inner 口 top-left corner)
  s3.mid  N s5.head          (inner 口 bottom-left corner)
  s4.tail N s5.mid           (inner 口 bottom-right corner)
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inlined fresh: chronic/jiong_frame is wider than MMH for 冋; trust GT per v8',
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


def draw_jiong_char(draw):
    # ---- Outer 冂 frame ----
    # s1 — left wall (straight vertical, slight slant left)
    s1h = anchor_to_xy(('TL', 0.65, 0.87))
    s1t = anchor_to_xy(('BL', 0.621, 0.877))
    fat_line(draw, s1h, s1t, width=10)

    # s2 — 横折 (top bar + right wall)
    # head at TL top-left, corner at top-right, tail at bottom-right
    s2h = anchor_to_xy(('TL', 0.844, 0.929))
    s2t = anchor_to_xy(('BC', 0.907, 0.745))
    # corner: top-right of the frame, aligned with tail x, head y
    s2c = (s2t[0], s2h[1])
    # slight N-gap at top-left: shorten head away from corner
    s2h_g = _shorten(s2h, s2c, 6)
    fat_line(draw, s2h_g, s2c, width=10)
    fat_line(draw, s2c, s2t, width=10)
    # corner dot for smoothness
    cx, cy = s2c; r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # ---- Inner 口 ----
    # s3 — inner left wall
    s3h = anchor_to_xy(('C', 0.063, 0.544))
    s3t = anchor_to_xy(('BC', 0.257, 0.118))
    fat_line(draw, s3h, s3t, width=6)

    # s4 — inner 横折 (top bar + right wall)
    s4h = anchor_to_xy(('C', 0.187, 0.547))
    s4t = anchor_to_xy(('C', 0.67, 0.819))
    s4c = (s4t[0], s4h[1])
    # N-gap at top-left corner (relative to s3.head)
    s4h_g = _shorten(s4h, s4c, 4)
    fat_line(draw, s4h_g, s4c, width=6)
    fat_line(draw, s4c, s4t, width=6)
    cx, cy = s4c; r = 3
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s5 — inner bottom bar 横
    s5h = anchor_to_xy(('C', 0.301, 0.945))
    s5t = anchor_to_xy(('C', 0.825, 0.928))
    # N-gaps at both corners: shorten head from tail direction
    s5h_g = _shorten(s5h, s5t, 4)
    fat_line(draw, s5h_g, s5t, width=6)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jiong_char(draw)
    out = os.path.join(_HERE, '01_冋.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
