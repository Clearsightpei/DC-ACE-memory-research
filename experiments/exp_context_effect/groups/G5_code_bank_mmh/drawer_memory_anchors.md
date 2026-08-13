# G5 drawer memory — MMH anchor calibration notes

*Extracted from drawer_memory.md at B9 split (2026-08-09, position 518).*
*Content: cases where MMH endpoints disagreed with GT silhouette and*
*which override strategy won. Consult when your MMH block anchors*
*don't match the GT visually.*

---

## MMH anchor calibration notes

Cases where MMH endpoints disagreed with GT silhouette and which won:

- **丿 (p2_radical_003, C+R1 FAIL)**: MMH head at TL(0.627, 0.794) → px (63, 79). GT silhouette actually places the visible centroid near x=145. Two retries with head at (90, 82) and (112, 80) both failed — the correct override is ~(140, 90), an ~80 px right-shift from MMH. Lesson: for MMH-underconstrained single-stroke radicals, override MMH by whatever distance the visible GT centroid demands, even if that means a > 40 px anchor shift.

- **力 (p2_radical_025, PASS via override)**: MMH s1 head at ML(0.668, 0.474) = (66.8, 147.4). Drawer overrode to (95, 105) to match GT horizontal start. Worked. Lesson: MMH medians for compound strokes (like 横折钩) often describe the median LINE, not the ENDPOINTS — override toward the visible corner.

- **艹 (p2_radical_039, PASS via override)**: MMH gave verticals only 65-80 px tall; GT shows ~130 px. Drawer extended heads up and tails down while keeping the MMH cross-points (32%/66% along heng) as pierce anchors. Lesson: MMH sometimes gives only the medial section; visible ink can extend past both endpoints.

- **山 (p2_radical_063, PASS via override)**: MMH placed the three verticals wider than the visible GT. Drawer compressed x-spread from (57/138/237) to (95/150/203). Lesson: for radicals with 3+ near-vertical strokes, MMH's x-spread often over-runs the visible ink; compress inward.

- **氵 (p2_radical_069, PASS clean)**: MMH ti tail y-frac=0.944 puts s3 tail at y=294. Drawer used it verbatim and PASSed — for ti (rising stroke), MMH endpoints are trustworthy end-to-end.

- **囗 (p2_radical_073, PASS clean)**: 囗 MMH anchors DIFFER from 口's — 囗 spans nearly full canvas (~65,79 to ~230,296) while 口 sits compact (~100,128 to ~225,258). Drawer inlined the stroke primitives directly rather than calling draw_kou. Lesson: don't force a bank whole-radical primitive when MMH-anchor spread differs from the primitive's baked-in geometry — inline from stroke bank instead. This is a case where composing from stroke primitives beat calling a plausibly-relevant radical primitive.

- **114_日 vs 057_口 (composition)**: 日 has 4 strokes (shu + heng_zhe_box + heng + heng), 口 has 3. Drawer did NOT call draw_kou for 日 — instead composed from stroke primitives. Same lesson as 囗: MMH stroke count is the truth.

- **兀 (p2_radical_074, FAIL)**: The right leg is 竖弯 (no upward hook), NOT 竖弯钩. Drawer knew this and inlined; still FAILed. Cause likely proportion/aspect rather than stroke choice. Note for B3: consider a bank `shu_wan_bare.py` primitive if 元/兀/... family reappears in Phase-3 characters.

- **气 (p2_radical_111, FAIL)**: 4th stroke is 横斜钩 (horizontal, then diagonal down-right, then small upward hook). No bank primitive covers this exact shape. Drawer's inline attempt FAILed. Note for B3: `heng_xie_gou.py` promotion candidate if a retry produces a PASS.

- **风 (p2_radical_094, FAIL)**: Stroke 2 is 横斜弯钩 — a single fluid arc across-and-down-and-around, not a rigid heng_zhe_gou. Same class as 气 s4 morphologically. Both terminal-freeze candidates without additional bank support.

### B3-era anchor calibration

- **月 (p2_radical_130, PASS)**: MMH s1 tail was (42.5, 295) — overshoots visible GT (ends ~y=265). Drawer overrode to (52.0, 268.0). Same P-MMH-002 pattern: MMH gives medial section, not always the visible endpoint.

- **宀 (p2_radical_060__retry_2, PASS)**: Successful recipe = call `draw_mi_cover` (冖) for left-dian + roof combined (they must ALIGN), then add top dian separately. Retry_1 FAILed because it drew the two dians and roof independently — they didn't visually cohere as one 宀 silhouette. Lesson: **composed primitives that share an alignment constraint should be called through a single wrapper, not summed from independent pieces**.

