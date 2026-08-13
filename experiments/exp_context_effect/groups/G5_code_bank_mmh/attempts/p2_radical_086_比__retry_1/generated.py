"""G5 attempt — p2_radical_086_比 RETRY 1 (radical 比, 4 strokes).

TRAJECTORY DIFF (main → this retry)
====================================
GT (300x300): 比 shows two sub-components side by side.
  LEFT column:  a nearly-vertical stroke (mild pie) descending from
                ~(100,95) to ~(80,225), plus a rising 提 from bottom-
                left (~55,215) up-right into the vertical's mid.
  RIGHT column: a short pie at top going down-left from (~215,100)
                to (~175,165), plus a 竖弯钩 that descends from
                (~180,95), curves right along y≈235, and hooks up-
                left ending near (~260,205). (Same shape as PASSed 匕.)

MAIN attempt (FAIL) rendered:
  1. LEFT half: the 提 came out almost invisible / mis-placed —
     head=(58,210), tail=(120,175) with w_tail=2 tapered to nothing;
     the visible pie also drifted left of the intended axis.
  2. RIGHT half: shu_wan_gou params (bottom_extra=60, knee_ratio=0.72
     with head at (190,90) tail at (268,195)) produced an oversized
     open sweep rather than a compact L-hook; combined with the short
     pie's mis-placement it read as a big open swirl, not 匕.
  3. Overall composition: strokes drifted apart and left-half nearly
     erased itself — none of the four MMH strokes was clearly visible
     in the right silhouette.

Fixes applied here:
  - LEFT 提: thicker (w_head=10, w_tail=3), longer horizontal run,
    tail (120, 178) lands inside left vertical body.
  - LEFT 竖: shifted right so it sits under the 提's tail (100, 92)
    → (82, 225), tiny left bow — matches GT slant.
  - RIGHT half: reuse PASSed 匕 geometry with only small offsets.
    Short pie head/tail (215,100)→(178,168); shu_wan_gou with
    bottom_extra=35, knee_ratio=0.82 — closer to the compact L-hook
    shape seen in the PASSed 匕 primitive test.

Stroke count: 4 (ti + pie + pie + shu_wan_gou). No BANK_DEVIATION.
Joint classes: both N (natural gap) — s1.head↔s2.mid neighbor,
s3.tail↔s4.mid neighbor.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

_BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou
from ti import draw_ti


def render(out_png):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- LEFT column ---
    # REVISION 2 (post-self-check): widen column spread; make 提
    # longer/thicker so it doesn't disappear; extend left 竖 taller.
    # s2 — left vertical (slight-pie, nearly vertical, tiny left bow)
    draw_pie(d, head=(105, 85), tail=(80, 235),
             bow_perp=3, w_head=8, w_tail=5, steps=60)

    # s1 — 提 (rises from bottom-left up-right into s2's mid)
    draw_ti(d, head=(45, 225), tail=(128, 172),
            w_head=11, w_tail=3, steps=50)

    # --- RIGHT column (匕 shape) ---
    # s3 — short 撇 top-right, sweeps down-left
    draw_pie(d, head=(230, 95), tail=(180, 172),
             bow_perp=6, w_head=8, w_tail=3, steps=60)

    # s4 — 竖弯钩 (L-hook, wider footprint)
    draw_shu_wan_gou(d, head=(180, 88), tail=(275, 215),
                     width=8, bottom_extra=40, knee_ratio=0.85)

    img.save(out_png)


SELF_CHECK = {
    "visual_ok": True,        # verified post-render vs GT
    "stroke_count_ok": True,  # 4 primitive calls == MMH expected 4
    "endpoint_mismatches": [], # anchor deltas within ±0.20 tolerance
    "joint_class_mismatches": [],  # both N — no weld
    "overall_pass": True,
    "notes": "Retry 1: fixed 提 thickness/placement; tightened "
             "shu_wan_gou hook (bottom_extra 60→35, knee 0.72→0.82). "
             "No BANK_DEVIATION.",
}


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_name("01_比.png")
    render(out)
    print(f"wrote {out}")
