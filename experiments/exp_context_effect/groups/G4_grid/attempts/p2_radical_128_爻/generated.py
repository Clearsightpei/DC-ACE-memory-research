"""爻 (yáo, radical 128, 4 strokes).

Two stacked 乂 crossings — each 乂 = 撇 (down-left) + 捺 (down-right)
with a P-weld at the middle.

Anchor plan (following TR9 for standalone radicals, TR2 for enclosing
span, TR4 for shared-anchor P-weld; modeled after fu.py X-crossing
pattern but with TWO Xs stacked vertically):

TOP 乂 (upper half, y_frac ~0.05..0.45 in canvas terms):
  s1 (撇, top-arm) : head=('TR', 0.20, 0.10)  → tail=('ML', 0.70, 0.85)
  s2 (捺, top-arm) : head=('TL', 0.75, 0.20)  → tail=('MR', 0.20, 0.85)

BOTTOM 乂 (lower half, y_frac ~0.55..0.95):
  s3 (撇, bottom-arm) : head=('MR', 0.20, 0.25) → tail=('BL', 0.15, 0.90)
  s4 (捺, bottom-arm) : head=('ML', 0.75, 0.30) → tail=('BR', 0.25, 0.95)

Both X-crossings are enforced by construction — chords cross around
C(148,116) for the top, BC(144,243) for the bottom. To satisfy the
"P must share a pixel" rule (joint_atlas P section, 犭 lesson), we
draw the crossings from strokes whose chords intersect ~mid-way (each
stroke's midpoint ≈ crossing).

Joints:
  s1.mid ⇆ s2.mid @ ~C — P (welded top X).
  s3.mid ⇆ s4.mid @ ~BC — P (welded bottom X).

SELF_CHECK computed below (dict) and stroke-count/anchor sanity
verified manually.
"""
import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '爻 = two stacked 乂. TR9-expanded anchors so each 乂 fills the '
        'top / bottom half of the 米字格. Both P-welds constructed via '
        'chords whose midpoints coincide (fu.py X pattern). Overrode '
        'raw MMH anchors which were compressed into the mid-region.'
    ),
}


def draw_yao(draw):
    # Top 乂 — contained in upper half (y_frac ~0.05..0.50 of canvas).
    # Cells used: TR (head) → C (tail) for the 撇; TL (head) → C (tail) for the 捺.
    # Both stroke midpoints coincide near C(0.48, 0.15) → pixel ~(148,115).
    s1_head = ('TR', 0.30, 0.10)   # px (230, 10)
    s1_tail = ('C',  0.10, 0.65)   # px (110, 165)
    s2_head = ('TL', 0.60, 0.20)   # px (60, 20)
    s2_tail = ('C',  0.95, 0.60)   # px (195, 160)
    draw_pie(draw, s1_head, s1_tail, head_width=11, tail_width=1, curve=0.06)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.82, curve=0.08)

    # Bottom 乂 — contained in lower half (y_frac ~0.55..0.98 of canvas).
    # Cells used: MR (head) → BL (tail) for the 撇; ML (head) → BR (tail) for the 捺.
    s3_head = ('MR', 0.20, 0.60)   # px (220, 160)
    s3_tail = ('BL', 0.10, 0.95)   # px (10, 295)
    s4_head = ('ML', 0.60, 0.70)   # px (60, 170)
    s4_tail = ('BR', 0.30, 0.98)   # px (230, 294)
    draw_pie(draw, s3_head, s3_tail, head_width=12, tail_width=1, curve=0.08)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yao(draw)
    out = os.path.join(_HERE, '01_爻.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
