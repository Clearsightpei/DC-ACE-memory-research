# BANK_DEVIATION
# skipped: none for stroke 1 (uses draw_pie from bank)
# replaced: strokes 2 and 3 inlined (no bank primitive matches the short
#           top-right dot/hook nor the 竖提 shape needed for 饣)
# reason: 饣 has a small angled hook (top) and a 竖提 (rising-hook tail)
#         that don't correspond to any current bank entry
# fresh_component: shi_top_hook_for_饣, shi_shu_ti_for_饣

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 strokes: pie, top-hook, shu-ti
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'N-class joints (natural gaps) between strokes 2/3 heads and pie mid; strokes not welded'
}

import sys
import pathlib
from PIL import Image, ImageDraw

BANK_DIR = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK_DIR))

from pie import draw_pie  # noqa: E402


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_top_hook(draw, head, tail):
    """Small angled hook — head goes down-right, then flicks slightly.
    For 饣's stroke 2 (short 横钩-like mark near mid-upper)."""
    ctrl = ((head[0] + tail[0]) / 2 + 4, (head[1] + tail[1]) / 2 - 6)
    pts = _bezier(head, ctrl, tail, steps=40)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = 3.2 + 2.2 * t  # thickens toward tail (hook end)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
    # small terminal flick pointing down-left (typical 横钩 hook)
    fx, fy = tail
    draw.line([tail, (fx - 8, fy + 6)], fill='black', width=4)


def draw_shu_ti(draw, head, tail):
    """竖提: starts near-vertical from head, curves at bottom, rises to tail.
    For 饣's stroke 3."""
    # go down first, then curve up-right to tail
    mid_x = head[0] - 4
    mid_y = tail[1] + 22  # curve extends below the tail y before rising
    ctrl1 = (head[0] - 2, head[1] + (mid_y - head[1]) * 0.6)
    corner = (mid_x, mid_y)
    # segment A: head → corner (near vertical, slight bow left)
    ptsA = _bezier(head, ctrl1, corner, steps=45)
    for i, (x, y) in enumerate(ptsA):
        t = i / (len(ptsA) - 1)
        r = 5.5 - 1.5 * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
    # segment B: corner → tail (the 提 rising portion — up-right)
    ctrlB = (corner[0] + 20, corner[1] + 4)
    ptsB = _bezier(corner, ctrlB, tail, steps=35)
    for i, (x, y) in enumerate(ptsB):
        t = i / (len(ptsB) - 1)
        r = 4.5 - 2.5 * t  # tapers to a fine tip (提 flicks to a point)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 撇 (long) — MMH head TC(0.447, 0.671) → tail ML(0.803, 0.995)
    #   TC cell x∈[100,200], y∈[0,100]  → head (144.7, 67.1)
    #   ML cell x∈[0,100], y∈[100,200]  → tail (80.3, 199.5)
    draw_pie(draw, head=(144, 67), tail=(80, 200),
             bow_perp=14, w_head=8, w_tail=3, steps=90)

    # Stroke 2: short top hook — MMH C(0.43, 0.356) → C(0.752, 0.714)
    #   head (143, 135.6), tail (175.2, 171.4)
    # Joint 1 is N-class: gap ~17px from pie midpoint — so nudge head slightly right
    draw_top_hook(draw, head=(148, 132), tail=(178, 168))

    # Stroke 3: 竖提 — MMH C(0.392, 0.673) → BC(0.901, 0.388)
    #   head (139.2, 167.3), tail (190.1, 238.8)
    # Joint 2 is N-class: gap ~30px from pie mid — nudge head slightly right
    draw_shu_ti(draw, head=(145, 172), tail=(192, 236))

    out = pathlib.Path(__file__).parent / '01_饣.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
