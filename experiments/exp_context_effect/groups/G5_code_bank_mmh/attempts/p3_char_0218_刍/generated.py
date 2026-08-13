"""p3_char_0218_刍 (chu, "fodder/grass").

Structure: ⺈-like top (pie + inner short stroke) + 彐-like bottom
(top-right heng-zhe + middle heng + bottom long heng). 5 strokes total.

Using bank primitives where fits; heng-zhe for s3 uses heng_zhe_box
(only top+right sides, no bottom — perfect fit).
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from dian import draw_dian
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


# ---- Anchors → pixels on 300×300 canvas (米字格 9 cells, each 100×100) ----
def A(cell, xf, yf):
    cx = {"TL": 0, "TC": 100, "TR": 200,
          "ML": 0, "C": 100, "MR": 200,
          "BL": 0, "BC": 100, "BR": 200}[cell]
    cy = {"TL": 0, "TC": 0, "TR": 0,
          "ML": 100, "C": 100, "MR": 100,
          "BL": 200, "BC": 200, "BR": 200}[cell]
    return (cx + xf * 100, cy + yf * 100)


# MMH endpoints
s1_head = A("TC", 0.365, 0.609)   # (137, 61)
s1_tail = A("ML", 0.706, 0.453)   # (71, 145)
s2_head = A("C", 0.254, 0.096)    # (125, 110)
s2_tail = A("C", 0.491, 0.623)    # (149, 162)
s3_head = A("ML", 0.674, 0.767)   # (67, 177)
s3_tail = A("BC", 0.942, 0.555)   # (194, 256)
s4_head = A("BL", 0.712, 0.247)   # (71, 225)
s4_tail = A("BC", 0.866, 0.177)   # (187, 218)
s5_head = A("BL", 0.712, 0.766)   # (71, 277)
s5_tail = A("BR", 0.188, 0.71)    # (219, 271)


img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# s1: main pie stroke — top-center descending down-left
draw_pie(d, s1_head, s1_tail, bow_perp=8, w_head=8, w_tail=3, steps=80)

# s2: short inner stroke — like a small pie/dian
draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=7, bow=3, steps=48)

# s3: top-right heng-zhe of 彐 (horizontal from s3_head then turns down to s3_tail)
# heng_zhe_box takes (top_left, bottom_right): horizontal then vertical drop
draw_heng_zhe_box(d, s3_head, s3_tail, width=7)

# s4: middle short heng inside 彐
draw_heng(d, s4_head, s4_tail, width_head=7, width_tail=8)

# s5: bottom long heng — the base of 彐
draw_heng(d, s5_head, s5_tail, width_head=8, width_tail=9)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 primitive calls (pie, dian, heng_zhe_box, heng, heng)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all four joints are N (neighbor) — no welding used
    'overall_pass': True,
    'notes': '5 strokes drawn as separate calls with natural neighbor gaps '
             '(no explicit welding). heng_zhe_box provides the top+right of 彐; '
             's4/s5 are drawn as independent hengs; s1 pie + s2 dian form the ⺈ top.'
}


if __name__ == "__main__":
    out = Path(__file__).parent / "01_刍.png"
    img.save(out)
    print(f"Wrote {out}")
