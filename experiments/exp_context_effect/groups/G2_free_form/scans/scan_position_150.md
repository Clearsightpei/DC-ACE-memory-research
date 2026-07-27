# G2 Errata Scan — Position 150

Scan performed at curriculum position 150 (end of B2, boundary into
B3). This is the **FIRST scan under v7 self-evolution** — memory was
just restructured at pos 168: created `form_catalog.md` (stroke forms
indexed by class × context) and `radical_position_rules.md` (whole-
radical silhouette + aspect-ratio + center-of-mass check).

Retry decisions follow shared_rules v6/v7:
(a) prospective / (b) retrospective, with 50-item cooldown after any
prior retry.

## Upcoming curriculum window (positions 151-200)

**Phase-2 tail (151-167)**: 水 瓦 尣 王 韦 文 毋 心 牙 爻 曰 月 爫 支 止 爪 无

**Phase-3 head (168-200, 1–4 画)**: 一 丨 乙 丶 丿 乚 乛 亅 了 丩 人
丷 十 乂 二 乃 又 乜 儿 亠 几 亻 九 八 力 冂 七 冖 入 冫 厂 凵 刀

## Cooldown check (retries logged at pos 150 → eligible pos 200)

The following items were retried during B2 (attempts logged at
scan_position=150 with PASS/FAIL outcomes) and are ON COOLDOWN until
pos 200 — cannot be retried in this scan even if (a)/(b) applies:

- p2_radical_011_匕 (retry_n=3, FAIL) — cooldown blocks despite 比 at pos 186 in P3
- p2_radical_015_刀 (retry_n=3, FAIL) — cooldown blocks despite 刀 at pos ~200 in P3
- p2_radical_030_入 (retry_n=1, FAIL) — cooldown blocks despite 入 at pos ~196 in P3
- p2_radical_047_飞 (retry_n=1, FAIL)
- p2_radical_048_干 (retry_n=2, FAIL)
- p2_radical_053_己 (retry_n=1, FAIL)
- p2_radical_058_马 (retry_n=1, FAIL)
- p2_radical_067_士 (retry_n=1, FAIL)

Also on cooldown: p1_stroke_24, p1_stroke_32 (batch-6 refresh @ pos 33
still within-window? — pos 33 + 50 = 83, expired; but subsequent
scan_100 SKIP is not a retry, so cooldown from pos 33 has long expired).

## Special (b) retrospective trigger — v7 restructure

The new `form_catalog.md` + `radical_position_rules.md` directly
address the "context-blindness" failure family: silhouette wrong,
wrong 撇 variant, wrong 点 orientation, sibling-pair confusion.
Every B2-new item (initial_batch: B2, retry_n=0) is a candidate to
re-attempt with the fresh memory scaffolding, weighted by whether
the failure diagnosis maps to an existing catalog entry.

## Special (a) prospective trigger — Phase-3 char overlap

Phase-3 chars in 168-200 that overlap with fail-list radicals: 人 力
八 冂 冖 厂 亻 (all GRADUATED already), and 入 刀 (COOLDOWN-BLOCKED).
Net effect: no (a) leverage from P3 head onto still-open items.
BUT plenty of (a) leverage from Phase-2 tail 151-167.

## Decisions

### Never-retried B1 items (retry_n=0)

**p2_radical_020_阝** — SKIP. Same belly-on-right unproven block as
before; no 阝-family in 151-200.

**p2_radical_032_厶** — SKIP. No 厶-embedding in 151-200. Marginal
retrospective coverage from new form_catalog.

**p2_radical_042_巛** — SKIP. No wave/triplet radical upcoming. 水
at pos 151 differs enough (three teardrops in 氵 style, not ㄑ).

**p2_radical_050_弓** — SKIP. 韦 at pos 155 is a folded-body compound
but not a 弓-topology sibling. No new "3-fold connected" primitive
proven.

**p2_radical_055_彑** — SKIP. No 彑-embedding upcoming. No new
chevron+彐 memory addition.

**p2_radical_056_巾** — SKIP. 巾 does not embed into any upcoming
item.

**p2_radical_059_门** — SKIP. No 门-family in 151-200.

**p1_stroke_24_横撇弯钩** — SKIP. Belly-on-right arc still unproven.
No 阝 or similar in 151-200.

**p1_stroke_32_横折折折钩** — SKIP. No 4-fold-plus-hook stroke embedded
in any upcoming item. retry_n=2 already.

### B2-new items (initial_batch: B2, retry_n=0, all fresh)

**p2_radical_075_夕** — RETRY. (b) STRONG: form_catalog "撇 as
body-crossing diagonal" + radical_position_rules "square" aspect
family directly diagnose the "thin/vertical-elongated" failure. (a)
moderate: 月 at pos 162 has a similar tall-narrow compound-lid
structure; 夕 form transfers.

