# Form Catalog — stroke × context lookup (G3 coord-bank)

*Created 2026-07-18 (v7 self-evolution) in direct response to the
B2 collapse (34% pass rate) and the user's diagnosis that "there
are many types of 点, 撇, they all look different and have different
angles — memory is restricting them too much".*

This is a **contextual form lookup**. For a given stroke label and a
given position/role, this file gives concrete angle / taper / bow /
size numbers that empirically worked in a PASS. Use with the adaptive
helpers `variant_pie / variant_na / variant_dian` in
`success_bank/code/_shared_helpers.py`, not the frozen scale-only
bank primitives.

Numbers reflect PASSes through B2 (positions 1–150). Add rows for
every future PASS whose stroke is a non-trivial variant.

Format:
```
| stroke | context / role | head (math) | tail (math) | bow_perp | w_head | w_tail | source item |
```

---

## 撇 (pie) — the largest variant family

### standalone / crossing / dominant
| stroke | context | head (math) | tail (math) | bow_perp | w_head | w_tail | source |
|--------|---------|-------------|-------------|----------|--------|--------|--------|
| 撇 | full-standalone (stroke exam) | (+65, +90) | (-45, -85) | -8 | 10 | 1 | pie.py |
| 撇 | 大-family crossing arm | (0, +25) | (-95, -110) | -6 | 7 | 1 | mu.py (木) |
| 撇 | 父 big-撇 (upper-mid-right → lower-left) | (30, 32) PIL(180,118) | (-95,-118) PIL(55,268) | -8 (perp px) | 9 | 1 | fu.py |
| 撇 | 耂 long sweeping (from right-upper to bottom-left) | (+90, +55) | (-115, -120) | -30 dx / -20 dy | 9 | 1 | lao_radical.py |

### top-of-radical / short
| 撇 | 小 left-of-shaft short | (-12, +10) | (-65, -45) | -4 | 9 | 1 | xiao.py |
| 撇 | 手 short top scoop | (+30, +85) | (-20, +45) | slight | 8 | 1 | (attempt code) |
| 撇 | 毛 top short | PIL(168,78) | PIL(98,128) | slight | 8 | 1.5 | mao.py |

### 丿 radical vs 撇 stroke
- 丿 has SHALLOWER slope and SOFTER curl than pie stroke — see P10.
  Use `variant_pie` with bow_perp closer to 0 (~-2) and w_head reduced
  to ~7 to soften.

## 捺 (na)

| stroke | context | head (math) | tail (math) | bow_perp | w_head | w_belly | w_tail | belly_u | source |
|--------|---------|-------------|-------------|----------|--------|---------|--------|---------|--------|
| 捺 | 大-family crossing arm | (0, +25) | (+95, -110) | +6 | 2 | 11 | 2 | 0.7 | mu.py |
| 捺 | 父 big-捺 | PIL(120,118) | PIL(248,268) | +8 (perp px) | 2 | 15 | 3 | 0.72 | fu.py |
| 捺 | 又 heng_pie tail | see you.py | | | | | | | you.py |

## 点 (dian)

| stroke | context | head (math) | tail (math) | bow_perp | w_head | w_tail | source |
|--------|---------|-------------|-------------|----------|--------|--------|--------|
| 点 | standalone (thick tail lower-right) | (-15, +25) | (+18, -20) | -3 | 3 | 13 | dian.py |
| 点 | 小 right of shaft (default orientation) | ox=+48, scale=0.65 | (uses dian primitive) | | | | xiao.py |
| 点 | 灬 leftmost 左点 (REVERSED: head upper-RIGHT) | PIL(108,195) head | PIL(92,225) tail | slight | 2 | 6.5 | huo_bottom.py |
| 点 | 灬 middle small vertical dot | PIL(139,200) | PIL(146,224) | slight | 2 | 5.5 | huo_bottom.py |
| 点 | 灬 rightmost (standard, tallest) | PIL(200,192) | PIL(228,226) | slight | 2 | 8 | huo_bottom.py |
| 点 | 礻 top small dot | (8, 90) | (24, 68) | via bezier | 2 | 7 | shi_ceremony_pang.py |
| 点 | 礻 right dot (mid-height) | (15, 15) | (38, -15) | via bezier | 2 | 7 | shi_ceremony_pang.py |

