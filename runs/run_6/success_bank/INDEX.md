# Success Bank — Index — run_6

Curator-owned. **Only mastered code lives here.** Entries are added when the Curator promotes them through the 5-gate (structural + judge panel).

## Hard mastery gate (run_6)

Promotion requires **ALL**:

1. `structural_pass == True` (stroke count + every anchor within 15 px + every joint within 20 px and in declared cell)
2. `judge_panel.unanimous_yes == True` (3 fresh-context skeptics)

OCR + visual_score are informational only. The c5/c20/c24 false-positive class is eliminated by gate 1.

## Architecture

Every entry stores **anchor notation** (no magic numbers). Anchors translate to turtle math-coords via `_anchor.py`.

- **Atomic strokes** (mastered c1–c6): horizontal stroke + vertical stroke + 撇/捺 diagonals + 提 + 点.
- **Compound strokes** (mastered c7–c13): 横折, 竖钩, 横折钩, 竖弯钩, 横撇, 竖折, 横折弯钩.
- **Characters** (c14+): compose mastered strokes by anchor.

The library is fully compositional: every entry calls only entries already in the bank.

## Entries

| name | file | tags | mastered |
|---|---|---|---|
| (anchor helper) | [code/_anchor.py](code/_anchor.py) | utility | run_6 init |
| 竖 | [code/shu.py](code/shu.py) | tag:atomic-stroke tag:shu tag:垂露 | c2 (structural ✓, v=0.83) |
| 横折 | [code/heng_zhe.py](code/heng_zhe.py) | tag:compound-stroke tag:heng_zhe | c13 (via 口) |
| 横折提 | [code/heng_zhe_ti.py](code/heng_zhe_ti.py) | tag:compound-stroke tag:heng_zhe_ti tag:three-segment | c31 (isolated, panel 3/3 YES) |
| 又 | [code/you.py](code/you.py) | tag:character | c34 (panel 3/3 YES, MMH-direct anchors with bend-corner) |
| 目 | [code/mu_eye.py](code/mu_eye.py) | tag:character | c42 (restart of c40, panel 3/3 YES with geometric L-corner) |
| 五 | [code/wu.py](code/wu.py) | tag:character | c49 (panel 3/3 YES, joint-snap + geometric L-corner) |
| 白 | [code/bai.py](code/bai.py) | tag:character | c50 (panel 3/3 YES) |
| 半 | [code/ban.py](code/ban.py) | tag:character | c52 (panel 3/3 YES, first char using dian) |
| 口 | [code/kou.py](code/kou.py) | tag:character | c32 (re-judged 3/3 YES with calligraphy-aware panel) |
| 七 | [code/qi.py](code/qi.py) | tag:character | c35 (re-judged 3/3 YES with calligraphy-aware panel) |
| 八 | [code/ba.py](code/ba.py) | tag:character | c53 (3/3 YES, apex_share override — strokes splay from shared apex y) |
| 人 | [code/ren.py](code/ren.py) | tag:character | c54 (3/3 YES, apex_share override — strokes meet at apex) |
| 牛 | [code/niu.py](code/niu.py) | tag:character | c59 (3/3 YES, raw MMH, 2 P + 1 N joints) |
| 立 | [code/li_stand.py](code/li_stand.py) | tag:character | c62 (3/3 YES, raw MMH; file named li_stand to avoid clash with 力) |
| 横折钩 | [code/heng_zhe_gou.py](code/heng_zhe_gou.py) | tag:compound-stroke tag:heng_zhe_gou tag:hook | c12 (via 力) |
| 横撇 | [code/heng_pie.py](code/heng_pie.py) | tag:compound-stroke tag:heng_pie | c11 (via 又) |
| 竖弯钩 | [code/shu_wan_gou.py](code/shu_wan_gou.py) | tag:compound-stroke tag:shu_wan_gou tag:hook | c10 (via 七) |
| 竖折 | [code/shu_zhe.py](code/shu_zhe.py) | tag:compound-stroke tag:shu_zhe tag:two-segment | c9 (via 乚) |
| 横折弯钩 | [code/heng_zhe_wan_gou.py](code/heng_zhe_wan_gou.py) | tag:compound-stroke tag:hook tag:three-segment | c8 (via 乙) |
| 横钩 | [code/heng_gou.py](code/heng_gou.py) | tag:compound-stroke tag:heng_gou tag:hook | c7 (via 乛, count ✓ vision ✓) |
| 竖钩 | [code/shu_gou.py](code/shu_gou.py) | tag:compound-stroke tag:shu_gou tag:hook | c6 (via 亅, structural ✓) |
| 捺 | [code/na.py](code/na.py) | tag:atomic-stroke tag:na tag:flat-kick | c5 (introduced via 八, structural ✓) |
| 点 | [code/dian.py](code/dian.py) | tag:atomic-stroke tag:dian | c4 (structural ✓) |
| 撇 | [code/pie.py](code/pie.py) | tag:atomic-stroke tag:pie tag:tapered-tip | c3 (structural ✓, from=9.8 to=5.1 px) |
| 横 | [code/heng.py](code/heng.py) | tag:atomic-stroke tag:heng tag:楷书 | c1 (structural ✓, panel 3/3 YES, v=0.83) |

(Empty otherwise — populated cycle by cycle.)

| 十 | [code/shi.py](code/shi.py) | tag:character | c16 |
| 干 | [code/gan.py](code/gan.py) | tag:character | c17 |
| 工 | [code/gong.py](code/gong.py) | tag:character | c18 |
| 上 | [code/shang.py](code/shang.py) | tag:character | c19 |
| 下 | [code/xia.py](code/xia.py) | tag:character | c20 |
| 大 | [code/da.py](code/da.py) | tag:character | c21 |
| 木 | [code/mu.py](code/mu.py) | tag:character | c22 |
| 王 | [code/wang.py](code/wang.py) | tag:character | c23 |
| 主 | [code/zhu.py](code/zhu.py) | tag:character | c24 |
| 不 | [code/bu.py](code/bu.py) | tag:character | c25 |
| 中 | [code/zhong.py](code/zhong.py) | tag:character | c26 |
| 日 | [code/ri.py](code/ri.py) | tag:character | c27 |
| 月 | [code/yue.py](code/yue.py) | tag:character | c28 |
| 田 | [code/tian.py](code/tian.py) | tag:character | c29 |
| 三 | [code/san.py](code/san.py) | tag:character tag:3-strokes | c15 |
| 二 | [code/er.py](code/er.py) | tag:character tag:2-strokes | c14 |

## Carry-over reference

Run_5's frozen Success Bank lives at `runs/run_5/success_bank/`. Run_6 does NOT import from it. The run_5 bank is a numeric-memory baseline for later comparison; run_6 starts fresh with structural memory.
| 自 | zi | 6 | c66 | 3/3 | pie + 日-box + 2 internal hengs |
| 林 | lin | 8 | c70 | 3/3 | 木+木 left/right symmetric |
| 京 | jing_capital | 8 | c72 | 3/3 | re-verified with MMH-derived anchors after demotion |
