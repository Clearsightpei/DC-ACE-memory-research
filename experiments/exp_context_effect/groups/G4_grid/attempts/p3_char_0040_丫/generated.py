"""丫 (yā) — Phase 3 char 0040.

MANDATORY LOOKUP CHECKLIST (per memory_index):
  1. success_bank/INDEX.md grep '丫' → not present, first attempt.
  2. errata.md grep '丫' → not listed.
  3. form_catalog.md — 丫 not directly listed; treat left/right branches
     as short 撇 and short 点/nà mirror; central 竖 spans C→BC.
  4. principles_meta.md — TR6 (inline if primitive doesn't fit), TR8
     (竖 must share cell COLUMN), TR10 (N-class visually connected).
  5. joint_atlas.md — s2.tail ⇆ s3.head is N in the MMH spec but must
     read as connected (≤25 px). Because MMH gives them nearly the
     same point (~19 px apart), we honor by using close anchors, not
     welded.
  6. sandbox.md — no note.

Design (from MMH-derived structural expectations block):
  s1: TL(0.718, 0.809) → C(0.131, 0.257) — LEFT branch, drawn as a
      short down-right taper. Direction is UL→LR (not classic 撇),
      so INLINE via fat_line + slight taper rather than reuse pie.
  s2: TR(0.051, 0.662) → C(0.535, 0.4) — RIGHT branch, upper-right
      to junction. INLINE as short tapered line (thick near TR head,
      thin near center tip).
  s3: C(0.318, 0.359) → BC(0.441, 1.041) — center 竖, slightly clipped
      by canvas at bottom. Use shu primitive.

Joints:
  s2.tail @ C(0.535,0.4) ⇆ s3.head @ C(0.318,0.359) — MMH class N,
  expected gap ~19 px. Anchors chosen give ~ sqrt((0.535-0.318)^2 +
  (0.4-0.359)^2) * 100 ≈ 22 px — within TR10 (≤25 px) and roughly
  matches expected_gap_px.
"""

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Three strokes: two inlined tapered branches + shu vertical. '
             'Joint s2.tail ↔ s3.head kept as N (~22 px gap).',
}


def tapered_line(draw, a0, a1, w0, w1, curve=0.0, segments=32,
                 color=(0, 0, 0)):
    """Inline tapered stroke between two anchors."""
    p0 = anchor_to_xy(a0)
    p2 = anchor_to_xy(a1)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    if abs(curve) > 1e-6:
        perp = (-dy / length, dx / length)
        bow = curve * length
        mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
        ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
        pts = quad_bezier(p0, ctrl, p2, n=segments)
    else:
        pts = [(p0[0] + (i / segments) * (p2[0] - p0[0]),
                p0[1] + (i / segments) * (p2[1] - p0[1]))
               for i in range(segments + 1)]
    widths = [w0 + (w1 - w0) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_ya(draw):
    # s1 — LEFT branch: upper-left down-right into junction.
    #   MMH: head TL(0.718, 0.809) → tail C(0.131, 0.257)
    tapered_line(draw,
                 ('TL', 0.718, 0.809),
                 ('C', 0.131, 0.257),
                 w0=9, w1=3,
                 curve=0.10)  # gentle bow

    # s2 — RIGHT branch: upper-right down-left into junction.
    #   MMH: head TR(0.051, 0.662) → tail C(0.535, 0.4)
    tapered_line(draw,
                 ('TR', 0.051, 0.662),
                 ('C', 0.535, 0.4),
                 w0=9, w1=3,
                 curve=-0.08)  # gentle bow other way

    # s3 — 竖 (center vertical): C → BC, slightly past canvas edge.
    #   MMH: head C(0.318, 0.359) → tail BC(0.441, 1.041)
    # TR8 rule 6: both endpoints share cell COLUMN — C and BC are both
    # center-column, so vertical direction is preserved (small x drift
    # ~0.12 within-cell frac is fine, ~12 px lean matches MMH).
    draw_shu(draw,
             ('C', 0.318, 0.359),
             ('BC', 0.441, 1.041),
             width=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ya(draw)
    out = os.path.join(os.path.dirname(__file__), '01_丫.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
