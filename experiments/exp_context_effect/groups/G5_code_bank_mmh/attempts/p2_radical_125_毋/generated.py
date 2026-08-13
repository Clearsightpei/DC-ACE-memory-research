"""p2_radical_125_毋 — 4-stroke radical.

MMH endpoints (canvas 300x300, 米字格 3x3 cells of 100 px):
  s1: TL(91,83)  -> BR(252,239)   compound  (LEFT-vertical + BOTTOM + up-right tail)
  s2: TC(106,89) -> BC(133,277)   横折钩    (TOP + RIGHT + hook back-left)
  s3: C(138,110) -> BL(66,282)    long 撇
  s4: ML(22,165) -> MR(270,155)   middle 横

Joint targets (from MMH):
  s1.mid(0.25) ⇆ s4.mid(0.28) @ (~91,162)   P
  s1.mid(0.61) ⇆ s3.mid(0.58) @ (~126,222)  P
  s1.mid(0.81) ⇆ s2.mid(0.68) @ (~191,222)  P
  s2.mid(0.48) ⇆ s4.mid(0.71) @ (~198,158)  P
  s3.mid(0.25) ⇆ s4.mid(0.49) @ (~144,160)  P
  s2.head ⇆ s3.head @ C                      N (natural gap ~33 px)

BANK_DEVIATION
  skipped: (no whole-radical primitive for 毋 exists)
  reason: 毋's s1 is an unusual left-down+bottom-across compound that no
          promoted stroke primitive covers; s2's 横折钩 has a very tall
          right-side and small hook, better inlined than parameterized
          via heng_zhe_gou.
  fresh_component: mu_frame (inline 4-stroke composition; not proposed
          for promotion — 毋 is a low-frequency radical, better let
          curator decide post-judgment).
"""

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revision 1: added explicit top-horizontal segment to s2 so top-of-box reads clearly; kept head/tail exactly at MMH anchors.'
}


def draw_polyline(draw, pts, width_fn, samples_per_seg=45):
    """Chain-of-ellipses along a linear polyline through pts.
    width_fn(global_t)->width where global_t in [0,1]."""
    total_segs = len(pts) - 1
    total = total_segs * samples_per_seg
    idx = 0
    for si in range(total_segs):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        for i in range(samples_per_seg):
            t = i / (samples_per_seg - 1) if samples_per_seg > 1 else 0
            bx = x0 + (x1 - x0) * t
            by = y0 + (y1 - y0) * t
            gt = idx / (total - 1) if total > 1 else 0
            w = width_fn(gt)
            draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
            idx += 1


def draw_heng(draw, head, tail, width=8):
    x0, y0 = head
    x1, y1 = tail
    steps = 120
    for i in range(steps):
        t = i / (steps - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        # very slight taper at both ends
        w = width - 1.5 * abs(2 * t - 1)
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def draw_pie(draw, pts, width_start=8, width_end=2):
    draw_polyline(draw, pts,
                  lambda gt: width_start + (width_end - width_start) * gt,
                  samples_per_seg=50)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- Stroke 1: LEFT vertical + BOTTOM horizontal + short up-right tail ---
    # Head at MMH TL(91,83), tail at MMH BR(252,239).
    # Interior path shaped so the character reads as a clear box on left+bottom.
    s1_pts = [
        (91, 83),     # head — top of left side
        (88, 165),    # left-vertical passes through s4 pierce anchor (~91,162)
        (110, 225),   # curve into bottom
        (200, 225),   # across bottom
        (252, 239),   # tail — bottom-right tail up a bit
    ]
    draw_polyline(d, s1_pts, lambda gt: 8.0, samples_per_seg=50)

    # --- Stroke 2: 横折钩 — top horizontal + right vertical + hook back-left ---
    # Head at MMH TC(106,89), tail at MMH BC(133,277).
    # Add a visible corner so top reads as a flat horizontal (calligraphic norm).
    s2_pts = [
        (106, 89),    # head — top of horizontal
        (215, 92),    # top-right corner (explicit — MMH median is slanted here)
        (210, 160),   # right vertical passes near s4 pierce (~198,158)
        (203, 225),   # continue right vertical
        (133, 277),   # tail — hook curls back-left
    ]
    draw_polyline(d, s2_pts, lambda gt: 8.0 - 3.5 * gt, samples_per_seg=45)

    # --- Stroke 3: long 撇 down-left from upper-center to BL ---
    # Head at MMH C(138,110), tail at MMH BL(66,282).
    s3_pts = [
        (138, 110),
        (143, 158),   # passes s4 pierce (~144,160)
        (126, 222),   # matches MMH mid at 58%
        (66, 282),
    ]
    draw_pie(d, s3_pts, width_start=8, width_end=3)

    # --- Stroke 4: middle 横 (long) ---
    draw_heng(d, (22, 165), (270, 155), width=8)

    out = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_125_毋/01_毋.png'
    img.save(out)
    print('Rendered 4-stroke 毋 to', out)


if __name__ == '__main__':
    main()
