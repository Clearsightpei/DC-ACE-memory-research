# To-Be-Learned — run_5

Append-only log of characters that have failed ≥ 2 cycles. Each entry decomposes the character into Success-Bank components, checks whether each component was rendered correctly in the failed attempts, and names a root-cause hypothesis + next-cycle plan.

**Rule** (auto-memory `feedback-decompose-persistent-failures`): after 2 consecutive carry-overs on the same character, write here BEFORE retrying. Never skip a failure.

---

## 七 — cycle history: c12 (v=0.76 shu_wan_gou over-paint), c17 (v=0.79, just under 0.8)

**Decomposition**:
- heng — Success Bank ✓ (mastered c1 run_4 + carried). Rendered OK both cycles.
- shu_wan_gou (竖弯钩) — Success Bank ✓ (compound stroke, run_4 c10). Rendered OK structurally; brushwork over-paints thin GT skeleton.

**Root-cause hypothesis**: renderer ceiling. The shu_wan_gou's wide brushwork (run_4 11–19 px) over-paints the MMH GT skeleton (~5 px band) — the Dice term caps below the visual gate. c17 came within 0.006 of the gate.

**Plan for next cycle**: try a smaller-scale shu_wan_gou (scale ~0.8 → 0.6) so the brushwork covers a smaller surplus area, even if it slightly underfits. OR accept that this is at the renderer's ceiling and park 七.

---

## 口 — cycle history: c15 (v=0.68), c17 (v=0.66)

**Decomposition**:
- shu (left vertical) — Success Bank ✓. Rendered with scale 0.39-0.44; visually correct.
- heng_zhe (top + right) — Success Bank ✓ (compound stroke). Rendered scale 0.78-0.85.
- heng (bottom) — Success Bank ✓. Rendered scale 0.39-0.54.

**Root-cause hypothesis**: composition + renderer ceiling. The 口 box is small relative to canvas; three brushed strokes around the box perimeter produce ~3x the GT's thin-skeleton pixel area, killing Dice. Independent skeptic in c17 also flagged a visible top-right closure gap (heng_zhe's top-heng-left tip didn't reach shu's top tip).

**Plan for next cycle**: explicitly close the box at both top-left and bottom corners by overlapping endpoints. Also try heavier shu/heng_zhe scales so the box perimeter is dominated by black pixels (Dice might recover slightly).

---

## 中 — cycle history: c17 (v=0.83 PASSED numeric, panel 2/3 — NO from skeptic for right-side gap)

**Decomposition**: 口 components + central piercing shu. Inherits 口's left-corner-gap problem.

**Plan for next cycle**: fix 口 first (above). Once 口 closes cleanly, retry 中 by adding the central shu.

---

## 大 — cycle history: c14 (v=0.37), c16 (v=0.51, OCR'd as 人)

**Decomposition**:
- heng — Success Bank ✓.
- pie (撇) — Success Bank ✓.
- na (捺) — Success Bank ✓.

**Root-cause hypothesis**: renderer ceiling for full-size 撇+捺 (the apex-cross-through-heng layout). c16 even confused OCR into reading it as 人 — the heng didn't dominate enough above the X-cross. Brushed pie/na produce ~2.5x GT skeleton pixels, Dice can't recover.

**Plan for next cycle**: park 大 until either (a) renderer is changed, or (b) gate is relaxed for diagonal-heavy chars. Adding more cycles with current renderer will produce v ≤ 0.55 (c10/c14/c16 trend).

---

## 不 — cycle history: c14 (v=0.74), c16 (v=0.73)

**Decomposition**:
- heng — Success Bank ✓.
- pie — Success Bank ✓.
- shu — Success Bank ✓.
- dian — Success Bank ✓.

**Root-cause hypothesis**: same diagonal renderer ceiling as 大, slightly milder because 不 has more vertical+horizontal mass. Caps around 0.74.

**Plan for next cycle**: park 不 until 大 is solved (they share the renderer issue).

---

## 人 — cycle history: c10 (v=0.47), c16 (v=0.48 — but OCR is_correct now AND structurally correct: 撇 dominates, 捺 attaches mid-shaft)

