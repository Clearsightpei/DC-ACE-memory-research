# p1_stroke_25_横折弯钩 — generated.py
# Draws 横折弯钩 (heng zhe wan gou) as coord-based PIL primitives.
# Structure: 横 (horizontal, slight rise) + 折 (short drop) + 弯 (curved
# bottom-right arc that turns left along the base) + 钩 (short up-and-left
# flick from the arc's leftmost tail).
#
# This attempt reuses idioms from wan_gou.py (curved body + hook flick) and
# heng_zhe.py (horizontal + corner blob), combined into one continuous
# tapered spine on a 300x300 canvas, math-coord convention (+y up).
#
# Rule compliance: writes only this file + PNG under attempts/.
# Does NOT create or edit anything under success_bank/code/.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _stroke_line(t, p0, p1, w0, w1, steps=60):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _stroke_curve(t, pts, w0, w1):
    n = len(pts)
    for i in range(n - 1):
        u = i / max(1, n - 1)
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        p1 = pts[i]
        p2 = pts[i + 1]
        t.line([p1, p2], fill=(0, 0, 0), width=max(1, int(round(w))))
        t.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))


def draw_heng_zhe_wan_gou(t, ox=0, oy=0, scale=1.0):
    """横折弯钩 = 横 rightward + 折 short drop + 弯 sweeping arc curving
    down-then-left + 钩 short up-and-left flick from the arc's tail."""

    # --- Segment 1: 横 (horizontal, slight upward tilt), left to right. ---
    # Math coords (center origin, +y up).
    p_h_start = (-70 * scale, 70 * scale)
    p_h_end = (55 * scale, 75 * scale)
    a = _to_pixel(ox + p_h_start[0], oy + p_h_start[1])
    b = _to_pixel(ox + p_h_end[0], oy + p_h_end[1])
    _stroke_line(t, a, b, 10 * scale, 12 * scale, steps=80)

    # 顿笔 blob at the corner where 横 turns into 折.
    corner1 = _to_pixel(ox + 58 * scale, oy + 75 * scale)
    r_corner = 9 * scale
    t.ellipse(
        [corner1[0] - r_corner, corner1[1] - r_corner,
         corner1[0] + r_corner, corner1[1] + r_corner],
        fill=(0, 0, 0),
    )

    # --- Segment 2: 折 short vertical drop, slightly left-leaning. ---
    p_v_start = (58 * scale, 75 * scale)
    p_v_end = (50 * scale, 10 * scale)
    va = _to_pixel(ox + p_v_start[0], oy + p_v_start[1])
    vb = _to_pixel(ox + p_v_end[0], oy + p_v_end[1])
    _stroke_line(t, va, vb, 12 * scale, 9 * scale, steps=60)

    # --- Segment 3: 弯 curved sweep, arcing from the bottom of 折
    # down-and-around to the left. Quadratic bezier: control point
    # placed to swing the belly downward then rightward's mirror-left. ---
    p_arc_start = (50 * scale, 10 * scale)
    p_arc_ctrl = (55 * scale, -70 * scale)   # pull down and slightly right
    p_arc_end = (-55 * scale, -75 * scale)   # ends left-of-center, low
    arc_pts_math = _qbez(p_arc_start, p_arc_ctrl, p_arc_end, 70)
    arc_pts_px = [_to_pixel(ox + p[0], oy + p[1]) for p in arc_pts_math]
    # Width profile: thin at top (u=0), belly around u=0.55, thin at tail.
    n = len(arc_pts_px)
    for i in range(n - 1):
        u = i / (n - 1)
        if u < 0.55:
            w = 8 + (12 - 8) * (u / 0.55)
        else:
            w = 12 - (12 - 6) * ((u - 0.55) / 0.45)
        w_int = max(3, int(round(w * scale)))
        p1 = arc_pts_px[i]
        p2 = arc_pts_px[i + 1]
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
        rr = w_int / 2.0
        t.ellipse([p2[0] - rr, p2[1] - rr, p2[0] + rr, p2[1] + rr], fill=(0, 0, 0))

    # --- Segment 4: 钩 short up-and-left flick from arc tail (per P1). ---
    hook_base = p_arc_end
    hook_ctrl = (-72 * scale, -60 * scale)
    hook_tip = (-82 * scale, -40 * scale)
    hook_pts_math = _qbez(hook_base, hook_ctrl, hook_tip, 24)
    hook_pts_px = [_to_pixel(ox + p[0], oy + p[1]) for p in hook_pts_math]
    m = len(hook_pts_px)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 6 - (6 - 2) * u
        w_int = max(2, int(round(w * scale)))
        p1 = hook_pts_px[i]
        p2 = hook_pts_px[i + 1]
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_wan_gou(draw, ox=0, oy=0, scale=1.0)
    out_path = (
        "<REPO_ROOT>/experiments/"
        "exp_context_effect/groups/G3_coords/attempts/"
        "p1_stroke_25_横折弯钩/01_横折弯钩.png"
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
