"""Render 学 (xue) to 300x300 PNG.
Layout matching GT:
- Top ~y=40-90: three small tick strokes (丷 + right small)
- Middle ~y=100-140: 冖 cover with small left descender + right hook down
- Bottom ~y=140-260: 子 (top 乛, main vertical-hook, long horizontal through middle)
"""
from PIL import Image, ImageDraw
import os, math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
INK = "black"
LW = 5

def line(pts, width=LW):
    draw.line(pts, fill=INK, width=width, joint="curve")

def bezier(p0, p1, p2, n=40):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t**2*p2[0],
             (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t**2*p2[1])
            for t in (i/n for i in range(n+1))]

# --- Top 3 dot strokes ---
# Left dot (slant down-left)
line([(115, 55), (100, 85)])
# Middle dot (small vertical/slight right slant)
line([(155, 50), (152, 80)])
# Right dot (slant down-right)
line([(185, 55), (200, 85)])

# --- 冖 cover ---
# left small descender
line([(78, 100), (88, 118)])
# long horizontal top, slight downward slope
line([(72, 118), (238, 128)])
# right hook down (short)
line([(238, 128), (235, 148)])

# --- 子 component ---
# Top 乛 of 子: short horizontal then hook down-left
line([(115, 158), (200, 162)])
line([(200, 162), (185, 178)])

# Main vertical hook of 子: curves down from top-right and hooks left at bottom
start = (175, 150)
mid   = (168, 220)
end   = (100, 265)
line(bezier(start, mid, end), width=LW)
# tiny hook up at end
line([(100, 265), (118, 258)])

# Long horizontal through middle of 子 (一)
line([(45, 215), (275, 213)])

img.save(os.path.join(os.path.dirname(__file__), "01_学.png"))
print("saved")
