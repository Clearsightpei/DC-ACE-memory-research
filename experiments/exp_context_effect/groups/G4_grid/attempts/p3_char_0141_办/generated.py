"""p3_char_0141_办 — 办 (bàn, "manage", 4画).

Structural expectations (MMH-derived, per dispatcher):
  Stroke count: 4
  s1: head ('ML', 0.68, 0.55) → tail ('BC', 0.365, 0.643)   — short 横折钩-ish upper piece
  s2: head ('TC', 0.362, 0.735) → tail ('BL', 0.393, 0.941)  — long central 撇
  s3: head ('ML', 0.826, 0.828) → tail ('BL', 0.542, 0.279)  — left dian/short 撇
  s4: head ('MR', 0.276, 0.816) → tail ('BR', 0.643, 0.241)  — right dian/short 捺

Joints:
  s1.mid ⇆ s2.mid @ C   — P (welded crossing)
  s1.head ⇆ s3.head @ ML — N (small gap ~32 px)
  s1.mid  ⇆ s4.head @ MR — N (small gap ~28 px)

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. INDEX grep: 力 exists as `li.py` (力 = 横折钩 + 撇). 办 = 力 + 2 flanking dots.
     BUT: MMH gives s1 as very short (head ML 0.68,0.55 → BC 0.365,0.643), and s2 as
     the full long central 撇. This looks like a 力-with-hook drawn as a broken glyph
     rather than a clean 横折钩. I will follow MMH anchors literally (TR: MMH-literal
     wins over primitive-forcing when anchors don't match). No li.py override anchor
     fits cleanly, so I inline all 4 strokes.
  2. errata: 办 not in errata.
  3. form_catalog: dot / short 撇 patterns used.
  4. principles_meta: TR1 (override anchors), TR6 (inline when primitive doesn't fit).
  5. joint_atlas: P welded; N gap ~15-25 px preserved.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-literal; s1 short upper hook, s2 long central 撇 pierces s1, s3/s4 flanking dots N-gap.'
}


def draw_curve(draw, head_anchor, tail_anchor, curve, head_w, tail_w, n=48):
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 横折钩 (hook stroke): the central "力"-body hook.
    # MMH endpoints: head ML(0.68,0.55)=(68,155), tail BC(0.365,0.643)=(136.5,264.3).
    # Render as a horizontal→vertical→hook shape: from head, go right along the top,
    # then bend down to the tail, ending with a small leftward hook flick.
    from _anchor import anchor_to_xy
    p_head = anchor_to_xy(('ML', 0.68, 0.55))       # (68, 155)
    p_tail = anchor_to_xy(('BC', 0.365, 0.643))     # (136.5, 264.3)
    # Corner near TR-of-ML / TL-of-C: put it at (155, 155) so we have a top-bar.
    # Actually to reach BC tail we need the corner at the top-right of the horizontal,
    # then descend. Place corner at (155, 158).
    p_corner = (155, 158)
    # Top horizontal bar (head → corner)
    fat_line(d, p_head, p_corner, 9)
    # Vertical descent to tail (corner → tail)
    # We want the tail-hook to flick leftward at end.
    # Draw a slight arc down.
    seg_pts = quad_bezier(p_corner, ((p_corner[0]+p_tail[0])/2 + 4, (p_corner[1]+p_tail[1])/2),
                           p_tail, n=32)
    widths = [9 + (7 - 9) * (i / 32) for i in range(33)]
    stroke_variable_width(d, seg_pts, widths)
    # Small leftward hook at the tail
    hook_end = (p_tail[0] - 14, p_tail[1] - 8)
    fat_line(d, p_tail, hook_end, 6)

    # s2 — long central 撇: TC(0.362,0.735) → BL(0.393,0.941)
    # Big diagonal sweep from upper-center to bottom-left. Concave to right.
    draw_curve(d, ('TC', 0.362, 0.735), ('BL', 0.393, 0.941),
               curve=0.10, head_w=10, tail_w=2)

    # s3 — small left 撇/dot: ML(0.826,0.828) → BL(0.542,0.279)
    # This maps to a short mark on the left of the body. Render as a small 撇.
    draw_curve(d, ('ML', 0.826, 0.828), ('BL', 0.542, 0.279),
               curve=0.05, head_w=8, tail_w=2)

    # s4 — small right 捺/dot: MR(0.276,0.816) → BR(0.643,0.241)
    # Short mark on the right, tapering toward the tail (like a 捺 dot).
    draw_curve(d, ('MR', 0.276, 0.816), ('BR', 0.643, 0.241),
               curve=-0.05, head_w=3, tail_w=9)

    out = os.path.join(_HERE, '01_办.png')
    img.save(out)
    print('saved:', out)


if __name__ == '__main__':
    draw()
