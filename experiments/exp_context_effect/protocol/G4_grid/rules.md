# G4 — Grid-Bank Memory (米字格)

## Overview

You are the **G4 (grid-bank)** group. You have a curator and a
**three-bank memory** with **米字格 (grid) anchor notation** and joint
specifications. This is the run_6 architecture.

Read this together with `../shared_rules.md`.

## The three-bank architecture

```
groups/G4_grid/
├── success_bank/
│   ├── INDEX.md
│   └── code/
│       ├── yi.py            ← draw_yi(t)  — using 米字格 anchors
│       ├── kou.py
│       └── ...
├── principle_bank.md
├── sandbox.md
├── errata.md                ← 错题集
├── retry_log.jsonl
├── curator_satisfaction_log.jsonl
└── attempts/
    └── <item_id>/generated.py, 01_<item>.png
```

## 米字格 anchor notation (MANDATORY)

The character region is divided into **9 cells** (`TL`, `TC`, `TR`,
`ML`, `C`, `MR`, `BL`, `BC`, `BR`). Every stroke's endpoints are
recorded as `(cell, x_frac, y_frac)` — cell name plus within-cell
position. Example:

```python
# success_bank/code/kou.py — 口 (kou, "mouth")
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng

def draw_kou(t):
    draw_shu(t, ('ML', 0.368, 0.212), ('BL', 0.844, 0.94))
    draw_heng_zhe(t, ('ML', 0.668, 0.272), ('MR', 0.488, 0.312), ('BR', 0.096, 0.456))
    draw_heng(t, ('BL', 0.928, 0.808), ('BR', 0.428, 0.652))
```

Anchor helper: `_anchor.anchor_to_xy((cell, x_frac, y_frac))` returns
turtle math-coords. This helper is available under the shared
primitives.

## Joint specs (part of memory)

Every entry in the Success Bank includes a **joint list** describing
where strokes meet, using the P/T/N classification:

- **P (Piercing)** — two strokes cross (e.g. 十 crossing).
- **T (Tangent)** — one stroke's tip touches another's body.
- **N (Neighbor)** — two strokes end near each other with a small
  natural gap (e.g. 口's non-welded corners).

The joint list can be represented inline in the docstring or as a
separate section in each `.py`. Example:

```python
# 口 joints:
#   stroke1.tail @ BL  ⇆  stroke2.corner @ BR   (P — welded)
#   stroke2.tail @ BR  ⇆  stroke3.head @ BL     (N — small gap OK)
#   stroke1.head @ ML  ⇆  stroke2.head @ ML     (N — small gap OK)
```

## Drawer role

1. **Read `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`,
   and relevant `success_bank/code/*.py`** for compositional reuse.
2. Look at the GT PNG.
3. Write `attempts/<item_id>/generated.py` using 米字格 anchors,
   composing bank entries where appropriate.
4. Run the script. Return the PNG.

## Curator role — merged structural + panel check

Called after every attempt.

Your judgment logic **combines** what were three separate agents in
run_6 (structural checker + 3 panel skeptics) into a single call:

1. **Structural check**: does the render's stroke count match MMH?
   Do the declared anchors land in the right cells (within tolerance)?
   Do the joint classes look right visually?
2. **Panel-skeptic check**: viewing the attempt alone, would you
   identify it as the target item? Would you accept it as a "correct"
   render given calligraphic norms?
3. Emit a single PASS/FAIL verdict with a one-sentence reason.

This is logged to `curator_satisfaction_log.jsonl`. **It is NOT the
gate.** The human's verdict is the gate. Your verdict is used for
post-hoc calibration analysis.

On **human PASS**:
- Write `success_bank/code/<item>.py` with 米字格 anchors + joint
  spec.
- Append to `success_bank/INDEX.md`.
- Update `principle_bank.md`.
- Reset `sandbox.md`.

On **human FAIL**:
- Read the human's short comment.
- Update `sandbox.md` with the specific fix.
- Return a "guidance for next attempt" message.

## 错题集

Standard rules — see `../shared_rules.md`.

## Explicit constraints

- You may NEVER use raw coordinate offsets like `(ox + 3, oy - 21)`.
- You must use `(cell, x_frac, y_frac)` anchor tuples.
- You must declare joint classes for multi-stroke items.
- Your Success Bank entries must be compositional: complex characters
  reuse component characters/radicals from the bank where possible.

## Reference materials

Predecessor run_6 established these conventions:

- 米字格 cell definitions: `runs/run_6/success_bank/code/_anchor.py`
- Joint classification (P/T/N) with MMH-derived thresholds:
  `runs/run_6/tools/classify_joints.py`
- Corner-cell rule for compound-stroke bends: `runs/run_6/MMH_ROLE.md`
- Deterministic structural judge: `runs/run_6/tools/structural_judge.py`
  (calibrated to 85.5% human agreement)

You may reference these files for the definitions but do NOT copy
run_6's mastered entries into your Success Bank. **G4 starts empty**
per the experiment's fair-comparison rule.
