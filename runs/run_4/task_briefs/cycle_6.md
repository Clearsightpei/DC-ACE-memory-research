# Cycle 6 — Focus: 点 (dian, dot)

Phase 1 atomic. Single-phase (eval=vision). Self-preview 2.

## What 点 is

A short teardrop-shaped dot. Used as decorative strokes inside many characters (火's two 点, 寸's 点, 之 character starts with one, etc.). Very different from 横/竖/撇/捺 — it's SHORT.

Canonical form (standard 右点 — "right dot", tilted ~45° down-right):
- **Direction:** upper-left (thin entry) → lower-right (heavy belly) with a quick taper back.
- **Length:** ~60 px (much shorter than the other atomics).
- **Brushwork:** thin entry (3) → heavy belly (14) by ~30% s → taper to fine tail (3) by s=1.0. Tilted ~45° down-right.

## Suggested coords
- Entry: (-25, +20). 
- Tail: (+30, -25).
- Belly maximum width 14 at s≈0.3.

## Width profile
```
w_dian(s):
  if s < 0.30: return 3 + (s/0.30) * 11   # 3 → 14 entry buildup
  return 14 - ((s-0.30)/0.70) * 11        # 14 → 3 taper out
```

## Reuse
`from heng import brushed_bezier`. ONE Bézier segment is enough.

On mastery → `success_bank/code/dian.py` (tag:atomic-stroke tag:点 tag:右点).