- **门 (p2_radical_059__retry_2, PASS)**: Successful recipe = keep the top-left dian small and offset from the frame corner, use draw_shu(width=5) for the left post (thin, not thick), use draw_heng_zhe_gou explicitly for the right frame with waypoints (heng_head=(128,92), corner=(215,92), gou_tail=(202,265), hook_tip=(182,252)). Retry_1 was C because dot was blobby; retry_2 fixed with slimmer parameters.

- **爻 (p2_radical_128, A verdict)**: 4-stroke stacked-X composition. MMH anchors used verbatim. Key A-recipe elements: (a) differentiated bow_perp per stroke (-14, -8, -18, -10) so top X and bottom X have visually distinct proportions; (b) explicit taper per stroke (w_head != w_tail); (c) steps=90 for top, steps=100 for larger bottom strokes.

- **了 (p3_char_0009, A verdict)**: BANK_DEVIATION with meticulous 3-bezier inline crafting. Fresh_component `wan_gou_for_了` promoted to `wan_gou.py`. Key A-recipe elements: (a) 横撇 s1 rendered as heng-arc + short pie-fold at the corner (not a single sweep); (b) 弯钩 s2 as cubic bezier bowing right through belly, terminating with quadratic-bezier hook flick LEFT and up; (c) explicit stamp-taper on all segments.

- **人 & 又 (p3_char_0011 & 0017, A verdicts)**: Both identity-call bank primitives (draw_ren, draw_you) with MMH anchors matching bootstrap/B1 anchors verbatim. Zero deviation. **A-recipe conclusion**: when a Phase-3 char is literally the same as a PASSed Phase-2 radical, direct bank reuse can produce A quality, not just PASS. This is the strongest evidence yet for P-RET-002.

### B4-era anchor calibration

