# p2_radical_046_大 — 大 radical (3画)
# Structure: 一 (heng) + 丿 (pie) + 乀 (na).
# The pie and na start from the same point on the horizontal's midpoint,
# sweeping down-left and down-right respectively. The pie's head sits
# ABOVE the horizontal (small tick above the crossing).
#
# Coord math convention: math coords, center origin, +y up, per P5.
# Canvas 300x300, PIL ImageDraw. Per P2, PIL preferred over turtle.
#
# Transform reasoning (TR1, TR6):
# - heng: standalone bank primitive is 200 px wide. Target width in GT
#   is ~140 px. scale = 0.70. Place slightly above center vertically
#   (GT has heng around y ~ +15 on 300 canvas). ox=0, oy=+15.
# - pie: bank pie head at (+65, +90) tail (-45, -85) in local coords.
#   For 大, pie needs to start from ~(+5, +65) (just above the heng's
#   middle) and sweep down-left to ~(-80, -110). This is a different
#   angle/length from the standalone pie. Bank pie at scale 1.0 has
#   head at (+65, +90) offset — too far right, too far up.
#   To place head near canvas midline: target head ~(+5,+65). Bank
#   head local: (65,90). Need scale ~ 1.05 and ox=-60, oy=-25.
#   But that would move tail to (-45-60, -85-25)=(-105,-110). Tail
#   pixel: (150-105, 150+110) = (45, 260). Fine — within canvas.
#   Actually the pie in 大 must clearly cross the horizontal. Head
#   above the horizontal, curve going through the horizontal near its
#   middle, tail extending to lower-left. This matches the standard
#   pie shape with ox shift.
# - na: bank na head at (-70,+80) tail (+80,-90). For 大, na needs to
#   start from ~(+5, +65) (same start-area as pie's crossing) and
#   sweep to lower-right ~(+95, -110). Bank na scale 1.0 head local
#   (-70,+80). Need head at (+5,+65). ox=+75, oy=-15.

from PIL import Image, ImageDraw
import os, sys

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from na import draw_na


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: 一 (heng) — horizontal near upper middle.
    # scale 0.70 → length 140 px. ox=0 (center), oy=+15 (slightly above
    # middle vertically, matches GT proportions).
    draw_heng(d, ox=0, oy=15, scale=0.70)

    # Stroke 2: 丿 (pie) — head sits ONLY A LITTLE above the heng at its
    # midpoint (short tick), then descends through the heng and sweeps to
    # lower-left. Head near (-5, +30); tail near (-90, -110).
    # Bank pie head local (+65,+90). Need head at (-5,+30): ox = -5-65 = -70,
    # oy = 30-90 = -60. Scale 1.0. Tail transformed = (-45-70, -85-60) =
    # (-115, -145) math → PIL (35, 295). That's too far down; use scale 0.95.
    # tail: (-45*0.95-70, -85*0.95-60) = (-113, -141) → still low. Use
    # scale 0.85. head: (65*0.85-70, 90*0.85-60) = (-14.75, 16.5) — head
    # would end up around math (-15, +17), just at the heng level. Want
    # head slightly ABOVE heng (y ~+30). Try scale 0.90 with ox=-60, oy=-55:
    # head local (+65,+90) → (65*0.9-60, 90*0.9-55) = (-1.5, 26). Good.
    # tail local (-45,-85) → (-45*0.9-60, -85*0.9-55) = (-100.5, -131.5) →
    # PIL (49.5, 281.5). Bottom of canvas — OK.
    draw_pie(d, ox=-60, oy=-55, scale=0.90)

    # Stroke 3: 乀 (na) — head near the pie's crossing on the heng (around
    # (+5, +15)) and sweeps to lower-right ~(+95, -110).
    # Bank na head local (-70,+80). Need head at (+5,+15): ox = 5-(-70)=75,
    # oy = 15-80 = -65. Scale 0.90.
    # tail local (+80,-90) → (80*0.9+75, -90*0.9-65) = (147, -146) →
    # PIL (297, 296). At right edge; pull back with ox=70.
    # tail (+80,-90) → (72+70, -81-65) = (142, -146) → PIL (292, 296). OK.
    draw_na(d, ox=70, oy=-65, scale=0.90)

    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_046_大/01_大.png"
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
