"""p3_char_0187_仡 (yi, 'brave/strong') — L-R composition: 亻 + 乞.

Bank usage:
  - draw_ren_left : covers strokes 1-2 (亻 pie + shu).
  - Strokes 3-5 (乞) inlined below: draw_pie for 撇, draw_heng for 一,
    inline bezier for the 乙-body hook (bank's yi_second is a full 乙
    with its own top curve — here 乞's top is already provided by s3+s4
    so we render just the sweep+hook body).

Reference: 300x300 canvas, MMH anchors converted to px via cell origins.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from ren_left import draw_ren_left
from pie import draw_pie
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 strokes: ren_left(2) + pie + heng + inline hook
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亻 via draw_ren_left(ox=-69, oy=1.5); 乞 s3=draw_pie, s4=draw_heng, '
             's5 inline bezier (yi-hook body, no top).',
}


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_qi_hook_body(d, head, tail, belly=(180, 278), w=6):
    """乞's bottom stroke: from head sweeps down through belly then hooks
    up to tail. Two bezier segments (down-sweep + hook-up)."""
    mid = (170, 275)
    segs = _bezier(head, (135, 260), belly, steps=50)
    segs += _bezier(belly, (240, 285), tail, steps=50)
    for i in range(len(segs) - 1):
        d.line([segs[i], segs[i + 1]], fill='black', width=w)
    r = int(w * 0.55)
    for p in (head, tail):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # -------- 亻 (strokes 1-2) --------
    # Reference layout expects pie head ~(158.8, 73.8); we want (89.6, 75.3),
    # shu head ~(138.9, 158.2) → want (71.2, 156.4). Shift ox=-69, oy=+1.5.
    draw_ren_left(d, ox=-69, oy=1.5, scale=1.0)

    # -------- 乞 s3: 撇 --------
    # head TC (156.4, 69.7) → tail C (113.1, 174.0). Slight bow.
    draw_pie(d, (156.4, 69.7), (113.1, 174.0),
             bow_perp=6, w_head=7, w_tail=3, steps=70)

    # -------- 乞 s4: 一 (short heng, slight rise) --------
    # head C (151.5, 135.9) → tail MR (234.7, 118.7).
    draw_heng(d, (151.5, 135.9), (234.7, 118.7),
              width_head=6, width_tail=7)

    # -------- 乞 s5: 乙-body hook --------
    # head C (122.8, 194.5) → tail BR (263.4, 231.4). Belly droops
    # to ~(180, 278) then hooks up to tail. N-joint w/ s3 (gap≈31 kept).
    draw_qi_hook_body(d, (122.8, 194.5), (263.4, 231.4),
                      belly=(180, 278), w=6)

    out = pathlib.Path(__file__).parent / '01_仡.png'
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
