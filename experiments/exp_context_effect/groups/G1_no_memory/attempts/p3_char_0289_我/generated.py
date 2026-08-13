"""Render 我 (wǒ) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 4  # stroke thickness


def line(p1, p2, w=TH):
    d.line([p1, p2], fill=BLACK, width=w)


def polyline(pts, w=TH):
    d.line(pts, fill=BLACK, width=w)


# 我 breakdown (7 strokes):
# 1. Top-right short 撇 (slash)
# 2. Long horizontal 横 across middle-left
# 3. Vertical 竖 (with slight left curve at bottom = 竖钩 style)
# 4. Left 提 (rising short stroke) at the bottom-left of vertical
# 5. Long 斜钩 (right-diagonal hook) from upper-mid down to lower-right, with hook up
# 6. 撇 from the crossing down to lower-left
# 7. Small 点 at top-right (over the hook end)

# 1. Top short 撇 (top-center, going down-left)
polyline([(160, 45), (140, 80)], w=TH)

# 2. Long horizontal 横 (middle band, slight tilt up-right)
polyline([(45, 130), (230, 115)], w=TH)

# 3. Vertical stroke 竖 (crosses horizontal, from ~top of horizontal down, tiny hook)
polyline([(95, 95), (90, 225), (82, 232)], w=TH)

# 4. Left short 提 (rising stroke lower-left of vertical)
polyline([(35, 195), (95, 175)], w=TH)

# 5. Long 斜钩 (diagonal from upper-middle to lower-right, ending with small hook up)
polyline([(135, 80), (175, 140), (215, 195), (250, 245), (262, 225)], w=TH)

# 6. 撇 from middle crossing down-left
polyline([(170, 135), (140, 195), (110, 260)], w=TH)

# 7. Small 点 upper-right (a short diagonal dot)
polyline([(215, 65), (232, 82)], w=TH+1)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_我.png")
img.save(out_path)
print(out_path)
