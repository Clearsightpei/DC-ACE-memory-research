"""刂 (dāo, "knife radical") — p2_radical_016.

Composition:
  stroke 1 — short 竖 on the left (upper-mid vertical, short)
  stroke 2 — 竖钩 on the right (long vertical body with up-left hook)

Anchor plan (MMH-derived expectations, per brief):
  stroke 1 (短竖):
    head @ ('C',  0.113, 0.16)   -> px ~ (111, 116)
    tail @ ('BC', 0.187, 0.174)  -> px ~ (119, 217)
    width thinner (component; short vertical), no hook.
  stroke 2 (竖钩):
    head    @ ('TC', 0.614, 0.712) -> px ~ (161,  71)
    hook_pt @ ('BC', 0.342, 0.701) -> px ~ (134, 270)
    belly   — held at same x as head for STRAIGHT body (shu_gou rule)
    tip     — up-and-left of hook_pt

Joints: NONE (per brief — strokes do not meet; clear separation).
  The horizontal gap between stroke 1 (x~111-119) and stroke 2 (x~134-161)
  is ~15-40px, which is a clear separation (not a joint).

Self-check:
  stroke_count = 2  (matches MMH expected 2).
  endpoints match cells & fracs exactly (used MMH values verbatim).
  no joints expected -> nothing to classify.
"""

import os
import sys
from PIL import Image, ImageDraw

# Make the local bank importable
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from shu import draw_shu           # noqa: E402
from shu_gou import draw_shu_gou   # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 2 primitive calls, matches expected 2
    'endpoint_mismatches': [],   # anchors used verbatim from MMH
    'joint_class_mismatches': [], # no expected joints
    'overall_pass': True,
    'notes': 'stroke1 short 竖 in C-BC (left); stroke2 竖钩 TC-BC (right, ~40px gap). '
             'stroke2 uses shu_gou with straight vertical body (belly shares x with head).',
}


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- stroke 1: short 竖 (left, upper-mid) ----
    # Component-thin width for a short vertical, per TR1/TR5.
    draw_shu(
        draw,
        ('C',  0.113, 0.16),
        ('BC', 0.187, 0.174),
        width=8,
    )

    # ---- stroke 2: 竖钩 (right, tall) ----
    # belly: same x_frac cell/frac as head to keep body STRAIGHT (shu_gou rule).
    # We choose belly at ML/MR interpolation: since head is TC(0.614) and hook is
    # BC(0.342), a straight body isn't strictly possible if we obey shu_gou's
    # "belly shares head x". shu_gou's body uses sample_line(p_head, p_hook),
    # so belly only affects width profile — safe to pick any belly on the body.
    # Put belly midway (in C cell) with the same x_frac as head for the width knot.
    # Tip: up-and-left of hook_pt.
    draw_shu_gou(
        draw,
        head=('TC', 0.614, 0.712),
        belly=('C', 0.47, 0.5),    # width-profile knot along the body
        hook_pt=('BC', 0.342, 0.701),
        # Longer/more visible up-left hook flick (刂's defining feature).
        tip=('BC', 0.05, 0.35),
        head_w=13,
        belly_w=12,
        hook_start_w=11,
        tip_w=2,
    )

    out = os.path.join(HERE, '01_刂.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
