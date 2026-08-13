"""wo_gou — 卧钩 (lying hook).

A wide horizontal 'smile' curve: head at upper-left, belly dipping down
through the middle, tail rising to upper-right, then a small hook
flicking up-and-slightly-back-left from the tail.

Promoted from p3_char_0112_心 B5 PASS. Fresh_component name at
extraction: `wo_gou_for_xin`.

Signature is endpoint-style (matches other stroke primitives):
  head = (x, y) upper-left anchor
  tail = (x, y) upper-right anchor (before hook)
  belly_y = pixel y of the belly's bottom (dip point). Default is a
    "medium" dip; tune upward for shallower smile or downward for a
    deeper belly per composition.
  width = stroke weight (default 8)
  hook_up, hook_back = small terminal hook, up-left flick from tail

Reuse targets: 心, 必, 忘, 忆, 忙, 志, 思, 念, 忽, 恕 (any 心-based
character where 卧钩 forms the base line).
"""

from PIL import Image, ImageDraw  # noqa: F401 (kept for parity w/ other bank files)


def draw_wo_gou(draw, head, tail, belly_y=None, width=8, hook_up=26, hook_back=6):
    """卧钩 — wide smile-curve terminating with an up-left hook.

    If belly_y is None, computed automatically as ~y_max + 50 relative to
    the head/tail line (rough default; caller should override for
    calligraphic tuning).
    """
    hx, hy = head
    tx, ty = tail
    if belly_y is None:
        belly_y = max(hy, ty) + 60

    # Cubic bezier body
    c1 = (hx - 15, belly_y + 30)
    c2 = (hx + (tx - hx) * 0.80, belly_y + 30)
    body = []
    n = 80
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * hx + b1 * c1[0] + b2 * c2[0] + b3 * tx
        y = b0 * hy + b1 * c1[1] + b2 * c2[1] + b3 * ty
        body.append((x, y))

    # Small hook flick up-left from tail
    hook_tip = (tx - hook_back, ty - hook_up)
    hook_ctrl = (tx + 2, ty - hook_up * 0.4)
    hook = []
    for i in range(21):
        t = i / 20
        u = 1 - t
        x = u * u * tx + 2 * u * t * hook_ctrl[0] + t * t * hook_tip[0]
        y = u * u * ty + 2 * u * t * hook_ctrl[1] + t * t * hook_tip[1]
        hook.append((x, y))

    pts = body + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')
