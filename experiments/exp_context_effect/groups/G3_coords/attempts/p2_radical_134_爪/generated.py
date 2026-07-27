"""p2_radical_134_爪 — 4-stroke radical (zhǎo/zhuǎ, "claw").

Stroke order per MMH-style convention:
  1) short 撇 at upper-center (small down-left slant)
  2) short 撇 in middle-right area (down-left slant, sits below stroke 1)
  3) long sweeping 撇 on the left (upper-center to lower-left)
  4) 竖/捺 combo on right: from center-top going down-right (bent 捺-like),
     visible in GT as the right descending arm.

Using PIL pixel coords directly (no bank primitive is a perfect fit —
爪 is 3 pies + 1 na-like arm; each pie has a distinct role).
Adaptive helpers from `_shared_helpers.py` are imported for consistency
with v7 form_catalog approach (variant_pie / variant_na).
"""
import sys, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _shared_helpers import variant_pie, variant_na, to_px  # noqa: E402


def draw_zhua(t):
    # Math coords: center (0,0), +y up. Canvas 300x300.
    # After first-pass comparison to GT, revising:
    #  - character sits too low & small on canvas — enlarge, shift up
    #  - right arm should be more bent (down then out), not smooth diag
    #  - left 撇 has strong curvature — good, keep bow

    # Stroke 1: short top 撇 (upper-left of the crown)
    # GT PIL ~ (145, 85) -> (115, 115). math (-5,+65) -> (-35,+35)
    variant_pie(t,
                head=(-5, 68),
                tail=(-33, 35),
                bow_perp=-3.0,
                w_head=6.0,
                w_tail=1.5,
                n=30)

    # Stroke 2: short middle 撇 — the small stroke that reaches to the
    # right side of the crown. In GT it looks nearly horizontal, going
    # from mid-right down to just left of center.
    # GT PIL ~ (180, 80) -> (140, 105). math (+30,+70) -> (-10,+45)
    variant_pie(t,
                head=(33, 72),
                tail=(-8, 48),
                bow_perp=-2.0,
                w_head=5.0,
                w_tail=1.5,
                n=30)

    # Stroke 3: long sweeping 撇 down the LEFT side, strong bow.
    # From the top-center starting point, curving down and left to lower-left.
    # GT PIL ~ (135, 100) -> (85, 260). math (-15,+50) -> (-65,-110)
    variant_pie(t,
                head=(-12, 50),
                tail=(-65, -115),
                bow_perp=-16.0,
                w_head=9.0,
                w_tail=1.5,
                n=70)

    # Stroke 4: the right arm — starts from center-top, drops down as a
    # (slightly bent) vertical, then swings out to the lower-right.
    # In GT this reads more like a 竖 that ends in a rightward foot.
    # Model as two segments joined at a bend:
    #   (a) near-vertical drop from (0,+45) to (+8,-40)
    #   (b) diagonal outward to lower-right ending around (+90,-105)
    # Use variant_pie for the drop (thin taper) and variant_na for
    # the belly-swelling outward sweep.
    variant_pie(t,
                head=(0, 48),
                tail=(8, -45),
                bow_perp=-2.0,
                w_head=5.0,
                w_tail=3.5,
                n=40)
    variant_na(t,
               head=(6, -35),
               tail=(95, -108),
               bow_perp=4.0,
               w_head=3.5,
               w_belly=10.0,
               w_tail=3.0,
               belly_u=0.65,
               n=60)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhua(d)
    out = os.path.join(HERE, "01_爪.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
