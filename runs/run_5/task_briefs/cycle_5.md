# Cycle 5 — 3 tasks

## Phase
1 (introducing 撇 + 捺 primitives — the diagonal sweep pair)

## Tasks — three subtly different 撇+捺 compositions

### Task 1 — 八 (bā)
- GT PNG: `ground_truths/cycle_5/01_八.png`
- Output PNG: `attempts/cycle_5/01_八.png`
- Output code: `attempts/cycle_5/generated.py`
- Distinguishing feature: **撇 and 捺 are SEPARATED at the top** — there is a visible gap between the two stroke heads, the shape opens like an upside-down V with a clear horizontal slot.
- Reusable: none yet (no 撇 or 捺 in the bank). Define both inline as new primitives.

### Task 2 — 人 (rén)
- GT PNG: `ground_truths/cycle_5/02_人.png`
- Output PNG: `attempts/cycle_5/02_人.png`
- Distinguishing feature: **撇 and 捺 SHARE the apex** at top (no gap between them). The 撇 is slightly steeper and longer; the 捺 sweeps further right.
- Reusable: 撇 and 捺 from task 1 (if you define them as reusable functions).

### Task 3 — 入 (rù)
- GT PNG: `ground_truths/cycle_5/03_入.png`
- Output PNG: `attempts/cycle_5/03_入.png`
- Distinguishing feature: **捺 dominates** — it starts at the top-left and sweeps all the way to the lower-right. The 撇 is a SHORTER stroke that attaches to the 捺's upper section as a secondary mark (it does NOT share the apex with the 捺). Looking at the GT: the 撇 head is BELOW the 捺's top, and the 撇 tail kicks down-left.
- Reusable: 撇 and 捺.

The three characters look superficially similar but the **structural distinctions are real and human-visible**. The run_5 strict-vision gate is set up specifically to catch these.

## Eval
`vision+ocr+gt`.

## New primitives needed

### 撇 (pie, diagonal sweep, tapered tip)
- Head (upper-right): heavy press, width 18.
- Shaft: 14 → 11 → 8.
- Tail (lower-left): taper to 3 (the §1.0 floor).
- Centerline: cubic Bezier with the controls placing the curve **above** the straight head-to-tail line (gentle concave-down arc).

### 捺 (na, right-diagonal with flat kick)
- Head (upper-left): thin, width 5.
- Sweep: grows 5 → 8 → 14 → 18 toward the tail.
- Tail (lower-right): heavy press, then a short flat kick (顿笔 + 出锋). The kick is a SECOND segment with its own width profile (18 → 16 hold for 25% → 3 release).
- Use the two-segment stitched pattern: segment A (main sweep, taper-up from 5 to 18) + segment B (flat kick, hold-and-release).

## Notes from Principle Bank

- **§1.0**: `max(3, w(s))` floor on every brushed stroke.
- **§1.1**: width-profile pattern (entry-press → shaft → closing-press) is the canonical 楷书 shape.
- **§2.1**: PIL-based reuse interface `(pil_draw, ox, oy, scale)`.
- **§2.2**: 竖 vs 横 patterns — not directly relevant here but good to keep in mind for future compositions.

## Self-preview budget

Max 2 internal iterations per task. **Open each attempt PNG and the GT PNG** and specifically check:
- 八: is there a clear GAP between 撇 and 捺 heads?
- 人: do 撇 and 捺 SHARE the apex?
- 入: does the 捺 visibly dominate (longer/higher) while the 撇 is a shorter secondary stroke?

If any of these distinguishing features is unclear, refine.