**p2_radical_077_忄** — RETRY. (b) STRONG: form_catalog "点 as 忄
heart-radical side dot" was created specifically for this failure
(codifies left-dot 35 px teardrop + right-dot short 横 flick).
(a) STRONG: **心 at pos 158** is the sibling — same three-splay
dot topology, so fixing 忄 now primes 心 immediately after.

**p2_radical_078_幺** — SKIP. No form_catalog entry for 幺-loops
yet; drawer_memory "撇折 family" was already available at first
attempt. No strong (a): 爻 at 161 is 乂+乂 not 幺+幺.

**p2_radical_080_尢** — RETRY. (a) VERY STRONG: **尣 at pos 153**
is a direct sibling of 尢 (same 一 + 撇 + 竖弯钩-leg structure);
also 无 at pos 167 shares the bent-leg pattern. (b) form_catalog
"捺 as right-leg" + drawer_memory "tangent-continuous 竖弯钩"
proven primitive.

**p2_radical_081_夂** — RETRY. (a) STRONG: 支 at pos 164 shares
the 又-like bottom half (横撇 + 捺 splay). (b) form_catalog "撇 as
top-of-radical single flick" + "捺 as right-leg of two-stroke
apex" pair directly address the failure.

**p2_radical_083_丬** — RETRY. (b) STRONG: form_catalog "点" entries
+ "竖 as through-going axis" cover both defects (dots too far left,
not touching the 竖). (a) moderate: 爿 at pos 107 (already in
errata, we're skipping) is the mirror, but fixing 丬 gives us the
form for future 爿 attempts too.

**p2_radical_084_夊** — SKIP. Redundant with 夂 retry (same
top-撇 + 捺-splay topology, dispatched together). If 夂 PASSes we
gain the form for 夊 next scan.

**p2_radical_085_贝** — SKIP. (b) form_catalog sibling-pair table
covers 贝-vs-见 but (a) is absent — no 贝-family in 151-200. 见 also
still failed. Save the slot until either sibling is proven.

**p2_radical_086_比** — SKIP. 比 = 匕+匕, and **匕 is on cooldown**.
Retrying 比 while its atomic component still fails is high-risk.
Defer to next scan (pos 200) when 匕 becomes eligible again.

**p2_radical_088_长** — SKIP. (b) moderate — form_catalog "square"
+ 捺-splay applies, but the specific 竖提 mid-body stroke has no
dedicated form_catalog entry yet. (a) absent — no 长-family upcoming.

**p2_radical_089_车** — RETRY. (b) STRONG: form_catalog "竖 as
through-going axis" + "横" length-differentiator + "横折 as top-right
corner of a box" all apply. Failure was a symmetric 王-like stack,
which the three-catalog-entries stack should correct. (a) moderate:
王 at pos 154 shares the multi-横 + through-竖 structure — fixing 车
transfers directly.

**p2_radical_092_厄** — SKIP. (b) radical_position_rules "off-center
L" family helps but the specific inside 卩 stroke set has no
form_catalog entry. (a) — 厂 P3 pos 194 already GRADUATED so no
prospective anchor.

**p2_radical_093_方** — RETRY. (b) STRONG: form_catalog "撇 as
top-lid" for the top 丶/亠 + drawer_memory 横折钩 primitive.
(a) STRONG: **文 at pos 156** shares the 亠-top (dot + 横) then
crossing body — fixing 方 now primes 文 immediately.

**p2_radical_094_风** — RETRY. (b) VERY STRONG: drawer_memory
"横折弯钩" is the proven KEY PRIMITIVE; the failure was a boxy
right-angle instead of the shouldered swept 横折弯钩. Direct fix.
(a) absent but the (b) leverage is exceptional — 横折弯钩 is one of
the highest-value primitives in memory.

**p2_radical_095_父** — RETRY. (b) form_catalog top-splay + 撇/捺
crossing. (a) STRONG: **爻 at pos 161** = two 乂 stacked, and 乂 is
the body of 父; also 爪 at pos 165 has top-splay pattern. Two
prospective hits.

**p2_radical_096_戈** — SKIP. (b) drawer_memory "斜钩" entry
addresses the fix, but (a) is absent — no 戈-family in 151-200.
Save for next scan when 戏/戒/我 family shows up.

**p2_radical_097_户** — SKIP. (b) form_catalog sibling-pair 户-vs-尸
+ "撇 as top-lid" apply, but (a) absent — no 户/尸-family in
151-200.

**p2_radical_098_火** — RETRY. (b) STRONG: form_catalog "点" family
+ "捺 as right-leg of two-stroke apex" + drawer_memory "left/right
dot flanking 人-body" all apply to the "dots placed as mid-body dots"
failure. (a) weak but 火 is a high-frequency radical that will recur;
proving it now is high-value.

**p2_radical_099_旡** — RETRY. (a) VERY STRONG: **无 at pos 167**
is a direct sibling of 旡 (essentially the same shape). Fixing 旡
directly primes 无. (b) form_catalog "横 as through-going" + "竖弯钩"
family cover the fix.

**p2_radical_100_见** — SKIP. (b) sibling-pair table addresses it
but (a) is absent — no 见 or 贝 in 151-200. Save until either
sibling is upcoming.

**p2_radical_101_斤** — SKIP. (b) moderate — form_catalog "撇 as
top-of-radical single flick" applies to the two stacked 撇. (a)
absent in 151-200.

**p2_radical_102_耂** — SKIP. (a) absent. (b) marginal — form_catalog
"撇 as body-crossing diagonal" would help but the specific old-土-top
composition is idiosyncratic.

**p2_radical_105_肀** — SKIP. Rare/idiosyncratic; no upcoming match,
no dedicated new memory.

**p2_radical_106_牛** — RETRY. (b) STRONG: form_catalog "横 as
top-vs-bottom length-differentiator" + "竖 as through-going axis"
+ "撇 as top-lid" all directly apply to the observed defect (wrong
length ratios, missing top 撇). (a) STRONG: **王 at pos 154** has
the same 3-横 stacked + through-竖 structure; fixing 牛 primes 王
by transferring the through-axis 竖 form + horizontal length
management.

**p2_radical_107_爿** — SKIP. Redundant with 丬 retry (mirror form).
If 丬 PASSes we learn the axis-竖 discipline that applies to 爿 as
well; deferred to next scan.

**p2_radical_108_片** — SKIP. Idiosyncratic bracket compound with no
strong upcoming (a). Save the slot.

**p2_radical_109_攴** — RETRY. (a) VERY STRONG: **支 at pos 164**
is a direct sibling of 攴 (essentially the same shape — 攴 is the
older form). Fixing 攴 primes 支 immediately. (b) form_catalog
"捺 as right-leg" for the bottom 又.

**p2_radical_110_攵** — SKIP. Redundant with 攴 retry (attributive
cursive form). Wait for 攴 outcome to know if the shared form
recipe works.

**p2_radical_115_氏** — SKIP. (b) STRONG (drawer_memory "斜钩"
proven) but (a) absent — no 氏-family in 151-200. Save for next
scan.

**p2_radical_116_礻** — SKIP. (b) form_catalog "点 as 宀 roof-cap
dot" applies to the top 丶 but (a) absent — no 礻/衤 upcoming.

## Summary

- **13 RETRY**: 夕 (075), 忄 (077), 尢 (080), 夂 (081), 丬 (083),
  车 (089), 方 (093), 风 (094), 父 (095), 火 (098), 旡 (099),
  牛 (106), 攴 (109).
- **26 SKIP**: stroke_24, stroke_32, 阝, 厶, 巛, 弓, 彑, 巾, 门,
  幺, 夊, 贝, 比, 长, 厄, 戈, 户, 见, 斤, 耂, 肀, 爿, 片, 攵, 氏, 礻.
- **8 COOLDOWN-BLOCKED** (retried at pos 150, next eligible pos 200):
  匕, 刀, 入, 飞, 干, 己, 马, 士.
- Retry rate this scan: 13/(13+26) = **33%** of eligible items.
  Balanced (not minimalist): every RETRY carries either a strong (a)
  prospective anchor to a specific pos-151-200 item OR a strong (b)
  retrospective anchor to a new v7 memory entry (form_catalog /
  radical_position_rules) that directly addresses the failure
  diagnosis.
- Retry-pool composition:
  - **8 retries driven primarily by (a) with pos-151-167 anchor**:
    忄→心, 尢→尣/无, 夂→支, 方→文, 父→爻/爪, 旡→无, 牛→王, 攴→支.
  - **3 retries driven primarily by (b) v7-catalog anchor**:
    风 (横折弯钩 KEY PRIMITIVE), 火 (点 + 捺 catalog), 车 (multi-
    catalog stack).
  - **2 retries with combined moderate (a) + strong (b)**:
    夕, 丬.
- The v7 restructure primarily enables (b) retries; the fact that
  most B2-new items map to a specific catalog entry validates the
  restructure's diagnostic value. Next scan (pos 200) will measure
  retry pass rate to check whether the catalog-driven fixes actually
  land.

---

*Scan performed by G2 curator at position 150. First scan under
v7 self-evolution (memory restructure at pos 168 that created
`form_catalog.md` and `radical_position_rules.md`).*
