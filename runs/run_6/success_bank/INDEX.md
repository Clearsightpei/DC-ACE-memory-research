# Success Bank — Index — run_6

Curator-owned. **Only mastered code lives here.** Entries are added when the Curator promotes them through the 5-gate (structural + judge panel).

## Hard mastery gate (run_6)

Promotion requires **ALL**:

1. `structural_pass == True` (stroke count + every anchor within 15 px + every joint within 20 px and in declared cell)
2. `judge_panel.unanimous_yes == True` (3 fresh-context skeptics)

OCR + visual_score are informational only. The c5/c20/c24 false-positive class is eliminated by gate 1.

## Architecture

Every entry stores **anchor notation** (no magic numbers). Anchors translate to turtle math-coords via `_anchor.py`.

- **Atomic strokes** (mastered c1–c6): horizontal stroke + vertical stroke + 撇/捺 diagonals + 提 + 点.
- **Compound strokes** (mastered c7–c13): 横折, 竖钩, 横折钩, 竖弯钩, 横撇, 竖折, 横折弯钩.
- **Characters** (c14+): compose mastered strokes by anchor.

The library is fully compositional: every entry calls only entries already in the bank.

## Entries

| name | file | tags | mastered |
|---|---|---|---|
| (anchor helper) | [code/_anchor.py](code/_anchor.py) | utility | run_6 init |
| 竖 | [code/shu.py](code/shu.py) | tag:atomic-stroke tag:shu tag:垂露 | c2 (structural ✓, v=0.83) |
| 横 | [code/heng.py](code/heng.py) | tag:atomic-stroke tag:heng tag:楷书 | c1 (structural ✓, panel 3/3 YES, v=0.83) |

(Empty otherwise — populated cycle by cycle.)

## Carry-over reference

Run_5's frozen Success Bank lives at `runs/run_5/success_bank/`. Run_6 does NOT import from it. The run_5 bank is a numeric-memory baseline for later comparison; run_6 starts fresh with structural memory.
