"""p3_char_0374_疙 (ge, 'pimple') — 疒 shell (5 strokes) + 乞 inside (3 strokes) = 8.

Composition analysis per MMH structural block:
- Strokes 1-5 = 疒 (sickness radical): top dot + rising heng + long pie
  + inside dot + inside ti. Same recipe as p3_char_0171_疒 PASSed
  layout, endpoints re-derived from THIS char's MMH anchors
  (疒 sits slightly wider here since 乞 fills the wrap).
- Strokes 6-8 = 乞: short 撇 + short 一 + 乙-body hook. Same recipe
  as p3_char_0187_仡's 乞 sub-render (draw_pie + draw_heng + inline
  bezier hook body), but scaled/translated per MMH.

Bank primitives called: dian, heng, pie, ti — verbatim MMH anchors.
乙 hook body is inline (bank has no 乙-body-only entry; yi_second is
a full 乙 with top curve which 乞's s6+s7 already provide).

Per P-A-006 / P-A-008: inline reasoning-trace for each sub-component
in this docstring. No bank whole-radical entry exists for 疒 (checked
INDEX — only guang_wide.py 广; MMH anchors here diverge from 广 bank's
hardcoded coords), so composition proceeds from stroke primitives.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from ti import draw_ti


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 primitive/inline calls, matches MMH 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 6 joints are N; gaps preserved
    'overall_pass': True,
    'notes': ('8 strokes: 5 for 疒 (dian+heng+pie+dian+ti) + 3 for 乞 '
              '(pie+heng+inline 乙 body). N-gaps preserved between '
              's2/s3 heads, s5.tail~s3, s6-s7-s8 vs s3.'),
}


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_qi_hook_body(d, head, belly, tail, w=6):
    """乙-body hook: sweep from head down through belly, then hook up to tail.
    Two bezier segments meeting at belly. Used for 乞's s8."""
    seg1 = _bezier(head, (head[0] + 25, belly[1] - 15), belly, steps=50)
    seg2 = _bezier(belly, (tail[0] - 5, belly[1] + 5), tail, steps=50)
    segs = seg1 + seg2
    for i in range(len(segs) - 1):
        d.line([segs[i], segs[i + 1]], fill='black', width=w)
    r = int(w * 0.55)
    for p in (head, tail):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill='black')


def draw(d: ImageDraw.ImageDraw):
    # ---- 疒 shell (strokes 1-5) ----

    # s1: top dot (丶) — MMH TC(0.377,0.571) -> TC(0.731,0.794)
    draw_dian(d, (137.7, 57.1), (173.1, 79.4),
              w_head=3, w_tail=8, bow=3)

    # s2: heng (一) — MMH C(0.075,0.116) -> TR(0.288,0.993)
    # Slightly rising to the right (top of 疒 shell). Head kept ~24px right
    # of s3.head to preserve the N-gap the joint spec asks for (~18px).
    draw_heng(d, (107.5, 111.6), (228.8, 99.3),
              width_head=8, width_tail=9)

    # s3: long 撇 (丿) — MMH ML(0.838,0.055) -> BL(0.24,0.982)
    # Full-height pie sweeping bottom-left, spine of 疒.
    draw_pie(d, (83.8, 105.5), (24.0, 298.2),
             bow_perp=16, w_head=9, w_tail=3, steps=80)

    # s4: inside dot (丶) — MMH ML(0.34,0.4) -> ML(0.598,0.655)
    # Small dot in middle-left, sits INSIDE the 疒 shell (冫-like left mark).
    draw_dian(d, (34.0, 140.0), (59.8, 165.5),
              w_head=3, w_tail=6, bow=2)

    # s5: inside 提 — MMH BL(0.188,0.262) -> ML(0.797,0.986)
    # Short rising stroke, tail lands ~22px inside pie curve (N-gap kept).
    draw_ti(d, (18.8, 226.2), (79.7, 198.6),
            w_head=8, w_tail=2, steps=50)

    # ---- 乞 inside (strokes 6-8) ----

    # s6: 乞's 撇 — MMH C(0.324,0.289) -> C(0.034,0.992)
    draw_pie(d, (132.4, 128.9), (103.4, 199.2),
             bow_perp=6, w_head=7, w_tail=3, steps=70)

    # s7: 乞's 一 — MMH C(0.383,0.667) -> MR(0.186,0.485)
    # Slight rising to right, sits below s6 pie mid.
    draw_heng(d, (138.3, 166.7), (218.6, 148.5),
              width_head=6, width_tail=7)

    # s8: 乙-body hook — MMH BC(0.257,0.001) -> BR(0.528,0.408)
    # Head (125,200) sweeps down through belly (~180,278) then hooks up-right
    # to tail (252,240). N-joint w/ s6 mid preserved (~30px gap).
    draw_qi_hook_body(d, (125.7, 200.1), (185.0, 282.0), (252.8, 240.8), w=6)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_疙.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
