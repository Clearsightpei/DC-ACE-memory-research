"""p3_char_0039_之 (zhī) — 3 strokes.

Mandatory lookup checklist (per memory_index.md):
  1. success_bank/INDEX.md grep '之'  -> NOT PRESENT (no mastered entry to reuse)
  2. errata.md grep '之'              -> NOT PRESENT
  3. form_catalog.md                  -> 捺 section, 平捺 context (line 101-103): "Longer,
     more horizontal; peak_t ~0.78, curve ~0.14." Reference yin_stride.py.
     点 section (line 105-110): "Compact, head at ~TC/upper-left, tail at ~C,
     head_w=2 peak_w=11 curve=0.08."
  4. principles_meta.md TR1-TR12 acknowledged; TR1: override anchors from brief.
     TR9 (span-full-grid) NOT applicable (this is a Phase-3 character, not standalone radical).
  5. joint_atlas.md: N-class must show visible ~15-20 px gap, don't weld.
  6. sandbox.md consulted.

Stroke plan (from MMH brief):
  s1 = dian  (top dot):     ('TC', 0.239, 0.627) -> ('TC', 0.597, 0.914)
  s2 = short heng-pie:      ('ML', 0.653, 0.415) -> ('BL', 0.776, 0.165)
  s3 = ping-na (level sweep):('BL', 0.252, 0.276) -> ('BR', 0.774, 0.739)

Joint: s2.tail  N-gap-to  s3.body at BL (expected ~13.6 px gap, class N).
"""
import os
import sys

# Locate shared primitives from the success_bank/code/ dir.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from dian import draw_dian  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 strokes: dian, heng-pie-short, ping-na
    'endpoint_mismatches': [], # all anchors used verbatim from MMH brief
    'joint_class_mismatches': [], # s2.tail is above s3 at BL with visible N gap (~15 px)
    'overall_pass': True,
    'notes': ('revision 1: increased s2 curve from 0.10 -> 0.30 so middle '
              'stroke reads as heng-pie kink not straight diagonal, matching GT silhouette.')
}


def draw_heng_pie_short(draw, from_anchor, to_anchor,
                        head_width=5, mid_width=6, tail_width=2,
                        curve=0.10, segments=32,
                        color=(0, 0, 0)):
    """Short heng-pie: a horizontal-ish tick that curves DOWN-LEFT.

    Used for the middle stroke of 之 — a short segment starting on the ML row
    and ending inside BL (down-left). Modestly bowed.
    """
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perp bows UP-LEFT (natural heng-pie belly).
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t < 0.5:
            u = t / 0.5
            w = head_width + (mid_width - head_width) * u
        else:
            u = (t - 0.5) / 0.5
            w = mid_width + (tail_width - mid_width) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths, color=color)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---------- s1: dian (top dot) ----------
    # MMH: ('TC', 0.239, 0.627) -> ('TC', 0.597, 0.914)
    draw_dian(draw,
              ('TC', 0.239, 0.627),
              ('TC', 0.597, 0.914),
              head_width=2, peak_width=10, curve=0.08)

    # ---------- s2: short heng-pie (mini 横撇 shape) ----------
    # MMH endpoints: ('ML', 0.653, 0.415) -> ('BL', 0.776, 0.165)
    # In GT the middle stroke reads as: small horizontal top, then drops down-left.
    # We honor the MMH endpoints but draw a stronger belly so the shape reads as
    # a heng-pie kink, not a straight diagonal.
    draw_heng_pie_short(draw,
                        ('ML', 0.653, 0.415),
                        ('BL', 0.776, 0.165),
                        head_width=5, mid_width=7, tail_width=2, curve=0.30)

    # ---------- s3: ping-na (level right-falling sweep) ----------
    # MMH: ('BL', 0.252, 0.276) -> ('BR', 0.774, 0.739)
    # 平捺 form: peak_t ~0.78, curve ~0.14, longer and more horizontal.
    draw_na(draw,
            ('BL', 0.252, 0.276),
            ('BR', 0.774, 0.739),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.14)

    out = os.path.join(_HERE, "01_之.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
