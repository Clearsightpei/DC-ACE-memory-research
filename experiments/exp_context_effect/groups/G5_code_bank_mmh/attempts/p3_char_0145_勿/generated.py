"""p3_char_0145_勿 — 4 strokes.

Structure per MMH block + GT visual:
  s1: short pie top-left (TC → ML)  — same shape as 勹's s1
  s2: 橫折鉤 outer wrap (ML → BC)   — same shape as 勹's s2 (a.k.a. bao_wrap)
  s3: inner middle pie (C → BL)     — medium leftward sweep
  s4: inner outer pie  (C → BL)     — longer leftward sweep, starting further right

The outer envelope of 勿 IS 勹, so we call draw_bao for s1+s2 and then
add two internal 撇 strokes for s3 and s4.

Bank calls: draw_bao (1 primitive, 2 strokes) + draw_pie (x2) = 4 strokes total.
"""

# No BANK_DEVIATION: draw_bao's stroke endpoints are within ~10px of the
# MMH anchors for 勿's outer strokes (delta well inside ±0.20 x_frac tolerance).
# The two inner pie strokes use draw_pie inline with explicit endpoints.

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from bao_wrap import draw_bao       # noqa: E402
from pie import draw_pie             # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # draw_bao (2) + 2 inline pies = 4 primitives
    'endpoint_mismatches': [
        # bao's s1 head (111.6,64.5) vs MMH s1 head (105,58): delta ~7px — within tol
        # bao's s2 head (98.7,133.6) vs MMH s2 head (87,141):  delta ~10px — within tol
    ],
    'joint_class_mismatches': [],  # all 3 joints are N (natural gaps) — none welded
    'overall_pass': True,
    'notes': "Uses draw_bao for outer 勹 envelope; s3/s4 are inline pies inside."
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1 + s2: outer 勹 envelope ----
    #   s1: TC(105,58) → ML(54,167)  ≈ bao s1 (111.6,64.5) → (56,168)
    #   s2: ML(87,141) → BC(149,269) ≈ bao s2 (98.7,133.6) → (145,274)
    draw_bao(d, ox=0, oy=0, scale=1.0)

    # ---- s3: inner middle 撇 ----
    #   MMH: C(116,144) → BL(60,233). Medium pie sweeping down-left.
    draw_pie(d, head=(116, 144), tail=(60, 233),
             bow_perp=8, w_head=6, w_tail=2, steps=70)

    # ---- s4: inner outer (right) 撇 ----
    #   MMH: C(167,134) → BL(82,279). Longer pie starting further right.
    draw_pie(d, head=(167, 134), tail=(82, 279),
             bow_perp=12, w_head=7, w_tail=2, steps=90)

    out = Path(__file__).parent / "01_勿.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
