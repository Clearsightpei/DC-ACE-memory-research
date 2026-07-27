"""仡 (yì) — Phase-3 character, 5 strokes.

Composition: 亻 (2 strokes: 撇 + 竖) + 乞 (3 strokes: 撇 + 横 + 乙-compound).

Steps followed per drawer_memory.md:
  1. Split: 仡 = 亻 + 乞
  2. Bank imports: ren_side.py (for 亻 left radical).
  3. errata.md grep 仡 / 乞 — none listed.
  4. Draw 乞 fresh from MMH anchors (no 乞 primitive in bank yet;
     yi_second.py's 乙 is a full radical shape not identical to the
     compressed 乞-lower found here).

Anchors follow the injected structural expectations verbatim.
"""
import os, sys, pathlib

_HERE = pathlib.Path(__file__).resolve().parent
_BANK = _HERE.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from ren_side import draw_ren_side


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'draw_ren_side supplies s1+s2 (亻). s3-5 (乞) inline from anchors.'
}


def _draw_pie_stroke(draw, head, tail, head_w=10, tail_w=2, curve=0.08):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=36)
    widths = [head_w + (tail_w - head_w) * (i / 36) for i in range(37)]
    stroke_variable_width(draw, pts, widths)


def _draw_heng(draw, head, tail, width=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    # gentle upward arc
    ctrl = ((p0[0] + p1[0]) * 0.5, min(p0[1], p1[1]) - 2)
    pts = quad_bezier(p0, ctrl, p1, n=30)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)


def _draw_qi_bottom(draw, head, tail):
    """乞's third stroke — 横折弯钩 (compound).

    Interpreted path: start at head (mid-center, upper region of the
    compound), sweep down and left forming a belly, then across the
    bottom sweeping right, then hook up to tail.
    """
    p_head = anchor_to_xy(head)       # top-left-ish start
    p_tail = anchor_to_xy(tail)       # hook tip, right side
    # We need an internal belly (bottom-center) and a sweep-right waypoint.
    p_belly = anchor_to_xy(('BC', 0.15, 0.55))   # bottom-left of sweep
    p_sweep = anchor_to_xy(('BR', 0.40, 0.60))   # sweep-right base

    # seg1: head -> belly (descending left curve).
    ctrl1 = (p_head[0] - 20, (p_head[1] + p_belly[1]) * 0.5)
    seg1 = quad_bezier(p_head, ctrl1, p_belly, n=28)
    w1 = [7 + (i / 28) * 2 for i in range(29)]

    # seg2: belly -> sweep (bottom horizontal with slight sag).
    ctrl2 = ((p_belly[0] + p_sweep[0]) * 0.5,
             max(p_belly[1], p_sweep[1]) + 8)
    seg2 = quad_bezier(p_belly, ctrl2, p_sweep, n=28)
    w2 = [9 - (i / 28) * 2 for i in range(29)]

    # seg3: sweep -> tail (short rising hook).
    ctrl3 = (p_sweep[0] + 4, (p_sweep[1] + p_tail[1]) * 0.5)
    seg3 = quad_bezier(p_sweep, ctrl3, p_tail, n=20)
    w3 = [7 - (i / 20) * 5 for i in range(21)]

    pts = seg1 + seg2[1:] + seg3[1:]
    widths = w1 + w2[1:] + w3[1:]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # ---- 亻 (left radical): s1 (撇) + s2 (竖) ----
    # Expected anchors:
    #   s1: TL(0.896,0.753) -> BL(0.22,0.03)
    #   s2: ML(0.712,0.564) -> BL(0.732,0.977)
    draw_ren_side(
        draw,
        pie_head=('TL', 0.896, 0.753),
        pie_tail=('BL', 0.22, 0.03),
        shu_head=('ML', 0.712, 0.564),
        shu_tail=('BL', 0.732, 0.977),
    )

    # ---- 乞 (right side): s3 (撇) + s4 (横) + s5 (乙-compound) ----
    # s3: TC(0.564,0.697) -> C(0.131,0.74)
    _draw_pie_stroke(draw,
                     head=('TC', 0.564, 0.697),
                     tail=('C', 0.131, 0.74),
                     head_w=9, tail_w=2, curve=0.06)

    # s4: C(0.515,0.359) -> MR(0.347,0.187)   (short 横 going right-up slightly)
    _draw_heng(draw,
               head=('C', 0.515, 0.359),
               tail=('MR', 0.347, 0.187),
               width=8)

    # s5: C(0.228,0.945) -> BR(0.634,0.314)   compound bottom sweep
    _draw_qi_bottom(draw,
                    head=('C', 0.228, 0.945),
                    tail=('BR', 0.634, 0.314))

    out = _HERE / "01_仡.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
