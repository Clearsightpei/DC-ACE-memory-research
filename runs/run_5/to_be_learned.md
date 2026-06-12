# To-Be-Learned — run_5 (FROZEN at run_5 end, reconciled)

This file is now the final research record for run_5 before run_6 begins. It has been reconciled on 2026-06-10 against the live Success Bank and against the user's reread of c20–c25 promotions.

**Reconciliation rules applied** (per the run_6 plan, see `~/.claude/plans/should-i-install-rapid-lexical-lantern.md`):

1. **Prune on mastery**: entries for characters that have since been promoted to `success_bank/code/` are moved to `to_be_learned_resolved.md` and removed from this file.
2. **Renderer-ceiling tag**: chars that have OCR is_correct + panel-unanimous-YES but failed only on visual_score (because brushed primitives over-paint thin MMH skeletons) are moved to the **Parked** section. They are not character-identity failures — they're a measurement-system limit that run_6's structural gates will replace.
3. **Composition-error retries**: chars where the failure mode was actually structural (extra strokes, missing strokes, wrong topology) stay in the **Retry** section but are flagged for re-attempt under run_6's 米字格 + joint-spec architecture.
4. **Suspect promotions called out**: 五 (c20) and 丘 (c24) were promoted to the Success Bank, but the user's c25-end review identified extra strokes (5 vs MMH 4, 6 vs MMH 5). These are documented in the **Suspect — false positives the 4-gate missed** section and will be revisited in run_6 cycle 0.

The 4-gate that produced these false positives is being replaced. The structural gates 4+5 in run_6 (stroke-count + anchor placement + joint placement) would have rejected both at the numeric step.

---

## Parked — structurally correct, renderer ceiling

These chars are visually correct to a human eye but failed `visual_score > 0.8` because the brushed Bézier primitives (width 11–19 px) over-paint MMH's thin (~5 px) skeleton GT, capping Dice and the blended visual score. Under run_6's anchor-placement + joint-placement gates, these will all be re-evaluated.

- **七** — c12 v=0.76, c17 v=0.79. heng + shu_wan_gou. Structure clean; renderer ceiling.
- **口** — c15 v=0.68, c17 v=0.66. shu + heng_zhe + bottom heng. Closed box, but brushwork over-paints; one c17 skeptic also flagged a small top-right closure gap.
- **人** — c10 v=0.47, c16 v=0.48. pie + na with 捺 head attaching to 撇 upper third. c16 OCR'd correctly with margin 0.98 AND structure matches MMH (the joint detector confirms `s2.head ⇆ s1.mid(0.31) @ C`). Pure renderer ceiling.
- **大** — c14 v=0.37, c16 v=0.51. heng + pie + na. Full-size diagonal pair; brushed over-paint is severe.
- **不** — c14 v=0.74, c16 v=0.73. heng + pie + shu + dian. Same diagonal ceiling, slightly milder.
- **本** — c21 v=0.76, c22 v=0.76, c25 v=0.76. draw_mu + small bottom dash. 4th attempt at the same brushed-mu+dash ceiling.
- **天** — c25 v=0.72. heng + heng + pie + na. Same diagonal renderer ceiling.

## Retry under run_6 architecture — composition errors

These chars failed because the Drawer's structural decomposition was wrong (extra strokes, wrong stroke order, OCR landing on the wrong character). They are candidates for re-attempt in run_6 with the joint-spec brief.

- **中** — c17 v=0.83 passed numeric, panel 2/3 NO because of a right-side gap. Inherits 口's closure problem. Will be cleanly buildable in run_6 once 口 is mastered with the new gate.
- **升** — c23 v=0.55, OCR returned nothing. Drawer's decomposition produced something readable as 牛 / 斗 rather than 升. Need joint spec.
- **千** — c23 v=0.67, OCR returned 十. The 撇 was too small / misplaced and OCR collapsed to 十.
- **正** — c23 v=0.72, OCR returned 丘. Decomposition was over-complex and overlapped 丘.
- **九** — c19 v=0.46, OCR returned 入. Drawer noted the 撇 and the heng_zhe_wan_gou's heng portion didn't intersect, but MMH's 九 has them crossing. Run_6 joint spec for 九 will name the crossing explicitly.

## Suspect — false positives the run_5 4-gate missed

These were promoted to the Success Bank in run_5 but the user's c25-end review identified structural flaws. Run_6's stroke-count gate would reject both. These entries are not deleted from the Success Bank (run_5 is frozen as a research record showing the 4-gate's failure modes), but they are flagged here and will be re-mastered fresh in run_6.

- **五** (success_bank/code/wu.py): Drawer used 5 turtle calls; MMH has 4 strokes (`points/stroke=[5, 6, 8, 7]`). The extra "closing bottom heng" was tucked into existing ink, absorbed by Dice's 21-px dilation, and the 3-judge panel was not asked to count strokes. Panel said 3/3 YES.
- **丘** (success_bank/code/qiu.py): Drawer used 6 turtle calls; MMH has 5 strokes (`points/stroke=[8, 7, 6, 5, 6]`). Extra right shu between middle and bottom heng. Panel said 3/3 YES.

Both are catalogued as part of run_5's research story (what the 4-gate let through) and will be retrained from cycle 0 in run_6 under the new 5-gate.
