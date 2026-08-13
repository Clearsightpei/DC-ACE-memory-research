"""Render 后 (hou) — Phase 3, char item p3_char_0235.

G3 attempt. Callable function form; inline PIL rendering (per v8
signature freedom). GT decomposition:

  Stroke 1  短撇   top-left → down-left short pie
  Stroke 2  长横   top horizontal spanning most of width, slight up-right tilt
  Stroke 3  短横   mid horizontal (shorter), inside the envelope
  Stroke 4  竖     left vertical descending (the 厂-like envelope's leg)
  Stroke 5  横折   口's top-right corner (short heng + turn down)
  Stroke 6  横     口's bottom closing 横

6 strokes total. Thin uniform ink per GT (MMH-style, not calligraphic).
"""

from PIL import Image, ImageDraw


def draw_hou(img_size=300):
    W = H = img_size
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    ink = "black"
    w_thin = 3  # uniform thin per GT

    # Stroke 1: 短撇 — from (~120, 50) down-left to (~55, 130)
    d.line([(120, 50), (100, 75), (78, 100), (58, 130)], fill=ink, width=w_thin)

    # Stroke 2: 长横 — from (~62, 128) to (~232, 108), slight up-right
    d.line([(62, 128), (145, 120), (232, 108)], fill=ink, width=w_thin)

    # Stroke 3: 左竖 — descending 厂 leg, from (~62, 128) to (~60, 280)
    # tapering slightly outward
    d.line([(62, 128), (60, 200), (58, 260), (58, 285)], fill=ink, width=w_thin)

    # Stroke 4: 短横 (inside, middle) — from (~110, 168) to (~245, 158)
    d.line([(110, 168), (175, 163), (245, 158)], fill=ink, width=w_thin)

    # 口 (bottom-right small rectangle, self-contained, 3 strokes)
    # box roughly x in [110, 245], y in [200, 275]
    kx0, kx1 = 112, 245
    ky0, ky1 = 200, 275

    # Stroke 5: 口 左竖
    d.line([(kx0, ky0), (kx0 + 1, ky0 + 40), (kx0 + 2, ky1)], fill=ink, width=w_thin)

    # Stroke 6: 口 横折 (top 横 then right 竖)
    d.line([(kx0, ky0), (170, ky0 - 2), (kx1, ky0 - 4)], fill=ink, width=w_thin)
    d.line([(kx1, ky0 - 4), (kx1, ky0 + 35), (kx1 - 2, ky1)], fill=ink, width=w_thin)

    # Stroke 7: 口 底横 (closes bottom of 口)
    d.line([(kx0 + 2, ky1), (170, ky1 - 2), (kx1 - 2, ky1)], fill=ink, width=w_thin)

    return im


if __name__ == "__main__":
    im = draw_hou()
    im.save(
        "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
        "groups/G3_coords/attempts/p3_char_0235_后/01_后.png"
    )
