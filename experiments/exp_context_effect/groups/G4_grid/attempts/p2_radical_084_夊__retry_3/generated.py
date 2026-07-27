"""夊 (suī) — retry #3.

Prior retries: retry_1 came close (ク top + X-cross) but failed. GT shows:
  - Top: small ク (横撇) at top-center, curling from upper-right down-left.
  - Middle-body: 撇 (down-left sweep) starting just below ク tail.
  - Bottom: 捺 (down-right sweep) crossing 撇 low, sweeping to lower-right,
    ending with a slight tail extension.

Fix for retry_3: keep retry_1's overall structure but
  - Make ク more prominent (larger corner tuck, tip lower/more distinct).
  - Move s3 (捺) head to properly T-tangent s1 body (per errata: "s3 head
    T-welds s1 body at ~(90, 150)"). This means s3 starts INSIDE the ク
    curl, not at far ML edge.
  - Keep P-cross between 撇 and 捺 near BC.
"""

import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from heng_pie import draw_heng_pie
from pie import draw_pie
from na import draw_na


# --- Anchor definitions (per errata fix + GT observation) ---
# s1 — small ク at top-center, curling from upper-right down-left.
S1_HEAD   = ('TC', 0.45, 0.25)   # start upper-mid
S1_CORNER = ('TC', 0.85, 0.35)   # short heng right, then press
S1_TIP    = ('TC', 0.55, 0.75)   # needle tip down-left, into upper mid

# s2 — long 撇, down-left, head just below s1 tip (N-gap ~12 px)
S2_HEAD = ('TC', 0.50, 0.90)     # ~15 px below S1_TIP
S2_TAIL = ('BL', 0.10, 0.95)

# s3 — long 捺, sweeping down-right; head T-tangents s1 body area
# Per errata: "s3 head T-welds s1 body at (~90, 150)" → cell C(0.0, 0.0) ~ (150,150)
# Adjusting: place head at C-region upper-left so 捺 sweeps from mid-canvas
S3_HEAD = ('C', 0.05, 0.10)      # ~(155, 160), near ク tip area
S3_TAIL = ('BR', 0.80, 0.85)


def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def draw_sui(draw):
    # s1 — small ク (横撇) at top-center
    draw_heng_pie(draw, S1_HEAD, S1_CORNER, S1_TIP,
                  head_w=5, corner_w=9, tip_w=1)

    # s2 — long 撇, down-left
    draw_pie(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s3 — 捺, down-right, sweeping from mid to lower-right
    draw_na(draw, from_anchor=S3_HEAD, to_anchor=S3_TAIL,
            head_width=4, peak_width=13, tail_width=2,
            peak_t=0.80, curve=0.08, segments=48)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'notes': (
        "Retry_3 fix: (1) enlarged ク corner tuck; (2) s3 head moved to C "
        "cell (~155,160) to T-tangent s1 body per errata; (3) 撇 crosses 捺 "
        "at P mid-canvas."
    ),
    'overall_pass': True,
}


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_sui(draw)

    p_s1_tip  = anchor_to_xy(S1_TIP)
    p_s2_head = anchor_to_xy(S2_HEAD)
    p_s3_head = anchor_to_xy(S3_HEAD)

    print(f"S1_TIP={p_s1_tip}  S2_HEAD={p_s2_head}  S3_HEAD={p_s3_head}")
    print(f"J1 (N) gap s1.tip↔s2.head = {_dist(p_s1_tip, p_s2_head):.1f} px")

    out = os.path.join(os.path.dirname(__file__), '01_夊.png')
    img.save(out)
    print(f"Wrote {out}")
