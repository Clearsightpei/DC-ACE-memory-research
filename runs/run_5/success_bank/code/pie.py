"""
撇 (pie) — atomic diagonal stroke, upper-right → lower-left, 斜撇 variant.

Tags: tag:atomic-stroke tag:撇 tag:斜撇 tag:tapered-tip
Component-of: (to fill — appears in 人, 入, 八, 大, 木, 不, 个, 仁, 介, ...)
Mastered: run_4 cycle 3, rubric 10/10
  (dunbi=2, hudu=2, taper=2, proportion=2, overall=2)

The canonical 楷书 斜撇 — a diagonal sweep with weighted head, gentle
concave-down curve, and a smooth taper to a fine point at the tail.
This is the first Success Bank entry with a TRUE tapered tip (vs the
symmetric barbells of 横 and 竖); it establishes the
heavy-head-to-pensize-3 pattern reused by 提 and any tail-tapered
compound stroke.

Reuse interface:
    from pie import draw as draw_pie
    draw_pie(t)                          # head (+150,+200) → tail (-180,-180)
    draw_pie(t, ox=-100, oy=0)           # shift left 100 px (e.g. left 撇 of 人)
    draw_pie(t, ox=0, oy=0, scale=0.7)   # shorter 撇

Width profile: head dunbi 18 → 14 (first 12%), shaft 14 → 11 (next
76%), tail taper 11 → 3 (final 12%, pensize-3 floor enforced by
brushed_bezier).

What this entry establishes:
- The heavy-head/light-shaft/fine-tail pattern for tapered-tip strokes.
- The "extend taper to final 12% (not 5%)" choice for a smoother
  visual taper — this was the c3 self-preview refinement that
  bumped iter-1's slightly-abrupt taper to canonical.
- Confirms self-preview iteration loop is producing measurable
  refinement (iter-1 → iter-2 both observable in the rubric notes).
"""

import sys
import os
from typing import Callable

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_pie_canonical(s: float) -> float:
    """斜撇 width profile.

    s ∈ [0, 1] from head (upper-right) to tail (lower-left).
      - Head dunbi (0–12%): peak 18 → 14.
      - Shaft (12–88%):     14 → 11.
      - Final taper (88–100%): 11 → 3 (rapid taper to fine point;
        the brushed_bezier max(3, …) floor enforces the minimum).
    """
    if s < 0.12:
        return 18.0 - (s / 0.12) * 4.0
    if s < 0.88:
        return 14.0 - ((s - 0.12) / 0.76) * 3.0
    return 11.0 - ((s - 0.88) / 0.12) * 8.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0,
         w_profile: Callable[[float], float] = _w_pie_canonical):
    """Draw 撇 with optional translate (ox, oy) and uniform scale.

    Canonical endpoints (before transform):
        P0 head = (+150, +200)
        P3 tail = (-180, -180)
    Control points (P1, P2) place the centerline slightly above the
    straight head-to-tail line → gentle concave-down arc.
    """
    P0 = (150.0 * scale + ox, 200.0 * scale + oy)
    P3 = (-180.0 * scale + ox, -180.0 * scale + oy)
    P1 = (30.0 * scale + ox, 130.0 * scale + oy)
    P2 = (-90.0 * scale + ox, -30.0 * scale + oy)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=240)
