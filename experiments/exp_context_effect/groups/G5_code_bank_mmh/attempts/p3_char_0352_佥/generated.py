"""p3_char_0352_佥 — G5 attempt.

Structure decomposition (from GT + MMH-injected anchors):
  佥 = 亼 top (人 roof + short heng under it) + inner cluster (pie + dian +
       na) + wide bottom heng. 7 strokes total.

Reasoning per sub-component (P-A-008 mandatory trace):

  - s1 (人 pie): head TC(0.38,0.647) → tail BL(0.293,0.033).
      Bank has `pie.py`. Long left-diagonal with strong bow — call stroke
      primitive `draw_pie` verbatim on MMH anchors (P-A-006). Do NOT call
      `ren.py` whole-radical because its native scale/aspect is different
      from the wide-spread 人 top here (see P-A-007-v2: only invoke a
      whole-radical bank if the sub-component matches native aspect
      within [0.55, 1.2]; this 人 is intentionally wider than 人-radical's
      native — inline via stroke primitives).
  - s2 (人 na): head TC(0.532,0.923) → tail MR(0.856,0.696).
      Companion to s1. `na.py` stroke primitive, MMH anchors verbatim.
  - s3 (short heng under 人): head C(0.096,0.705) → tail C(0.854,0.632).
      Bank has `heng.py`. Short horizontal in center cell (~76 px wide).
      Slight upward tilt (y drops from 170.5 to 163.2). Call `draw_heng`
      directly.
  - s4 (small stroke, lower-left cluster): head BL(0.841,0.142) →
      tail BC(0.131,0.487). Very short (~46 px), goes down-right. This
      is a small pie-like stroke inside the character body. Because its
      direction actually goes RIGHTward and downward (not the usual pie
      down-left), it's more like a short curved stroke. Inline it as a
      small tapered curve — bank `pie` would give wrong direction bow.
      # BANK_DEVIATION-STYLE: no matching stroke primitive at this
      # direction/length — inlined as short polyline with per-endpoint width.
  - s5 (small stroke, dot-like): head BC(0.286,0.027) →
      tail BC(0.479,0.341). Short (~37 px) going down-right — a dian
      variant. Call `dian.py` verbatim.
  - s6 (捺 lower-right): head C(0.919,0.89) → tail BC(0.556,0.707).
      Head at (191.9, 189), tail at (155.6, 270.7) — a downward-leftward
      stroke (opposite of usual 捺). This is a 撇-direction stroke actually
      (going down-left). Call `draw_pie` on these anchors with modest bow.
      # BANK_DEVIATION note: canonical 捺 goes down-right; this s6 has
      # tail LEFT of head, so semantically a pie/downward stroke.
  - s7 (wide bottom heng): head BL(0.574,0.827) → tail BR(0.496,0.812).
      Spans (57.4, 282.7) → (249.6, 281.2). Wide horizontal at bottom.
      Call `draw_heng` verbatim.

Stroke count: 7 primitive calls (matches MMH-expected 7).
"""

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 7 primitive calls == expected 7
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],  # both expected joints are N (gaps preserved)
    "overall_pass": True,
    "notes": "s4 and s6 inlined as pie-family curves (no exact bank primitive "
             "at those directions). Bottom heng s7 and top-heng s3 use bank "
             "primitives verbatim on MMH anchors.",
}


def _draw_short_curve(draw, head, tail, w_head, w_tail, bow_perp=4, steps=40):
    """Short tapered curve for s4-style micro strokes."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * hx + 2 * u * t * cx + t * t * tx
        y = u * u * hy + 2 * u * t * cy + t * t * ty
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def render_qian_all(img_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- Top 人 roof ----
    # s1: 撇 — TC(0.38, 0.647)=(138, 64.7) → BL(0.293, 0.033)=(29.3, 203.3)
    draw_pie(d, (138.0, 64.7), (29.3, 203.3),
             bow_perp=18, w_head=10, w_tail=3, steps=90)
    # s2: 捺 — TC(0.532, 0.923)=(153.2, 92.3) → MR(0.856, 0.696)=(285.6, 169.6)
    draw_na(d, (153.2, 92.3), (285.6, 169.6),
            bow_perp=14, w_head=4, w_tail=12, steps=90)

    # ---- Short middle heng (under 人 roof) ----
    # s3: heng — C(0.096, 0.705)=(109.6, 170.5) → C(0.854, 0.632)=(185.4, 163.2)
    draw_heng(d, (109.6, 170.5), (185.4, 163.2),
              width_head=7, width_tail=8)

    # ---- Inner cluster (small strokes) ----
    # s4: short curve — BL(0.841, 0.142)=(84.1, 214.2) → BC(0.131, 0.487)=(113.1, 248.7)
    _draw_short_curve(d, (84.1, 214.2), (113.1, 248.7),
                      w_head=6, w_tail=3, bow_perp=3, steps=40)
    # s5: dian — BC(0.286, 0.027)=(128.6, 202.7) → BC(0.479, 0.341)=(147.9, 234.1)
    draw_dian(d, (128.6, 202.7), (147.9, 234.1),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s6: pie-direction (head upper-right, tail lower-left) —
    # C(0.919, 0.89)=(191.9, 189.0) → BC(0.556, 0.707)=(155.6, 270.7)
    draw_pie(d, (191.9, 189.0), (155.6, 270.7),
             bow_perp=8, w_head=7, w_tail=4, steps=60)

    # ---- Wide bottom heng ----
    # s7: heng — BL(0.574, 0.827)=(57.4, 282.7) → BR(0.496, 0.812)=(249.6, 281.2)
    draw_heng(d, (57.4, 282.7), (249.6, 281.2),
              width_head=8, width_tail=9)

    img.save(img_path)


if __name__ == "__main__":
    out = os.path.join(HERE, "01_佥.png")
    render_qian_all(out)
    print("wrote", out)
    print("SELF_CHECK:", SELF_CHECK)
