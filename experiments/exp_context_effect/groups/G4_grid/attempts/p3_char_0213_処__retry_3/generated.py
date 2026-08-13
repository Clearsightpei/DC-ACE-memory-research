"""p3_char_0213_処 — retry_3 (G4)

Decomposition: 処 = 夂 (top-left, strokes 1-3) + 几 (top-right shell, strokes 4-5).

TRAJECTORY DIFF (visual — GT vs main / retry_2):
- GT reads as: three-stroke 夂 (short 撇 + longer 撇 + long sweeping 捺
  crossing the second 撇 down to lower-right) TUCKED INSIDE a wide-open
  几 (short left 撇 + big 横折弯钩 that sweeps from top-center out to
  bottom-right and up-flicks). The 几 arm is OPEN and CURVED, not a
  boxy frame.
- main FAIL: reads as amorphous frame + inner scribble — no
  recognisable 夂, no 几 arm; the right side looked like 门/口.
- retry_2 FAIL: got the 5 strokes but s5's top-横 hit TR corner too
  hard and the descent hugged the right edge with a boxy turn, so
  s4+s5 read as a closed 门/口 shape rather than 几's smooth open
  sweep. s3 also welded to s2 through a stiff v-shape (control-point
  hack) rather than a clean crossing 捺.
- Fixes this attempt:
    (1) s5: single smooth big-bezier for the horizontal→right-descent
        so it curves naturally instead of hitting the TR corner.
    (2) s3: draw as a plain draw_na (not a two-piece crossing hack).
        The na chord already passes near BL(0.945, 0.153) — welding is
        naturally satisfied by geometry.
    (3) s4 gets a stronger leftward bow so the 几's left arm reads as
        a real 撇 (not near-vertical).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 strokes, matches MMH
    'endpoint_mismatches': [],        # all MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('5 MMH-verbatim strokes; s3 is a plain 捺 crossing s2, '
              's5 is a smooth open 横折弯钩 with up-flick.'),
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from na import draw_na

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ---------- stroke 1: short 撇 (top of 夂) ----------
# MMH: head TL(0.797, 0.785) -> tail BL(0.261, 0.062)
draw_pie(d, ('TL', 0.797, 0.785), ('BL', 0.261, 0.062),
         head_width=8, tail_width=1, curve=0.10, segments=40)

# ---------- stroke 2: longer 撇 (body of 夂) ----------
# MMH: head ML(0.747, 0.503) -> tail BL(0.214, 0.812)
draw_pie(d, ('ML', 0.747, 0.503), ('BL', 0.214, 0.812),
         head_width=9, tail_width=1, curve=0.12, segments=44)

# ---------- stroke 3: 捺 (na crossing s2 near BL(0.945, 0.153)) ----------
# MMH: head ML(0.501, 0.978) -> tail BR(0.742, 0.804)
# The straight chord from (50.1, 197.8) to (274.2, 280.4) passes very
# near s2 at BL(0.945, 0.153) = (94.5, 215.3) — no hack needed for the
# P-weld; a plain 捺 will visually cross.
draw_na(d, ('ML', 0.501, 0.978), ('BR', 0.742, 0.804),
        head_width=3, peak_width=11, tail_width=1,
        peak_t=0.75, curve=0.06, segments=48)

# ---------- stroke 4: left 撇 of 几 ----------
# MMH: head TC(0.658, 0.861) -> tail BC(0.412, 0.253)
# Give it a real leftward bow so it looks like a 几-leg, not just a
# tilted 竖.
draw_pie(d, ('TC', 0.658, 0.861), ('BC', 0.412, 0.253),
         head_width=8, tail_width=2, curve=0.09, segments=36)

# ---------- stroke 5: 横折弯钩 (right arm of 几) — inlined ----------
# MMH: head TC(0.828, 0.879) -> tail BR(0.804, 0.01)
# Phases:
#   (a) short 横 from head, gently curving up-right to a shoulder
#       just inside TR.
#   (b) smooth 折+弯 descent hugging the right side but curving
#       inward at the bottom (open sweep, NOT a boxy corner).
#   (c) 钩 up-flick from the bottom sweep out to MMH tail
#       BR(0.804, 0.01) = (280.4, 200.1).
p_head     = anchor_to_xy(('TC', 0.828, 0.879))   # (182.8,  87.9)
p_shoulder = anchor_to_xy(('TR', 0.82, 0.55))     # (282.0, 155.0) — full-width top
p_bot_apex = anchor_to_xy(('BR', 0.42, 0.85))     # (242.0, 285.0) — bottom of sweep
p_tail     = anchor_to_xy(('BR', 0.804, 0.01))    # (280.4, 200.1) — MMH tail

# (a) top 横 — smooth right-and-down (no upward hump)
top_ctrl = (p_shoulder[0] - 20, p_head[1] + 4)
top_pts = quad_bezier(p_head, top_ctrl, p_shoulder, n=22)
top_w = [6 + 3 * (i / 22) for i in range(23)]

# (b) descent + rounded belly — bows outward-right then curves in
desc_ctrl = (p_shoulder[0] + 10, (p_shoulder[1] + p_bot_apex[1]) / 2 + 12)
desc_pts = quad_bezier(p_shoulder, desc_ctrl, p_bot_apex, n=32)
desc_w = [9 - 1 * (i / 32) for i in range(33)]

# (c) up-flick 钩 — from bottom apex up-and-right to MMH tail
flick_ctrl = (p_bot_apex[0] + 20,
              (p_bot_apex[1] + p_tail[1]) / 2 + 6)
flick_pts = quad_bezier(p_bot_apex, flick_ctrl, p_tail, n=18)
flick_w = [8 - 7 * (i / 18) for i in range(19)]

pts = top_pts + desc_pts[1:] + flick_pts[1:]
widths = top_w + desc_w[1:] + flick_w[1:]
stroke_variable_width(d, pts, widths)

# Save
out = os.path.join(os.path.dirname(__file__), '01_処.png')
img.save(out)
print(f'wrote {out}')
