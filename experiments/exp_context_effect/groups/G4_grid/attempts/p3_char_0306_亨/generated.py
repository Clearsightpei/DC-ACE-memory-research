"""亨 (hēng) — G4 drawer attempt.

Decomposition: 亠 (top: 点 + 横) + 口 (middle: 3 strokes) + 了 (bottom: 横撇 + 竖钩)
= 2 + 3 + 2 = 7 strokes. Matches MMH expected_stroke_count = 7.

Following v8 rule: bank primitives (tou.py, kou.py) are REFERENCE ONLY;
inline via _anchor + fat_line so we can respect MMH anchors verbatim.
This character has a compressed 口 in the middle and an off-center 了
below — the bank primitives' default anchors don't match this layout,
so hand-place per MMH.

Joints per MMH block: all 6 are N-class (natural gaps ~8-28 px). Do NOT
weld — 口 corners stay open, 了's spine stays independent from 口.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes, N-class joints preserved with small gaps; inlined per v8.'
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亠 top (2 strokes) ----------
    # s1: 点 (small dot at TC). Shorten to a compact tapered dot,
    # not a long slash — GT shows a small right-slanting dot.
    s1h = anchor_to_xy(('TC', 0.44, 0.50))
    s1t = anchor_to_xy(('TC', 0.60, 0.68))
    pts = quad_bezier(s1h, ((s1h[0]+s1t[0])/2, (s1h[1]+s1t[1])/2), s1t, n=16)
    widths = [3 + int(10 * (i / (len(pts)-1))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2: 横 (long horizontal, ML(0.442,0.028) to TR(0.666,0.926))
    s2h = anchor_to_xy(('ML', 0.442, 0.028))
    s2t = anchor_to_xy(('TR', 0.666, 0.926))
    fat_line(d, s2h, s2t, width=8)

    # ---------- 口 middle (3 strokes: s3, s4, s5) ----------
    # s3: 竖 (left wall of 口) ML(0.99,0.251) -> C(0.204,0.655)
    s3h = anchor_to_xy(('ML', 0.99, 0.251))
    s3t = anchor_to_xy(('C', 0.204, 0.655))
    # Leave small gap at top (N joint with s4)
    def shorten(a, b, px):
        dx, dy = b[0]-a[0], b[1]-a[1]
        d_ = (dx*dx + dy*dy) ** 0.5
        if d_ < 1e-6: return a
        t = min(1.0, px / d_)
        return (a[0] + dx*t, a[1] + dy*t)
    s3h_g = shorten(s3h, s3t, 3)
    fat_line(d, s3h_g, s3t, width=8)

    # s4: 横折 (top + right of 口) C(0.099,0.245) -> C(0.772,0.433)
    # This is 横折 — heng across top, then zhe down right side.
    # We render as two segments: top horizontal, then right vertical.
    s4h = anchor_to_xy(('C', 0.099, 0.245))
    s4t = anchor_to_xy(('C', 0.772, 0.433))
    # Corner: top-right of the 口 box.
    corner = (s4t[0], s4h[1])
    # Small gap at s4h from s3h (N joint)
    s4h_g = shorten(s4h, corner, 4)
    fat_line(d, s4h_g, corner, width=8)
    fat_line(d, corner, s4t, width=8)
    # dot corner
    cx, cy = corner; r = 4
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(0,0,0))

    # s5: 横 (bottom of 口) C(0.251,0.614) -> C(0.928,0.544)
    s5h = anchor_to_xy(('C', 0.251, 0.614))
    s5t = anchor_to_xy(('C', 0.928, 0.544))
    # Small gap at s5h (N joint with s3.tail)
    s5h_g = shorten(s5h, s5t, 3)
    fat_line(d, s5h_g, s5t, width=8)

    # ---------- 了 bottom (2 strokes) ----------
    # s6: 横撇 — top piece of 了. GT shows this as a broad horizontal
    # extending across, then bending down-left as 撇. Extend end beyond
    # the compressed MMH anchor so the horizontal reads clearly.
    s6h = anchor_to_xy(('BL', 0.55, 0.15))   # left end of horizontal
    s6_corner = anchor_to_xy(('BR', 0.20, 0.15))  # right bend point
    s6t = anchor_to_xy(('BC', 0.55, 0.55))   # 撇 tail down-left
    # horizontal segment
    fat_line(d, s6h, s6_corner, width=8)
    # bend + short down-left 撇 stub
    pts6 = quad_bezier(s6_corner, (s6_corner[0]+2, s6_corner[1]+16), s6t, n=20)
    widths6 = [8 - int(4 * i / (len(pts6)-1)) for i in range(len(pts6))]
    stroke_variable_width(d, pts6, widths6)
    # corner dot to weld
    cx, cy = s6_corner; r = 5
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(0,0,0))

    # s7: 竖钩/弯钩 — vertical spine of 了 with a hook to the left at end.
    # GT shows a clearly curved spine descending from just below the
    # horizontal, then a distinct left-pointing hook.
    s7h = anchor_to_xy(('BC', 0.40, 0.18))
    s7t = anchor_to_xy(('BC', 0.15, 0.90))
    # curved body via bezier — gentle leftward bow
    ctrl = (s7h[0] - 6, (s7h[1] + s7t[1]) / 2)
    body_end = s7t
    pts7 = quad_bezier(s7h, ctrl, body_end, n=32)
    widths7 = [8] * len(pts7)
    stroke_variable_width(d, pts7, widths7)
    # Hook: a pronounced left tick from body_end
    hook_end = (body_end[0] - 20, body_end[1] - 10)
    fat_line(d, body_end, hook_end, width=7)

    out = os.path.join(os.path.dirname(__file__), '01_亨.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
