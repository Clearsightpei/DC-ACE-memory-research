# G4 drawer_memory (v8, position 350)

*Free-form persistent memory added at v8 unlock. Same shape as G2's
memory. Curator writes here; drawer reads it via `memory_index.md`.
Read this BEFORE the structured bank — for many items it will already
name the primitive to call.*

*The grid bank (`success_bank/code/`) + principles + form_catalog +
joint_atlas remain available as REFERENCE. Nothing in them is mandatory
under v8. When this file and the structured bank disagree, follow this
file.*

---

## Fast lookup — call these primitives directly

The single highest-value action per B6 evidence: **when a character
contains one of these components as a sub-part, IMPORT and CALL the
primitive**. Do not reinvent. B6 had ~15 items where reuse would have
saved the attempt; ~8 of them FAILed by drawing fresh instead.

### Chronic canonical primitives (mandatory imports)

If the target contains 丿, 刀, 冂, 弓, 马 as a component: **import the
chronic module**. B6 showed drawers cite these in comments but never
import them; that is treated as a mechanism failure. From B7 onward,
comment-only mention is not sufficient.

```python
from chronic.pie_radical import draw_pie_radical    # 丿
from chronic.dao_char     import draw_dao_char       # 刀 (and 刅, 刀-containing chars)
from chronic.jiong_frame  import draw_jiong_frame    # 冂 (and 用, 内, 円, 内, 门-containing chars)
from chronic.gong_bow     import draw_gong_bow       # 弓 (and 引, 弗, 弘)
from chronic.ma_horse     import draw_ma_horse       # 马 (and 乌, 鸟)
```

If the character contains the component but at a different position/
scale, still call the chronic primitive first and shift its output via
the `offset_x`/`offset_y`/`scale` parameters where available, rather
than redrawing.

### High-value component primitives

For left-radical or bottom-radical compositions, these bank files are
worth importing:

```python
from ren_side  import draw_ren_side    # 亻 (仔/付/打/化/他/仝/仕 all reused this in B6)
from shou_side import draw_shou_side   # 扌
from xin_side  import draw_xin_side    # 忄
from si_silk   import draw_si_silk     # 纟
from chi_step  import draw_chi_step    # 彳
from you_again import draw_you_again   # 又 (needed for 反 又 对 权 etc)
from bi        import draw_bi          # 匕 (mirror for 比; call TWICE for 比)
from li        import draw_li          # 力 (needed for 办 加 男)
from bao_char  import draw_bao_char    # 勹 (needed for 勻 匀 匆)
from er_legs   import draw_er_legs     # 儿 (needed for 元 兄 光)
from xin       import draw_xin         # 心 (needed for 必)
from tu        import draw_tu          # 土 (needed for 去 圭 坐)
from si_private import draw_si_private # 厶 (needed for 去 台 参)
from shan      import draw_shan        # 山 (call TWICE stacked for 出)
```

### Never-tune-anchors rule for reused primitives

When you import a primitive, call it with its DEFAULT signature. If
the primitive doesn't fit exactly, prefer inlining fresh (per shared
rules "supplementary aid") — do NOT try to override 3+ anchors of a
mastered primitive. That path caused the p2_082_子 chronic saturation
in B4.

---

## Compositional playbook — how to think about 3+-part characters

B6 diagnosis: all 24 main FAILs are multi-part characters where the
sub-parts don't visually cohere. All 26 main PASSes are either
simple 3-4 stroke chars or 亻/扌/宀-prefixed reuses. **The failure
mode is composition, not stroke rendering.**

**Step 1**: split the target into named sub-radicals BEFORE looking at
anchors. Write the split as a comment: `# 反 = 厂 + 又`.

**Step 2**: for each sub-radical, look for a mastered bank primitive
in the shortlist above OR in `success_bank/INDEX.md`. If one exists,
IMPORT it.

**Step 3**: place the sub-radicals in a grid layout:
- **Left-right** (亻+X, 扌+X): left in x∈[0.05, 0.40], right in x∈[0.45,
  0.95]. Both fill y∈[0.10, 0.90].
- **Top-bottom** (宀+X, 一+X, 亠+X): top in y∈[0.05, 0.35], bottom in
  y∈[0.35, 0.95].
- **Enclosing** (囗+X, 门+X, 冂+X): frame fills [0.10, 0.90] both axes;
  inner sub-radical fills middle 60% both axes.
- **Stacked repeated** (出=山+山, 比=匕+匕): use SAME primitive twice
  with mirrored or offset anchors.

**Step 4**: enforce compositional coherence — every sub-radical must
share at least one anchor pixel with an adjacent sub-radical, or leave
a visible ~15-25 px gap. Never touch AND never disconnected.

---

## B6 systematic failure notes

**Enclosing frames (冂/门/囗-containing chars)**: 用, 们, 内 all failed
by not calling `chronic/jiong_frame.py`. If the target contains an
enclosing frame, the FIRST line of code should be
`from chronic.jiong_frame import draw_jiong_frame`.

**Left 阝 radical is missing from the bank.** 队 FAILed because there
is no primitive for 阝-left. Right 阝 exists (`fu_right.py`) but is
NOT a mirror. Until a `fu_left.py` promotion arrives, decompose 阝-left
as: short 撇 top + 竖 left + 横折 bend + tail — 3 strokes in x∈[0.05,
0.35] column.

**Stroke-count omissions**: 水 keeps rendering as 3 strokes (missing
right 捺); 礻 keeps rendering as 3 strokes (missing top dot). Add an
explicit `assert len(strokes) == expected` before rendering, and add a
retry pass if the count is off.

**Symmetry pairs (比, 丱, 从, 双)**: these characters are TWO copies
of the same sub-radical. Compute anchors ONCE, then mirror x_frac via
`(cell, 1 - x_frac, y_frac)` for the mirrored copy. Do NOT hand-derive
two independent copies — they will not match.

**顶部单点 items (礻 主 亠-family)**: the top dot is often the first
thing dropped by the drawer. Render the dot LAST as a defensive step
so it can't be overwritten by later strokes.

**Chronic-mechanism import discipline**: when the target maps to a
chronic primitive, the drawer's `generated.py` MUST include the
`from chronic.<x> import draw_<x>` line and MUST call it. A comment
citing the primitive is NOT sufficient (B6 evidence: 18 comment
mentions, 0 imports across all history since position 300).

---

## What NOT to do (drawer traps from B1–B5)

- Do not chain multiple beziers to fake a compound stroke. Use
  `stroke_variable_width` with a single polyline. (see 飞 chronic fails)
- Do not draw two separate strokes for what MMH lists as one compound.
  (e.g. 及, 廷, 建 need `heng_zhe_zhe_zhe.py` NOT 3 pieces.)
- Do not tune the anchors of a chronic primitive. Call it as-is. If
  it looks wrong to you, that means your visual read of the GT differs
  from the panel's — the panel wins.
- Do not skip `errata.md` on repeat items. Every retry is against a
  drawer's own prior failure, and the errata fix is the panel's summary
  of what needs to change.
- Do not soft-interpret an errata fix. "Widen to anti-diagonal ('TR',
  0.85, 0.15) → ('BL', 0.15, 0.85)" means those exact tuples, not
  "something more diagonal than before."

---

## Interpretation window (from v8 rules)

Everything in the bank + principles + form_catalog + joint_atlas is
REFERENCE ONLY. If your visual read of the GT disagrees with them,
follow your read. But: when an item has failed 2+ times and the errata
gives a literal fix, the interpretation window closes — follow the
errata verbatim. The 4-batch chronic-cluster saga (see `evolution.md`
position 300) is the negative evidence.
