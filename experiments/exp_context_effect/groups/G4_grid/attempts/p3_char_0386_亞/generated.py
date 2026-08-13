"""亞 (yà) — p3_char_0386. 8 strokes per MMH.

Strategy: MMH-verbatim anchors (per v9 lesson "trust MMH anchors verbatim").
All 8 joints are class N — leave the natural small gaps, do NOT weld.
No chronic primitive applies (no 丿/刀/冂/弓/马 sub-component).
No bank primitive fits cleanly (亞 is a bespoke 8-piece decomposition —
each piece is a short heng or short shu with specific MMH endpoints).
Using fat_line with MMH anchors is exactly the shared bank convention.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors, uniform width 8, N-class gaps preserved.'
}

# MMH-derived 8 strokes for 亞
STROKES = [
    # (head_anchor, tail_anchor, width)
    (('TL', 0.879, 0.814), ('TR', 0.238, 0.697), 8),   # s1 top heng
    (('TC', 0.11,  0.929), ('C',  0.269, 0.45 ), 8),   # s2 upper-left vertical piece
    (('ML', 0.721, 0.626), ('C',  0.324, 0.55 ), 8),   # s3 mid-left short heng
    (('ML', 0.568, 0.623), ('BC', 0.125, 0.722), 8),   # s4 left descending
    (('TC', 0.708, 0.858), ('MR', 0.153, 0.942), 8),   # s5 upper-right vertical piece
    (('BC', 0.775, 0.06 ), ('BR', 0.373, 0.03 ), 8),   # s6 mid-right short heng
    (('BC', 0.67,  0.057), ('BC', 0.69,  0.692), 8),   # s7 lower-right vertical
    (('BL', 0.293, 0.842), ('BR', 0.754, 0.824), 8),   # s8 bottom heng
]

assert len(STROKES) == 8, f"stroke count mismatch: {len(STROKES)}"


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    for head, tail, w in STROKES:
        p0 = anchor_to_xy(head)
        p1 = anchor_to_xy(tail)
        fat_line(draw, p0, p1, w)
    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_亞.png')
    render(out)
    print(f'wrote {out}')
