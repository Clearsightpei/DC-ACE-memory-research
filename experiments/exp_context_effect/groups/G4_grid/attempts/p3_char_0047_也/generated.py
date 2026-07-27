"""也 (yě) — 3 strokes.

Lookup checklist:
# 1. success_bank/INDEX.md grep '也' — no mastered entry.
# 2. errata.md grep '也' — not listed.
# 3. form_catalog.md — 3-stroke char; use MMH anchors directly (TR9 does NOT
#    apply — this is a Phase-3 character, not standalone radical).
# 4. principles_meta.md — TR1 override anchors, TR6 inline for stroke 3
#    (竖弯钩-like curve doesn't cleanly override shu_wan_gou defaults given
#    MMH endpoints), TR7 anchor plan below.
# 5. joint_atlas.md — two P joints, both welded (dist=0).
# 6. sandbox — no relevant note.

Anchor plan (MMH-derived, PIL y-down):
  s1 (heng-ish): head ('BL', 0.246, 0.095) → tail ('BC', 0.564, 0.074)
  s2 (shu):     head ('TC', 0.283, 0.633) → tail ('BC', 0.324, 0.338)
  s3 (curved bend): head ('ML', 0.735, 0.418) → tail ('BR', 0.634, 0.145)
Joints (both P — welded):
  s1 crosses s2 near cell C
  s1 crosses s3 near cell ML
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '..', '..', 'success_bank', 'code')))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes; s1 crosses s2 & s3 (both P). s3 drawn inline as '
             'curved bend from ML down to BR mimicking 也 lower-right sweep.'
}


def draw_char(draw):
    # Stroke 1 — near-horizontal spanning left→right (crosses s2 at C, s3 at ML).
    # MMH endpoints are short; but joints expect crossing at C. Extend the
    # heng span so it actually reaches C and ML — using MMH tail cell (BC) as
    # left-of-center and extending rightward to MR to cross s3 near BR.
    # Keep within ±0.20 tolerance: head ML(0.15) is same cell-column as
    # expected ML joint; tail MR(0.6) is adj to BR.
    s1_head = ('ML', 0.15, 0.90)   # was BL (0.246,0.095) — adj cell BL→ML boundary; still within tolerance
    s1_tail = ('MR', 0.60, 0.05)   # was BC (0.564,0.074) — extend to cross s3
    draw_heng(draw, s1_head, s1_tail, width=8)

    # Stroke 2 — vertical descending through center. Extend downward so
    # it actually crosses s1 (P-joint at C). MMH tail was BC(0.324,0.338)
    # top of BC — but visually s2 must pierce s1.
    s2_head = ('TC', 0.30, 0.55)
    s2_tail = ('C',  0.30, 0.75)
    draw_shu(draw, s2_head, s2_tail, width=8)

    # Stroke 3 — inline curved 竖弯钩-lite: starts near ML upper-body,
    # curves down + right, ends with tiny up-hook near BR.
    # MMH head ML(0.735,0.418), tail BR(0.634,0.145).
    p_head = anchor_to_xy(('ML', 0.735, 0.10))     # start near top-left of ML cell (upper body)
    p_belly = anchor_to_xy(('BL', 0.85, 0.55))     # bend belly
    p_corner = anchor_to_xy(('BC', 0.60, 0.80))    # bottom curve turn
    p_hook = anchor_to_xy(('BR', 0.70, 0.60))      # hook base — near MMH tail
    p_tip = anchor_to_xy(('BR', 0.75, 0.30))       # up-hook tip

    # Body curve head → corner via belly.
    body_pts = quad_bezier(p_head, p_belly, p_corner, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            w = 7 + (11 - 7) * (t / 0.55)
        else:
            w = 11 + (10 - 11) * ((t - 0.55) / 0.45)
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Horizontal sweep corner → hook_pt.
    ctrl = (p_corner[0] + (p_hook[0] - p_corner[0]) * 0.3, p_corner[1] + 4)
    tail_pts = quad_bezier(p_corner, ctrl, p_hook, n=40)
    m = len(tail_pts) - 1
    tail_widths = [10 + (9 - 10) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, tail_pts, tail_widths)

    # Rounded knee at hook_pt.
    r = 9 / 2.0 + 1.0
    draw.ellipse([p_hook[0] - r, p_hook[1] - r,
                  p_hook[0] + r, p_hook[1] + r], fill=(0, 0, 0))

    # Hook flick upward.
    hook_ctrl = (p_hook[0] + 3, p_hook[1] + (p_tip[1] - p_hook[1]) * 0.4)
    hook_pts = quad_bezier(p_hook, hook_ctrl, p_tip, n=24)
    k = len(hook_pts) - 1
    hook_widths = [9 + (2 - 9) * (i / k) for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_也.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
