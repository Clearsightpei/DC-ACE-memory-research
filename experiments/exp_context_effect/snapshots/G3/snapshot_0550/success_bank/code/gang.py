# gang.py — 冈 (gāng), 4 strokes: 竖 + 横折钩 (冂 frame) + 乂 inside (撇 + 捺).
# PASSed at p3_char_0127_冈 (B5, pos 267). Frame authored in PIL-pixel coords
# (like men_char); 乂 uses variant_pie/variant_na in math coords.
# NOTE: ox/oy/scale ignored — PIL-pixel recipe.
from _shared_helpers import variant_pie, variant_na


def draw_gang(t, ox=0, oy=0, scale=1.0):
    """冈 — 冂 frame + 乂 inside. ox/oy/scale ignored (PIL-pixel recipe)."""
    def _tapered_line_px(p0, p1, w0, w1, steps=24):
        for i in range(steps):
            u0 = i / steps
            u1 = (i + 1) / steps
            xa = p0[0] + (p1[0] - p0[0]) * u0
            ya = p0[1] + (p1[1] - p0[1]) * u0
            xb = p0[0] + (p1[0] - p0[0]) * u1
            yb = p0[1] + (p1[1] - p0[1]) * u1
            w = max(1, int(round(w0 + (w1 - w0) * u0)))
            t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)

    # Stroke 1: 竖 (left vertical)
    left_top = (72, 78)
    left_bot = (68, 258)
    _tapered_line_px(left_top, left_bot, w0=8, w1=9, steps=32)
    t.ellipse([left_top[0] - 4, left_top[1] - 4,
               left_top[0] + 4, left_top[1] + 4], fill=(0, 0, 0))
    t.ellipse([left_bot[0] - 5, left_bot[1] - 5,
               left_bot[0] + 5, left_bot[1] + 5], fill=(0, 0, 0))

    # Stroke 2: 横折钩
    h_left = (78, 70)
    h_right = (232, 66)
    _tapered_line_px(h_left, h_right, w0=8, w1=10, steps=28)
    t.ellipse([h_right[0] - 6, h_right[1] - 6,
               h_right[0] + 6, h_right[1] + 6], fill=(0, 0, 0))
    v_top = (232, 66)
    v_bot = (228, 256)
    _tapered_line_px(v_top, v_bot, w0=10, w1=9, steps=32)
    t.ellipse([v_bot[0] - 6, v_bot[1] - 6,
               v_bot[0] + 6, v_bot[1] + 6], fill=(0, 0, 0))
    hook_end = (v_bot[0] - 24, v_bot[1] - 18)
    _tapered_line_px((v_bot[0] + 1, v_bot[1] + 2), hook_end,
                     w0=9, w1=2, steps=14)

    # Strokes 3+4: 乂 inside
    variant_pie(t,
                head=(40, 40),
                tail=(-50, -80),
                bow_perp=-5.0, w_head=7.0, w_tail=1.5, n=60)
    variant_na(t,
               head=(-40, 20),
               tail=(50, -80),
               bow_perp=5.0, w_head=2.0, w_belly=9.0, w_tail=2.0,
               belly_u=0.65, n=70)
