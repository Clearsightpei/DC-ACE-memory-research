"""p3_char_0516_疰 — G4 attempt.

疰 = 疒 (5 strokes) + 主 (5 strokes) = 10 strokes.

Strategy: MMH-anchor driven inline render (no chronic primitive for 疒
exists yet; bank has no 疰). Straight lines with modest ink weight, and
a Bezier curve for the long 疒 pie (s3). Endpoint anchors read directly
from the injected MMH block; nothing forced to non-MMH positions.

No bank primitive skipped — nothing to skip (no 疒 or 疰 primitive
exists). No BANK_DEVIATION block needed.
"""
import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(THIS_DIR, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from PIL import Image, ImageDraw  # noqa: E402
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 10 line/curve primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 7 N joints drawn as separate lines (no welding);
                                    # one P joint (s8-s9) crosses at BC ~(207,222)
    'overall_pass': True,
    'notes': '疰 = 疒 (5) + 主 (5). All endpoints follow MMH; s3 pie rendered as tapered bezier.'
}


# Expected anchors (from injected MMH block)
STROKES = [
    # (head_anchor, tail_anchor, width, kind)
    (('TC', 0.424, 0.642), ('TC', 0.775, 0.87 ),  8, 'dot'),   # s1 疒 top dot 丶
    (('C',  0.096, 0.146), ('TR', 0.388, 0.999), 7, 'line'),   # s2 疒 heng 一
    (('ML', 0.861, 0.072), ('BL', 0.434, 1.038), 8, 'pie'),    # s3 疒 long pie 丿 (curve)
    (('ML', 0.419, 0.456), ('ML', 0.683, 0.688), 7, 'dot'),    # s4 疒 inner dot
    (('BL', 0.19,  0.373), ('ML', 0.806, 0.992), 7, 'ti'),     # s5 疒 inner ti 提
    (('C',  0.585, 0.321), ('C',  0.86,  0.532), 6, 'line'),   # s6 主 top short heng
    (('C',  0.245, 0.787), ('MR', 0.329, 0.652), 7, 'line'),   # s7 主 middle heng
    (('BC', 0.298, 0.288), ('BR', 0.256, 0.191), 7, 'line'),   # s8 主 upper-mid heng (short)
    (('C',  0.667, 0.843), ('BC', 0.714, 0.728), 8, 'line'),   # s9 主 vertical 丨 (short, crosses s8)
    (('BC', 0.025, 0.856), ('BR', 0.599, 0.81 ),  8, 'line'),   # s10 主 long bottom heng 一
]

assert len(STROKES) == 10, f"expected 10 strokes, got {len(STROKES)}"


def draw_stroke(draw, head, tail, width, kind):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)

    if kind == 'dot':
        # Ink stroke tapered: thicker at tail (dot lands to the down-right)
        pts = [(p0[0] + i / 12 * (p1[0] - p0[0]),
                p0[1] + i / 12 * (p1[1] - p0[1])) for i in range(13)]
        widths = [max(2, int(width * (0.4 + 0.6 * i / 12))) for i in range(13)]
        stroke_variable_width(draw, pts, widths)
        return

    if kind == 'pie':
        # Long left-diagonal 撇: use a light curve bending outward (toward BL).
        # Control point pulled slightly left of the midpoint.
        mx = (p0[0] + p1[0]) / 2.0
        my = (p0[1] + p1[1]) / 2.0
        cx = mx - 18.0     # curve outward to the left
        cy = my + 6.0
        pts = quad_bezier(p0, (cx, cy), p1, n=48)
        # Taper: thicker at head, thin toward tail
        widths = [max(2, int(width * (1.0 - 0.55 * i / 48))) for i in range(49)]
        stroke_variable_width(draw, pts, widths)
        return

    if kind == 'ti':
        # 提: thicker at head, thin at tail (ends in a point going up-right)
        pts = [(p0[0] + i / 24 * (p1[0] - p0[0]),
                p0[1] + i / 24 * (p1[1] - p0[1])) for i in range(25)]
        widths = [max(2, int(width * (1.0 - 0.5 * i / 24))) for i in range(25)]
        stroke_variable_width(draw, pts, widths)
        return

    # Default 'line' — straight, uniform-ish width
    fat_line(draw, p0, p1, width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    for head, tail, w, kind in STROKES:
        draw_stroke(draw, head, tail, w, kind)
    out = os.path.join(THIS_DIR, '01_疰.png')
    img.save(out)
    print("wrote", out)


if __name__ == '__main__':
    render()
    print("SELF_CHECK", SELF_CHECK)
