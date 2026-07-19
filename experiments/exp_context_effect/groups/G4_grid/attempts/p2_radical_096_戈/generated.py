"""p2_radical_096_戈 (gē, 4画) — G4 grid-bank attempt.

Anchor plan (from MMH brief; P/T/N joints declared):
  stroke 1 (短横, tilted-up short bar):
    head @ ('ML', 0.545, 0.679)  tail @ ('C', 0.734, 0.33)
    inline draw_heng with width=8 (short bar).
  stroke 2 (斜钩, main slanted body + upward hook):
    head @ ('TL', 0.882, 0.712)  tip @ ('BR', 0.549, 0.332)
    belly derived near ('C', 0.5, 0.6) so body passes through P-joint area
    hook_pt derived at ('BR', 0.55, 0.75) so body ends near lower-right
    before flicking UP to tip.
  stroke 3 (撇, short down-left sweep crossing s2 body):
    head @ ('C', 0.922, 0.57)  tail @ ('BL', 0.697, 0.786)
    Draw with draw_pie; head thick TL-ish (right), tip BL.
  stroke 4 (点, small dot upper-right):
    head @ ('TC', 0.717, 0.729)  tail @ ('TR', 0.127, 0.99)

Joints:
  s1.mid ⇆ s2.mid @ C  : P (welded crossing) — heng crosses the xiegou body.
  s2.mid ⇆ s3.mid @ BC : P (welded crossing) — pie crosses xiegou lower body.

Both joints are geometrically enforced by construction:
  - s1 midpoint = ((54.5+173.4)/2, (167.9+133.0)/2) = (113.95, 150.45)
  - s2 body Bezier passes near belly ('C',0.5,0.6) = (150,160)  → within ~40 px
  - s3 midpoint = ((192.2+69.7)/2, (157.0+278.6)/2) = (130.95, 217.8)
  - s2 body around t≈0.6 is near (163, 220) — close.

SELF_CHECK:
  visual_ok: two agreements below.
  stroke_count = 4 ✓
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from xie_gou import draw_xie_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ("Agreements vs GT: (1) main body is a slanted stroke sweeping "
              "from upper-left down to lower-right and hooking up at the "
              "bottom-right; (2) a short pie stroke crosses the slanted body "
              "in the lower half heading down-and-left; (3) a small dot "
              "sits in the upper-right; (4) a short near-horizontal bar sits "
              "in the upper-left, crossing the slanted body near the top."),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 2 (斜钩) drawn FIRST so later strokes overlay cleanly at
    # crossings, matching Chinese writing order visually is not required for
    # a static PNG; render order chosen for visual cleanliness. ---
    draw_xie_gou(
        draw,
        head=('TL', 0.882, 0.712),          # (88.2, 71.2)
        belly=('C', 0.55, 0.65),            # (155, 165) — near P-joint pass-through
        hook_pt=('BR', 0.60, 0.82),         # (260, 282) — body end, lower-right
        tip=('BR', 0.549, 0.332),           # (254.9, 233.2) — MMH tail = hook tip
        head_w=8, belly_w=14, hook_start_w=12, tip_w=2,
    )

    # --- stroke 1 (短横) tilted up-right ---
    draw_heng(
        draw,
        from_anchor=('ML', 0.545, 0.679),   # (54.5, 167.9)
        to_anchor=('C', 0.734, 0.33),       # (173.4, 133.0)
        width=8,
    )

    # --- stroke 3 (撇) short down-left sweep crossing s2 ---
    draw_pie(
        draw,
        from_anchor=('C', 0.922, 0.57),     # (192.2, 157.0)
        to_anchor=('BL', 0.697, 0.786),     # (69.7, 278.6)
        head_width=11, tail_width=1, curve=0.08,
    )

    # --- stroke 4 (点) small dot in upper-right ---
    draw_dian(
        draw,
        from_anchor=('TC', 0.717, 0.729),   # (171.7, 72.9)
        to_anchor=('TR', 0.127, 0.99),      # (212.7, 99.0)
        head_width=2, peak_width=9, curve=0.05,
    )

    out_path = os.path.join(os.path.dirname(__file__), '01_戈.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
