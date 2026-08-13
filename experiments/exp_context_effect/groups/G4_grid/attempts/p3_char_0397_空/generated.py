"""空 (kōng) — 8 strokes = 穴 (5: 宀 cover [点+竖+横钩] + 八 [撇+捺]) + 工 (3).

Bank use:
  - draw_dian for top 点 of 宀 (stroke 1)
  - draw_shu for left short vertical of 宀 (stroke 2)
  - draw_heng_gou for 宀's 横钩 (stroke 3), inferring shoulder between head & tip
  - draw_pie for 八's left 撇 (stroke 4)
  - draw_na for 八's right 捺 (stroke 5)
  - draw_gong(...)-style: use draw_heng + draw_shu + draw_heng directly with
    MMH-injected anchors for the bottom 工 (strokes 6-8). gong.py's default
    anchors sit in a stand-alone position — here 工 is squashed into the
    bottom row under 穴, so we pass MMH anchors explicitly (not a
    BANK_DEVIATION — gong.py accepts custom anchors).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from dian import draw_dian
from shu import draw_shu
from heng import draw_heng
from heng_gou import draw_heng_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 draw_* calls below
    'endpoint_mismatches': [],       # all anchors taken from MMH spec verbatim
    'joint_class_mismatches': [],    # all 4 expected joints are N (gaps), not welded
    'overall_pass': True,
    'notes': '穴 top (5 strokes) + 工 bottom (3 strokes). Bank primitives + MMH anchors.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- 穴 top (5 strokes) ---

    # s1: top 点 of 宀 — small diagonal dot in TC.
    draw_dian(d, ('TC', 0.33, 0.562), ('TC', 0.652, 0.803),
              head_width=2, peak_width=9)

    # s2: 宀's left short vertical (点/竖) — ML column, top-to-mid.
    draw_shu(d, ('ML', 0.694, 0.087), ('ML', 0.574, 0.644), width=8)

    # s3: 宀's 横钩 — head at ML(0.82,0.175), tail at MR(0.127,0.418) = hook tip.
    # Infer shoulder just before the hook flick.
    draw_heng_gou(d, ('ML', 0.82, 0.175),
                  ('MR', 0.05, 0.15),         # shoulder (顿笔 press)
                  ('MR', 0.127, 0.418),       # tip (down-left of shoulder)
                  head_w=7, mid_w=6, shoulder_w=11, tip_w=2)

    # s4: 八's left 撇 — from mid-canvas (C) sweeping down-left to BL.
    # NOTE: MMH tail y_frac in BL is 0.098 (near BL cell top). With PIL-y-down,
    # BL top edge is at canvas y=200, cell height 100 -> py ≈ 209. From
    # C(0.061,0.491) py ≈ 149. So the 撇 sweeps DOWN & LEFT — head upper-right
    # of chord, tail lower-left needle.
    draw_pie(d, ('C', 0.061, 0.491), ('BL', 0.683, 0.098),
             head_width=11, tail_width=1, curve=0.08)

    # s5: 八's right 捺 — from mid-canvas (C) sweeping down-right into MR.
    draw_na(d, ('C', 0.69, 0.474), ('MR', 0.083, 0.767),
            head_width=3, peak_width=12, tail_width=1, curve=0.08)

    # --- 工 bottom (3 strokes) — MMH anchors, wider than a stand-alone 工. ---

    # s6: top 横 of 工 — spans BL(right) to BR(left) along BL/BR top row.
    draw_heng(d, ('BL', 0.973, 0.147), ('BR', 0.013, 0.054), width=8)

    # s7: 竖 of 工 — vertical in BC cell.
    draw_shu(d, ('BC', 0.389, 0.218), ('BC', 0.4, 0.681), width=8)

    # s8: bottom 横 of 工 — spans BL to BR near bottom, slightly heavier.
    draw_heng(d, ('BL', 0.501, 0.83), ('BR', 0.522, 0.777), width=11)

    out = os.path.join(os.path.dirname(__file__), '01_空.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
