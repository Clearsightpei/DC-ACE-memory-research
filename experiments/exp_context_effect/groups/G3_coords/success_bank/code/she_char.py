# she_char.py — 社 — promoted from p3_char_0341_社 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# p3_char_0341_社 — 社 (shè, community/altar), 7 strokes.
# L-R composition: 礻 (left, 4 strokes) + 土 (right, 3 strokes).
#
# Both components are mastered bank entries. Reuse:
#   - shi_ceremony_pang.py (INDEX row 84, PASSed at p2_radical_116_礻)
#   - tu.py (INDEX row 71, PASSed at p2_radical_072_土)
#
# L-R placement per drawer_memory L-R table pattern (们-like 0.55/0.55):
# 礻 primitive spans roughly x∈[-45,+38], y∈[-115,+90] at scale 1.
# 土 primitive spans roughly x∈[-105,+105] (bottom heng), y∈[-86,+36] at scale 1.
# Both are relatively "tall" so we can use ~0.6 scale each side without collision.
#   - 礻 at ox=-70, oy=0, scale=0.65 → left half
#   - 土  at ox=+65, oy=-5, scale=0.55 → right half, slight downshift
#     to sit lower like the GT (bottom heng near baseline).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_ceremony_pang import draw_shi_ceremony_pang  # noqa: E402
from tu import draw_tu  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Left: 礻  (bumped scale + shifted slightly right to close L-R gap)
    draw_shi_ceremony_pang(d, ox=-55.0, oy=5.0, scale=0.72)
    # Right: 土  (slimmed so bottom heng doesn't dominate)
    draw_tu(d, ox=60.0, oy=-10.0, scale=0.50)
    img.save(os.path.join(os.path.dirname(__file__), "01_社.png"))


if __name__ == "__main__":
    main()
