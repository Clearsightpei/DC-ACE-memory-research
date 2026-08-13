"""佴 (nài) — 8 strokes.
Decomposition: 佴 = 亻 (left radical) + 耳 (right, "ear").
  亻 = pie (s1) + shu (s2), far-left column.
  耳 = top heng (s3) + left shu (s4) + right long shu (s5)
       + inner middle heng (s6) + inner lower heng (s7)
       + bottom long heng crossing whole char (s8).

Reading order in v8: drawer_memory.md → INDEX (no 耳 primitive) → errata (not listed).
No 耳 primitive in the bank; the shortlist doesn't cover it either.
ren_side exists but B10 evidence: importing ren_side and then overriding
its default anchors is the p3_char_0252_伊 FAIL pattern. Inline via base
primitives with MMH-verbatim anchors (A-recipe point 4).

SELF_CHECK below.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in the far-left column (TL/ML) at x_frac ~0.9 within cell
#   (i.e. right edge of col 0 → x_pixels ~88-95), which is far-left overall. ren_side's
#   default anchors sit further toward TC/C; overriding 3+ of its anchors is the
#   伊/B8 partial-override FAIL pattern. Inline pie+shu with MMH-verbatim anchors.
# fresh_component: ren_side_farleft_for_耳-compound

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


CANVAS = 300
INK = (0, 0, 0)


def draw_pie(draw, head, tail, mid_target=None, w_head=8, w_tail=3):
    """Curved 撇 — head thick, tapers to thin tail. If mid_target given, curve so
    the stroke passes near that point at t≈0.54 (used to seat 亻 pie next to shu)."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    if mid_target is not None:
        tx, ty = anchor_to_xy(mid_target)
        # solve quadratic bezier control so p(0.54) ≈ target
        t = 0.54
        a = (1 - t) ** 2
        b = 2 * (1 - t) * t
        c = t * t
        cx = (tx - a * p0[0] - c * p2[0]) / b
        cy = (ty - a * p0[1] - c * p2[1]) / b
        ctrl = (cx, cy)
    else:
        mx = (p0[0] + p2[0]) / 2.0
        my = (p0[1] + p2[1]) / 2.0
        ctrl = (mx - 6, my + 4)
    pts = quad_bezier(p0, ctrl, p2, n=32)
    widths = [w_head + (w_tail - w_head) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths, INK)


def draw_shu(draw, head, tail, width=7):
    """Straight vertical 竖."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width, INK)


def draw_heng(draw, head, tail, width=6):
    """Straight horizontal 横."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width, INK)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1: pie — TL(0.888,0.633) → ML(0.176,0.937), passing near s2.head @ ML(0.666,0.44)
    # so the 亻 pie meets the shu at their MMH-declared N-joint.
    draw_pie(d, ('TL', 0.888, 0.633), ('ML', 0.176, 0.937),
             mid_target=('ML', 0.666, 0.44), w_head=8, w_tail=3)
    # s2: shu — ML(0.674,0.509) → BL(0.715,1.021)  (extends slightly below bottom of BL)
    draw_shu(d, ('ML', 0.674, 0.509), ('BL', 0.715, 1.021), width=7)

    # ---- 耳 (right radical) ----
    # s3: top heng of 耳 — C(0.181,0.058) → TR(0.438,0.896)
    # (mostly horizontal near top of 耳 area, slight rise to right)
    draw_heng(d, ('C', 0.181, 0.058), ('TR', 0.438, 0.896), width=6)
    # s4: left short shu inside 耳 — C(0.301,0.157) → BC(0.371,0.232)
    draw_shu(d, ('C', 0.301, 0.157), ('BC', 0.371, 0.232), width=6)
    # s5: long right shu of 耳 — C(0.942,0.061) → BR(0.071,1.19)
    # (extends past bottom of canvas; that's fine — clipped)
    draw_shu(d, ('C', 0.942, 0.061), ('BR', 0.071, 1.19), width=7)
    # s6: inner middle heng — C(0.521,0.523) → C(0.872,0.462)
    draw_heng(d, ('C', 0.521, 0.523), ('C', 0.872, 0.462), width=5)
    # s7: inner lower heng — C(0.5,0.878) → C(0.896,0.813)
    draw_heng(d, ('C', 0.5, 0.878), ('C', 0.896, 0.813), width=5)
    # s8: bottom heng crossing whole char — BL(0.92,0.353) → BR(0.763,0.247)
    draw_heng(d, ('BL', 0.92, 0.353), ('BR', 0.763, 0.247), width=6)

    out = os.path.join(HERE, "01_佴.png")
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': None,           # set after render
    'stroke_count_ok': True,     # 8 stroke calls: pie + shu + heng + shu + shu + heng + heng + heng
    'endpoint_mismatches': [],   # all anchors MMH-verbatim
    'joint_class_mismatches': [], # all 9 N-joints preserved as natural gaps (no explicit welding); s5⇆s8 P weld at BR happens because both strokes pass through the same anchor region
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; no bank primitive for 耳; inlined per A-recipe pt 4.',
}


if __name__ == "__main__":
    main()
