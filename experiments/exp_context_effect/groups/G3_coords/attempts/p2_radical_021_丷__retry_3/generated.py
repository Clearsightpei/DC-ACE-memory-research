# 丷 (p2_radical_021) retry_3 — 2画 radical, mirror-pair of dots opening outward.
#
# GT observation (looking at gt/phase2/丷.png at 300x300):
#   - Both marks sit roughly at canvas mid-vertical, symmetric around x=0.
#   - LEFT mark: small tapered dot slanting DOWN-LEFT (a "左点"/反点).
#     Head thin at upper-right, tail heavy at lower-left. Short: ~30 px span.
#   - RIGHT mark: longer, thinner tapered dot/short-pie slanting DOWN-RIGHT
#     visually, but reading like a mirror of the left. Head thin at
#     upper-LEFT, tail thickening at lower-RIGHT. ~30 px span.
#   - They "open outward" like the top of 八, but sit closer than 八's arms.
#
# Retry-3 fix idea (both prior attempts FAILED despite decent-looking output):
#   - Retry_1 dots were too thin/needle-like at scale 0.5 (max width capped
#     around 7 px). The GT dots are more substantial — visible tail bulges
#     of ~10-12 px width, not thin needles.
#   - Use adaptive `variant_dian` from _shared_helpers.py with hand-tuned
#     head/tail positions per catalog "mirrored dot pairs" guidance
#     (form_catalog.md: use variant_dian for BOTH, same w_head/w_tail,
#     swap head/tail for mirror).
#   - Slightly bigger canvas span (span ~35 px per dot instead of 30) so
#     the shapes read as solid dots not thin lines.
#   - Bow_perp slight so each dot has a mild inward curl.
#   - Place slightly ABOVE center (oy=+15) since 丷 as a radical sits at TOP.

import sys
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code")

from PIL import Image, ImageDraw
from _shared_helpers import variant_dian

CANVAS = 300

OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_021_丷__retry_3/01_丷.png"


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # 丷 sits slightly above vertical center. Use oy_base = +10 (math coords).
    oy_base = 10.0

    # Revised for GT match: LEFT and RIGHT dots each read as substantial
    # mirrored marks. Keep both symmetric (per form_catalog rule for
    # mirrored dot pairs — same widths, mirror the position).
    #
    # LEFT dot (反点 / 左点): thin head at upper-RIGHT, heavy tail at lower-LEFT.
    variant_dian(
        draw,
        head=(-20.0, oy_base + 15.0),   # thin upper-right head
        tail=(-48.0, oy_base - 20.0),   # heavy lower-left tail
        w_head=3.0,
        w_tail=12.0,
        bow_perp=+3.0,  # slight outward curl
    )

    # RIGHT dot (right-dian): thin head at upper-LEFT, heavy tail at lower-RIGHT.
    variant_dian(
        draw,
        head=(+20.0, oy_base + 15.0),   # thin upper-left head
        tail=(+48.0, oy_base - 20.0),   # heavy lower-right tail
        w_head=3.0,
        w_tail=12.0,
        bow_perp=-3.0,  # mirror bow direction
    )

    return img


if __name__ == "__main__":
    out = render()
    out.save(OUT)
    print(f"Saved {OUT}")
