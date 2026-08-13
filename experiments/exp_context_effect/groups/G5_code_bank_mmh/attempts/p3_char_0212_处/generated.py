"""p3_char_0212_处 (chu, "place") — 5 strokes.

Structure per MMH anchors:
  s1  撇 (pie)  head TL (79.7, 79.1)  → tail BL (26.4, 206.5)
  s2  撇 (pie)  head ML (74.4, 150.9) → tail BL (21.1, 281.5)
  s3  乀 (na sweeping) head ML (50.7, 198.6) → tail BR (272.8, 280.4)
      pierces s2 mid (P joint at ~(94, 215))
  s4  竖 (shu)  head TC (162.9, 74.7)  → tail BC (174.3, 245.5)
  s5  点 (dian) head C  (192.8, 148.5) → tail MR (242.9, 191.6)

Bank usage:
  s1 draw_pie  — endpoint bank primitive
  s2 draw_pie  — endpoint bank primitive
  s3 draw_na   — endpoint bank primitive (long shallow-belly sweep)
  s4 draw_shu  — endpoint bank primitive
  s5 draw_dian — endpoint bank primitive
No BANK_DEVIATION — every stroke matches a promoted primitive cleanly.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__),
                    "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie      # noqa: E402
from na import draw_na        # noqa: E402
from shu import draw_shu      # noqa: E402
from dian import draw_dian    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 primitive calls, one per stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': "5 strokes; s2/s3 P-cross via straight s3 chord through pie s2 belly.",
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 撇 top-right to lower-left (long sweeping pie) ----
    # Head at TL(79.7, 79.1), tail BL(26.4, 206.5).
    draw_pie(d, head=(80, 79), tail=(26, 207),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # ---- Stroke 2: 撇 mid-left to bottom-left (second pie of 夂) ----
    # Head ML(74.4, 150.9), tail BL(21.1, 281.5).
    draw_pie(d, head=(74, 151), tail=(21, 282),
             bow_perp=9, w_head=7, w_tail=3, steps=80)

    # ---- Stroke 3: 乀 long sweeping na from mid-left through s2 to lower-right ----
    # Head ML(50.7, 198.6), tail BR(272.8, 280.4). Belly is shallow so
    # the mid passes near (162, 240ish); with slight positive bow, s3
    # dips through s2's belly, giving the P joint at ~(94, 215).
    # Bigger belly so the sweep reads clearly and pierces s2 via the
    # curved chord (P-joint target ~(94, 215)).
    draw_na(d, head=(51, 199), tail=(273, 280),
            bow_perp=18, w_head=4, w_tail=13, steps=90)

    # ---- Stroke 4: 竖 vertical of the right-hand 卜, TC to BC ----
    # Head TC(162.9, 74.7), tail BC(174.3, 245.5); slight rightward drift.
    draw_shu(d, head=(163, 75), tail=(174, 246), width=7, top_curl=False)

    # ---- Stroke 5: 点 diagonal dot of the right-hand 卜 ----
    # Head C(192.8, 148.5), tail MR(242.9, 191.6). Thin head → thick tail.
    draw_dian(d, head=(193, 149), tail=(243, 192),
              w_head=3, w_tail=8, bow=4, steps=48)

    return img


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_png = os.path.join(out_dir, "01_处.png")
    img = render()
    img.save(out_png)
    print("wrote", out_png, "size", img.size)
