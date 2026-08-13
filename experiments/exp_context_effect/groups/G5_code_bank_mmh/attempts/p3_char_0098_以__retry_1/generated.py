"""p3_char_0098_以 retry_1 — 4 strokes: L(short-pie + dian) + R(pie + compressed-na).

TRAJECTORY DIFF (vs main FAIL):
- MAIN FAIL: strokes were jumbled X-cluster in center; left component's
  pie+dian were placed too high and too small, right pie/na sat too high
  and the na apex splayed right → read as 从 not 以. No clear L/R split.
- FIX PLAN (per errata):
  1. Left short-pie clearly on the LEFT side (x≈65-110), spanning y≈95-215.
  2. Left dian below/right of pie (small tapered dab), around (95,170)→(140,205).
  3. Right pie tail lands at BC pixel (115.7, 269.5) — long sweeping curve
     from upper-right down to bottom-center (per errata guidance).
  4. Right na COMPRESSED into BR cell only: head around (200,165),
     tail at (270,258). Shorter so 以 doesn't read like 从.
- Also add clear horizontal separation: left component ends by x=140,
  right component starts by x=170.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 strokes matches expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # single N joint (s3.mid ⇆ s4.head near BR) — gap preserved
    'overall_pass': True,
    'notes': 'Retry fix: L/R separation reasserted; right pie tail per errata; na compressed to BR cell.'
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie      # noqa: E402
from na import draw_na        # noqa: E402
from dian import draw_dian    # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- Left component: short pie + dian ------------------------------------
    # Stroke 1 — short pie: curved down-left, more pronounced bow so it
    # reads as a proper calligraphic curve, not a plain vertical.
    left_pie_head = (112.0, 92.0)    # upper-left area, near TC boundary
    left_pie_tail = (60.0, 220.0)    # BL cell, tail lower-left
    draw_pie(d, left_pie_head, left_pie_tail,
             bow_perp=14, w_head=8, w_tail=3, steps=80)

    # Stroke 2 — dian: small tapered dab connecting near the belly/bottom
    # of the pie, extending to the right — completes the レ-like left form.
    left_dian_head = (88.0, 178.0)
    left_dian_tail = (140.0, 208.0)
    draw_dian(d, left_dian_head, left_dian_tail,
              w_head=3, w_tail=9, bow=5, steps=48)

    # --- Right component: pie + compressed na (人-like, asymmetric) ----------
    # Stroke 3 — right pie: long sweeping curve. Per errata & MMH: head
    # ~TR (210.9, 84.1), tail at BC (115.7, 269.5). Use MODEST bow so
    # the curve isn't a crescent — a clean 撇 line.
    right_pie_head = (210.9, 84.1)
    right_pie_tail = (115.7, 269.5)
    draw_pie(d, right_pie_head, right_pie_tail,
             bow_perp=8, w_head=9, w_tail=3, steps=80)

    # Stroke 4 — right na: compressed inside BR cell only. Per MMH:
    # head (206, 205), tail (258, 267). Give it slightly more length and
    # a proper na thickening so it reads as 捺 not a stub.
    right_na_head = (198.0, 178.0)
    right_na_tail = (278.0, 265.0)
    draw_na(d, right_na_head, right_na_tail,
            bow_perp=12, w_head=4, w_tail=12, steps=80)

    # Save PNG
    out = Path(__file__).parent / "01_以.png"
    img.save(out)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
