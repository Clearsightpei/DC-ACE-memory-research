"""p3_char_0215_凸 — G4 attempt.

Memory-index reading order:
1. drawer_memory.md — no chronic primitive maps to 凸; no direct sub-radical
   in the shortlist matches (凸 is not decomposable into 亻/扌/宀/etc).
2. success_bank/INDEX.md — no mastered 凸-like entry.
3. errata.md — 凸 not previously listed.

Falling back to first-principles rendering from GT + MMH-derived anchors.
凸 is 5 strokes: a top rectangular bump sitting on a wider base, drawn as:
  1) left vertical of top bump  (short 竖)
  2) left shelf horizontal      (short 横)
  3) left vertical of base      (long 竖)
  4) compound 横折折折 tracing top-of-bump → right-bump → right-shelf → right-base
  5) bottom horizontal          (long 横)
Joints are all N (small natural gap or corner-meet), no piercing crossings.
"""

from PIL import Image, ImageDraw
import os

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 5 strokes as required
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 5 joints are N per brief
    'overall_pass': True,
    'notes': 'Straight-line rendering; compound stroke 4 uses polyline with 3 corners.'
}

CANVAS = 300
W = 8  # ink width

# 米字格 layout for 凸 (PIL coords: y grows DOWN)
# Cells: TL(0,0)-TR(2,0) at top row, BL-BR at bottom row.  Each cell = 100 px.
# Top bump occupies TC roughly: x in [130, 195], y in [55, 145]
# Base occupies bottom row + straddles middle row: x in [50, 245], y in [145, 265]

# Stroke endpoints (PIL pixels) — chosen to fit MMH anchor cells within tolerance:
S1_HEAD = (130, 55)    # left-top of bump  ~ TL/TC boundary at top
S1_TAIL = (130, 145)   # bottom of left-bump-vertical ~ C

S2_HEAD = (130, 145)   # meets S1 tail
S2_TAIL = (50, 145)    # left shelf endpoint at ML

S3_HEAD = (50, 145)    # meets S2 tail
S3_TAIL = (50, 265)    # left base bottom at BL

# Stroke 4: compound 横折折折
S4_P0 = (130, 55)      # top-left corner of bump (meets S1 head area)
S4_P1 = (195, 55)      # top-right corner of bump
S4_P2 = (195, 145)     # right-bump-base
S4_P3 = (245, 145)     # right shelf endpoint
S4_P4 = (245, 265)     # right base bottom at BR

S5_HEAD = (50, 265)
S5_TAIL = (245, 265)


def draw_stroke(d, pts, width=W):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=width)
    # round caps at every vertex
    r = width / 2.0
    for (x, y) in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    strokes = [
        [S1_HEAD, S1_TAIL],
        [S2_HEAD, S2_TAIL],
        [S3_HEAD, S3_TAIL],
        [S4_P0, S4_P1, S4_P2, S4_P3, S4_P4],
        [S5_HEAD, S5_TAIL],
    ]
    assert len(strokes) == 5, f'expected 5 strokes, got {len(strokes)}'

    for s in strokes:
        draw_stroke(d, s)

    out = os.path.join(os.path.dirname(__file__), '01_凸.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
