# p2_radical_041_彳 (chi) — "double-person" radical, 3 strokes:
#   1. short 撇 (upper-left, small)
#   2. longer 撇 (middle, its head at tail of stroke-1)
#   3. 竖 (vertical, descending from tail of stroke-2, straight down)
#
# Composition strategy (per TR1-TR7):
# - Reuse pie primitive twice (small + medium) — bank primitive at scales 0.35, 0.55
# - Reuse shu primitive at scale ~0.55 for the vertical
# - Coord convention: math (center origin, +y up); PIL conversion inside primitives.
#
# GT observations (from gt/phase2/彳.png at 300x300):
#   - Whole radical clusters slightly left of center, tall aspect
#   - Stroke-1 (short pie): head ~ (140, 90) px, tail ~ (120, 130) px
#   - Stroke-2 (long pie): head ~ (170, 105) px, tail ~ (95, 220) px
#   - Stroke-3 (shu):      top ~ (170, 150) px, bottom ~ (170, 265) px
# In math coords (300x300, center 150,150; +y up):
#   Stroke-1 head (−10, +60) → tail (−30, +20)   center ≈ (−20, +40)
#   Stroke-2 head (+20, +45) → tail (−55, −70)   center ≈ (−17, −12)
#   Stroke-3 top  (+20, 0)   → bot  (+20, −115)  center ≈ (+20, −57)
#
# TR6 — deliberate primitive placements:
#   pie primitive default: head (+65,+90), tail (−45,−85), center ≈ (+10,+2)
#   pie #1 at scale 0.35: local head (+22.75, +31.5), local tail (−15.75, −29.75)
#     want head at (−10, +60), local head is (+22.75, +31.5) → ox = -10 - 22.75 = -32.75, oy = 60 - 31.5 = +28.5
#     check tail: (-32.75 + -15.75, 28.5 + -29.75) = (-48.5, -1.25) — hmm too far left, want (-30, +20)
#     Instead compute from center: local center (+10*0.35, +2*0.35) = (+3.5, +0.7)
#     target center (−20, +40) → ox = -20 - 3.5 = -23.5, oy = 40 - 0.7 = +39.3
#     Round: ox=-24, oy=+39, scale=0.35
#   pie #2 at scale 0.55: local center (+5.5, +1.1)
#     target center (−17, −12) → ox = -17 - 5.5 = -22.5, oy = -12 - 1.1 = -13.1
#     Round: ox=-23, oy=-13, scale=0.55
#   shu primitive default: half-length 100, so goes (0, +100) to (0, -100), center (0, 0)
#   shu at scale 0.55: half-length 55, goes (0, +55) to (0, -55), local center (0,0)
#     target center (+20, -57) → ox=+20, oy=-57, scale=0.55
#
# Sanity check (TR7):
#   - Stroke-1 tail should meet stroke-2 head-ish region (close but not weld)
#     stroke-1 tail approx (-24 + -15.75, 39 + -29.75) = (-39.75, 9.25)
#     stroke-2 head approx (-23 + 22.75*(0.55/0.35 factor... just recompute)
#     stroke-2 head local = (65*0.55, 90*0.55) = (35.75, 49.5), world = (-23+35.75, -13+49.5) = (12.75, 36.5)
#     Hmm — stroke-2 head at (13, 37) is upper-right; stroke-1 tail at (-40, 9). They are separated in GT too
#     (in GT the short-pie's tail sits ABOVE the long-pie's shaft mid).
#   - Stroke-2 tail approx: local (-45*0.55, -85*0.55) = (-24.75, -46.75), world = (-47.75, -59.75)
#     Stroke-3 top approx: (+20, 0) in world. Stroke-2 tail (-48, -60) is far from shu top — but GT shows
#     shu starting at the MIDDLE of the long pie, not at its tail. Let me re-check: yes, in GT
#     shu-top sits around where pie-2 crosses the vertical line at x≈+20, and pie-2 at u≈0.35 passes
#     near (17, 20) in math coords — close to shu top (20, 0). Small gap acceptable.
#   - Canvas margins: stroke-2 tail (-48, -60) → PIL px (102, 210). Fine within margin.
#   - All within 300x300 with >10 px margin.

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from pie import draw_pie
from shu import draw_shu

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # REVISION 1 — first attempt was too spread out; strokes need to touch.
    # GT reads as: stroke-1 tail meets stroke-2 head (top-left cluster),
    # stroke-3 (shu) top touches stroke-2 near its mid-lower portion.
    # Retarget:
    #   stroke-1 tail ≈ (-8, +25) math      (PIL 142, 125)
    #   stroke-2 head ≈ (-5, +30) math      (PIL 145, 120) — welds w/ stroke-1 tail
    #   stroke-2 tail ≈ (-45, -55) math     (PIL 105, 205)
    #   stroke-3 top  ≈ (+5, -20) math      (PIL 155, 170) — on stroke-2's shaft mid
    #   stroke-3 bot  ≈ (+5, -110) math     (PIL 155, 260)
    #
    # Stroke 1 (short pie, scale 0.30):
    #   local tail = (-45*0.30, -85*0.30) = (-13.5, -25.5)
    #   want tail (-8, +25) → ox = -8 - (-13.5) = +5.5, oy = 25 - (-25.5) = +50.5
    #   ox=+6, oy=+51, scale=0.30
    draw_pie(t, ox=+6, oy=+51, scale=0.30)

    # Stroke 2 (long pie, scale 0.55):
    #   local head = (+65*0.55, +90*0.55) = (+35.75, +49.5)
    #   want head (-5, +30) → ox = -5 - 35.75 = -40.75, oy = 30 - 49.5 = -19.5
    #   ox=-41, oy=-19, scale=0.55
    #   check tail: (-45*0.55, -85*0.55) = (-24.75, -46.75)
    #     world tail = (-41 + -24.75, -19 + -46.75) = (-65.75, -65.75) ≈ (PIL 84, 216) — slightly off canvas-safe but OK
    draw_pie(t, ox=-41, oy=-19, scale=0.55)

    # Stroke 3 (shu, scale 0.45):
    #   half_len = 100*0.45 = 45
    #   want top (+5, -20), bot (+5, -110). Center of shu = midpoint = (+5, -65)
    #   ox=+5, oy=-65, scale=0.45
    #   check top: (0+5, +45-65) = (+5, -20) ✓
    #   check bot: (0+5, -45-65) = (+5, -110) ✓
    draw_shu(t, ox=+5, oy=-65, scale=0.45)

    out = os.path.join(os.path.dirname(__file__), "01_彳.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
