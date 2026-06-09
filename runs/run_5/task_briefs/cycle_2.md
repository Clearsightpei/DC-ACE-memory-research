# Cycle 2 — 3 tasks (all carry-overs)

## Phase
1

## Tasks

### Task 1 — 一 (yī) — CARRY OVER from c1
- GT PNG: `ground_truths/cycle_2/01_一.png`
- Output PNG: `attempts/cycle_2/01_一.png`
- Output code: `attempts/cycle_2/generated.py`
- Why this task: c1 attempt was unambiguously 一 in identity but failed the dunbi (右端收笔) rubric criterion — the right end TAPERED THIN instead of pressing thick. See `sandbox.md` for the specific width-profile fix.

### Task 2 — 二 (èr) — CARRY OVER from c1
- GT PNG: `ground_truths/cycle_2/02_二.png`
- Output PNG: `attempts/cycle_2/02_二.png`
- Why this task: composition was correct (top short, bottom long); same brushwork fix as task 1.

### Task 3 — 三 (sān) — CARRY OVER from c1
- GT PNG: `ground_truths/cycle_2/03_三.png`
- Output PNG: `attempts/cycle_2/03_三.png`
- Why this task: composition correct (three stacks, bottom longest); same brushwork fix as task 1.

## Eval

`vision+ocr+gt`.

## Critical brushwork fix (from Sandbox)

The c1 attempt used a **bell-curve width** (light → heavy → light). This is wrong for 楷书 横. The correct profile is **entry-press → moderate shaft → CLOSING-press at the right end** (right end is the HEAVIEST point of the stroke). Concretely:

```
w_profile(s) =
    16 over s ∈ [0.00, 0.10]   # entry press 起笔
    16 → 11 over s ∈ [0.10, 0.20]   # taper into shaft
    11 over s ∈ [0.20, 0.80]   # shaft 行笔
    11 → 19 over s ∈ [0.80, 0.95]   # press into closing
    19 over s ∈ [0.95, 1.00]   # closing press 收笔
```

The right end should be ~70% wider than the shaft. Keep the `max(3, w)` floor (§1.0) but in this case nothing should be at 3 — the smallest width is 11 at the shaft.

If the c1 `draw_heng` had small angled "feet" at the ends, KEEP them but make the right foot SHORT and at the closing-press width (19), not tapering down to thin.

## Self-preview budget

Max 2 internal iterations per task. **Open each attempt PNG and the GT PNG.** Specifically check: is the right end of each 横 the THICKEST point of the stroke? If yes, commit. If no, fix.
