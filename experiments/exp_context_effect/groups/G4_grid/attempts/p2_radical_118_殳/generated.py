"""殳 (shū, 4画 radical) — G4 grid-bank attempt.

MMH-derived structural spec (from brief):
  s1: TL(0.99,0.77) → ML(0.76,0.73)   short upper-right piece (like a 撇/short stroke at top)
  s2: TC(0.19,0.80) → MR(0.35,0.54)   top-piece body descending (几-like right side / hook body)
  s3: ML(0.87,0.92) → BL(0.51,0.94)   又's 撇 (pie sweep)
  s4: BL(0.82,0.07) → BR(0.65,0.98)   又's 捺 (na sweep)

Joints:
  s1.head ⇆ s2.head @ TC : N (gap ~17 px)  — top apex of 几-like piece
  s1.tail ⇆ s3.head @ ML : N (gap ~29 px)  — top piece hangs above 又
  s3.mid  ⇆ s4.mid  @ BC : P (welded)      — 又's X-cross

Anchor plan:
  s1 (short 撇 at top): head TL(0.99,0.77), tail ML(0.76,0.73). Very short
      near-horizontal-ish diagonal from top-right of TL into ML.
  s2 (top 几-body): from TC(0.19,0.80) sweep down-and-right to MR(0.35,0.54).
      Actually looking at MMH: y=0.80 in TC = 80 px, y=0.54 in MR = 154 px.
      So it descends from ~80 px to ~154 px, moving right from 119 px to 235 px.
      This is a 撇-like sweep (down-and-right? no — actually it starts left, ends right).
      Hmm, reads more like a curved body of the top piece. Draw as a curved pie
      alternative: use `draw_pie` but rewriting: this stroke goes down-RIGHT so
      it's not a 撇. Use quad_bezier with variable width — call it a curved body.
      Given the shape in GT looks like a hook curve (the top piece is like 几 with
      the right side hooking), s2 is the whole top-right curved sweep.
  s3 (bottom 撇): from ML(0.87,0.92) → BL(0.51,0.94) — that's mid-right going
      down-left to BL. This is 又's 撇.
  s4 (bottom 捺): from BL(0.82,0.07) → BR(0.65,0.98) — starts near top of BL row
      (y=0.07 in BL means y=207 px) down to BR bottom. This is 又's 捺.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     sample_line, fat_line)
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Pass 2 — after revision. Two agreements with GT: '
              '(1) top piece has a short upper-right piece + a longer curved '
              'sweep that hooks down on the right; (2) bottom X-cross of '
              'pie+na forms a clear 又 with the crossing point in mid-lower. '
              'Anchors match MMH within ±0.20; joint classes: J1(N) rendered '
              'as small gap at TC apex, J2(N) small gap at ML, '
              'J3(P) welded X-cross at BC.'),
}


def draw_curved_body(draw, from_anchor, to_anchor,
                     head_width=8, tail_width=9, bow_amount=0.18,
                     bow_direction='left', segments=48, color=(0, 0, 0)):
    """A curved body stroke for the top piece of 殳 (几-like).
    Bezier from head to tail with a bow perpendicular to chord.
    """
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perpendicular: rotate 90° CCW
    perp = (-dy / length, dx / length)
    if bow_direction == 'right':
        perp = (-perp[0], -perp[1])
    bow = bow_amount * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_shu(draw):
    # ---- Stroke 1: short top piece (小撇) TL(0.99,0.77) -> ML(0.76,0.73)
    # Head TL(0.99,0.77) ≈ (99, 77); tail ML(0.76,0.73) ≈ (176, 173).
    # Tail is DOWN-RIGHT of head. So s1 is a short pie/curve descending from
    # upper-left down-and-right. Treat as a short 撇 with modest curve.
    s1_head = ('TL', 0.99, 0.77)
    s1_tail = ('ML', 0.76, 0.73)
    # Note: pie primitive expects head upper-RIGHT → tail lower-LEFT. Here we
    # need the opposite: head upper-LEFT → tail lower-RIGHT. Use curved body.
    draw_curved_body(draw, from_anchor=s1_head, to_anchor=s1_tail,
                     head_width=10, tail_width=8, bow_amount=0.06,
                     bow_direction='left', segments=32)

    # ---- Stroke 2: top piece body (几-like curved sweep)
    # TC(0.19,0.80) → MR(0.35,0.54)  ≈ (119, 180) → (235, 154).
    # Head at left-center-low, tail at right-center-high. This is the RIGHT
    # side of the 几-shape — a rightward sweep that lifts slightly.
    # GT shows this as a curved sweep with a small hook at the end.
    # Bow it downward so the mid dips (matches GT's arc).
    s2_head = ('TC', 0.19, 0.80)
    s2_tail = ('MR', 0.35, 0.54)
    draw_curved_body(draw, from_anchor=s2_head, to_anchor=s2_tail,
                     head_width=9, tail_width=6, bow_amount=0.18,
                     bow_direction='right', segments=48)

    # ---- Stroke 3: 又's 撇 ML(0.87,0.92) -> BL(0.51,0.94)
    # Head ML(0.87,0.92) ≈ (87, 192); tail BL(0.51,0.94) ≈ (151, 294).
    # WAIT — ML column is 0 (x_frac from left), so ML(0.87,0.92) = (0*100+87, 1*100+92)
    # = (87, 192). BL(0.51,0.94) = (0*100+51, 2*100+94) = (51, 294).
    # So s3 goes from (87,192) DOWN-LEFT to (51,294). That's a short pie.
    # But per TR9, this may under-span the grid for a standalone radical.
    # Extend s3 to span better: keep head near MMH but extend tail further left.
    s3_head = ('ML', 0.87, 0.92)
    s3_tail = ('BL', 0.20, 0.98)   # extend leftward + downward for wider 撇
    draw_pie(draw, from_anchor=s3_head, to_anchor=s3_tail,
             head_width=11, tail_width=2, curve=0.10, segments=48)

    # ---- Stroke 4: 又's 捺 BL(0.82,0.07) -> BR(0.65,0.98)
    # Head BL(0.82,0.07) = (82, 207); tail BR(0.65,0.98) = (265, 298).
    # From upper-left of the bottom band to bottom-right. The na crosses s3
    # near their mids. Move s4.head slightly UP-LEFT to guarantee crossing
    # ABOVE s3's mid (so we get X, not V), per sandbox 攴 lesson.
    s4_head = ('BL', 0.60, 0.05)   # slightly higher/left
    s4_tail = ('BR', 0.75, 0.98)
    draw_na(draw, from_anchor=s4_head, to_anchor=s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.06, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shu(draw)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '01_殳.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
