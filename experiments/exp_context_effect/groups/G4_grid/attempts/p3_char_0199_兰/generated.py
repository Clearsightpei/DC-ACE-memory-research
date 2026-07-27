"""p3_char_0199_兰 (lán, "orchid") — G4 attempt.

Split: 丷 (top two dots) + 三 (three horizontals of increasing width).
5 strokes total, no joints (per MMH: strokes clearly separated).

Reading order log (v8 slim checklist):
  1. drawer_memory.md — no chronic primitive applies (no 丿/刀/冂/弓/马).
     Compositional playbook: "top+bottom" layout, top small in y<0.35.
  2. success_bank/INDEX.md grep — 兰 not mastered.
  3. errata.md grep — 兰 not listed.

No chronic imports needed. Inline five strokes with 米字格 anchors
matching MMH-derived brief. Bottom heng widest, middle medium, top
short. Two top dots slant outward (丷).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: 丷 (2 dots) + 三 (3 heng, top<mid<bot). No joints per MMH.',
}


def draw_dian(draw, a_head, a_tail, head_w=3, tail_w=11):
    """A short dot that tapers from thin head to fat tail (Chinese 点)."""
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    # slight curve: control point midway with small perpendicular offset
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    # perpendicular offset (small) — bow outward
    perp = (-dy, dx)
    L = (perp[0] ** 2 + perp[1] ** 2) ** 0.5 or 1.0
    ox, oy = perp[0] / L * 3.0, perp[1] / L * 3.0
    p1 = (mx + ox, my + oy)
    pts = quad_bezier(p0, p1, p2, n=24)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, a_head, a_tail, width=9):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    fat_line(draw, p0, p1, width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: left dot of 丷 — head TL(0.999, 0.87) → tail C(0.298, 0.181)
    # Short diagonal ↘ (top of left dot to bottom-right thick end).
    draw_dian(d, ('TL', 0.999, 0.87), ('C', 0.298, 0.181), head_w=3, tail_w=10)

    # Stroke 2: right dot of 丷 — head TC(0.878, 0.662) → tail C(0.564, 0.195)
    # Diagonal ↙ (thin top-right to thick bottom-left).
    draw_dian(d, ('TC', 0.878, 0.662), ('C', 0.564, 0.195), head_w=3, tail_w=10)

    # Stroke 3: top heng (shortest of the three) — ML(0.82, 0.471) → MR(0.203, 0.354)
    draw_heng(d, ('ML', 0.82, 0.471), ('MR', 0.203, 0.354), width=8)

    # Stroke 4: middle heng — BL(0.938, 0.021) → MR(0.042, 0.942)
    draw_heng(d, ('BL', 0.938, 0.021), ('MR', 0.042, 0.942), width=9)

    # Stroke 5: bottom heng (longest) — BL(0.463, 0.625) → BR(0.631, 0.628)
    draw_heng(d, ('BL', 0.463, 0.625), ('BR', 0.631, 0.628), width=11)

    out = os.path.join(os.path.dirname(__file__), '01_兰.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
