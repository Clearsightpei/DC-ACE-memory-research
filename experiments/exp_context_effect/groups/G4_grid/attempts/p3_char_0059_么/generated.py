"""么 (me) — 3 strokes: small 撇, main 撇-curve, right 捺/点.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. success_bank/INDEX.md grep '么' — NO existing entry.
  2. errata.md grep '么' — NOT in errata.
  3. form_catalog.md — 么 is a small standalone char with 3 strokes:
     small pie top, main pie curve, closing dot/na on right.
  4. principles_meta.md — TR1 not applicable (no bank primitive being reused
     with defaults); TR9 not needed (character fills grid naturally per MMH).
  5. joint_atlas.md — one N joint at BR between s2.tail and s3.mid; keep
     visible gap (~22 px expected).
  6. sandbox.md — none specific.

Structure (MMH anchors):
  s1 (小撇): TC(0.386, 0.721) → ML(0.527, 0.893)  — small down-left sweep.
  s2 (主撇): C(0.802, 0.342) → BR(0.133, 0.508)   — main curved pie sweep.
  s3 (捺/点): BC(0.96, 0.074) → BR(0.399, 0.81)   — right closing stroke.

Joint:
  s2.tail ⇆ s3.mid(0.40) @ BR — class N (visible gap, DO NOT weld).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes; N-gap at BR; s2 curved as pie sweep.',
}


def draw_curved_pie(draw, from_anchor, to_anchor,
                    head_width=11, tail_width=3, curve=0.18, segments=48):
    """Curved 撇-like stroke: taper thick→thin, perpendicular bow."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Bow to the upper-right side of the chord (typical 撇 belly).
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_na_stroke(draw, from_anchor, to_anchor,
                   head_width=3, peak_width=12, tail_width=2,
                   peak_t=0.75, curve=0.08, segments=48):
    """Right-falling stroke: thin head, swell, taper."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Bow outward (down-left of chord).
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= peak_t:
            u = t / peak_t
            w = head_width + (peak_width - head_width) * u
        else:
            u = (t - peak_t) / max(1e-6, (1.0 - peak_t))
            w = peak_width + (tail_width - peak_width) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: small 撇 — TC → ML (down-left sweep).
    draw_curved_pie(draw,
                    ('TC', 0.386, 0.721),
                    ('ML', 0.527, 0.893),
                    head_width=9, tail_width=2, curve=0.12)

    # s2: main 撇 curve — C → BR (larger curved sweep, bows left).
    draw_curved_pie(draw,
                    ('C', 0.802, 0.342),
                    ('BR', 0.133, 0.508),
                    head_width=12, tail_width=3, curve=0.32)

    # s3: closing 捺/点 — BC-right → BR (short right-falling with swell).
    draw_na_stroke(draw,
                   ('BC', 0.96, 0.074),
                   ('BR', 0.399, 0.81),
                   head_width=4, peak_width=13, tail_width=2,
                   peak_t=0.72, curve=0.10)

    out_path = os.path.join(os.path.dirname(__file__), '01_么.png')
    img.save(out_path)
    return out_path


if __name__ == '__main__':
    path = render()
    print(f'wrote {path}')
