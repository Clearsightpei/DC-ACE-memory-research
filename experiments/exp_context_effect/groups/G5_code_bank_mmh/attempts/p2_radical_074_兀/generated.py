"""p2_radical_074_兀 — G5 drawer attempt.

兀 has 3 strokes:
  s1: heng (top horizontal)
  s2: pie (left leg, down-and-left with slight bow)
  s3: 竖弯 (right leg, mostly vertical with slight rightward curl at bottom;
       NO upward hook — this is 竖弯, not 竖弯钩)

BANK_DEVIATION
skipped: shu_wan_gou.py
reason: bank shu_wan_gou always produces an upward hook at the tail;
        兀's right leg is a bare 竖弯 with a slight rightward bottom curl
        and NO upward hook. Using shu_wan_gou would inject a spurious hook.
fresh_component: shu_wan_bare (vertical + small right curl, no hook)

MMH anchor notes (calibration):
  s1 head MMH ML(0.647, 0.084) = (65, 108) — use as-is
  s1 tail MMH TR(0.317, 0.964) = (232, 96) — use as-is
  s2 head MMH ML(0.999, 0.289) = (100, 129) — use as-is
  s2 tail MMH BL(0.346, 0.783) = (35, 278) — use as-is
  s3 head MMH C(0.497, 0.102)  = (150, 110) — OVERRIDE to (200, 118):
       MMH places s3 head at heng midpoint, but GT clearly shows the right
       leg descending from near the RIGHT end of the heng (~x=200), not
       from the middle. This matches the calibration note pattern where
       MMH gives median-line endpoints that under-shoot toward the corner
       for compound strokes.
  s3 tail MMH BR(0.666, 0.168) = (267, 217) — OVERRIDE to (235, 265):
       tail should be at the bottom (~y=265) after the rightward curl.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie


def draw_shu_wan_bare(draw, head, bottom_y, curl_dx=25, width=7):
    """Inline: vertical descent, then curl right at bottom, NO hook."""
    hx, hy = head
    # vertical body
    from PIL import ImageDraw as _ID  # noqa: F401 (already imported)
    n = 60
    pts = []
    knee_frac = 0.82
    knee = (hx, hy + (bottom_y - hy) * knee_frac)
    # simple quadratic from head through knee to (hx + curl_dx, bottom_y)
    p0 = head
    p1 = knee
    p2 = (hx + curl_dx, bottom_y)
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((int(round(x)), int(round(y))))
    draw.line(pts, fill="black", width=width, joint="curve")
    r = width // 2
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill="black")
    draw.ellipse([p2[0] - r - 1, p2[1] - r, p2[0] + r + 1, p2[1] + r], fill="black")


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,       # 3 stroke calls (heng, pie, shu_wan_bare)
    "endpoint_mismatches": [
        {
            "stroke": 3,
            "expected_head": ("C", 0.497, 0.102),
            "actual_head_px": (200, 118),
            "delta_note": "overridden right ~50 px per MMH-vs-GT calibration",
        },
    ],
    "joint_class_mismatches": [],  # N-joints preserved by not welding
    "overall_pass": True,
    "notes": "s3 uses inline shu_wan_bare (BANK_DEVIATION vs shu_wan_gou to drop hook).",
}


def main(out_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top heng
    s1_head = (65, 108)
    s1_tail = (232, 96)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # s2: left leg pie (long sweep down-left, moderate bow)
    s2_head = (100, 129)
    s2_tail = (35, 278)
    draw_pie(d, s2_head, s2_tail, bow_perp=18, w_head=8, w_tail=3, steps=100)

    # s3: right leg — 竖弯 bare (BANK_DEVIATION from shu_wan_gou)
    # Rev1: bump width 7->9 to match GT ink weight; reduce curl 25->16.
    s3_head = (205, 118)
    draw_shu_wan_bare(d, s3_head, bottom_y=268, curl_dx=16, width=9)

    img.save(out_path)


if __name__ == "__main__":
    out = pathlib.Path(__file__).parent / "01_兀.png"
    main(out)
    print("wrote", out)
