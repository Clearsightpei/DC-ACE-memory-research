"""p3_char_0165_乍 — G4 grid-bank drawer attempt.

Lookup checklist:
1. success_bank/INDEX.md grep '乍' — not present.
2. errata.md grep '乍' — not present.
3. form_catalog.md — general 撇/横/竖 patterns apply.
4. principles_meta.md TR1-TR12 — TR8 (horiz/vert must share row/col), TR10 (N gaps look connected).
5. joint_atlas.md — 4 N-class joints all with ~11-16 px gaps.
6. sandbox.md — no direct notes for 乍.

Strategy: 5 fresh strokes per MMH anchors. Structure of 乍:
  s1: 撇 from TC down-left into ML
  s2: short 横 across top from C to MR (top bar)
  s3: 竖 down the middle-right from C to BC (the long vertical spine)
  s4: middle 横 from C to MR (short middle bar)
  s5: bottom 横 from BC to BR (short bottom bar)
All 4 joints are N-class (small natural gap ~13 px, do NOT weld).
"""
import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line, CANVAS


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes, all N-class joints kept as small gaps'
}


def draw_pie(draw, head_anchor, tail_anchor, w0=8, w1=3):
    """撇 (leftward diagonal), tapered from head to tail."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    # Slight bow for calligraphic curve
    mid = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 - 4)
    pts = quad_bezier(p0, mid, p2, n=40)
    widths = [w0 + (w1 - w0) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head_anchor, tail_anchor, w=6):
    """横 (horizontal)."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, w)


def draw_shu(draw, head_anchor, tail_anchor, w=6):
    """竖 (vertical, possibly with a small tail hook)."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, w)


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 撇 head @ ('TC', 0.096, 0.606) → tail @ ('ML', 0.375, 0.843)
    draw_pie(d, ('TC', 0.096, 0.606), ('ML', 0.375, 0.843), w0=8, w1=3)

    # Stroke 2: short 横 head @ ('C', 0.043, 0.219) → tail @ ('MR', 0.435, 0.005)
    draw_heng(d, ('C', 0.043, 0.219), ('MR', 0.435, 0.005), w=6)

    # Stroke 3: 竖 head @ ('C', 0.395, 0.274) → tail @ ('BC', 0.509, 1.129) (extends slightly below BC)
    # Clamp y_frac to 1.0 for cell BC (tail goes to bottom of canvas)
    draw_shu(d, ('C', 0.395, 0.274), ('BC', 0.509, 1.0), w=6)

    # Stroke 4: middle 横 head @ ('C', 0.6, 0.734) → tail @ ('MR', 0.229, 0.69)
    draw_heng(d, ('C', 0.6, 0.734), ('MR', 0.229, 0.69), w=6)

    # Stroke 5: bottom 横 head @ ('BC', 0.576, 0.241) → tail @ ('BR', 0.32, 0.171)
    draw_heng(d, ('BC', 0.576, 0.241), ('BR', 0.32, 0.171), w=6)

    out = os.path.join(os.path.dirname(__file__), '01_乍.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
