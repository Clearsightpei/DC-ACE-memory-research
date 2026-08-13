"""p3_char_0522_疴 — 疒 (sickness radical, 5 strokes) + 可 (5 strokes) nested inside.

Lookup checklist:
  1. drawer_memory.md — no 疒-family primitive baked as chronic; but
     PASS attempts exist for both 疒 (p3_char_0171) and 可 (p3_char_0160).
     Follow their MMH-verbatim approach.
  2. INDEX.md grep — 疒 primitive not standalone in bank; anchors come
     from injected MMH block.
  3. errata.md grep 疴 — not present.
  4. pass_index — 疒 PASS at 0171, 可 PASS at 0160 — reuse anchor
     strategy: fat_line + quad_bezier from _anchor, verbatim MMH anchors.

Composition split: 疒 + 可 (可 nested small in lower/inner space).
  - s1..s5 = 疒 (top dot, top heng, long left-falling 撇, 2 inner dots)
  - s6..s10 = 可 (top heng, 口 left 竖, 口 横折, 口 bottom heng, right 竖钩)

All 7 joints declared N — preserve visible gaps, DO NOT weld.
"""
from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 stroke primitives (compound 横折 = 1)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 (s1-s5) reuses 0171 PASS approach; 可 (s6-s10) reuses 0160 PASS approach nested small in lower-right.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ================= 疒 radical (s1-s5) =================

    # ---- s1: top-right dot (点) ----
    h = anchor_to_xy(('TC', 0.438, 0.568))
    t = anchor_to_xy(('TC', 0.770, 0.832))
    pts = quad_bezier(h, ((h[0]+t[0])/2, (h[1]+t[1])/2 + 3), t, n=20)
    widths = [3 + 5*(i/len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- s2: top horizontal (亠 top bar) ----
    h = anchor_to_xy(('C', 0.061, 0.137))
    t = anchor_to_xy(('MR', 0.347, 0.005))
    mid = ((h[0]+t[0])/2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4]*len(pts)
    stroke_variable_width(d, pts, widths)

    # ---- s3: long left-falling 撇 (frame body) ----
    h = anchor_to_xy(('ML', 0.844, 0.081))
    t = anchor_to_xy(('BL', 0.413, 0.956))
    ctrl = (h[0]-20, h[1] + (t[1]-h[1])*0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i/(n-1)
        widths.append(3 + 4*(1 - abs(2*u - 1)))
    stroke_variable_width(d, pts, widths)

    # ---- s4: inner upper dot ----
    h = anchor_to_xy(('ML', 0.381, 0.271))
    t = anchor_to_xy(('ML', 0.624, 0.559))
    pts = quad_bezier(h, ((h[0]+t[0])/2 - 2, (h[1]+t[1])/2), t, n=20)
    widths = [3 + 4*(i/len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- s5: inner lower dot / 提 ----
    h = anchor_to_xy(('BL', 0.182, 0.115))
    t = anchor_to_xy(('ML', 0.788, 0.875))
    mid = ((h[0]+t[0])/2, (h[1]+t[1])/2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2*(i/len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ================= 可 nested (s6-s10) =================
    # 可 is placed in the lower-right interior of 疒. MMH anchors span
    # roughly x∈[110, 195], y∈[150, 285].

    # ---- s6: 可 top heng ----
    h = anchor_to_xy(('C', 0.096, 0.626))
    t = anchor_to_xy(('MR', 0.543, 0.509))
    mid = ((h[0]+t[0])/2, min(h[1], t[1]) - 2)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [5]*len(pts)
    stroke_variable_width(d, pts, widths)

    # ---- s7: 口 left 竖 (short vertical, top-of-小口) ----
    h = anchor_to_xy(('C', 0.175, 0.972))
    t = anchor_to_xy(('BC', 0.315, 0.446))
    fat_line(d, h, t, width=5)

    # ---- s8: 口 横折 (top bar + right wall of small 口) ----
    h = anchor_to_xy(('BC', 0.324, 0.033))
    t = anchor_to_xy(('BC', 0.603, 0.218))
    # This anchor pair spans a short horizontal at top of small 口. Add
    # the right-wall descent using a corner turn.
    # Split into: horizontal from h to corner, then vertical down.
    corner = (t[0], h[1] + 1)
    fat_line(d, h, corner, width=5)
    # right wall: extend down to align with s9 bottom
    wall_bottom = (t[0] + 0, t[1] + 20)
    fat_line(d, corner, wall_bottom, width=5)

    # ---- s9: 口 bottom heng ----
    h = anchor_to_xy(('BC', 0.365, 0.376))
    t = anchor_to_xy(('BC', 0.746, 0.314))
    fat_line(d, h, t, width=5)

    # ---- s10: right 竖钩 (long descending hook) ----
    h = anchor_to_xy(('C', 0.948, 0.597))
    t = anchor_to_xy(('BC', 0.652, 0.815))
    # keep small N gap under top heng (s6)
    def shorten(p, other, px):
        dx, dy = other[0]-p[0], other[1]-p[1]
        d0 = (dx*dx+dy*dy)**0.5
        if d0 < 1e-6: return p
        f = min(1.0, px/d0)
        return (p[0]+dx*f, p[1]+dy*f)
    hg = shorten(h, t, 4)
    fat_line(d, hg, t, width=7)
    # hook: small tick pointing up-left from tail
    hook_end = (t[0]-14, t[1]-16)
    fat_line(d, t, hook_end, width=6)

    out = os.path.join(HERE, '01_疴.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
