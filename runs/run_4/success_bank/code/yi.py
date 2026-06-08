"""
一 (yi) — the simplest character (single 横 stroke).

Tags: tag:character tag:1-stroke tag:heng tag:component-of(三, 二, 王, 工, 干, 上, 下, ...)
Mastered: run_4 cycle 14, rubric 10/10, OCR 一 conf 0.77, visual_score 0.85
First Phase-3 character. FIRST two-phase cycle (skeleton + brushwork).

一 IS a single 横 stroke. This entry is a thin wrapper that calls
the mastered c1 heng at the GT-derived position (y=-100, scale 0.8).

Reuse:
    from yi import draw as draw_yi
    draw_yi(t)                            # standalone 一
    draw_yi(t, ox=0, oy=+150, scale=0.6)  # inset top heng (e.g. 二's top, 三's top)

The brushed widths come straight from heng.py; only translate/scale
are applied per §2.1.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import draw as draw_heng


def draw(t, ox: float = 0.0, oy: float = -100.0, scale: float = 0.8):
    """Draw 一 by translating/scaling the mastered c1 heng."""
    draw_heng(t, ox=ox, oy=oy, scale=scale)
