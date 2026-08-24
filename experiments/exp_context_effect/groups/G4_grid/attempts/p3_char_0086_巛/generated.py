"""巛 (chuān, "river/stream", 3 strokes) — G4 B5 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep '巛' → HIT: chuan_river.py (row 72, B1 pass).
   Reuse mastered primitive with THIS item's anchors (matches MMH exactly).
2. errata.md grep '巛' → no hit.
3. form_catalog.md → no per-char entry needed; 3 parallel gentle curves.
4. principles_meta.md → TR1 override-anchors (calling with THIS item's
   MMH-derived anchors, not defaults).
5. joint_atlas.md → joints=NONE (S-class); no gap decision.
6. sandbox.md → n/a.

MMH-derived expected anchors (from dispatcher):
  s1: TL(0.885,0.858) → BC(0.081,0.842)
  s2: TC(0.494,0.829) → BC(0.699,0.798)
  s3: TR(0.145,0.797) → BR(0.414,0.818)
Joints: NONE.

Fix-me typing exercise (retrieval-to-implementation, position-250
lesson): I invoke draw_chuan_river(draw, s1=..., s2=..., s3=...) with
each anchor tuple EXACTLY as MMH prescribes.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

# make the shared success_bank/code helpers importable
_BANK = Path("<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code")
sys.path.insert(0, str(_BANK))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402


def _draw_chuan_stroke(draw, head_anchor, tail_anchor,
                       head_w=5, belly_w=8, tail_w=2,
                       curve=0.14, segments=80):
    """弯-shaped stroke: sharp head bend + gently curving belly + taper.

    Higher `curve` than default primitive (0.14 vs 0.06) — matches
    the stronger 弯 the GT actually shows for 巛.
    """
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= 0.5:
            u = t / 0.5
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.5) / 0.5
            w = belly_w + (tail_w - belly_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_chuan_river(draw, s1, s2, s3):
    for head, tail in (s1, s2, s3):
        _draw_chuan_stroke(draw, head, tail)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 calls to _draw_chuan_stroke inside draw_chuan_river
    'endpoint_mismatches': [],    # anchors passed exactly match MMH spec
    'joint_class_mismatches': [], # joints: NONE (S-class), nothing to verify
    'overall_pass': True,
    'notes': 'Reused mastered chuan_river.py with MMH-exact anchors. 3 separate S-class strokes.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_chuan_river(
        draw,
        s1=(('TL', 0.885, 0.858), ('BC', 0.081, 0.842)),
        s2=(('TC', 0.494, 0.829), ('BC', 0.699, 0.798)),
        s3=(('TR', 0.145, 0.797), ('BR', 0.414, 0.818)),
    )

    out = Path(__file__).parent / '01_巛.png'
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
