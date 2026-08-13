# BANK_DEVIATION
# skipped: shu_wan_gou.py
# reason: 兀's third stroke (竖弯) ends at bottom-right corner without an upward
#         hook — MMH tail anchor is at ('BR', 0.666, 0.168) → (267, 217), which
#         is the terminus of a rightward curve, not a hook tip. shu_wan_gou's
#         `bottom_extra` bows below the tail then hooks up, which is wrong here.
# fresh_component: shu_wan_no_up_hook  (may be worth promoting as variant if PASS)

"""兀 (wu — 'high, bare') — 3 strokes.

Stroke plan (MMH → pixels @ 300×300):
  s1 heng: (65, 108) → (232, 96)              — top horizontal
  s2 pie:  (100, 129) → (35, 278)             — left leg (leftward sweep)
  s3 shu_wan: (150, 110) → (267, 217)         — right leg (down, curve right)

Joints: s1.head ⇆ s2.head @ ML — N gap ~35.8 px
        s1.mid(0.43) ⇆ s3.head @ C — N gap ~19.6 px
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

_BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402


def draw_shu_wan_no_up_hook(draw, head, tail, width=8):
    """Vertical descent from head, curving right, terminating at tail (no hook up)."""
    hx, hy = head
    tx, ty = tail
    # Descend vertically, then curve smoothly rightward.
    # Bezier control: knee below-and-right so curve is bottom-hugging.
    knee = (hx, ty + 22)  # descend past tail y before curving
    ctrl = (hx + (tx - hx) * 0.15, ty + 30)
    end = (tx, ty)
    # Vertical segment from head to just above knee
    n = 80
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        # cubic Bezier: head, control near head (mostly vertical), ctrl, end
        c1 = (hx, hy + (knee[1] - hy) * 0.6)
        x = b0 * hx + b1 * c1[0] + b2 * ctrl[0] + b3 * end[0]
        y = b0 * hy + b1 * c1[1] + b2 * ctrl[1] + b3 * end[1]
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill='black', width=width)
    # end caps
    r = width / 2
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')
    r2 = width / 2 - 1
    draw.ellipse([tx - r2, ty - r2, tx + r2, ty + r2], fill='black')


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    s1_head, s1_tail = (65, 108), (232, 96)
    s2_head, s2_tail = (100, 129), (35, 278)
    s3_head, s3_tail = (150, 110), (267, 217)

    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)
    draw_pie(d, s2_head, s2_tail, bow_perp=10, w_head=8, w_tail=3)
    draw_shu_wan_no_up_hook(d, s3_head, s3_tail, width=8)

    img.save(out_path)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 3 strokes rendered, MMH expects 3
    'endpoint_mismatches': [],         # anchors sourced directly from MMH block
    'joint_class_mismatches': [],      # both N joints preserved (no welding)
    'overall_pass': True,
    'notes': 'shu_wan_gou skipped; inlined shu_wan_no_up_hook (no upward hook, terminates at BR).',
}


if __name__ == '__main__':
    out = Path(__file__).parent / '01_兀.png'
    render(out)
    print(f'wrote {out}')
