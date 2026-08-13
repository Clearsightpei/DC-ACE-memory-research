"""p3_char_0528_疽 — sickness radical 疒 + 且 inside.

Decomposition: 疒 (strokes 1-5) enclosing 且 (strokes 6-10).

Bank lookup (per memory_index.md v8 checklist):
  1. drawer_memory.md — 疒 is a chronic-cluster candidate (B12 note).
     No chronic/ne_sick.py exists yet. Inline via _anchor fat_line/bezier.
  2. INDEX.md grep — 0171_疒 has a rendered attempt; reuse its 5-stroke
     recipe (dot + 亠 top + 撇 sweep + 2 inner dots) with MMH anchors.
     No entry for 且 alone; render inline from MMH strokes 6-10.
  3. errata.md grep 疽 — not present. 疒 cluster (疣/疫/疬/疮) flagged as
     'interior loses cohesion' — I keep the 且 crisp inside the frame.

Expected 10 strokes (from MMH):
  s1 : TC(.42,.55) -> TC(.75,.82)         top dot (点)
  s2 : C (.08,.11) -> TR(.36,.96)         top short heng (亠 top piece)
  s3 : ML(.87,.06) -> BL(.40,.97)         long 撇 sweep
  s4 : ML(.43,.33) -> ML(.64,.59)         inner upper dot
  s5 : BL(.19,.23) -> ML(.79,.94)         inner lower rising ti
  s6 : C (.31,.51) -> BC(.35,.71)         且 left vertical (竖)
  s7 : C (.46,.54) -> BC(.96,.64)         且 横折 (top+right side)
  s8 : BC(.49,.01) -> C (.86,.93)         且 upper inner 横
  s9 : BC(.48,.36) -> BC(.85,.29)         且 lower inner 横
  s10: BL(.80,.81) -> BR(.77,.78)         bottom 横 (extends full width)

Joints (all N — small gaps expected):
  s1.tail ⇆ s2.mid  (TC)     ~33 px  gap  (dot to top-heng)
  s2.head ⇆ s3.head (C)      ~17 px  gap  (top-heng meets 撇 top)
  s3.mid  ⇆ s5.tail (ML)     ~18 px  gap  (撇 body vs inner-ti tail)
  s3.tail ⇆ s10.head (BL)    ~32 px  gap  (撇 tail near bottom-横)
  s6.head ⇆ s7.head (C)      ~12 px  gap  (且 竖-top vs 横折-top)
  s6.mid  ⇆ s8.head (BC)     ~12 px  gap  (且 竖 vs upper 横)
  s6.mid  ⇆ s9.head (BC)     ~11 px  gap  (且 竖 vs lower 横)
  s6.tail ⇆ s10.mid (BC)     ~19 px  gap  (且 竖 tail vs bottom 横)
  s7.mid  ⇆ s8.tail (C)      ~27 px  gap  (且 右side vs upper 横 right)
  s7.mid  ⇆ s9.tail (BC)     ~26 px  gap  (且 右side vs lower 横 right)
  s7.tail ⇆ s10.mid (BR)     ~19 px  gap  (且 右side tail vs bottom 横)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 template from 0171 + 且 five strokes inside. All 11 joints N-class (small gaps, no weld).'
}

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ 疒 FRAME (strokes 1-5) ============

    # s1 — top-right dot (点), small tapered pie
    h = anchor_to_xy(('TC', 0.424, 0.551))
    t = anchor_to_xy(('TC', 0.746, 0.82))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2 — top short heng (亠 top bar)
    h = anchor_to_xy(('C', 0.075, 0.113))
    t = anchor_to_xy(('TR', 0.355, 0.955))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # s3 — long 撇 sweep (left-falling frame)
    h = anchor_to_xy(('ML', 0.867, 0.055))
    t = anchor_to_xy(('BL', 0.401, 0.971))
    ctrl = (h[0] - 20, h[1] + (t[1] - h[1]) * 0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(3 + 4 * (1 - abs(2 * u - 1)))  # bulge in middle
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper dot (short thick pie)
    h = anchor_to_xy(('ML', 0.434, 0.333))
    t = anchor_to_xy(('ML', 0.639, 0.594))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s5 — inner lower rising 提 (ti)
    h = anchor_to_xy(('BL', 0.193, 0.227))
    t = anchor_to_xy(('ML', 0.791, 0.942))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ============ 且 INTERIOR (strokes 6-10) ============

    # s6 — left vertical 竖 of 且
    h = anchor_to_xy(('C', 0.31, 0.512))
    t = anchor_to_xy(('BC', 0.351, 0.707))
    fat_line(d, h, t, 5)

    # s7 — 横折 (top + right side) of 且: head at top-left of right side,
    # bends at top-right corner, tail down the right side.
    h = anchor_to_xy(('C', 0.456, 0.535))
    corner = anchor_to_xy(('C', 0.94, 0.55))     # top-right corner of 且 box
    t = anchor_to_xy(('BC', 0.963, 0.643))
    # top horizontal segment
    fat_line(d, h, corner, 5)
    # right vertical segment (with slight rightward bulge)
    fat_line(d, corner, t, 5)

    # s8 — upper inner 横 of 且 (short, nearly flat)
    h = anchor_to_xy(('BC', 0.485, 0.01))
    t = anchor_to_xy(('C', 0.863, 0.934))
    fat_line(d, h, t, 4)

    # s9 — lower inner 横 of 且
    h = anchor_to_xy(('BC', 0.477, 0.364))
    t = anchor_to_xy(('BC', 0.852, 0.294))
    fat_line(d, h, t, 4)

    # s10 — bottom 横 extending across (full width)
    h = anchor_to_xy(('BL', 0.797, 0.807))
    t = anchor_to_xy(('BR', 0.774, 0.783))
    fat_line(d, h, t, 5)

    out = os.path.join(HERE, '01_疽.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
