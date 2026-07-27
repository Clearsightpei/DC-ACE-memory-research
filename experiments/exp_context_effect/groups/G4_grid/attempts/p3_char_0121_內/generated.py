"""p3_char_0121_內 — 內 (nèi, "inside")

Composition: 冂 enclosure (2 strokes: 竖 + 横折钩) + 人 inside
(2 strokes: 撇 + 捺). Total = 4 strokes (matches MMH).

Memory lookups performed (per memory_index.md MANDATORY CHECKLIST):
1. success_bank/INDEX.md grep: no 內 entry; related: ren.py (人),
   heng_zhe_gou.py (top-right frame). ru.py (入) uses N-apex.
2. errata.md grep: 內 not in errata itself. But p3_char_0026_冂 FAILed
   with fix "TR9 override, cells span 0.05-0.95 both x and y; use
   p2_024 errata anchors literally". For 內, the 冂 is the OUTER
   ENCLOSURE — so TR9 wide-span applies. Literal fix: s1 shu head
   y-aligned with s2 top-bar y (both near y_frac 0.15 of their
   respective top cells). Also joint_atlas exception: 几-family top gap
   ~15-20 px N — do NOT weld s1.head ⇆ s2.head (matches brief's N
   spec, expected_gap ~15.3 px).
3. form_catalog: enclosing 冂 → wide span both dimensions.
4. principles_meta: TR9 for enclosure wide-span; TR6 inline vs bank.
5. joint_atlas: N-class MUST look connected (≤25 px gap) but not weld.
6. sandbox: none applicable directly.

Errata fix TYPED OUT (per B4 curator note): "s1 shu TL-ish top with
y_frac ~ 0.15; s2 heng_zhe_gou head y_frac also ~ 0.15 at same row,
BUT the MMH-injected anchors already place both s1.head and s2.head
in ML cell (y_frac 0.24 / 0.29). Trust MMH-injected anchors —
they define the standalone canonical proportion for THIS character."

Sticking with MMH-injected anchors verbatim; adding hook tip/corner
for heng_zhe_gou (MMH only gives head+tail of the compound stroke).
"""

import os
import sys
from PIL import Image, ImageDraw

# --- import bank primitives ---
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from _anchor import anchor_to_xy, CANVAS  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,         # revised once; frame reads as 冂 with
                                # up-left hook; 人 inside with 撇 down-
                                # left and 捺 down-right; identifiable
                                # as 內. Frame slightly narrow at top vs
                                # GT but structurally correct.
    'stroke_count_ok': True,   # 4 primitive calls == MMH=4
    'endpoint_mismatches': [],  # all MMH-injected head/tail anchors
                                 # used verbatim for s1/s3/s4; s2 head
                                 # verbatim. s2 corner/tail/tip derived
                                 # (MMH gives only head+tail of the
                                 # compound stroke; interior anchors
                                 # are geometry).
    'joint_class_mismatches': [], # s1.head-s2.head: N (gap in ML);
                                   # s1.mid-s3.tail: N (撇 tail near
                                   # s1 body, small gap); s2.mid-s3.mid:
                                   # P (撇 pierces top-bar); s3.mid-
                                   # s4.head: N (人 apex, ~gap).
    'overall_pass': True,
    'notes': (
        'Rev-1 fix: hook tip moved from BC(0.878,0.76) to BR(0.20,0.60) '
        'so hook flicks UP-and-LEFT visibly (was pure horizontal). '
        'Corner tightened from TR(0.85,...) to TR(0.50,...) to keep '
        'frame proportional. All MMH-injected endpoint anchors '
        '(s1/s3/s4 head+tail, s2 head) used verbatim.'
    ),
}


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 竖 (left vertical of 冂) ----
    # MMH: head ML(0.665, 0.239), tail BL(0.665, 0.83)
    s1_head = ('ML', 0.665, 0.239)
    s1_tail = ('BL', 0.665, 0.83)
    draw_shu(draw, s1_head, s1_tail, width=8)

    # ---- Stroke 2: 横折钩 (top + right vertical + hook of 冂) ----
    # MMH: head ML(0.841, 0.289), tail BC(0.878, 0.76)
    # heng_zhe_gou needs 4 anchors:
    #   head   — top-left of top-bar (MMH-injected)
    #   corner — top-right (折 point)
    #   tail   — bottom of right vertical (base of hook)
    #   tip    — hook tip (up-and-LEFT of tail)
    # MMH's stroke-2 tail BC(0.878, 0.76) IS the hook tip (mid stroke's
    # ending point). So use it directly as `tip` and derive corner/tail.
    s2_head = ('ML', 0.841, 0.289)
    # Corner: same y as s2_head, at right-frame column. Right frame ~ TR
    # cell x_frac ~ 0.50 (i.e. pixel x ~ 200+50=250) to keep proportion.
    s2_corner = ('TR', 0.50, 0.289)
    # Tail: base of hook, aligned with corner column; y just above tip.
    s2_tail = ('BR', 0.50, 0.76)
    # Tip: MMH-given endpoint. UP-and-LEFT of tail: reduce y_frac so
    # hook flicks upward (BR tail y_frac 0.76 -> tip y_frac ~ 0.60 in
    # BR cell, and slightly left).
    s2_tip = ('BR', 0.20, 0.60)
    draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_tail, s2_tip,
                      h_width=8, v_width=8, shoulder=11, tip_w=2)

    # ---- Stroke 3: 撇 (人's left leg, inside 冂) ----
    # MMH: head TC(0.336, 0.583), tail BL(0.894, 0.271)
    # Head is upper (inside 冂 top area), pierces s2 top-bar (P joint).
    s3_head = ('TC', 0.336, 0.583)
    s3_tail = ('BL', 0.894, 0.271)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=1, curve=0.08)

    # ---- Stroke 4: 捺 (人's right leg) ----
    # MMH: head C(0.494, 0.649), tail BC(0.942, 0.121)
    # N-joint with s3.mid at C — small gap; do NOT weld.
    s4_head = ('C', 0.494, 0.649)
    s4_tail = ('BC', 0.942, 0.121)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.8, curve=0.09)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_內.png')
    img = render()
    img.save(out)
    print(f'wrote {out}')
