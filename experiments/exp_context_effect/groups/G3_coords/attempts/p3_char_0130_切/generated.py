# p3_char_0130_切 (qiē) — G3 attempt.
# Composition: 七 on the left (bank primitive) + 刀 on the right (inline fresh).
# 刀 has persistent errata (retry_n=3 as radical, char also FAIL). Fix idea from
# errata.md: draw 刀 as ONE continuous polyline (heng → 折 corner → 竖 → 钩 up-left)
# with a separate 撇 crossing at ~60% along the horizontal.
#
# Reasons for inline 刀 over bank dao_pang: dao_pang is the 刂 radical (2 vertical
# strokes), not the full 刀 shape. 刀 needs horizontal + hook + crossing pie.
import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from qi import draw_qi  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_dao_inline(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 刀 as one continuous polyline (heng → 折 → 竖钩) + separate crossing 撇.

    Coord system: math convention (y grows up). Origin (ox, oy) is 刀's center.
    Scale=1.0 gives 刀 that fits in ~90px wide box.
    """
    thickness = max(1, int(round(11 * scale)))

    # ---- Continuous polyline: heng (top) → zhe (corner) → shu (down) → hook up-left
    # heng: from left to right, slight downward tilt (calligraphic 横)
    heng_start = _to_pixel(ox + (-40) * scale, oy + 40 * scale)
    heng_end = _to_pixel(ox + 40 * scale, oy + 32 * scale)
    # zhe corner + descender (竖 going down-slightly-left curving right)
    corner = heng_end
    shu_bot = _to_pixel(ox + 20 * scale, oy - 55 * scale)
    # hook tip pointing up-left
    hook_tip = _to_pixel(ox + 4 * scale, oy - 40 * scale)

    # Draw heng
    t.line([heng_start, heng_end], fill=(0, 0, 0), width=thickness)
    # Draw zhe→shu with slight bow
    n_seg = 10
    prev = corner
    for i in range(1, n_seg + 1):
        u = i / n_seg
        # slight bow: shaft curves gently to the left as it descends
        cx = corner[0] + u * (shu_bot[0] - corner[0]) + (-3 * scale) * (u * (1 - u) * 4)
        cy = corner[1] + u * (shu_bot[1] - corner[1])
        t.line([prev, (cx, cy)], fill=(0, 0, 0), width=thickness)
        prev = (cx, cy)
    # Draw hook (tapered)
    hook_base = prev
    n_hook = 6
    for i in range(n_hook):
        u0 = i / n_hook
        u1 = (i + 1) / n_hook
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(2, int(round(thickness * (1 - (u0 + u1) / 2 * 0.7))))
        t.line([p0, p1], fill=(0, 0, 0), width=w)

    # ---- Separate 撇 (long sweeping pie) that crosses the heng at ~60% mark
    # In 刀, the 撇 comes from upper-right area near heng's ~60% and sweeps down-left
    # crossing shaft, going past the bottom of the character.
    pie_head_x = ox + (-20) * scale  # near heng's ~60% from left (heng spans -40..40)
    pie_head_y = oy + 38 * scale
    pie_tail_x = ox + (-55) * scale
    pie_tail_y = oy - 70 * scale
    pie_head = _to_pixel(pie_head_x, pie_head_y)
    pie_tail = _to_pixel(pie_tail_x, pie_tail_y)

    # Tapered polyline for the 撇 (thick head → thin tail), slight leftward bow
    n_pie = 14
    for i in range(n_pie):
        u0 = i / n_pie
        u1 = (i + 1) / n_pie
        # bow perpendicular to direction (curves outward to the left)
        bow0 = -6 * scale * (u0 * (1 - u0) * 4)
        bow1 = -6 * scale * (u1 * (1 - u1) * 4)
        p0 = (pie_head[0] + u0 * (pie_tail[0] - pie_head[0]) + bow0,
              pie_head[1] + u0 * (pie_tail[1] - pie_head[1]))
        p1 = (pie_head[0] + u1 * (pie_tail[0] - pie_head[0]) + bow1,
              pie_head[1] + u1 * (pie_tail[1] - pie_head[1]))
        w = max(2, int(round(thickness * (1 - (u0 + u1) / 2 * 0.75))))
        t.line([p0, p1], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # 七 on the LEFT: shift left, scale so it fills the left column.
    draw_qi(t, ox=-65, oy=-10, scale=0.85)

    # 刀 on the RIGHT: centered around x=+55, larger, so pie sweeps to bottom.
    draw_dao_inline(t, ox=55, oy=-5, scale=1.15)

    out_path = os.path.join(_HERE, "01_切.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
