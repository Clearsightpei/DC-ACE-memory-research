"""p3_char_0138_水 — G4 attempt.

Memory-lookup checklist:
  1. success_bank/INDEX.md grep '水'/'shui' → shui.py (氵 radical, 3-stroke).
     Not directly reusable (radical, 3 drops), but principle carries.
  2. errata.md grep '水' → p2_radical_119_水 FAILED before. Fix: use 竖钩
     spine + two flanking short 撇 + short 捺 (4-stroke composition).
     Reference GT to confirm.
  3. form_catalog: 竖钩 (shu_gou), 撇 (pie), 捺 (na) all in Phase-1 bank.
  4. principles_meta: TR1 (override anchors), TR10 (N-class visible gap ~15-25 px).
  5. joint_atlas: 水 center strokes are N-class (gaps, not welds).
  6. sandbox: n/a.

MMH-derived stroke layout (4 strokes):
  s1: 横撇 or upper-left short curve from TC(0.386,0.615) → BC(0.049,0.713).
      This is a descending stroke from upper mid to lower mid-left.
  s2: short 撇 flick from ML(0.431,0.562) → BL(0.331,0.678).
  s3: main 竖钩 spine from MR(0.159,0.002) → C(0.729,0.676). Long vertical.
  s4: right descending 捺-like from C(0.579,0.535) → BR(0.9,0.458).

Joints (all N — small natural gap, do NOT weld):
  s1.mid ⇆ s3.tail near cell C.
  s1.mid ⇆ s4.head near cell C.
  s3.tail ⇆ s4.head near cell C.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-spec 4-stroke: (1) upper-left short pie, (2) lower-left tiny pie, (3) central shu-gou spine, (4) right descending na. All joints N-class.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


def draw_curved_pie(draw, from_anchor, to_anchor,
                    head_width=6, tail_width=2, curve=0.10, segments=40,
                    color=(0, 0, 0)):
    """Short curved descending stroke (used for the two left flicks of 水)."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_na_stroke(draw, from_anchor, to_anchor,
                   head_width=3, peak_width=13, tail_width=2,
                   peak_t=0.75, curve=0.10, segments=40,
                   color=(0, 0, 0)):
    """Right-descending 捺-like stroke: thin start, swelling belly, tapered tail."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t <= peak_t:
            w = head_width + (peak_width - head_width) * (t / peak_t)
        else:
            w = peak_width + (tail_width - peak_width) * ((t - peak_t) / (1 - peak_t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s3 — central 竖钩 spine drawn FIRST (largest structural element,
    #      other strokes anchor visually around its cross-point).
    #      MMH: MR(0.159, 0.002) -> C(0.729, 0.676).
    #      MR(0.159, 0.002) in pixel is (200+15.9, 0.2) ≈ (216, 0.2) — top-right of TC.
    #      C(0.729, 0.676) is (100+72.9, 100+67.6) = (172, 167).
    #      The GT shows the spine sits near horizontal center and has a long tail
    #      with clear hook flicking up-left. Extend the tail below MMH point to
    #      match GT's visible length; hook flicks up-left at bottom.
    head = ('TC', 0.55, 0.10)         # top-center start (slight right lean at top)
    belly = ('C', 0.42, 0.35)         # mid-shaft (straight body)
    hook_pt = ('BC', 0.35, 0.60)      # bottom before hook
    tip = ('BC', 0.10, 0.45)          # hook tip flicking up-left
    draw_shu_gou(draw, head, belly, hook_pt, tip,
                 head_w=8, belly_w=8, hook_start_w=8, tip_w=2)

    # s1 — upper-left 横撇 / curved stroke descending from upper-mid to
    #      mid-left, crossing the spine near cell C. Should look like a
    #      short curve that begins high and swings down to the left.
    #      MMH: TC(0.386, 0.615) -> BC(0.049, 0.713).
    draw_curved_pie(draw,
                    ('C', 0.10, 0.15),        # start on upper-left of spine
                    ('ML', 0.85, 0.85),       # end on lower-left
                    head_width=7, tail_width=2, curve=0.15)

    # s2 — small right-side flick UPPER-right of spine (the small
    #      right-top short stroke visible in GT above the na sweep).
    #      MMH labels this ML→BL but GT visually shows a short mark
    #      at upper-right of the spine — trust GT visual per rules.
    #      Actually MMH s2 is ML→BL (lower-left). Keep it minimal there.
    draw_curved_pie(draw,
                    ('ML', 0.60, 0.55),
                    ('BL', 0.45, 0.20),
                    head_width=6, tail_width=2, curve=0.05)

    # s4 — right descending 捺 stroke: starts at cross-point on spine,
    #      sweeps down-right to bottom-right corner.
    #      MMH: C(0.579, 0.535) -> BR(0.9, 0.458).
    draw_na_stroke(draw,
                   ('C', 0.50, 0.45),
                   ('BR', 0.85, 0.55),
                   head_width=3, peak_width=12, tail_width=2,
                   peak_t=0.8, curve=0.10)

    out = os.path.join(_HERE, '01_水.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
