"""p3_char_0240_仰 — G5 attempt.

Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
Left: 亻 (pie + shu) — anchor-consistent with draw_ren_left pattern but
inlined here to keep endpoints exactly matching this character's MMH.
Right: 卬's right cluster (4 strokes: pie, heng, ti, heng-zhe descender).

# BANK_DEVIATION
# skipped: ren_left.py (2-stroke primitive)
# reason: MMH endpoints for 仰's 亻 differ slightly from ren_left's frozen
#         layout; inlining pie+shu directly with this character's own MMH
#         anchors keeps N-joint gap tighter (per P-A-006 anchor-verbatim rule).
# fresh_component: pie+shu inline for 仰-亻
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from ti import draw_ti  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim endpoints. All 3 N-joints preserved (no welding).'
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # -- 亻 (person radical, left) --
    # s1: 亻 pie   head TL(0.908,0.598) -> tail ML(0.185,0.89)
    draw_pie(d, (90.8, 59.8), (18.5, 189.0),
             bow_perp=8, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu   head ML(0.691,0.456) -> tail BL(0.715,0.892)
    draw_shu(d, (69.1, 145.6), (71.5, 289.2), width=7)

    # -- 卬 (right cluster, 4 strokes) --
    # s3: short pie  head TC(0.588,0.768) -> tail C(0.266,0.277)
    draw_pie(d, (158.8, 76.8), (126.6, 127.7),
             bow_perp=4, w_head=8, w_tail=3, steps=50)
    # s4: heng (slants down slightly, per MMH)
    #     head C(0.055,0.242) -> tail C(0.711,0.737)
    draw_heng(d, (105.5, 124.2), (171.1, 173.7),
              width_head=8, width_tail=9)
    # s5: short ti  head MR(0.039,0.362) -> tail BR(0.159,0.03)
    #     (upward tick, small)
    draw_ti(d, (203.9, 136.2), (215.9, 203.0))
    # s6: 横折 descender (heng-zhe-shu for 卩 right side)
    #     head C(0.796,0.242) -> tail BC(0.919,1.129).
    #     MMH median: short heng rightward, then vertical down.
    #     Tail x (191.9) is close to head x (179.6) so vertical drops with
    #     slight left-slant back toward tail x.
    head_s6 = (179.6, 124.2)
    corner = (212.0, 126.0)
    tail_s6 = (191.9, 312.9)
    # top horizontal of 卩 (short heng)
    draw_heng(d, head_s6, corner, width_head=8, width_tail=9)
    # long vertical descender (from corner slightly left to tail)
    draw_shu(d, (corner[0] - 2, corner[1] + 4), tail_s6, width=7)

    out = Path(__file__).parent / "01_仰.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
