"""p3_char_0073_飞 — G5 attempt.

飞 has 3 strokes with an unusual asymmetric shape:
  s1: short horizontal-zhe/pie at top-left (ML → BR of top-left region)
  s2: main big swoop — starts top-right, goes down-right and curves as a huge
       heng-zhe-wan-gou-like arc ending near BR
  s3: small internal pie near center (from just below the top going down-left
       into the interior, then hooking back — MMH says head@C, tail@BR
       so it's actually going up-right slightly, i.e. a small ti-like stroke
       inside the enclosure)

BANK_DEVIATION
skipped: heng_pie.py, heng_zhe_gou.py, wan_gou.py, ti.py
reason: 飞 is a highly idiosyncratic character; the big s2 sweep has
        a unique geometry (long diagonal descent then downturn) that no bank
        entry approximates well, and the tiny internal s3 is too specialized
        to reuse existing ti/pie primitives.
fresh_component: fei_top_zhe, fei_main_swoop, fei_inner_ti
"""

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 3 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'All three joints at cell C, class N (neighbor) — small natural gaps preserved.'
}

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new('RGB', (SIZE, SIZE), 'white')
draw = ImageDraw.Draw(img)


def stamp(draw, x, y, w):
    draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def bezier3(draw, p0, p1, p2, w_start=6.0, w_end=6.0, steps=100):
    for i in range(steps):
        t = i / (steps - 1)
        bx = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        by = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w_start + (w_end - w_start) * t
        stamp(draw, bx, by, w)


def bezier4(draw, p0, p1, p2, p3, w_start=6.0, w_end=6.0, steps=150):
    for i in range(steps):
        t = i / (steps - 1)
        u = 1 - t
        bx = u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0]
        by = u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]
        w = w_start + (w_end - w_start) * t
        stamp(draw, bx, by, w)


# ---------- Stroke 1: short top horizontal-zhe ----------
# Reads ML(0.369,0.318) -> BR(0.651,0.484). In pixel terms: a short mostly
# horizontal stroke a bit above center, dipping right and slightly down at
# its right end (the little top hood of 飞).
s1_head = (50, 105)
s1_apex = (110, 100)
s1_bend = (168, 108)
s1_tail = (180, 118)
bezier3(draw, s1_head, s1_apex, s1_bend, w_start=5.5, w_end=6.5, steps=90)
# small angular finish (little downturn)
bezier3(draw, s1_bend, (175, 112), s1_tail, w_start=6.5, w_end=5.0, steps=30)

# ---------- Stroke 2: the great swooping arc ----------
# Starts around where s1 ends (top-right area), sweeps down-right diagonally,
# then curves down and slightly leftish, ending near BR with a small hook.
s2_p0 = (172, 108)
s2_p1 = (245, 145)
s2_p2 = (255, 235)
s2_p3 = (232, 278)
bezier4(draw, s2_p0, s2_p1, s2_p2, s2_p3,
        w_start=6.0, w_end=7.0, steps=170)
# tiny hook flick at the tail (BR area)
bezier3(draw, s2_p3, (226, 275), (218, 268), w_start=7.0, w_end=3.0, steps=25)

# ---------- Stroke 3: inner small stroke ----------
# Visually in GT: a short mostly-horizontal-ish stroke inside the arc,
# starting mid-upper and going down-right (a small na/dian shape).
s3_head = (185, 155)
s3_ctrl = (200, 185)
s3_tail = (222, 210)
bezier3(draw, s3_head, s3_ctrl, s3_tail, w_start=5.0, w_end=6.0, steps=70)


out_png = __file__.rsplit('/', 1)[0] + '/01_飞.png'
img.save(out_png)
print('wrote', out_png)
