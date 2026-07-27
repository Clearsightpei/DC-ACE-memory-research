"""p3_char_0019_儿 — G4 attempt (re-render vs CLEAN GT).

Character 儿 (ér, "legs"): 2 strokes.
  s1 — 撇 (piě, left sweeping stroke)
       head @ ML(0.929, 0.093), tail @ BL(0.393, 0.827)   [MMH]
  s2 — 竖弯钩 (shù wān gōu, vertical-turn-hook, right leg)
       head @ TC(0.567, 0.838), tail(tip) @ BR(0.71, 0.227) [MMH]
       Body descends vertically along x≈156.7 (TR8 rule 6),
       corner near bottom (BC), sweeps right to hook_pt in BR,
       then flicks UP to MMH tip.

Joints: NONE (per MMH — strokes have clear separation).

Bank reuse (per TR1 — override anchors):
  - draw_pie(...) for s1
  - draw_shu_wan_gou(...) for s2 (5-anchor compound stroke primitive
    that counts as ONE stroke matching MMH stroke count).

Prior attempt (against corrupt GT) had thin 撇 and body corner too high.
This revision:
  - increases 撇 head width (13 -> 16) to match GT ink weight.
  - re-anchors s2 body so it descends further before the bend
    (corner y ≈ 260 px, i.e. deep in BC), giving a taller right leg
    that matches GT proportions.
  - places hook_pt at BR(0.4, 0.6) so horizontal sweep is short and
    the tip flick UP to BR(0.71, 0.227) is clearly visible.
"""
import os
import sys
from PIL import Image, ImageDraw

# Bank imports.
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie                       # noqa: E402
from shu_wan_gou import draw_shu_wan_gou       # noqa: E402
from _anchor import anchor_to_xy               # noqa: E402


# ---- Anchor plan (TR7) ----------------------------------------------

S1_HEAD    = ('ML', 0.929, 0.093)   # MMH — upper right of ML cell
S1_TAIL    = ('BL', 0.393, 0.827)   # MMH — lower left area

S2_HEAD    = ('TC', 0.567, 0.838)   # MMH — bottom of TC cell (top-center, low)
S2_BELLY   = ('C',  0.567, 0.60)    # keeps x aligned with head — straight body (TR8 r6)
S2_CORNER  = ('BC', 0.567, 0.60)    # bend deep in BC (y ≈ 260 px)
S2_HOOK_PT = ('BR', 0.40, 0.60)     # base of hook, right side (x ≈ 240, y ≈ 260)
S2_TIP     = ('BR', 0.71, 0.227)    # MMH (hook flick UP)


# ---- SELF_CHECK -----------------------------------------------------

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitive calls == expected 2 strokes
    'endpoint_mismatches': [
        # s1: exact MMH match on both endpoints.
        # s2: head + tip are MMH-verbatim; belly/corner/hook_pt are
        # internal to the compound-stroke primitive (not part of MMH
        # endpoint spec, but chosen to keep the body vertical per
        # TR8 r6 and give a clear UP flick at the tip).
    ],
    'joint_class_mismatches': [],  # NONE expected, NONE implemented
    'overall_pass': True,
    'notes': ('Revised vs prior attempt: thicker 撇 (head_w 13->16), '
              'body corner pushed deeper into BC so right leg is taller '
              'to match the clean GT proportions.'),
}


# ---- Render ---------------------------------------------------------

def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 撇 (thicker head so it's readable at 300x300 like GT).
    draw_pie(draw, S1_HEAD, S1_TAIL,
             head_width=16, tail_width=2, curve=0.10, segments=48)

    # s2 — 竖弯钩
    draw_shu_wan_gou(draw, S2_HEAD, S2_BELLY, S2_CORNER, S2_HOOK_PT, S2_TIP,
                     head_w=10, belly_w=13, corner_w=12,
                     hook_start_w=11, tip_w=2)

    out = os.path.join(HERE, '01_儿.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
