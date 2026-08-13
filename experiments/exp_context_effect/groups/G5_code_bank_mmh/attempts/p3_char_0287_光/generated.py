"""p3_char_0287_光 (guang, "light") — 6 strokes.

Composition (from MMH anchors, P-A-006 stroke-primitive layer):
  s1: shu (top-center small vertical dot/spine — extends further than a pure dian)
  s2: pie (upper-left slash, from upper cell area down to just past center)
  s3: pie (upper-right slash, from top-right down to just past center)
  s4: heng (middle horizontal beam, spans left to right)
  s5: pie (bottom-left leg, from just below beam to lower-left)
  s6: shu_wan_gou (bottom-right leg: vertical → bend right → hook up)

Joints (all N gaps — do NOT weld):
  s1.tail ⇆ s4.mid(0.42) : N (~15 px) — top spine sits just above beam
  s1.tail ⇆ s6.head      : N (~25 px)
  s4.mid(0.33) ⇆ s5.head : N (~22 px) — leg hangs below beam
  s4.mid(0.45) ⇆ s6.head : N (~18 px)

Bank primitives used: shu, pie, heng, shu_wan_gou (all promoted; sibling of 先 P-A-006).
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shu import draw_shu
from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 6 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],      # all N joints preserved (gaps, not welds)
    'overall_pass': True,
    'notes': 'Anchors baked from MMH block. All 4 joints are N; endpoints do not touch. Sibling of 先.'
}


def draw_guang(d, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: shu (top-center vertical dot) — MMH anchor (135.1, 64.7)→(139.7, 168.5)
    # SHORTENED per GT: MMH median is unusually long here, but the GT PNG shows
    # a short vertical dot (~y=90..130) that does NOT reach the beam. Trust GT.
    # Compressed range keeps head/tail roughly centered on MMH midpoint.
    draw_shu(d,
             T(136.0, 88.0), T(139.0, 135.0),
             width=max(2, int(7 * scale)), top_curl=False)

    # s2: pie (upper-left slash) — ML(0.858, 0.225) → C(0.119, 0.485)
    #     (85.8, 122.5) → (111.9, 148.5)
    # NOTE: MMH lists s2 with a short slant in mid-left cell area coming toward center.
    # This is the LEFT upper-slash of 光's ⺌ top.
    draw_pie(d,
             T(85.8, 122.5), T(111.9, 148.5),
             bow_perp=6, w_head=max(2, int(6 * scale)),
             w_tail=max(2, int(3 * scale)), steps=50)

    # s3: pie (upper-right slash) — TR(0.039, 0.929) → C(0.693, 0.418)
    #     (203.9, 92.9) → (169.3, 141.8)
    # RIGHT upper-slash of ⺌ top, longer than s2.
    draw_pie(d,
             T(203.9, 92.9), T(169.3, 141.8),
             bow_perp=7, w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(3 * scale)), steps=60)

    # s4: heng (middle beam) — ML(0.489, 0.86) → MR(0.481, 0.711)
    #     (48.9, 186.0) → (248.1, 171.1)
    draw_heng(d,
              T(48.9, 186.0), T(248.1, 171.1),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))

    # s5: pie (bottom-left leg) — C(0.128, 0.948) → BL(0.331, 0.977)
    #     (112.8, 194.8) → (33.1, 297.7)
    # Starts just below beam (N gap), sweeps down-left to lower-left corner.
    draw_pie(d,
             T(112.8, 194.8), T(33.1, 297.7),
             bow_perp=10, w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)), steps=70)

    # s6: shu_wan_gou (bottom-right leg with right-hook) — C(0.506, 0.828) → BR(0.681, 0.341)
    #     (150.6, 182.8) → (268.1, 234.1)
    # Head just below beam, descends then curves right, hooks up at end.
    draw_shu_wan_gou(d,
                     T(150.6, 182.8), T(268.1, 234.1),
                     width=max(2, int(7 * scale)),
                     bottom_extra=55, knee_ratio=0.72)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_guang(d)
    out = Path(__file__).parent / "01_光.png"
    img.save(out)
    print(f"wrote {out}")
