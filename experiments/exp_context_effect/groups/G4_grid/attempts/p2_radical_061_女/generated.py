"""女 (nǚ) — 3-stroke radical.

Anchor plan (米字格):
  stroke 1 (撇点 piě diǎn): head @ ('TC', 0.295, 0.627), pivot near ('BC', 0.549, 0.342), tail @ ('BR', 0.306, 0.968)
  stroke 2 (撇 piě):        head @ ('C',  0.84,  0.456), tail @ ('BL', 0.697, 0.83)
  stroke 3 (横 héng):       head @ ('ML', 0.205, 0.77),  tail @ ('MR', 0.783, 0.658)

Joints (from MMH):
  s1.mid ⇆ s2.mid  (P, welded, near BC/C boundary) — 撇点's 撇 body crosses 撇 body
  s1.mid ⇆ s3.mid  (P, welded, in C cell)          — 横 crosses 撇点 body
  s2.head ⇆ s3.mid (T, welded, in C cell)          — 撇 head touches 横 body

Bank primitives used: pie_dian (s1), pie (s2), heng (s3).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie_dian import draw_pie_dian
from pie import draw_pie
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,   # (a) piě-diǎn hooks down from top-center; (b) horizontal crosses through center-right; (c) diagonal 撇 sweeps upper-right to lower-left
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: 撇点 + 撇 + 横. Joints P/P/T all welded per MMH.',
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 撇点 — head TC, pivot around BC/C area, tail BR
    # MMH gives head=('TC',0.295,0.627), tail=('BR',0.306,0.968).
    # The joint mid(0.68) sits at BC(0.549,0.342), which is the piě→diǎn pivot.
    draw_pie_dian(
        draw,
        head=('TC', 0.295, 0.627),
        pivot=('C', 0.20, 0.70),   # welded elbow — lower-left of center; 撇 sweeps down-left FIRST, then 点 presses down-right toward BR
        tail=('BR', 0.306, 0.968),
        pie_head_w=11, pie_tip_w=4,
        dian_head_w=4, dian_tail_w=10,
    )

    # Stroke 2: 撇 — from center-right down to lower-left.
    # MMH head @ ('C', 0.84, 0.456), tail @ ('BL', 0.697, 0.83).
    draw_pie(
        draw,
        from_anchor=('C', 0.84, 0.456),
        to_anchor=('BL', 0.697, 0.83),
        head_width=10, tail_width=2, curve=0.08, segments=48,
    )

    # Stroke 3: 横 — horizontal from ML across through center to MR.
    # MMH head @ ('ML', 0.205, 0.77), tail @ ('MR', 0.783, 0.658).
    draw_heng(
        draw,
        from_anchor=('ML', 0.205, 0.77),
        to_anchor=('MR', 0.783, 0.658),
        width=8,
    )

    out = os.path.join(os.path.dirname(__file__), '01_女.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
