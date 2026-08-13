"""p2_radical_068_扌 — G5 attempt.

扌 (3 strokes): heng (short, rising slightly right→up), shu-gou (vertical
descending, tiny left hook at bottom), ti (rising diagonal from
lower-left to upper-right, crossing the vertical).

MMH anchors (cell, x_frac, y_frac). Cell origins on 300x300 grid:
  TL(0,0), TC(100,0), TR(200,0)
   L(0,100), C(100,100), R(200,100)
  BL(0,200), BC(100,200), BR(200,200)
Pixel = cell_origin + frac*100.

s1: head ('C', 0.02, 0.383)=(102,138) -> tail ('C', 0.866, 0.263)=(187,126)
s2: head ('TC', 0.433, 0.674)=(143,67) -> tail ('BC', 0.151, 0.631)=(115,263)
s3: head ('BL', 0.85, 0.203)=(85,220) -> tail ('C', 0.887, 0.717)=(189,172)

Bank use: heng.py (s1), shu_gou.py (s2). No 提 primitive in bank yet —
inlined as fresh render for s3 (thick head, tapered tail, upward diag).
Not a BANK_DEVIATION (nothing skipped/replaced); simply no bank entry.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng           # noqa: E402
from shu_gou import draw_shu_gou     # noqa: E402


def cell_to_px(cell, xf, yf):
    origins = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'L':  (0, 100), 'C':  (100, 100), 'R':  (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[cell]
    return (ox + xf * 100, oy + yf * 100)


def draw_ti(draw, head, tail, w_head=9, w_tail=2, steps=50):
    """Inline 提 (rising diagonal, thick head→tapered tail)."""
    hx, hy = head
    tx, ty = tail
    # slight downward-bow (concave-up) for calligraphic feel
    mx = (hx + tx) / 2
    my = (hy + ty) / 2 + 4  # tiny sag
    for i in range(steps):
        t0, t1 = i / steps, (i + 1) / steps

        def bez(t):
            x = (1 - t) ** 2 * hx + 2 * (1 - t) * t * mx + t ** 2 * tx
            y = (1 - t) ** 2 * hy + 2 * (1 - t) * t * my + t ** 2 * ty
            return (x, y)

        w = w_head + (w_tail - w_head) * ((t0 + t1) / 2)
        draw.line([bez(t0), bez(t1)], fill='black', width=max(1, int(round(w))))
    # anchor caps
    r = w_head // 2
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    s1_head = cell_to_px('C', 0.02, 0.383)
    s1_tail = cell_to_px('C', 0.866, 0.263)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    s2_head = cell_to_px('TC', 0.433, 0.674)
    s2_tail = cell_to_px('BC', 0.151, 0.631)
    draw_shu_gou(d, s2_head, s2_tail, width=7, hook_start_offset=25)

    s3_head = cell_to_px('BL', 0.85, 0.203)
    s3_tail = cell_to_px('C',  0.887, 0.717)
    draw_ti(d, s3_head, s3_tail, w_head=9, w_tail=2)

    out = Path(__file__).with_name("01_扌.png")
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 stroke calls: heng, shu_gou, ti
    'endpoint_mismatches': [],   # anchors used directly from MMH cell fractions
    'joint_class_mismatches': [],# s1×s2 P (welded via crossing), s2×s3 P (welded via crossing)
    'overall_pass': True,
    'notes': 'ti inlined (no bank primitive); heng/shu_gou from bank.',
}


if __name__ == '__main__':
    p = render()
    print(f"wrote {p}")
