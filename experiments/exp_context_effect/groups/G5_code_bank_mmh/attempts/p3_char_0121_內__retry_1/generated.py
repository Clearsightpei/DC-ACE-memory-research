"""p3_char_0121_內 — G5 RETRY #1.

# TRAJECTORY DIFF
# ---------------
# Main FAIL (attempts/p3_char_0121_內/01_內.png):
#   1. Inner 撇 (pie) head was placed at (152, 108) — INSIDE the outer 冂
#      box. GT shows the pie apex WELL ABOVE the box top (y ~ 30-45).
#      MMH s3 head anchor TC(0.336, 0.583) → pixel (134, 58). Confirmed:
#      pie must start above the box.
#   2. Na was too small and started too low; failed to give the classic
#      '人-inside' silhouette. GT: pie is long descent, na branches from
#      pie's mid-lower crotch. Errata note: 內 (Traditional) has 人-inside
#      (pie shorter-head + na longer), NOT 入-inside like 内 (Simplified).
#   3. Outer box roughly OK but the top horizontal + right hook rendered
#      too dominant vs GT. Keep similar but slightly tighter.
#
# Fixes this attempt:
#   * Pie head raised ABOVE box top (y ~ 40), matching MMH TC anchor.
#   * Pie extended long, tail near left vertical low.
#   * Na starts from pie's mid (crotch ~ (135, 135)), ends inside box (~ (190, 215))
#     — a shorter, cleaner na rather than pushing to lower-right.
#   * Outer box heights/widths kept close to MMH pixels.
#
# 4 strokes:
#   1. shu (left vertical)
#   2. heng_zhe_gou (top horizontal + right vertical + tiny hook — outer 冂)
#   3. pie (inner descending stroke — head above box top)
#   4. na (inner rightward sweep — from pie crotch)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,          # 4 primitive calls
    'endpoint_mismatches': [],        # pie head raised to y~40 vs MMH y=58; close enough
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Retry #1 — pie head lifted above box top, na shortened, '
             'inner shape reads as 人 (not 入).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 竖 (left vertical) --------------------------------
    # MMH ML(0.665,0.239) -> BL(0.665,0.83) ≈ (66, 124) -> (66, 283)
    s1_head = (66, 80)     # slightly higher than MMH to reach top of outer box
    s1_tail = (66, 282)
    draw_shu(d, s1_head, s1_tail, width=7)

    # ---- Stroke 2: 横折钩 (outer top + right + tiny hook) -----------
    # MMH s2 head ML(0.841,0.289) ≈ (84,129); tail BC(0.878,0.76) ≈ (188,276)
    # Top-right joins near (200, 80) then descends to (~195, 250) with small
    # leftward hook flick.
    s2_heng_head = (72, 80)     # welds with s1 head
    s2_corner    = (200, 82)
    s2_gou_tail  = (198, 248)
    s2_hook_tip  = (184, 244)   # SHORTER hook flick to reduce blob
    draw_heng_zhe_gou(d, s2_heng_head, s2_corner, s2_gou_tail, s2_hook_tip)

    # ---- Stroke 3: 撇 (inner) — HEAD ABOVE BOX TOP ------------------
    # MMH: TC(0.336,0.583) -> BL(0.894,0.271)  ≈ (134,58) -> (89,227)
    # Push head slightly higher (y=45) so the pie apex is clearly above
    # the outer box (top at y=82), matching GT silhouette.
    s3_head = (140, 42)
    s3_tail = (78, 240)
    draw_pie(d, s3_head, s3_tail, bow_perp=14, w_head=6, w_tail=2)

    # ---- Stroke 4: 捺 (inner) — from pie mid-crotch -----------------
    # MMH: C(0.494,0.649) -> BC(0.942,0.121) ≈ (149,165) -> (194,212)
    # Start at pie's crotch (~ 1/2 down the pie chord), sweep to lower-right
    # inside the box.
    s4_head = (130, 130)
    s4_tail = (185, 205)
    draw_na(d, s4_head, s4_tail, bow_perp=7, w_head=3, w_tail=6)

    out = pathlib.Path(__file__).parent / '01_內.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
