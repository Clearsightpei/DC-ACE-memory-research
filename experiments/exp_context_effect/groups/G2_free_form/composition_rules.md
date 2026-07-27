# Composition Rules (v7.3, pos 300)

*Created 2026-07-24 as part of B5 self-evolution response (evolution.md
pos 326). B5 main-fails were dominated by compound-character failures
where the component was known (from form_catalog) but the composition
was not. This file surfaces composition rules that transfer across
whole families.*

**Consult BEFORE drawing any 4+-stroke character whose top-level
decomposition is `<component> + <component>`.** If the target label
matches a composition family below, verbatim-copy the rule into your
generated.py docstring as a `# COMPOSITION RULE:` block.

---

## 亻 + X (left-position person radical + right body)

**Applies to**: 化, 他, 们, 仔, 仕, 仗, 付, 仝, 仞, 仇, 仑, 仓,
从 (double 亻-like), 你, 他, 侄, 修, and any 亻-prefix P3 char.

**Rule**:
- **亻 sits LEFT, taking ~30% of canvas width** (x=40–110 out of 300).
  A wider 亻 crushes the body; a narrower 亻 detaches from the body.
- **亻 = short 撇 (top) + straight 竖 (below)**:
  - 撇 starts x≈95 y≈60, ends x≈50 y≈130 (SHORT ~85 px).
  - 竖 starts x≈75 y≈120, ends x≈75 y≈240 (through-axis).
  - Joint at (~75, 125) shared, NOT gapped.
- **Body sits RIGHT (x=120–260, y=60–260)** — the body has almost
  the FULL height of the canvas, unlike 亻 which stops at 240.
- **Body scales to fit the right ~55% of canvas** — don't shrink
  the body to match 亻's compression.

**Avoid**:
- 亻 dominating the canvas horizontally → body squeezed unreadable.
- 亻's 竖 short (stopping at y≈180) → 亻 looks like a floating radical.
- Body offset too low → reads as vertically-stacked, not left-right.

**Cross-ref**: form_catalog "撇 as left-position radical component";
sibling_signature_checklist has no direct row (not a sibling-risk
family). Prior fails: 仇, 仑, 仓 (all B5 main-fails).

---

## 人-lid + X (top-hat 人 covering a body)

**Applies to**: 个, 仝, 仑, 仓, 全, 内, 兪, and any char whose top
component is 人 (a two-stroke apex with 撇+捺).

**Rule**:
- **人-lid = 撇 + 捺 sharing apex at TOP-CENTER** (~x=150, y=55–65).
  Both strokes throw OUTWARD, foot-spread wider than shoulders.
- **捺 has visible thick foot** (the 顿 dab at terminal, width ≥6 px).
  A thin-tail 捺 makes the lid read as 入 (overhanging) or 亇 (two
  撇). Copy sibling_signature_checklist rows 人/入 verbatim if unsure.
