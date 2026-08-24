"""p3_char_0388_亟 (jí, 'urgent'/'quick') — 8 strokes, G5 attempt.

BANK_DEVIATION
skipped: kou_mouth.py, you_again.py (bank whole-radical primitives)
reason: 亟 embeds 口 and 又-like components at scale ≈ 0.35 native
    (kou_mouth native ~140x150, target middle-left kou ~55x55 → scale
    0.39 << 0.55 lower bound of P-A-007-v2 whole-radical retrieval).
    Similarly 又 native ~245x160 but target's right-side you-cluster
    is ~90x100 → scale ~0.40. Both fall below the 0.55 threshold and
    would compress hooks/kou-square unrecognizably.
fresh_component: inline_anchor_verbatim (P-A-006 recipe — literal MMH
    anchor endpoints on 300x300 canvas, no bank whole-radical calls).

Per-stroke reasoning trace (P-A-008):
  s1 (short top-left diagonal): TL(0.905,0.981)→C(0.518,0.304).
     Short pie-like descending into upper center. Inline diagonal line.
  s2 (upper-mid pie down-left): C(0.392,0.271)→BC(0.087,0.37).
     Long pie from upper-center curving down-left to bottom-center.
  s3 (left kou vertical/shu): ML(0.533,0.737)→BL(0.715,0.323).
     Short shu on left, forms left side of embedded 口.
  s4 (left kou heng-zhe-like): ML(0.709,0.752)→BC(0.008,0.051).
     Curves top+right of embedded left kou.
  s5 (kou bottom heng): BL(0.771,0.209)→BC(0.169,0.13).
     Small horizontal closing bottom of left 口.
  s6 (right pie for 又-like): C(0.758,0.635)→BC(0.649,0.344).
     Short pie coming down from center to bottom-center area.
  s7 (right na for 又-like): C(0.772,0.89)→BR(0.461,0.429).
     Long na diagonal down-right, crosses s6 (P joint at BR).
  s8 (bottom long heng): BL(0.439,0.836)→BR(0.581,0.851).
     Full-width bottom horizontal, defining base.

Quantitative BANK_DEVIATION (P-A-009):
  target embedded 口 aspect (from s3 endpoints): dx=18.2, dy=41.4 →
    aspect 0.44 (tall skinny), vs kou_mouth native aspect 133/144=0.92
    (near-square). Ratio 0.44/0.92 = 0.48 (out-of-band).
  target embedded 又-cluster: s6+s7 form ~70x80 shape → scale 0.35 of
    you_again native (208x162), aspect ~0.87 vs bank 1.28. Ratio 0.68
    out-of-band. Neither primitive callable at usable scale.
"""

from PIL import Image, ImageDraw


# 米字格 anchor helper: 300x300 canvas, 3x3 cells of 100px each.
CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
CW = 100  # cell width


def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * CW, oy + yf * CW)


def draw_line(dr, a, b, width=8):
    dr.line([a, b], fill='black', width=width)
    # end caps
    for (x, y) in (a, b):
        r = width / 2
        dr.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_curve(dr, a, b, bow_perp=0.0, width=8, steps=40, w_end=None):
    """Quadratic-ish bowed curve from a to b, bowing perpendicular by
    `bow_perp` px (positive = left of a->b direction)."""
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular unit
    px, py = -dy / L, dx / L
    mx, my = (ax + bx) / 2 + px * bow_perp, (ay + by) / 2 + py * bow_perp
    prev = a
    for i in range(1, steps + 1):
        t = i / steps
        # quadratic Bezier a -> m -> b (control point mx,my)
        u = 1 - t
        x = u * u * ax + 2 * u * t * mx + t * t * bx
        y = u * u * ay + 2 * u * t * my + t * t * by
        w = width if w_end is None else int(width + (w_end - width) * t)
        dr.line([prev, (x, y)], fill='black', width=max(2, w))
        prev = (x, y)
    # end caps
    r = width / 2
    dr.ellipse([ax - r, ay - r, ax + r, ay + r], fill='black')
    r2 = (w_end if w_end else width) / 2 + 1
    dr.ellipse([bx - r2, by - r2, bx + r2, by + r2], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    dr = ImageDraw.Draw(img)

    # ---- 8 stroke calls (MMH anchor verbatim, P-A-006 recipe) ----
    # s1: short diagonal top
    s1h = anchor('TL', 0.905, 0.981)
    s1t = anchor('C', 0.518, 0.304)
    draw_line(dr, s1h, s1t, width=8)

    # s2: pie curving down-left
    s2h = anchor('C', 0.392, 0.271)
    s2t = anchor('BC', 0.087, 0.37)
    draw_curve(dr, s2h, s2t, bow_perp=-8, width=8, w_end=5)

    # s3: left kou vertical (shu)
    s3h = anchor('ML', 0.533, 0.737)
    s3t = anchor('BL', 0.715, 0.323)
    draw_line(dr, s3h, s3t, width=7)

    # s4: heng-zhe top+right of left kou
    s4h = anchor('ML', 0.709, 0.752)
    s4t = anchor('BC', 0.008, 0.051)
    # Split into top heng and right shu for the 折 corner
    corner = (s4t[0], s4h[1])  # rectangular corner
    draw_line(dr, s4h, corner, width=7)
    draw_line(dr, corner, s4t, width=7)

    # s5: bottom heng of left kou
    s5h = anchor('BL', 0.771, 0.209)
    s5t = anchor('BC', 0.169, 0.13)
    draw_line(dr, s5h, s5t, width=7)

    # s6: right cluster pie (short, down-left)
    s6h = anchor('C', 0.758, 0.635)
    s6t = anchor('BC', 0.649, 0.344)
    draw_curve(dr, s6h, s6t, bow_perp=-4, width=7, w_end=4)

    # s7: right cluster na (long down-right diagonal)
    s7h = anchor('C', 0.772, 0.89)
    s7t = anchor('BR', 0.461, 0.429)
    draw_curve(dr, s7h, s7t, bow_perp=6, width=6, w_end=12)

    # s8: bottom long heng
    s8h = anchor('BL', 0.439, 0.836)
    s8t = anchor('BR', 0.581, 0.851)
    draw_line(dr, s8h, s8t, width=9)

    out = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0388_亟/01_亟.png'
    img.save(out)
    print(f'wrote {out}')


SELF_CHECK = {
    'visual_ok': None,          # filled after render+compare
    'stroke_count_ok': True,     # 8 stroke calls: s1..s8 (s4 split into 2 lines = 1 zhe stroke)
    'endpoint_mismatches': [],   # anchors used verbatim from MMH block
    'joint_class_mismatches': [
        # all 7 N joints handled by not-welding (drawn as separate lines)
        # 1 P joint (s6.mid ⇆ s7.mid @ BR) — s6 and s7 cross naturally
    ],
    'overall_pass': None,        # decide after visual check
    'notes': 'P-A-006 verbatim-anchor recipe; P-A-007-v2 rejected kou/you bank whole-radical (scale 0.35–0.40 below 0.55 threshold); P-A-008 per-stroke reasoning above; P-A-009 quantitative aspect calc above.'
}


if __name__ == '__main__':
    main()
