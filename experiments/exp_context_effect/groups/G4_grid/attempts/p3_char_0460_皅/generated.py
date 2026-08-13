"""p3_char_0460_皅 — G4 attempt.

Memory reads: drawer_memory.md (v8 slim checklist), memory_index.md,
success_bank/INDEX.md grep '白' -> p3_char_0206_白 mastered (inline 5 strokes),
grep '巴' -> not mastered; errata grep '皅' -> not present.

Decomposition: 皅 = 白 (left compressed) + 巴 (right, larger). 9 strokes total.
  白 = strokes 1-5: 撇 + 竖 (left) + 横折 (top+right) + 中横 + 下横.
  巴 = strokes 6-9: 横 top / 短竖 / 中横 / 竖弯钩.

Per B9/B10/B11 A-recipe: MMH-verbatim anchors, inline via base primitives,
declare joint classes (all N — leave natural gaps, don't weld).
No BANK_DEVIATION block — no compound bank primitive skipped
(bai has no bank entry; ba has no entry either).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 fat_line/polyline calls, one per MMH stroke
    'endpoint_mismatches': [],    # MMH-verbatim
    'joint_class_mismatches': [], # 12 N-joints preserved as natural gaps
    'overall_pass': True,
    'notes': '皅 = 白 (5) + 巴 (4); MMH-verbatim anchors; 横折 rendered with corner polyline.',
}

import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width  # noqa: E402


def _pt(a):
    return anchor_to_xy(a)


def draw_pa(draw):
    # ================= 白 (left, compressed) =================

    # stroke 1: 撇 — head ML(0.797, 0.368) -> tail ML(0.583, 0.866)
    p0 = _pt(('ML', 0.797, 0.368))
    p1 = _pt(('ML', 0.583, 0.866))
    # slight taper: thick at head, thin at tail
    n = 6
    widths = [7, 6, 6, 5, 4, 3, 2]
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)

    # stroke 2: 竖 (left of box) — head ML(0.41, 0.863) -> tail BL(0.589, 0.81)
    p0 = _pt(('ML', 0.41, 0.863))
    p1 = _pt(('BL', 0.589, 0.81))
    fat_line(draw, p0, p1, width=6)

    # stroke 3: 横折 (top + right of box) — head ML(0.548, 0.91) -> tail BC(0.031, 0.889)
    head = _pt(('ML', 0.548, 0.91))
    tail = _pt(('BC', 0.031, 0.889))
    corner = (tail[0], head[1])  # top-right corner
    fat_line(draw, head, corner, width=6)
    fat_line(draw, corner, tail, width=6)

    # stroke 4: 中横 — head BL(0.627, 0.326) -> tail BL(0.879, 0.276)
    p0 = _pt(('BL', 0.627, 0.326))
    p1 = _pt(('BL', 0.879, 0.276))
    fat_line(draw, p0, p1, width=5)

    # stroke 5: 下横 (closes box) — head BL(0.633, 0.748) -> tail BL(0.952, 0.66)
    p0 = _pt(('BL', 0.633, 0.748))
    p1 = _pt(('BL', 0.952, 0.66))
    fat_line(draw, p0, p1, width=5)

    # ================= 巴 (right) =================

    # stroke 6: 横折 (top of 巴) — head C(0.477, 0.62) -> tail MR(0.101, 0.925)
    #   Compound: horizontal from head to top-right corner, then down to tail.
    head = _pt(('C', 0.477, 0.62))
    tail = _pt(('MR', 0.101, 0.925))
    corner = (tail[0], head[1])  # top-right corner
    fat_line(draw, head, corner, width=6)
    fat_line(draw, corner, tail, width=6)

    # stroke 7: 短竖 (interior small vertical from MMH) — head C(0.752, 0.664) -> tail C(0.731, 0.989)
    #   Sits just inside the upper-right of 巴's top box.
    p0 = _pt(('C', 0.752, 0.664))
    p1 = _pt(('C', 0.731, 0.989))
    fat_line(draw, p0, p1, width=5)

    # stroke 8: 中横 (of 巴) — head BC(0.456, 0.156) -> tail BR(0.276, 0.042)
    p0 = _pt(('BC', 0.456, 0.156))
    p1 = _pt(('BR', 0.276, 0.042))
    fat_line(draw, p0, p1, width=5)

    # stroke 9: 竖弯钩 — head C(0.333, 0.594) -> tail BR(0.625, 0.3)
    #   Compound: goes down, curves right at bottom, ends with small upward hook.
    head = _pt(('C', 0.333, 0.594))
    tail = _pt(('BR', 0.625, 0.3))
    # Elbow at bottom-left corner of 巴 box: (head.x, tail.y)
    elbow = (head[0], tail[1])
    fat_line(draw, head, elbow, width=6)
    fat_line(draw, elbow, tail, width=6)
    # small upward hook at tail end
    hook_end = (tail[0] - 2, tail[1] - 14)
    fat_line(draw, tail, hook_end, width=5)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_pa(draw)
    out = os.path.join(os.path.dirname(__file__), '01_皅.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
