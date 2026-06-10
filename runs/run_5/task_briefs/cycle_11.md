# Cycle 11 — 十 / 干 / 工 (横+竖 compositions)

## Hard gate (4-component)
- OCR is_correct AND ocr_margin >= 0.3
- visual_score > 0.8
- Judge panel unanimous YES

## Why this slate

c6 showed that 横-dominant chars clear visual > 0.8 with the brushed `heng.py`. c10 showed that diagonal-heavy chars cap at visual ~0.76 with brushed pie/na. So: build out the 横+竖 ladder while the foundations are easy.

- **十** = heng + shu (cross). 2 strokes.
- **干** = heng + heng + shu. 3 strokes.
- **工** = heng + heng + shu. 3 strokes (top heng shorter, like 二's top).

All three primitives (`heng.py`, `shu.py`) are mastered in run_4 with rubric 10/10. The 一/二/三 c6 entries also exist — reuse them where the composition contains a complete 一/二.

## Tasks

1. **十**: one 横 + one 竖, the 竖 crossing the 横's midpoint. Could reuse `yi.py` for the 横 if positioning matches.
2. **干**: two 横 stacked (top short, bottom long, like 二) + one 竖 through both. Could reuse `er.py` for the 横 pair.
3. **工**: top 横 (shorter), bottom 横 (longer), with a 竖 connecting their midpoints. Similar to 二 with a 竖.

## Renderer

Same turtle + postscript pattern. No subprocess. `t.reset()` between tasks.

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
# optionally:
from yi import draw as draw_yi
from er import draw as draw_er
```

## Self-preview budget

Max 2 iterations per task. Compare your PNG to GT. Verify:
- 十: 竖 crosses the 横 at its center
- 干: 竖 passes through both 横 (bottom 横 longer)
- 工: 竖 connects the midpoints of top and bottom 横

## Allowlist
- `task_briefs/cycle_11.md`, `task_briefs/cycle_11_dataset.json`
- `ground_truths/cycle_11/*.png`
- all `success_bank/code/*.py` (active entries — heng, shu, pie, na, ti, dian, compound strokes, yi, er, san)
- `success_bank/INDEX.md`, `principle_bank.md`, `sandbox.md`
- own attempt PNGs

## Forbidden
- `tools/` (quarantined)
- prior `attempts/cycle_*/` (do NOT read)
- `success_bank/_revoked/`
- `subprocess`, `os.system`
- judge_results, teaching_*, dashboard

## Output

`attempts/cycle_11/generated.py` + 3 PNGs.
