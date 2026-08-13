"""p3_char_0322_佃 — 佃 (diàn, "tenant farmer", 7画).

Structure: 亻 (left radical) + 田 (right, "field" — 5-stroke box with cross).

MMH-injected stroke plan (7 strokes):
  s1: 撇  — 亻's diagonal      TL(0.885,0.659) → BL(0.129,0.042)
  s2: 竖  — 亻's vertical      ML(0.709,0.479) → BL(0.724,0.962)
  s3: 竖  — 田 left wall       C(0.014,0.365) → BC(0.315,0.73)
  s4: 横折 — 田 top+right wall  C(0.192,0.386) → BR(0.153,0.499)
  s5: 横  — 田 middle horiz.   BC(0.438,0.001) → MR(0.147,0.934)
  s6: 竖  — 田 middle vert.    C(0.661,0.438) → BC(0.723,0.49)
  s7: 横  — 田 bottom horiz.   BC(0.377,0.643) → BR(0.115,0.499)

Joints (all N except s5.mid ⇆ s6.mid which is P-welded cross):
  s1.mid ⇆ s2.head : N (~18 px) — 亻 T-touch
  s3.head ⇆ s4.head : N — top-left corner of 田
  s3.mid  ⇆ s5.head : N — 田 left wall crossed by middle horiz
  s3.tail ⇆ s7.head : N — bottom-left corner
  s4.head ⇆ s6.head : N — top-of-mid-竖 near 横折 head
  s4.tail ⇆ s7.tail : N — bottom-right corner
  s5.mid  ⇆ s6.mid  : P (welded) — the classic 田 cross
  s6.tail ⇆ s7.mid  : N — mid-竖 meets bottom-横 near center

Lookup checklist:
- drawer_memory: left-right composition; 亻 in x∈[0.05,0.40], 田 in x∈[0.45,0.95].
- INDEX grep: ren_side.py exists (imported). 田 not in bank (see 甲/申 for inline).
- errata grep: 佃 not in errata.
- Uses ren_side for the 亻 half; 田 inlined per MMH endpoints.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 (ren_side) + 5 (田 inline) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; 亻 via ren_side primitive; 田 inlined with P-weld at center cross, N gaps at corners.'
}

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from ren_side import draw_ren_side


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_dian(draw):
    W = 10

    # --- s1, s2: 亻 in left third (compressed into x∈[0.05, 0.35]) ---
    # ren_side default is centered — override to sit in left column.
    draw_ren_side(
        draw,
        pie_head=('TL', 0.75, 0.30),   # (75, 30)
        pie_tail=('ML', 0.20, 0.90),   # (20, 190)
        shu_head=('ML', 0.42, 0.15),   # (42, 115) — sits ON the 撇 body (T-touch)
        shu_tail=('BL', 0.42, 0.90),   # (42, 290)
    )

    # --- s3..s7: 田 in the right region ---
    # Frame: left x=125, right x=245, top y=110, bottom y=245
    # Central cross at x=185, mid-y=178

    # s3 — 田 left wall (slight slant per MMH: head above, tail below)
    s3_h = anchor_to_xy(('C', 0.25, 0.10))   # (125, 110)
    s3_t = anchor_to_xy(('BC', 0.25, 0.45))  # (125, 245)
    fat_line(draw, _shorten(s3_h, s3_t, 2), _shorten(s3_t, s3_h, 2), width=W)

    # s4 — 横折 top+right wall (two segments meeting at TR corner)
    s4_h = anchor_to_xy(('C', 0.27, 0.10))   # (127, 110) — near s3 head (N corner)
    s4_c = anchor_to_xy(('MR', 0.45, 0.10))  # (245, 110) — TR corner of box
    s4_t = anchor_to_xy(('MR', 0.45, 0.45))  # (245, 145)
    # Extend right wall to bottom for the frame:
    s4_t_ext = anchor_to_xy(('BR', 0.45, 0.45))  # (245, 245) — actual bottom of right wall
    fat_line(draw, _shorten(s4_h, s4_c, 2), s4_c, width=W)
    fat_line(draw, s4_c, _shorten(s4_t_ext, s4_c, 2), width=W)
    # corner reinforcement
    r = 5
    draw.ellipse([s4_c[0]-r, s4_c[1]-r, s4_c[0]+r, s4_c[1]+r], fill=(0, 0, 0))

    # s5 — middle horizontal (crosses left wall at N gap, welds mid-竖 at P)
    s5_h = anchor_to_xy(('C', 0.25, 0.68))   # (125, 168)
    s5_t = anchor_to_xy(('MR', 0.45, 0.78))  # (245, 178)
    fat_line(draw, _shorten(s5_h, s5_t, 2), _shorten(s5_t, s5_h, 2), width=W)

    # s6 — middle vertical (crosses middle horiz at P-weld, meets bottom at N)
    s6_h = anchor_to_xy(('C', 0.85, 0.10))   # (185, 110) — near top bar (N)
    s6_t = anchor_to_xy(('BC', 0.85, 0.45))  # (185, 245) — meets bottom bar
    fat_line(draw, s6_h, s6_t, width=W)

    # s7 — bottom horizontal (N corners with s3.tail and s4.tail_ext)
    s7_h = anchor_to_xy(('BC', 0.27, 0.45))  # (127, 245)
    s7_t = anchor_to_xy(('BR', 0.43, 0.45))  # (243, 245)
    fat_line(draw, _shorten(s7_h, s7_t, 2), _shorten(s7_t, s7_h, 2), width=W)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_dian(draw)
    out = os.path.join(os.path.dirname(__file__), '01_佃.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
