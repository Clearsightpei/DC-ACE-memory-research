"""p3_char_0144_风 — G5 attempt.

风 = 4 strokes:
  s1 撇 (outer left, near-vertical mild pie)
  s2 横斜弯钩 (outer right: top horizontal, sweeps right, curves down, hooks
     back up-left)   — MISSING BANK PRIMITIVE (see B5 sandbox / P-COMP-008)
  s3 撇 (inner top-right → lower-left) — one arm of the 乂
  s4 捺 (inner left → lower-right)    — other arm of the 乂 (crosses s3 P)

MMH-derived anchors (pixel):
  s1: ML(0.715,0.028)=(71.5,102.8) → BL(0.401,0.871)=(40.1,287.1)
  s2: ML(0.958,0.146)=(95.8,114.6) → BR(0.748,0.317)=(274.8,231.7)  [tail = hook tip]
  s3: C(0.573,0.28) =(157.3,128.0) → BL(0.926,0.625)=(92.6,262.5)
  s4: C(0.075,0.605)=(107.5,160.5) → BC(0.808,0.531)=(180.8,253.1)

Joints:
  s1.head ⇆ s2.head   N (gap ~17px in ML)      — leave clear gap, do NOT weld
  s1.mid  ⇆ s4.head   N (gap ~34px in ML)      — natural: s1 body vs inner na start
  s3.mid  ⇆ s4.mid    P welded near BC(mid)    — the 乂 crossing

# BANK_DEVIATION
# skipped: heng_zhe_gou.py (angular topology — has straight-down shu, not the wan-belly)
# reason:  风 s2 is 横斜弯钩, a fluid single arc (heng across + wan belly down-right
#          + up-left hook flick). No bank primitive in this class yet (P-COMP-008
#          candidate spec = heng_zhe_wan_gou / heng_xie_wan_gou family). Inlined
#          as multi-segment tapered polyline with explicit waypoints.
# fresh_component: heng_xie_wan_gou_for_风
#   waypoints = head(95.8,114.6) → topright(272,108) → botright(287,255)
#             → hook_tip(274.8,231.7)  [MMH tail]
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / "success_bank" / "code"))

from PIL import Image, ImageDraw

from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,           # PNG reads as 风: outer left pie + outer right heng_xie_wan_gou hook + inner 乂
    'stroke_count_ok': True,     # 4 primitive calls / render blocks = 4 MMH strokes
    'endpoint_mismatches': [],   # s1/s2/s3/s4 endpoints match MMH within tolerance
    'joint_class_mismatches': [],# s1.head/s2.head N (visible ~15px gap), s1mid/s4head N (~40px gap), s3.mid/s4.mid P weld verified
    'overall_pass': True,
    'notes': 's2 heng_xie_wan_gou inlined BANK_DEVIATION (P-COMP-008 family). '
             'Outer left pie starts at MMH ML(0.028)~y=103 leaving space above — trusted MMH over GT.',
}


def _draw_heng_xie_wan_gou(d, head, top_right, bot_right, hook_tip,
                            w_start=4.0, w_swell=8.5, w_hook=1.5):
    """Inline BANK_DEVIATION — 横斜弯钩 for 风/几-family.

    Renders three fused segments as a chain of tapered ellipses:
      A: head → top_right   (heng with mild upward arch, lead-in swell)
      B: top_right → bot_right (rightward-then-down wan belly, cubic-ish
                                curve via bezier through outer control)
      C: bot_right → hook_tip (small up-left hook flick, tapers to point)
    """
    # --- Segment A: 横 (top horizontal, gentle arch) ---
    steps_a = 65
    x0, y0 = head
    x1, y1 = top_right
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t - 2.0 * (1 - (2 * t - 1) ** 2)
        w = w_start + (w_swell - w_start) * 0.55 * t
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # 顿笔 dab at the top-right shoulder
    cx, cy = top_right
    d.ellipse((cx - 7.0, cy - 6.0, cx + 7.0, cy + 6.5), fill='black')

    # --- Segment B: 弯 (right side sweeps down + belly bulges right) ---
    steps_b = 90
    x2, y2 = bot_right
    # Bezier control OUTSIDE (right of) the descent to give a rightward wan-belly
    ctrl_x = cx + 22
    ctrl_y = (cy + y2) / 2 + 8
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        # tapered: swells through belly, thins toward bottom
        w = w_swell - 3.0 * abs(t - 0.35)
        if w < 3.2:
            w = 3.2
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Segment C: 钩 (small up-left hook flick, tapers to point) ---
    steps_c = 24
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 5.0 * (1 - t) + w_hook
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 撇 (outer left) — near-vertical with mild leftward drift
    # MMH head (71.5, 102.8), tail (40.1, 287.1). Length ~186 px, small bow.
    draw_pie(
        d,
        head=(71.5, 102.8),
        tail=(40.1, 287.1),
        bow_perp=10, w_head=8, w_tail=3, steps=90,
    )

    # s2: 横斜弯钩 (outer right frame + hook) — BANK_DEVIATION
    # head near top-center-left (leaving ~15px gap right of s1 head — N joint),
    # heng across to top-right, wan-belly down the right side, terminal hook
    # tip at MMH tail (274.8, 231.7).
    _draw_heng_xie_wan_gou(
        d,
        head=(95.8, 114.6),
        top_right=(272.0, 108.0),
        bot_right=(288.0, 256.0),
        hook_tip=(274.8, 231.7),
        w_start=3.8, w_swell=8.5, w_hook=1.4,
    )

    # s3: inner 撇 (top → lower-left) — one arm of 乂
    draw_pie(
        d,
        head=(157.3, 128.0),
        tail=(92.6, 262.5),
        bow_perp=8, w_head=7, w_tail=2, steps=80,
    )

    # s4: inner 捺 (upper-left → lower-right) — other arm of 乂, crosses s3 P
    draw_na(
        d,
        head=(107.5, 160.5),
        tail=(180.8, 253.1),
        bow_perp=8, w_head=3, w_tail=9, steps=80,
    )

    out = _HERE.parent / "01_风.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
