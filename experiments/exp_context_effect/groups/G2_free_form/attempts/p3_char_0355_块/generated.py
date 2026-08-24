"""
块 (kuài) = 提土旁 (土 on left, bottom stroke rises as 提)
          + 夬 (right: 横折 / 横 / 撇 / 捺)

7 strokes total:
  Left 提土旁 (3): 横, 竖, 提
  Right 夬  (4): 横折, 横, 撇, 捺

Notes from memory (form_catalog + drawer_memory):
- 提 (rising): starts low-left, rises to upper-right
- 撇 in "夬": short-mid flick from upper-middle to lower-left
- 捺 (right side of 夬): long diagonal, thickens toward end
- Left component is compressed (about 35-40% width, tall)
- Right component slightly wider, center of mass slightly higher
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, width=6):
    d.line([p1, p2], fill=BLACK, width=width)


def brush(points, widths):
    """Variable-width polyline via dabs."""
    n = len(points)
    assert n == len(widths)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        steps = max(2, int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            w = widths[i] + (widths[i + 1] - widths[i]) * t
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---------- LEFT: 提土旁 (compressed, x ~ 30..110) ----------

# stroke 1 — 横 (top horizontal of 土, short)
brush([(45, 105), (108, 100)], [5, 7])

# stroke 2 — 竖 (vertical of 土, goes from top-horiz down)
brush([(78, 92), (80, 195)], [6, 7])

# stroke 3 — 提 (rising: low-left to upper-right)
brush([(40, 205), (115, 178)], [10, 4])

# ---------- RIGHT: 夬 (x ~ 130..280) ----------

# stroke 4 — 横折 (top horizontal + short turn down at right end)
# horizontal segment
brush([(160, 108), (248, 102)], [5, 7])
# short vertical drop (the 折 tail — short, not full box)
brush([(248, 102), (245, 150)], [7, 6])

# stroke 5 — 横 (middle horizontal, shorter, inside the 夬)
brush([(170, 160), (245, 155)], [5, 7])

# stroke 6 — 撇 (from ABOVE top horizontal, sweeps down through both horizontals to lower-left)
brush([(210, 78), (145, 250)], [5, 3])

# stroke 7 — 捺 (long diagonal from crossing near middle-top, down to lower-right, thickens)
brush([(195, 140), (285, 268)], [4, 13])
# terminal taper flick
brush([(285, 268), (293, 272)], [13, 3])

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0355_块/01_块.png"
)
print("saved")