Note: for mirrored dot pairs (忄, 丷, 火, 犬 side dots), use
`variant_dian` for BOTH dots with same widths and swap head/tail
positions for the mirror.

## 横 (heng)

Most 横 are uniform ~12 px. Variations:

| stroke | context | source | notes |
|--------|---------|--------|-------|
| 横 | 土 top (shorter) | tu.py | scale 0.60 |
| 横 | 土 bottom (longer) | tu.py | scale 1.05 |
| 横 | 木 crossing bar | mu.py | thickness 7 (thinner than primitive) |
| 横 | 毛 short top w/ 顿笔 | mao.py | PIL length ~103 with corner blob |
| 横 | 日 tall-rectangle top/bottom | ri.py | full width 115 PIL, thickness 11 |
| 横 | 日 middle short | ri.py | thickness 9 (thinner middle) |

Rule: when composing with a shu, MATCH the heng thickness to the
shu thickness (P4 lesson from 屮 fail).

## 竖 (shu)

| stroke | context | source | notes |
|--------|---------|--------|-------|
| 竖 | full-standalone | shu.py | scale 1.0, length 200 |
| 竖 | 木 long crossing shaft | mu.py | thickness 7, length ~165 |
| 竖 | 日 left / right walls | ri.py | thickness 11, length 200 |
| 竖 | 耂 short vertical | lao_radical.py | thickness 7, length 50 |

## Enclosing boxes (aspect matters)

| box | aspect | source | notes |
|-----|--------|--------|-------|
| 口 (kou) | ~1:1 | kou.py | scale 0.65 |
| 囗 (wei) | ~1:1.3 | wei_radical.py | scale 0.875 shu + 0.794 heng_zhe + inline right ext |
| 日 (ri) | ~1:2 tall | ri.py | FULLY inlined — kou would distort |

**Lesson**: never force `kou` primitive for a non-1:1 box. Inline
fresh with matched aspect (or use the tall-rectangle recipe from
`ri.py` as template).

## Corner joints (顿笔)

Small filled ellipse at every 横折 / 竖折 corner where a real brush
would pause. Radius 4-6 px, black. Position at the numeric corner
pixel (compute in comments per TR6).

---

## Growing the catalog

**Every future PASS should add one row per stroke that DIFFERS from
its bank-primitive default.** Curator adds rows post-judgment based
on which numbers empirically worked. Do NOT copy bank-primitive
numbers here — those are already in the .py files. This catalog is
for VARIATIONS.

## Retrieval pattern (drawer's use)

Before drawing stroke X in position Y:
1. Look up `X | Y or similar context | ...` in this table.
2. Copy the head/tail/bow_perp/widths into a `variant_pie` (or
   variant_na / variant_dian) call in `generated.py`.
3. Adjust the head/tail pixels to match your target center; keep
   the bow/widths from the catalog.
4. If no matching row: derive fresh, and post-judgment (if PASS) the
   curator will add YOUR numbers to the catalog.

---

## B3 additions (2026-07-22)

### 撇 (pie) — additional contexts

