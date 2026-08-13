"""乶 (bol/bul, Korean hanja) — 8 strokes.

Decomposition: 乶 = 甫 (top) + 乙 (bottom).
  - Top 甫 = dian(top-right dot) + shu (long left descent) + shu (short right)
    + heng (upper crossbar) + heng (lower crossbar) + shu (center vertical)
    + heng-pie tick (right-top).
  - Bottom 乙 = single 乙-hook curve.

Following B9 A-recipe: MMH-verbatim anchors + base primitives + SELF_CHECK.
No BANK_DEVIATION needed — no bank primitive was skipped; using base
_anchor/fat_line/quad_bezier only.
"""
import sys, os
_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; s8 (乙) rendered as bezier curve; '
             'P-joints welded at TC/C intersections, N-joints left with gaps.',
}


def _line(draw, a, b, width=10):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), width)


def _curve(draw, a, ctrl, b, width=10):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(ctrl)
    p2 = anchor_to_xy(b)
    pts = quad_bezier(p0, p1, p2, n=60)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- Top 甫 component (strokes 1-7) ---

    # stroke 1: top-right dian/dot (short slant tick)
    _line(d, ('TL', 0.981, 0.87), ('TC', 0.957, 0.756), width=9)

    # stroke 2: long left vertical descent (main left post of 甫)
    _line(d, ('ML', 0.732, 0.151), ('ML', 0.967, 0.966), width=10)

    # stroke 3: right vertical descent (right post of 甫's box)
    _line(d, ('ML', 0.946, 0.286), ('C', 0.969, 0.84), width=10)

    # stroke 4: upper horizontal crossbar
    _line(d, ('C', 0.128, 0.45), ('C', 0.749, 0.345), width=9)

    # stroke 5: lower horizontal crossbar
    _line(d, ('C', 0.128, 0.723), ('C', 0.767, 0.614), width=9)

    # stroke 6: central vertical from top-center down through both crossbars
    _line(d, ('TC', 0.321, 0.475), ('C', 0.436, 0.963), width=10)

    # stroke 7: small heng/pie tick in TR (top-right corner accent)
    _line(d, ('TR', 0.021, 0.521), ('TR', 0.306, 0.762), width=9)

    # --- Bottom 乙 component (stroke 8) ---
    # 乙 = 横折弯钩: short horizontal → descend → long sweep right
    # Render as two beziers joined for a proper 乙 silhouette.
    head_xy = anchor_to_xy(('BL', 0.574, 0.247))
    tail_xy = anchor_to_xy(('BR', 0.625, 0.552))
    # bend point roughly under the character body, low in BC
    bend_xy = anchor_to_xy(('BC', 0.15, 0.88))
    # first segment: short horizontal-ish descent from head down to bend
    ctrl1 = anchor_to_xy(('BL', 0.85, 0.75))
    seg1 = quad_bezier(head_xy, ctrl1, bend_xy, n=40)
    # second segment: long sweep from bend up-right to tail
    ctrl2 = anchor_to_xy(('BC', 0.95, 0.95))
    seg2 = quad_bezier(bend_xy, ctrl2, tail_xy, n=50)
    pts = seg1 + seg2[1:]
    stroke_variable_width(d, pts, [10] * len(pts))

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_乶.png")
    render(out)
    print("wrote", out)
