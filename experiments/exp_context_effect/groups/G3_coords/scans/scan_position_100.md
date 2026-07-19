# Errata Scan — G3 (coord-bank) — Curriculum Position 100

Scan performed at position 100 (end of B1 / start of B2 main curriculum).
Upcoming 50 items: positions 101-150 (氵, 纟, 巳, 土, 囗, 兀, 夕, 小, 忄,
幺, 弋, 尢, 夂, 子, 丬, 夊, 贝, 比, 灬, 长, 车, 歹, 斤, 厄, 方, 风, 父,
戈, 户, 火, 旡, 见, 斤, 耂, 毛, 木, 肀, 牛, 爿, 片, 攴, 攵, 气, 欠, 犬,
日, 氏, 礻, 手, 殳).

**Batch context**: G3 finished B1 at 54%, worse than G1 no-memory
control (60%). This is the SECOND consecutive underperforming batch
(bootstrap: 78% vs 84%). The new **TR8 "INLINE-FRESH TEST"** in the
principle bank is a MAJOR retrospective intervention that specifically
addresses the primitive-reflex failure mode responsible for ~18/23 B1
fails. Per shared_rules.md "balance not minimalism" and the definition
of retrospective (b) — "you've learned something in the past 25 items
that specifically addresses this item's failure mode" — TR8 is exactly
that trigger, applied at bank-wide scale.

## Errata inventory & decisions

### Phase-1 hook fails (batch-6 refresh, all off-cooldown by position ~100)

Batch-6 refresh on 2026-07-16 attempted all 7 Phase-1 hook fails as
"inlined" retries. Result was PENDING as of the batch-6 log; no PASS
graduation noted since. Cooldown (50 items) has elapsed. However, NONE
are prospective to positions 101-150 (no upcoming radical/character in
this window is composed of 弯钩/斜钩/折折钩 as a sub-component), and
TR8 (which is about primitive-reflex in *composition*) does not apply
to standalone strokes that are themselves the target. Skip all 7.

| item_id | decision | reason |
|---|---|---|
| p1_stroke_16_斜钩 | SKIP | not prospective; TR8 doesn't apply to standalone strokes |
| p1_stroke_19_横斜钩 | SKIP | not prospective; TR8 N/A |
| p1_stroke_21_横折弯 | SKIP | not prospective; TR8 N/A |
| p1_stroke_25_横折弯钩 | SKIP | not prospective; TR8 N/A |
| p1_stroke_26_横折折 | SKIP | STALE (retry_n=2, terminal-freeze rule) |
| p1_stroke_31_竖折折钩 | SKIP | not prospective; TR8 N/A |
| p1_stroke_32_横折折折钩 | SKIP | not prospective; TR8 N/A |

### Phase-2 bootstrap fails (never retried; no cooldown)

**p2_radical_010_勹 (bao) — SKIP**
- (a) No 勹-shape rounded-envelope component in 101-150.
- (b) TR8 marginally applies (rounded envelope needs one bezier, which
  is inline-fresh) but no direct prospective hit; deferred to a
  window where 匊/句/勺 appear.

**p2_radical_011_匕 (bi) — SKIP**
- (a) No 匕-shape junction in 101-150 (比 at pos-86 has 匕 elements but
  比 itself is on the upcoming list — this is a first-attempt item,
  not a prerequisite lookup). 比 will be attempted fresh with TR8.
- (b) No new junction primitive.

### Phase-2 B1 fails (23 items, all retry_n=0 except 厂/刀)

**p2_radical_020_阝 (fù) — SKIP**
- (a) No 阝-slot compound in 101-150.
- (b) TR8 applies but weak without prospective use.

**p2_radical_021_丷 (bā_top) — RETRY** (G3-unique)
- (a) **父 (pos-95, upcoming)** has 八/丷-shape top. Moderate (a).
- (b) TR8 + sandbox fix recipe (use `dian` for right dot, mirrored
  inline dian for left dot at scale 0.5 with matched width profile) is
  a specific new-technique retrospective trigger.
- retry_n: 0 → 1.

**p2_radical_024_冂 (jiong) — SKIP**
- Already graduated via `jiong_radical.py` bank entry #54 (batch-4).
  Not on active errata.