- **礻 R2 PASS (p2_radical_116)**: Successful recipe = crossbar (heng_pie) at mid-band y~148 (not upper-third), central shu head at y~193 well BELOW crossbar with a proper ~40px N-gap, right dian moderate size (~80px extent, not >130). Retry_1 FAIL modes: crossbar too high, shu welded into crossbar, right dian bloated.
- **长 R2 PASS (p2_radical_088)**: Successful recipe = SLIM strokes (~7-8px, not 15), long wide horizontal, explicit 竖提 polyline with rising up-right flick at bottom, na starts inside the vertical. Both prior attempts had a "starburst" appearance from over-thick strokes clustering near center.
- **韦 R1 PASS (p2_radical_123)**: Successful recipe = top_curl=True on the central shu (adds calligraphic entry tick), inline bottom-hook compound (wider-than-heng_zhe_gou with deeper descending curl + explicit back-left hook flick), steeper heng slant (~15px lift over 130px run).
- **毋 R1 PASS (p2_radical_125)**: Successful recipe = prominent rising tail on s1 extending to (275,195), softened top-right corner (no hard 90°), mild leftward bow on s3 pie, explicit leftward hook waypoint on s2 at (150,265). Uses inline polyline (not a bank compound).
- **尣 R1 PASS (p2_radical_121)**: Successful recipe = bump w_head on long pie (10 vs 9), reduce bow_perp to 16 (from 20), broader shu_wan_gou shelf with knee_ratio=0.55 and bottom_extra=58.
- **B4 identity-reuse Phase-3 chars (勹/匕/大/山/口/干/门/宀/女/艹/小)**: All 11 called their bank primitive at (ox=0, oy=0, scale=1.0) and PASSed cleanly. NONE lifted to A this batch (B3 pattern didn't replicate for 3+ stroke items — see A-recipe playbook update above).

### B4 FAIL calibration notes

- **也 (p3_char_0047)**: 3 strokes (heng + shu + shu_wan_gou). All 3 bank primitives used. FAIL likely because the shu_wan_gou's wrap extends too far right of the shu's midpoint; the standard `shu_wan_gou` defaults are tuned for 匕/儿 which have a much shorter horizontal reach. Retry hint: increase bottom_extra to 75+ and pull knee_ratio down to 0.62 for a longer/flatter bottom sweep before hook.
- **卂 (p3_char_0060)**: 3 strokes (xie_gou + heng + shu). Bank primitives used. FAIL likely due to composition — the xie_gou's diagonal descent visually collides with the shu; drawers should offset the shu slightly right of MMH C anchor to prevent collision, or reduce the xie_gou's terminal hook flick.
- **与 (p3_char_0061)**: 3 strokes (heng + heng_zhe_gou + heng). All bank primitives. FAIL because heng_zhe_gou spans the FULL height (top-to-bottom) — the drawer used default heng_zhe_gou which is tuned for 力's compact size. Retry hint: pass explicit `heng_head` at TC top, `gou_tail` near BC bottom (much taller than default).
- **刁 (p3_char_0034)**: 2 strokes. Same shu_wan_gou-vs-wan_gou tuning problem as 也. Retry hint: use wan_gou with belly_right bumped to 40+ and hook_up 25+ for the taller/deeper vertical.
- **丸 (p3_char_0044)**: Same missing heng_zhe_wan_gou primitive as 几/九/瓦/风/凡. Sandbox spec still applies; no PASS from B4 R1 attempts to promote from.
- **子 (R2 C)**: Persistent 3-stroke child character; the sandbox wan_gou tuning helps for 孑/孓 (both PASSed B4) but not 子 (needs the top heng-pie longer than the sibling forms). Terminal-freeze candidate.
- **飞 (p3_char_0073)**: Idiosyncratic 3-stroke. BANK_DEVIATION named fresh_components fei_top_zhe, fei_main_swoop, fei_inner_ti. FAIL — the main swoop is too unique to reuse. Sandbox candidate: `heng_xie_wan_gou.py` if a B5 attempt PASSes.
- **夂 vs 夊 (both FAIL)**: 3-stroke bottom-X clusters. draw_pu-style skeleton doesn't fit (draw_pu is 4-stroke). Terminal-freeze candidates.

### B5-era sibling notes (2026-08-08)

- **内 vs 內** (B5, sibling error caused 內 FAIL): both are 4-stroke box+inner. **内** (Simplified) has inner 入-style (pie's tail lower than na, na wraps up). **內** (Traditional) has inner 人-style (pie shorter, na longer sweep). Reference GT strictly — do NOT copy the sibling's inner render.
- **马 vs 乌** (B5): 乌 = 马 + top pie (extra s1). Both fail on missing heng_zhe_wan_gou for main body (s2 for 马, s3 for 乌). Same retry template applies.
- **仇 vs 仉 vs 亢** (B5): all 亻/亠+bottom-right compound. 仇 = 亻+九; 仉 = 亻+几; 亢 = 亠+儿-style. First two need heng_zhe_wan_gou; 亢 needs shu_wan_gou with bottom_extra tuning (wider wrap than 匕/儿 default).
- **冗 vs 冘** (B5): 冗 = 冖+几 (4 strokes, needs heng_zhe_wan_gou for bottom). 冘 = 冖+人 (top is 冖, bottom is 人 — no hook compound needed). Distinguishing: bottom is a hook or a leg?
- **心 (PASS via wo_gou)**: Confirmed template = 3 dians (left/middle/right) + 卧钩 as s2. Now callable via `draw_wo_gou`. Reuse targets: 必 (add pie), 忘 (亡 on top), 忙 (忄 on left), 志 (士 on top), 思 (田 on top), 念 (今 on top), 忽 (勿 on top), 恕 (如 on top). All will need wo_gou now that it's promoted.
- **五 (PASS via heng_zhe_wide)**: Confirmed template = heng + pie + heng_zhe_wide + heng. Distinct from 乙/五-family which use different turns. Reuse targets: 亚, 世 (S-turn family — different compound), 巫.

### B5-era anchor calibration

- **心 (p3_char_0112, PASS)**: 卧钩 belly reaches y=260 for a canvas
  where head y=161, tail y=185 — a very deep dip (~75px below the
  tail's y). The default `belly_y = max(hy, ty) + 60` computes 245 for
  this case; pass belly_y=260 explicitly for a deeper 心-style dip.
  Hook flick: hook_up=26, hook_back=6 (small).
- **五 (p3_char_0122, PASS)**: heng_zhe_wide s3 head at ML(80,173),
  corner at (172,171), tail at (173,248). The near-square corner
  wants a visible 顿笔 dab (corner_dab=6). Both segments width=8.
- **文/日/中/工 identity-calls (B5 PASSes, ALL NOT-A)**: confirmed
  P-A-004: identity-calling `draw_wen`, `draw_ri`, `draw_gong_work`,
  or `draw_kou` variants for chars 文/日/工/中 delivers PASS but not
  A at 4-stroke complexity. If future batches include 1-2 stroke items
  identity-callable to a mastered radical, expect A per P-A-001.
- **B5 FAIL calibration (hook-family)**:
  - **马/乌/仇/仉/冗**: all inlined DEVIATIONs for heng_zhe_wan_gou.
    All FAILed. Sandbox now carries a *candidate spec* — copy into B6
    retry attempts verbatim; PASS promotes the primitive to bank.
  - **予**: heng_pie primitive too wide for 予's compact top. B6 retry:
    inline heng_pie with apex_x offset 40-50 from head, bow_perp=25
    (steeper), narrower horizontal segment.
  - **以**: right-人 asymmetric. Pie tail at BC(115.7, 269.5), na apex
    inside BR cell only (not spilling into MR).
  - **亢**: shu_wan_gou needs bottom_extra=80+, knee_ratio=0.65 for the
    wide 儿-style bottom (per P-RET-004).
  - **见**: box scale-up (larger than bank default). Wide-N joint
    between s3.mid and s4.head (~54 px vs expected ~20). Both are
    dispatched by MMH — render the wide gap faithfully.
  - **兮**: wan_gou shaft is only ~109 px (short). Pass belly_right=15
    (smaller than default 27), hook_len=20 (smaller than default 26).
  - **內**: inner 人-style (pie shorter than na); do NOT use the 内
    (Simplified) inner-入 template.

### B6-era sibling notes (2026-08-08)

- **义 vs 又 vs 乂** (all 3-stroke crossing): 义 = dian(TL) + pie + na
  (3 strokes). 又 = heng_pie + na (2 strokes). 乂 = pie + na (2 strokes).
  Distinguishing: is there a top-left dot? (义 yes, 又/乂 no.)
- **元 vs 无** (both 4-stroke top-heng + bottom-hook): 元's pie STARTS at
  s2 mid-level, doesn't cross above top heng. 无's pie crosses the top
  heng (starts higher). Sibling-pair distinguishing = pie's top y.
- **化 vs 花 vs 华**: 化 = 亻+匕 (4 strokes). Add 艹 on top → 花 (7 strokes).
  Add ⺊ radicals → 华 variants. Bank now has draw_hua; caller for 花 can
  compose draw_cao (top) + draw_hua (bottom).
- **反 vs 板 vs 饭 vs 版**: 反 stands alone (4 strokes). L-R prefix
  radicals (木/饣/片) + draw_fan (compressed to right-column) = board/meal/
  edition. Use draw_fan(ox=+30, scale=0.75) as starting point.
- **主 vs 王**: 主 = dian on top + 王-triple-heng-lowered + shu. The 王
  inside 主 sits LOWER than standalone 王 (top heng y~130 vs standalone
  y~95). draw_zhu bakes this offset; draw_wang_king is for standalone 王
  and the older 王-tops (王/玉).
- **正 vs 止 vs 之**: 正 = top-heng + 止 (5 strokes). 止 alone is 4 strokes
  (draw_zhi_stop from B3). 之 has a wave shape at bottom (draw_zhi_this
  from B4). Do NOT confuse.
- **生 vs 龶**: 龶 = heng + heng + heng + shu (4 strokes). 生 = pie + heng
  + heng + shu + heng (5 strokes; extra top pie). draw_sheng adds the
  pie; identity-call for 龶 stays as inline.
- **平 vs 半 vs 干 vs 于**: all similar 5-stroke/6-stroke shapes. 平 has
  BOTH left-dian AND right-pie on top of the middle beam. 半 has 丷 on
  top. 干 has TWO hengs. 于 has bottom-hook. draw_ping distinguishes by
  having exactly one dian + one pie top.
- **他 vs 化** (both 亻+X L-R): 化's right side 匕 is 2-stroke calligraphic;
  他's right side 也 is 3-stroke with heng_zhe_wan_gou top arc. NOT
  interchangeable; 也 needs a compound bank primitive we still lack.
- **引 vs 弘 vs 张**: 引 = 弓+丨 (4 strokes). 弘 = 弓+厶 (5 strokes). 张
  = 弓+长 (7 strokes; use draw_chang_long from B4 for right side). Bank
  has NO 弓 primitive (bare 弓 was terminal-frozen in B3). Any 弓-prefix
  char is a candidate for FAIL until we get a 弓 primitive.

### B6-era anchor calibration

- **义 R1 A (p3_char_0089__retry_1)** — P-A-005 template:
  * dian: MMH ML(0.976, 0.099)→(98, 110) head, C(0.321, 0.38)→(132, 138)
    tail. `w_head=3, w_tail=9, bow=3`.
  * pie: MMH C(0.723, 0.017)→(172, 102) head, BL(0.416, 0.842)→(42, 284)
    tail. **`bow_perp=-45` (NEGATIVE)** to push mid-belly DOWN-RIGHT
    toward BC crossing anchor. `w_head=10, w_tail=3`.
  * na: MMH ML(0.712, 0.635)→(71, 164) head, BR(0.780, 0.912)→(278, 291)
    tail. `bow_perp=+20, w_head=4, w_tail=12`. Strong tail-thickening.
  * Result: welded X at BC(~145, 233). A verdict.
- **化 (p3_char_0134, PASS)** — L-R shrink recipe: `draw_ren_left(ox=-40,
  oy=+15, scale=0.75)` + `draw_bi(ox=+100, oy=+40, scale=0.65)`. This is
  the STARTING template for any 亻+X 4-stroke L-R char.
- **反 (p3_char_0140, PASS)** — 4-stroke inline (no whole-又 because interior
  crossings must weld). Key: heng_pie apex_x=170, corner_x=175 for the
  interior compound; na bow_perp=14; both s3.mid + s4.mid weld at BC.
- **元 (p3_char_0152, PASS)** — 4 strokes: top-heng SHORT (99→189, y~90);
  middle-heng LONGER (52→220, y~155); pie starts at MIDDLE heng level
  (99, 173) descending BL(33, 282); shu_wan_gou (144, 159)→(267, 222)
  with `bottom_extra=52, knee_ratio=0.72`. Do NOT let pie start above
  the top heng — that's 无, not 元.
- **主 (p3_char_0174, PASS)** — 5 strokes: dian at (131, 61)→(168, 92);
  王-triple-heng shifted DOWN so top heng y~130 (not the standalone 王's
  y~95); central shu (141, 145)→(144, 266); bottom heng y~278. Skips
  draw_wang_king in favor of inline 王 (BANK_DEVIATION).
- **正 (p3_char_0182, PASS)** — 5 strokes: top heng (55, 84)→(232, 76)
  wide crown; 止 shape shifted DOWN (upper-shu at y~108-250, mid-heng
  y~168, left-shu y~172-253, bottom-heng y~266). Use inline 止 to
  achieve the shift.
- **生 (p3_char_0162, PASS)** — 5 strokes: top pie (95, 82)→(58, 178)
  extended slightly upward per P-MMH-002 (visible ink past MMH medial);
  shu ends at y=262 (10.5 px above MMH y=272 for N-gap with s5).
  bottom_heng y~285.
- **平 (p3_char_0176, PASS)** — 5 strokes: top-heng short (99, 77)→
  (204, 65); left-dian (79, 112)→(106, 146); right-pie (202, 94)→
  (175, 144); middle-heng long (36, 188)→(273, 174); central shu (136, 87)
  → clamped y=298 (MMH tail y=311 out of canvas — clamp).

### B6 FAIL calibration (for future retries or sibling chars)

- **刅 (p3_char_0135, FAIL)**: 4-stroke composition of 刀-body + 2 side ticks.
  Inline heng_zhe_gou (bank) had wrong topology; drawer should use inline
  heng_zhe with tight joint, not the bank compound. Very-low-freq char —
  do not retry.
- **水 (p3_char_0138, FAIL)**: known bank gap for 3-directional 水.
  Terminal-frozen in B4 as bare radical. Do not retry.
- **风 (p3_char_0144, FAIL)**: needs heng_xie_wan_gou (right side outer wrap).
  Bank gap. Terminal-frozen bare 风 in B4. Do not retry.
- **引 (p3_char_0150, FAIL)**: bank has NO 弓 primitive. Any 弓-prefix
  char (张/弟/弱/弘/弹) will FAIL until 弓 gets promoted from a PASSing
  attempt. LOW priority for retry.
- **他 (p3_char_0154, FAIL)**: 也 needs heng_zhe_wan_gou top arc.
  Do not retry until we have that primitive (unlikely per B6 test).
- **仗 (p3_char_0177, FAIL)**: 亻+丈 L-R proportion. Retry hint = shrink
  ren_left to scale=0.55, extend 丈 anchors further right.
- **丱 (p3_char_0163, FAIL)**: rare 5-stroke; do not retry.
- **发 (p3_char_0170, FAIL)**: HIGH-freq char (发展/头发). All bank
  primitives used — issue is composition proportion. Retry hint = compress
  top heng vertical range, shorten na tail. MEDIUM priority for B7 R1.
- **必 (p3_char_0155, C)**: uses draw_wo_gou (B5 promotion) but dot
  placement off. Retry hint = 3 dians at TR/C/BL, wo_gou belly slightly
  deeper.
- **打, 付 (p3_char_0180/0179, C)**: 扌+丁/寸 L-R. Retry hint = shrink 扌
  width, extend right radical.

---
