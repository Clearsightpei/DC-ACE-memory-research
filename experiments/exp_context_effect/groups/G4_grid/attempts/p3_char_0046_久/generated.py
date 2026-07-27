"""p3_char_0046_久 (jiǔ, "long time", 3 strokes) — G4 attempt.

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
- success_bank/INDEX.md grep for '久' → not in bank (first attempt).
- errata.md grep for '久' → not present.
- form_catalog.md: 撇 and 捺 in character-context; standard slash pair.
- principles_meta.md: TR1 (OVERRIDE anchors when reusing bank primitives).
- joint_atlas.md: N-class means small visible gap ~15-20 px, do NOT weld.

Stroke plan (matches MMH-injected brief):
  s1 — short 撇 (top): head TC(0.24,0.69) → tail ML(0.48,0.95).
  s2 — long curved 撇 (spine): head C(0.19,0.35) → tail BL(0.37,0.93).
  s3 — 捺 (right slash): head BC(0.58,0.06) → tail BR(0.77,0.95).

Joints:
  s1.mid ⇆ s2.head @ C : N (small gap ~17 px — s2 head starts just
    inside/under s1's midpoint; leave a natural gap, do NOT weld).
  s2.mid ⇆ s3.head @ C : N (small gap ~17 px — s3's head starts near
    the crotch on s2's belly; leave a natural gap).

SELF_CHECK dict populated at end of first render pass.
"""
import os
import sys
from PIL import Image, ImageDraw

# Import bank primitives (path already set up under success_bank/code).
_BANK = os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, os.path.abspath(_BANK))

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first render, 3 strokes: short pie + long spine pie + na. '
             'N joints preserved (no weld at s1-s2 or s2-s3).',
}


def render(out_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # s1 — short 撇 at top. Small, tapered. Head thick, tail needle.
    # Slight leftward bow (curve small to keep it near-straight).
    draw_pie(
        draw,
        from_anchor=('TC', 0.236, 0.691),
        to_anchor=('ML', 0.478, 0.948),
        head_width=8, tail_width=1, curve=0.06, segments=48,
    )

    # s2 — long spine 撇, from C region down to BL. Thicker head, moderate
    # bow to the left (concave-right, typical 撇 shape).
    draw_pie(
        draw,
        from_anchor=('C', 0.187, 0.354),
        to_anchor=('BL', 0.369, 0.933),
        head_width=13, tail_width=1, curve=0.12, segments=48,
    )

    # s3 — 捺, starting near the crotch (top of BC cell, just below s2 mid)
    # sweeping down-right to BR. Peak swell near end for typical 捺 foot.
    draw_na(
        draw,
        from_anchor=('BC', 0.579, 0.057),
        to_anchor=('BR', 0.769, 0.95),
        head_width=3, peak_width=14, tail_width=1,
        peak_t=0.80, curve=0.10, segments=48,
    )

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_久.png')
    render(out)
    print('wrote', out)
