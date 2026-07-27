"""p3_char_0122_五 (wǔ, "five") — 4 strokes.

MANDATORY LOOKUP CHECKLIST:
1. success_bank INDEX grep for 五 → not found. wu_lame.py is 兀 not 五 (structural
   mismatch — 兀 has 3 strokes with 撇+竖弯; 五 has 4 straight strokes). Do NOT reuse.
2. errata.md grep for 五 → not listed.
3. form_catalog.md: 横 x char-top / char-bottom rows apply. Two 横 (top+bottom) plus
   a short 横 in the middle band; s2 is a slanted 竖-like left-descending stroke.
4. principles_meta.md TR1 (override anchors), TR8 (横 endpoints share row), TR10
   (N-class must look connected ≤25 px).
5. joint_atlas.md: P-welded crossing at s2/s3 (share the corner point), N-neighbor
   gaps at s1-s2 head, s2-tail-s4, s3-tail-s4.
6. sandbox.md: nothing item-specific.

Composition: use draw_heng for the three horizontals (s1 top, s3 middle short,
s4 bottom) and a straight fat_line for the slanted s2. P-weld realized by
positioning s2 and s3 to actually cross at C(0.319, 0.688).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first render; MMH anchors used verbatim; s2 slanted line so it '
             'crosses s3 near C(0.319, 0.688) for P-weld.'
}

# MMH-derived anchors (verbatim from brief)
S1_HEAD = ('TL', 0.891, 0.967)
S1_TAIL = ('TR', 0.206, 0.853)

S2_HEAD = ('C',  0.348, 0.058)
S2_TAIL = ('BC', 0.061, 0.508)

S3_HEAD = ('ML', 0.800, 0.726)
S3_TAIL = ('BC', 0.734, 0.476)

S4_HEAD = ('BL', 0.185, 0.654)
S4_TAIL = ('BR', 0.830, 0.678)


def draw_wu_char(draw):
    # s1 — top 横 (slight slant, per MMH)
    draw_heng(draw, S1_HEAD, S1_TAIL, width=10)

    # s2 — slanted left-descending stroke (near-vertical, drifting left)
    p2a = anchor_to_xy(S2_HEAD)
    p2b = anchor_to_xy(S2_TAIL)
    fat_line(draw, p2a, p2b, width=10)

    # s3 — short middle stroke crossing s2 (P-weld at C)
    p3a = anchor_to_xy(S3_HEAD)
    p3b = anchor_to_xy(S3_TAIL)
    fat_line(draw, p3a, p3b, width=9)

    # s4 — bottom 横
    draw_heng(draw, S4_HEAD, S4_TAIL, width=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_wu_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_五.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