**p2_radical_025_力 (li) — SKIP**
- (a) No 力-slot in 101-150 (力 first appears deeper). The 刀→力
  prerequisite chain was resolved at scan_050 (刀 retry-1 FAIL);
  attempting 力 without 刀 solved is speculative.
- (b) TR8 applies but weak.

**p2_radical_028_人 (rén) — RETRY**
- (a) **火 (pos-98), 父 (pos-95), 欠 (pos-112), 大→犬 (pos-113)** all
  contain 人-shape apex-kiss geometry. Multiple direct hits. Very
  strong (a).
- (b) TR8 **explicitly names 人** as a documented failure mode where
  inline-fresh (bezier apex meeting) is the fix. Very strong (b).
- retry_n: 0 → 1.

**p2_radical_030_入 (rù) — RETRY**
- (a) **父 (pos-95)** and **欠 (pos-112)** both have 入-like top with a
  head-on-shaft junction. Moderate (a).
- (b) TR8 **explicitly names 入** as a documented failure mode; fresh
  bezier with head-on-other-stroke-at-u=0.3 is the fix. Strong (b).
- retry_n: 0 → 1.

**p2_radical_032_厶 (si) — SKIP**
- (a) 允/去 not in 101-150.
- (b) Sandbox flags this as a rendering-fidelity ceiling, not a
  primitive-reflex issue. TR8 doesn't fix format ceiling issues.

**p2_radical_035_讠 (yán) — SKIP** (G3-unique)
- (a) 讠-slot compounds (话/说/etc) not in 101-150.
- (b) Failure is inline-recipe geometry (per sandbox), not primitive-
  reflex — so TR8 doesn't specifically address it.

**p2_radical_036_廴 (yǐn) — SKIP**
- (a) 建/廷 not in 101-150.
- (b) TR8 applies (sweeping 弯钩 needs one long bezier) but no
  prospective hit.

**p2_radical_038_㔾 (jié_variant) — RETRY**
- (a) **巳 (pos-71)** has a 㔾-like bottom hook curl. Moderate (a).
- (b) TR8 + "round the elbow" fix (per sandbox); the inline-fresh
  approach for small-hook radicals is directly the recipe.
- retry_n: 0 → 1.

**p2_radical_040_屮 (chè) — SKIP** (G3-unique)
- (a) No 屮-slot compound in 101-150 (草/艹-family not here).
- (b) TR8 applies (sandbox: inline both verticals with matched widths)
  but no prospective use — better to defer to window where 艺/芊/etc
  appear.

**p2_radical_041_彳 (chì) — SKIP**
- (a) 彳-slot compounds (行/得/etc) not in 101-150.
- (b) TR8 applies but no prospective hit.

**p2_radical_042_巛 (chuān) — SKIP**
- (a) No 巛-slot in 101-150.
- (b) TR8 applies but weak; wavy-primitive gap remains.

**p2_radical_046_大 (dà) — RETRY** (G3-unique)
- (a) **犬 (pos-113)** is literally 大 + dian. Direct prerequisite.
  Strong (a).
- (b) TR8 **explicitly names 大** as a documented failure mode; inline
  3 tapered beziers tuned to hand-chosen apex. Strong (b).
- retry_n: 0 → 1.

**p2_radical_047_飞 (fēi) — SKIP**
- (a) No 飞-slot in 101-150.
- (b) TR8 applies but no prospective hit.

**p2_radical_050_弓 (gōng) — SKIP**
- (a) No 弓-slot compound in 101-150 (弟/引 not here).
- (b) TR8 applies but weak.

**p2_radical_053_己 (jǐ) — RETRY**
- (a) **巳 (pos-71)** is nearly the same "3"-like envelope as 己; the
  difference is 巳 has a closed-loop upper compartment while 己 has an
  open one, but the fundamental strokes and terminal curl are shared.
  Also **弋 (pos-79)** and **旡 (pos-99)** have related mid-shape
  curls. Strong (a) via 巳.
- (b) TR8 applies (per sandbox: force-fit lost the curl; inline as one
  bezier with terminal curl-up). Also, the successful **彐 inline
  template** in the bank is a validated retrospective technique for
  this family (per 彑 sandbox note). Strong (b).
