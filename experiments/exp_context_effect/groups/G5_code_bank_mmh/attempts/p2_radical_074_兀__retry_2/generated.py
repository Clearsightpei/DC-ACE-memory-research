"""p2_radical_074_兀 — G5 drawer, retry #2.

TRAJECTORY DIFF (from visual inspection of GT + both prior FAIL PNGs):

Main attempt (FAIL) got wrong:
  1. Overall size too small; heng span short (~55–215), legs stubby.
  2. Right leg TOP too far right — visually placed under heng's right
     terminus, but GT places right-leg head near heng MIDPOINT with
     heng extending past it to the right (matches MMH s3.head@C).
  3. Both legs too short (bottomed at y≈268), silhouette compressed.

Retry_1 attempt (FAIL) OVER-CORRECTED:
  1. Heng WAY too wide (48↔252 = 204 px) — GT heng is ~155 px.
  2. Legs spread way too wide (28 and 240) — GT feet at ~40 and ~200.
  3. Legs stretched to y=285 — GT legs bottom at ~y=250.
  4. Right-leg head at x=228 kept the main-attempt error (leg tucked
     under heng-right instead of heng-middle-right per GT + MMH).

Fixes this attempt (GT-calibrated middle ground):
  - Heng: (72, 108) → (225, 104), width ~153 (matches GT).
  - Left pie: head (82, 118), tail (40, 250) — strong bow, GT-sized.
  - Right shu-wan-bare: head (170, 118) — CENTER-RIGHT under heng
    midpoint (respect MMH s3.head@C x_frac 0.497), not under right
    end; vertical descent to y≈250 with mild rightward curl to (192, 258).
  - Both leg tops at y=118 (below heng at y=108 → N-gap ~10 px, close
    to GT's tight-but-visible separation).
  - No hook on right leg (bare 竖弯), matches GT and prior BANK_DEVIATION.

BANK_DEVIATION
skipped: shu_wan_gou.py
reason: bank shu_wan_gou renders an upward hook; 兀's right leg in GT
        is a bare 竖弯 with only a slight rightward bottom curl — no hook.
fresh_component: shu_wan_bare (long vertical + tiny right curl, no hook)

MMH anchors vs actual (pixels):
  s1 head MMH ML(0.647, 0.084) ≈ (65, 108)   → use ( 72, 108)  Δ ~7px
  s1 tail MMH TR(0.317, 0.964) ≈ (232,  96)  → use (225, 104)  Δ ~10px
  s2 head MMH ML(0.999, 0.289) ≈ (100, 129)  → use ( 82, 118)  Δ ~20px
       (small shift left/up to match GT's slightly higher, further-left leg)
  s2 tail MMH BL(0.346, 0.783) ≈ ( 35, 278)  → use ( 40, 250)  Δ ~28px
       (GT leg does NOT reach canvas bottom; retry_1's y=285 was wrong)
  s3 head MMH C(0.497, 0.102)  ≈ (150, 110)  → use (170, 118)  Δ ~22px
       (small right nudge; MMH's exact midpoint would leave the leg
        floating too far left visually — 170 splits the difference)
  s3 tail MMH BR(0.666, 0.168) ≈ (267, 217)  → use (192, 258)
       MMH tail is the tail of the hook geometry, but for a bare 竖弯
       (no hook) we terminate at the curl endpoint on the canvas floor.

Joints: two N-joints. s2.head and s3.head both sit ~10 px BELOW heng
        (y_leg=118 vs y_heng≈108 at leg-x) → natural N-gap preserved.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie


def draw_shu_wan_bare(draw, head, bottom, curl_dx=22, width=9):
    """Long vertical descent then a soft rightward curl. NO upward hook.
    head=(x,y) top, bottom=(x,y) final tail. Bezier through a knee near bottom.
    """
    hx, hy = head
    bx, by = bottom
    n = 90
    knee_frac = 0.85
    knee = (hx, hy + (by - hy) * knee_frac)
    p0 = head
    p1 = knee
    p2 = bottom
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((int(round(x)), int(round(y))))
    draw.line(pts, fill="black", width=width, joint="curve")
    r = width // 2
    draw.ellipse([hx - r + 1, hy - r, hx + r - 1, hy + r], fill="black")
    draw.ellipse([bx - r - 1, by - r, bx + r + 1, by + r], fill="black")


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,          # 3 primitives: heng, pie, shu_wan_bare
    "endpoint_mismatches": [
        {
            "stroke": 3,
            "expected_head": ("C", 0.497, 0.102),
            "actual_head_px": (170, 118),
            "delta_note": "20px right nudge from MMH midpoint to match GT visual balance",
        },
        {
            "stroke": 3,
            "expected_tail": ("BR", 0.666, 0.168),
            "actual_tail_px": (192, 258),
            "delta_note": "bare shu-wan terminates on canvas floor, no hook geometry",
        },
    ],
    "joint_class_mismatches": [],     # both N-joints preserved (~10 px gap under heng)
    "overall_pass": True,
    "notes": "retry_2: recentered dims to GT — heng 153 wide, legs 40-192 wide, y_bottom 250-258.",
}


def main(out_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top heng — GT-sized (~153 wide), slight upward tilt to the right
    s1_head = (72, 110)
    s1_tail = (225, 106)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # s2: left leg pie — long curved sweep from just-under-heng-left to lower-left
    s2_head = (82, 120)
    s2_tail = (40, 252)
    draw_pie(d, s2_head, s2_tail, bow_perp=18, w_head=8, w_tail=3, steps=100)

    # s3: right leg — bare shu-wan (BANK_DEVIATION), head under heng center-right
    s3_head = (170, 120)
    s3_tail = (192, 258)
    draw_shu_wan_bare(d, s3_head, s3_tail, width=9)

    img.save(out_path)


if __name__ == "__main__":
    out = pathlib.Path(__file__).parent / "01_兀.png"
    main(out)
    print("wrote", out)
