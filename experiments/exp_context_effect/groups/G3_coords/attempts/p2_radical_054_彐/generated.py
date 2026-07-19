# p2_radical_054_彐 (ji) — 3-stroke radical
#
# 彐 anatomy (per GT visual):
#   S1: 横折 — top horizontal spanning most of upper area, turning down at
#       right to form the right vertical (which descends to bottom).
#   S2: 横   — middle horizontal, SHORTER, starts at left side, does NOT
#       touch the right vertical.
#   S3: 横   — bottom horizontal, spans full width, its right end meets
#       the foot of the right vertical (weld).
#
# Bank fit analysis (per TR1-TR7 + shared_rules "supplementary" principle):
#   - `heng_zhe.py` primitive: default spans from (-90,60) to (80,60) with
#     drop to (80,-75). For 彐 we need the vertical to descend much further
#     (top ~ +60 math, bottom ~ -70 math => drop ~130px, but the standalone
#     drops 135). Actually close — but standalone heng_zhe corner is at
#     +80 x, and we need the horizontal top to reach farther right for 彐
#     (the top is the widest horizontal). So heng_zhe primitive geometry
#     is close but not tuned. Given the tail must weld with S3, INLINE
#     the 横折 fresh (per TR5) rather than reuse heng_zhe.
#   - `heng.py` for S2 and S3: heng is a pure horizontal, scalable, perfect
#     fit. Use it with deliberate (ox, oy, scale).
#
# TR6 transformation notes:
#   Canvas math coords, center = (150, 150) in PIL, +y up.
#   Target extents (from GT visual read):
#     - Top horizontal: from x=-75 to x=+70 at y=+65 (math coord)
#     - Right vertical: from (+70, +65) down to (+70, -70)
#     - Middle horizontal (S2): from x=-70 to x=+30 at y=0 (short, doesn't reach right)
#     - Bottom horizontal (S3): from x=-75 to x=+72 at y=-70 (welds to vertical foot)
#
# Eyeball sanity (TR7):
#   All strokes within 300x300 canvas with margin.
#   S1 corner (+70,+65) shared with vertical top; vertical bottom (+70,-70)
#   shared with S3 right end -> weld pixel match.
#   S2 middle is short (100px) vs. S1 top (145px) and S3 bottom (147px).

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return (CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy)


def draw_ji_radical(t):
    ink_w = 10

    # S1: 横折 (inlined — TR5, because standalone heng_zhe corner too shallow)
    s1_left = _to_pixel(-75, 65)
    s1_corner = _to_pixel(70, 65)
    s1_bottom = _to_pixel(70, -70)
    t.line([s1_left, s1_corner], fill=(0, 0, 0), width=ink_w)
    t.line([s1_corner, s1_bottom], fill=(0, 0, 0), width=ink_w)
    # 顿笔 corner blob (per P6) — small
    r = ink_w // 2
    for pt in (s1_left, s1_corner, s1_bottom):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))

    # S2: middle 横 (shorter, does NOT touch right vertical)
    # Inlined heng instead of primitive call to match short length precisely.
    # target: x from -70 to +30 at y=0.  Length = 100 (vs standalone 200).
    s2_left = _to_pixel(-70, 0)
    s2_right = _to_pixel(30, 0)
    t.line([s2_left, s2_right], fill=(0, 0, 0), width=ink_w)
    for pt in (s2_left, s2_right):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))

    # S3: bottom 横 (full width, welds to S1 vertical foot at +70,-70)
    # target: x from -75 to +72 at y=-70.
    s3_left = _to_pixel(-75, -70)
    s3_right = _to_pixel(72, -70)
    t.line([s3_left, s3_right], fill=(0, 0, 0), width=ink_w)
    for pt in (s3_left, s3_right):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ji_radical(draw)
    out_path = __file__.rsplit("/", 1)[0] + "/01_彐.png"
    img.save(out_path)


if __name__ == "__main__":
    main()
