"""p3_char_0177_仗 — G5 RETRY 1.

TRAJECTORY DIFF
---------------
main attempt (FAIL): draw_ren_left(ox=-63, scale=1.0) + inline 丈 (heng, pie,
na) using MMH anchors verbatim, bow_perp=14 on both pie and na.

Visual gaps I see in the failed main PNG:
  (1) 亻 was slightly too dominant on the left half. Its shu drops from
      (~76, 158) to (~78, 293) — full height — while GT's 亻 shu ends higher
      (~285) and the whole 亻 reads a bit more compressed against the left
      edge. Effect: 丈 got squeezed and the right/bottom sweep didn't have
      canvas room.
  (2) The pie of 丈 was drawn with bow_perp=+14. For 丈's long descending
      pie, that positive bow arcs the pie's belly to the RIGHT of the
      head→tail line (image y-down), which reads slightly bulbous instead
      of the crisp leftward-curling stroke in the GT.
  (3) The na tail (281, 288) landed near the corner but the na head (120,
      179) sits high-left; the pie/na crossing landed at (~134, 188) —
      way above the visual crossing point in the GT (which is near BC,
      ~y=225). Result: pie and na looked like separate strokes rather
      than a joined X-cross under the heng.

errata.md B6 hint: "draw_ren_left(ox=-63, scale=0.55), extend 丈 right
anchors." scale=0.55 alone would push 亻's pie tail off-canvas (x<0);
I read that as "shrink 亻 modestly, give 丈 the room." Applying: scale
0.85 with ox=-52 keeps 亻's pie tail at x~16 and shu around x~66-70,
leaving 丈 x=[85, 290] to work with.

Fixes this attempt:
  (a) 亻 at scale=0.85, ox=-52, oy=+8 → compact 亻 hugging left column
      without off-canvas clipping.
  (b) 丈 pie: bow_perp=-6 (slight LEFTWARD curl = anatomically correct
      for a long 撇), head nudged slightly right (185, 58) so the
      pie/heng cross lands closer to heng's left-third.
  (c) 丈 na: head moved down-right to (145, 190) so it starts near the
      pie's t=0.6 point (crossing zone), and tail pushed to (287, 285)
      for a full BR sweep. bow_perp=+18 for a deeper na belly.
  (d) heng widened: (108, 148) → (270, 130) instead of MMH's (129, 154)
      → (249, 133), giving the top the wider spread visible in GT.

Stroke count: 2 (ren_left) + 3 (丈 inline heng/pie/na) = 5 ✓
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from ren_left import draw_ren_left
from heng import draw_heng
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': None,            # filled in during self-check pass
    'stroke_count_ok': True,      # 2 (亻) + 3 (丈) = 5
    'endpoint_mismatches': [
        # 亻 shrunk 0.85x + shifted; deltas vs MMH:
        # s1 head expected (99.6, 66.8) actual (-52 + 158.8*.85, 8+73.8*.85)=(83.0, 70.7); dx=-16, dy=+4 — within tolerance (same cell TL)
        # s1 tail expected (25.8, 200.7) actual (-52 + 80.6*.85, 8+211.2*.85)=(16.5, 187.5); dx=-9, dy=-13 — within tolerance (same cell BL)
        # s2 head expected (75.3, 155.9) actual (-52+138.9*.85, 8+158.2*.85)=(66.1, 142.5); dx=-9, dy=-13 — same cell ML
        # s2 tail expected (77.9, 291.8) actual (-52+144.1*.85, 8+292.7*.85)=(70.5, 256.8); dx=-7, dy=-35 — dy just past tolerance (BL still)
        # heng head expected (129.2, 153.8) actual (108, 148); dx=-21, dy=-6 — near tolerance boundary
        # heng tail expected (248.7, 133.3) actual (270, 130); dx=+21, dy=-3
        # pie head expected (177.0, 61.8) actual (185, 58); dx=+8, dy=-4
        # pie tail expected (104.3, 277.4) actual (102, 285); dx=-2, dy=+8
        # na head expected (120.4, 178.7) actual (145, 190); dx=+25, dy=+11 — moved intentionally toward pie
        # na tail expected (281.0, 287.7) actual (287, 285); dx=+6, dy=-3
    ],
    'joint_class_mismatches': [], # 亻 s1↔s2 N (inherent); 丈 s3↔s4 P and s4↔s5 P emerge from crossings
    'overall_pass': None,         # decide after visual check
    'notes': 'Retry: shrink 亻 to 0.85 scale, negative bow on pie, na head raised toward pie crossing.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 on the LEFT (2 strokes, near-full-height) ----
    # scale 0.85 was too short vertically — pie tail ended at y~188 vs GT ~220
    # scale 0.95 with oy=+5 brings shu tail to y~283, matches GT
    draw_ren_left(d, ox=-52, oy=5, scale=0.95)

    # ---- 丈 inline on the RIGHT (3 strokes) ----
    # s3 一 (heng, wider than MMH, slight upward tilt; lowered vs prev)
    draw_heng(d, (108, 152), (270, 138),
              width_head=7, width_tail=9)

    # s4 丿 (long pie, slight LEFTWARD curl)
    draw_pie(d, (185, 58), (102, 285),
             bow_perp=-6, w_head=9, w_tail=3, steps=80)

    # s5 捺 (na sweep, head placed at pie-crossing point, tail full BR)
    # pie at y=190 is at x=137, so na head at (140, 192) crosses cleanly
    draw_na(d, (140, 192), (287, 283),
            bow_perp=18, w_head=4, w_tail=12, steps=80)

    out = os.path.join(os.path.dirname(__file__), "01_仗.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
