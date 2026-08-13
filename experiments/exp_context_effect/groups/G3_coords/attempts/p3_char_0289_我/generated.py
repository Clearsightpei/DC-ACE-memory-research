# p3_char_0289_我 — 7 strokes: 撇 + 横 + 竖钩 + 提 + 斜钩 + 撇 + 点
# GT shows thin uniform strokes (~4-5 px). Compose fresh (inline) —
# no direct identity alias in bank. Reuse tapered_bezier/tapered_line
# helpers (P12: uniform thin widths).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _shared_helpers import tapered_bezier, tapered_line

W = 4  # uniform thin width per P12 (MMH GT)

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# Math coords: center=(150,150), +y up. Composition targets:
# left cluster = 手-like (short-pie + heng + shu-hook + ti)
# right cluster = 戈-like (xie-gou + pie + dian)

# --- LEFT: 手-side ---
# S1: short 撇 top-left of char (above heng), tapered.
tapered_bezier(d, (-15, 82), (-28, 65), (-45, 48), w_head=4, w_tail=3, n=32)

# S2: long 横 across middle, slight upward tilt.
tapered_line(d, (-88, 30), (48, 38), 4, 4)

# S3: 竖钩 — vertical from just above heng, straight down, hook up-left.
tapered_line(d, (-38, 55), (-46, -78), 4, 4)
# small hook back up-left
tapered_line(d, (-46, -78), (-58, -66), 4, 3)

# S4: 提 — rising stroke bottom-left going up-right toward center.
tapered_line(d, (-78, -46), (-8, -22), 5, 3)

# --- RIGHT: 戈-side ---
# S5: 斜钩 — long belly bezier from top-mid to bottom-right, then hook up.
tapered_bezier(d, (-8, 82), (35, -10), (78, -80), w_head=4, w_tail=5, n=64)
# hook up (nearly vertical, slightly left)
tapered_line(d, (78, -80), (72, -55), 5, 3)

# S6: 撇 — small inside 戈, short from upper-right down-left toward heng.
tapered_bezier(d, (58, 62), (42, 45), (22, 32), w_head=4, w_tail=3, n=32)

# S7: 点 — small dot upper-right corner.
tapered_line(d, (78, 85), (92, 70), 3, 6)

img.save(os.path.join(os.path.dirname(__file__), "01_我.png"))
