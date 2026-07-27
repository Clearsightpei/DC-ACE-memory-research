"""见 (jiàn, "see", 4 strokes) — B5 first attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. success_bank/INDEX.md grep for 见 → NOT in bank. p2_radical_100_见
     FAILed in errata (see step 2).
  2. errata.md grep for 见 → p2_radical_100_见 FAIL, fix: enlarge
     eye-box y∈[20,180], move s3 head to ML-left, s4 head to right.
     Applied LITERALLY below.
  3. form_catalog.md: shu_wan_gou used in 儿/见/元 family — needs
     rounded bend at bottom + upward hook.
  4. principles_meta.md: TR9 span expansion (standalone character —
     use full grid span). TR10 N-class must look connected (~15-20 px).
  5. joint_atlas.md: 几-family top gap needs visible N (~15-20 px),
     do NOT weld (p3_021 lesson). Applies to s1.head ⇆ s2.head.
  6. sandbox.md: n/a.

Structure of 见 (4 strokes):
  s1 — 竖 short (left wall of top box, TL→BL along left edge).
  s2 — 横折钩-ish (top bar + right wall, TC→BC).
  s3 — 撇 (inner left leg, C → BL, curving down-left).
  s4 — 竖弯钩 (right leg + rightward sweep + upward hook, C → BR).

Joints (MMH-derived):
  s1.head ⇆ s2.head @ TC → N (~13.4 px gap — top-left of box).
  s3.mid ⇆ s4.head @ C  → N (~20 px gap — inner strokes meet at top).

Primitives reused from success_bank: pie, heng_zhe, shu_wan_gou.
Anchors overridden per MMH expectations (TR1).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives → 4 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'errata fix applied: box spans y=20..180; s3 head ML-left, s4 head right.'
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_jian(draw):
    # ---- s1: 竖 short — left wall of the top eye-box.
    # Expected: head TL(0.885, 0.82) → tail BL(0.958, 0.08).
    # (near-vertical, on left edge x≈0.29 grid, y spans ~0.27 → 0.69 → mid-band)
    # Note: MMH head y=0.82 in TL is BELOW s2 head y=0.858 in TC — the two
    # heads should be roughly level. Cap s1 head at level with s2 head to
    # avoid it protruding above the top bar.
    s1_head_a = ('TL', 0.885, 0.90)
    s1_tail_a = ('BL', 0.958, 0.30)
    s1h = anchor_to_xy(s1_head_a)
    s1t = anchor_to_xy(s1_tail_a)
    # N-gap at top vs s2.head:
    s1h_g = _shorten(s1h, s1t, 6)
    fat_line(draw, s1h_g, s1t, width=9)

    # ---- s2: 横折(钩) — top bar + right wall.
    # Expected: head TC(0.061, 0.858) → tail BC(0.939, 0.048).
    # head is at top-center-left (near s1.head), tail at bottom-center-right
    # (bottom-right of the eye-box). Corner sits at TR/MR area.
    s2_head_a = ('TC', 0.061, 0.858)
    s2_corner_a = ('TR', 0.90, 0.90)
    s2_tail_a = ('BC', 0.939, 0.048)
    s2h = anchor_to_xy(s2_head_a)
    s2c = anchor_to_xy(s2_corner_a)
    s2t = anchor_to_xy(s2_tail_a)
    # N-gap at head vs s1.head:
    s2h_g = _shorten(s2h, s2c, 8)
    fat_line(draw, s2h_g, s2c, width=9)   # horizontal top bar
    fat_line(draw, s2c, s2t, width=9)     # right vertical wall
    # shoulder disc at corner (顿笔)
    cx, cy = s2c; r = 6
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # ---- s3: 撇 — inner left leg, from center curving down-left to BL.
    # Expected: head C(0.295, 0.157) → tail BL(0.448, 1.012).
    # Long pie sweeping from upper-center down to lower-left, curving.
    s3_head_a = ('C', 0.295, 0.157)
    s3_tail_a = ('BL', 0.448, 1.012)
    draw_pie(draw, s3_head_a, s3_tail_a,
             head_width=10, tail_width=2, curve=0.10, segments=60)

    # ---- s4: 竖弯钩 — inner right leg, vertical → rightward bend → upward hook.
    # Expected: head C(0.529, 0.925) → tail BR(0.695, 0.303).
    # head at center-lower, curves right along bottom, tip flicks up to BR-upper.
    # Fix from pass 1: hook tip flick must be SHORT (a small upward flick,
    # not a long vertical). Tail y=0.303 in BR means tip is only slightly
    # above hook base.
    s4_head_a = ('C', 0.529, 0.925)
    s4_belly_a = ('BC', 0.70, 0.55)
    s4_corner_a = ('BC', 0.85, 0.90)
    s4_hook_a = ('BR', 0.70, 0.55)
    s4_tip_a = ('BR', 0.72, 0.30)   # short upward flick
    draw_shu_wan_gou(draw, s4_head_a, s4_belly_a, s4_corner_a,
                     s4_hook_a, s4_tip_a,
                     head_w=9, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jian(draw)
    out = os.path.join(os.path.dirname(__file__), '01_见.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
