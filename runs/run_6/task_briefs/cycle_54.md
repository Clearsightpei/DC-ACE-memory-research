# Cycle 54 — Focus: 人 (rén) — apex_share verification

## Phase
2 — character composition.

## MMH stroke count
2

## Strokes
1. `draw_pie(t, from=('TC', 0.384, 0.604), to=('BL', -0.26, 1.168))`
2. `draw_na(t,  from=('TC', 0.348, 0.604), to=('BR', 1.3, 1.188))`

## Overrides
- apex_share: s2.from.y = s1.from.y = 89.6 (canvas math-coords).
  (raw MMH heads: pie at y=+89.6 (top), na at y=-14.0 (middle); the
   raw render leaves a ~100 px vertical gap between heads. The
   canonical handwritten 人 expects both strokes to start from a shared
   apex. We lift na.head.y to match pie.head.y. Heads end up very
   close (3.6 px horizontal gap) — essentially touching at the apex.)

## Joints (classified)
- s1.mid(0.31) ⇆ s2.head @ C: N (d=51.2, would expect ~20 px gap, but
  apex_share override converts this to a near-touch at apex.)

## Eval gates
- Stroke count: 2.
- OCR: informational.
- Panel: 3/3 YES with explicit per-char rule (人 = strokes MEET at apex,
  distinct from 八 where they don't meet, and 入 where 撇 attaches to 捺).

## Output
attempts/cycle_54/generated.py + attempts/cycle_54/01_人.png
