"""p3_char_0554_监 — G4 rendering.

Split: 监 = top (臣-like left + top-right mark) + 皿 bottom.
10 strokes total (matches MMH). Following MMH-derived anchors verbatim.

- s1: left long vertical of 臣 (ML top -> ML bottom)
- s2: outer left descending stroke (TC -> BC)
- s3: top horizontal of upper-right box (TC -> C)
- s4: small right upper mark / short 横 (C -> MR)
- s5: right descending / 卜 dot area (C -> MR)
- s6: 皿 left side (BL -> BC diagonal)
- s7: 皿 right side (BL -> BC)
- s8: 皿 inner vertical #1 (BC vertical)
- s9: 皿 inner vertical #2 (BC vertical)
- s10: 皿 base horizontal (BL -> BR)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Rendered per MMH anchors verbatim. 10 strokes, all N-joints kept as neighbors (no welding).',
}

STROKES = [
    (('ML', 0.686, 0.075), ('ML', 0.812, 0.843)),  # 1
    (('TC', 0.081, 0.768), ('BC', 0.207, 0.048)),  # 2
    (('TC', 0.761, 0.703), ('C',  0.433, 0.658)),  # 3
    (('C',  0.805, 0.251), ('MR', 0.481, 0.119)),  # 4
    (('C',  0.840, 0.515), ('MR', 0.188, 0.857)),  # 5
    (('BL', 0.782, 0.209), ('BC', 0.022, 0.769)),  # 6
    (('BL', 0.917, 0.206), ('BC', 0.975, 0.687)),  # 7
    (('BC', 0.277, 0.276), ('BC', 0.327, 0.754)),  # 8
    (('BC', 0.632, 0.191), ('BC', 0.603, 0.725)),  # 9
    (('BL', 0.305, 0.856), ('BR', 0.687, 0.821)),  # 10
]

assert len(STROKES) == 10, f"Expected 10 strokes, got {len(STROKES)}"


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    for h, t in STROKES:
        p0 = anchor_to_xy(h)
        p1 = anchor_to_xy(t)
        fat_line(draw, p0, p1, 5)
    out = os.path.join(os.path.dirname(__file__), '01_监.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
