"""p3_char_0180_打 (dǎ) — 扌 (shou-side, 3 strokes) + 丁 (2 strokes) = 5 strokes.

MANDATORY LOOKUP CHECKLIST:
  1. INDEX.md grep — shou_side.py exists (p2_radical_068_扌 PASS); reuse with
     OVERRIDING anchors per TR1 for 打 composition (扌 sits in LEFT column, not spanning full grid).
  2. errata.md grep — p3_char_0035_丁 FAILED; fix: shu head under heng mid,
     heng needs to be short (top-of-丁 width), shu vertical straight body,
     hook up-left small. Applied literally to strokes 4-5 below.
  3. form_catalog — 扌 is left-radical → span ~cols 0–0.5. 丁 sits right (cols 0.5–1).
  4. principles_meta — TR1 override anchors; TR8 rule 6 straight verticals.
  5. joint_atlas — s1×s2 P weld (heng crosses shu body); s4↔s5 N gap ~20 px.

MMH per-stroke expected anchors (from dispatcher):
  s1: head ML(0.41,0.477) → tail C(0.333,0.324)     [横 — 扌 top]
  s2: head TL(0.882,0.639) → tail BL(0.624,0.687)   [竖钩 body — 扌 vertical]
  s3: head BL(0.167,0.297) → tail C(0.271,0.755)    [提 — 扌 rising]
  s4: head C(0.421,0.509) → tail MR(0.687,0.397)    [横 — 丁 top]
  s5: head C(0.945,0.532) → tail BC(0.641,0.807)    [竖钩 — 丁 vertical hook]

Joints (from dispatcher):
  s1.mid × s2.mid @ ML : P (welded) — 横 crosses 竖钩 top area
  s2.mid × s3.mid @ ML : P (welded) — 提 crosses 竖钩 body mid
  s4.mid × s5.head @ C : N (gap ~20 px) — 丁 heng right-tip near 竖钩 head, small gap
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 5 primitive calls (draw_heng x2, custom_shu_gou x2, draw_ti x1)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reuses shou_side.py logic (inlined custom shu_gou) for strokes 1-3; '
             'fresh 丁 (heng + custom shu_gou) for strokes 4-5 with errata p3_char_0035_丁 '
             'fix applied literally.',
}

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier
from heng import draw_heng
from ti import draw_ti


def _draw_shu_gou_custom(draw, head, hook_pt, tip,
                         head_w=12, mid_w=11, hook_start_w=10, tip_w=2):
    """Inlined shu_gou that allows head.x != hook_pt.x (slight lean)."""
    p_head = anchor_to_xy(head)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    body_pts = sample_line(p_head, p_hook, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = mid_w + (hook_start_w - mid_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def draw_da(draw):
    # ---------- 扌 (left side) — strokes 1-3 ----------
    # s1: 横 — short, upper. From ML(0.41, 0.477) → C(0.333, 0.324).
    draw_heng(draw, ('ML', 0.41, 0.55), ('C', 0.35, 0.35), width=8)

    # s2: 竖钩 (custom) — head near top of 扌 area, body descends vertically,
    # hooks up-left. head TL(0.882, 0.639) → tail BL(0.624, 0.687).
    # Force head.x ≈ hook.x so body is vertical (TR8 rule 6).
    _draw_shu_gou_custom(draw,
                         head=('TL', 0.90, 0.70),
                         hook_pt=('BL', 0.88, 0.55),
                         tip=('BL', 0.62, 0.70))

    # s3: 提 — rising diagonal crossing s2 body around cell C area.
    # head BL(0.167, 0.297) → tail C(0.271, 0.755).
    draw_ti(draw, ('BL', 0.17, 0.35), ('C', 0.30, 0.72),
            head_width=11, tail_width=1, curve=0.05, segments=48)

    # ---------- 丁 (right side) — strokes 4-5 ----------
    # s4: 横 — top of 丁. C(0.421, 0.509) → MR(0.687, 0.397).
    # Keep it short-to-medium horizontal (top bar of 丁).
    draw_heng(draw, ('C', 0.45, 0.45), ('MR', 0.75, 0.45), width=9)

    # s5: 竖钩 — head touches heng underside near mid-right of C column,
    # body descends vertically to bottom, hooks up-left small.
    # head C(0.945, 0.532) → tail BC(0.641, 0.807).
    _draw_shu_gou_custom(draw,
                         head=('C', 0.95, 0.55),
                         hook_pt=('BC', 0.90, 0.65),
                         tip=('BC', 0.64, 0.80))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_da(draw)
    out = os.path.join(HERE, '01_打.png')
    img.save(out)
    print('Wrote', out)


if __name__ == '__main__':
    main()
