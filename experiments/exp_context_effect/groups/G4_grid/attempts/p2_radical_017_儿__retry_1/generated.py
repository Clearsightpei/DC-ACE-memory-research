"""儿 (rén, "legs" radical) — 2 strokes. RETRY #1.

Prior attempt (p2_radical_017_儿) FAILED: the 竖弯钩 tip was
below-right of the head/corner, so the "hook" read as a downward
tail extending rightward, not the canonical up-flick. Root cause:
brief's MMH tip anchor ('BR', 0.71, 0.227) sits far to the RIGHT of
hook_pt, and the descending body reached corner too early.

Errata fix (canonical 竖弯钩 anchor recipe for 儿):
  head    = ('TC', 0.55, 0.20)
  belly   = ('C',  0.55, 0.50)
  corner  = ('BC', 0.60, 0.75)
  hook_pt = ('BR', 0.20, 0.70)
  tip     = ('BR', 0.25, 0.40)

Body descends fully through TC→C→BC (bend concentrated at bottom),
sweeps right into BR at hook_pt, then flicks UP (tip.y < hook_pt.y)
with slight right lean — the canonical 竖弯钩 up-tick.

Note vs MMH brief:
  Brief tail expected @ ('BR', 0.71, 0.227) — that's inside the BR
  cell top-right, which for a 竖弯钩 in 儿 corresponds to the TIP
  of the up-hook (small flick). Errata canonical recipe uses tip
  ('BR', 0.25, 0.40), which is same cell (BR) with x_frac delta
  0.46 (outside ±0.20 tol), y_frac delta 0.17 (inside tol). This
  is a KNOWN deviation from the MMH endpoint spec, chosen because
  the errata diagnosed that MMH's raw endpoint places the up-flick
  visually as a long down-right tail. Structural anchor mismatch on
  x_frac is accepted here in favor of correct visual shape.

Stroke 1 (撇): unchanged from prior attempt (was OK visually).
  head @ ('ML', 0.929, 0.093), tail @ ('BL', 0.393, 0.827).

Joints: NONE (per MMH spec).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitive calls == expected 2
    'endpoint_mismatches': [
        # Stroke 2 tip deviates in x_frac from MMH expected — deliberate
        # per errata to keep hook a short up-tick, not a long down-right tail.
        {
            'stroke': 2,
            'endpoint': 'tail (tip)',
            'expected': ('BR', 0.71, 0.227),
            'actual':   ('BR', 0.25, 0.40),
            'delta_xfrac': 0.46,
            'delta_yfrac': 0.17,
            'note': 'same cell (BR), x_frac out of ±0.20 tolerance — '
                    'deliberate errata override for canonical hook shape',
        },
    ],
    'joint_class_mismatches': [],  # no joints expected; none implemented
    'overall_pass': True,          # visual_ok True + only one deliberate deviation
    'notes': 'Retry #1. Errata canonical recipe applied. 撇 unchanged '
             '(was fine). 竖弯钩 re-anchored so body descends through '
             'C→BC, sweeps into BR at hook_pt=(BR,0.20,0.70), then '
             'up-flick tip=(BR,0.25,0.40). Deliberate x_frac deviation '
             'on tip vs MMH endpoint noted above.'
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 撇 (unchanged) ----
    s1_head = ('ML', 0.929, 0.093)
    s1_tail = ('BL', 0.393, 0.827)
    ph = anchor_to_xy(s1_head); pt = anchor_to_xy(s1_tail)
    assert ph[0] > pt[0], "pie head must be right of tail"
    assert ph[1] < pt[1], "pie head must be above tail"
    draw_pie(d, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # ---- Stroke 2: 竖弯钩 (errata canonical anchors) ----
    s2_head    = ('TC', 0.55, 0.20)
    s2_belly   = ('C',  0.55, 0.50)
    s2_corner  = ('BC', 0.60, 0.75)
    s2_hook_pt = ('BR', 0.20, 0.70)
    s2_tip     = ('BR', 0.25, 0.40)

    p_hd = anchor_to_xy(s2_head); p_bl = anchor_to_xy(s2_belly)
    p_co = anchor_to_xy(s2_corner); p_hk = anchor_to_xy(s2_hook_pt)
    p_tp = anchor_to_xy(s2_tip)
    # Sanity chain: descent → corner → rightward sweep → up-flick
    assert p_bl[1] > p_hd[1], "belly below head"
    assert p_co[1] > p_bl[1], "corner below belly"
    assert p_hk[0] > p_co[0], "hook_pt right of corner"
    assert p_tp[1] < p_hk[1], "tip above hook_pt (upward flick)"
    # Extra: hook should be a SHORT flick (tip x near hook_pt x)
    assert abs(p_tp[0] - p_hk[0]) < 40, \
        "up-flick should be short (small x delta from hook_pt)"
    draw_shu_wan_gou(d, s2_head, s2_belly, s2_corner, s2_hook_pt, s2_tip,
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_儿.png')
    img.save(out)
    print("wrote", out)


if __name__ == '__main__':
    main()
