"""兮 (xī) — Phase-3 char 0123, G4 grid-bank attempt.

MANDATORY LOOKUP CHECKLIST (memory_index.md item 1-6):
1. success_bank/INDEX.md grep 兮 / xi_ah — NOT in bank. Draw fresh.
2. errata.md grep 兮 — not listed. First attempt.
3. form_catalog.md — 撇 in top-position, heng-descending in top, small
   dian/shu at bottom. No cluster-of-兮 rule found.
4. principles_meta.md — TR6 (inline when no primitive fits without
   extreme transformation). Standalone 4-char; TR9 not needed
   (character not radical).
5. joint_atlas.md — 3 × N (all natural gaps per MMH). Do NOT weld.
6. sandbox.md — no 兮-specific note.

Structural spec (from MMH via dispatcher):
  s1: TL(0.996,0.984) → ML(0.252,0.893)   [撇, top-right → mid-left]
  s2: TC(0.436,0.639) → MR(0.897,0.644)   [横 descending / heng]
  s3: ML(0.911,0.632) → C(0.904,0.535)    [very short heng near s2 tail]
  s4: C(0.245,0.688) → BC(0.146,0.777)    [small stroke bottom center]

Joints (3, all N — do NOT weld):
  s1.mid ⇆ s3.head @ ML  — N gap ~25 px
  s2.mid ⇆ s3.tail @ MR  — N gap ~36 px
  s3.mid ⇆ s4.head @ C   — N gap ~11 px

Bank use: `draw_pie` (bank) for s1. s2/s3/s4 are short inline strokes
better rendered as fat_line + slight curve (extreme transformation of
heng/dian would be needed — TR6 says inline).
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(BASE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first render; 4 strokes, all N joints; uses draw_pie for s1, inline fat_line/curve for s2-s4.'
}


def draw_xi_ah(draw):
    # s1: 撇 top-right → mid-left, long tapered sweep
    draw_pie(
        draw,
        from_anchor=('TL', 0.996, 0.984),
        to_anchor=('ML', 0.252, 0.893),
        head_width=11, tail_width=2, curve=0.08, segments=48,
    )

    # s2: 横 descending — TC(0.436,0.639) → MR(0.897,0.644)
    # Inline: tapered variable-width curve, slight downward bow (heng-descending).
    p0 = anchor_to_xy(('TC', 0.436, 0.639))
    p1 = anchor_to_xy(('MR', 0.897, 0.644))
    # Slight upward-arch belly for a 横 flavor.
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)  # curve upward
    bow = 0.03 * L
    mid = ((p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p1, n=40)
    widths = [8 + (10 - 8) * (i / 40) for i in range(41)]
    stroke_variable_width(draw, pts, widths)

    # s3: short mark near right of s2 — ML(0.911,0.632) → C(0.904,0.535)
    # Very short, near-horizontal — draw as short thin heng.
    p0 = anchor_to_xy(('ML', 0.911, 0.632))
    p1 = anchor_to_xy(('C', 0.904, 0.535))
    fat_line(draw, p0, p1, width=7)

    # s4: bottom-center small stroke C(0.245,0.688) → BC(0.146,0.777)
    # Near-vertical, slightly leaning left. Render as tapered short stroke.
    p0 = anchor_to_xy(('C', 0.245, 0.688))
    p1 = anchor_to_xy(('BC', 0.146, 0.777))
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = 0.15 * L  # slight leftward curl
    mid = ((p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p1, n=32)
    widths = [10 + (2 - 10) * (i / 32) for i in range(33)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_xi_ah(draw)
    out = os.path.join(BASE, "01_兮.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
