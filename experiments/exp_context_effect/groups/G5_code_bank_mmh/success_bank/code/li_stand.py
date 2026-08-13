"""Bank primitive: 立 (lì, 'stand' — 5 strokes: dian + heng + short-pie + short-dian + long-heng).

Promoted from p3_char_0198_立 (G5 B7 PASS, 2026-08-08). HIGH-freq
phonetic radical component.
Reuse targets: 立, 站, 位, 泣, 拉, 粒, 翌, 竖, 竣, 竟, 亲 (top), 童 (top),
妾 (top), 章 (top).
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _tapered_line(draw, head, tail, w_head, w_tail, steps=40):
    """Short calligraphic slant with linear taper (for stroke 3 and 4)."""
    for i in range(steps):
        t = i / (steps - 1)
        x = head[0] + t * (tail[0] - head[0])
        y = head[1] + t * (tail[1] - head[1])
        w = w_head + (w_tail - w_head) * t
        draw.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=(0, 0, 0))


def draw_li_stand(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top dian (center dot)
    draw_dian(draw, _tx(124.2, 73.8, ox, oy, scale), _tx(165.2, 98.1, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(9 * scale)),
              bow=max(2, int(4 * scale)), steps=48)
    # s2: upper heng (medium length)
    draw_heng(draw, _tx(80.6, 153.8, ox, oy, scale), _tx(220.0, 134.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s3: left short slant/dian
    _tapered_line(draw, _tx(93.8, 187.2, ox, oy, scale), _tx(118.4, 227.3, ox, oy, scale),
                  w_head=max(2, int(4 * scale)),
                  w_tail=max(2, int(10 * scale)), steps=44)
    # s4: right short slant/pie
    _tapered_line(draw, _tx(176.7, 164.9, ox, oy, scale), _tx(156.2, 253.4, ox, oy, scale),
                  w_head=max(2, int(4 * scale)),
                  w_tail=max(2, int(9 * scale)), steps=60)
    # s5: long baseline heng
    draw_heng(draw, _tx(33.4, 273.3, ox, oy, scale), _tx(271.0, 271.6, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
