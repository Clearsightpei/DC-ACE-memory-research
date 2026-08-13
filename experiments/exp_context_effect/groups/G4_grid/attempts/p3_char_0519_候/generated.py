# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (pie head TL(0.80,0.68) → BL(0.19,0.02); shu ML(0.69,0.47) → BL(0.69,0.91)) — well left of ren_side's TC/C standalone defaults. Per B10-B12 ren_side_far_left named pattern, inline pie+shu with MMH-verbatim anchors preserves compositional proportion.
# fresh_component: ren_side_far_left_for_候

"""候 (hòu) — 10 strokes.
Decomposition: 候 = 亻 (left, s1-s2) + 侯-right (s3-s10).
  亻 : pie (s1) + shu (s2), far-left column.
  Right radical top: short pie (s3) + heng-with-drop (s4).
  Middle: heng (s5).
  Bottom (矢-cluster with X-cross): vertical pie (s6) + heng (s7) +
    horizontal bar (s8) welded with pie (s9) X-cross + na (s10).
All anchors MMH-verbatim per B9-B12 A-recipe.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 10 strokes matches MMH
    'endpoint_mismatches': [],    # all anchors MMH-verbatim
    'joint_class_mismatches': [], # N-joints preserved as natural gaps; s8/s9 X-cross welded (P)
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 亻 far-left inlined (BANK_DEVIATION vs ren_side); X-cross s8/s9 welded via shared BC(0.813, 0.17) apex per B7r 文 recipe.',
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK_CODE = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK_CODE))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie   # noqa: E402
from shu import draw_shu   # noqa: E402
from heng import draw_heng # noqa: E402
from na import draw_na     # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: 亻 pie — TL(0.803, 0.683) → BL(0.193, 0.019)
    draw_pie(d, ('TL', 0.803, 0.683), ('BL', 0.193, 0.019),
             head_width=12, tail_width=1, curve=0.04, segments=48)

    # s2: 亻 shu — ML(0.691, 0.468) → BL(0.686, 0.906)
    draw_shu(d, ('ML', 0.691, 0.468), ('BL', 0.686, 0.906), width=9)

    # s3: short pie at top of right radical — C(0.046, 0.438) → BC(0.107, 0.37)
    #     (near-vertical short taper — top-left tick of 侯 right)
    draw_pie(d, ('C', 0.046, 0.438), ('BC', 0.107, 0.37),
             head_width=8, tail_width=2, curve=0.05, segments=32)

    # s4: top heng-with-drop (横折) — TC(0.45, 0.861) → C(0.966, 0.157) per MMH.
    # MMH gives just head/tail; visual GT shows a horizontal arch that
    # spans wide across the top then drops. Add inferred corner at
    # ('TR', 0.6, 0.85) so the arch shape reads correctly. Endpoints
    # remain MMH-verbatim.
    from heng_zhe import draw_heng_zhe  # noqa: E402
    draw_heng_zhe(d,
                  head=('TC', 0.45, 0.861),
                  corner=('TR', 0.6, 0.85),
                  tail=('C', 0.966, 0.157),
                  h_width=9, v_width=9)

    # s5: middle heng of right radical — C(0.301, 0.304) → MR(0.572, 0.207)
    draw_heng(d, ('C', 0.301, 0.304), ('MR', 0.572, 0.207), width=8)

    # s6: vertical/pie stroke down-left inside right radical —
    #     C(0.57, 0.33) → C(0.318, 0.96)
    draw_pie(d, ('C', 0.57, 0.33), ('C', 0.318, 0.96),
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s7: heng in bottom half — C(0.573, 0.752) → MR(0.323, 0.617)
    draw_heng(d, ('C', 0.573, 0.752), ('MR', 0.323, 0.617), width=8)

    # s8 + s9 form the X-cross (P — welded) at ~BC(0.813, 0.17).
    # Weld both through a shared apex per B7r 文 recipe.
    CROSS = anchor_to_xy(('BC', 0.813, 0.17))

    # s8: heng-like piece — BC(0.266, 0.229) → BR(0.593, 0.112)
    s8_a = anchor_to_xy(('BC', 0.266, 0.229))
    s8_b = anchor_to_xy(('BR', 0.593, 0.112))
    fat_line(d, s8_a, CROSS, 8)
    fat_line(d, CROSS, s8_b, 8)

    # s9: pie down-left through the cross — C(0.731, 0.802) → BC(0.128, 0.9)
    #     Route via CROSS as mid to weld with s8.
    s9_head = anchor_to_xy(('C', 0.731, 0.802))
    s9_tail = anchor_to_xy(('BC', 0.128, 0.9))
    # Variable-width pie: fat at head, taper to tail; forced through CROSS.
    pts_a = quad_bezier(s9_head, CROSS, ((s9_head[0]+CROSS[0])/2, (s9_head[1]+CROSS[1])/2), n=1)
    # Simpler: two segments head→CROSS→tail with taper.
    seg1 = quad_bezier(s9_head, ((s9_head[0]+CROSS[0])/2, (s9_head[1]+CROSS[1])/2), CROSS, n=20)
    seg2 = quad_bezier(CROSS, ((CROSS[0]+s9_tail[0])/2, (CROSS[1]+s9_tail[1])/2), s9_tail, n=28)
    pts = seg1 + seg2[1:]
    widths = [10 + (1 - 10) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s10: na (right-falling) — BC(0.887, 0.241) → BR(0.804, 0.903)
    draw_na(d, ('BC', 0.887, 0.241), ('BR', 0.804, 0.903),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.10, segments=48)

    out = Path(__file__).parent / "01_候.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
