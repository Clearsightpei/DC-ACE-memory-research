"""p3_char_0210_四 — 四 (sì, "four", 5画)

Reading order used:
1. drawer_memory.md — no direct 四 primitive; 口-family composition, GT
   shows a wide 口 enclosure with two inner strokes (撇 + 竖弯) and a
   bottom-sealing 横. Under v8, MMH anchors are authoritative; bank
   kou.py is REFERENCE only (its anchors are tuned for tall standalone
   口, wrong proportions for 四's wide enclosure).
2. success_bank/INDEX.md — 口 primitive exists (kou.py, kou_char.py)
   but 四's enclosure is a different proportion (wider, shorter). MMH
   gives us 5 explicit stroke anchors, drawing fresh from those.
3. errata.md — 四 not present.

Structure per MMH:
  s1 = left 竖 (slanting)              ML→BL
  s2 = 横折 (top + right wall)         ML→BR, corner @ TR
  s3 = inner-left 撇 (down-left short) C →BL
  s4 = inner-right 竖弯 (down-right)   C →MR
  s5 = bottom 横 (sealing bar)         BL→BR

All 5 joints are N-class (small natural gaps, 口-family open corners),
per MMH structural spec. No welding.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        # Deliberate: MMH anchors produce an over-slanted parallelogram
        # (v1 render). Per v8 rules "if GT and memory disagree, trust
        # GT" — snapped enclosure walls closer to rectangular while
        # keeping inner strokes near MMH anchors. Deltas < 0.20 in cell
        # frac, tolerated by G4 rule.
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; N joints via _shorten gaps. Revised once to reduce excessive slant vs GT.',
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_si(draw):
    # Rectangularized 口-enclosure (trust GT over literal MMH slant).
    # 四 GT is a wide, near-rectangular box with two inner strokes and
    # a bottom sealing bar. Snap outer walls to near-vertical/horizontal.
    #
    # Outer box spans roughly x=[45, 255], y=[110, 235] on the 300 canvas.
    #   TL cell = col 0 row 0 → origin (0,0); each cell 100x100.
    #   x=45  = ('ML', 0.45, ...) in col 0 or (col*100 + xf*100)
    #   Using anchor tuples inside cells:

    # s1: left 竖 — slight left-lean top→bottom (as in kou family)
    s1_h = anchor_to_xy(('ML', 0.55, 0.10))   # x≈55, y≈110
    s1_t = anchor_to_xy(('BL', 0.55, 0.35))   # x≈55, y≈235

    # s2: 横折 — top bar then right wall, corner top-right of char
    s2_h = anchor_to_xy(('ML', 0.65, 0.10))   # x≈65, y≈110 (N gap from s1_h)
    s2_c = anchor_to_xy(('MR', 0.55, 0.10))   # x≈255, y≈110 (corner)
    s2_t = anchor_to_xy(('BR', 0.55, 0.35))   # x≈255, y≈235

    # s3: inner-left short stroke — slight down-left slant (撇)
    s3_h = anchor_to_xy(('C',  0.10, 0.28))   # x≈110, y≈128
    s3_t = anchor_to_xy(('BL', 0.87, 0.10))   # x≈87,  y≈210

    # s4: inner-right stroke — 竖弯 short, curves down-right
    s4_h = anchor_to_xy(('C',  0.55, 0.20))   # x≈155, y≈120
    s4_t = anchor_to_xy(('MR', 0.15, 0.90))   # x≈215, y≈190

    # s5: bottom 横 — sealing bar, near-horizontal, N gaps at both ends
    s5_h = anchor_to_xy(('BL', 0.75, 0.35))   # x≈75,  y≈235
    s5_t = anchor_to_xy(('BR', 0.45, 0.35))   # x≈245, y≈235

    w = 9
    gap = 5

    # s1: left 竖 — shorten both ends for N joints @ top-left (with s2)
    #     and bottom-left (with s5)
    fat_line(draw, _shorten(s1_h, s1_t, gap), _shorten(s1_t, s1_h, gap), width=w)

    # s2: 横折 — top bar (s2_h -> s2_c) then right wall (s2_c -> s2_t).
    # shorten s2_h from top-left (N with s1_h), leave corner welded to
    # itself (same-stroke S), shorten s2_t at bottom-right (N with s5_t).
    fat_line(draw, _shorten(s2_h, s2_c, gap), s2_c, width=w)
    fat_line(draw, s2_c, _shorten(s2_t, s2_c, gap), width=w)
    # fill the corner
    cx, cy = s2_c; r = w / 2.0
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3: inner-left 撇 (shorten head from s2 body — N)
    fat_line(draw, _shorten(s3_h, s3_t, gap), _shorten(s3_t, s3_h, 2), width=w)

    # s4: inner-right 竖弯 (shorten head from s2 body — N)
    fat_line(draw, _shorten(s4_h, s4_t, gap), _shorten(s4_t, s4_h, 2), width=w)

    # s5: bottom 横 — sealing bar; both ends shortened (N with s1_t, s2_t)
    fat_line(draw, _shorten(s5_h, s5_t, gap), _shorten(s5_t, s5_h, gap), width=w)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_si(draw)
    out = os.path.join(_HERE, '01_四.png')
    img.save(out)
    print('wrote', out)
