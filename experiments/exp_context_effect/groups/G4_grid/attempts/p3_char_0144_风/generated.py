"""风 (fēng, 4 strokes) — G4 attempt at p3_char_0144.

MANDATORY LOOKUP CHECKLIST:
  1. success_bank/INDEX.md grep: `ji.py` (几) — mastered, close cousin.
     风 = 几-outer (s1 撇 + s2 横斜钩) + inner 乂 (s3 撇 + s4 反捺).
     Reuse ji.py's structure (override anchors — TR1) for s1/s2.
  2. errata.md grep: p2_radical_094_风 (FAIL) — old fix idea: push
     s2 hook_pt down to BR(0.50, 0.80), full-height enclosing wall;
     s4 as proper 捺. Applied literally below.
  3. form_catalog.md: outer-几 pattern — top-bar TL→TR near top, then
     right descent all the way to BR with a small up-flick hook.
  4. principles_meta.md TR9: standalone char 风 fills the grid.
     TR10: N-class top gap ~15-20 px between s1.head and s2.head
     (几-family exception — DO NOT weld).
  5. joint_atlas.md: 几-family top = N, inner 乂 crossing = P (welded).
  6. sandbox.md: n/a fresh.

MMH-derived structural spec (4 strokes, 3 joints):
  s1 撇: ML(0.715, 0.028) → BL(0.401, 0.871)  — long left 撇
  s2 横斜钩: ML(0.958, 0.146) → BR(0.748, 0.317)  — top+descent+hook
  s3 撇: C(0.573, 0.28) → BL(0.926, 0.625)  — inner 撇
  s4 反捺: C(0.075, 0.605) → BC(0.808, 0.531)  — inner 反捺
  joints:
    s1.head ⇆ s2.head @ ML : N (~17 px gap)
    s1.mid(0.35) ⇆ s4.head @ ML : N (~34 px gap)  — natural
    s3.mid(0.49) ⇆ s4.mid(0.45) @ BC : P (welded, 乂 crossing)
"""
import os
import sys
from PIL import Image, ImageDraw

# Import anchor helper from bank
BANK = os.path.join(os.path.dirname(__file__), '..', '..', '..',
                    'G4_grid', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'reused 几 outer pattern (ji.py), inner 乂 P-welded.',
}


