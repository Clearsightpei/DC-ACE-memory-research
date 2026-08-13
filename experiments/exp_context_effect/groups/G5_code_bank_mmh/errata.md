# G5 错题集 (errata)

*FAILed / C-verdict items and their diagnostic notes. Append-only per batch.*

---

## Bootstrap (2026-08-08) — 3 C-verdicts

### p2_radical_002_亅 (亅) — C → **R1 PASS (B1)** ✓ RESOLVED

**GT observation**: A clean 竖钩 with a smooth entry tick that becomes the vertical shaft (no separate "hat"), a nearly-vertical body, and a soft leftward hook at the bottom. Body sits around x≈150.

**Attempt failure mode** (main): The rendered head tick is disconnected from the shaft in a way that reads as two strokes.

**R1 fix that worked**: Continuous curl entry + tapered hook tip. Retry PASSed at B1.

### p2_radical_003_丿 (丿) — C → **R1 FAIL (B1)**

**GT observation**: A rightward-bowing pie starting mid-upper-right (~x=145, y=90) and sweeping down-left to about (30, 285). Thick head, tapered fine tail. Curvature is pronounced.

**Main failure mode**: The drawer nudged the head all the way LEFT to (90, 82) instead of ~(145, 90).

**R1 failure mode**: Drawer moved head to (112, 80) per errata guidance — still too far left of GT visual centroid (~145). The MMH median at (63, 79) is systematically ~80 px left of the visible centroid, and drawer wasn't willing to override MMH by that much.

**Retry-2 hint (if attempted)**: Ignore MMH entirely; use pixel head near (140, 90), tail near (30, 285), bow_perp=0.20-0.24 for pronounced curvature. Note: single-stroke MMH-underconstrained items may be terminal-freeze candidates.

### p2_radical_017_儿 (儿) — C → **R1 C (B1)**

**Main failure mode**: 竖弯钩 bottom sweep too tight; 撇 didn't overlap with hook top.

**R1 attempt**: Used shu_wan_gou with bottom_extra=85, knee_ratio=0.88, and nudged 撇 head to x=118 for overlap. Still C-verdict. Diagnosis: the sweep may still be under-extended; the two-stroke balance/proportion is subtle.

**Retry-2 hint**: Try bottom_extra=100, extend s2.tail further right (~x=290). Nudge pie head slightly further right and down (x=125, y=100). If still C, terminal-freeze — the difficulty is the visual balance, not any specific coord.

---

## B1 (2026-08-08) — 12 C's + 7 FAILs (main-channel only, retries above)

### C-verdict cluster (12 items)

**p2_radical_020_阝 (阜/right-ear) — C**
- Structure: 横撇弯钩 ("3-shape ear") + shu.
- BANK_DEVIATION for s1 (no primitive for the 3-shape compound).
- Failure: inline "ear" curve was noisy/off-shape; 3-shape needs precise 3-turn Bezier chain.
- Retry hint: reference 卩's (23) heng_zhe_gou inline for the top loop, then add a wan (curve) segment before the terminal hook.

**p2_radical_035_讠 (yán speech-radical) — C**
- Structure: 点 + 横折提 (heng-zhe-ti compound).
- BANK_DEVIATION for s2 (no rising-ti tail in bank at that time).
- Failure: horizontal + corner + rising tí produced but proportions off; tí too short relative to horizontal.
- Retry hint: now that `ti.py` exists in the bank, compose s2 as inline heng + shu_zhe (down) + ti (rising). Tí should sweep from lower-left corner up-right to end at ~(140, 165).

**p2_radical_036_廴 (yin — long-stride) — C**
- Structure: multi-turn zigzag + 平捺.
- BANK_DEVIATION for s1 (multi-turn top compound).
- Failure: zigzag path had too many/too-abrupt turns; ping_na used but head placement off.
- Retry hint: now `ping_na.py` and `heng_pie.py` exist. Try s1 as inlined 3-segment path with only 2 corners (not 3). Reference 辶 (which PASSed) for the ping_na integration.

**p2_radical_045_寸 (cun — inch) — C**
- Structure: 横 + 竖钩 + 丶.
- All 3 primitives from bank (heng, shu_gou, dian) — no deviation.
- Failure: likely the dot placement or the shu_gou hook angle; needs visual inspection.
- Retry hint: dian s3 should sit inside the lower-left interior at ~(125, 210) with a small down-right bow. Verify shu_gou hook curls left, not just tapers.

**p2_radical_050_弓 (gong — bow) — C**
- Structure: heng_zhe + heng + 横折弯钩 (complex bottom).
- BANK_DEVIATION for s3 (3-corner complex hook).
- Failure: bottom stroke's 3-corner turn was under-articulated; the terminal hook may have pointed wrong direction.
- Retry hint: decompose s3 as: horizontal at top (~y=170), corner-down, vertical descent (~y=270), corner-right, small horizontal (~x=175), terminal hook UP-LEFT ending near (135, 250). Very specific 5-waypoint path.

