"""heng_zhe_wide — wide, sharp-cornered 横折 for mid-body use.

Distinct from `heng_zhe_short` (a small bezier ⌐ tuned for the top of
冖/宀) and from `heng_zhe_box` (口-frame corner). This variant is a
wide horizontal segment terminating in a near-square corner followed
by a straight vertical drop — the shape 五's s3 and similar mid-body
turns want.

Promoted from p3_char_0122_五 B5 PASS. Fresh_component name at
extraction: `heng_zhe_wide_inline_for_wu`.

Signature is endpoint-style with an explicit `corner` parameter:
  head = (x, y) top-left anchor of the horizontal segment
  tail = (x, y) bottom-right anchor of the vertical drop
  corner = (x, y) turning point (top-right of the L). If None, computed
    from (tail.x, head.y) — the L is right-angled.

Reuse targets: 五, 亚, 世, 巫, 甄, and any glyph with a wide mid-body
right-angle turn where the horizontal and vertical segments both need
to read as thick lines with a visible 顿笔 dab at the corner.
"""

from PIL import Image, ImageDraw  # noqa: F401


def draw_heng_zhe_wide(draw, head, tail, corner=None, width=8,
                        w_head=8, w_tail=8, corner_dab=6):
    """Wide 横折: heng segment head -> corner, then shu segment corner -> tail."""
    hx, hy = head
    tx, ty = tail
    if corner is None:
        corner = (tx, hy)
    cx, cy = corner

    # Horizontal (heng) segment
    draw.line([head, corner], fill='black', width=w_head)
    # Small end-cap at heng head
    r_h = max(1, w_head // 2)
    draw.ellipse([hx - r_h, hy - r_h, hx + r_h, hy + r_h], fill='black')

    # 顿笔 dab at corner (thicker than either segment)
    draw.ellipse([cx - corner_dab, cy - corner_dab,
                  cx + corner_dab, cy + corner_dab], fill='black')

    # Vertical (shu) segment
    draw.line([corner, tail], fill='black', width=w_tail)
    r_t = max(1, w_tail // 2 + 1)
    draw.ellipse([tx - r_t, ty - r_t, tx + r_t, ty + r_t], fill='black')
