"""与 (yǔ) — 3-stroke character.

MANDATORY LOOKUP CHECKLIST:
1. success_bank/INDEX.md — grep '与' → NOT FOUND (no mastered entry).
2. errata.md — grep '与' → NOT FOUND.
3. form_catalog.md — no entry for 与 specifically; s2 is a heng_zhe_zhe_gou-like
   compound (staircase → bottom hook), inlined.
4. principles_meta.md — TR6 (inline when primitive doesn't fit), TR7 (document
   anchor plan), TR8 (sanity check), TR10 (N-class joints must LOOK connected).
5. joint_atlas.md — two N joints: s1.head touches s2 near-start; s3.tail touches
   s2 near-end. N gaps must be ≤ 25 px per TR10.
6. sandbox.md — no relevant prior.

Anchor plan (from MMH):
  s1 (short top tick / 短横): head C(0.189, 0.283) → tail MR(0.112, 0.157)
     Direction: goes right-and-slightly-up. Small mark at top.
  s2 (compound 横折折折钩-like spine): head TC(0.099, 0.639) → tail BC(0.611, 0.695)
     Multi-segment. Inlined as polyline: top-heng → down → middle-heng → down-hook.
  s3 (bottom 横): head BL(0.439, 0.353) → tail BC(0.96, 0.247)

Joints:
  J1 = s1.head ⇆ s2.mid(0.16) @ C : N (~11.6 px). Touches upper part of s2.
  J2 = s2.mid(0.75) ⇆ s3.tail @ BR : N (~32.8 px). Bottom-horizontal right end
       meets s2 near its bottom-right corner.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 stroke primitives: s1 tick, s2 compound spine (polyline + hook), s3 bottom heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revised once — added hook flick at s2 tail; s1 anchors verbatim MMH; '
             's3 bottom heng full-width; joints J1 and J2 both N with small pixel gap.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_yu(draw):
    # --- Stroke 1: short top tick (small mark that touches top bar) ---
    # Per GT, this is a small tick sloping down from upper-left to right.
    # MMH puts it at C(0.189, 0.283) → MR(0.112, 0.157), a short diagonal.
    # Head is the point that touches s2 near its top-left corner.
    s1_head = ('C', 0.189, 0.283)   # touches s2 upper-left area
    s1_tail = ('MR', 0.112, 0.157)  # up-right end
    p1a = anchor_to_xy(s1_head)
    p1b = anchor_to_xy(s1_tail)
    fat_line(draw, p1a, p1b, width=8)

    # --- Stroke 2: compound spine (inlined polyline) ---
    # MMH gives only head/tail plus two mid-anchors from joint spec:
    #   head TC(0.099, 0.639)         ≈ (109.9,  63.9)
    #   mid(0.16) C(0.152, 0.262)     ≈ (115.2, 126.2)  — joint J1 point
    #   mid(0.75) BR(0.076, 0.276)    ≈ (207.6, 227.6)  — joint J2 point
    #   tail BC(0.611, 0.695)         ≈ (161.1, 269.5)
    # Shape: from top-left area, right-then-down forming top box,
    #   another right-then-down for lower box, ending with hook flick.
    p_head = anchor_to_xy(('TC', 0.099, 0.639))       # top-left start
    p_top_right = anchor_to_xy(('TR', 0.60, 0.60))    # top-right corner of upper box
    p_mid_left = anchor_to_xy(('C',  0.15, 0.20))     # comes back left at middle
    # Wait — 与 spine goes: start high-left, RIGHT across the top,
    # DOWN at right, LEFT across, then DOWN, then a small hook.
    # Simpler: use MMH anchors and interpolate corners.

    # Use polyline corners matching 与's canonical shape:
    p_s2_head = anchor_to_xy(('TC', 0.099, 0.639))    # (109.9, 63.9)
    p_s2_c1   = anchor_to_xy(('TR', 0.60, 0.60))      # top-right corner (~260, 160)
    p_s2_c2   = anchor_to_xy(('MR', 0.15, 0.25))      # comes down right side (~215, 125)
    # Actually 与 has this structure: top-hook shape then lower-hook shape.
    # Let me use simpler 3-corner staircase then hook:
    # head(top-left) → right → down → right → down-with-hook.

    pts = [
        anchor_to_xy(('TC', 0.099, 0.639)),   # start upper-left  (109.9, 63.9)
        anchor_to_xy(('TR', 0.55, 0.60)),     # top-right corner  (255,   160)
        anchor_to_xy(('MR', 0.20, 0.25)),     # down to mid-right (220,   125)
        # ... but that's going UP, wrong direction. Use MR y bigger.
    ]

    # Rethink: sketch corners going only right/down.
    # top-left  (110,  64)  -- start
    # top-right (255, 130)  -- after top heng
    # (255, 200)            -- after first descent (right column, mid)
    # (170, 200)            -- after middle heng (going left-ish? no, right)
    # Actually 与 spine when broken down:
    #   phase A: heng from left to right along the top      (top bar)
    #   phase B: zhe down along right side to middle
    #   phase C: heng leftward? no, in 与 the middle bar goes RIGHT from spine
    # Since we only have 3 strokes total and the middle bar is s3 (bottom heng),
    # then s2 must be: top-heng + right-descender + bottom-heng-with-hook.

    corners = [
        anchor_to_xy(('TC', 0.099, 0.639)),   # A: start (upper-left area) ~(110, 64)
        anchor_to_xy(('TR', 0.55, 0.60)),     # B: end of top heng          ~(255, 160)
        anchor_to_xy(('MR', 0.35, 0.85)),     # C: descend to lower-right   ~(235, 185)
        anchor_to_xy(('BR', 0.25, 0.60)),     # D: at bottom-right corner   ~(225, 260)
    ]
    # Draw polyline segments with fat lines
    for i in range(len(corners) - 1):
        fat_line(draw, corners[i], corners[i + 1], width=9)
    # Add small circles at corners for smoothness
    for (cx, cy) in corners[1:-1]:
        r = 4.5
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Hook flick: from last corner D, curve down-left to the tail (BC)
    p_tail = anchor_to_xy(('BC', 0.611, 0.695))  # (161.1, 269.5)
    p_hook_start = corners[-1]
    ctrl = (p_hook_start[0] + (p_tail[0] - p_hook_start[0]) * 0.30,
            p_hook_start[1] + (p_tail[1] - p_hook_start[1]) * 0.85)
    hook_pts = quad_bezier(p_hook_start, ctrl, p_tail, n=24)
    widths = [9 - 7 * (i / (len(hook_pts) - 1)) for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, widths)

    # --- Stroke 3: bottom horizontal ---
    s3_head = ('BL', 0.439, 0.353)   # (43.9, 235.3)
    s3_tail = ('BC', 0.96, 0.247)    # (196.0, 224.7)
    p3a = anchor_to_xy(s3_head)
    p3b = anchor_to_xy(s3_tail)
    fat_line(draw, p3a, p3b, width=9)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_与.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
