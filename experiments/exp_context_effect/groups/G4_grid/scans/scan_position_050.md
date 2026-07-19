# Errata Scan — position 50 (G4 grid-bank)

Scan performed at curriculum position 50 (end of bootstrap batch, before
positions 51-100 batch begins). Cooldown rule: an item retried at
curriculum position P is on cooldown until P+50.

Reviewed each active errata entry against:
- (a) Prospective — upcoming items 51-100 whose success would depend on
  or benefit from mastering this item.
- (b) Retrospective — new memory (principle bank / bank primitives)
  since last attempt that specifically addresses the prior failure
  mode.

Key new principle since last attempt on the bootstrap items:
**TR11. SELF_CHECK.visual_ok is a real check, not a checkbox** —
Before setting `visual_ok = True`, the drawer must name TWO SPECIFIC
visual features that agree between rendered PNG and GT. All 6/6 G4
bootstrap FAILs had rubber-stamped `visual_ok=True`. This principle
directly unlocks retries whose failure mode was diagnostic complacency
(not genuinely missing primitives).

Also load-bearing (already in bank at last attempt but re-emphasized):
- TR9. MMH anchors are a floor, not a ceiling for standalone radicals.
- TR10. N-class joints must LOOK connected — enforce pixel proximity.
- TR4. Joint enforcement via shared anchor tuples.
- TR6. Inline the recipe when a primitive's assumptions don't fit.

---

## Item-by-item decisions

### p1_stroke_19_横斜钩 — SKIP (cooldown)
- **Last attempt**: batch 6 refresh (retry_n=2, curriculum position ~32).
- **Cooldown**: expires ~position 82. Still on cooldown at 50.
- **Prospective**: no upcoming item uses 横斜钩 as an isolated component
  in positions 51-100. Weak.
- **Retrospective**: TR11 does apply, but the failure mode was
  compositional (fusing phases), not diagnostic. No new primitive
  bridges the compound-stroke gap.
- Verdict: **SKIP — cooldown + weak prospective.**

### p1_stroke_25_横折弯钩 — SKIP (cooldown)
- **Last attempt**: batch 6 refresh (retry_n=2, curriculum position ~32).
- **Cooldown**: expires ~position 82. Still on cooldown at 50.
- **Prospective**: 几 (022) is the strongest prospective match — but its
  own item is upcoming and better tackled fresh; 马 (058) contains
  弯钩 profile. Moderate.
- **Retrospective**: TR11 applies. No new bank primitive addresses the
  vertical-descent-vs-yi-diagonal shape gap.
- Verdict: **SKIP — cooldown blocks; will re-evaluate at scan 75.**

### p1_stroke_29_横折折撇 — SKIP (cooldown)
- **Last attempt**: batch 6 refresh (retry_n=2, curriculum position ~32).
- **Cooldown**: expires ~position 82. Still on cooldown at 50.
- **Prospective**: 廴 (036), 辶 (044) both contain 横折折撇-family motion.
  Would be nice to have, but 廴/辶 are themselves upcoming items and
  can be drawn fresh from the target.
- Verdict: **SKIP — cooldown + component target coming up anyway.**

### p2_radical_003_丿 — RETRY
- **Last attempt**: bootstrap position ~35 (retry_n=0 recorded as
  bootstrap FAIL, NOT a retry). Prior to bootstrap, batch-2 also FAILed
  it. Treating bootstrap FAIL as attempt zero of Phase-2; retry_n=1 now.
- **Cooldown**: no formal cooldown (bootstrap FAIL was original P2
  attempt, not a retry). Even under strict counting the last retry-2
  was pre-position-33, cooldown expires at ~83 — but the errata explicit
  fix (widen to anti-diagonal + TR9) has NEVER been applied. Retrying
  now is legitimate application of new memory.
- **Prospective — STRONG**: 撇 appears in 亻 (029), 人 (028), 入 (030),
  彳 (041), 犭 (062), 女 (061), 大 (046), 广 (052), 尸 (065), 饣 (066),
  扌 (068). Nearly a third of the upcoming batch uses 撇.
- **Retrospective — STRONG**: TR9 explicitly names 丿 as its MMH-floor
  example. TR11 catches the rubber-stamp failure mode. Errata fix
  (head TR(0.85,0.15) → tail BL(0.15,0.85), head_width=16, curve=0.15)
  is concrete and follows the same pattern that worked for 丨/亅/乛/一/丶.
- Verdict: **RETRY.**

### p2_radical_007_乚 — RETRY
- **Last attempt**: bootstrap position ~39 (retry_n=0 in Phase-2 counting).
- **Cooldown**: no formal cooldown blocks this scan.
- **Prospective — MODERATE**: 己 (053) has a 乚-family finish, 马 (058)
  contains 竖弯钩 profile. 匕 already promoted uses 竖弯钩 successfully,
  which is close cousin. Good prospective use.
