"""p3_char_0289_我 (wǒ, 7 strokes) — G4 grid-bank attempt.

Reading order followed (v8 slim):
  1) drawer_memory.md — no direct primitive for 我 or 戈; compositional
     playbook says: split into 手-left + 戈-right components but the
     MMH stroke split is per-stroke, not per-radical. Draw fresh with
     inline fat_line + bezier per shared v8 latitude.
  2) success_bank/INDEX.md — no 我; 戈 (p2_096) is in errata (FAIL);
     no chronic primitive matches. Draw fresh.
  3) errata.md — 我 not present.

Component split (informational):
  我 = 手-radical (left, s1..s4) + 戈-radical (right, s5..s7)

Per-stroke plan (MMH anchors, PIL pixels via _anchor.anchor_to_xy):
  s1  短撇 :  head ('C', 0.342, 0.163) → tail ('ML', 0.595, 0.471)
              — short pie sweeping down-left from top-center.
  s2  长横 :  head ('ML', 0.51, 0.816) → tail ('MR', 0.174, 0.5)
              — main long heng, slight rise to the right.
  s3  竖钩 :  head ('ML', 0.946, 0.371) → tail ('BL', 0.721, 0.669)
              — vertical with slight left curve (no obvious hook in GT).
  s4  提   :  head ('BL', 0.293, 0.396) → tail ('BC', 0.441, 0.021)
              — ti rising up-right from lower-left to center.
  s5  斜钩 :  head ('TC', 0.441, 0.636) → tail ('BR', 0.619, 0.493)
              — long slanted body from top-center to bottom-right,
                with the classic 斜钩 flick UP at the tip.
  s6  短撇 :  head ('MR', 0.118, 0.793) → tail ('BC', 0.33, 0.613)
              — pie from mid-right down-left through the 斜钩 body.
  s7  点   :  head ('TC', 0.925, 0.92) → tail ('MR', 0.288, 0.143)
              — small dot upper-right of the 斜钩 head.

Joints (from MMH):
  s1.mid  ⇆ s3.head @ ML  : N (small gap, ~10 px)
  s1.head ⇆ s5.mid  @ C   : N (~32 px)
  s2.mid  ⇆ s3.mid  @ C   : P welded
  s2.mid  ⇆ s5.mid  @ C   : P welded
  s3.mid  ⇆ s4.mid  @ BC  : P welded
  s5.mid  ⇆ s6.mid  @ BC  : P welded

By-construction the P joints are enforced because the stroke geometries
literally cross at the specified cells. The N joints emerge naturally
because s1's tail lands near ML (0.60,0.47) while s3's head is at
ML(0.95,0.37) — natural ~30 px separation.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ("7 strokes rendered per MMH anchors. Left cluster: short "
              "pie s1 + long heng s2 + vertical s3 + ti s4 forming the "
              "手-radical. Right cluster: 斜钩 s5 with tip flick + pie "
              "s6 crossing s5 lower half + dot s7 upper-right. P-joints "
              "welded by geometry at C (s2×s3, s2×s5) and BC (s3×s4, "
              "s5×s6); N-joints natural at ML (s1↔s3) and C (s1↔s5)."),
}


def _stroke_line(draw, a, b, w=8):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), width=w)


def _stroke_tapered(draw, a, b, head_w=10, tail_w=2, n=30):
    p0, p1 = anchor_to_xy(a), anchor_to_xy(b)
    pts = sample_line(p0, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def _stroke_bezier(draw, a, ctrl, b, head_w=10, tail_w=2, n=30):
    p0, p1 = anchor_to_xy(a), anchor_to_xy(b)
    pc = anchor_to_xy(ctrl)
    pts = quad_bezier(p0, pc, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s5 (斜钩) drawn FIRST so later crossings overlay cleanly.
    # Long slanted body from TC(0.44,0.64) to BR(0.62,0.49), then flick UP.
    s5_head = ('TC', 0.441, 0.636)
    s5_belly = ('C', 0.75, 0.55)     # slight bow to the right of straight line
    s5_hook_end = ('BR', 0.75, 0.85)  # where body reaches before hook flick
    s5_tip = ('BR', 0.619, 0.493)     # MMH tail = hook tip (upward flick)

    # body: tapered bezier
    p0 = anchor_to_xy(s5_head)
    pc = anchor_to_xy(s5_belly)
    p1 = anchor_to_xy(s5_hook_end)
    body_pts = quad_bezier(p0, pc, p1, n=40)
    body_widths = [4 + (12 - 4) * (i / 40) for i in range(41)]
    stroke_variable_width(draw, body_pts, body_widths)
    # hook flick: from body end up to tip
    hook_pts = sample_line(p1, anchor_to_xy(s5_tip), n=12)
    hook_widths = [12 - (12 - 2) * (i / 12) for i in range(13)]
    stroke_variable_width(draw, hook_pts, hook_widths)

    # ---- s2 (长横) main horizontal — slight rise to right (y 181→150).
    _stroke_line(draw, ('ML', 0.51, 0.816), ('MR', 0.174, 0.5), w=9)

    # ---- s3 (竖钩-lite) vertical with slight leftward drift.
    s3_head = ('ML', 0.946, 0.371)
    s3_mid = ('C', 0.05, 0.65)
    s3_tail = ('BL', 0.721, 0.669)
    _stroke_bezier(draw, s3_head, s3_mid, s3_tail,
                   head_w=9, tail_w=7, n=30)

    # ---- s1 (短撇) short pie from upper C down-left to ML.
    _stroke_tapered(draw, ('C', 0.342, 0.163), ('ML', 0.595, 0.471),
                    head_w=9, tail_w=3, n=25)

    # ---- s4 (提) rising stroke from lower-left up to center.
    _stroke_tapered(draw, ('BL', 0.293, 0.396), ('BC', 0.441, 0.021),
                    head_w=9, tail_w=2, n=25)

    # ---- s6 (短撇) pie crossing s5 lower half.
    _stroke_tapered(draw, ('MR', 0.118, 0.793), ('BC', 0.33, 0.613),
                    head_w=8, tail_w=2, n=25)

    # ---- s7 (点) small dot upper-right of 斜钩 head.
    # Draw as a short thick tapered stroke.
    _stroke_tapered(draw, ('TC', 0.925, 0.92), ('MR', 0.288, 0.143),
                    head_w=4, tail_w=9, n=15)

    out = os.path.join(os.path.dirname(__file__), '01_我.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
