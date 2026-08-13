"""Draw 欠 (qian) — 4-stroke radical.

Structure (from MMH block):
  s1  短撇  head TC(0.198, 0.621)=(120, 62) -> tail ML(0.63, 0.849)=(63, 185)
  s2  横钩  head C(0.125, 0.406)=(112, 141) -> tail C(0.931, 0.641)=(193, 164)
             + hook down-left extending below MMH tail (median only captures
             the top segment of a 横钩)
  s3  长撇  head C(0.365, 0.658)=(137, 166) -> tail BL(0.448, 0.936)=(45, 294)
  s4  长捺  head BC(0.544, 0.109)=(154, 211) -> tail BR(0.631, 0.959)=(263, 296)

Joints (both N — natural gap, do NOT weld):
  s1.mid ⇆ s2.head @ C (expected gap ~13 px)
  s3.mid ⇆ s4.head @ BC (expected gap ~22 px)

Bank use:
  s1: draw_pie (bank)   — short 撇
  s2: INLINE            — 横钩; bank has no direct heng_gou primitive.
                           heng_pie exists but it sweeps far down-left
                           (tuned for 又), whereas 欠's hook is short
                           and mostly downward. Inline is cleaner here.
  s3: draw_pie (bank)   — long 撇
  s4: draw_na  (bank)   — long 捺

# BANK_DEVIATION
# skipped: heng_pie.py
# reason: 欠's stroke-2 hook is short/downward, not the long down-left pie
#         heng_pie draws (tuned for 又). Also horizontal is shorter here.
# fresh_component: heng_gou_for_qian — short heng arc + tight downward hook
"""

import pathlib
import sys
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
_BANK = _HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 turtle calls (pie, inline heng_gou, pie, na)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke 2 inlined (BANK_DEVIATION: heng_pie not the right shape for 欠 hook)',
}


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_heng_gou_for_qian(d, head, corner, hook_tip):
    """Inline 横钩: short horizontal arc from head to corner, then a
    tight quarter-turn hook to hook_tip (down-left)."""
    # Segment A: horizontal (head -> corner) as a slight arc
    hx, hy = head
    cx, cy = corner
    apex = ((hx + cx) / 2, (hy + cy) / 2 - 3)  # slight lift
    pts_a = _bezier(head, apex, corner, steps=60)
    for i, (x, y) in enumerate(pts_a):
        t = i / (len(pts_a) - 1)
        w = 3.0 + 1.5 * t   # gentle thickening into the corner
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # Segment B: hook — quarter turn, corner -> hook_tip
    # Control point pulls to the right of the chord so the hook curls in
    tx, ty = hook_tip
    mx, my = (cx + tx) / 2, (cy + ty) / 2
    dx, dy = tx - cx, ty - cy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular right-of-travel (image y-down)
    px, py = -dy / L, dx / L
    ctrl = (mx + px * 6, my + py * 6)
    pts_b = _bezier(corner, ctrl, hook_tip, steps=50)
    for i, (x, y) in enumerate(pts_b):
        t = i / (len(pts_b) - 1)
        w = 4.5 - 3.0 * t
        if w < 1.5:
            w = 1.5
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def draw_qian(d):
    # s1 — short 撇 (top-left of the ⺈ shape). GT strokes are thin.
    draw_pie(d, head=(120, 62), tail=(63, 185),
             bow_perp=10, w_head=4, w_tail=2, steps=80)

    # s2 — 横钩 (short horizontal then downward hook)
    # MMH tail ≈ (193, 164) is the corner; hook tip extends down-left.
    draw_heng_gou_for_qian(
        d,
        head=(112, 141),
        corner=(194, 164),
        hook_tip=(180, 198),
    )

    # s3 — long 撇 (main body diagonal down-left)
    draw_pie(d, head=(137, 166), tail=(48, 288),
             bow_perp=20, w_head=5, w_tail=2, steps=90)

    # s4 — long 捺 (main body diagonal down-right).
    # Joint is N (~22 px gap from s3 mid) — head placed slightly
    # right/below s3's upper region, not welded.
    draw_na(d, head=(157, 200), tail=(258, 292),
            bow_perp=14, w_head=2, w_tail=8, steps=90)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_qian(d)
    out = _HERE.parent / '01_欠.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