| stroke | context | head (math/PIL) | tail (math/PIL) | bow_perp | w_head | w_tail | source |
|--------|---------|-------------|-------------|----------|--------|--------|--------|
| 撇 | 文 crossing arm (below heng) | PIL(180,100) | PIL(70,260) | -12 (perp px) | 9 | 1 | wen.py |
| 撇 | 爻 top-乂 arm | PIL(178,55) | PIL(90,155) | -8 (perp px) | 8 | 1 | yao.py |
| 撇 | 乂 standalone crossing arm | math(+45,+65) | math(-105,-110) | -7 | 7 | 1 | yi_cross.py |
| 撇 | 月 near-vertical scoop (long left) | PIL(128,55) | PIL(85,255) | ctrl_x = head_x-2 (bezier) | 12 | 2 | yue.py |
| 撇 | 丿-char thin uniform (MMH-style) | math(+5,+70) | math(-65,-115) | -10 | 4 | 2 | pie_char.py |
| 撇 | 爫 short claw descender | math(0,+32) | math(-10,+12) | -2 | 5.5 | 1.2 | zhao_top.py |

**New rule (P12 candidate)**: for GTs rendered in MMH-median style
(thin uniform lines, no brush profile), use w_head ~4 and w_tail ~2
regardless of stroke label. The bank's calligraphic brush profile
(w_head 10-14) is WRONG for these targets. Check GT visually first
— if lines are uniform-thin, all strokes should use thin uniform
widths, not the calligraphic default.

### 捺 (na) — additional contexts

| stroke | context | head (math/PIL) | tail (math/PIL) | bow_perp | w_belly | belly_u | source |
|--------|---------|-------------|-------------|----------|---------|---------|--------|
| 捺 | 文 crossing arm (below heng) | PIL(120,105) | PIL(240,258) | +10 | 14 | 0.72 | wen.py |
| 捺 | 爻 top-乂 arm (softer) | PIL(122,60) | PIL(218,158) | +8 | 8 | 0.72 | yao.py |
| 捺 | 乂 standalone crossing (softer) | math(-45,+40) | math(+100,-110) | +6 | 10 | 0.65 | yi_cross.py |

### 点 (dian) — additional contexts

| stroke | context | head | tail | bow_perp | w_head | w_tail | source |
|--------|---------|-------------|-------------|----------|--------|--------|--------|
| 点 | 文 top small dot | PIL(158,55) | PIL(138,78) | -2 | 3 | 8 | wen.py |
| 点 | 心 left dot (mirrored, lower-left of bowl) | math(-75,+5) | math(-92,-28) | slight | 2 | 8 | xin.py |
| 点 | 心 middle top dot (angled right) | math(-15,+25) | math(-2,+8) | slight | 2 | 7 | xin.py |
| 点 | 心 right dot (like a small 撇, thick to thin) | math(+55,+40) | math(+42,+8) | slight | 8 | 2 | xin.py |

### 横 (heng) — additional contexts

| stroke | context | source | notes |
|--------|---------|--------|-------|
| 横 | 曰 squat rectangle | yue_speak.py | thickness 11, w=140 (wider than 日) |
| 横 | 月 tall interior (short, tapered thin) | yue.py | w_head 5, w_tail 7 |
| 横 | 七 top (slight downward tilt right, PIL length ~170) | qi.py | uniform 12 |
| 横 | 文 medium below top dot (spans upper-mid) | wen.py | w_head 6, w_tail 8, x=[78,226] |

### Compound / composition patterns

| item | pattern | source |
|------|---------|--------|
| 了 (liao) | inline 横钩 top + wan_gou descender at (26, -62, 0.85) | liao.py |
| 心 (xin) | wo_gou bowl at (-5, -20, 0.85) + 3 tapered dots | xin.py |
| 丩 (jiu_char) | continuous 竖折 (line + 2 bezier segments) + top-hook shaft | jiu_char.py |
| 七 (qi) | inline top heng + bank shu_wan_gou at (-25, -15, 1.0) | qi.py |
| 亅 (jue_char) | inline: short curl entry + shaft + hook base blob + tapered hook flick | jue_char.py |

### Character-vs-radical scaling (aliases pattern)

Many Phase-3 characters are orthographically identical to a Phase-2
radical. B3 PASSes show a consistent scaling recipe:

