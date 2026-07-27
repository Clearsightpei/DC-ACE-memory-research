# p2_radical_132_支 — G3 attempt (revision 2)
# Decomposition of 支 (4 strokes):
#   1. 短竖 with tiny left tick at top (upper stem)
#   2. 横 wider horizontal (upper bar) crossing near the top of the shu
#   3. 横撇 the top-left of the 又-bottom
#   4. 捺 crossing the 撇 sweeping to the lower right
#
# Revision notes vs r1:
#   - Widened the top heng (0.55 -> 0.75) to span like real 支.
#   - Shortened the top shu (0.45 -> 0.30) — it barely descends below
#     the heng in the GT.
#   - Moved shu up (oy=+18 -> oy=+35) so top block is contained.
#   - Enlarged the 又 bottom (0.70 -> 0.90 heng_pie; 0.65 -> 0.85 na).
#   - Lowered the 又 (oy -25 -> -20 heng_pie; -60 -> -55 na).
#   - Shifted 捺 origin right (+22 -> +28) for the wide GT sweep.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng          # noqa: E402
from shu import draw_shu            # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from na import draw_na              # noqa: E402


def draw_zhi(t, ox=0.0, oy=0.0, scale=1.0):
    """支 radical composition."""
    # --- TOP HALF ---
    # Stroke 1: 竖 short vertical stem near center-top. Very short —
    #   in the GT it protrudes only slightly above and below the heng.
    #   scale=0.30 -> length ~60 px total.
    draw_shu(t, ox=ox + -3 * scale, oy=oy + 42 * scale, scale=0.30 * scale)

    # Stroke 2: 横 upper horizontal, WIDER — spans much of the width.
    #   scale=0.75 -> ~150 px length. Placed at oy=+38.
    draw_heng(t, ox=ox + 0, oy=oy + 38 * scale, scale=0.75 * scale)

    # --- BOTTOM HALF (larger 又 pattern) ---
    # Stroke 3: 横撇 — larger. In you.py it sits at (0, +10) scale 0.85.
    #   Here we lower it to oy=-15 and enlarge to scale 0.95.
    draw_heng_pie(t, ox=ox + -8 * scale, oy=oy + (-15) * scale,
                  scale=0.95 * scale)

    # Stroke 4: 捺 crossing through the 撇 to the lower right, wide sweep.
    #   Enlarged to 0.85 and shifted right to (+28, -55).
    draw_na(t, ox=ox + 22 * scale, oy=oy + (-55) * scale, scale=0.85 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_zhi(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_支.png")
    img.save(out)
    print("wrote", out)
