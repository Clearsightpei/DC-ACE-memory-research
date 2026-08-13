"""伥 = 亻 + 长. Right half 长 has no chronic yet (candidate per errata);
render fresh via MMH anchors. Left 亻 draws inline with ren_side-style
curves (avoid cross-package import from attempts dir).

6 strokes (MMH):
  s1 亻撇 TL(0.86,0.76) → BL(0.21,0.04)
  s2 亻竖 ML(0.65,0.63) → BL(0.72,0.94)
  s3 长短撇 TR(0.05,0.90) → C(0.61,0.52)
  s4 长横 ML(0.98,0.84) → MR(0.55,0.71)
  s5 长竖提 TC(0.38,0.74) → BC(0.92,0.55)   (long descend with flick)
  s6 长捺 C(0.60,0.85) → BR(0.81,0.60)
"""
import os, sys
from PIL import Image, ImageDraw

CANVAS = 300
_CELL = CANVAS / 3.0
_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}

def A(a):
    cell, xf, yf = a
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)

def quad_bezier(p0, p1, p2, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts

def polyline(draw, pts, widths):
    for i in range(len(pts)-1):
        w = max(1, int(round((widths[i]+widths[i+1])/2.0)))
        draw.line([pts[i], pts[i+1]], fill=(0,0,0), width=w)
    for (x,y), w in zip(pts, widths):
        r = max(1, w/2.0)
        draw.ellipse([x-r,y-r,x+r,y+r], fill=(0,0,0))

def fat_line(draw, p0, p1, width):
    draw.line([p0, p1], fill=(0,0,0), width=int(round(width)))
    r = width/2.0
    for (x,y) in (p0,p1):
        draw.ellipse([x-r,y-r,x+r,y+r], fill=(0,0,0))

def pie(draw, head, tail, hw=11, tw=1, curve=0.14, n=56):
    p0 = A(head); p2 = A(tail)
    mx = (p0[0]+p2[0])/2 + curve*(p2[1]-p0[1])
    my = (p0[1]+p2[1])/2 - curve*(p2[0]-p0[0])
    pts = quad_bezier(p0, (mx,my), p2, n=n)
    widths = [hw + (tw-hw)*i/n for i in range(n+1)]
    polyline(draw, pts, widths)

def heng(draw, head, tail, w=9):
    fat_line(draw, A(head), A(tail), w)

def shu(draw, head, tail, w=9):
    fat_line(draw, A(head), A(tail), w)

def na(draw, head, tail, hw=3, tw=13, n=48):
    p0 = A(head); p2 = A(tail)
    # slight belly to left (na sags then thickens)
    mx = (p0[0]+p2[0])/2 - 0.08*(p2[1]-p0[1])
    my = (p0[1]+p2[1])/2 + 0.08*(p2[0]-p0[0])
    pts = quad_bezier(p0, (mx,my), p2, n=n)
    widths = [hw + (tw-hw)*i/n for i in range(n+1)]
    polyline(draw, pts, widths)

def shu_ti(draw, head, tail, w=9):
    # long descend then flick up-right at the end. Model as bezier from
    # head straight down through a knee, then out to tail.
    p0 = A(head); pt = A(tail)
    # knee: same x as head, y near tail y
    knee = (p0[0], pt[1] - 10)
    pts = quad_bezier(p0, knee, pt, n=48)
    widths = [w]*(len(pts)-6) + [max(2, w - i) for i in range(6)]
    widths = widths[:len(pts)]
    polyline(draw, pts, widths)


def main(out_png):
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    strokes = []

    # s1: 亻 pie
    pie(d, ('TL',0.86,0.76), ('BL',0.21,0.04), hw=12, tw=1, curve=0.10); strokes.append('s1')
    # s2: 亻 shu
    shu(d, ('ML',0.65,0.63), ('BL',0.72,0.94), w=9); strokes.append('s2')
    # s3: 长 short pie (top-right down to center)
    pie(d, ('TR',0.05,0.90), ('C',0.61,0.52), hw=10, tw=2, curve=0.08); strokes.append('s3')
    # s4: 长 heng across middle
    heng(d, ('ML',0.98,0.84), ('MR',0.55,0.71), w=9); strokes.append('s4')
    # s5: 长 shu_ti (long descent with flick)
    shu_ti(d, ('TC',0.38,0.74), ('BC',0.92,0.55), w=9); strokes.append('s5')
    # s6: 长 na
    na(d, ('C',0.60,0.85), ('BR',0.81,0.60), hw=3, tw=13); strokes.append('s6')

    assert len(strokes) == 6, f"expected 6 strokes, got {len(strokes)}"

    img.save(out_png)
    print(f'wrote {out_png}')


SELF_CHECK = {
    'visual_ok': None,           # to be filled after render
    'stroke_count_ok': True,     # 6 strokes
    'endpoint_mismatches': [],   # anchors used verbatim from MMH
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'MMH anchors verbatim; 长 half rendered fresh (no chronic promoted yet).',
}


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    main(os.path.join(here, '01_伥.png'))