| item | pattern | scale bump |
|------|---------|-----------|
| 十 (char) | shi (radical) | 1.1 |
| 又 (char) | you (radical) | 1.15 (oy=-5) |
| 儿 (char) | er_ren (radical) | 1.3 (oy=-5) |
| 乚 (char) | ya_radical | 1.5 (ox=+15, oy=-5) |
| 二 (char) | er (radical) | 1.0 (oy=+10) |
| 丶 (char) | dian_radical | 1.15 |
| 凵 (char) | qu_radical | 1.05 (oy=-15) |
| 冫 (char) | bing (radical) | 1.0 (oy=+15) |
| 亠, 亻, 冖, 厂, 八 | (identity aliases — same scale) | 1.0 |
| 丨, 乙 | (identity aliases) | 1.0 |

**Retrieval shortcut**: when a Phase-3 character equals a Phase-2
radical, first try IDENTITY alias. If GT shows the character fills
more of the canvas, bump scale 1.05-1.30 (larger for radicals that
were small like 儿/乚). Nudge oy negative if the primitive's natural
center sits high.

---

## B3-second-pass additions (2026-07-22): worked composition examples

*B3 evidence: 5 of 7 helper-using retries had fail-mode SHIFT — the
per-stroke variant fixed the isolated stroke but composition
(where strokes meet) is now the bottleneck. These worked examples show
the full recipe including joint computation. Use `kiss_apex` /
`pie_point` / `mirror_dian_pair` from `_shared_helpers.py`.*

### X-crossing family (人, 入, 大, 犬, 乂, 文)

**Recipe** (all X-crossings):
```python
from _shared_helpers import variant_pie, variant_na, kiss_apex, pie_point

# Choose crossing style by character:
# 人 → u_pie=0.0 (kiss at pie head, apex up)
# 入 → u_pie=0.30 (na starts on pie shaft, apex up)
# 大 → u_pie=0.5 (crossing at pie midpoint, apex is on heng crossbar)
# 乂 → u_pie=0.5, but no top strokes (see yi_cross.py — PASSED)

pie_head = (+35, +90); pie_tail = (-60, -95)  # target character coords
pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail=(+65, -95),
                        u_pie=0.0, bow_pie=-6.0)
variant_pie(draw, head=pie_h, tail=pie_tail, bow_perp=-6, w_head=9, w_tail=1)
variant_na(draw, head=na_h, tail=(+65, -95), bow_perp=+6,
           w_head=2, w_belly=12, w_tail=2, belly_u=0.7)
# Both strokes now share the exact apex pixel `pie_h`.
```

**Failing without weld** (what the B3 retries did): drawer sets
`pie_head = (+35, +90)` and `na_head = (+30, +85)` (two nearby but
non-identical pixels) — the visual gap breaks the character silhouette.

### Mirror-dot family (忄, 丷, 火, 犬 side dot)

**Recipe**:
```python
from _shared_helpers import variant_dian, mirror_dian_pair

# 忄 with shu_gou at math_x=0:
left, right = mirror_dian_pair(shaft_x=0, y_center=+10,
                                spread=32, w_tail=8, tilt=6)
variant_dian(draw, **left)
variant_dian(draw, **right)
# Then draw the shu_gou shaft at (0, 0, 1.0).
```

**Failing without helper** (what B3 忄 retry_1 did): hand-tuned each
dot separately, got the bow_perp sign wrong on the mirror; dots pointed
the same direction instead of mirroring.

### Radical-alias family (Phase-3 characters that == Phase-2 radicals)

**Recipe**:
```python
# 1. Look up character in the "Character-vs-radical scaling" table above.
# 2. If listed with a scale bump, use that number.
# 3. If listed as "identity alias", call bank primitive with (0, 0, 1.0).
# 4. If not listed but character == some radical form, TRY identity first,
#    then bump scale 1.05-1.30 if GT shows the char fills more canvas.

# Example:
# 十 (char) == 十 (radical), catalog says scale 1.1
from shi import draw_shi
draw_shi(draw, ox=0, oy=0, scale=1.1)
```

