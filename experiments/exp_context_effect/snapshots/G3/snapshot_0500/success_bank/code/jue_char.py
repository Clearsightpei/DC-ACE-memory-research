# jue_char.py — 亅 character, 1 stroke 竖钩.
# PASSed at p3_char_0008_亅 (B3 pos 165).
# Inline fresh (bank jue_radical hook too short). Longer L-shaped hook +
# top 顿笔.
CANVAS = 300


def _to_px(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def draw_jue_char(t, ox=0, oy=0, scale=1.0):
    shaft_x = 20 * scale + ox
    shaft_top_y = 95 * scale + oy
    shaft_bot_y = -85 * scale + oy
    thickness = max(1, int(round(10 * scale)))

    head_px, head_py = _to_px(shaft_x - 4, shaft_top_y + 2)
    t.ellipse([head_px - 5, head_py - 5, head_px + 5, head_py + 5], fill=(0, 0, 0))
    c0 = _to_px(shaft_x - 6, shaft_top_y - 2)
    c1 = _to_px(shaft_x, shaft_top_y - 6)
    t.line([c0, c1], fill=(0, 0, 0), width=max(1, thickness - 2))

    x_top, y_top = _to_px(shaft_x, shaft_top_y)
    x_bot, y_bot = _to_px(shaft_x, shaft_bot_y)
    t.line([(x_top, y_top), (x_bot, y_bot)], fill=(0, 0, 0), width=thickness)

    corner_px, corner_py = _to_px(shaft_x, shaft_bot_y)
    t.ellipse([corner_px - 5, corner_py - 5, corner_px + 5, corner_py + 5], fill=(0, 0, 0))
    hook_tip_x = shaft_x - 32 * scale
    hook_tip_y = shaft_bot_y + 12 * scale
    n_seg = 6
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        mx0 = shaft_x + u0 * (hook_tip_x - shaft_x)
        my0 = shaft_bot_y + u0 * (hook_tip_y - shaft_bot_y)
        mx1 = shaft_x + u1 * (hook_tip_x - shaft_x)
        my1 = shaft_bot_y + u1 * (hook_tip_y - shaft_bot_y)
        w = max(2, int(round(thickness * (1 - 0.6 * ((u0 + u1) / 2)))))
        p0 = _to_px(mx0, my0)
        p1 = _to_px(mx1, my1)
        t.line([p0, p1], fill=(0, 0, 0), width=w)
