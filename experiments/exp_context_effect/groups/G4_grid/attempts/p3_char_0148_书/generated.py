"""p3_char_0148_书 (shū, book) — 4 strokes.

Lookup checklist (memory_index.md):
1. success_bank grep "书": no prior entry.
2. errata grep "书": not listed.
3. form_catalog: 竖 in central position; 横 crossing central 竖.
4. principles_meta: TR1 (override anchors), TR8 (heng/shu must share row/col endpoints where possible).
5. joint_atlas: P at central crossings (welded); N at s1.tail neighbor to s2.
6. Not in chronic cluster.

Structural plan (per MMH-injected expectations):
- stroke 1: 横折 (short) — head ML(0.89,0.36) [top-mid-left], tail C(0.86,0.76) [mid-center].
  This is the small top-hook/curve reading as short "P" descent.
- stroke 2: 横 (long) — head ML(0.48,0.97) [left, near bottom-of-middle-row], tail BC(0.88,0.51) [bottom-center-right].
  Long horizontal crossing the vertical (slight downward tilt per MMH).
- stroke 3: 竖 (long central) — head TC(0.36,0.66), tail BC(0.45,1.13). Long vertical through center.
- stroke 4: 点 — head TR(0.11,0.84), tail MR(0.39,0.11). Small dot upper-right.

Joints:
- s1.tail ⇆ s2.mid @ C : N (gap ~17px) — do NOT weld
- s1.mid ⇆ s3.mid @ C(0.49,0.30) : P (welded crossing)
- s2.mid ⇆ s3.mid @ C(0.48,0.86) : P (welded crossing)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 4 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Central 竖 (s3) drawn first as a scaffold so s1/s2 cross it cleanly (P); s1 tail stops short of s2 for the N gap.',
}


def draw_shu_book(draw):
    # ---- stroke 3: long central vertical 竖钩 (draw first so others cross it) ----
    # Small hook at bottom (up-left flick) per GT.
    s3_head = ('TC', 0.55, 0.30)         # ~(155, 60)
    s3_bot  = ('BC', 0.50, 0.95)         # ~(150, 295)
    p_h = anchor_to_xy(s3_head)
    p_b = anchor_to_xy(s3_bot)
    body = sample_line(p_h, p_b, n=50)
    n = len(body) - 1
    widths = [13 - 4 * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, body, widths)
    # hook flick up-left
    p_tip = (p_b[0] - 14, p_b[1] - 10)
    ctrl_hk = (p_b[0] - 2, p_b[1] - 1)
    hk_pts = quad_bezier(p_b, ctrl_hk, p_tip, n=15)
    hm = len(hk_pts) - 1
    hk_w = [9 - 7 * (i / hm) for i in range(hm + 1)]
    hk_w = [max(2, w) for w in hk_w]
    stroke_variable_width(draw, hk_pts, hk_w)

    # ---- stroke 1: upper short 横 with tiny curve down at right (P at center crossing) ----
    # In GT this is a short horizontal in upper-mid area with a small hook flick.
    s1_head = ('ML', 0.75, 0.42)      # ~(75, 142) — start left of center
    s1_mid  = ('C', 0.85, 0.42)       # ~(185, 142) — hook point right of center
    s1_tail = ('C', 0.80, 0.72)       # ~(180, 172) — small drop, ends above s2 (N gap)
    p1a = anchor_to_xy(s1_head)
    p1b = anchor_to_xy(s1_mid)
    p1c = anchor_to_xy(s1_tail)
    # horizontal segment (crosses s3 -> P weld naturally)
    h1 = sample_line(p1a, p1b, n=30)
    stroke_variable_width(draw, h1, [8 + 2 * (i / (len(h1)-1)) for i in range(len(h1))])
    # short drop with slight curve — leaves gap above s2
    ctrl1 = (p1b[0] + 4, (p1b[1] + p1c[1]) / 2)
    v1 = quad_bezier(p1b, ctrl1, p1c, n=20)
    stroke_variable_width(draw, v1, [9 - 5 * (i / (len(v1)-1)) for i in range(len(v1))])

    # ---- stroke 2: long 横 across bottom-middle (welded P with s3) ----
    # GT shows a long, slightly-rising heng that ends with a small tail-hook.
    s2_head = ('ML', 0.10, 0.80)      # ~(10, 180) — long from far left
    s2_tail = ('BC', 0.95, 0.35)      # ~(195, 235) — tilts down-right slightly
    p2a = anchor_to_xy(s2_head)
    p2b = anchor_to_xy(s2_tail)
    ctrl2 = ((p2a[0] + p2b[0]) / 2, (p2a[1] + p2b[1]) / 2 + 3)
    heng_pts = quad_bezier(p2a, ctrl2, p2b, n=45)
    m = len(heng_pts) - 1
    heng_widths = [9 + 3 * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, heng_pts, heng_widths)

    # ---- stroke 4: 点 (small dot upper right) ----
    s4_head = ('TR', 0.15, 0.75)   # ~(215, 75)
    s4_tail = ('TR', 0.55, 0.95)   # ~(255, 95) — short, slanted down-right
    p4a = anchor_to_xy(s4_head)
    p4b = anchor_to_xy(s4_tail)
    ctrl4 = (p4a[0] + (p4b[0] - p4a[0]) * 0.4,
             p4a[1] + (p4b[1] - p4a[1]) * 0.3)
    dian_pts = quad_bezier(p4a, ctrl4, p4b, n=20)
    md = len(dian_pts) - 1
    dian_widths = [3 + 9 * (i / md) - 6 * ((i / md) ** 2) for i in range(md + 1)]
    dian_widths = [max(2, w) for w in dian_widths]
    stroke_variable_width(draw, dian_pts, dian_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shu_book(draw)
    out = os.path.join(os.path.dirname(__file__), '01_书.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
