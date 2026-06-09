"""
捺 (na) — atomic right-diagonal sweep with flat-kick tail, 斜捺 variant.

Tags: tag:atomic-stroke tag:捺 tag:斜捺 tag:flat-kick-tail tag:multi-segment
Component-of: (to fill — appears in 人, 入, 八, 大, 木, 不, 个, 介, 仁, ...)
Mastered: run_4 cycle 4, rubric 10/10
  (dunbi=2, hudu=2, taper=2, proportion=2, overall=2)

The canonical 楷书 斜捺 — the right-diagonal companion to 撇, with the
WIDTH PROFILE REVERSED (thin upper-left head → heavy lower-right tail)
and a distinctive **flat-kick** at the end (the 顿笔 + 出锋 release
that is 捺's diagnostic feature). Without the flat kick this stroke
reads as a flipped 撇 — not 捺.

This entry establishes the **two-Bézier-segment stitched stroke**
pattern: one main sweep + one short tail segment, joined tangentially
so the junction doesn't read as a notch. Many compound strokes
(横折, 竖钩, 横折钩, ...) will reuse this two-segment idea.

Reuse interface:
    from na import draw as draw_na
    draw_na(t)                          # head (-150,+200) → kick tip (+240,-172)
    draw_na(t, ox=100, oy=0)             # shift right 100 (e.g. right 捺 of 人)
    draw_na(t, ox=0, oy=0, scale=0.7)    # shorter 捺

Width profile (reversed vs 撇):
  Main sweep:   5 (head) → 8 → 14 → 18 (just before kick base)
  Flat kick:    18 → 16 (press hold, 25%) → 3 (release, 75%)

What this entry establishes:
- The reversed width profile (thin entry, heavy exit) for thicken-as-it-goes strokes.
- The two-segment stitched-stroke pattern with tangential junction control.
- The 顿笔 + 出锋 (press-hold then release) micro-profile for 捺's tail.
- Pairs with 撇 (c3) to unlock 人/八/入/大/木/不/个 in Phase 3.
"""

import sys
import os
from typing import Callable

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_na_main(s: float) -> float:
    """Main sweep width: THIN head → HEAVY just-before-kick.

    s ∈ [0, 1] from head (upper-left) to kick base (lower-right).
      - Entry (0–10%):    5 → 8  (thin, almost from a point — opposite of 撇)
      - Shaft (10–80%):   8 → 14
      - Pre-kick (80–100%): 14 → 18 (heaviest right before the kick base)
    """
    if s < 0.10:
        return 5.0 + (s / 0.10) * 3.0
    if s < 0.80:
        return 8.0 + ((s - 0.10) / 0.70) * 6.0
    return 14.0 + ((s - 0.80) / 0.20) * 4.0


def _w_na_kick(s: float) -> float:
    """Flat-kick width: heavy press (顿笔) → fine release (出锋).

    s ∈ [0, 1] over the short ~70 px horizontal kick segment.
      - Press hold (0–25%): 18 → 16  (the 顿笔)
      - Release (25–100%):  16 → 3   (the 出锋)
    """
    if s < 0.25:
        return 18.0 - (s / 0.25) * 2.0
    return 16.0 - ((s - 0.25) / 0.75) * 13.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 捺 as two stitched cubic Béziers (main sweep + flat kick).

    Canonical endpoints (before transform):
      Segment A (main sweep): (-150, +200) → (+170, -180)
        — controls A1=(-60,+80), A2=(+90,-150) place the centerline
        BELOW the straight head-to-tail line, giving a concave-up arc.
        A2 is pulled toward horizontal-right so the sweep arrives
        at the kick base tangentially (eliminates the junction notch).
      Segment B (flat kick): (+170, -180) → (+240, -172)
        — ~70 px horizontal release with tiny 8 px lift.
    """
    # Main sweep
    A0 = (-150.0 * scale + ox, 200.0 * scale + oy)
    A1 = (-60.0 * scale + ox, 80.0 * scale + oy)
    A2 = (90.0 * scale + ox, -150.0 * scale + oy)
    A3 = (170.0 * scale + ox, -180.0 * scale + oy)
    brushed_bezier(t, A0, A1, A2, A3, _w_na_main, samples=240)

    # Flat kick
    B0 = (170.0 * scale + ox, -180.0 * scale + oy)
    B1 = (195.0 * scale + ox, -180.0 * scale + oy)
    B2 = (220.0 * scale + ox, -175.0 * scale + oy)
    B3 = (240.0 * scale + ox, -172.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_na_kick, samples=160)
