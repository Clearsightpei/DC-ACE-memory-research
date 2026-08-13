"""p3_char_0180_打 — G5 attempt.

打 = 扌 (left) + 丁 (right). 5 strokes total.

Composition strategy:
  - Left 扌  → call bank primitive `shou_hand.draw_shou` with ox=-60
    (shifts full-canvas 扌 to the left half of the composition). This
    contributes strokes 1-3 (heng + shu_gou + ti). Bank anchor deltas
    all land within ~10 px of the MMH-injected targets — see below.
  - Right 丁 → inline: `heng.draw_heng` (s4) + `shu_gou.draw_shu_gou`
    (s5). Only 2 strokes and the bank has no 丁 primitive yet, so
    inline is simpler than searching for a compound.

MMH anchors (300 px canvas, 米字格 cells 100 px wide, TL cell at (0,0)):
  s1 head ML(0.41,0.477)=(41,148)   tail C (0.333,0.324)=(133,132)
  s2 head TL(0.882,0.639)=(88,64)   tail BL(0.624,0.687)=(62,269)
  s3 head BL(0.167,0.297)=(17,230)  tail C (0.271,0.755)=(127,176)
  s4 head C (0.421,0.509)=(142,151) tail MR(0.687,0.397)=(269,140)
  s5 head C (0.945,0.532)=(195,153) tail BC(0.641,0.807)=(164,281)

draw_shou (bank) hard-codes:
  s1 (102,138)-(187,126)  s2 (143,67)-(115,263)  s3 (85,220)-(189,172)
With ox=-60, oy=0, scale=1.0 the bank anchors become:
  s1 (42,138)-(127,126) vs MMH (41,148)-(133,132) — dx/dy ≤ 10 ✓
  s2 (83,67)-(55,263)   vs MMH (88,64)-(62,269)   — dx/dy ≤ 7  ✓
  s3 (25,220)-(129,172) vs MMH (17,230)-(127,176) — dx/dy ≤ 10 ✓
All endpoints within the ±20 % / adjacent-cell tolerance.

Joints:
  s1.mid ⇆ s2.mid @ ML : P (welded crossing of 扌 heng × shu) — draw_shou
    already crosses these strokes at (~85, 130); implicit weld.
  s2.mid ⇆ s3.mid @ ML : P (welded crossing of 扌 ti × shu) — draw_shou
    already crosses these strokes near (~70, 200); implicit weld.
  s4.mid ⇆ s5.head @ C : N (natural ~20 px gap) — s5.head at (195, 153)
    sits below s4 heng (heng y ≈ 146 at x=195 → ~7 px raw gap). To
    hit the ~20 px N target, we lower s5.head to y=165 (shifts the 丁
    hook down and clears the horizontal by ~20 px). No bank deviation
    — the shu_gou primitive still receives (head, tail).
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
)
sys.path.insert(0, os.path.abspath(BANK))

from shou_hand import draw_shou  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "draw_shou at ox=-60 fits MMH 扌 anchors within 10 px; "
             "丁 inlined as heng + shu_gou; N-joint gap tuned to ~20 px "
             "by lowering s5.head y from 153 → 165.",
}


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # strokes 1-3: 扌 via bank primitive, shifted to left half
    draw_shou(d, ox=-60, oy=0, scale=1.0)

    # stroke 4: 丁 heng (slightly rising left→right)
    draw_heng(d, head=(142, 151), tail=(269, 140),
              width_head=9, width_tail=10)

    # stroke 5: 丁 shu_gou (vertical with left hook flick)
    # Head lowered from MMH-raw 153 → 165 to yield the ~20 px N gap
    # under the s4 heng midpoint (heng y ≈ 146 at x=195 → gap ≈ 19 px).
    draw_shu_gou(d, head=(195, 165), tail=(164, 281),
                 width=7, hook_start_offset=30)

    img.save(path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_打.png")
    render(out)
    print(f"wrote {out}")
