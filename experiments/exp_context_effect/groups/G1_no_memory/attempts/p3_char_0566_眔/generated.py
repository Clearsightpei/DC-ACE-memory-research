"""G1 render of 眔 (top: 罒 net radical; bottom: 氺 water)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = "black"
lw = 4

def line(p1, p2, width=lw):
    d.line([p1, p2], fill=ink, width=width)

# ---------- TOP: 罒 (net radical) as a wide rectangle with 2 vertical dividers ----------
# Rectangle spans roughly x=80..220, y=55..135
L, R = 80, 220
T, B = 55, 135

# Left vertical (slight lean)
line((L, T), (L - 5, B))
# Top horizontal
line((L, T), (R + 3, T - 2))
# Right vertical with a small hook top-right
line((R + 3, T - 2), (R + 5, B))
# Bottom horizontal (closes rectangle)
line((L - 5, B), (R + 5, B))
# Two inner verticals
line(((L + R) // 3 + 15, T + 4), ((L + R) // 3 + 12, B - 2))
line((2 * (L + R) // 3 - 5, T + 4), (2 * (L + R) // 3 - 8, B - 2))

# ---------- BOTTOM: 氺 (water variant) ----------
# Center vertical hook (main stroke)
cx = 150
line((cx, 145), (cx, 260))
# Little hook at bottom of vertical (going left)
line((cx, 260), (cx - 8, 252))

# Upper-left short diagonal (dot-like)
line((cx - 20, 165), (cx - 35, 185))
# Upper-right short diagonal
line((cx + 20, 165), (cx + 35, 185))

# Lower-left long sweeping diagonal (撇)
line((cx - 5, 195), (cx - 55, 275))
# Lower-right long diagonal (捺)
line((cx + 5, 195), (cx + 60, 275))

out_path = os.path.join(os.path.dirname(__file__), "01_眔.png")
img.save(out_path)
print("Wrote", out_path)