**Decomposition**:
- pie — Success Bank ✓.
- na — Success Bank ✓.

**Root-cause hypothesis**: renderer ceiling. 人 is two big diagonals — the worst case for the brushed-vs-thin-GT Dice mismatch.

**Plan for next cycle**: park 人. The c16 attempt is STRUCTURALLY CORRECT and OCR'd correctly with high margin (0.98). Only the visual gate blocks it. This is a real data point for "renderer ceiling" — visual gate at 0.8 is structurally unreachable for pure-diagonal chars with brushed pie+na primitives.

---

## 末 — cycle history: c18 (v=0.63), c20 (v=0.83 numerical PASS, panel 1/3 YES — top heng not visibly longer than middle)

**c20 outcome**: Numerical gates passed (visual 0.83, OCR margin 1.00) BUT the judge panel caught a real flaw — 2 of 3 skeptics said the top heng was the same length as the middle heng, so the render reads as 木 rather than 末. **System working as designed: 100%-rule + panel skepticism caught a false positive that would have contaminated the bank.**

**Plan for next cycle**: increase top heng scale to ~0.75 (from 0.62) so it's UNAMBIGUOUSLY longer than the middle heng (scale 0.45). The c20 attempt was 0.62 vs 0.45 — visually similar. Need the contrast to be ~70% wider, not ~38%.

## (original c18 decomposition retained for record)
## 末 — cycle history: c18 (v=0.63)

**Decomposition**:
- 木 — Success Bank ✓ (c14 mastered).
- heng (top, long) — Success Bank ✓.

**Root-cause hypothesis**: composition error. The Drawer used `draw_mu(t)` verbatim and added a heng above. But MMH's 末 has the 木 component shifted DOWN; calling draw_mu unchanged kept 木 at its original mid-canvas position, so the top heng overlapped poorly.

**Plan for next cycle (c20)**: shift the 木 component down with explicit `draw_mu(t, oy=-40, scale=0.85)` then add the top heng at oy ~ +120. Same fix for 未.

---

## 未 — cycle history: c18 (v=0.65)

Same root-cause as 末. Plan: same fix, but top heng SHORTER (scale ~0.50 vs 末's ~0.85). The 末-vs-未 distinguisher is top heng length.

---

## 五 — cycle history: c19 (v=0.70, OCR'd as 左)

**Decomposition**:
- heng × 3 — Success Bank ✓.
- shu (or pie for slant) — Success Bank ✓.
- heng_zhe — Success Bank ✓.

**Root-cause hypothesis**: composition error. The Drawer's 5-call decomposition was over-complex AND OCR confused it with 左. The actual MMH 五 stroke order is: heng (top) + shu (slanting down) + heng (middle) + heng_zhe (right side wrapping into bottom heng). Use that decomposition cleanly.

**Plan for c20**: simpler decomposition. 4 turtle calls (one per stroke): heng + shu + heng + heng_zhe. Place per MMH measurement.

---

## 六 — cycle history: c19 (v=0.74, OCR 六 correct margin 1.00, just under visual gate)

**Decomposition**:
- dian (top dot) — Success Bank ✓.
- heng — Success Bank ✓.
- pie (lower-left) — Success Bank ✓.
- dian or short-na (lower-right) — Success Bank ✓ for dian.

**Root-cause hypothesis**: 六 has a small 撇 that adds to the diagonal pixel surplus but is short. visual 0.74 is right at the boundary. Could push past 0.8 with even smaller 撇 scale.

**Plan for next cycle**: scale the 撇 to 0.30 (down from 0.28 which was close), and try a smaller dian for the lower-right (matches MMH thin dot better).

---

## 九 — cycle history: c19 (v=0.46, OCR'd as 入)

**Decomposition**:
- pie — Success Bank ✓.
- heng_zhe_wan_gou — Success Bank ✓ (compound).

**Root-cause hypothesis**: composition error (Drawer noted 撇 and the heng_zhe_wan_gou's heng portion didn't intersect, but MMH's 九 has them crossing). Plus diagonal renderer ceiling.

**Plan for next cycle**: place 撇 head higher and to the right so it crosses the heng_zhe_wan_gou's heng segment near its left end. Then iterate.
