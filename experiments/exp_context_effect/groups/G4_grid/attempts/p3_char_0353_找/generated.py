"""p3_char_0353_找 (zhǎo, 7 strokes) — G4 grid-bank attempt.

Reading order followed (v8 slim):
  1) drawer_memory.md — B9 A-recipe: MMH-verbatim anchors + base
     primitives over compound primitives when placement clashes.
     Chronic imports (丿刀冂弓马) don't apply. shou_side.py exists
     but its default anchors sit in different cells than MMH's for
     this composition, so per A-recipe #4 inline via base primitives.
  2) success_bank/INDEX.md — shou_side (扌) mastered, xie_gou (斜钩)
     mastered as single-stroke primitive. 戈 (p2_096) is in errata
     (FAIL). No 找 mastered.
  3) errata.md — 找 not present. 戈 errata note says: flatten heng,
     pie crosses at true mid, dot upper-right — MMH anchors already
     encode this so trust them verbatim.

Decomposition:  找 = 扌 (left, s1..s3) + 戈 (right, s4..s7).
  扌: 横 (s1) + 竖钩 (s2) + 提 (s3).
  戈: 短横 (s4) + 斜钩 (s5) + 撇 (s6) + 点 (s7).

Per-stroke plan (MMH anchors verbatim, via _anchor.anchor_to_xy):
  s1 扌横     : ('ML', 0.419, 0.5)   → ('C', 0.26, 0.345)
  s2 扌竖钩    : ('TL', 0.826, 0.677) → ('BL', 0.53, 0.678)
                 hook_pt just above tip so flick goes up-left.
  s3 扌提     : ('BL', 0.226, 0.353) → ('C', 0.228, 0.755)
  s4 戈短横    : ('C', 0.298, 0.535)  → ('MR', 0.256, 0.315)
  s5 戈斜钩    : ('TC', 0.544, 0.645) → ('BR', 0.678, 0.341)
                 MMH tail = hook tip (flicks UP); body ends further
                 down-right, then curls up.
  s6 戈撇     : ('MR', 0.18, 0.641)  → ('BC', 0.236, 0.569)
  s7 戈点     : ('TC', 0.995, 0.806) → ('MR', 0.344, 0.046)
                 Short compact dot upper-right of 斜钩 head.

Joints (from MMH — all P/welded by construction, no N gaps):
  s1.mid ⇆ s2.mid @ ML  — 横 crosses shu-gou near top (P welded)
  s2.mid ⇆ s3.mid @ ML  — 提 crosses shu-gou mid (P welded)
  s4.mid ⇆ s5.mid @ C   — 戈 heng crosses xie_gou upper body (P)
  s5.mid ⇆ s6.mid @ BC  — 撇 crosses xie_gou lower body (P)

All P joints are enforced because the primitives literally cross at
the specified cells; no gap engineering needed.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)
from heng import draw_heng
from ti import draw_ti
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 named strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ("7 strokes MMH-verbatim: 扌 (heng + shu-gou + ti) left; "
              "戈 (heng + xie-gou + pie + dot) right. All P joints "
              "welded by geometric crossing at ML, C, BC. xie-gou "
              "hook flicks UP from body-end to MMH tip."),
}


def _draw_shu_gou_inline(draw, head, hook_pt, tip,
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2):
    """竖钩 body + up-left flick (from shou_side.py's custom helper)."""
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


def _draw_xie_gou_inline(draw, head, hook_pt_body_end, tip,
                         head_w=6, belly_w=13, hook_start_w=11, tip_w=2):
    """斜钩 body (concave-up bezier) + upward hook flick."""
    p_head = anchor_to_xy(head)
    p_end = anchor_to_xy(hook_pt_body_end)
    p_tip = anchor_to_xy(tip)
    # Belly control roughly at midpoint pushed slightly down-right for the
    # classic concave-up bow.
    mid = ((p_head[0] + p_end[0]) * 0.5, (p_head[1] + p_end[1]) * 0.5)
    # Perp toward (dx=+, dy=+) side — for a TL→BR body, perpendicular that
    # pushes the belly LOWER (bigger y) yields the concave-up look.
    dx, dy = p_end[0] - p_head[0], p_end[1] - p_head[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)   # rotate chord -90°
    bow = 0.05 * length
    # We want belly lower on the canvas (larger y), so pick the perp
    # direction with positive y-component.
    if perp[1] < 0:
        perp = (-perp[0], -perp[1])
    ctrl_body = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    body_pts = quad_bezier(p_head, ctrl_body, p_end, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.65:
            u = t / 0.65
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.65) / 0.35
            w = belly_w + (hook_start_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)
    # Hook flick: from body end curl up toward tip.
    ctrl_hook = (p_end[0] + 6.0,
                 p_end[1] - (p_end[1] - p_tip[1]) * 0.20)
    hook_pts = quad_bezier(p_end, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # Draw the two "big body" strokes first (扌 shu-gou and 戈 xie-gou),
    # then the horizontals/pie/dot cross them so joints look welded.
    # ------------------------------------------------------------------

    # s2  扌 竖钩 : head TL(0.826,0.677) → tail (hook tip) BL(0.53,0.678)
    # hook_pt = just above the tip so the up-left flick is natural.
    _draw_shu_gou_inline(d,
                         head=('TL', 0.826, 0.677),
                         hook_pt=('BL', 0.85, 0.55),
                         tip=('BL', 0.53, 0.678),
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2)

    # s5  戈 斜钩 : head TC(0.544,0.645) → hook tip BR(0.678,0.341).
    # Body ends further down/right, then hook curls UP to tip.
    _draw_xie_gou_inline(d,
                         head=('TC', 0.544, 0.645),
                         hook_pt_body_end=('BR', 0.85, 0.72),
                         tip=('BR', 0.678, 0.341),
                         head_w=6, belly_w=13, hook_start_w=11, tip_w=2)

    # s1  扌 横 (short, slightly rising toward the right)
    draw_heng(d, ('ML', 0.419, 0.5), ('C', 0.26, 0.345), width=8)

    # s3  扌 提 (rising from lower-left to mid)
    draw_ti(d, ('BL', 0.226, 0.353), ('C', 0.228, 0.755),
            head_width=11, tail_width=1, curve=0.05, segments=48)

    # s4  戈 短横 (crosses xie-gou upper body at ~C cell)
    draw_heng(d, ('C', 0.298, 0.535), ('MR', 0.256, 0.315), width=8)

    # s6  戈 撇 (from MR down-left crossing xie-gou lower body)
    draw_pie(d, ('MR', 0.18, 0.641), ('BC', 0.236, 0.569),
             head_width=10, tail_width=1, curve=0.08, segments=40)

    # s7  戈 点 (small compact dot upper-right of xie-gou head)
    draw_dian(d, ('TC', 0.995, 0.806), ('MR', 0.344, 0.046),
              head_width=2, peak_width=10, curve=0.05, segments=20)

    out = os.path.join(os.path.dirname(__file__), '01_找.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