**p2_radical_053_己 (ji — self) — C**
- Structure: heng_zhe_short + heng + shu_wan_gou.
- All 3 from bank; no deviation.
- Failure: proportions/joint spacing off. 己's top loop and bottom sweep balance is subtle.
- Sibling note: 己 vs 已 vs 巳 — the top opening/closing distinguishes them. 己 has top LEFT open (heng_zhe short + short middle heng that doesn't touch the right vertical).
- Retry hint: nudge s1 tail down to y=150 (larger top loop), extend shu_wan_gou bottom further right.

**p2_radical_056_巾 (jin — towel) — C**
- Structure: shu + 横折(sharp variant) + shu.
- BANK_DEVIATION for s2 (sharp corner + longer vertical drop than heng_zhe_short).
- Failure: aspect wrong — 巾 is TALLER than wide (~1:1.5). Attempt may have been too square.
- Retry hint: now `heng_zhe_box.py` exists in the bank — use it with top_left=(90, 110), bottom_right=(210, 210), then the two verticals extend BELOW that box. Middle shu is the tallest stroke; short outer verticals sit inside the box's bottom.

**p2_radical_059_门 (men — door, simplified) — C**
- Structure: 点 + 竖 + 横折钩 (full-height).
- BANK_DEVIATION for s3 (rendered as one continuous heng+shu+hook path).
- Failure: full-height 横折钩 aspect / hook direction likely off.
- Retry hint: now `heng_zhe_gou.py` exists — call it directly with heng_head=(115, 90), corner=(215, 88), gou_tail=(200, 275), hook_tip=(180, 260).

**p2_radical_060_宀 (mian — roof) — C**
- Structure: 2 dians + heng_zhe_short.
- All 3 primitives from bank; no BANK_DEVIATION.
- Failure: proportions of the roof frame likely off — the heng_zhe_short's corner should sit at the top-right, but the two dians as top-and-left tick placement may be misaligned. Also the drawer marked visual_ok=None (not confirmed), so may not have inspected the output before submitting.
- Retry hint: reduce top dian's downward angle (make it more horizontal); place left dian at (60, 155)→(50, 210) (steeper). Heng_zhe_short spans from (85, 175) to (215, 210) with corner_offset=(10, 0).

**p2_radical_061_女 (nü — woman) — C**
- Structure: 撇点(pie-dian composite) + 撇 + 横.
- BANK_DEVIATION for s1 (fused compound).
- Failure: the fused compound stroke's corner geometry likely off; also the crossing of s2 (long pie) through s1 needs the right joint.
- Sibling note: 女 has THREE strokes; do not add a fourth by splitting s1.
- Retry hint: draw s1 as one continuous path: pie from (140, 100) down-left to (100, 175), then sharp corner into dian sweeping down-right to (170, 200). Long s2 pie crosses through s1's corner region.

**p2_radical_065_尸 (shi-body) — C**
- Structure: heng_zhe_short + heng + pie.
- All 3 from bank; no deviation.
- Failure: the 尸's enclosing frame proportions off — the top heng_zhe_short's corner and the middle heng's spacing don't produce the recognizable 尸 silhouette. Drawer marked visual_ok=None (didn't inspect).
- Retry hint: heng_zhe_short's corner should form a distinct top-right corner (s1_tail y=115, not 131). Middle heng shorter, tucked inside (from x=105 to x=180). Pie sweeps from just under s1's head (90, 100) down to (30, 285).

**p2_radical_066_饣 (shi — food-radical, simplified) — C**
- Structure: pie + short top-hook + 竖提.
- BANK_DEVIATION for s2, s3 (no primitives for angled top hook or 竖提).
- Failure: 竖提 (vertical + rising ti) not well-formed — needs a clear corner between vertical descent and rising tail.
- Retry hint: now `ti.py` exists — for s3, draw shu from head to corner, then draw_ti from corner to tail. The corner sits at the vertical's bottom.

### FAIL cluster (7 items)

**p2_radical_022_几 (ji — small-table) — FAIL**
- Structure: pie + 横折弯钩 (heng-zhe-wan-gou compound).
- BANK_DEVIATION for s2 (bank has shu_wan_gou but no leading heng tick).
- Failure: compound with top heng + shu + wan + gou is 4-segment; inline was likely simplified.
- Retry hint: 5-waypoint path — head(120, 105), corner1(170, 100), knee(215, 250), tail_before_hook(255, 240), hook_tip(240, 210). Use chain-of-ellipses ink.

**p2_radical_038_㔾 (variant of 卩) — FAIL**
- Structure: small internal dian + 横折弯 (seal-loop).
- BANK_DEVIATION for s2 (seal-loop is a wide horizontal-then-down-then-curve-up).
- Failure: shape ambiguous — reads more like nothing recognizable.
- Retry hint: this is a low-frequency radical; consider terminal-freeze after one more retry attempt. If retrying, focus on wide U-shape with clear rightward-curling terminal.

**p2_radical_042_巛 (chuan — flowing-water) — FAIL**
- Structure: 3 wavy strokes.
- No BANK_DEVIATION; used draw_pie with leftward bow.
- Failure: strokes may have been too straight, or bows in wrong direction (巛 has S-curves, not pure pie).
- Retry hint: each stroke should be an S-shape: head near top, curves right-down through middle, ends near bottom drifting back left. Use draw_pie with alternating bow_perp signs across the 3 strokes.

**p2_radical_047_飞 (fei — fly, simplified) — FAIL**
- Structure: 横斜钩 + short 横撇 + short 撇.
- BANK_DEVIATION for all three strokes (long arc-hook, plus small tapered segments).
- Failure: composition of the three parts didn't cohere as 飞's silhouette.
- Retry hint: 飞 is a 3-stroke calligraphy piece — dominant s1 is a long right-swooping arc ending in an upward hook (like a wave). The other two strokes are compact at top-right. Reference the GT PNG carefully.

**p2_radical_055_彑 (ji — pig-head bracket) — FAIL**
- Structure: 3 strokes with 横折 shapes forming a comb.
- No BANK_DEVIATION (rendered polylines); rendered directly.
- Failure: comb shape didn't match GT; may have wrong number of visible turns.
- Retry hint: 彑 is 3 strokes; each is a 横折 (horizontal + drop). Top and middle rows connect on the LEFT (like a "ヨ" mirrored). Very low frequency — consider terminal-freeze.

**p2_radical_058_马 (ma — horse, simplified) — FAIL**
- Structure: heng_zhe + 竖折折钩 (3-turn compound) + heng.
- BANK_DEVIATION for s1 and s2.
- Failure: 3-turn zigzag body of s2 is hard; likely wrong turn positions.
- Retry hint: 马's s2 is the signature stroke — vertical descent from top (~x=90, y=90), corner-right to (~x=210, y=155), corner-down to (~y=240), corner-right to (~x=245, y=245), terminal hook UP-LEFT. Bottom heng crosses this loop.

**p2_radical_062_犭 (quan — dog-radical, left position) — FAIL**
- Structure: 2 pies + 1 body-shu.
- BANK_DEVIATION for the body (slight-bow near-vertical).
- Failure: the 3-stroke arrangement (2 pies stacked on left of a long body) has specific proportions.
- Retry hint: top pie sweeps from ~(180, 100) to ~(115, 160); body from ~(140, 90) to ~(115, 265); bottom pie from ~(145, 170) to ~(80, 275). Body is nearly vertical with a mild rightward bow. Piercing joint between top pie and body.

---

## Cross-item learnings (bootstrap → B1)

- **Bare single-stroke radicals may need MMH-anchor discretion**: 丿 still failed at R1 with too-conservative override. Rule of thumb: if MMH-median puts a stroke > 40 px away from the GT-visible centroid, trust the GT.
- **Hooks + entry ticks should be continuous, not separate line segments** (亅 R1 confirmed): merged curl works.
- **Composite radicals with 3+ turns are the hardest class**: 马, 弓, 阝, 廴, 㔾, 几 all FAIL/C on the multi-turn compound stroke. The bank now has `heng_zhe_gou`, `heng_pie`, `shu_zhe`, `heng_zhe_box`, `ping_na`, `ti` — B2 retries should compose these cleanly rather than re-inlining.
- **Left-position radicals shrink AND drift right in Phase-3**: applies to 亻, 扌, 彳, 犭 when embedded. Not yet tested in Phase-3, but pre-registered as a hypothesis.
- **Sibling pairs to watch** (accumulated for B2 dispatch attention):
  - 士 vs 土: top-heng length (士 longer top, 土 longer bottom) — already handled correctly in 士.
  - 干 vs 于 vs 千: 干 has TWO heng + shu piercing both; 于 has one heng + heng+hook; 千 has pie + heng + shu.
  - 己 vs 已 vs 巳: top-loop closure. 己 = open top-left.
  - 刀 vs 力: 力 has piercing pie through heng_zhe_gou; 刀 has neighbor-only.
  - 人 vs 入: 人 head at TC, 入 head at C (na extends up past pie).

---

## B2 (2026-08-08) — 18 FAILs + 13 C's + 8 retry FAILs + 7 retry C's

### FAIL cluster A: compound-stroke gaps (bank missing the class)

**p2_radical_074_兀 (wu) — FAIL** — 3 strokes. Right leg is 竖弯 (no upward hook). Drawer knew this and inlined shu_wan_bare. Failure likely proportion / leg-spread balance. Retry hint: use bank draw_shu_wan_gou but override to NOT render the hook (or extract shu_wan_bare primitive).

**p2_radical_094_风 (feng) — FAIL** — 4 strokes. s2 is 横斜弯钩, a single fluid arc across-top-then-down-right-then-hook. Bank has no primitive for this class. Terminal-freeze if a second retry FAILs — the arc is drawer-tunable but subtle.

**p2_radical_111_气 (qi) — FAIL** — 4 strokes. s4 is 横斜钩 (heng + xie + hook). Same class problem. Retry with the new `xie_gou.py` for s4 with head at (~155, 105) and tail at (~275, 235) — the horizontal head-run turns into the diagonal descent naturally.

**p2_radical_115_氏 (shi) — C** — s4 is xie_gou. Now that `xie_gou.py` exists in the bank (extracted from 弋+戈), retry should use it directly instead of the shu_wan_gou substitute the drawer tried.

**p2_radical_099_旡 (ji) — FAIL** — 4 strokes. Composite shape resembling 无 with extra top tick. Drawer used shu_wan_gou but stroke class is likely 横斜钩. Retry hint: use `xie_gou.py` for s4.

**p2_radical_088_长 (chang) — FAIL** — 4 strokes: pie + heng + pie + na, but the pie is a long xie-diagonal and the na is a wide sweep. This is the same class as 长/衣/农. Retry hint: model s3 as a long pie with steep bow (bow_perp=25) starting near center; s4 na starts near s3's mid, sweeps to BR.

### FAIL cluster B: multi-turn compounds (still hard even with new bank)

**p2_radical_082_子 (zi) — FAIL** — 3 strokes. s1 is 横撇 (short + compact, not the wide 又 shape); s2 is 弯钩 (curved-body vertical, left hook). Bank has no direct 弯钩 primitive (shu_gou is straight-body). Retry hint: inline curved-body with a modest rightward bow, then shu_gou-style left hook.

**p2_radical_078_幺 (yao) — FAIL** — 3 strokes with 2 pie_zhe compounds. Bank has heng_pie (wrong order) and no pie_zhe. Note for B3: `pie_zhe.py` promotion candidate if a retry attempt PASSes.

**p2_radical_105_肀 (yu, brush-hand) — FAIL** — 4 strokes with central vertical piercing 2 hengs. Drawer used shu + 2 heng + slanted stroke, but proportion likely wrong. Related to 手 (also C). Retry hint: reference 手's PASS geometry once achieved.

**p2_radical_107_爿 (pan) — FAIL** — 4 strokes forming a mirror bracket. Complex; low-frequency. Terminal-freeze after 1 more retry.

**p2_radical_118_殳 (shu) — FAIL** — 4 strokes. Top is 几-shape, bottom is 又-shape. Drawer inlined the top heng-zhe. Retry hint: for s2 use heng_zhe_short with corner_offset increased; for s3/s4 use draw_you (又 primitive) with appropriate transform.

### FAIL cluster C: 3-4 stroke radicals with tight geometry

**p2_radical_075_夕 (xi, evening) — FAIL** — 3 strokes: short pie + long pie + interior dian. Drawer used correct primitives but composition proportions likely off. Retry hint: for s1 (top-right curl) use bow_perp=15 for a strong curve.

**p2_radical_081_夂 (zhi) — FAIL** — 3 strokes: 2 pies + na (bottom X, P joint). Same skeleton as 攵's lower half but with 3 strokes not 4. Retry hint: use draw_pu but override to skip s2 (heng).

**p2_radical_086_比 (bi) — FAIL** — 4 strokes forming two sub-radicals side by side. Complex composition. Retry hint: the LEFT half is 匕 (bi_dagger), the RIGHT half is 匕 rotated; use two draw_bi calls with different transforms.

**p2_radical_090_歹 (dai) — FAIL** — 4 strokes. Similar to 夕 but with an extra heng on top. Related family to 夕 (also FAIL). Retry after 夕 PASSes.

**p2_radical_093_方 (fang) — FAIL** — 4 strokes: dian + heng + 横折钩 + pie. Bank has heng_zhe_gou but drawer inlined a simpler shape. Retry hint: use draw_heng_zhe_gou for s3 with heng_head=(56, 130), corner=(220, 130), gou_tail=(180, 260), hook_tip=(155, 245).

**p2_radical_098_火 (huo, fire) — FAIL** — 4 strokes: dian + dian + pie + na (bottom X). Same skeleton as 攵 but with 2 dians replacing the top pie+heng. Now that pu_action.py PASSed, retry hint: use draw_pu with s1/s2 replaced by two dians (via BANK_DEVIATION).

**p2_radical_100_见 (jian) — FAIL** — 4 strokes: box top + 儿 bottom. Same top-box as 贝 (also C). Class: box+leg composition. Retry hint: use draw_wei_enclose (or draw_kou) for top with a slightly compressed footprint (~scale 0.55), then draw 儿 (shu_wan_gou + pie) below.

**p2_radical_109_攴 (pu, tap) — FAIL** — 4 strokes = 卜-top + 又-bottom. Drawer confused geometry with 攵 (which PASSed). Retry hint: 攴's top is 卜 (shu + dian angling down-right), NOT pie+heng. Use draw_bu for top half.

### C cluster: proportions / minor tuning

**p2_radical_070_纟 (silk-radical) — C** — Bank lacks pie_zhe. Retry with inline compact pie_zhe. Related to 幺 FAIL.

**p2_radical_071_巳 (si) — C** — 3 strokes: heng_zhe_short + heng + shu_wan_gou (same as 己). Distinguishing feature: 巳's s3 starts at TL height (~91) not ML (~146). Retry hint: nudge shu_wan_gou head up to y=90.

**p2_radical_080_尢 (wang) — C** — 3 strokes: heng + long pie + shu_wan_gou. Simple; proportions off. Retry with tighter x-spread.

**p2_radical_084_夊 (sui) — C** — 3 strokes: pie + pie + na (bottom X). Related to 夂 FAIL. Same retry hint (draw_pu-like structure without heng).

**p2_radical_085_贝 (bei) — C** — 4 strokes: box + 八 bottom. Related to 见 FAIL. Retry hint: use draw_wei_enclose at ~scale 0.55, ox +20, oy -20 for compressed top-box; then draw_ba below.

**p2_radical_092_厄 (e) — C** — 4 strokes: 厂 outer + 㔾 inner. Drawer used draw_chang correctly. Interior likely off. Retry hint: interior heng-zhe (s3) at (75, 138)→(180, 138) then wrap with s4 shu_wan_gou.

**p2_radical_101_斤 (jin) — C** — 4 strokes. Drawer used correct primitives. Proportions and shu tail length likely off (MMH said y=320, drawer capped).

**p2_radical_102_耂 (lao-top) — C** — 4 strokes: short heng + shu + long heng + long pie. Similar to 老. Retry hint: this radical is basically 土 + long pie; consider `draw_tu` + pie composition.

**p2_radical_103_毛 (mao) — C** — 4 strokes: pie + heng + heng + shu_wan_gou. Sibling of 手 (also C). Distinguishing: 手 has shu_gou (central hook) with 3 hengs; 毛 has shu_wan_gou (right-curl) with 2 hengs + top pie.

**p2_radical_108_片 (pian) — C** — 4 strokes. Complex bracket-like shape. Compound stroke s4 is heng-zhe. Related to 爿 FAIL (mirror image).

**p2_radical_116_礻 (shi, spirit-radical) — C** — 4 strokes: dian + heng_pie + shu + dian. Drawer used correct primitives. Proportions likely off; the shu should be centered exactly under heng_pie's mid.

**p2_radical_117_手 (shou) — C** — 4 strokes: top curve + 2 hengs + shu_gou. Drawer used correct primitives. Sibling with 毛 (C). Retry hint: the shu_gou head at TC(0.389, 0.92)=(139,92) sits INSIDE the top curve loop; ensure the curve wraps above it. Now that `手` C, may need principle: the s1 top hook is a compact curl NOT a pie.

### Retry channel — B2 (20 R1 items from B1 queue + 3 R2)

**PASS at R1 (3)**: 廴, 巾, 饣 — all directly used the new B1 stroke primitives (ping_na, heng_zhe_box, ti). Confirms P-RET-003: promoting compound stroke primitives directly enables recovery.

**C at R1 (7)**: 门, 讠, 寸, 尸, 己, 阝, 弓 — closer to PASS but not there. All get queued to B3 R2.

**C at R2 (2)**: 儿, 门 — 儿 will likely stay C; **terminal-freeze after R2**.

**FAIL at R1 (7)**: 宀, 女, 犭, 巛, 马, 飞, 㔾 — nothing about the new primitives helps these. Most are complex compound shapes.

**FAIL at R2 (2)**: 丿 (2nd retry failed), 儿 not yet R2-FAIL (still C). 丿 and 㔾 both hit **terminal-freeze**: two batches, no progress.

### Cross-item learnings (B2)

- **MMH stroke count trumps whole-radical primitive stroke count** (P-COMP-001). Do NOT force draw_kou for 日 (4-stroke) or 囗 (3-stroke but big-canvas).
- **Two-BANK_DEVIATION promotion rule** (P-COMP-002). Applied for xie_gou (弋+戈 both PASSed inline).
- **Sibling-pair failures cluster on the distinguishing feature** (P-COMP-003). B2 evidence: 户/尸/肀 (top-dot), 攴/攵 (top-half class), 弋/戈 (stroke count), 手/毛 (shu variant class).
- **Bottom-X composition (pie + na crossing)** is now well-covered by draw_pu (攵). Sibling failures 火/夂/夊/父 all share this pattern; retry with draw_pu as the base.
- **Box + leg composition** (见/贝) — needs both `draw_wei` (or scaled draw_kou) AND the leg component. Currently no unified helper; will need to develop for Phase-3.
- **Xie-gou family** (斜钩) is now bank-covered. Any radical with a long diagonal + terminal up-hook (弋/戈/我/成/找) can call `draw_xie_gou`.

---

## B3 (2026-08-08) — 8 main FAILs + 7 main C's + 12 retry FAILs + 19 retry C's

### FAIL cluster HH — Missing heng_zhe_wan_gou-family primitive (Phase-3 hook cluster)

**p3_char_0016_乃 (nai) — FAIL** — 2 strokes. s1 is 横折折折钩 (4-segment
compound: heng, first turn down, second turn leftward-down, hook back-right).
No bank primitive covers this; drawer inlined via 3-bezier chain but result
didn't cohere as 乃 silhouette. Retry hint for B4: consider more angular
first-corner geometry; 乃 is an unusual multi-turn shape best modeled as
segmented polyline with explicit ~90° corners.

**p3_char_0018_乜 (mie) — FAIL** — 2 strokes: heng + shu_wan_gou. Drawer
used both bank primitives. Cause likely proportion/silhouette — 乜's s2 wraps
wide right and comes back up sharply. Retry hint: extend shu_wan_gou tail
further right + higher up (approaching upper-right past MMH tail anchor).

**p3_char_0019_儿 (er) — FAIL** — Same class as p2_radical_017_儿 (terminal-frozen
after 3 batches of C). Phase-3 儿 also FAILed on first attempt. Sibling
proportion issue persistent; may terminal-freeze after 1 retry.

**p3_char_0021_几 (ji) — FAIL** — 2 strokes: pie + 横折弯钩. Bank has no
`heng_zhe_wan_gou` primitive. Drawer inlined `heng_zhe_wan_gou_for_几`
BANK_DEVIATION. FAILed on visual proportions. Retry hint for B4: use the
sandbox `heng_zhe_wan_gou` geometry spec (see B3 sandbox postmortem).

**p3_char_0023_九 (jiu) — FAIL** — 2 strokes: pie + 横折弯钩. Same class
as 几 (both need heng_zhe_wan_gou). Same failure mode. Same retry hint.

### FAIL cluster W — 3-directional stroke radicals

**p2_radical_119_水 (shui) — FAIL** — 4 strokes: central curving shu +
short pie + upper-right pie + right na. Drawer composed correctly from
stroke bank but the central curving shu didn't read as water's central
line, and the tight spacing of the two side pies + na wasn't captured.
Retry hint: use a stronger curve on s1 (approach as pie with bow rather
than shu_gou); tighten s3 head toward center.

**p2_radical_120_瓦 (wa) — FAIL** — 4 strokes with s3 being 横折弯钩 (same
missing primitive as cluster HH). Drawer inlined; FAILed. Retry hint:
try with sandbox heng_zhe_wan_gou spec; s4 dian should be smaller.

**p2_radical_134_爪 (zhua) — FAIL** — 4 strokes; s3 shu drops off canvas
(MMH tail y=312 > 300). Drawer used shu bank. FAILed likely on
proportion — top strokes should sit higher and tighter. Retry hint:
compress vertical extent of top pies + na to fit above the shu head.

### C-verdict cluster — proportion / structure close but not through

**p2_radical_121_尣 (wang variant) — C** — 4 strokes; sibling of 尢/尤.
Drawer used pie, dian, pie, shu_wan_gou. Proportions off.

**p2_radical_123_韦 (wei) — C** — 4 strokes with a compound bottom hook.
BANK_DEVIATION `wei_bottom_hook_for_韦` inline. Close silhouette but not
right. Retry hint: bottom hook needs wider horizontal + smaller descending curl.

**p2_radical_125_毋 (wu) — C** — 4 strokes; BANK_DEVIATION for compound s1.
Retry hint: joint constraints are complex (5 P joints + 1 N); may need
multiple retries.

**p2_radical_126_心 (xin, heart) — C** — 4 strokes; s2 is 卧钩 (wide
smile-shape). No bank primitive for 卧钩; drawer inlined via cubic bezier
(fresh_component `wo_gou_for_xin`). Retry hint: **candidate primitive
`wo_gou.py` if a retry PASSes** — 卧钩 appears in 心/必/志/忠/忽 (all high-freq).

**p2_radical_127_牙 (ya) — C** — 4 strokes; composed from stroke bank.
Proportions off. Retry hint: s2 heng should span wider (right edge farther out).

**p3_char_0026_冂 (jiong) — C** — 2 strokes: shu + wide heng_zhe. BANK_DEVIATION
`heng_zhe_wide_for_jiong`. Same class as p2_radical_024_冂 attempt. Retry hint:
if a retry PASSes, promote `heng_zhe_wide.py` (differs from heng_zhe_short and
heng_zhe_box).

**p3_char_0027_七 (qi) — C** — 2 strokes: rising heng + curved descend
(BANK_DEVIATION `pie_wan_for_qi`). Retry hint: descend needs stronger
bend + terminal upflick.

### Retry-channel outcomes B3

**PASS at R1 (2)**: 肀, 幺 — both directly used new stroke primitives
(heng_zhe_short for 肀 top; pie_zhe now extracted from 幺).

**PASS at R2 (5)**: 门, 讠, 阝, 宀, 女 — all recovered with careful
trajectory-diff work. Strong showing at R2 (5/6 R2 escalations PASSed).
Validates the retry channel's value.

**C at R1 (14)**: 氏, 旡, 气, 火, 巳, 见, 贝, 斤, 厄, 耂, 毛, 手, 礻, 片 —
close but not through. Requeue to B4.

**C at R2 (5)**: 寸, 尸, 己, 弓, 几 — all C at second retry. **Terminal-freeze
candidates** unless a specific unblock is identified.

**FAIL at R1 (12)**: 攴, 方, 子, 兀, 长, 夂, 夊, 歹, 夕, 比, 纟, 尢 — geometry-hard
across the board. Several are terminal-freeze candidates after this second failed attempt.

### Cross-item learnings (B3)

- **A-recipe emerged (P-A-001 + P-A-002)**. Route 1: identity bank reuse
  (人 A, 又 A). Route 2: meticulous MMH-verbatim composition with taper
  (爻 A, 了 A). Both routes require stroke-count match + explicit taper.
- **Alignment via wrapper** (P-COMP-004). 宀 R2 PASSed via draw_mi_cover
  wrapping the left-dian + roof pair; R1 FAILed by drawing them independently.
- **Whole-radical vs stroke-recomposition rule refined** (P-COMP-005): if
  MMH anchors match a bank primitive within tolerance (structural identity),
  use whole-radical; if anchor spread or stroke count differs, compose
  from stroke primitives.
- **Missing heng_zhe_wan_gou primitive** blocks the 几/九/瓦/风/凡 family
  and likely other Phase-3 items. Explicit sandbox geometry spec provided
  for B4 drawers; if a B4 retry PASSes with the spec, promote.
- **卧钩 (wo_gou) also missing**; blocks 心/必/志/忠. Candidate primitive
  for B4 promotion if a retry PASSes.
- **Sibling 无/旡/既** — 无 PASSed (draw_wu_none); 旡 still C. Distinguishing
  feature: top-stroke type + s2 curl direction.

---

## B4 (2026-08-08) — 8 main FAILs + 13 main C's + 21 retry FAILs + 10 retry C's

### FAIL cluster HW — hook/curve/wrap family (Phase-3, mains)

**p3_char_0034_刁 (diao) — FAIL** — 2 strokes: heng_pie + tall curved-shu-with-left-hook.
BANK_DEVIATION noted "no fresh_component — reuse wan_gou with tuned params" but
wan_gou default belly_right=27 is too shallow for 刁's tall body. Retry hint:
call wan_gou with belly_right=42, hook_len=32, hook_up=20 for a taller frame.

**p3_char_0044_丸 (wan) — FAIL** — 3 strokes: pie + heng_zhe_wan_gou-like + dian.
Bank has NO primitive for s2 (same class as 九/几/瓦/风). Drawer inlined
`heng_zhe_wan_gou_for_丸`. FAILed on shape. Same missing primitive as B3 HH
cluster. Retry hint: try wan_gou primitive with head at the corner and belly
pulled to the bottom-right.

**p3_char_0047_也 (ye) — FAIL** — 3 strokes: heng + shu + shu_wan_gou. All bank primitives
used. FAIL because default shu_wan_gou (bottom_extra=60, knee_ratio=0.75) is
tuned for 匕/儿's compact form; 也's wrap extends much further right. Retry hint:
call shu_wan_gou with bottom_extra=80, knee_ratio=0.60, and pull tail x
to ~285 for the long right sweep.

**p3_char_0049_子 (zi) — FAIL** — 3 strokes: heng_pie + wan_gou + heng. Bank
has all 3 primitives; both wan_gou (from 了 A-verdict) and heng_pie now available.
FAIL persists across main + R2. Sibling 孑 and 孓 both PASSed B4 with heng_pie
tuning, but 子's cross-bar heng distinguishes and the composition proportions
are tighter. **Terminal-freeze candidate** after B5.

**p3_char_0060_卂 (xun) — FAIL** — 3 strokes: xie_gou + heng + shu. All bank
primitives used with MMH anchors. FAIL likely because xie_gou's terminal hook
flick visually collides with the shu; drawers should reduce hook_back on xie_gou
or offset shu ~10 px right of MMH C anchor.

**p3_char_0061_与 (yu) — FAIL** — 3 strokes: heng + heng_zhe_gou (full-height) + heng.
FAIL because default heng_zhe_gou is tuned for 力's compact size. Retry hint:
pass explicit heng_head=(TC, top), corner=(TR, top), gou_tail=(BC, bottom),
hook_tip=(BC-30, bottom-15) for the tall full-frame geometry.

**p3_char_0072_夊 (sui) — FAIL** — 3 strokes: pie + pie + na (bottom-X). Sibling
of 夂 (also FAIL). draw_pu is 4-stroke and can't be used directly. Bank has
pie + na; the 3-stroke bottom-X composition is under-covered.

**p3_char_0073_飞 (fei) — FAIL** — 3 idiosyncratic strokes. BANK_DEVIATION for
all three; fresh_components fei_top_zhe, fei_main_swoop, fei_inner_ti. Highly
character-specific; unlikely to promote as reusable primitive.

### C-verdict cluster B4 (13 items)

**p3_char_0035_丁 (ding) — C** — 2 strokes: heng + shu_gou. Bank primitives used.
Close but not clean. Retry: nudge shu_gou hook_start_offset up (~35) and thicken.

**p3_char_0036_刂 (dao-right) — C** — 2 strokes; sibling of 刀 (which PASSed).
draw_dao_right existed but shape didn't quite match. Retry: extend shu tail
further down and thin the pie.

**p3_char_0046_久 (jiu) — C** — 3 strokes: pie + heng_pie + na. Different from
夂 (2 pies + na). Composition needs middle heng_pie proportions tuned.

**p3_char_0048_乇 (tuo) — C** — 3 strokes; low-freq. Compound with wan_gou-like body.

**p3_char_0050_亍 (chu) — C** — 3 strokes: heng + shu + dian. Similar to 于 sibling family.

**p3_char_0051_于 (yu) — C** — 3 strokes: heng + heng_zhe_gou (thin) + shu. Sibling
of 干/千 (both PASSed). Distinguisher: 于 has TWO horizontal-family strokes
plus vertical, with s2 being a compound heng_zhe_gou.

**p3_char_0058_兀 (wu char) — C** — 3 strokes; sibling of 儿/元 (all in the shu_wan
family). Same class as Phase-2 兀 which terminal-froze at R2.

**p3_char_0059_么 (me) — C** — 3 strokes: pie + heng_pie + dian. Sibling of 幺/纟.

**p3_char_0065_及 (ji) — C** — 3 strokes: pie + heng_zhe_wan_gou (compound) + na.
Missing heng_zhe_wan_gou primitive; drawer inlined.

**p3_char_0070_夂 (zhi) — C** — 3 strokes. Different from Phase-3 dispatch of same
form: see FAIL cluster.

**p3_char_0079_已 (yi) — C** — 3 strokes; sibling family 己/已/巳. Distinguisher:
top opening (己 open TL, 已 half-closed, 巳 closed). 已 close but not through.

**p3_char_0082_尢 (wang variant) — C** — 3 strokes; sibling of 尣 (which PASSed
as p2 R1). Slight proportion difference.

**p3_char_0083_才 (cai) — C** — 3 strokes: heng + shu_gou + pie. Sibling family
with 扌 (which is a radical); 才 stands alone. Retry: bank draw_shou is
4-stroke; 才 is 3-stroke. Compose from stroke bank instead.

### Retry channel — B4 (36 retries: 5 PASS + 10 C + 21 FAIL)

**PASS at R1 (3)**: 尣, 韦, 毋 — all diagnosed by trajectory-diff hints
from B3 postmortem. All 3 promoted (2 as bank primitives 韦→wei_leather,
礻→shi_spirit — 毋 not promoted low-reuse).

**PASS at R2 (2)**: 礻 (via trajectory diff to mid-band crossbar), 长 (via
slim strokes + explicit 竖提 polyline). Both promoted as bank primitives.

**C at R2 (8 — terminal-freeze candidates after 2 rounds of C)**:
- 氏 R2 C — HIGH-priority queue that didn't cash out; xie_gou call didn't
  fit 氏's specific composition. **Terminal-freeze**.
- 子 R2 C — retry with wan_gou didn't fix composition. **Terminal-freeze**.
- 纟 R2 C — pie_zhe primitive available but composition proportions still off.
  **Terminal-freeze**.
- 见, 斤, 耂, 毛, 手 — all C at R2. **Terminal-freeze**.

**C at R1 (2)**: 儿 R1 C (Phase-3 char), 几 R1 C (Phase-3 char).
Both B5 R2 queue.

**FAIL at R2 (14 — terminal-freeze candidates after 2 rounds of FAIL)**:
旡, 气, 火, 巳, 贝, 厄, 攴, 方, 兀, 比, 歹, 夕, 夂, 夊 — all had B3 R1
FAIL/C then B4 R2 FAIL. **Terminal-freeze all**. Diagnoses:
- 旡/气 — both need `heng_xie_wan_gou` compound stroke; no bank primitive
  and inline attempts all failed. Endpoint-dumbbell artifact issue also
  observed in 旡. Terminal-freeze.
- 火 — 4 strokes; bottom-X with 2 dians on top. draw_pu skeleton doesn't
  match. Retry_2 tried direct MMH-inline; still FAIL.
- 巳 — sibling of 己/已; heng_zhe_short + heng + shu_wan_gou. R2 tuning
  bottom_extra=68, knee_ratio=0.72 didn't achieve balance. Terminal-freeze.
- 贝, 见 — box+leg composition. Need dedicated `draw_box_and_儿` helper;
  none created. Terminal-freeze on the radical channel; may revisit
  as Phase-3 chars.
- 攴 — sibling confusion with 攵 (which PASSed). 攴 top is 卜 not pie+heng.
  Attempts confused. Terminal-freeze.
- 兀 — Phase-2 R2 FAIL (Phase-3 has separate 兀 which was C).
  Terminal-freeze radical channel.
- 方 — draw_heng_zhe_gou for s3 should work but composition proportions off.
  Terminal-freeze.
- 夕, 歹, 夂, 夊, 比 — 3-4 stroke tight-geometry radicals; none PASSed
  across 2 rounds. Terminal-freeze.

**FAIL at R1 (7 — B5 R2 queue)**: 牙, 乃, 乜, 九, 水, 瓦, 爪, 儿 (Phase-3 char).

### Cross-item learnings (B4)

- **Identity-reuse (P-A-001) lifts to PASS reliably at Phase-3, but the
  A-verdict yield collapses on 3+ stroke chars.** See P-A-003.
- **Bank primitives baked for Phase-2 radical context often need per-composition
  tuning at Phase-3.** See P-RET-004.
- **Retry escalation past R2 has diminishing returns unless a new bank
  primitive or explicit trajectory-diff was added between rounds.** See P-COMP-006.
- **HIGH-priority retry queue predictions from B3 (氏/旡/气/火/巳 all had
  bank primitives named as unlockers) largely did NOT cash out.** Ranking
  needs more skepticism; the presence of a related bank primitive is not
  enough — the primitive must actually fit the composition's specific
  aspect/orientation/scale.
- **Hook/curve/wrap family continues to be the largest un-covered gap**:
  heng_zhe_wan_gou (blocks 几/九/瓦/凡/丸/及); heng_xie_wan_gou (blocks
  旡/气/风); 卧钩 (blocks 心/必/志). All are candidate primitives if a
  future retry PASSes with a working inline.

---

## B5 diagnostic section (2026-08-08)

### FAIL cluster HZ (heng_zhe_wan_gou family — 5 items)

Same root cause as B3/B4 R2 terminal-freezes: the 横折弯钩 (horizontal
+ right-angle + U-belly + up-right hook) compound is still missing from
the bank. B5 confirmed 5 new items requiring it, all FAILed:

- **p3_char_0085_马** — s1 (small 横折 top) OK via `heng_zhe_short`;
  s2 (big body compound) inlined as `heng_zhe_gou` — WRONG topology
  (heng_zhe_gou has straight-down shu terminal + gou tip; 马 wants
  deep-U belly). Retry with candidate `heng_zhe_wan_gou` spec.
- **p3_char_0097_乌** — same as 马 with extra top 撇 (s1). Same failure
  mode on s3. Sibling of 马 — same retry approach.
- **p3_char_0111_仇** — s4 (九 body) BANK_DEVIATION for
  `heng_zhe_wan_gou_for_九` — inlined attempt FAILed. Compare to B4/B5
  frozen 九 (R2 FAIL). Retry with candidate spec.
- **p3_char_0113_仉** — s4 (几 body) BANK_DEVIATION — same failure. R1
  retry with candidate spec.
- **p3_char_0131_冗** — s4 (几 body inside 冖) BANK_DEVIATION — same.

### FAIL cluster LR (proportion / L-R composition — 5 items)

- **p3_char_0098_以** — L (short-pie + dian) + R (asymmetric 人-like with
  compressed na in BR cell only). Drawer correctly identified `draw_ren`
  didn't fit but the inline pie/na proportion was off — na apex sat too
  far right, making 以 read as 从-shaped. Retry: keep pie tail at
  BC(115.7, 269.5), shrink na to fit inside BR cell only.
- **p3_char_0103_亢** — 亠 top + 儿-bottom. s4 was `shu_wan_gou` with
  bottom_extra=60 default — the 儿-bottom in 亢 wants wider wrap
  (P-RET-004 applies). Retry: bottom_extra=80, knee_ratio=0.65.
- **p3_char_0114_见** — 4 strokes: shu + heng_zhe_box + pie + shu_wan_gou.
  Drawer noted the wide-N joint (s3.mid ⇆ s4.head ≈54.4 px vs expected
  ~20 px). Box scale-up + pie/shu_wan_gou tuning per that joint.
- **p3_char_0123_兮** — s4 is a short `wan_gou` (C→BC ~109 px shaft).
  Drawer tuned wan_gou but likely still too straight. Retry with
  explicit belly_right=15, hook_len=20 for the shorter shaft.
- **p3_char_0121_內** — sibling of 内 (which PASSed). Both are shu +
  heng_zhe_gou + pie + na, but 內 is Traditional shape (人-inside)
  while 内 (which PASSed) is Simplified 入-inside. Drawer used same
  inline for both — 內's inner should be 人 (pie shorter, na longer)
  but was drawn as 入-style. Sibling-pair error. Retry with clearer
  s3/s4 geometry per MMH block for 內.

### FAIL cluster HP (heng_pie proportion — 1 item)

- **p3_char_0099_予** — s1 and s2 both `heng_pie` DEVIATIONS. Bank
  primitive tuned for 又 (wide, gentle bow). 予's tops want compact
  angular heng-pie (narrow horizontal, steep pie). Drawer inlined but
  proportion still didn't cash. Retry with apex_x=+80, bow_perp=25
  (steeper), narrower horizontal.

### C-verdict cluster (12 items)

- **Multi-curve calligraphic (4)**: 巛, 川, 幺, 乡 — bank has `chuan_river`
  for 川 but curve calligraphy remains poor. Deferred; not R1-queued.
- **Proportion (7)**: 义, 仃, 无, 仑, 仓, 切, 冘, 气 — L-R or top-bottom
  proportion issues, none require new primitive. Selective retry with
  trajectory-diff.

### Retry outcomes (B5 R2 slots — 9 items, 0 PASS)

**P-COMP-006 rule confirmed exactly**. 8 R2 FAILs + 1 R2 C: no new bank
primitive was added between R1 (in B4) and R2 (in B5) for any of these
items. All 9 items involve the still-missing heng_zhe_wan_gou family.
Terminal-freeze all 9:

- p2_radical_127_牙 R2 FAIL — terminal-freeze
- p3_char_0016_乃 R2 FAIL — terminal-freeze
- p3_char_0018_乜 R2 FAIL — terminal-freeze
- p3_char_0023_九 R2 FAIL — terminal-freeze
- p2_radical_119_水 R2 FAIL — terminal-freeze
- p2_radical_120_瓦 R2 FAIL — terminal-freeze
- p2_radical_134_爪 R2 FAIL — terminal-freeze
- p3_char_0021_几 R2 FAIL — terminal-freeze
- p3_char_0019_儿 R2 C — terminal-freeze (per P-COMP-006 R2-C policy)

### Cross-item learnings (B5, new)

- **P-A-001 identity call does not scale to 4-stroke chars** — 文, 日,
  中, 工 all identity-called existing bank radicals; all PASSed but
  none earned A. Confirms P-A-003; codified as P-A-004.
- **1st PASSing DEVIATION on a distinct MMH-named stroke class is
  sufficient promotion evidence** — codified as P-COMP-007. wo_gou
  and heng_zhe_wide promoted on 1st evidence (not waiting for 2nd).
- **A missing bank primitive can cascade across a whole compound
  character family for 3+ batches** — heng_zhe_wan_gou has now blocked
  ≥ 15 items (几, 九, 儿, 乃, 乜, 瓦, 爪, 水, 牙, 马, 乌, 仇, 仉, 冗, +
  earlier 及, 凡, 丸). Codified as P-COMP-008: elevate to hypothesis-
  driven candidate spec in sandbox for the next batch to attempt.
- **Sibling pair 内/內**: Simplified vs Traditional inner-radical
  (入-inside vs 人-inside). Add to sibling-pair notes; drawer must
  distinguish per glyph.

## B6 (2026-08-08, position 318-368) — diagnostic notes

### Main-channel FAILs (8) — 4 clusters

**Cluster A: WAVE / WRAPAROUND (3)**
- **p3_char_0135_刅 (FAIL)**: 4-stroke 刀+2 side ticks. Inline heng_zhe_gou
  had wrong topology for the compact 刀 body. Fix: inline heng_zhe with
  tighter joint (do NOT call bank heng_zhe_gou). Very-low-freq — do not retry.
- **p3_char_0138_水 (FAIL)**: 4-stroke 3-directional 水. Bank gap. Bare 水
  terminal-frozen in B4. Do not retry.
- **p3_char_0170_发 (FAIL)**: 5-stroke top-heavy 发. All bank primitives used;
  proportion off. **HIGH-freq** char. Retry hint: compress top heng, shorten
  na tail. MEDIUM priority for B7 R1.

**Cluster B: CHRONIC-FREEZE family (1)**
- **p3_char_0144_风 (FAIL)**: 4-stroke. Needs heng_xie_wan_gou (right side
  outer wrap + hook). Bank gap. Bare 风 terminal-frozen in B4. Inline
  3-segment tapered polyline attempted; FAILed. Do not retry.

**Cluster C: L-R proportion (3)**
- **p3_char_0150_引 (FAIL)**: 4-stroke 弓+丨. Bank has NO 弓 primitive
  (bare 弓 terminal-frozen in B3). Any 弓-prefix will FAIL. LOW retry priority.
- **p3_char_0154_他 (FAIL)**: 5-stroke 亻+也. 也 needs heng_zhe_wan_gou top
  arc. Bank gap. Do not retry.
- **p3_char_0177_仗 (FAIL)**: 5-stroke 亻+丈. Proportion off (亻 too big).
  Retry hint: `draw_ren_left(ox=-63, scale=0.55)`, extend 丈 right anchors.
  MEDIUM priority for B7 R1.

**Cluster D: Rare structure (1)**
- **p3_char_0163_丱 (FAIL)**: 5-stroke rare guan. Inline BANK_DEVIATION
  reasonable but wide anchor spread + rare char. Do not retry.

### Main-channel C's (10) — proportion / sibling / rare

- **p3_char_0136_比 (C)**: 匕/匕 sibling confusion; needs sibling-pair
  discipline (see drawer_memory B6 sibling notes).
- **p3_char_0141_办 (C)**: close but proportion tuning; low ROI.
- **p3_char_0153_卬 (C)**: rare structure; low ROI.
- **p3_char_0155_必 (C)**: uses draw_wo_gou; dot placement off. MEDIUM retry.
- **p3_char_0160_可 (C)**: no clear mechanism; low ROI.
- **p3_char_0168_用 (C)**: 4-stroke box + strokes; close proportion; LOW.
- **p3_char_0169_疋 (C)**: rare structure; low ROI.
- **p3_char_0179_付 (C)**: 扌+寸 L-R proportion. MEDIUM retry.
- **p3_char_0180_打 (C)**: 扌+丁 L-R proportion. MEDIUM retry.
- **p3_char_0183_仞 (C)**: rare structure; low ROI.

### Retry FAILs at R1 (12) — heng_zhe_wan_gou hypothesis TEST-FAILED

**Hypothesis test outcome**: sandbox `heng_zhe_wan_gou` candidate spec
(P-COMP-008) was made available to B6 R1 drawers for the 5 hook-family
items (马, 乌, 仇, 仉, 冗). All 5 FAILed. **The "just missing primitive"
hypothesis is INSUFFICIENT** for this family — failure is composition-level,
not just bank gap.

- **马 R1 FAIL**: distinct compound (heng_zhe_zhe_gou with down-left hook,
  not heng_zhe_wan_gou). Inline attempted. Terminal-freeze.
- **乌 R1 FAIL**: 马 + top pie. Same missing compound. Terminal-freeze.
- **仇 R1 FAIL**: 亻+九. 九 needs the compound. Terminal-freeze.
- **仉 R1 FAIL**: 亻+几. 几 needs the compound. Terminal-freeze.
- **冗 R1 FAIL**: 冖+几. Same. Terminal-freeze.
- **予 R1 FAIL**: heng_pie tightness trajectory-diff FAILed. Terminal-freeze.
- **亢 R1 FAIL**: shu_wan_gou wider trajectory-diff FAILed. Terminal-freeze.
- **以 R1 FAIL**: right-人 asymmetric trajectory-diff FAILed. Terminal-freeze.
- **见 R1 FAIL**: box + shu_wan_gou tuning FAILed. Terminal-freeze.
- **兮 R1 FAIL**: wan_gou tuning FAILed. Terminal-freeze.
- **无 R1 FAIL**: LOW-priority burn-test per B5 postmortem. Confirmed FAIL.
  Terminal-freeze.
- **气 R1 FAIL**: LOW-priority burn-test (bare 气 was terminal-frozen in
  Phase-2). Confirmed FAIL. Terminal-freeze.

### Retry PASSes (2, including first-ever retry A)

- **义 R1 A (p3_char_0089__retry_1)**: **First A verdict from retry channel**.
  P-A-005 recipe (see principle_bank + drawer_memory B6 sections). Promoted
  as `yi_x.py`.
- **内 R1 PASS (p3_char_0121__retry_1)**: trajectory-diff (pie head raised
  above box top, na shortened to inside box) worked. Kept inline; low
  general reuse.

### Cross-item learnings (B6, new)

- **P-A-005 (retry-A recipe)**: for 3-stroke crossing chars, force welded
  crossings at MMH-anchored joint points using **negative** bow_perp on
  the primary stroke. Not just endpoint anchors — deliberately-tuned bow
  direction is what closes the gap between PASS and A.
- **P-COMP-008 hypothesis test result**: candidate specs must PASS at least
  once to justify bank promotion. A candidate that FAILs across many items
  is EVIDENCE against, not just null. Do NOT hand-craft a primitive to
  bank without a PASSing case.
- **Cross-group PASS-lift compounding**: G5 vs G3 delta was +12 (B3), +4
  (B4), +16 (B5), +18 (B6). The B4 dip appears item-pool artifact; the
  trend line is UP. MMH's value is not attenuating at depth — it is
  intensifying.
- **弓-prefix chars are a family gap**: 引 FAIL confirms that any 弓-prefix
  will FAIL until 弓 gets a bank primitive. Bare 弓 was terminal-frozen in
  B3; a Phase-3 char with cleaner composition would need to inline-PASS
  the 弓 body first before we can promote.
- **Wave-family (水/氺) may need a curve primitive library**: 水 and 氺
  both need multi-directional flowing curves that don't decompose into
  standard MMH stroke classes. Same for 巛/川-tail forms. Consider this
  a design-space issue, not just missing primitive.

---

## B7 (2026-08-08) diagnostic — BIGGEST CROSS-GROUP DELTA YET

**Raw counts (mains 50, Phase-3 idx 184-233)**: 5 A + 28 PASS + 9 C + 8 FAIL = **33/50 = 66% PASS**.
**Retry queue (7)**: 2 PASS (用, 比) + 3 C (必, 付, 打) + 2 FAIL (发, 仗).
**Cross-group vs G3 B7** (same items, no MMH): G3 = 16/50 = 32%; G5 = 33/50 = 66%. **Delta = +34 pts absolute — biggest cross-group delta of the experiment (previous best B6's +18)**.
**Cumulative through B7**: **221/368 = 60% PASS, 9 A total**.

### 5 A verdicts — one recipe

All 5 A verdicts (业, 仟, 仨, 冉, 乓) followed **P-A-006**: MMH anchors
verbatim + stroke-primitive layer (skipping whole-radical composition).
See principle_bank.md for full recipe.

- **业 (p3_char_0184 A)**: 5-stroke grid; 2 shus + 2 dians + baseline heng.
- **仟 (p3_char_0185 A)**: L-R 亻+千 template; bypasses draw_ren_left + draw_qian_thousand.
- **仨 (p3_char_0189 A)**: L-R 亻+三 (NOT promoted separately — template already crystallized in 仟).
- **冉 (p3_char_0201 A)**: frame + wide-piercing bar. s5 overdraws s1/s2 for welded P-joints.
- **乓 (p3_char_0224 A)**: 6-stroke 丘 + descender. s2 uses bow_perp=-4 (negative).

### 8 mains FAILs — 4 clusters

**Cluster A: L-R double-transform (2)**
- **仡 (p3_char_0187 FAIL)**: 亻 (bank) + 乞 (inline) — 乞's inline hook body mis-shaped. See P-COMP-009 corollary.
- **边 (p3_char_0188 FAIL)**: 辶+力 wrap; chuo_walk + li_power double-transform. Direct P-COMP-009 evidence.
- **记 (p3_char_0214 FAIL)**: 讠+己 L-R; 己's inline hook family unresolved (chronic heng_zhe_wan_gou gap).

**Cluster B: BANK_DEVIATION fresh-composition FAIL (2)**
- **东 (p3_char_0196 FAIL)**: BANK_DEVIATION for shu_gou-at-diagonal (`dong_spine_diagonal`); fresh composition didn't cohere. Bank gap = "diagonal-with-hook".
- **冎 (p3_char_0209 FAIL)**: rare-char inline; anchor cluster mis-interpreted.

**Cluster C: chronic freeze family (2)**
- **处 (p3_char_0212 FAIL)** + **処 (p3_char_0213 FAIL)**: both variants FAILed. 処's BANK_DEVIATION explicitly cited no-夂/no-几 bank. **Clean falsification**: this cluster is genuinely stuck at the composition-level, not just the bank gap (same as B6 hook-family P-COMP-008 update).

**Cluster D: 阝-position (1)**
- **那 (p3_char_0233 FAIL)**: 冄+阝 6-stroke. Left 冄 reasonable; right 阝 via ox-shifted draw_er_ear mis-positioned. Codified: 阝-right chars need `er_ear_right.py` variant.

### 9 mains C's — proportion / character-specific

- **加 (p3_char_0190 C)**: L-R 力+口; BANK_DEVIATION on li_power for placement. Awaiting 2nd DEVIATION per P-COMP-002.
- **仫 (p3_char_0191 C)**: 亻+么; BANK_DEVIATION mo_right_variant.
- **癶 (p3_char_0193 C)**: X-cross cluster; close (near-PASS) — footprint composition inline.
- **冋 (p3_char_0205 C)**: rare 4-stroke.
- **册 (p3_char_0207 C)**: sibling of 冊 (PASSed); slight variation didn't land.
- **冯 (p3_char_0211 C)**: 冫+马; 马-body inline sub-PASS. Chronic 马 gap.
- **凹 (p3_char_0217 C)**: character-specific polylines inline.
- **刍 (p3_char_0218 C)**: rare 4-stroke.
- **地 (p3_char_0223 C)**: 土+也; chronic 也/heng_zhe_wan_gou gap.

### Retry outcomes (7)

**PASSes (2)**:
- **用 R1 PASS**: tuning-only retry — moved s1 pie head from MMH-verbatim to share top-left corner of box per errata note. Bank primitives unchanged.
- **比 R1 PASS**: **P-RET-005 evidence** — retry PASS from applying existing B6 sibling-pair note (rebalance 匕/匕 halves, flip right-pie bow_perp negative). No new bank; discipline-driven.

**C's (3)** — terminal-freeze per P-COMP-006:
- **必 R1 C** (idx 155): deepened wo_gou belly, thickened dians. Not enough for PASS.
- **付 R1 C** (idx 179): thinned strokes, MR-crossing forced. Not enough.
- **打 R1 C** (idx 180): shrunk 扌 to scale=0.88, extended 丁 rightward. Not enough.

**FAILs (2)** — terminal-freeze:
- **发 R1 FAIL** (idx 170): top-heavy layout is proportion-level, not joint-geometry.
- **仗 R1 FAIL** (idx 177): pie/na crossing off-anchor after 亻 shrink.

### Cross-item learnings (B7, new)

- **P-A-006 (MMH-anchor + stroke-primitive layer)**: **NEW A-recipe route**
  identified from B7's 5 A's (all followed same pattern). This is now the
  primary route for 5-6 stroke chars — surpasses P-A-001 identity-reuse in
  that range because whole-radical composition suffers double-transform.
- **P-COMP-009 (double-transform diagnosis)**: whole-radical L-R composition
  with `(ox, oy, scale)` uniformly scales both stroke widths AND joint
  positions, which breaks calligraphic proportion for Phase-3 chars with
  asymmetric component sizing (辶+力, 亻+乞, 讠+己). Fix = P-A-006 for the
  compressed component.
- **P-COMP-010 (X-cross cluster is NOT frozen)**: MMH anchors let G5 place
  the crossing at the true joint point (3 PASS + 1 C on X-cross members).
  Cross-group finding: MMH compensates strongest for cluster-blocked
  failures with clean median-endpoint geometry; MMH does NOT compensate
  for compound-stroke primitive gaps (heng_zhe_wan_gou family still frozen).
- **P-RET-005 (sibling-pair discipline R1 route)**: 比 R1 PASS refines
  P-COMP-006 with a third mechanism-change kind. R1 can PASS from
  (a) new bank between rounds, (b) mechanism-specific trajectory diff
  (P-A-005), (c) applying an existing sibling-pair / calibration note.
- **Cross-group PASS-lift compounding continues**: G5 vs G3 delta was
  +12 (B3), +4 (B4), +16 (B5), +18 (B6), **+34 (B7)**. Trend confirms
  MMH's value is intensifying at depth — B4 dip was item-pool artifact.
- **A rate boundary**: user's calibration note (only compare A rates from
  B9 onward for cross-group fairness) implies B7's 5 A's are memory-benefit
  markers, not fair-comparison A's. B8 (idx 234-283) is where fair-comparison
  A verdicts start being available. Per pattern in B7, expect P-A-006
  recipe to continue delivering A verdicts on 5-6 stroke chars with clean
  MMH anchor coverage.

---

## Batch 8 (2026-08-09) — 20 FAILs + 10 C-verdicts + 0 A on 50 mains

**FAIL cluster A — 亻+X 6-stroke L-R with hook-compound right (7 items)**
per P-COMP-011:
- **p3_char_0248_伄** (亻+吊): 吊 = 冂+巾 with hook_compound; bank gap.
- **p3_char_0250_伉** (亻+亢): 亢 needs shu_wan_gou wide-bottom tuning per
  B5 note; drawer inlined; composition-level FAIL.
- **p3_char_0254_伎** (亻+支): 支 = 十+又; 又 heng_pie welds awkwardly
  with 亻 shu; composition proportion.
- **p3_char_0260_伙** (亻+火): 火 pie-dian 4-stroke ordering; P-A-006
  inline doesn't capture.
- **p3_char_0264_伢** (亻+牙): 牙 heng_zhe compound + shu_gou; bank gap.
- **p3_char_0270_伧** (亻+仓): 仓 has 人-cover + top wraparound; bank gap.
- **p3_char_0276_佤** (亻+瓦): 瓦 wave-hook chronic; P-COMP-008 refuted.

All 7 drawers correctly applied P-A-006 (verified: BANK_DEVIATION headers
refusing draw_ren_left). None-of-the-above mechanism-change; do-not-queue.

**FAIL cluster B — whole-radical refusal (P-A-007 R1 candidates, 4 items)**:
- **p3_char_0247_军** (冖+车): drawer inlined 6 strokes; NEVER used
  `mi_cover.py` or `che_car.py`. **B9 R1 with bank primitive call.**
- **p3_char_0265_名** (夕+口): drawer inlined 6; NEVER used `kou_mouth.py`.
  **B9 R1 with draw_kou for bottom.**
- **p3_char_0243_成** (5-stroke 戈-piercing): inlined; NEVER used
  `ge_dagger.py`. **B9 R1 with draw_ge_dagger base.**
- **p3_char_0267_西** (frame + inner): inlined 6; did NOT identity-call
  `si_four.py`. **B9 R1 with draw_si_four as base + inner adaptation.**

**FAIL cluster C — chronic-freeze (3 items, terminal-freeze)**:
- **p3_char_0236_亥**: G4-frozen chronic; interlaced hook body.
- **p3_char_0279_色** (top pie + 巴): 巴 heng_zhe_wan_gou chronic; do-not-retry.
- **p3_char_0283_传** (亻+专): 专 curl-hook chronic gap.

**FAIL cluster D — L-R with 女 inline (2 items)**:
- **p3_char_0253_好** (女+子): drawer inlined `nu_left_compressed` fresh
  component; could have called `draw_nu_woman(ox=-40, scale=0.75)` (bank
  since B3 R2). **B9 R1 with bank 女 + inline 子.**
- **p3_char_0241_如** (女+口): same P-A-006 refusal of nu_woman;
  proportion collapse. Do-not-queue (marginal only).

**FAIL cluster E — hook-body full-char (4 items)**:
- **p3_char_0240_仰** (亻+卬): 卬 heng_zhe descender proportion off;
  composition-level.
- **p3_char_0261_再** (frame + wide piercing bar): drawer adapted from
  `ran.py` (冉 A). Close. **B9 R1 with refined adaptation.**
- **p3_char_0271_老** (top+匕 bottom, 6 str): shu_wan_gou default params
  too compact for 老's wide bottom sweep. **B9 R1 with
  `shu_wan_gou(bottom_extra=75, knee_ratio=0.62)` per P-RET-004.**
- **p3_char_0281_设** (讠+殳): 殳 hook_compound; chronic. Do-not-queue.

**C cluster (10 items — sibling-adjacent proportion / anchor tuning)**:
p3_char_0238_亦 (dian/pie tuning), p3_char_0258_伕 (亻+夫 straight-stroke
should have PASSed; check taper), p3_char_0263_她 (女+也 chronic 也 gap),
p3_char_0266_伥 (亻+长 — long_chang tuning), p3_char_0272_伪 (亻+为 —
为 has hook_compound), p3_char_0274_伫 (亻+宁 — 宁's wan_gou tuning),
p3_char_0277_先 (top pie tuning), p3_char_0278_齐 (6-stroke top+bottom),
p3_char_0280_兆 (dots proportion), p3_char_0282_兇 (儿-body + top).

**Cross-item learnings (5 new)**:

1. **P-A-006 overshoot is real (P-A-007 emerges)**: when the target char
   contains a sub-component whose structural identity matches a bank
   primitive AT NATIVE SCALE, drawers should call the bank primitive —
   not inline via stroke-primitive layer. 4 avoidable FAILs (军/名/成/西)
   from this pattern. Recorded as P-A-007.

2. **亻+X 6-stroke boundary (P-COMP-011)**: P-A-006 recipe (verified via
   仟 A precedent) generalizes only when X is straight-stroke composable.
   7 亻+X FAILs in B8 all had hook-compound right halves; no
   mechanism-change available without bank extension.

3. **STRUCTURAL A CEILING (first fair-A batch)**: same 40% PASS as G4 on
   identical items but 0 A vs G4's 10. G5's uniform PIL line width cannot
   produce the calligraphic weight distribution the judge rewards. Do not
   diagnose 0-A batches as discipline regression when PASS taper/joint
   discipline sample is intact.

4. **Bank primitive usage audit is a curator tool**: for every FAIL,
   check whether generated.py imports the bank primitives corresponding
   to structural sub-components. If not, that's a P-A-007 mechanism-change
   for retry queue.

5. **B7 A-recipe (P-A-006) has finite scope**: 5 A's on B7 were on
   grid-like / straight-stroke L-R chars where anchor precision maxed
   G5's format ceiling. B8's 6-stroke pool has less headroom. Do not
   generalize P-A-006 to "always refuse whole-radical" — that's the
   overshoot P-A-007 warns against.



## B9 (2026-08-09, position 518) — 22/50 PASS (44%), 4 A, 11 C, 17 FAIL; R1 3/7 PASS

**Cross-group delta B9 (idx 284-333)**: G3 12/50 (24% 0A); G4 19/50 (38% 10A);
**G5 22/50 (44% 4A)** — first batch where G5 PASS > G4 PASS. **First G5 A
verdicts since B7** (5 A's in B7, 0 in B8, 4 in B9); breaks the "structural
A ceiling" pattern observed in B8 for a subset of items where P-A-007
reasoning aligned with anchor precision.

### A verdicts (4 items) — deep-dive

- **p3_char_0284_龹 (A)**: NOVEL top-radical (no bank primitive existed).
  6 strokes; A-recipe geometry = cubic-bezier bent-pie (s5) whose control
  points pass through BOTH P-joint centers (s3.mid @ (138.7,135.3) and
  s4.mid @ (126.6,171.8)). Straight chord would miss both. Two opposing
  short dians + 2 stacked hengs + bent pie + right na. Promoted as
  `juan_yong.py`.
- **p3_char_0305_还 (A)**: TEXTBOOK P-A-007 rule-1 application. 不
  (top-right, 4 strokes) inlined at MMH anchors (no 不 bank primitive);
  辶 (wrap, 3 strokes) CALLED as `draw_chuo_walk` (ox=+3, oy=+7 minor
  offset). No BANK_DEVIATION needed — bank primitive fit natively.
  Promoted as `hai_still.py`.
- **p3_char_0313_位 (A)**: TEXTBOOK P-A-007 clause-2 fallback. Drawer
  reasoned in docstring: "Also considered P-A-007 whole-radical route
  (call draw_ren_left + draw_li_stand), but 立 in 位 is aspect-skewed
  (~0.75× width / ~0.98× height) vs standalone li_stand — draw_li_stand
  only accepts uniform scale, would render 立 too short vertically.
  Falling back to P-A-006 per P-A-007 clause 2." **This is the first
  batch where explicit P-A-007 reasoning appears in an A verdict's
  docstring.** Promoted as `wei_position.py`.
- **p3_char_0320_伾 (A)**: 亻+丕. Rejected draw_ren_left because MMH pie
  head at TL(0.87, 0.656) sits higher than baked geometry (clause-2
  fallback); inlined 丕 (no bank primitive). Second explicit P-A-007
  clause-2 reasoning. Promoted as `pi_flourish.py`.

**Why B8 got 0 A but B9 got 4** (same difficulty band): P-A-007 was
NEW in B8 and drawers hadn't yet integrated its reasoning trace. By B9,
drawers explicitly wrote "considered whole-radical vs inline; chose X
because Y" — this reasoning correlates with A verdicts. **P-A-007 is
now a retrieval mechanism, not just a corrective principle** (see
P-A-008: inline-reasoning trace required).

**On P-COMP-011 boundary — 位/伾 A verdicts appear to break the freeze**:
NOT ACTUALLY a break. 位 and 伾 both have RIGHT halves that are
straight-stroke composable (立 and 丕). They satisfy P-COMP-011's
"X = straight-stroke only" condition. The 亻+X hook-compound cluster
(你/伶/伽/佇/佈) still FAILed in B9. P-COMP-011 boundary is intact.

### FAIL cluster analysis (17 items)

**Cluster A — 亻+X hook-compound right (P-COMP-011 confirmed, 6 items)**:
- **p3_char_0297_你** (亻+尔): 尔 has heng_gou + shu_gou. Bank has both
  primitives — drawer used them — but composition tight.
- **p3_char_0314_伶** (亻+令): 令 has 冫 + 卩 hook_compound.
- **p3_char_0318_伽** (亻+力+口 L-M-R): 力 has heng_zhe_gou; drawer noted
  "3-radical tight L-M-R layout" — over-transform risk.
- **p3_char_0326_佇** (亻+宁): 宁 has shu_gou (亅).
- **p3_char_0328_佈** (亻+布): 布 has heng_zhe_gou + shu_gou.
- **p3_char_0317_员** (口+贝): 贝 has hooks. Drawer wrote BANK_DEVIATION
  refusing kou_mouth (compressed aspect) — P-A-007 clause-2 applied
  correctly BUT hook-compound bottom-half is bank gap.

Do-not-queue per P-COMP-011/012 boundary; no mechanism-change available.

**Cluster B — chronic recycles from G3 terminal-frozen items (2)**:
- **p3_char_0306_亨** (亠+口+了): G3 already terminal-frozen; recycled
  for G5 fresh-start bank; still FAILed. Terminal-freeze for G5.
- **p3_char_0315_声** (士+尸-like top+bottom): G3 already terminal-frozen;
  声's top-heng + shu compound + 尸 body has 3-part vertical composition
  that doesn't decompose cleanly into bank sub-components. Terminal-freeze.

**Cluster C — 3-part / crossbar composition (3 items)**:
- **p3_char_0286_冱** (冫+互): 互 has central Z-like compound stroke —
  no bank primitive; drawer inlined and geometry drifted.
- **p3_char_0309_两** (top+2-frame+X-crosses): 7-stroke frame with
  heng_zhe_gou frame + 2 pie-na X-cross pairs; composition-level.
- **p3_char_0307_没** (氵+殳): 殳 hook_compound bank gap (same as B8 设).

**Cluster D — hook-body / long-descender full char (4 items)**:
- **p3_char_0311_身** (7-stroke frame + long descender): "身 frame based
  loosely on zi_self/yue_moon" — geometry adaptation didn't converge.
- **p3_char_0288_凫** (top wrap + 几-frame): no bank; inlined with own
  bezier. Not close enough.
- **p3_char_0331_更** (十+曰-like + 又-descender): rare char, complex.
- **p3_char_0333_条** (夂+木 top+bottom): 夂 no bank; 3-stroke inline
  with pie+heng-pie compound.

**Cluster E — 3-radical L-M-R with tight composition (2 items)**:
- **p3_char_0319_听** (口+斤): 口 narrow-left compressed; 斤 straight
  but 3-part tight layout. Kou compressed aspect known-issue from B8 员.
- **p3_char_0329_运** (云+辶): P-A-007 correctly applied (draw_chuo_walk
  for 辶). Failure was in 云 — s3 撇折 compound (pie-zhe) curl direction.

### R1 retry outcomes (7 items — 3 PASS, 4 FAIL)

**PASS (3)**:
- **p3_char_0247_军 R1 PASS**: called draw_mi_cover (ox=8, oy=-18) +
  draw_che (ox=28, oy=49, scale=0.85) per queue instruction. P-A-007
  rule-1 confirmed. Promoted as `jun_army.py`.
- **p3_char_0243_成 R1 PASS**: tuned xie_gou (bow=14, hook_up=36,
  hook_back=8) + inflated s3 into compact heng_zhe_gou. Did NOT use
  draw_ge_dagger despite queue suggestion (drawer reasoned 成 anchors
  differ from 戈 anchors enough). Promoted as `cheng_become.py`.
- **p3_char_0271_老 R1 PASS**: tuned shu_wan_gou(bottom_extra=32,
  knee_ratio=0.72) per queue P-RET-004 instruction. Promoted as
  `lao_old.py`.

**FAIL (4)** — TERMINAL-FREEZE candidates:
- **p3_char_0265_名 R1 FAIL**: drawer called draw_kou for bottom, tuned
  夕 top; still FAIL. Terminal-freeze — 夕-half proportion is a bank gap.
- **p3_char_0267_西 R1 FAIL**: drawer identity-called draw_si_four; still
  FAIL. 西 inner-marks differ from 四 (top bar + inner shu_zhe direction);
  sibling adaptation didn't converge. Terminal-freeze.
- **p3_char_0253_好 R1 FAIL**: drawer called draw_nu_woman + inline 子;
  still FAIL. Terminal-freeze — 女+子 composition tight even with bank.
- **p3_char_0261_再 R1 FAIL**: drawer adapted ran.py (冉 A precedent);
  still FAIL. Terminal-freeze — 再/冉 sibling diff too far.

### C-verdicts (11 items) — no retries queued

师, 光, 我, 甹, 疔, 进, 疖, 伲, 把, 形, 识. All C-verdicts per P-COMP-006
"no retry without mechanism-change" — none have available P-A-007 lever.

### Cross-item learnings (4 new)

1. **P-A-008 emerges — inline-reasoning trace required for A verdicts**:
   3 of 4 B9 A verdicts explicitly reasoned about "call bank primitive
   vs inline" in the docstring. Contrast: B9 FAILs generally lack this
   reasoning. Curator will now grep for the reasoning trace during
   FAIL-diagnosis pass.

2. **P-A-007 3/4 R1 validation**: 军/成/老 R1 PASSed on mechanism-change
   ("call the bank primitive you skipped" / "tune the bank primitive's
   params"). 名/西 R1 FAILed even after calling the bank primitive —
   P-A-007 is necessary but not sufficient. Sibling-adaptation is a
   separate lever.

3. **P-COMP-012 refines P-COMP-011**: hook-compound right FAILs when the
   compound stroke type is NOT in the bank at usable geometry. 伺 (亻+司)
   PASSed because bank's heng_zhe_gou handled 司's outer 4-anchor compound
   cleanly. The straight-stroke-only rule was a proxy for "bank has
   compound-stroke primitive at usable geometry."

4. **PIL-uniform-line still caps A absolutely on hook-heavy chars**: 4 A
   verdicts (龹/还/位/伾) all have LOW hook density (龹 has none;
   还 hooks live in draw_chuo bank primitive; 位/伾 have none). Hook-heavy
   chars still FAIL absolutely because uniform PIL line can't render the
   hook flick's calligraphic thickening. Consistent with B8's format-ceiling
   observation.


## B10 (2026-08-09, position 568) — main FAILs + retry outcomes

### Main FAILs (15 items)

**Cluster A — 疒-family bank gap (all TERMINAL-FREEZE)**:
- **p3_char_0374_疙**: 疒+乞. Drawer inlined 5-stroke 疒 (dian + heng
  + pie + dian + ti) + 乞 (pie + heng + inline 乙 body). Bank gap on
  疒 whole-radical. Do NOT retry until organic PASS.
- **p3_char_0378_疝**: 疒+山. Inlined; called shan_mountain
  BANK_DEVIATION (山 squeezed inside 疒). Both halves gap.
- **p3_char_0380_疟**: 疒+虐-inner. Inlined 5+3 strokes; no bank for
  either half. Terminal-freeze.
- **p3_char_0382_疠**: 疒+万. BANK_DEVIATION on guang_wide for the
  疒 base + inline 万 (which lacks proper 竖钩 hook variant).
- **p3_char_0372_疌**: 肀-top + 止-body. BANK_DEVIATION on yu_brush_top
  + zhi_stop (both aspect mismatch). Similar bank-gap pattern.

**Cluster B — 亻+X mixed**:
- **p3_char_0340_佚** (亻+失): drawer correctly CALLED ren_left for 亻;
  inlined 失. Terminal-freeze (X-cross bottom of 失 no bank primitive).
- **p3_char_0341_社** (礻+土): drawer BANK_DEVIATIONed BOTH shi_spirit
  AND tu_earth per P-A-007-v2 aspect skew. **B11 R1 P-A-007 candidate**
  — quantitative recheck suggests scale ratios were actually inside
  window; drawer over-applied DEVIATION. Retry with instruction to
  CALL both bank primitives.
- **p3_char_0342_佛** (亻+弗): 亻 inline (declined ren_left); 弗 inline
  (shu_gou hook). Do-not-queue per P-COMP-011/012 boundary.
- **p3_char_0343_即** (皀+卩): No 皀 whole-radical; 5+2 inline. Do-not-
  queue (no available bank primitive).
- **p3_char_0346_佞** (亻+二+女, 3-part): drawer CALLED ren_left correctly;
  BANK_DEVIATIONed er_two + nu_woman. **B11 R1 P-A-007 candidate** —
  quantitative recheck suggests both bank primitives should have been
  CALLED per P-A-007-v2 (ratios inside window). Retry with instruction.

**Cluster C — novel 8-stroke unique compositions (do-not-queue)**:
- **p3_char_0367_事**: unique 龶+口+亅 layout; 8 strokes inline. No
  clean decomposition into bank whole-radicals.
- **p3_char_0368_乖**: 千 shell + mirror-hook cluster. Inline
  stroke-primitive layer; no whole-radical decomposition.
- **p3_char_0370_乶**: rare 甫+乙 with 8-stroke complex layout. Inline
  BANK_DEVIATION on yi_second (bank 乙 wrong aspect for flat bottom).

**Cluster D — compound-heavy right (B11 R1 MEDIUM candidates)**:
- **p3_char_0366_畅** (甲/申 + 勿-like): drawer BANK_DEVIATIONed you_by
  (由) per structural mismatch (申 has s5 shu extending above box vs
  由's compact top). **B11 R1 MEDIUM**: try you_by + extend s5 vertically
  for 申-top overshoot.
- **p3_char_0375_经** (纟+圣, 8 strokes): 纟 has no whole-radical; drawer
  inlined. BANK_DEVIATION on you_again + tu_earth. **B11 R1 MEDIUM**:
  quantitative recheck of both bank primitives; if in window, CALL.

### Retry outcomes (B10 R1, 5 items)

**A (1)** — trajectory-diff mechanism-change:
- **p3_char_0329_运 R1 A**: called draw_pie_zhe with explicit corner
  (140, 210) for s3 (main FAIL had collapsed diagonal). draw_chuo_walk
  kept for 辶. **Validates P-A-005** (trajectory-diff R1 to A) — third
  such A recorded. Kept as inline template (not standalone wrapper) —
  reference `attempts/p3_char_0329_运__retry_1/generated.py`.

**C (1)** — improvement without PASS:
- **p3_char_0311_身 R1 C**: drawer identity-called zi_self base per
  queue instruction; adapted with long-descender pie s7. Improvement
  visible but still C. Terminal-freeze (2 rounds no PASS).

**FAIL (3)** — TERMINAL-FREEZE candidates:
- **p3_char_0288_凫 R1 FAIL**: P-A-008 test queued (rewrite docstring
  with per-sub-component reasoning). Drawer added reasoning trace but
  几-frame + top-wrap composition still FAILed. Bank-gap chronic.
- **p3_char_0333_条 R1 FAIL**: P-A-008 test queued (call draw_mu_wood
  for bottom 木 + inline 夂). Drawer applied but the 夂-top +
  mu_wood composition read as two disconnected pieces (P-COMP-009
  double-transform pattern). Terminal-freeze.
- **p3_char_0309_两 R1 FAIL**: speculative frame + draw_heng_zhe_gou +
  4 inner strokes. Frame proportions off. Terminal-freeze (composition
  chronic).

### C-verdicts (9 items) — no retries queued

张, 佘, 每, 改, 块, 到, 甾, 疚, 学. All per P-COMP-006 no retry without
mechanism-change (none have available P-A-007 lever). 疚 also in
Cluster A (疒-family) — reinforces terminal-freeze.

### Cross-item learnings (3 new)

1. **P-A-009 emerges — quantitative BANK_DEVIATION reasoning is the
   A-quality signature**: 4 of 7 B10 A verdicts contain quantitative
   aspect/scale calc in BANK_DEVIATION blocks; the FAILs (社/佛/佞)
   have qualitative reasoning. Curator now grep-scans BANK_DEVIATION
   blocks for numeric values; qualitative-only DEVIATIONs are flagged
   as P-A-007 mechanism-change candidates.

2. **P-COMP-011 boundary softens**: hook-compound right halves reach A
   when hook lives inside a stroke primitive at usable scale
   (佔 亻+占 with kou_mouth DEVIATION → inline heng_zhe_box PASSes at A;
   佟 亻+冬 with heng_pie hook → A). The strict "straight-stroke only"
   rule from B8 is really "no hook-compound at large canvas-spanning
   scale needing per-endpoint width".

3. **疒-family cluster is a structural bank gap** (not P-A-007 miss):
   all 4 疒-family FAILs consistently inline the 5-stroke decomposition;
   the inline recipe does NOT cohere calligraphically. Do NOT retry
   until a Phase-3 char with 疒 sub-component organically PASSes;
   THEN promote its inline as nao_sickness.py. Consistent with
   P-COMP-008 refutation of hand-crafting missing primitives.

---

## B11 (2026-08-09, position 618) — 19 mains-FAIL + 3 C + 4 R1 FAIL

### Cluster A: 疒-family bank gap (terminal-freeze, 1)

**p3_char_0384_疡** (FAIL) — 5-stroke 疒 inline (dian + heng +
long_pie + 2 short interior ti/dian). Docstring explicitly notes
B10 terminal-freeze declaration; drawer inlined anyway. Same failure
mode as B10 疙/疟/疠/疝: the 5-stroke inline does not cohere
calligraphically as 疒. **Action**: terminal-freeze per B10
declaration. Do NOT queue.

### Cluster B: 亻+X hook-compound or 3-part (mixed, 5)

**p3_char_0408_佾** (FAIL) — 亻+八+月 (3 sub-components, 8 strokes).
Drawer CALLED ren_left correctly; BANK_DEVIATIONed ba (aspect
0.50/0.64 = 0.78 nominally in-window, but per-stroke chord check
showed uniform-scale infeasible) and yue_moon (0.48/0.66 = 0.73
nominally in-window, per-axis scale conflict). Inlined pie+na for
八, pie+heng_zhe_gou+2 heng for 月. FAIL on inter-component
spacing. **Action**: P-A-010 kind (e) — multi-DEVIATION correct-math
composition-level. Do-not-queue.

**p3_char_0410_侃** (FAIL) — 亻+idiosyncratic-right (冂+二+儿-ish,
8 strokes). Drawer BANK_DEVIATIONed ren_left on position (>60 px
shift). No whole-radical for the right side (冂+二+儿 combo).
Inlined all 8 strokes. Right side fragmented. **Action**: do-not-queue
(no bank + no recipe).

**p3_char_0416_侉** (FAIL) — 亻+夸=大+亏. Drawer CALLED ren_left
correctly; BANK_DEVIATIONed da_big (aspect 114/240 = 0.48 <
lower bound 0.55). Inlined 大 top + 亏 bottom (no bank for 亏).
FAIL on stacked-compression + hook-compound (亏's shu_wan-tail).
**Action**: P-COMP-011/012 hook-compound + do-not-queue.

**p3_char_0420_侌** (FAIL) — 今+云 stacked (8 strokes). Drawer
BANK_DEVIATIONed hui_meet and he_together on stroke-count/inner-
composition mismatch. Inlined 今 (pie+na+dian+hook-diagonal) +
云 (2 hengs + pie_zhe + dian). FAIL on 今 s4 diagonal (novel
compound-stroke). **Action**: do-not-queue.

**p3_char_0426_侔** (FAIL) — 亻+牟 (亻+厶-top+牛-body, 8 strokes).
Drawer CALLED both ren_left AND niu_cow per P-A-007-v2 with
quantitative math (scale=1.0 for 亻, scale=0.72 for 牛); inlined 厶
top (2 strokes, no bank). Bank primitives rendered; FAIL on 厶-top
positioning between 亻 and 牛. **Action**: **B12 R1 MEDIUM** —
P-A-010 kind (b) trajectory-diff on 厶-top spacing; explicit
instruction to place 厶 with wider gap from 亻 and centered above 牛.

### Cluster C: L-R with no bank for either half (mostly do-not-queue, 5)

**p3_char_0401_取** (FAIL) — 耳+又 (8 strokes). No 耳 whole-radical.
BANK_DEVIATIONed you_again on aspect non-uniform (0.68 vs 0.77 x/y
scales). Inlined耳 (6 strokes) + 又 (2 strokes). **Action**:
do-not-queue (耳 chronic bank gap; no P-A-010 route).

**p3_char_0407_规** (FAIL) — 夫+见 (8 strokes). No 夫, no 见.
Inlined 8 strokes. FAIL on X-cross of 夫 + hook of 见 without
per-endpoint width. **Action**: do-not-queue (double bank gap;
format-ceiling on hook).

**p3_char_0388_亟** (FAIL) — Unique layout (top-diagonal + 口
+ 又-cluster). BANK_DEVIATIONed kou_mouth and you_again on
scale <0.4 (both below 0.55 lower bound). Inlined 8 strokes.
**Action**: do-not-queue (unique layout; no decomposition).

**p3_char_0415_转** (FAIL) — 车-radical+专 (8 strokes). No 专;
车 compressed to 0.44 aspect (below 0.55 window). Inlined per
MMH. FAIL on both halves. **Action**: do-not-queue (车-left
compression chronic; wait for organic PASS).

**p3_char_0418_例** (FAIL) — 亻+歹+刂 (3-part, 8 strokes). Drawer
BANK_DEVIATIONed ren_left on anisotropic aspect (79% x-compression)
AND had dao_right note ("bank uses gap 50px vs target 40px").
Inlined all 8 strokes. **Action**: **B12 R1 MEDIUM** — P-A-010
kind (a): P-A-007 quantitative recheck says the 79% aspect is
inside [0.55, 1.2] and drawer's "anisotropic 16 px miss" concern
is exactly what P-A-007-v2 says to accept (uniform-scale is fine
if aspect ratio in window). CALL ren_left AND dao_right per queue
instruction.

### Cluster D: Top-radical aspect-mismatch queueable (B12 R1, 3)

**p3_char_0393_实** (FAIL) — 宀+头 (8 strokes). Drawer
BANK_DEVIATIONed mian_roof on aspect 1.45 vs bank 2.43 = ratio
0.60 < lower bound 0.55. Inlined 3-stroke 宀 + 5-stroke 头.
**Recheck**: 0.60 is JUST below the 0.55 lower bound; the
current drawer_memory ding_fix template for 宀-top uses similar
aspect (see B10 ding_fix promotion). **Action**: **B12 R1 HIGH** —
P-A-010 kind (a): call mian_roof per B10 ding_fix template
precedent (which PASSed at similar aspect). If mian_roof rendering
extends beyond target box, use scale=0.85 not 1.0.

**p3_char_0405_治** (FAIL) — 氵+台 (8 strokes). Drawer CALLED
sanshui correctly (aspect 0.87, in-window) + inlined 厶 top +
BANK_DEVIATIONed kou_mouth (aspect 1.42 vs bank 0.87 = 1.63,
out-of-window). Kou_mouth genuinely doesn't fit (aspect skew is
real). Trajectory-diff route: **B12 R1 MEDIUM** — P-A-010 kind (b):
tune kou_mouth call by passing per-stroke width override so bottom
heng stretches wider than sides (achieves the flat-口 aspect
without inline).

**p3_char_0403_放** (FAIL) — 方+攵 (8 strokes). Drawer inlined 方
(no 方 primitive) + BANK_DEVIATIONed pu_action (aspect 0.91 vs
0.67 = 36% dev, out-of-window). Inlined 攵 too. **Action**:
**B12 R1 MEDIUM** — P-A-010 kind (b): tune pu_action call at
scale ~0.72 (matches vertical scale 1.06) and accept horizontal
compression 0.78; or accept inline attempt as ceiling.

### Cluster E: L-R complex hook-compound (do-not-queue, 3)

**p3_char_0429_是** (FAIL) — 日+龰 (8 strokes). Drawer
BANK_DEVIATIONed ri_sun (aspect 1.13 vs 0.62 = 1.82, out-of-
window) AND zheng_correct (structural mismatch pi vs zheng).
Inlined all 8. FAIL is format-ceiling: G5 uniform PIL line
can't render calligraphic squat 日 that G4's per-endpoint fat_line
achieves (G4 got A). **Action**: do-not-queue (format ceiling).

**p3_char_0431_说** (FAIL, 9 strokes) — 讠+兑. Drawer CALLED
yan_speech at (ox=-30, oy=-5, scale=0.85); BANK_DEVIATIONed ba
and kou_mouth on 兑's compressed sub-components. Multi-DEVIATION.
**Action**: P-A-010 kind (e) — do-not-queue.

**p3_char_0427_线** (FAIL) — 纟+戋 (8 strokes). No 纟 whole-
radical; BANK_DEVIATIONed ge (戈) on aspect 0.66 vs 0.91 = 30%
dev. Inlined all 8 strokes. Multi-inline. **Action**: do-not-queue.

### Cluster F: 亞/traditional/覀 (do-not-queue, 2)

**p3_char_0386_亞** (FAIL) — Traditional 亞 (8 strokes). Drawer
BANK_DEVIATIONed ya_asia (6 strokes) on stroke-count mismatch
(6 vs 8). Inlined all 8 per P-A-006. **Action**: do-not-queue
(no traditional-8-stroke bank primitive; wait for organic PASS).

**p3_char_0433_要** (FAIL, 9 strokes) — 覀+女. Drawer CALLED
nu_woman + heng_zhe_wide + hengs + shus. 覀 top (6 strokes)
inlined; s3 heng_zhe_wide didn't cohere as right-post. **Action**:
do-not-queue (覀-top chronic; no bank).

### Cluster G: 3 C's (do-not-queue, 3)

**p3_char_0391_表** (C), **p3_char_0396_佴** (C), **p3_char_0402_佻** (C).
Standard P-COMP-006 — no mechanism-change available at R1. Skipped.

### B11 R1 outcomes (all 4 FAILed — P-A-010 discovery)

**p3_char_0341_社__retry_1** (FAIL) — Drawer CALLED shi_spirit
+ tu_earth per B10 queue instruction with quantitative math
(0.741 and 0.792 in-window). Both bank primitives rendered
cleanly. **FAIL mode**: L-R spacing between 礻 and 土 was
never bank-authored (each primitive positioned via ox/oy but the
inter-primitive gap was drawer-guessed at ~30 px). Bank primitives
correct in isolation but the composition never welded.
**Terminal-freeze** per 2-round no-PASS rule. Retrospect: this is
P-A-010 kind (d) — L-R spacing between 2 whole-radical primitives.

**p3_char_0346_佞__retry_1** (FAIL) — Drawer CALLED ren_left +
er_two + nu_woman per B10 queue instruction. 3-part vertical
composition (亻 | 二/女) with two horizontal-splits. Bank
primitives rendered correctly but the 二 sat too low relative to
女 (drawer used ox based on lower heng anchor). FAIL on inter-
primitive spacing. **Terminal-freeze**. P-A-010 kind (d).

**p3_char_0366_畅__retry_1** (FAIL) — Drawer tried "extend you_by
s5 shu to represent 申's top-extension" per B10 queue trajectory-
diff instruction. But then abandoned the bank-adaptation and
inlined 申 box + shu fresh (with ignore-MMH strategy) + inline 勿-
sweep. FAIL on both halves' proportions. **Terminal-freeze**.
P-A-010 kind (e) — trajectory-diff on the wrong primitive was the
queue instruction's flaw.

**p3_char_0375_经__retry_1** (FAIL) — Drawer BANK_DEVIATIONed you_again
+ tu_earth with quantitative math confirming DEVIATION was justified
(0.69 vs 0.95 for 又; 1.45 for 土 bottom heng); inlined right half
with angle/width tuning. Trajectory-diff addressed component quality;
composition still didn't cohere. **Terminal-freeze**. P-A-010
kind (e) — multi-DEVIATION correct-math composition-level.

### B11 postmortem summary

1. **P-A-010 discovered from 0/4 R1 outcome** — R1 mechanism-change
   taxonomy limits queueing to kinds (a)/(b)/(c). Kinds (d)/(e) are
   do-not-queue: inter-primitive spacing / multi-DEVIATION correct-
   math composition problems don't have a primitive-call R1 rescue.
2. **G4-vs-G5 CORRECTED** — the pre-batch note "G5 beats G4 on both"
   was wrong. Actual B11 labels: G4 62%/17A > G5 56%/9A > G3 28%/0A.
   Two-factor decomposition from B8 still holds.
3. **9 A discipline crystallization compounds** — monotonic-up
   B8/B9/B10/B11 = 0/4/7/9. Not a format-absolute ceiling; discipline
   lever (P-A-006 through P-A-009 in the drawer's docstring self-check)
   consistently produces the recipe.

---

## B12 (2026-08-09) — 23 FAILs + 4 C's (main-channel only; R1 outcomes below)

### Cluster A: 疒-family bank gap (5 FAILs, terminal-freeze per B10 declaration)

**p3_char_0446_疤** (FAIL, 9 strokes) — 疒+巴. Drawer BANK_DEVIATIONed both 疒 (family terminal-freeze) and 巴 (no bank). Inline both. Same 5-stroke 疒 decomposition (2 dians + heng + long pie + ti) fails to cohere visually. **Action**: terminal-freeze (9 cumulative 疒 FAILs, do-not-queue).

**p3_char_0450_疫**, **p3_char_0452_疬**, **p3_char_0454_疭**, **p3_char_0456_疮** — same 疒-inline decomposition, same FAIL mode. **Action**: all terminal-freeze.

### Cluster B: 亻+X hook-compound (6 FAILs, mixed queueable/frozen)

**p3_char_0464_侯** (FAIL, 9 strokes) — 亻+矦-like right (7). Drawer BANK_DEVIATIONed ren_left with quant math: pie shift Δx=-72.7px, shu shift Δx=-65.4px, differential 7.3px. Cited "non-uniform shift → single (ox,oy,scale) cannot preserve MMH+joint". **Retrospect**: 7.3px differential is well inside P-A-007-v2's ~15px tolerance for uniform-scale. This is a systematic P-A-007-v2 refusal pattern. **Action**: B13 R1 HIGH kind-(a) — force CALL ren_left at ox≈-73, oy≈-8, scale≈0.94.

**p3_char_0469_便** (FAIL, 9 strokes) — 亻+更. Same ren_left BANK_DEVIATION pattern (main cited "systematic left-shift of ~74 px"). Multi-DEVIATION also on 日 (nestled). **Action**: B13 R1 HIGH kind-(a).

**p3_char_0480_俊** (FAIL, 9 strokes) — 亻+夋. Likely same ren_left DEVIATION pattern. **Action**: B13 R1 MEDIUM kind-(a).

**p3_char_0472_侷** (FAIL) — 亻+局. 局 has heng_zhe_gou hook — P-COMP-012 chronic. **Action**: do-not-queue.

**p3_char_0474_係** (FAIL) — 亻+系. No 系 whole-radical bank; complex inner (幺+小). **Action**: do-not-queue kind-(e).

**p3_char_0478_俉** (FAIL) — 亻+吾 = 亻+五+口. Multi-DEVIATION: ren_left (systematic-shift excuse) AND kou_mouth (2.08 vs 0.67 aspect = genuine out-of-window). **Action**: do-not-queue kind-(e).

### Cluster C: 3-part composition / L-R with bank-mismatch (5 FAILs, do-not-queue kind d/e)

**p3_char_0461_亲** (FAIL, 9 strokes) — 立-top + 木-like bottom. Drawer BANK_DEVIATIONed li_stand (non-uniform 0.62 vertical vs 0.88 horizontal) AND mu_wood (shu descends from above rather than piercing midway). Kind (e) multi-DEVIATION. **Action**: do-not-queue.

**p3_char_0473_城** (FAIL, 9 strokes) — 土-left (with 提 terminal) + 成. Drawer BANK_DEVIATIONed tu_earth (bank has flat heng; target has ti) AND cheng_become (bank standalone anchors differ). Kind (b1) potential for tu-with-ti swap, but it's a stroke-CLASS change not a parameter change. **Action**: B13 R1 LOW kind-(b1); skip if budget tight.

**p3_char_0467_结** (FAIL, 9 strokes) — 纟+吉. No 纟 whole-radical bank. Multi-inline. **Action**: do-not-queue kind-(e).

**p3_char_0453_度** (FAIL, 9 strokes) — 广+廿+又. Drawer BANK_DEVIATIONed guang_wide (vertical span 246 vs native 178 = 1.38× stretch, genuine out-of-window) AND you_again (compressed 又). Kind (e). **Action**: do-not-queue.

**p3_char_0481_济** (FAIL, 9 strokes) — 氵+齐. sanshui called, but 齐 has no bank + interior 廾-like sub. **Action**: do-not-queue kind-(d).

### Cluster D: Novel / unique / traditional (6 FAILs, do-not-queue)

**p3_char_0438_畐** (FAIL) — 一 + 口 + 田 stacked, no whole-radical for 畐. Composition irregular.

**p3_char_0442_乹** (FAIL) — 乾-family traditional variant. No decomposition.

**p3_char_0439_将** (FAIL) — 爿+夕+寸, 3-radical L-R, no 爿 bank. Drawer inlined all 9; L-R spacing failed.

**p3_char_0440_畑** (FAIL) — 火+田 (Japanese kokuji). No 火-left, no 田 whole-radical primitives. **Note**: could be kind-(a) if 田 primitive existed; currently do-not-queue.

**p3_char_0458_癸** (FAIL) — 癶-top + 天-like bottom. Unique composition, no bank support.

**p3_char_0459_带** (FAIL) — Unique 带-top (3 shus + heng + 巾) + 巾 bottom. No support.

**p3_char_0460_皅** (FAIL) — 白+巴. 巴 has hook-compound; 白 has bank primitive (bai_white). 白 called + 巴 inlined; 巴's hook rendering failed. **Action**: do-not-queue P-COMP-012 boundary.

### 4 C-verdicts (no retries queued per P-COMP-006)

**p3_char_0436_畏** (C), **p3_char_0437_种** (C), **p3_char_0441_前** (C), **p3_char_0462_皈** (C). Standard P-COMP-006 — no mechanism-change available.

### B12 R1 outcomes (3/5 = 60% recovery — P-A-010 validated)

**p3_char_0393_实__retry_1** (A) — mian_roof called at scale=0.85 per queue kind-(a) instruction. Bottom 头 inlined. **P-A-010 kind (a) VALIDATED**: primitive-skipped-with-borderline-aspect (0.60) rescues at R1.

**p3_char_0405_治__retry_1** (PASS) — kind (b1) parameter-tune: main FAIL had open-bottom 口 (box bottom_right=y=261 while shu descended to y=296). R1 inlined wide-flat 口 as shu+heng_zhe_box+heng with box aligned to y=296. **P-A-010 kind (b1) VALIDATED**: single-primitive parameter fix rescues.

**p3_char_0403_放__retry_1** (PASS) — kind (b1) with mixed rescue. Fixed 3 stroke-level details for 方 (dian too high, pie floating), switched 攵 to pu_action bank call at scale=0.85 per kind-(a) portion. Mixed-strategy PASSed.

**p3_char_0418_例__retry_1** (C) — kind (a) partial rescue: called ren_left + dao_right per instruction; 歹-middle inline still noisy. **New sub-observation**: 3-radical L-R with kind-(a) fixes for 2 of 3 sub-components → C-ceiling not PASS. Boundary case. **Action**: terminal-freeze (2-round no PASS).

**p3_char_0426_侔__retry_1** (FAIL) — kind (b) MISCLASSIFIED as kind (d). Queue instruction "trajectory-diff on 厶-top placement between 亻 and 牛" is INTER-PRIMITIVE SPACING = kind (d) in disguise. Same failure mode as B11 社/佞. **Action**: terminal-freeze; sharpens P-A-010-v2.

### B12 postmortem summary

1. **10 A verdicts (new G5 ceiling)** — monotonic-up B8-B12 = 0/4/7/9/10.
   Two archetypes: DEVIATION-heavy inline (7/10) + bank-template-stack (3/10).
2. **3 SOLO A wins** (面/神/俅) validate discipline lever independent of pool.
3. **First LEGITIMATE G5>G4 batch on aligned idx** (46% vs 40% PASS,
   10 vs 8 A). Three-factor mechanism: 50% discipline + 30% bank-critical-mass +
   20% pool-favorability. NOT stable win; expect pool-dependent going forward.
4. **P-A-010-v2 sharpened**: kind (b1) vs (d) distinction — "trajectory-diff on
   inter-primitive spacing" is kind (d), not (b). Kind (a) has boundary case
   for 3-radical L-R (C-ceiling with 2-of-3 fixes). Mechanical decision
   procedure: "what single object gets changed?"
5. **疒-family terminal-freeze REAFFIRMED** — 9 cumulative FAILs. Bank push
   REJECTED per P-COMP-008 refutation precedent.
