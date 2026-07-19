# Errata Scan — G3 (coord-bank) — Curriculum Position 50

Scan performed at position 50 (end of bootstrap window / start of B1 main
curriculum). Upcoming 50 items: 019 匚 → 068 扌 (positions 51-100).

## Errata inventory & decisions

### Phase-1 hook fails (all attempted in batch-6 refresh)

Batch-6 refresh log timestamped 2026-07-16. Treating those as most-recent
retries; per shared_rules.md 50-item cooldown, they are locked until at
least position ~82. Every one is SKIP for that reason alone; additionally
none are prospectively related to the upcoming 51-100 items (which are
frames, radicals, and simple characters — none of them require the
弯钩/斜钩/折折钩 zigzag stroke family as a sub-component).

| item_id | decision | reason |
|---|---|---|
| p1_stroke_16_斜钩 | SKIP | cooldown (batch-6 refresh); not prospective to 51-100 |
| p1_stroke_19_横斜钩 | SKIP | cooldown; not prospective |
| p1_stroke_21_横折弯 | SKIP | cooldown; not prospective |
| p1_stroke_25_横折弯钩 | SKIP | cooldown; not prospective |
| p1_stroke_26_横折折 | SKIP | cooldown + STALE (retry_n=2 hard-frozen) |
| p1_stroke_31_竖折折钩 | SKIP | cooldown; not prospective |
| p1_stroke_32_横折折折钩 | SKIP | cooldown; not prospective |

### Phase-2 bootstrap fails (positions 10, 11, 14, 15 — NOT on cooldown)

These four bootstrap fails have never been retried since the original
FAIL judgment. No cooldown applies. Evaluated by (a) prospective use and
(b) retrospective learning.

**p2_radical_010_勹 (bao) — SKIP**
- (a) Prospective: 匚 (019/pos-51), 冂 (024/pos-56), 匸 (034/pos-66) are
  in the upcoming window. They are related in the loose "enclosing frame"
  family, but they are ANGULAR frames — 勹's failure was specifically the
  rounded envelope requiring one continuous bezier, which the angular
  frames do NOT share. Weak (a).
- (b) Retrospective: no new bezier-envelope primitive has been added to
  the bank since the fail. Sandbox meta-lesson still stands but no
  validated technique.
- Decision: SKIP.

**p2_radical_011_匕 (bi) — SKIP**
- (a) Prospective: no 匕-shape component appears in 51-100. Nothing like
  a "撇 lands on a 竖弯钩 shaft" junction is upcoming.
- (b) Retrospective: no new junction primitive in bank.
- Decision: SKIP.

**p2_radical_014_厂 (chang) — RETRY**
- (a) Prospective: **广 (052 / pos-84)** is literally 丶 stacked on top
  of 厂. Solving 厂 cleanly is a direct prerequisite. 065 尸 (pos-97)
  also has a 厂-like top-left corner (heng + descending stroke).
  Two upcoming items depend on 厂. Strong (a).
- (b) Retrospective: sandbox already has a specific fix recipe (reuse
  `heng.py` at scale ~0.65, draw 撇 as almost-vertical with shallow
  scoop only near the tail — control point on the chord midpoint, NOT
  offset left; head anchored at heng's left end as a weld). P10
  (pie vs 丿 curvature discipline) directly informs this. Strong (b).
- retry_n: 0 → 1.
- Decision: **RETRY**.

**p2_radical_015_刀 (dao) — RETRY**
- (a) Prospective: **力 (025 / pos-57)** shares the same skeletal
  structure as 刀 — 横折钩 (top+right frame) + a 撇 that CROSSES the
  horizontal. Structurally identical junction to 刀. Solving 刀 now
  is a direct prerequisite for 力. Strong (a).
- (b) Retrospective: sandbox has clear fix recipe (increase heng_zhe_gou
  scale to ~0.8 so the top spans more of the canvas; place pie head at
  math y ≈ +75 ABOVE the horizontal so pie head is above and the tail
  descends below — the two strokes must CROSS, not weld). This
  directly maps to a validated primitive (heng_zhe_gou.py) plus an
  inline pie with a specific placement. Strong (b).
- retry_n: 0 → 1.
- Decision: **RETRY**.

## Summary

- 11 errata items considered.
- 7 SKIP (Phase-1 hook fails on cooldown from batch-6 refresh).
- 2 SKIP (p2 勹, p2 匕: no strong (a) or (b) match).
- 2 RETRY (p2 厂, p2 刀: both have direct prospective use in 51-100 AND
  specific retrospective recipes in sandbox / principle_bank).

Retry rate = 2/11 — deliberate, not conservative. All non-cooldown items
were considered on the merits; 2 have real (a)+(b) rationale, 2 do not.