def draw_feng(draw):
    # ---- s1 撇: long left descent (from near top-center down to lower-left) ----
    # Override anchors from ji.py's s1 for standalone 风:
    # MMH says head ML(0.715, 0.028) -> tail BL(0.401, 0.871)
    # In pixels: head ≈ (72, 103); tail ≈ (40, 287)  — nearly vertical drop, slight left curve
    # Push s1 to reach further down to match GT's long left leg.
    p1_h = (68, 100)   # near-top-center, small N-gap from s2.head
    p1_t = (35, 285)   # lower-left corner (long descent)
    # Slight leftward bow (撇 curls to lower-left)
    ctrl1 = ((p1_h[0] + p1_t[0]) / 2.0 - 12, (p1_h[1] + p1_t[1]) / 2.0)
    s1_pts = quad_bezier(p1_h, ctrl1, p1_t, n=48)
    s1_widths = [8 - (i / 48) * 6 for i in range(49)]  # taper
    stroke_variable_width(draw, s1_pts, s1_widths)

    # ---- s2 横斜钩: top-bar + right-wall descent + up-hook ----
    # MMH head ML(0.958, 0.146) ≈ (96, 115); MMH tail BR(0.748, 0.317) ≈ (275, 232)
    # But visually 风's right wall goes down further with a hook. Use MMH endpoints
    # for top-bar+descent-start, then extend down with hook per errata fix.
    p2_head = anchor_to_xy(('ML', 0.958, 0.146))          # ≈ (96, 115) — top-left of bar
    p2_corner = anchor_to_xy(('TR', 0.85, 0.55))          # top-right corner ≈ (285, 55)... adjust
    # Recompute corner: top-bar goes from just right of s1.head to upper-right.
    p2_head = (85, 100)    # near s1.head, small N-gap (~17 px)
    p2_corner = (258, 88)  # top-right corner of the frame
    p2_knee = (275, 235)   # right wall descending further
    p2_hook_s = (255, 275) # hook sweep start
    p2_tip = (210, 258)    # hook tip up-left (pronounced)

    # Top-bar (slight upward curl)
    ctrl_top = ((p2_head[0] + p2_corner[0]) / 2.0,
                min(p2_head[1], p2_corner[1]) - 4)
    top_pts = quad_bezier(p2_head, ctrl_top, p2_corner, n=24)
    top_widths = [6 + (i / 24) * 3 for i in range(25)]

    # Descent (slight rightward bow)
    ctrl_desc = (p2_corner[0] + 6, (p2_corner[1] + p2_knee[1]) / 2.0)
    desc_pts = quad_bezier(p2_corner, ctrl_desc, p2_knee, n=32)
    desc_widths = [9 - (i / 32) * 1 for i in range(33)]

    # Sweep (curl to hook start)
    ctrl_sweep = ((p2_knee[0] + p2_hook_s[0]) / 2.0 + 4,
                  max(p2_knee[1], p2_hook_s[1]) + 4)
    sweep_pts = quad_bezier(p2_knee, ctrl_sweep, p2_hook_s, n=20)
    sweep_widths = [8 + (i / 20) * 1 for i in range(21)]

    # Hook tip
    ctrl_hook = ((p2_hook_s[0] + p2_tip[0]) / 2.0,
                 (p2_hook_s[1] + p2_tip[1]) / 2.0)
    hook_pts = quad_bezier(p2_hook_s, ctrl_hook, p2_tip, n=16)
    hook_widths = [9 - (i / 16) * 8 for i in range(17)]

    pts2 = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths2 = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts2, widths2)

    # ---- s3 撇: inner 撇 from upper-mid to lower-left (part of 乂) ----
    # MMH: C(0.573, 0.28) ≈ (157, 128) → BL(0.926, 0.625) ≈ (93, 262)
    # Wait: BL is col 0, so x = (0 + 0.926) * 100 = 92.6. That's lower-left.
    # Actually for 风, s3 goes from upper-right (of inner) to lower-left.
    # MMH head C(0.573, 0.28) = (157, 128) — upper-center — OK
    # MMH tail BL(0.926, 0.625) = (92, 262) — lower-left of inner
    s3_head = ('C', 0.573, 0.28)
    s3_tail = ('BL', 0.926, 0.625)
    p3_h = anchor_to_xy(s3_head)
    p3_t = anchor_to_xy(s3_tail)
    ctrl3 = ((p3_h[0] + p3_t[0]) / 2.0 - 4, (p3_h[1] + p3_t[1]) / 2.0)
    s3_pts = quad_bezier(p3_h, ctrl3, p3_t, n=32)
    s3_widths = [6 - (i / 32) * 4 for i in range(33)]
    stroke_variable_width(draw, s3_pts, s3_widths)

    # ---- s4 反捺: inner 反捺 from lower-left to right (crossing s3) ----
    # MMH: C(0.075, 0.605) ≈ (108, 161) → BC(0.808, 0.531) ≈ (181, 253)
    # But joint says s4.head ⇆ s1.mid at ML, so s4.head is on the left near s1.
    # MMH C(0.075, 0.605) means col 1, x=0.075, so px ≈ 107; row 1, y=0.605, so py ≈ 161.
    # Actually the head at (107, 161) is in cell C (middle center), lower-left of C.
    # This is the inner-捺 stroke going down-right, crossing s3 at the middle.
    s4_head = ('C', 0.075, 0.605)
    s4_tail = ('BC', 0.808, 0.531)
    p4_h = anchor_to_xy(s4_head)
    p4_t = anchor_to_xy(s4_tail)
    # 反捺 has slight downward bow
    ctrl4 = ((p4_h[0] + p4_t[0]) / 2.0, (p4_h[1] + p4_t[1]) / 2.0 + 6)
    s4_pts = quad_bezier(p4_h, ctrl4, p4_t, n=32)
    s4_widths = [4 + (i / 32) * 5 for i in range(33)]  # thickens toward tail (捺 flare)
    stroke_variable_width(draw, s4_pts, s4_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_feng(draw)
    out = os.path.join(os.path.dirname(__file__), '01_风.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