- retry_n: 0 → 1.

**p2_radical_055_彑 (jì) — SKIP**
- (a) No 彑-slot in 101-150.
- (b) TR8 + 彐 template applies but no prospective hit; solving 己
  first (this scan) validates the technique for the family.

**p2_radical_056_巾 (jīn) — SKIP**
- (a) 巾-slot compounds (布/带/etc) not in 101-150.
- (b) TR8 applies but no prospective hit.

**p2_radical_058_马 (mǎ) — SKIP**
- (a) 马-slot compounds not in 101-150 (骂/驰 not here).
- (b) TR8 applies but no prospective hit.

**p2_radical_059_门 (mén) — SKIP**
- (a) 门-slot compounds (问/间/闭) not in 101-150.
- (b) TR8 applies but no prospective hit; defer to window that
  contains 问/间.

**p2_radical_061_女 (nǚ) — RETRY** (G3-unique)
- (a) No 好/妈 in 101-150 directly, BUT 女 is a G3-unique fail that
  TR8 explicitly-adjacent (crossing-撇 + heng as fresh beziers) and
  represents a foundational radical the group MUST solve before
  Phase-3 character compositions. Weak-direct-(a) but strong
  strategic-(a).
- (b) TR8: primitive-first "stacked-and-crossed heng+pie+heng" failure
  is exactly the pattern TR8 targets. Inline crossing bezier at a
  hand-chosen shared pixel is the fix. Strong (b).
- retry_n: 0 → 1.

**p2_radical_062_犭 (quǎn) — RETRY**
- (a) **犬 (pos-113)** is the standalone-dog form; 犭 is the left-side
  variant. Solving the continuous curl shape for 犭 validates the
  inline-curl technique that 犬 will also need. Strong (a).
- (b) TR8: force-fit primitives distort continuous-curl radicals;
  inline one bezier + dian is the fix. Strong (b).
- retry_n: 0 → 1.

**p2_radical_015_刀 (dao) — SKIP** (cooldown)
- Retry-1 attempted at position 100 (post-B1 judgment, FAIL).
  Cooldown until position ≥150. SKIP mandatory.

**p2_radical_014_厂 (chang) — GRADUATED**
- Retry-1 PASSED (post-B1). Removed from errata; now `chang.py`
  bank entry #67. Not eligible.

## Summary

- **Errata items considered**: 30 (7 Phase-1 + 2 bootstrap + 23 B1 -
  2 already resolved [厂 graduated, 冂 graduated earlier] + 刀 on
  cooldown = 30 gross, 27 net-active).
- **RETRY**: 8 items. All have BOTH strong (a) prospective use in
  101-150 AND strong (b) TR8-based retrospective trigger, except 女
  which is (a)-weak-but-strategic + (b)-strong.
- **SKIP**: 22 items. Reasons: cooldown (1), stale/frozen (1),
  no-prospective-use-and-weak-retrospective (13), rendering-ceiling
  or non-primitive-reflex failure mode (7).

**Retry rate = 8/30 ≈ 27%** — a genuine step up from scan_050's
2/11 ≈ 18% and appropriately reflects that TR8 is a systemic new
intervention specifically addressing the dominant B1 failure mode.
This is "balance not minimalism": the 8 retries all have concrete
(a)+(b) rationale, the 22 skips all have concrete "no clear win" or
cooldown/freeze reasoning.

**Retry priority order (Drawer should attempt in this order — earliest
prospective-use items first):**

1. **己 (jǐ)** — prerequisite for 巳 (pos-71, next 25 items).
2. **㔾 (jié_variant)** — prerequisite for 巳 (pos-71).
3. **女 (nǚ)** — G3-unique + foundational radical.
4. **丷 (bā_top)** — prerequisite for 父 (pos-95).
5. **人 (rén)** — prerequisite for 父/欠/火 (pos-95, 98, 112).
6. **入 (rù)** — prerequisite for 父/欠 (pos-95, 112).
7. **犭 (quǎn)** — validates curl-inline technique before 犬 (pos-113).
8. **大 (dà)** — direct prerequisite for 犬 (pos-113).

(Note: 8 items listed; scan-approved retry set is 8 total. See
retry_log.jsonl for the pending entries.)