- **Body sits UNDER the lid** with:
  - Body top just below the 捺 foot (y≈130+).
  - Body horizontally CENTERED under the lid's apex, not offset.
  - Body width ≤ lid foot span (don't let the body poke out sideways).
- **Vertical spacing**: 20–30 px gap between lid-捺-foot (y≈130)
  and body-top. Too tight = fused blob; too loose = detached.

**Avoid**:
- Rendering the lid as 亠 (一 + 丶) — that's a different lid family.
- 撇 and 捺 not meeting at apex (creates a gap → reads as 八 top).
- Body overflows lid → the compound reads as two stacked glyphs.

**Cross-ref**: sibling_signature_checklist 人 / 入 rows;
form_catalog "捺 as right-leg of two-stroke apex". Prior fails: 仑,
仓 (B5), 亾 (B4).

---

## 冂 + interior (bracket enclose + interior element)

**Applies to**: 内, 內, 冈, 冂-based chars, 用, 甪, 甫, 网.

**Rule**:
- **冂 = top 一 (横) + right shoulder 横折 (竖)**. The bracket has:
  - Top 一 at y≈55, spanning x=70–230 (wide).
  - Left 竖 dropping from (x≈70, y≈55) to (x≈70, y≈240).
  - Right shoulder-折 dropping from (x≈230, y≈55) to (x≈230, y≈240).
- **Interior sits in the LOWER 2/3 of the bracket**:
  - Interior top-edge at y≈100 (30–45 px BELOW the top-一).
  - Interior does NOT touch the bracket walls; keep 8–15 px margin
    on all sides.
- **If interior is 人** (as in 内 / 內): apex y≈130, feet spread to
  x=95 (left) and x=205 (right), captured BELOW top-一 by 20+ px.
- **If interior is 一** (as in 冂-base compounds): 一 sits at ≈y=180
  (LOWER third of box, NOT top).

**Avoid**:
- Interior touching the walls → reads as filled-box glyph.
- Interior at top of box → the whole char reads as 凡 or 冂 itself.
- Bracket width < 150 px → the box crushes any interior.

**Cross-ref**: form_catalog "冂-square" and "内-square"; the 见
failure (interior 横 at top of box) is a direct violation of the
"lower 2/3" rule. Prior fails: 内, 內, 见, 冈 (B5).

---

## 亠 + X (dot-撇 lid + body)

**Applies to**: 亢, 亦, 交, 亥, 京, 亭, 主 (亠-like top with 王),
方 (亠 + 力-body), 六, and any 亠-top char.

**Rule**:
- **亠 lid = top 丶 (small dot at x≈150 y≈50) + wide 一 (x=60–240 y≈80)**.
  The dot sits ABOVE the 一, not merged into it (5–10 px gap).
- **Lid 一 must be WIDE — spanning at least 70% of canvas width**.
  A narrow 一 makes the lid look cramped and the body reads as if
  detached.
- **Body sits UNDER the 一 with a 15–25 px gap** — same spacing
  discipline as 人-lid.
- **Body centered horizontally** under the lid's midpoint (x≈150).

**Avoid**:
- Rendering the 亠 dot as a 撇 (that's a different lid family — a
  proper 亠 has a small dot, not a diagonal stroke).
- 一 too narrow → the compound loses its "lid + body" balance,
  reads as 六 or 亠 alone with orphaned strokes below.

**Cross-ref**: form_catalog "撇 as top-lid" (adjacent family);
form_catalog "亡 as 亠 + L body". Prior fails: 亢 (B5), 方 (B5,
frozen-candidate but not yet frozen).

---

## 阝 + X (right-ear or left-ear enclose)

**Applies to**: 队 (阝-left + 人), 阴, 阳, 陈, 郑, 部, 都 (阝-right).

**Rule**:
- **阝 is a compound bracket-glyph rendered as an 陀-shape**:
  - Top loop (a small 横撇弯钩 or 3-stroke loop, x=50–100 y=50–150).
  - Bottom straight 竖 (from bottom of loop to y=250).
- **Left-position 阝 (队, 阴)**: 阝 sits LEFT (x=30–100), body sits
  RIGHT (x=120–260). Same left-radical scaling as 亻.
- **Right-position 阝 (部, 都)**: 阝 sits RIGHT (x=200–270), body
  sits LEFT (x=30–180).

**Avoid**:
- Rendering 阝 as a 3 or B-shape (loops too round). It should look
  like a right-ear-radical with a straight vertical tail.
- 阝 not touching its own top loop's bottom → the tail floats,
  reads as two disconnected marks.

**Cross-ref**: p2_radical_020_阝 in errata (belly-on-right arc);
form_catalog "撇 as left-position radical component" for left-阝
scaling. Prior fails: 阝 itself (never graduated).

---

## Composition-rule anti-patterns (universal)

Independent of the above families:

1. **Never draw a component full-canvas-size and then draw the other
   component OUT of the canvas** — always plan both components' spans
   BEFORE drawing either.
2. **Joints between components must be visible or contact-touching,
   never floating** — 亻's 竖-bottom aligned with body's midpoint;
   人-lid's 捺-foot aligned above body's top edge; 冂's walls
   framing interior with margin.
3. **Component compression is asymmetric** — the left/top component
   compresses; the right/bottom component keeps close to full height/
   width. Don't compress both.

---

## How this file transfers (test hypothesis)

**Target**: B6 main-pass rate on compound characters (items involving
亻 / 冂 / 亠 / 人-lid) ≥ 60%. If <45%, this file joined the checklist
as another additive-not-effective intervention.

Cite this file in your generated.py docstring when your target has
a top-level decomposition into two components matching a family above.
Format:

```
# COMPOSITION RULE (per composition_rules.md):
#   family = <亻+X | 人-lid+X | 冂+interior | 亠+X | 阝+X>
#   rule = <verbatim key rule from the family section>
```
