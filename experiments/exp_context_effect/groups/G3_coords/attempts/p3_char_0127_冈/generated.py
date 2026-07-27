# p3_char_0127_冈 (gang) — 4 strokes: 竖 + 横折钩 (冂 frame) + 撇 + 捺 (乂 inside)
# Approach: adapt men_char's 冂-frame (widen for near-square aspect of 冈),
# then place yi_cross-style 乂 inside the frame.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import variant_pie, variant_na  # noqa: E402


def _tapered_line_px(D, p0, p1, w0, w1, steps=24):
    """PIL-pixel tapered line (used for the frame, which is authored in
    PIL coords like men_char.py)."""
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_gang_char(D):
    # === Stroke 1: 竖 (left vertical) ===
    left_top = (72, 78)
    left_bot = (68, 258)
    _tapered_line_px(D, left_top, left_bot, w0=8, w1=9, steps=32)
    D.ellipse([left_top[0] - 4, left_top[1] - 4,
               left_top[0] + 4, left_top[1] + 4], fill=(0, 0, 0))
    D.ellipse([left_bot[0] - 5, left_bot[1] - 5,
               left_bot[0] + 5, left_bot[1] + 5], fill=(0, 0, 0))

    # === Stroke 2: 横折钩 (top horizontal + right vertical + inward hook) ===
    h_left = (78, 70)
    h_right = (232, 66)
    _tapered_line_px(D, h_left, h_right, w0=8, w1=10, steps=28)
    D.ellipse([h_right[0] - 6, h_right[1] - 6,
               h_right[0] + 6, h_right[1] + 6], fill=(0, 0, 0))
    v_top = (232, 66)
    v_bot = (228, 256)
    _tapered_line_px(D, v_top, v_bot, w0=10, w1=9, steps=32)
    D.ellipse([v_bot[0] - 6, v_bot[1] - 6,
               v_bot[0] + 6, v_bot[1] + 6], fill=(0, 0, 0))
    # hook
    hook_end = (v_bot[0] - 24, v_bot[1] - 18)
    _tapered_line_px(D, (v_bot[0] + 1, v_bot[1] + 2), hook_end,
                     w0=9, w1=2, steps=14)

    # === Strokes 3+4: 乂 inside (math coords: center origin, +y up) ===
    # Interior available in math coords: x in [-78..78], y in [+80..-108].
    # Place 乂 centered around (0, -20) — occupies interior x [-55..55], y [50..-95]
    # Stroke 3: 撇 — starts upper-right, sweeps to lower-left. Kept
    # inside frame (frame interior in math y is roughly +80..-100).
    variant_pie(D,
                head=(40, 40),      # upper-right (math)
                tail=(-50, -80),    # lower-left (math)
                bow_perp=-5.0, w_head=7.0, w_tail=1.5, n=60)
    # Stroke 4: 捺 — starts upper-left near crossing, sweeps to lower-right
    variant_na(D,
               head=(-40, 20),
               tail=(50, -80),
               bow_perp=5.0, w_head=2.0, w_belly=9.0, w_tail=2.0,
               belly_u=0.65, n=70)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_gang_char(D)
    out = os.path.join(os.path.dirname(__file__), "01_冈.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
