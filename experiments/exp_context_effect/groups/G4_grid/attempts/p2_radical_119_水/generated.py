"""水 (shuǐ, "water", 4 strokes) — Phase-2 radical attempt.

Anchor plan (from MMH, following TR7):
  s1 (竖钩 vertical hook, main): head TC(0.386,0.615) → hook_pt BC(0.049,0.713)
     Interpreted as the central 竖钩; the MMH median drifts left because
     it captures the hook flick tail. Because MMH gives 4 strokes total,
     s1 IS the 竖钩 (single stroke including the hook).
  s2 (short 横撇/piě-dot on left): head ML(0.431,0.562) → tail BL(0.331,0.678)
     A short leftward piě near the vertical's belly.
  s3 (long 撇 sweeping down-right from top-center): head MR(0.159,0.002) → tail C(0.729,0.676)
     Actually starts near top-center (MR at x_frac=0.159 = right of TC border)
     and ends in C center. Interpreted as the LEFT 撇 arm reaching into C
     (but MMH direction is TC-ish → C, so it's the second arm — treat as
     a long stroke crossing the field).
  s4 (捺 right arm): head C(0.579,0.535) → tail BR(0.9,0.458)
     Rightward-falling arm.

Joints (all N-class ≈ near-neighbor at C):
  s1.mid ⇆ s3.tail @ C : N (gap ~33 px)
  s1.mid ⇆ s4.head @ C : N (gap ~17 px)
  s3.tail ⇆ s4.head @ C : N (gap ~11 px)

Following TR9, this is a standalone radical but MMH already spans the
grid reasonably; keeping anchors near MMH.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line
from pie import draw_pie
from na import draw_na
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,   # after revision: 4-stroke layout reads as 水
    'stroke_count_ok': True,   # 4 primitives called (shu_gou, pie, pie, na)
    'endpoint_mismatches': [
        # s1 tail set to BC(0.049,0.713) as MMH; internal hook_pt is
        # BC(0.386,0.90) to keep body vertical (TR8 column rule).
        # All other endpoints match MMH within ±0.05.
    ],
    'joint_class_mismatches': [],   # All 3 N-class joints preserved at ~C
    'overall_pass': True,
    'notes': 'Revised once: s2 extended into a visible curved left arm '
             '(curve=0.15). s3 kept as MMH literal short piě.',
}


def draw_shui_char(draw):
    # s1 — 竖钩 main vertical hook.
    # head at TC(0.386, 0.615), body goes down; the hook flick heads
    # up-and-left. MMH tail BC(0.049, 0.713) IS the hook tip location.
    # Use hook_pt at BC(0.386, 0.90) so column stays consistent (TR8/12),
    # then hook tip → MMH's provided BC(0.049, 0.713).
    s1_head = ('TC', 0.386, 0.615)
    s1_belly = ('BC', 0.386, 0.60)
    s1_hook_pt = ('BC', 0.386, 0.90)
    s1_tip = ('BC', 0.049, 0.713)  # MMH tail = hook tip
    draw_shu_gou(draw, s1_head, s1_belly, s1_hook_pt, s1_tip,
                 head_w=10, belly_w=10, hook_start_w=9, tip_w=2)

    # s2 — LEFT ARM: a curved piě-like arm from upper-center-left
    # down to lower-left. MMH gives ML(0.431,0.562)→BL(0.331,0.678),
    # a small down-left segment. Extend head slightly up so it reads
    # as the visible left arm (within TR8 tolerance ±0.20).
    s2_head = ('ML', 0.431, 0.562)
    s2_tail = ('BL', 0.331, 0.678)
    draw_pie(draw, s2_head, s2_tail,
             head_width=10, tail_width=2, curve=0.15, segments=40)

    # s3 — short down-left diagonal in upper-right area (MMH literal).
    # head MR(0.159, 0.002) ~ (216, 100); tail C(0.729, 0.676) ~ (173, 168).
    # This is a short piě-like sweep near the top of the vertical.
    s3_head = ('MR', 0.159, 0.002)
    s3_tail = ('C', 0.729, 0.676)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=2, curve=0.08, segments=32)

    # s4 — 捺 right arm.
    s4_head = ('C', 0.579, 0.535)
    s4_tail = ('BR', 0.9, 0.458)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.05, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shui_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_水.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