**Failure to consult** (what would have saved p3_char_0007_乛): bank
had `heng_gou_radical` (PASSED), the char is orthographically identical,
but the drawer didn't identify the identity alias and derived fresh.

### Retrieval discipline (B3 lesson)

- **Copy from EXACT context, not similar-looking context**. Retry
  083_丬 failed because the drawer copied 忄 dot numbers into a 丬
  composition — but 丬 is compacter and the dots need different
  spread. Prefer "derive fresh with catalog widths" over "copy
  wholesale from adjacent row".
- **When no exact row exists**, use the closest stroke×role match,
  but treat the head/tail POSITIONS as targets to re-derive against
  YOUR character's proportions. Keep only bow_perp / w_head /
  w_tail / belly_u from the catalog row.

---

## B4 additions (2026-07-23)

### 撇 (pie) — additional contexts (thin-uniform MMH GTs, P12)

| stroke | context | head | tail | bow_perp | w_head | w_tail | source |
|--------|---------|------|------|----------|--------|--------|--------|
| 撇 | 亼-roof (thin uniform, kiss_apex at apex) | math(-2,+75) | math(-90,-50) | -6 | 4 | 2 | ji_meet_char.py |
| 撇 | 丫 fork left arm (short, thin) | math(-55,+55) | math(0,0) | -4 | 4 | 2 | ya_char.py |
| 撇 | 之 corner-continuing (bezier from 横 corner) | math(+40,+50) | math(-30,-35) | via bezier mid=(+5,+11) | 8 | 2 | zhi_char.py |
| 撇 | 久 middle 横撇 continuation | math(+38,+43) | math(-70,-50) | -10 | 8 | 1 | jiu_long_char.py |
| 撇 | 久 top long sweep | math(+5,+105) | math(-70,+10) | -8 | 9 | 1 | jiu_long_char.py |

### 捺 (na) — additional contexts

| stroke | context | head | tail | bow_perp | w_belly | belly_u | source |
|--------|---------|------|------|----------|---------|---------|--------|
| 捺 | 亼 right arm (thin, kiss_apex) | math(-2,+75) | math(+90,-45) | +6 | 4 | 0.7 | ji_meet_char.py |
| 捺 | 丫 right arm mirror (short, thin) | math(+55,+55) | math(0,0) | +4 (via variant_pie mirror) | 4 | n/a | ya_char.py |
| 捺 | 久 long sweep from mid-cross | math(-10,-20) | math(+105,-125) | +10 | 14 | 0.72 | jiu_long_char.py |
| 捺 | 之 平捺 base (gentle sag, long horizontal exit) | math(-70,-70) | math(+120,-55) | -10 (sag) | 13 | 0.75 | zhi_char.py |

### 点 (dian) — additional contexts

| stroke | context | head | tail | bow_perp | w_head | w_tail | source |
|--------|---------|------|------|----------|--------|--------|--------|
| 点 | 之 top small tilted dot | math(+2,+112) | math(+22,+92) | -2 | 2.5 | 9 | zhi_char.py |
| 点 | 叉 crook mark (small pie-like) | math(-30,+40) | math(+5,+25) | -1.5 | 2 | 4 | cha_char.py |

### 横 (heng) — additional contexts

| stroke | context | source | notes |
|--------|---------|--------|-------|
| 横 | 亼 base (thin uniform, MMH-style) | ji_meet_char.py | w=3 uniform |
| 横 | 三 三-line pattern (95 / 80 / 180 length_px) | san_char.py | draw_yi.length_px override per stroke |
| 横 | 上 bottom long | shang_char.py | draw_heng scale 1.05 |
| 横 | 下 top wide | xia_char.py | draw_heng scale 1.05 |
| 横 | 于/亍 top short + mid wide pattern | yu_char.py, chu_char.py | 0.50 short + 0.95 wide |
| 横 | 亡 middle | wang_char.py | draw_heng scale 1.15 |
| 横 | 子 mid crossing | zi_char.py | draw_heng scale 1.0 with ox=+15 |

