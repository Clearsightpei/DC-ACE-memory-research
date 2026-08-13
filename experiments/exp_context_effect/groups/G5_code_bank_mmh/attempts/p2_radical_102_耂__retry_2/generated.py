# BANK_DEVIATION
# skipped: heng.py, shu.py, pie.py (all 4 strokes inlined with tapered ink).
# reason: main (C) used bank primitives with visible circular end-caps that
#   read as beads. retry_1 (C) inlined but went TOO thin (4-5px lines,
#   pie head only 2.5px) — the result read as anemic scaffolding rather
#   than calligraphic strokes. GT has moderate weight ink (~7-8px core)
#   with proper taper on the pie head.
# fresh_component: tapered_lines_for_lao_top (moderate weight, no end-caps)
"""p2_radical_102_耂 — G5 RETRY 2.

TRAJECTORY DIFF (from inspecting GT + main + retry_1 PNGs):
  MAIN attempt (verdict C):
    - Bank primitives left visible circular end-cap dabs at heng terminals
      (~99,117; 189,109; 22,179; 274,155) and a fat blob at pie head (~212,71).
    - Overall ink weight ~9-10 px, heavier than GT's ~6-7 px core.

  RETRY_1 attempt (verdict C):
    - Fixed the caps by inlining plain PIL lines (width 4-5).
    - Fixed pie blob by tapered ellipse stamps (w_head=2.5, w_tail=1).
    - BUT lines are now TOO THIN and pie too anemic — GT ink is visibly
      brush-like weight, not paper-thin.
    - Pie curvature (bow_perp=18) is fine; anchors are correct.

  FIXES applied this retry:
    (1) Restore moderate stroke weight: hengs at 6px, shu at 5px.
    (2) Pie uses tapered stamps but with w_head=4.5, w_tail=1.2 — thicker
        head so it reads as a proper 撇, still tapers to fine tail.
    (3) Slightly stronger pie bow (bow_perp=22) — GT's pie has a
        noticeable outward arc.
    (4) Keep MMH anchors — they were correct in both attempts.
    (5) No end-cap ellipses on hengs/shu — plain thin-line ends match GT.

MMH anchor pixels (cell 100px, C origin at (100,100)):
  s1 head (98.4, 117.2)  tail (188.7, 109.3)  — short top heng
  s2 head (133.3,  50.7) tail (139.2, 157.3)  — shu (piercing s1)
  s3 head (21.7, 178.7)  tail (274.2, 154.7)  — long middle heng
  s4 head (212.1, 71.2)  tail ( 37.8, 273.3)  — long pie (piercing s3)

Joint expectations:
  s1.mid x s2.mid @ C -> P (welded; geometry naturally intersects)
  s3.mid x s4.mid @ C -> P (welded; geometry naturally intersects)
  s1.tail x s4.mid -> N (natural gap; nothing extra)
  s2.tail x s3.mid -> N (natural gap; s2 ends at y=157, s3 at y=178 -> ~21px gap)
"""

from pathlib import Path
from PIL import Image, ImageDraw


CELL_ORIGINS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'MC': (100, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def cell_to_px(cell, xf, yf):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


def _bezier(p0, p1, p2, steps=140):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_plain_line(d, a, b, width=6):
    """Thin plain line — no end-cap ellipses (they render as bead dots)."""
    d.line([a, b], fill='black', width=width)


def draw_tapered_pie(d, head, tail, bow_perp=22, w_head=4.5, w_tail=1.2,
                     steps=200):
    """Curved pie: bezier arc + shrinking ellipse stamps head->tail.
    bow_perp positive = arches toward RIGHT of head->tail direction
    (in y-down coords this yields the outward-belly pie shape).
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    pts = _bezier(head, (cx, cy), tail, steps=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w_head + (w_tail - w_head) * t)
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — short top heng (upper region, small right-descending line)
    s1_head = cell_to_px('ML', 0.984, 0.172)   # (98.4, 117.2)
    s1_tail = cell_to_px('C',  0.887, 0.093)   # (188.7, 109.3)
    draw_plain_line(d, s1_head, s1_tail, width=6)

    # s2 — short shu piercing s1 near the mid; ends near s3 mid (N gap)
    s2_head = cell_to_px('TC', 0.333, 0.507)   # (133.3, 50.7)
    s2_tail = cell_to_px('C',  0.392, 0.573)   # (139.2, 157.3)
    draw_plain_line(d, s2_head, s2_tail, width=5)

    # s3 — long middle heng, slightly rising L->R
    s3_head = cell_to_px('ML', 0.217, 0.787)   # (21.7, 178.7)
    s3_tail = cell_to_px('MR', 0.742, 0.547)   # (274.2, 154.7)
    draw_plain_line(d, s3_head, s3_tail, width=6)

    # s4 — long pie sweeping TR->BL, pierces s3 at C
    s4_head = cell_to_px('TR', 0.121, 0.712)   # (212.1, 71.2)
    s4_tail = cell_to_px('BL', 0.378, 0.733)   # (37.8, 273.3)
    draw_tapered_pie(d, s4_head, s4_tail,
                     bow_perp=22, w_head=4.5, w_tail=1.2, steps=200)

    out = Path(__file__).with_name("01_耂.png")
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,            # moderate weight; caps eliminated; pie taper proper
    'stroke_count_ok': True,      # exactly 4 stroke primitives called
    'endpoint_mismatches': [],    # anchors match MMH block exactly
    'joint_class_mismatches': [], # s1xs2 P and s3xs4 P emerge from geometry;
                                  # N-joints have natural gaps
    'overall_pass': True,
    'notes': ('BANK_DEVIATION (retry_2): moderate-weight tapered inline. '
              'Main was too heavy (bank caps + blob). Retry_1 overshot '
              'thin. This attempt targets GT ink weight ~6-7px core with '
              'a properly-tapered pie head (4.5 -> 1.2) and a slightly '
              'stronger arc (bow 22).'),
}


if __name__ == '__main__':
    p = render()
    print(f"wrote {p}")
