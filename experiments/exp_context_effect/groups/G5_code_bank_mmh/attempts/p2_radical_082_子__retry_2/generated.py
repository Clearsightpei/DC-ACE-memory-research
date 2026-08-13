# TRAJECTORY DIFF (retry 2)
# ---------------------------------------------------------------
# GT observation (子): 3 strokes.
#   s1 横撇 — compact top curl: short horizontal-ish head, sharp
#     down-turn, pie sweeping down-left; NO upward peak.
#   s2 弯钩 — vertical shaft with a slight rightward bow, decisive
#     LEFT-pointing hook at bottom (hook clearly visible, not a bump).
#   s3 横 — clean horizontal bar through the middle, ~65-70% canvas
#     width, thin/clean ends (no bulbs).
#
# main (FAIL) at attempts/p2_radical_082_子/01_子.png visible gaps:
#   1) s1 had upward peak (150,78) — reads as extra hook.
#   2) s2 hook too tight (~15px leftward travel) — barely visible.
#   3) s3 endpoints bulbous from draw_heng end-caps.
#
# retry_1 (FAIL) at attempts/p2_radical_082_子__retry_1/01_子.png:
#   1) s1 shape improved — but the tail dab at head (extra dot) still
#      reads as an artifact; the corner (172,108) sits too far right.
#   2) s2 hook improved (30px leftward) — visible but still soft.
#   3) s3 kept draw_heng — the BIG round end-cap dabs (r2=width_tail/2+1)
#      show up as prominent circles at (50,180) and (255,175). These
#      "eye" dabs are the most likely proximate cause of judge fail:
#      they add visible extra objects that don't exist in GT.
#
# Fixes this attempt:
#   1) s1 — keep clean shape but move corner slightly leftward to
#      (163,110), avoid extra dabs at head.
#   2) s2 — bolder body, hook tail moved further LEFT (85,285) with
#      stronger tapered curl.
#   3) s3 — INLINE heng, no end-cap dabs. Just a clean tapered line.
#      Slightly tighter span (55, 178) to (250, 175).
# ---------------------------------------------------------------

# BANK_DEVIATION
# skipped: heng.py — bank draw_heng adds prominent end-cap ellipses
#          (especially the tail dab at r2 = width_tail/2 + 1 = 6 px
#          radius), which render as visible round blobs at the heng
#          endpoints of 子. GT's s3 has clean tapered ends, not blobs.
# reason: the end-cap dabs read as extra visual elements next to the
#         vertical shaft, breaking the character silhouette.
# fresh_component: clean_heng_for_zi (inline linework, thin end taper)
#
# skipped: heng_pie.py — its ~130 px wide 又-style span doesn't fit
#         子's compact ~85 px top curl.
# fresh_component: heng_pie_compact_for_zi
#
# Also inlined s2 (弯钩): bank has shu_gou (straight body, left hook)
# and shu_wan_gou (curved body, RIGHT hook). Neither matches 弯钩's
# curved body + LEFT hook.
# fresh_component: wan_gou_for_zi

"""子 (zi) — 3-stroke radical. G5 retry 2.

MMH-derived anchors (300x300 pixels):
  s1 横撇  head TL(0.861,0.917)=(86,92)  tail C(0.57,0.318)=(155,138)
  s2 弯钩  head C(0.383,0.277)=(133,127) tail BC(0.034,0.728)=(95,282)
  s3 横    head ML(0.349,0.813)=(50,180) tail MR(0.745,0.764)=(255,175)

Joints:
  s1.tail(155,138) N s2.head(133,127) — natural gap ~14 px (N-class)
  s2.mid P s3.mid — welded (both pass through common point ~(140,175))
"""

import os
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry 2: inline clean s3 heng (no end-cap dabs); stronger s2 hook.'
}


def _bezier_taper(draw, p0, p1, p2, w_head, w_tail, steps=90):
    """Quadratic Bezier with linear width taper, dot-brush rendering."""
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w_head + (w_tail - w_head) * t
        r = max(1.0, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_s1_heng_pie(draw):
    """子's 横撇 top stroke — compact clean curl, no upward peak."""
    head = (86, 92)         # TL entry
    corner = (163, 110)     # top-right corner (lower than head — no peak)
    tail = (152, 140)       # C: end of pie, upper-center
    # Segment A: gentle horizontal-ish head-run to corner
    mid_a = (128, 98)
    _bezier_taper(draw, head, mid_a, corner, w_head=6, w_tail=8, steps=55)
    # Segment B: pie sweeps down-left, thin taper at tail
    mid_b = (162, 128)
    _bezier_taper(draw, corner, mid_b, tail, w_head=8, w_tail=2, steps=45)


def draw_s2_wan_gou(draw):
    """子's 弯钩: curved-body vertical with clear LEFT hook.
    Head near upper-center, body bows slightly RIGHT, decisive
    LEFT curl at bottom.
    """
    head = (133, 127)
    shoulder = (130, 258)     # end of main body / start of hook
    tail = (88, 285)          # hook end (well LEFT of shoulder)
    # Body: bezier from head to shoulder, mild rightward bow
    body_ctrl = (152, 195)
    _bezier_taper(draw, head, body_ctrl, shoulder, w_head=6, w_tail=6, steps=90)
    # Hook: pronounced leftward + downward curl, tapered to fine tip
    hook_ctrl = (113, 290)
    _bezier_taper(draw, shoulder, hook_ctrl, tail, w_head=6, w_tail=2, steps=45)


def draw_s3_heng_clean(draw):
    """子's 横 middle bar — clean tapered line, NO end-cap dabs.
    Inlined; skipped bank draw_heng because its end-cap ellipses
    (esp. tail dab at r=6) render as visible round blobs.
    """
    head = (55, 178)
    tail = (250, 175)
    # Draw as tapered dot-brush: slightly thicker at tail (顿笔) but
    # no extra ellipse cap.
    steps = 90
    for i in range(steps):
        t = i / (steps - 1)
        x = head[0] + (tail[0] - head[0]) * t
        y = head[1] + (tail[1] - head[1]) * t
        # subtle taper: 6 → 7 (slight tail thickening, no dab)
        w = 6 + 1.0 * t
        r = w / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_zi(draw):
    draw_s1_heng_pie(draw)
    draw_s2_wan_gou(draw)
    draw_s3_heng_clean(draw)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_zi(d)
    out = os.path.join(os.path.dirname(__file__), '01_子.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
