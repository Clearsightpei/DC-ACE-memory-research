"""力 (lì, "strength" as Phase-3 CHAR, 2画) — B4 retry PASS promotion.

Thin wrapper: char-context reuse of li.py (already a B3 retry PASS as
Phase-2 radical p2_radical_025_力). Retry-1 lesson: drawer originally
skipped bank retrieval; fix = call li.py with its DEFAULT anchors,
which ARE the MMH anchors for the standalone character 力.

Strokes: 横折钩 + 撇 (P weld at C — 撇 pierces 横 descent).
"""
from li import draw_li


def draw_li_char(draw, **overrides):
    # li.py DEFAULTS are the MMH-standalone anchors for 力; TR1's override
    # rule doesn't apply here (this IS the target item, not a reuse in a
    # different composition).
    draw_li(draw, **overrides)
