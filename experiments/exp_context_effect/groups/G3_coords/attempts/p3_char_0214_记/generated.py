"""p3_char_0214_记 — G3 attempt.

记 = 讠 (speech radical, left) + 己 (right).

G3 constraint: storage unit is a callable Python function. No bank
primitive exists for 讠 or 己 at time of attempt — inline fresh under
v8 signature freedom. PIL-pixel recipe (screen coords, y grows down).
"""
from PIL import Image, ImageDraw


def draw_ji_speak(ox=0, oy=0, scale=1.0):
    """Render 记 to a 300x300 PIL image. Returns the image.

    ox, oy, scale kept as knobs per G3 convention, though this recipe
    is authored at native 300x300.
    """
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)

    def px(x, y):
        return (ox + x * scale, oy + y * scale)

    def line(a, b, w):
        d.line([px(*a), px(*b)], fill="black", width=w)

    def polyline(pts, w):
        pts_t = [px(*p) for p in pts]
        d.line(pts_t, fill="black", width=w, joint="curve")

    # ------------------------------------------------------------
    # LEFT: 讠 (simplified speech radical)
    # Small 点 up-left, then 横折提 below.
    # ------------------------------------------------------------
    # 点: short diagonal blob (upper-right slanting into lower-left)
    polyline([(72, 70), (60, 92)], 8)

    # 横折提 (h-turn-rise): flat top, drop, then rising 提 to upper-right
    # top short heng
    polyline([(48, 138), (95, 138)], 6)
    # descent (slight inward curve)
    polyline([(95, 138), (90, 168), (78, 178)], 6)
    # rising 提 up to the right (thins toward tip in real calligraphy,
    # here rendered as a short slanted line)
    polyline([(78, 178), (115, 160)], 6)

    # ------------------------------------------------------------
    # RIGHT: 己
    # Stroke 1 — 横折 (top heng into descending shu)
    # Stroke 2 — middle 横
    # Stroke 3 — 竖弯钩 (down, sweep right, small upward hook)
    # ------------------------------------------------------------
    # Stroke 1: 横折 — top heng
    polyline([(130, 95), (250, 95)], 7)
    # then shu down (short)
    polyline([(250, 95), (250, 155)], 7)

    # Stroke 2: middle heng
    polyline([(130, 158), (250, 158)], 7)

    # Stroke 3: 竖弯钩
    # Down from where the middle heng starts
    polyline([(133, 158), (133, 235)], 7)
    # Curve right along the bottom
    polyline([(133, 235), (150, 250), (240, 250)], 7)
    # Small upward hook
    polyline([(240, 250), (250, 232)], 7)

    return img


if __name__ == "__main__":
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img = draw_ji_speak()
    img.save(os.path.join(out_dir, "01_记.png"))
