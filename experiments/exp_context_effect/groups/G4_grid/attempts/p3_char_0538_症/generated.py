"""p3_char_0538_症 — sickness radical 疒 + 正 inside.

Decomposition: 疒 (strokes 1-5) top-left frame + 正 (strokes 6-10) inside.

Bank lookup (per memory_index.md v8 checklist):
  1. drawer_memory.md — 疒 named-pattern (B13 recipe from 疽 A + 疸 PASS).
     No chronic/ne_sick.py — inline all 5 疒 strokes MMH-verbatim.
     Interior 正 also inline MMH-verbatim (zhi_stop.py exists but the
     MMH slot compresses 正 into bottom-right — full-canvas would overrun).
  2. INDEX.md grep — 症 not mastered. 疽 (0528) is closest sibling; reuse
     its 疒 frame primitives directly with same widths/curves.
  3. errata.md grep 症 — not present. 疒 cluster note: keep interior crisp
     inside the frame, MMH-verbatim endpoints, no full-canvas primitive.

Expected 10 strokes (from MMH block):
  s1  TC(.474,.577) -> TC(.808,.817)    top-right dot (点)
  s2  C (.084,.178) -> MR(.332,.014)    top short heng (亠 bar)
  s3  ML(.861,.102) -> BL(.401,.979)    long 撇 sweep (frame left)
  s4  ML(.466,.342) -> ML(.677,.597)    inner upper dot
  s5  BL(.199,.229) -> ML(.782,.980)    inner lower rising 提
  s6  C (.327,.635) -> MR(.265,.515)    正 top heng
  s7  C (.673,.693) -> BC(.717,.669)    正 left short vertical
  s8  BC(.852,.165) -> BR(.335,.065)    正 middle heng (long)
  s9  BC(.198,.054) -> BC(.327,.710)    正 middle vertical
  s10 BL(.861,.821) -> BR(.646,.751)    正 bottom long heng

All 6 joints N-class (natural small gaps, do NOT weld):
  s2.head ⇆ s3.head @ C     ~16 px  (top-heng meets 撇 top)
  s3.mid  ⇆ s5.tail @ BL    ~17 px  (撇 body vs inner-ti tail)
  s6.mid  ⇆ s7.head @ C     ~13 px  (正 top-heng vs left-vert top)
  s7.mid  ⇆ s8.head @ BC    ~15 px  (正 left-vert vs middle-heng)
  s7.tail ⇆ s10.mid @ BC    ~17 px  (正 left-vert tail vs bottom-heng)
  s9.tail ⇆ s10.mid @ BC    ~16 px  (正 mid-vert tail vs bottom-heng)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 10 primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 frame from B13 canonical recipe (疽/疸) + 正 five strokes '
             'inline MMH-verbatim; all 6 joints N-class small gaps, no welds.'
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

    # s1 — top-right dot (点), short tapered pie
    h = anchor_to_xy(('TC', 0.474, 0.577))
    t = anchor_to_xy(('TC', 0.808, 0.817))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2 — top short heng (亠 top bar)
    h = anchor_to_xy(('C', 0.084, 0.178))
    t = anchor_to_xy(('MR', 0.332, 0.014))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # s3 — long 撇 sweep (left-falling frame)
    h = anchor_to_xy(('ML', 0.861, 0.102))
    t = anchor_to_xy(('BL', 0.401, 0.979))
    ctrl = (h[0] - 20, h[1] + (t[1] - h[1]) * 0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(3 + 4 * (1 - abs(2 * u - 1)))  # bulge in middle
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper dot (short thick pie)
    h = anchor_to_xy(('ML', 0.466, 0.342))
    t = anchor_to_xy(('ML', 0.677, 0.597))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s5 — inner lower rising 提 (ti)
    h = anchor_to_xy(('BL', 0.199, 0.229))
    t = anchor_to_xy(('ML', 0.782, 0.980))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ============ 正 INTERIOR (strokes 6-10) ============

    # s6 — 正 top heng (rising slightly)
    h = anchor_to_xy(('C', 0.327, 0.635))
    t = anchor_to_xy(('MR', 0.265, 0.515))
    fat_line(d, h, t, 5)

    # s7 — 正 left short vertical
    h = anchor_to_xy(('C', 0.673, 0.693))
    t = anchor_to_xy(('BC', 0.717, 0.669))
    fat_line(d, h, t, 5)

    # s8 — 正 middle heng (long, rising rightward)
    h = anchor_to_xy(('BC', 0.852, 0.165))
    t = anchor_to_xy(('BR', 0.335, 0.065))
    fat_line(d, h, t, 4)

    # s9 — 正 middle vertical (long)
    h = anchor_to_xy(('BC', 0.198, 0.054))
    t = anchor_to_xy(('BC', 0.327, 0.710))
    fat_line(d, h, t, 5)

    # s10 — 正 bottom long heng (extends beyond right of frame)
    h = anchor_to_xy(('BL', 0.861, 0.821))
    t = anchor_to_xy(('BR', 0.646, 0.751))
    fat_line(d, h, t, 6)

    out = os.path.join(HERE, '01_症.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