### Composition / composition patterns (B4)

| item | pattern | source |
|------|---------|--------|
| 刁 (diao) | inlined 横折竖 + inline 提 (bank ti didn't match angle) | diao_char.py |
| 丁 (ding) | heng + shu_gou (2-primitive T-shape) | ding_char.py |
| 勹 (bao) | short pie + continuous cubic-bezier envelope (curve NOT right-angle) | bao_char.py |
| 亍 / 于 | 2-heng + 亅 / 竖钩 pattern (2 hengs stacked + vertical hook) | chu_char.py / yu_char.py |
| 亡 | dian + heng + inline 竖折 (bank shu_zhe aspect wrong for 亡) | wang_char.py |
| 亼 | 人-roof (kiss_apex u=0.0) + 一 base — SUCCESS recipe for X-crossing helper use | ji_meet_char.py |
| 子 (both char and radical) | liao skeleton + crossing 横 (compositional reuse) | zi_char.py |
| 叉 | 又 identity + variant_dian in upper crook | cha_char.py |
| 兀 (char) | heng + er_ren (radical form of 兀 STILL FAILS — char form scales differently: heng 0.85, er_ren 0.95, both centered) | wu_char.py |
| 门 (char) | inline all-3 strokes for tall/narrow aspect (dian + 竖 + 横折钩) — char PASSes with inline; radical FAILS with same approach at different scale | men_char.py |
| 卄 | 3 inline lines (2 near-verticals + heng) — bank gong_radical's 撇 too curved for 卄's straight verticals | nian_char.py |
| 孑 | inline all 3 strokes: 横撇 + 弯钩 + 提 (different from 子's 3 = 横撇 + 弯钩 + 横) | jie_char.py |

### Character-vs-radical scaling (B4 additions)

| item | pattern | scale bump |
|------|---------|-----------|
| 刂 (char) | dao_pang (radical) | 1.0 (identity) |
| 囗 (char) | wei_radical | 1.0 (identity) |
| 山 (char) | shan (radical) | 1.0 (identity) |
| 干 (char) | gan (radical) | 1.0 (identity) |
| 口 (char) | kou (radical) | 1.0 (identity) |
| 艹 (char) | cao_zi_tou (radical) | 1.0 (identity) |
| 宀 (char) | bao_gai_tou (radical) | 1.0 (identity) |
| 小 (char) | xiao (radical) | 1.0 (identity) |

**Retrieval discipline (B4 lesson, extending B3's)**:
- **The "char == radical" identity-alias pattern is now DOMINANT** among
  Phase-3 easy chars. When encountering a Phase-3 character, GREP the
  existing `INDEX.md` for the same glyph first — 8 of 27 B4 PASSes were
  1-line aliases, and several main FAILs (e.g., could-have-been 兀
  radical retry) missed the alias opportunity.
- **Beware the reverse asymmetry**: a Phase-2 radical FAIL does NOT
  block the Phase-3 char PASS — 兀 and 门 PASSed as chars while their
  radical retries FAILed. This suggests the char-drawer benefited from
  the retry's fresh reasoning even without a bank primitive. Do NOT
  block a Phase-3 char attempt just because its radical is in errata.

### B4 non-lesson: composition helpers still unused on retries

Every one of the 8 B4 retries went inline with hand-rolled `_tb` /
`_var_line` helpers instead of importing `kiss_apex` / `pie_point` /
`mirror_dian_pair` — even 夂/夊/兀 whose retry rationales explicitly
called for kiss_apex. Retry drawers appear to skip the memory-index
read on FAIL-remediation prompts (or the retry brief overrides it with
a heavier "fresh from GT" injunction). See evolution.md 2026-07-23 for
the B5 fix.
