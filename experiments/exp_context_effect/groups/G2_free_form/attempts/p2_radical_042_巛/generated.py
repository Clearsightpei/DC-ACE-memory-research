"""巛 (chuān) — 3-stroke radical.

GT analysis: three parallel "wavy" strokes. Each stroke has this shape:
  - starts upper-right
  - short descending-LEFT segment (like a mini-撇)
  - bends near the middle-top
  - long descending body curves down and slightly RIGHT to lower-left area
Overall silhouette per stroke is like a stretched ")" or shallow S: top
bulges right, bottom bulges left. Strokes get progressively slightly
shorter and higher toward the right (rightmost is highest).

Render each as ONE quadratic Bezier from (top_x + dx_top, top_y) through
a control point pulled LEFT (creating the top-right→bottom-left throw)
then landing at (bot_x, bot_y). Add a tapered thin→thicker→thin body:
thin top, medium middle, thin tip.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bez_quad(P0, P1, P2, r_fn, steps=500):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        r = r_fn(t)
        dab(x, y, r)


def chuan_element(top_x, top_y, bot_x, bot_y, bow=28):
    """Render one 巛 element as a curved stroke.

    top-anchor (upper-right) -> control (pulled LEFT below top) ->
    bot-anchor (lower-left).  Curvature 'bow' controls how sharply the
    top swings left before descending.
    """
    P0 = (top_x, top_y)
    P2 = (bot_x, bot_y)
    # Control point sits well to the LEFT of the chord midpoint, and
    # slightly above midway (so the curve bulges left in the upper half
    # and straightens at the bottom).
    mid_x = (top_x + bot_x) / 2
    mid_y = (top_y + bot_y) / 2
    ctrl = (mid_x - bow, mid_y - 15)
    # Taper: start thin (tip at top), thicken through middle, thin at
    # bottom tip. Peak radius ~ 4.5, tips ~ 1.4.
    def r_fn(t):
        # Bell-ish: r rises then falls
        peak = 4.8
        edge = 1.5
        # symmetric-ish around t=0.5
        return edge + (peak - edge) * (1 - (2 * (t - 0.5)) ** 2)
    bez_quad(P0, ctrl, P2, r_fn, steps=500)


# Three strokes, spaced ~55 px apart, right-hand-highest.
# Endpoints tuned to match GT silhouette.

# Stroke 1 (leftmost)
chuan_element(top_x=110, top_y=105, bot_x=80,  bot_y=250, bow=32)
# Stroke 2 (middle)
chuan_element(top_x=170, top_y=95,  bot_x=140, bot_y=245, bow=32)
# Stroke 3 (rightmost)
chuan_element(top_x=230, top_y=85,  bot_x=200, bot_y=235, bow=32)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_巛.png")
img.save(out)
print("saved", out)
