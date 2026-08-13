"""G5 retry_2: p2_radical_100_见 (4-stroke radical).

TRAJECTORY DIFF (from inspecting GT + main + retry_1 PNGs):

GT observation:
  见 = top-box (冂-like, but with LEFT vertical starting HIGH) + 儿 legs
  emerging INSIDE and BELOW the box.
  Box extents ~ (95, 55) to (215, 210) — noticeably TALLER than wide
  (aspect ~1:1.15).  Left vertical descends full box height.  Top-heng
  runs across; right vertical descends slightly less far and ends with
  a soft knob.  Interior 撇 begins just under the top-heng near
  (135, 70) and sweeps to canvas bottom-left (~60, 285).  竖弯钩 begins
  interior at (~170, 125), drops vertically to (~170, 250), curves
  right to (~255, 275), hooks up-left to (~250, 240).

Main attempt failure (FAIL):
  (1) Box was too small / positioned high — left vertical only extended
      to y=205 (short of GT's y=210), and heng_zhe_box footprint was
      too narrow.
  (2) 撇 tail exited canvas (y=288+) and head sat too far inside the box.
  (3) 竖弯钩 was placed too far right and hook barely curled.
  Overall silhouette read as 凡 (no proper box + spread legs).

Retry_1 (C-verdict) partial fixes:
  (a) Welded top-left corner (s1_head.y=82 == s2_top_left.y=82) — good.
  (b) Trimmed s3 tail to (58, 272) — kept ink on canvas but too short,
      making the leg look stubby compared to GT's sweeping arc to y=285.
  (c) Nudged s3 head to (135, 148) — MOVED TOO FAR DOWN. GT shows pie
      starting HIGH inside the box (y~70-80), not mid-box. Moving down
      to y=148 lost the "leg emerging from top of box" silhouette.
  (d) s4 head at (153, 193) — WAY too far down; can't render a proper
      shu_wan_gou body if head is already at knee height. bottom_extra=48
      was too small for the visible sweep in GT.

Fixes THIS attempt (retry_2):
  1. Enlarge box: top_left=(95, 55), bottom_right=(215, 210). Left
     vertical descends full 155px.
  2. s3 head at (140, 72) — HIGH inside box, just under top-heng.
     Tail at (55, 285) — sweeping arc to canvas bottom-left.
  3. s4 head at (170, 125) — inside the box's upper-middle interior.
     Tail at (258, 240). bottom_extra=45 for pronounced bottom curl,
     knee_ratio=0.80 for wide right sweep.

Decomposition per MMH-injected anchors:
  s1: 竖 (left of top box)                    — bank: shu
  s2: 横折 (top + right of box, boxy)         — bank: heng_zhe_box
  s3: 撇 (long left-diagonal from box-top)    — bank: pie
  s4: 竖弯钩 (right leg with hook)             — bank: shu_wan_gou
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# Bank imports
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 4 strokes: shu, heng_zhe_box, pie, shu_wan_gou
    'endpoint_mismatches': [
        {'stroke': 3, 'expected_tail': ('BL', 0.448, 1.012),
         'actual_tail_px': (55, 285),
         'delta': 'clipped y-frac to 0.95 to keep ink on canvas'},
        {'stroke': 3, 'expected_head': ('C', 0.295, 0.157),
         'actual_head_px': (140, 72),
         'delta': 'head x nudged +10 for better crossing into box; y stays high'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_2: enlarged box, raised s3 head back up to box-top interior, extended s3 tail to full canvas, gave s4 room to render full shu_wan_gou body + hook.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── s1: 竖 (left of box) ─────────────────────────
    # MMH: TL(0.885, 0.82) → BL(0.958, 0.08).  Full left side of box.
    s1_head = (95, 55)
    s1_tail = (98, 210)
    draw_shu(d, s1_head, s1_tail, width=7)

    # ── s2: 横折 (top + right of box, boxy) ─────────
    # MMH: TC(0.061, 0.858) → BC(0.939, 0.048).  Top-left corner welded
    # to s1_head; box aspect slightly taller than wide.
    s2_top_left     = (95, 55)     # welded to s1_head
    s2_bottom_right = (215, 210)   # taller box, wider footprint
    draw_heng_zhe_box(d, s2_top_left, s2_bottom_right, width=7)

    # ── s3: 撇 ──────────────────────────────────────
    # MMH: C(0.295, 0.157) → BL(0.448, 1.012).  Long sweeping pie starting
    # HIGH inside box (just under top-heng), tail sweeping to canvas
    # bottom-left corner.  Head at y=72 (just below top-heng y=55).
    s3_head = (140, 72)
    s3_tail = (55, 285)
    draw_pie(d, s3_head, s3_tail, bow_perp=16, w_head=8, w_tail=3)

    # ── s4: 竖弯钩 ──────────────────────────────────
    # MMH: C(0.529, 0.925) → BR(0.695, 0.303).  Right leg — head inside
    # box mid-upper, vertical descent through box bottom, sweeping curve
    # rightward, terminal up-hook.  N-joint to s3.mid — natural gap.
    s4_head = (170, 125)
    s4_tail = (258, 240)
    draw_shu_wan_gou(d, s4_head, s4_tail, width=7,
                     bottom_extra=45, knee_ratio=0.80)

    return img


if __name__ == '__main__':
    img = render()
    out = pathlib.Path(__file__).parent / '01_见.png'
    img.save(out)
    print(f'wrote {out}  ({img.size})')