- **Retrospective — STRONG**: TR9 (extend to BR corner), TR11 (name
  visual agreements), plus errata's explicit anchor recipe
  (head TC(0.50,0.10) → belly C(0.50,0.75) → corner BC(0.55,0.80) →
  tail BR(0.95,0.50)) never applied. Sandbox pattern-1 addresses this.
- Verdict: **RETRY.**

### p2_radical_014_厂 — RETRY
- **Last attempt**: bootstrap position ~46 (retry_n=0 in Phase-2 counting).
- **Cooldown**: no formal cooldown blocks this scan (retry_n=0).
- **Prospective — VERY STRONG**: 广 (052) is literally 厂 + 丶.
  尸 (065) shares the 厂-frame top. If 厂 masters, 广 and 尸 first
  attempts become dramatically more likely to PASS.
- **Retrospective — VERY STRONG**: TR4 (shared anchor tuple weld) +
  TR10 (N-class must LOOK connected) are exactly the failure-mode fixes.
  TR11 catches the diagnostic complacency. Errata prescribes concrete
  weld anchor ('TC', 0.15, 0.5).
- Verdict: **RETRY.**

### p2_radical_015_刀 — RETRY
- **Last attempt**: bootstrap position ~47 (retry_n=0 in Phase-2 counting).
- **Cooldown**: no formal cooldown blocks this scan.
- **Prospective — VERY STRONG**: 力 (025) is literally the same
  compound structure as 刀 with a different second stroke. 又 (037)
  also compositionally close. 刀 mastery is a direct prerequisite for
  力 next batch.
- **Retrospective — VERY STRONG**: TR4 (T-weld), TR10 (visual connect),
  TR11 (named agreements). Errata prescribes explicit hook direction
  assertion (tip.y < tail.y AND tip.x < tail.x) and shared anchor for
  the 撇+横折钩 junction.
- Verdict: **RETRY.**

### p2_radical_016_刂 — RETRY
- **Last attempt**: bootstrap position ~48 (retry_n=0 in Phase-2 counting).
- **Cooldown**: no formal cooldown blocks this scan.
- **Prospective — MODERATE**: 川 (043) has a 3-vertical structure with
  hooked terminals; 卩 (023) contains a 竖 partner similar to 刂's
  短竖. Useful but not decisive.
- **Retrospective — STRONG**: TR8 sanity check (belly.x==head.x for
  shu_gou) — the failure was the drawer noting the constraint violation
  then rendering anyway. TR6 says INLINE if primitive doesn't fit.
  TR11 catches the rubber-stamp. Errata prescribes hook_pt override
  to share head's x_frac.
- Verdict: **RETRY.**

### p2_radical_017_儿 — RETRY
- **Last attempt**: bootstrap position ~49 (retry_n=0 in Phase-2 counting).
- **Cooldown**: no formal cooldown blocks this scan.
- **Prospective — STRONG**: 几 (022) is a very close relative of 儿
  (both 2-stroke bottom-supporting radicals with similar 竖弯钩 or
  横折弯钩 finish). 凵 (027) shares the wan-family bottom curve.
- **Retrospective — STRONG**: TR11 catches the visual disagreement
  the drawer suppressed. Errata gives a canonical 5-anchor plan
  (head TC 0.55,0.2 → belly C 0.55,0.5 → corner BC 0.6,0.75 →
  hook_pt BR 0.2,0.7 → tip BR 0.25,0.4) that keeps the hook up-right.
  Sandbox pattern-5 also suggests inlining 竖弯钩 as 2 Bezier segments
  if the 5-anchor primitive keeps failing.
- Verdict: **RETRY.**

---

## Summary

- **RETRY (6)**: p2_radical_003_丿, 007_乚, 014_厂, 015_刀, 016_刂, 017_儿.
- **SKIP (3, cooldown)**: p1_stroke_19_横斜钩, p1_stroke_25_横折弯钩,
  p1_stroke_29_横折折撇.

Rationale for size: prior G4 scans were flagged as too conservative
(2/18 attempted). All 6 bootstrap Phase-2 FAILs have both (a)
prospective — 撇/横折钩/乚-family/hook-family motifs are dominant in
positions 51-100 — AND (b) retrospective — TR11 (SELF_CHECK
named-agreement rule) is a genuinely new principle that directly
addresses the shared root cause of the 6 FAILs (rubber-stamped
visual_ok). Skipping any of the 6 would be under-attempting.

The 3 Phase-1 SKIPs are honest cooldown blocks (retry_n=2, last
attempt within the last ~20 positions of curriculum). Re-evaluate at
scan position 75.
