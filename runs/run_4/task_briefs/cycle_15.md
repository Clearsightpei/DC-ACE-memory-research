# Cycle 15 — Focus: 二 (er, two)

## Phase 3. Two-phase cycle.

## Prerequisites verified
- 横 (heng) — `success_bank/code/heng.py`, mastered c1 10/10.
- 一 — `success_bank/code/yi.py`, mastered c14 10/10.

## What 二 is

Two horizontal strokes stacked: SHORT top + LONG bottom. The long-bottom convention is critical — if both hengs are the same length it doesn't read as 二.

## Skeleton targets (from GT)

- **Top heng:** (-90, +50) → (+50, +50). Length ~140 px (shorter).
- **Bottom heng:** (-130, -100) → (+130, -100). Length ~260 px (longer).
- Vertical gap between hengs: ~150 px.

## Brushwork phase composition

Use the mastered 横 with translate+scale:
```python
draw_heng(t, ox=-20, oy=+50, scale=0.35)   # top: shifted left slightly, 35% width
draw_heng(t, ox=0, oy=-100, scale=0.65)    # bottom: 65% width
```
(Adjust ox to center each heng over the GT positions.)

## Eval
`gt+ocr+vision`. Mastery: is_correct AND conf≥0.4 AND rubric≥7 no 0.

On mastery → `success_bank/code/er.py` (tag:character tag:2-strokes tag:heng-stacked).
