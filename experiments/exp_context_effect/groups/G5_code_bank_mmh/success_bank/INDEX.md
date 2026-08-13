# G5 Success Bank — INDEX

*Registry of callable-Python bank primitives. One row per file in `success_bank/code/`. Curator appends after each PASSed item that gets promoted.*

*Fresh start 2026-08-08 — bank seeded from bootstrap batch; extended B1–B12. Current size: **177 primitives** (22 stroke + 155 radical/char) after B12 (+10 promoted: 10 A verdicts; 1 promoted as wrapper `shen_god.py`, 9 kept as inline templates in `attempts/`).*

## Stroke primitives (endpoint-signature)

Callers pass `(draw, head, tail, ...)` where head/tail are MMH-derived pixel anchors.

| # | Kind | Item ID | Char | Batch | File | Fn signature |
|---|------|---------|------|-------|------|--------------|
| 1 | stroke | p2_radical_001_丨 | 丨 | bootstrap | `shu.py` | `draw_shu(d, head, tail, width=7, top_curl=False)` |
| 2 | stroke | p2_radical_005_一 | 一 | bootstrap | `heng.py` | `draw_heng(d, head, tail, width_head=9, width_tail=10)` |
| 3 | stroke | p2_radical_008_丶 | 丶 | bootstrap | `dian.py` | `draw_dian(d, head, tail, w_head=3, w_tail=8, bow=5, steps=48)` |
| 4 | stroke | (extracted from p2_radical_009_八 s1) | 撇 | bootstrap | `pie.py` | `draw_pie(d, head, tail, bow_perp=12, w_head=9, w_tail=3, steps=80)` |
| 5 | stroke | (extracted from p2_radical_009_八 s2) | 捺 | bootstrap | `na.py` | `draw_na(d, head, tail, bow_perp=14, w_head=4, w_tail=11, steps=80)` |
| 6 | stroke | p2_radical_004_乛 | 乛 | bootstrap | `heng_zhe_short.py` | `draw_heng_zhe_short(d, head, tail, corner_offset=(0,4))` |
| 7 | stroke | (extracted from p2_radical_011_匕 s2) | 竖弯钩 | bootstrap | `shu_wan_gou.py` | `draw_shu_wan_gou(d, head, tail, width=7, bottom_extra=60, knee_ratio=0.75)` |
| 8 | stroke | (extracted from p2_radical_016_刂 s2) | 竖钩 | bootstrap | `shu_gou.py` | `draw_shu_gou(d, head, tail, width=6, hook_start_offset=40)` |
| 9 | stroke | (extracted from p2_radical_068_扌 s3, B1) | 提 | B1 | `ti.py` | `draw_ti(d, head, tail, w_head=9, w_tail=2, steps=50)` |
| 10 | stroke | (extracted from p2_radical_063_山 s2 via BANK_DEVIATION, B1) | 竖折 | B1 | `shu_zhe.py` | `draw_shu_zhe(d, head, corner, tail, width=7)` |
| 11 | stroke | (extracted from p2_radical_025_力 s1 via BANK_DEVIATION, B1) | 横折钩 | B1 | `heng_zhe_gou.py` | `draw_heng_zhe_gou(d, heng_head, corner, gou_tail, hook_tip)` |
| 12 | stroke | (extracted from p2_radical_037_又 s1 via BANK_DEVIATION, B1) | 横撇 | B1 | `heng_pie.py` | `draw_heng_pie(d, head, tail, apex_x=None, corner_x=None)` |
| 13 | stroke | (extracted from p2_radical_044_辶 s3 via BANK_DEVIATION, B1) | 平捺 | B1 | `ping_na.py` | `draw_ping_na(d, head, tail, belly_drop=8)` |
| 14 | stroke | (extracted from p2_radical_057_口 s2 via BANK_DEVIATION, B1) | 横折(box) | B1 | `heng_zhe_box.py` | `draw_heng_zhe_box(d, top_left, bottom_right, width=8)` |
| 15 | stroke | (extracted from p2_radical_079_弋 s2 + 096_戈 s2 via BANK_DEVIATION, B2) | 斜钩 | B2 | `xie_gou.py` | `draw_xie_gou(d, head, tail, width=8, bow=10, hook_up=32, hook_back=6)` |
| 16 | stroke | (extracted from p2_radical_112_欠 s2 via BANK_DEVIATION, B2) | 横钩 | B2 | `heng_gou.py` | `draw_heng_gou(d, head, corner, hook_tip, w_start=3, w_corner=5, w_tip=1.5)` |
| 17 | stroke | (extracted from p3_char_0009_了 via BANK_DEVIATION, B3 **A**) | 弯钩 | B3 | `wan_gou.py` | `draw_wan_gou(d, head, tail, belly_right=27, hook_len=26, hook_up=13, w_head=5, w_body=5.5, w_tail=2)` |
| 18 | stroke | (extracted from p2_radical_035_讠__retry_2 via BANK_DEVIATION, B3) | 横折提 | B3 | `heng_zhe_ti.py` | `draw_heng_zhe_ti(d, head, tail, corner=None, descend_mid=None, ti_head=None, width=6)` |
| 19 | stroke | (extracted from p2_radical_078_幺__retry_1 via BANK_DEVIATION, B3) | 撇折 | B3 | `pie_zhe.py` | `draw_pie_zhe(d, head, corner, tail, pie_bow=7, zhe_bow=1, w_head=6, w_corner=5, w_tail=4)` |
| 20 | stroke | (extracted from p3_char_0112_心 via BANK_DEVIATION, B5) | 卧钩 | B5 | `wo_gou.py` | `draw_wo_gou(d, head, tail, belly_y=None, width=8, hook_up=26, hook_back=6)` |
| 21 | stroke | (extracted from p3_char_0122_五 via BANK_DEVIATION, B5) | 横折(wide) | B5 | `heng_zhe_wide.py` | `draw_heng_zhe_wide(d, head, tail, corner=None, w_head=8, w_tail=8, corner_dab=6)` |

## Radical primitives (position-signature)

Callers pass `(draw, ox=0, oy=0, scale=1.0)`. Reference canvas is 300×300; callers translate/scale into the composition.

| # | Kind | Item ID | Char | Batch | File | Fn signature |
|---|------|---------|------|-------|------|--------------|
| 15 | radical | p2_radical_006_乙 | 乙 | bootstrap | `yi_second.py` | `draw_yi_second(d, ox=0, oy=0, scale=1.0)` |
| 16 | radical | p2_radical_007_乚 | 乚 | bootstrap | `yi_hook.py` | `draw_yi_hook(d, ox=0, oy=0, scale=1.0)` |
| 17 | radical | p2_radical_009_八 | 八 | bootstrap | `ba.py` | `draw_ba(d, ox=0, oy=0, scale=1.0)` |
| 18 | radical | p2_radical_010_勹 | 勹 | bootstrap | `bao_wrap.py` | `draw_bao(d, ox=0, oy=0, scale=1.0)` |
| 19 | radical | p2_radical_011_匕 | 匕 | bootstrap | `bi_dagger.py` | `draw_bi(d, ox=0, oy=0, scale=1.0)` |
| 20 | radical | p2_radical_012_冫 | 冫 | bootstrap | `bing_ice.py` | `draw_bing(d, ox=0, oy=0, scale=1.0)` |
| 21 | radical | p2_radical_013_卜 | 卜 | bootstrap | `bu_divine.py` | `draw_bu(d, ox=0, oy=0, scale=1.0)` |
| 22 | radical | p2_radical_014_厂 | 厂 | bootstrap | `chang_cliff.py` | `draw_chang(d, ox=0, oy=0, scale=1.0)` |
| 23 | radical | p2_radical_015_刀 | 刀 | bootstrap | `dao_knife.py` | `draw_dao(d, ox=0, oy=0, scale=1.0)` |
| 24 | radical | p2_radical_016_刂 | 刂 | bootstrap | `dao_right.py` | `draw_dao_right(d, ox=0, oy=0, scale=1.0)` |
| 25 | radical | p2_radical_018_二 | 二 | bootstrap | `er_two.py` | `draw_er(d, ox=0, oy=0, scale=1.0)` |
| 26 | radical | p2_radical_025_力 | 力 | B1 | `li_power.py` | `draw_li(d, ox=0, oy=0, scale=1.0)` |
| 27 | radical | p2_radical_026_冖 | 冖 | B1 | `mi_cover.py` | `draw_mi_cover(d, ox=0, oy=0, scale=1.0)` |
| 28 | radical | p2_radical_028_人 | 人 | B1 | `ren.py` | `draw_ren(d, ox=0, oy=0, scale=1.0)` |
| 29 | radical | p2_radical_029_亻 | 亻 | B1 | `ren_left.py` | `draw_ren_left(d, ox=0, oy=0, scale=1.0)` |
| 30 | radical | p2_radical_030_入 | 入 | B1 | `ru.py` | `draw_ru(d, ox=0, oy=0, scale=1.0)` |
| 31 | radical | p2_radical_031_十 | 十 | B1 | `shi_ten.py` | `draw_shi_ten(d, ox=0, oy=0, scale=1.0)` |
| 32 | radical | p2_radical_033_亠 | 亠 | B1 | `tou_lid.py` | `draw_tou(d, ox=0, oy=0, scale=1.0)` |
| 33 | radical | p2_radical_037_又 | 又 | B1 | `you_again.py` | `draw_you(d, ox=0, oy=0, scale=1.0)` |
| 34 | radical | p2_radical_039_艹 | 艹 | B1 | `cao_grass.py` | `draw_cao(d, ox=0, oy=0, scale=1.0)` |
| 35 | radical | p2_radical_043_川 | 川 | B1 | `chuan_river.py` | `draw_chuan(d, ox=0, oy=0, scale=1.0)` |
| 36 | radical | p2_radical_044_辶 | 辶 | B1 | `chuo_walk.py` | `draw_chuo(d, ox=0, oy=0, scale=1.0)` |
| 37 | radical | p2_radical_046_大 | 大 | B1 | `da_big.py` | `draw_da(d, ox=0, oy=0, scale=1.0)` |
| 38 | radical | p2_radical_048_干 | 干 | B1 | `gan_dry.py` | `draw_gan(d, ox=0, oy=0, scale=1.0)` |
| 39 | radical | p2_radical_049_工 | 工 | B1 | `gong_work.py` | `draw_gong_work(d, ox=0, oy=0, scale=1.0)` |
| 40 | radical | p2_radical_052_广 | 广 | B1 | `guang_wide.py` | `draw_guang(d, ox=0, oy=0, scale=1.0)` |
| 41 | radical | p2_radical_057_口 | 口 | B1 | `kou_mouth.py` | `draw_kou(d, ox=0, oy=0, scale=1.0)` |
| 42 | radical | p2_radical_063_山 | 山 | B1 | `shan_mountain.py` | `draw_shan(d, ox=0, oy=0, scale=1.0)` |
| 43 | radical | p2_radical_067_士 | 士 | B1 | `shi_scholar.py` | `draw_shi_scholar(d, ox=0, oy=0, scale=1.0)` |
| 44 | radical | p2_radical_068_扌 | 扌 | B1 | `shou_hand.py` | `draw_shou(d, ox=0, oy=0, scale=1.0)` |
| 45 | radical | p2_radical_069_氵 | 氵 | B2 | `sanshui.py` | `draw_sanshui(d, ox=0, oy=0, scale=1.0)` |
| 46 | radical | p2_radical_072_土 | 土 | B2 | `tu_earth.py` | `draw_tu(d, ox=0, oy=0, scale=1.0)` |
| 47 | radical | p2_radical_073_囗 | 囗 | B2 | `wei_enclose.py` | `draw_wei(d, ox=0, oy=0, scale=1.0)` |
| 48 | radical | p2_radical_076_小 | 小 | B2 | `xiao.py` | `draw_xiao(d, ox=0, oy=0, scale=1.0)` |
| 49 | radical | p2_radical_077_忄 | 忄 | B2 | `xin_left.py` | `draw_xin_left(d, ox=0, oy=0, scale=1.0)` |
| 50 | radical | p2_radical_087_灬 | 灬 | B2 | `si_fire_bot.py` | `draw_si_fire_bot(d, ox=0, oy=0, scale=1.0)` |
| 51 | radical | p2_radical_089_车 | 车 | B2 | `che_car.py` | `draw_che(d, ox=0, oy=0, scale=1.0)` |
| 52 | radical | p2_radical_095_父 | 父 | B2 | `fu_father.py` | `draw_fu(d, ox=0, oy=0, scale=1.0)` |
| 53 | radical | p2_radical_096_戈 | 戈 | B2 | `ge_dagger.py` | `draw_ge(d, ox=0, oy=0, scale=1.0)` |
| 54 | radical | p2_radical_097_户 | 户 | B2 | `hu_door.py` | `draw_hu(d, ox=0, oy=0, scale=1.0)` |
| 55 | radical | p2_radical_104_木 | 木 | B2 | `mu_wood.py` | `draw_mu(d, ox=0, oy=0, scale=1.0)` |
| 56 | radical | p2_radical_106_牛 | 牛 | B2 | `niu_cow.py` | `draw_niu(d, ox=0, oy=0, scale=1.0)` |
| 57 | radical | p2_radical_110_攵 | 攵 | B2 | `pu_action.py` | `draw_pu(d, ox=0, oy=0, scale=1.0)` |
| 58 | radical | p2_radical_112_欠 | 欠 | B2 | `qian_owe.py` | `draw_qian(d, ox=0, oy=0, scale=1.0)` |
| 59 | radical | p2_radical_113_犬 | 犬 | B2 | `quan_dog.py` | `draw_quan(d, ox=0, oy=0, scale=1.0)` |
| 60 | radical | p2_radical_114_日 | 日 | B2 | `ri_sun.py` | `draw_ri(d, ox=0, oy=0, scale=1.0)` |
| 61 | radical | p2_radical_056_巾__retry_1 | 巾 | B2 (retry PASS) | `jin_towel.py` | `draw_jin(d, ox=0, oy=0, scale=1.0)` |
| 62 | radical | p2_radical_066_饣__retry_1 | 饣 | B2 (retry PASS) | `shi_food.py` | `draw_shi_food(d, ox=0, oy=0, scale=1.0)` |
| 63 | radical | p2_radical_122_王 | 王 | B3 | `wang_king.py` | `draw_wang(d, ox=0, oy=0, scale=1.0)` |
| 64 | radical | p2_radical_124_文 | 文 | B3 | `wen_text.py` | `draw_wen(d, ox=0, oy=0, scale=1.0)` |
| 65 | radical | p2_radical_128_爻 | 爻 | B3 **A** | `yao_lines.py` | `draw_yao_lines(d, ox=0, oy=0, scale=1.0)` |
| 66 | radical | p2_radical_129_曰 | 曰 | B3 | `yue_say.py` | `draw_yue_say(d, ox=0, oy=0, scale=1.0)` |
| 67 | radical | p2_radical_130_月 | 月 | B3 | `yue_moon.py` | `draw_yue_moon(d, ox=0, oy=0, scale=1.0)` |
| 68 | radical | p2_radical_131_爫 | 爫 | B3 | `zhao_claw_top.py` | `draw_zhao_claw_top(d, ox=0, oy=0, scale=1.0)` |
| 69 | radical | p2_radical_132_支 | 支 | B3 | `zhi_branch.py` | `draw_zhi_branch(d, ox=0, oy=0, scale=1.0)` |
| 70 | radical | p2_radical_133_止 | 止 | B3 | `zhi_stop.py` | `draw_zhi_stop(d, ox=0, oy=0, scale=1.0)` |
| 71 | radical | p2_radical_135_无 | 无 | B3 | `wu_none.py` | `draw_wu_none(d, ox=0, oy=0, scale=1.0)` |
| 72 | radical | p2_radical_105_肀__retry_1 | 肀 | B3 (retry PASS) | `yu_brush_top.py` | `draw_yu_brush_top(d, ox=0, oy=0, scale=1.0)` |
| 73 | radical | p2_radical_078_幺__retry_1 | 幺 | B3 (retry PASS) | `yao_tiny.py` | `draw_yao_tiny(d, ox=0, oy=0, scale=1.0)` |
| 74 | radical | p2_radical_059_门__retry_2 | 门 | B3 (R2 PASS) | `men_gate.py` | `draw_men_gate(d, ox=0, oy=0, scale=1.0)` |
| 75 | radical | p2_radical_035_讠__retry_2 | 讠 | B3 (R2 PASS) | `yan_speech.py` | `draw_yan_speech(d, ox=0, oy=0, scale=1.0)` |
| 76 | radical | p2_radical_020_阝__retry_2 | 阝 | B3 (R2 PASS) | `er_ear.py` | `draw_er_ear(d, ox=0, oy=0, scale=1.0)` |
| 77 | radical | p2_radical_060_宀__retry_2 | 宀 | B3 (R2 PASS) | `mian_roof.py` | `draw_mian_roof(d, ox=0, oy=0, scale=1.0)` |
| 78 | radical | p2_radical_061_女__retry_2 | 女 | B3 (R2 PASS) | `nu_woman.py` | `draw_nu_woman(d, ox=0, oy=0, scale=1.0)` |
| 79 | radical | p2_radical_123_韦__retry_1 | 韦 | B4 (retry PASS) | `wei_leather.py` | `draw_wei_leather(d, ox=0, oy=0, scale=1.0)` |
| 80 | radical | p2_radical_116_礻__retry_2 | 礻 | B4 (R2 PASS) | `shi_spirit.py` | `draw_shi_spirit(d, ox=0, oy=0, scale=1.0)` |
| 81 | radical | p2_radical_088_长__retry_2 | 长 | B4 (R2 PASS) | `chang_long.py` | `draw_chang_long(d, ox=0, oy=0, scale=1.0)` |
| 82 | char    | p3_char_0045_上 | 上 | B4 | `shang_up.py` | `draw_shang(d, ox=0, oy=0, scale=1.0)` |
| 83 | char    | p3_char_0053_下 | 下 | B4 | `xia_down.py` | `draw_xia(d, ox=0, oy=0, scale=1.0)` |
| 84 | char    | p3_char_0055_三 | 三 | B4 | `san_three.py` | `draw_san(d, ox=0, oy=0, scale=1.0)` |
| 85 | char    | p3_char_0075_千 | 千 | B4 | `qian_thousand.py` | `draw_qian(d, ox=0, oy=0, scale=1.0)` |
| 86 | char    | p3_char_0052_亡 | 亡 | B4 | `wang_gone.py` | `draw_wang_gone(d, ox=0, oy=0, scale=1.0)` |
| 87 | char    | p3_char_0039_之 | 之 | B4 | `zhi_this.py` | `draw_zhi_this(d, ox=0, oy=0, scale=1.0)` |
| 88 | char    | p3_char_0089_义__retry_1 | 义 | B6 **A** (retry) | `yi_x.py` | `draw_yi_x(d, ox=0, oy=0, scale=1.0)` |
| 89 | char    | p3_char_0134_化 | 化 | B6 | `hua_change.py` | `draw_hua(d, ox=0, oy=0, scale=1.0)` |
| 90 | char    | p3_char_0140_反 | 反 | B6 | `fan_reverse.py` | `draw_fan(d, ox=0, oy=0, scale=1.0)` |
| 91 | char    | p3_char_0152_元 | 元 | B6 | `yuan_first.py` | `draw_yuan(d, ox=0, oy=0, scale=1.0)` |
| 92 | char    | p3_char_0174_主 | 主 | B6 | `zhu_lord.py` | `draw_zhu(d, ox=0, oy=0, scale=1.0)` |
| 93 | char    | p3_char_0182_正 | 正 | B6 | `zheng_correct.py` | `draw_zheng(d, ox=0, oy=0, scale=1.0)` |
| 94 | char    | p3_char_0162_生 | 生 | B6 | `sheng_born.py` | `draw_sheng(d, ox=0, oy=0, scale=1.0)` |
| 95 | char    | p3_char_0176_平 | 平 | B6 | `ping_flat.py` | `draw_ping(d, ox=0, oy=0, scale=1.0)` |
| 96 | char    | p3_char_0184_业 | 业 | B7 **A** | `yi_ye.py` | `draw_yi_ye(d, ox=0, oy=0, scale=1.0)` |
| 97 | char    | p3_char_0185_仟 | 仟 | B7 **A** | `qian_person.py` | `draw_qian_person(d, ox=0, oy=0, scale=1.0)` |
| 98 | char    | p3_char_0201_冉 | 冉 | B7 **A** | `ran.py` | `draw_ran(d, ox=0, oy=0, scale=1.0)` |
| 99 | char    | p3_char_0224_乓 | 乓 | B7 **A** | `ping_pang.py` | `draw_ping_pang(d, ox=0, oy=0, scale=1.0)` |
| 100 | char   | p3_char_0198_立 | 立 | B7 | `li_stand.py` | `draw_li_stand(d, ox=0, oy=0, scale=1.0)` |
| 101 | char   | p3_char_0206_白 | 白 | B7 | `bai_white.py` | `draw_bai_white(d, ox=0, oy=0, scale=1.0)` |
| 102 | char   | p3_char_0204_由 | 由 | B7 | `you_by.py` | `draw_you_by(d, ox=0, oy=0, scale=1.0)` |
| 103 | char   | p3_char_0210_四 | 四 | B7 | `si_four.py` | `draw_si_four(d, ox=0, oy=0, scale=1.0)` |
| 104 | char   | p3_char_0231_会 | 会 | B7 | `hui_meet.py` | `draw_hui_meet(d, ox=0, oy=0, scale=1.0)` |
| 105 | char   | p3_char_0221_有 | 有 | B7 | `you_have.py` | `draw_you_have(d, ox=0, oy=0, scale=1.0)` |
| 106 | char   | p3_char_0227_年 | 年 | B7 | `nian_year.py` | `draw_nian_year(d, ox=0, oy=0, scale=1.0)` |
| 107 | char   | p3_char_0229_自 | 自 | B7 | `zi_self.py` | `draw_zi_self(d, ox=0, oy=0, scale=1.0)` |
| 108 | char   | p3_char_0194_世 | 世 | B7 | `shi_world.py` | `draw_shi_world(d, ox=0, oy=0, scale=1.0)` |
| 109 | stroke | p3_char_0245_多 (DEVIATION) | 横撇-slim | B8 | `heng_pie_slim.py` | `draw_heng_pie_slim(d, head, tail, apex_x, corner_x, bow_perp=6, w_head=6, w_tail=3)` |
| 110 | char   | p3_char_0234_亚 | 亚 | B8 | `ya_asia.py` | `draw_ya_asia(d, ox=0, oy=0, scale=1.0)` |
| 111 | char   | p3_char_0235_后 | 后 | B8 | `hou_after.py` | `draw_hou_after(d, ox=0, oy=0, scale=1.0)` |
| 112 | char   | p3_char_0237_行 | 行 | B8 | `xing_walk.py` | `draw_xing_walk(d, ox=0, oy=0, scale=1.0)` |
| 113 | char   | p3_char_0245_多 | 多 | B8 | `duo_many.py` | `draw_duo_many(d, ox=0, oy=0, scale=1.0)` |
| 114 | char   | p3_char_0249_同 | 同 | B8 | `tong_same.py` | `draw_tong_same(d, ox=0, oy=0, scale=1.0)` |
| 115 | char   | p3_char_0259_回 | 回 | B8 | `hui_return.py` | `draw_hui_return(d, ox=0, oy=0, scale=1.0)` |
| 116 | char   | p3_char_0257_问 | 问 | B8 | `wen_ask.py` | `draw_wen_ask(d, ox=0, oy=0, scale=1.0)` |
| 117 | char   | p3_char_0269_合 | 合 | B8 | `he_together.py` | `draw_he_together(d, ox=0, oy=0, scale=1.0)` |
| 118 | char   | p3_char_0284_龹 | 龹 | B9 **A** | `juan_yong.py` | `draw_juan_yong(d, ox=0, oy=0, scale=1.0)` |
| 119 | char   | p3_char_0305_还 | 还 | B9 **A** | `hai_still.py` | `draw_hai_still(d, ox=0, oy=0, scale=1.0)` |
| 120 | char   | p3_char_0313_位 | 位 | B9 **A** | `wei_position.py` | `draw_wei_position(d, ox=0, oy=0, scale=1.0)` |
| 121 | char   | p3_char_0320_伾 | 伾 | B9 **A** | `pi_flourish.py` | `draw_pi_flourish(d, ox=0, oy=0, scale=1.0)` |
| 122 | char   | p3_char_0247_军 R1 | 军 | B9 | `jun_army.py` | `draw_jun_army(d, ox=0, oy=0, scale=1.0)` |
| 123 | char   | p3_char_0271_老 R1 | 老 | B9 | `lao_old.py` | `draw_lao_old(d, ox=0, oy=0, scale=1.0)` |
| 124 | char   | p3_char_0243_成 R1 | 成 | B9 | `cheng_become.py` | `draw_cheng_become(d, ox=0, oy=0, scale=1.0)` |
| 125 | char   | p3_char_0293_来 | 来 | B9 | `lai_come.py` | `draw_lai_come(d, ox=0, oy=0, scale=1.0)` |
| 126 | char   | p3_char_0299_里 | 里 | B9 | `li_inside.py` | `draw_li_inside(d, ox=0, oy=0, scale=1.0)` |
| 127 | char   | p3_char_0295_时 | 时 | B9 | `shi_time.py` | `draw_shi_time(d, ox=0, oy=0, scale=1.0)` |
| 128 | char   | p3_char_0301_作 | 作 | B9 | `zuo_make.py` | `draw_zuo_make(d, ox=0, oy=0, scale=1.0)` |
| 129 | char   | p3_char_0324_但 | 但 | B9 | `dan_but.py` | `draw_dan_but(d, ox=0, oy=0, scale=1.0)` |
| 130 | char   | p3_char_0334_佔 | 佔 | B10 **A** | `zhan_occupy.py` | `draw_zhan_occupy(d, ox=0, oy=0, scale=1.0)` |
| 131 | char   | p3_char_0348_佟 | 佟 | B10 **A** | `dong_person.py` | `draw_dong_person(d, ox=0, oy=0, scale=1.0)` |
| 132 | char   | p3_char_0352_佥 | 佥 | B10 **A** | `qian_all.py` | `draw_qian_all(d, ox=0, oy=0, scale=1.0)` |
| 133 | char   | p3_char_0359_的 | 的 | B10 **A** | `de_target.py` | `draw_de_target(d, ox=0, oy=0, scale=1.0)` |
| 134 | char   | p3_char_0360_並 | 並 | B10 **A** | `bing_and.py` | `draw_bing_and(d, ox=0, oy=0, scale=1.0)` |
| 135 | char   | p3_char_0365_和 | 和 | B10 **A** | `he_harmony.py` | `draw_he_harmony(d, ox=0, oy=0, scale=1.0)` |
| 136 | char   | p3_char_0383_些 | 些 | B10 **A** | `xie_some.py` | `draw_xie_some(d, ox=0, oy=0, scale=1.0)` |
| 137 | char   | p3_char_0357_花 | 花 | B10 | `hua_flower.py` | `draw_hua_flower(d, ox=0, oy=0, scale=1.0)` |
| 138 | char   | p3_char_0363_国 | 国 | B10 | `guo_country.py` | `draw_guo_country(d, ox=0, oy=0, scale=1.0)` |
| 139 | char   | p3_char_0373_者 | 者 | B10 | `zhe_person.py` | `draw_zhe_person(d, ox=0, oy=0, scale=1.0)` |
| 140 | char   | p3_char_0377_法 | 法 | B10 | `fa_law.py` | `draw_fa_law(d, ox=0, oy=0, scale=1.0)` |
| 141 | char   | p3_char_0381_定 | 定 | B10 | `ding_fix.py` | `draw_ding_fix(d, ox=0, oy=0, scale=1.0)` |
| 142 | char   | p3_char_0347_证 | 证 | B10 | `zheng_prove.py` | `draw_zheng_prove(d, ox=0, oy=0, scale=1.0)` |
| 143 | char   | p3_char_0353_找 | 找 | B10 | `zhao_seek.py` | `draw_zhao_seek(d, ox=0, oy=0, scale=1.0)` |
| 144 | char   | p3_char_0371_所 | 所 | B10 | `suo_place.py` | `draw_suo_place(d, ox=0, oy=0, scale=1.0)` |
| 145 | char   | p3_char_0345_志 | 志 | B10 | `zhi_will.py` | `draw_zhi_will(d, ox=0, oy=0, scale=1.0)` |
| 146 | char   | p3_char_0329_运 R1 | 运 | B10 **A** (retry) | (attempts/p3_char_0329_运__retry_1/generated.py — inline template, not wrapped) | — |
| 147 | char   | p3_char_0387_果 | 果 | B11 **A** | `guo_fruit.py` | `draw_guo_fruit(d, ox=0, oy=0, scale=1.0)` |

## PROMOTED B11 as inline templates only (not wrapped as bank .py; access via attempts/)

Only **果 (guo_fruit)** was wrapped as an exemplar of the X-crossing
family unlock (novel structural pattern where interior 竖 pierces
both 田 AND 木 shaft — high downstream reuse for 巢/棵/裸/课/颗).
The other 8 A verdicts + 6 high-reuse PASSes are promoted as inline
templates via the attempt-file path — this follows the B7/B10
convention where character-specific compositions live in `attempts/`
and are surfaced via drawer_memory retrieval hints. This avoids
bank bloat while preserving the recipe-as-reference reuse pattern
that drawers actually use at Phase-3 depth (per B9 sandbox: chars
mostly re-inline from MMH anchors rather than identity-call
wrappers at this depth).

| # | Item | Attempt path | Reuse target |
|---|------|--------------|--------------|
| 148 | p3_char_0392_佯 (A) | `attempts/p3_char_0392_佯/generated.py` | 亻+X 8-stroke where X grid-like (extends 仟). P-A-007-v2 clause-1 exemplar (ren_left scale 0.977 within 5%). |
| 149 | p3_char_0397_空 (A) | `attempts/p3_char_0397_空/generated.py` | 穴-family (穹/穿/窗/窝/究). P-A-006/007 blend: skipped BOTH mian_roof AND gong_work with quant math. |
| 150 | p3_char_0399_往 (A) | `attempts/p3_char_0399_往/generated.py` | 彳/亻+主-like right-half L-R (征/彼/律/得/待). P-A-007-v2 clause-2 exemplar. |
| 151 | p3_char_0404_佼 (A) | `attempts/p3_char_0404_佼/generated.py` | 亻+交-family (校/较/绞/狡). ren_left called + 交 inlined. |
| 152 | p3_char_0406_佽 (A) | `attempts/p3_char_0406_佽/generated.py` | 亻+冫+欠 triple-vertical (次/资 sibling). Refused ren_left AND qian_owe on aspect; heng_gou primitive for s6. |
| 153 | p3_char_0411_受 (A) | `attempts/p3_char_0411_受/generated.py` | 爫+冖+又 stacked (授/爱-simplified). Mixed bank-CALL (zhao_claw_top+mi_cover) + inline (又 too flat). |
| 154 | p3_char_0412_來 (A) | `attempts/p3_char_0412_來/generated.py` | Traditional 來 8-stroke. Wait for 2nd P-COMP-002 DEVIATION before wrapping as lai_traditional.py. |
| 155 | p3_char_0413_采 (A) | `attempts/p3_char_0413_采/generated.py` | 爫+木 compressed (彩/菜/採). Mixed bank (zhao_claw_top) + inline (木 flat). |
| 156 | p3_char_0395_金 (PASS) | `attempts/p3_char_0395_金/generated.py` | 钅-radical L-R base (钟/钢/铁/银/铜) + 金-bottom (鑫/釜). HIGH REUSE. Wrap when B12 exposes 2nd 金-family compound. |
| 157 | p3_char_0389_话 (PASS) | `attempts/p3_char_0389_话/generated.py` | 讠+舌 template; extends zheng_prove for 舌-family. |
| 158 | p3_char_0421_或 (PASS) | `attempts/p3_char_0421_或/generated.py` | 戈+口 template; extends xie_gou family (成/戎/戒/我 sibling). |
| 159 | p3_char_0423_苦 (PASS) | `attempts/p3_char_0423_苦/generated.py` | 艹+古 template; bottom-radical variant of hua_flower. |
| 160 | p3_char_0419_知 (PASS) | `attempts/p3_char_0419_知/generated.py` | 矢+口 template; 矢-left family (短/矫). |
| 161 | p3_char_0425_具 (PASS) | `attempts/p3_char_0425_具/generated.py` | 目+一+八 stacked; 目-family (真/直/县 sibling). |

**Total B11 promotions**: 15 (1 wrapped + 14 inline-template) — bank
grows 152 → 167 by count, 152 → 153 by wrapper-file count.

**Reuse-target map for B12 (idx 434-483)**:
- 亻+X compounds: use guo_fruit precedent for X-crossing; 佼/佯 for L-R clean.
- 讠 family: reference #157 hua_speech (讠+舌 template).
- 戈 family: reference #158 huo_maybe (戈+口) + zhao_seek (扌+戈).
- 艹 family: hua_flower (top) or #159 ku_bitter (bottom).
- 目 family: reference #161 ju_tool.
- 矢 family: reference #160 zhi_know.
- 钅 family: reference #156 jin_gold (wrap on 2nd sighting).

## PASSed in B11 but NOT promoted separately (idx 384-433)

Phase-3 chars that PASSed via P-A-006 stroke-primitive composition or
identity-reuse of existing bank primitives; kept inline for pass_index
/ retrieval-example use:
- p3_char_0385_物 (牛+勿; niu_cow-side variant, 勿 inline)
- p3_char_0390_佬 (亻+老; both bank primitives available and used)
- p3_char_0394_佰 (亻+百; 亻 bank, 百 inline)
- p3_char_0398_併 (亻+并; 亻 bank, 并 inline)
- p3_char_0400_佶 (亻+吉; 亻 bank, 吉 inline)
- p3_char_0409_油 (氵+由; both bank: sanshui + you_by)
- p3_char_0414_侈 (亻+多; both bank: ren_left + duo_many)
- p3_char_0417_单 (unique top-cross frame; inline)
- p3_char_0422_侍 (亻+寺; 亻 bank, 寺 inline via zhu_lord partial)
- p3_char_0424_侑 (亻+有; both bank: ren_left + you_have)
- p3_char_0428_侖 (traditional 侖; inline)
- p3_char_0430_畈 (田+反; both bank: ri_sun-adapted + fan_reverse)
- p3_char_0432_畋 (田+攵; both bank: ri_sun-adapted + pu_action)

## Not promoted from B11 (C/FAIL, terminal-freeze or do-not-queue)

**Main FAILs (19)** clustered per B11 postmortem:
- **Cluster A — 疒-family bank gap (terminal-freeze)** (1): 疡.
- **Cluster B — 亻+X hook-compound right / 3-part vertical** (5):
  佾 (亻+八+月; B12 R1 candidate — 3-DEVIATION but 2 sub-components
  are compact, worth quant-recheck by P-A-010 rule if reclassified),
  侃 (do-not-queue), 侉 (do-not-queue P-COMP-011), 侌 (do-not-queue),
  侔 (B12 R1 MEDIUM — 亻+niu_cow both called; interior 厶 recheck).
- **Cluster C — L-R with no bank for either half (do-not-queue)** (5):
  取, 规, 亟, 转, 例 (B12 R1 MEDIUM: 例 has dao_right P-A-007 recheck lever).
- **Cluster D — top-radical aspect-mismatch queueable (B12 R1)** (3):
  实 (mian_roof P-A-007-v3 recheck), 治 (kou_mouth recheck),
  放 (pu_action recheck).
- **Cluster E — L-R complex hook-compound** (3):
  说 (讠+兑, do-not-queue), 线 (纟+戋, do-not-queue),
  是 (日+龰, do-not-queue — format ceiling).
- **Cluster F — Traditional / 覀 top** (2):
  亞 (do-not-queue — no traditional-8-stroke path),
  要 (do-not-queue — 覀 top no bank).

**Main C's (3)** — no retries queued per P-COMP-006 unless P-A-010
classification says queue: 表 (391), 佴 (396), 佻 (402). All
do-not-queue at this pass.

**R1 outcomes from B10 queue (4)** — all FAILed at R1:
- 社 R1 FAIL — P-A-010 kind (d) classification retrospect: L-R spacing
  problem not addressable by primitive-call R1.
- 佞 R1 FAIL — P-A-010 kind (d) classification retrospect: 3-part
  vertical spacing.
- 畅 R1 FAIL — P-A-010 kind (e) retrospect: trajectory-diff on wrong
  primitive; drawer inlined fresh 申 anyway.
- 经 R1 FAIL — P-A-010 kind (e) retrospect: multi-DEVIATION with
  correct math; composition-level failure.

Terminal-freeze all 4 (2 rounds no PASS). See errata.md B11 postmortem
for full R1 diagnosis.

See `errata.md` and `sandbox.md` (B11 postmortem).

## PASSed in B10 but NOT promoted separately (idx 334-383)

Phase-3 chars that PASSed via P-A-006 stroke-primitive composition or
identity-reuse of existing bank primitives (kept inline for pass_index
/ retrieval-example use):
- p3_char_0335_别 (刂+另 — dao_right + inline)
- p3_char_0336_佗 (亻+它 — inline; hook body in 它 handled by shu_wan_gou)
- p3_char_0344_佝 (亻+句 — inline; 句 has heng_zhe_gou bank primitive)
- p3_char_0350_佣 (亻+用 — inline; 用 has moderate reuse)
- p3_char_0354_佧 (rare 亻+卡 — inline)
- p3_char_0356_皃 (rare 白+儿 — inline)
- p3_char_0358_盯 (目+丁 — inline; 目 has bank ri_sun sibling)
- p3_char_0364_畀 (田+丌 — inline)
- p3_char_0369_其 (inline stroke composition — kept inline)
- p3_char_0351_步 (止+少 — inline P-A-006 layer)
- p3_char_0329_运 R1 **A** — inline template preserved in
  `attempts/p3_char_0329_运__retry_1/generated.py`. Uses draw_chuo +
  draw_pie_zhe + draw_heng + draw_dian. **Trajectory-diff A recipe**:
  fixed 云 s3 (called draw_pie_zhe with corner at (140, 210) instead
  of inlining collapsed diagonal). 云-family template also covers
  会/合/回 top variants where the outer 厶/口 has a similar closure.

## PASSed in B9 but NOT promoted separately (idx 284-333)

10 additional B9 mains PASSed but kept inline (kept for pass_index /
retrieval-example use):
- p3_char_0290_甸 (勹+田 wrap; uses bao_wrap + inline 田)
- p3_char_0291_这 (辶+文 wrap; BANK_DEVIATION vs wen_text/chuo_walk;
  inline per P-A-007 clause 2)
- p3_char_0294_町 (田+丁; inline stroke-primitive)
- p3_char_0296_串 (2 stacked kou + central shu; all bank primitives fit)
- p3_char_0298_丽 (BANK_DEVIATION on heng_zhe_short; narrow compartment)
- p3_char_0300_乱 (甲+乚; shu_wan_gou at native scale)
- p3_char_0308_亩 (亠+田; stroke-primitive layer)
- p3_char_0310_伯 (亻+白 — bai_white in bank but drawer inlined per P-A-006)
- p3_char_0316_伺 (亻+司; heng_zhe_gou bank primitive handled outer 4-anchor)
- p3_char_0322_佃 (亻+田 stroke-primitive)
- p3_char_0325_状 (丬+犬 side-radical stroke-primitive)
- p3_char_0330_佉 (BANK_DEVIATION vs tu_earth; compressed right-half)
- p3_char_0332_佐 (亻+左 stroke-primitive)

## Not promoted from B9 (C/FAIL, terminal-freeze or do-not-queue)

**Main FAILs (17)**:
- **Cluster A — 亻+X hook-compound right (P-COMP-011/012 do-not-queue)** (6):
  你 (亻+尔 hooks), 伶 (亻+令 hooks), 伽 (亻+力+口), 佇 (亻+宁 shu_gou),
  佈 (亻+布 heng_zhe_gou+shu_gou), 员 (口+贝 hooks) — none have available
  mechanism-change.
- **Cluster B — chronic-freeze recycles** (2): 亨 (G3 already terminal-frozen),
  声 (G3 already terminal-frozen; recycled for G5, still FAIL).
- **Cluster C — 3-part / crossbar composition** (3): 没 (氵+殳),
  两 (top+2-cell frame with X-crosses), 亩 (actually PASS; miscounted)
  → correct: 没, 两, 冱 (冫+互 crossbar).
- **Cluster D — hook-body / long-descender full char** (4): 身 (7-stroke frame + descender),
  凫 (top wrap + 几-frame; no bank), 更 (帀+又-like descender), 条 (夂+木 descender).
- **Cluster E — 3-radical L-M-R with hook** (1): 听 (口+斤 — narrow 口 left
  + 斤 has straight strokes but composition tight); 运 (云+辶 — draw_chuo
  called but 云 s3 pie-zhe curl unresolved).
- **Cluster F — 3-part vertical** (1): 317 员 (口+贝 hooks).

**Main C's (11)** — no retries queued per P-COMP-006 unless mechanism-change:
师, 光, 我, 甹, 疔, 进, 疖, 伲, 把, 形, 识.

**R1 FAILs (4)** — terminal-freeze candidates: 名, 西, 好, 再 (2 rounds FAIL).

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B9 postmortem).

## PASSed in B8 but NOT promoted separately (Phase-3 chars idx 234-283 reusing existing bank primitives or P-A-006 template-only)

Phase-3 chars that PASSed via stroke-primitive composition (P-A-006
template documented in principle_bank / drawer_memory rather than as a
wrapper): p3_char_0239_过 (辶+寸 wrap; uses draw_chuo_walk), p3_char_0242_仲
(亻+中), p3_char_0244_仳 (亻+比; identity of B7 比 R1 pattern), p3_char_0246_仵
(亻+午), p3_char_0251_当, p3_char_0252_伊 (亻+尹), p3_char_0255_此 (止+匕
both in bank), p3_char_0256_伐 (亻+戈), p3_char_0262_伛 (亻+区),
p3_char_0268_伦 (亻+仑), p3_char_0275_任 (亻+壬). All are P-A-006
stroke-primitive layer with MMH-verbatim anchors; template lives in
drawer_memory B7 P-A-006 playbook.

## Not promoted from B8 (C/FAIL, terminal-freeze or do-not-queue)

**Main FAILs (20)** clustered A-E per errata:
- **Cluster A — 亻+X hook-compound right (P-COMP-011; do-not-queue)** (7):
  伄, 伉, 伎, 伙, 伢, 伧, 佤
- **Cluster B — whole-radical refusal (P-A-007; B9 R1 queue)** (4):
  军, 名, 成, 西
- **Cluster C — chronic-freeze (terminal-freeze)** (3): 亥, 色, 传
- **Cluster D — 女-inline** (2): 好 (B9 R1 P-A-007), 如 (do-not-queue)
- **Cluster E — hook-body full-char** (4): 仰 (do-not-queue), 再 (B9 R1),
  老 (B9 R1 P-RET-004 tuning), 设 (terminal-freeze)

**Main C's (10)**: 亦, 伕, 她, 伥, 伪, 伫, 先, 齐, 兆, 兇 — no retries queued
per P-COMP-006 unless a P-A-007-style mechanism-change appears.

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B8 postmortem).

## PASSed in B7 but NOT promoted separately (Phase-3 chars idx 184-233 reusing existing bank primitives or low-reuse)

Phase-3 chars that PASSed via stroke-primitive composition already
covered by existing bank primitives (no new bank entry needed):
- p3_char_0186_本 (BANK_DEVIATION on mu_wood — 木-variant for 本; awaiting 2nd DEVIATION per P-COMP-002)
- p3_char_0189_仨 (亻 inline + 三 inline — L-R composition template; kept inline)
- p3_char_0190_加 (BANK_DEVIATION on li_power — 力-variant for 加 L-R placement; awaiting 2nd DEVIATION)
- p3_char_0192_代 (亻+弋 L-R composition; stroke primitives cover)
- p3_char_0195_皿 (shu + heng_zhe_box + 2 shus + heng — bottom-radical, moderate-reuse; kept inline)
- p3_char_0197_矢 (dian + pie + heng + heng + na — X-cross cluster PASS)
- p3_char_0199_兰 (dian + pie + 3 hengs — stroke composition)
- p3_char_0200_市 (dian + heng + short-shu + heng_zhe_gou + long-shu — moderate reuse)
- p3_char_0202_术 (draw_mu identity + dian — P-A-001)
- p3_char_0203_冊 (5 strokes inline; low-freq variant of 册)
- p3_char_0208_北 (short-pie/dian variants — sibling of 比)
- p3_char_0211_冯 (BANK_DEVIATION for 马-body inline; 马 known chronic gap)
- p3_char_0215_凸 (BANK_DEVIATION zigzag inline — character-specific)
- p3_char_0216_失 (heng + heng + pie + na — X-cross cluster PASS)
- p3_char_0217_凹 (BANK_DEVIATION inline polylines — character-specific)
- p3_char_0219_在 (heng + shu + pie + shu + heng — inline; 土+才-like)
- p3_char_0220_丢 (pie + heng + heng + shu + dian — inline; sibling 去)
- p3_char_0222_乑 (multi-pie composition inline)
- p3_char_0225_而 (heng + pie + shu + heng_zhe_gou + 2 shus — moderate reuse; kept inline)
- p3_char_0226_乔 (2 pies + shu-hook + na + pie/dian — stroke composition)
- p3_char_0228_乩 (X-cross cluster PASS; 占+乚 composition)
- p3_char_0230_亘 (heng + shu + heng_zhe_box variant + hengs — sibling of 亙)
- p3_char_0232_亙 (BANK_DEVIATION near-straight pie s2 — 亘 variant)
- p3_char_0168_用__retry_1 (retry PASS; 用 = pie + heng_zhe_gou + heng + shu + shu — kept inline, moderate reuse — could be promoted if reused again)
- p3_char_0136_比__retry_1 (retry PASS; sibling-pair 匕/匕 — inline)

Special BANK_DEVIATIONs preserved inline but NOT promoted (character-specific,
low general reuse):
- p3_char_0186_本 (`mu_wood_variant_for_本` — proportion shift for root-mark)
- p3_char_0190_加 (`li_variant_for_加` — pie extension shift for L-R)
- p3_char_0193_癶 C (mirror-symmetric footprint — kept inline; X-cross cluster C)
- p3_char_0196_东 FAIL (`dong_spine_diagonal` — bank_deviation for shu_gou-at-diagonal; FAIL, not promoted)
- p3_char_0209_冎 FAIL (rare-char inline; not promoted)
- p3_char_0211_冯 (`ma_body_zigzag_inline` — 马-body deviant; keep in sandbox)
- p3_char_0215_凸 (`tu_right_compound_zigzag` — character-specific)
- p3_char_0217_凹 (`ao_inline_polylines_v1` — character-specific)
- p3_char_0232_亙 (`yun_left_wall_for_亙` — near-straight variant; low reuse)

**Promotion decisions**:
- 13 whole-char promotions (4 A + 9 high-reuse PASSes): 业, 仟, 冉, 乓 (A);
  立, 白, 由, 四, 会, 有, 年, 自, 世 (PASSes with wide phonetic/positional reuse).
- 皿/而/市/术/北/本/加 all PASSed but held off promotion this batch: 皿/而
  candidates for B8 promotion if a compound char (盘/耐) uses them; 术/北
  identity-served by draw_mu + inline; 本/加 have DEVIATION variants awaiting
  2nd occurrence per P-COMP-002.
- **Discovery**: all 5 A verdicts followed a **new recipe P-A-006** —
  MMH-anchor verbatim + stroke-primitive layer (bypassing whole-radical
  primitives). Documented in principle_bank.

## PASSed in B6 but NOT promoted separately (Phase-3 chars idx 134-183 reusing existing bank primitives or low-reuse)

Phase-3 chars that PASSed via identity-call of an existing bank primitive
(no new bank entry needed):
- p3_char_0139_礻 (draw_shi_spirit from B4 retry) — P-A-001 identity
- p3_char_0137_刈 (draw_dao_right + xie-like inline pie — stroke composition)
- p3_char_0142_区 (draw_kou-variant inline + interior 乂 — stroke composition)
- p3_char_0143_勻 (draw_bao_wrap + interior 2 hengs — L/wrap composition)
- p3_char_0145_勿 (draw_bao_wrap + 3 pies — composition)
- p3_char_0147_卅 (3 shus + heng — inline; 廿-like)
- p3_char_0149_升 (pie + heng + heng + shu inline — 千 sibling)
- p3_char_0151_卞 (dian + heng + draw_bu inline — composition)
- p3_char_0157_甲 (draw_ri-like + shu descender — composition)
- p3_char_0158_出 (2x draw_shan-like inline stacked — composition)
- p3_char_0159_申 (draw_ri + shu piercing — composition)
- p3_char_0161_甴 (draw_ri + shu inside — composition)
- p3_char_0164_对 (又+寸 inline L-R composition)
- p3_char_0165_乍 (pie + shu + heng + heng + heng inline)
- p3_char_0167_乎 (pie + 2 dians + heng + wan_gou inline)
- p3_char_0171_疒 (draw_guang variant + dians — composition)
- p3_char_0172_只 (draw_kou + ba-bottom inline)
- p3_char_0173_仔 (draw_ren_left + 子 inline — L-R composition)
- p3_char_0175_仕 (draw_ren_left + draw_shi_scholar — L-R composition)
- p3_char_0178_外 (draw_xi_dusk + draw_bu-variant inline — composition; BANK_DEVIATION on bu_divine)
- p3_char_0181_仝 (draw_ren top + draw_gong_work-variant bottom — stacked composition)
- p3_char_0121_內__retry_1 (draw_shu + draw_heng_zhe_gou + pie + na inline; trajectory-diff PASS)

Special BANK_DEVIATIONs preserved inline but NOT promoted (character-specific,
low general reuse):
- p3_char_0146_队 (`er_ear_for_left_position` compact ear variant — awaiting
  2nd DEVIATION per P-COMP-002)
- p3_char_0148_书 (`shu_book_body` cursive body — 书-specific)
- p3_char_0156_们 (narrower 门 variant — could inform future L-R 门 shrink but
  low reuse; keep inline)
- p3_char_0166_去 (compressed 土 top — could inform 土 top-position variant;
  awaiting 2nd DEVIATION)

**Promotion decisions**:
- 8 whole-char primitives promoted (yi_x, hua_change, fan_reverse, yuan_first,
  zhu_lord, zheng_correct, sheng_born, ping_flat) — all high-reuse per
  compound-derived family maps documented in each file's docstring.
- Retry A (义) source: `attempts/p3_char_0089_义__retry_1/generated.py`.
  First-ever A verdict from the retry channel; recipe codified as P-A-005.

## PASSed in B5 but NOT promoted separately (Phase-3 chars idx 084-133 reusing existing bank primitives)

Phase-3 chars that PASSed via identity-call of an existing bank primitive
(no new bank entry needed):
- p3_char_0084_屮 (draw_shu + inline heng-with-hook) — identity + stroke bank
- p3_char_0087_工 (draw_gong_work from B1) — P-A-001 identity
- p3_char_0092_廾 (heng + shu + pie inline — sibling of p2 廾)
- p3_char_0093_弋 (dian + xie_gou from B2 stroke bank)
- p3_char_0094_不 (heng + pie + shu + dian — stroke composition)
- p3_char_0095_丹 (heng_zhe_gou + shu + dian + heng — stroke composition)
- p3_char_0096_为 (dian + heng_pie + heng_zhe_wan_gou inline BANK_DEVIATION)
- p3_char_0100_中 (kou + shu — identity-ish; sibling family)
- p3_char_0101_亓 (heng + shu + pie inline)
- p3_char_0102_天 (heng + heng + pie + na — stroke composition; declines draw_da due to anchor mismatch)
- p3_char_0104_方 (dian + heng + heng_zhe_gou + pie — stroke composition)
- p3_char_0105_仂 (draw_ren_left + draw_heng_zhe_gou + heng — L-R composition)
- p3_char_0106_日 (draw_ri from B2) — P-A-001 identity
- p3_char_0109_仄 (draw_ren_left underneath draw_chang_cliff — L-R composition)
- p3_char_0110_分 (draw_ba compressed + draw_dao 2-stroke variant — stroke composition)
- p3_char_0112_心 (dian + wo_gou_inline + dian + dian — BANK_DEVIATION → PROMOTED wo_gou.py)
- p3_char_0115_仌 (draw_ren top + draw_ren bottom)
- p3_char_0116_公 (draw_ba + draw_si-shape below)
- p3_char_0118_从 (2x draw_pie + 2x draw_na asymmetric BANK_DEVIATION inline — not promoted, low reuse)
- p3_char_0122_五 (heng + pie + heng_zhe_wide inline + heng — BANK_DEVIATION → PROMOTED heng_zhe_wide.py)
- p3_char_0124_文 (draw_wen from B3) — P-A-001 identity (expected A per P-A-001; got PASS per P-A-003)
- p3_char_0125_円 (draw_shu + draw_heng_zhe_gou + 2x heng inside — 円 = 円/圆 shape)
- p3_char_0126_长 (draw_chang_long from B4 retry) — P-A-001 identity
- p3_char_0127_冈 (shu + heng_zhe_gou + pie + na — stroke composition)
- p3_char_0128_太 (heng + pie + na + dian — sibling of 大)
- p3_char_0129_龶 (heng + heng + heng + shu — stroke composition, sibling of 三/王)
- p3_char_0132_内 (shu + heng_zhe_gou + pie + na — stroke composition)

**Promotion decisions**:
- `wo_gou.py` PROMOTED (per P-RET-003 proactive promotion; 心-family reuse targets: 必/忘/忙/志/思/念/忽/恕).
- `heng_zhe_wide.py` PROMOTED (per P-RET-003 proactive promotion; 五/亚/世/巫-family reuse).
- 从's `cong_two_ren_asymmetric` — NOT promoted (character-specific asymmetry; low general reuse).
- No whole-char primitive promoted for any B5 PASS: 天/内/文/日 either identity-call an existing bank entry or are compositions already covered by stroke primitives.

## PASSed in B4 but NOT promoted separately (Phase-3 characters that reused existing bank primitives cleanly, or low-reuse retry PASSes)

Phase-3 chars that PASSed via identity-call of an existing bank radical primitive
(no new bank entry needed — the char IS the radical):
- p3_char_0037_勹 (draw_bao from bootstrap) — P-A-001 identity
- p3_char_0038_匕 (draw_bi from bootstrap) — P-A-001 identity
- p3_char_0041_大 (draw_da from B1) — P-A-001 identity
- p3_char_0057_小 (draw_xiao from B2) — P-A-001 identity
- p3_char_0063_门 (draw_men_gate from B3) — P-A-001 identity
- p3_char_0066_囗 (draw_wei from B2) — P-A-001 identity
- p3_char_0067_山 (draw_shan from B1) — P-A-001 identity
- p3_char_0069_干 (draw_gan from B1) — P-A-001 identity
- p3_char_0071_口 (draw_kou from B1) — P-A-001 identity
- p3_char_0080_宀 (draw_mian_roof from B3) — P-A-001 identity
- p3_char_0081_女 (draw_nu_woman from B3) — P-A-001 identity
- p3_char_0078_艹 (draw_cao from B1) — P-A-001 identity
- p3_char_0068_纟 (composed via pie_zhe/pie_zhe/ti stroke primitives)
- p3_char_0042_丬 (pie+ti+shu — no separate primitive needed)
- p3_char_0043_个 (pie+na+shu — inline; sibling of 人)
- p3_char_0040_丫 (pie+dian+shu — inline)
- p3_char_0054_亼 (dian+pie+na — inline)
- p3_char_0056_亾 (BANK_DEVIATION shu_zhe-style s3 — inlined; low reuse)
- p3_char_0062_卄 (2 hengs + 2 shus — inline)
- p3_char_0064_叉 (heng_pie+na+dian — inline; sibling of 又)
- p3_char_0074_孑 (BANK_DEVIATION heng_pie inline — logged as promotion candidate in sandbox)
- p3_char_0076_孓 (heng_pie+wan_gou+heng — inline, sibling of 孑)
- p3_char_0077_习 (heng_zhe_gou variant + dian + dian — inline)

Low-reuse retry PASSes NOT promoted (available inline in `attempts/`):
- p2_radical_121_尣__retry_1 (尣) — low-freq wang-variant
- p2_radical_125_毋__retry_1 (毋) — low-freq (mostly standalone; 毒 uses it)

## PASSed in B3 but NOT promoted separately (Phase-3 characters that reused existing bank primitives cleanly)

Phase-3 chars that PASSed via identity-call of an existing bank radical primitive
(no new bank entry needed):
- p3_char_0011_人 **A** (draw_ren from B1) — first A verdict; validates P-RET-002
- p3_char_0017_又 **A** (draw_you from B1) — first A verdict; validates P-RET-002
- p3_char_0029_入 (draw_ru from B1)
- p3_char_0022_亻 (draw_ren_left from B1)
- p3_char_0025_力 (draw_li from B1)
- p3_char_0028_冖 (draw_mi_cover from B1)
- p3_char_0020_亠 (draw_tou from B1)
- p3_char_0030_冫 (draw_bing from bootstrap)
- p3_char_0031_厂 (draw_chang from bootstrap)
- p3_char_0032_凵 (draw from inline — same shape as B1)
- p3_char_0033_刀 (draw_dao from bootstrap)
- p3_char_0024_八 (draw_ba from bootstrap)
- p3_char_0013_十 (draw_shi_ten from B1)
- p3_char_0015_二 (draw_er from bootstrap)
- p3_char_0012_丷 (2 dians — inline)
- p3_char_0014_乂 (pie + na — inline)
- p3_char_0001–0010 (single-stroke / 2-stroke chars — all PASSed via stroke bank)

## PASSed in B2 but NOT promoted (low reuse; still-usable inline)

- p2_radical_079_弋 (弋) — low-freq bare-radical; the useful shape was extracted as `xie_gou.py` stroke primitive
- p2_radical_083_丬 (丬) — low-freq; simple pie+ti+shu composition
- p2_radical_091_斗 (斗) — low-freq; simple dian+dian+heng+shu
- p2_radical_036_廴__retry_1 (廴) — enclosing radical; multi-turn top compound + ping_na is drawer-specific,
  and MMH gives a cleaner injection than baking the awkward geometry into a bank fn (revisit if Phase-3 needs it).

## PASSed in B1 but NOT promoted (still-usable inline; low-reuse or specialized)

The following 13 items PASSed but their whole-radical primitive is not
promoted here because either (a) they are unusual shapes with few
composition uses (匚, 匸, 凵, 冂, 屮, 厶, 廾, 彐, 彑 — bracket-family and
odd shapes), (b) they are too similar to an already-promoted primitive
(丷 ≈ inverted 八; 彳 ≈ double-pie left position; 彡 ≈ triple 撇), or (c)
the drawer inlined significant portions with BANK_DEVIATION but the
compound sub-elements are already covered by the promoted stroke bank
(卩 uses inline heng-zhe-gou-like → covered by `heng_zhe_gou.py`).

Attempt code is preserved under `attempts/<item>/generated.py` and remains
readable for future reference.

- p2_radical_019_匚 (匚 fang-bracket) — 2-stroke left bracket; inline OK
- p2_radical_021_丷 (丷 ba-bottom) — 2 dians
- p2_radical_023_卩 (卩 jie) — 2-stroke; heng_zhe_gou variant + shu
- p2_radical_024_冂 (冂 jiong) — shu + heng_zhe_wide (BANK_DEVIATION)
- p2_radical_027_凵 (凵 qu, up-bracket) — BANK_DEVIATION shu_zhe direction inverted
- p2_radical_032_厶 (厶 mou) — BANK_DEVIATION pie-zhe compound + dian
- p2_radical_034_匸 (匸 xi) — heng + BANK_DEVIATION shu_zhe
- p2_radical_040_屮 (屮 che) — BANK_DEVIATION L-shape + shu
- p2_radical_041_彳 (彳 chi-step) — pie + pie + shu (left-position radical, worth revisiting if reuse appears)
- p2_radical_051_廾 (廾 gong-hands) — heng + shu + pie
- p2_radical_054_彐 (彐 ji) — 3-stroke bracket (heng + heng + heng-shaped)
- p2_radical_064_彡 (彡 shan-hair) — 3 pies cascading

## Not promoted (C/FAIL, deferred to B2 retry queue)

- p2_radical_017_儿 (儿) — C (retry_1: C again — MMH-anchor overlap plus shu_wan_gou tuning still not landing)
- p2_radical_003_丿 (丿) — FAIL (retry_1: still FAIL — MMH-vs-GT anchor mismatch)
- p2_radical_020_阝 (阝) — C (BANK_DEVIATION: inline "3-shape" ear was off)
- p2_radical_035_讠 (讠) — C (BANK_DEVIATION: heng_zhe_ti compound)
- p2_radical_036_廴 (廴) — C (BANK_DEVIATION: multi-turn zigzag + ping_na)
- p2_radical_045_寸 (寸) — C
- p2_radical_050_弓 (弓) — C (BANK_DEVIATION: complex bottom hook)
- p2_radical_053_己 (己) — C
- p2_radical_056_巾 (巾) — C
- p2_radical_059_门 (门) — C
- p2_radical_060_宀 (宀) — C
- p2_radical_061_女 (女) — C (BANK_DEVIATION: pie-dian composite)
- p2_radical_065_尸 (尸) — C
- p2_radical_066_饣 (饣) — C
- p2_radical_022_几 (几) — FAIL
- p2_radical_038_㔾 (㔾) — FAIL
- p2_radical_042_巛 (巛) — FAIL
- p2_radical_047_飞 (飞) — FAIL
- p2_radical_055_彑 (彑) — FAIL
- p2_radical_058_马 (马) — FAIL (BANK_DEVIATION: 3-turn zigzag)
- p2_radical_062_犭 (犭) — FAIL

## Not promoted from B3 (C/FAIL, deferred or terminal-freeze)

**Main-channel B3 FAILs (8)**: 水, 瓦, 爪 (Phase-2 radicals with 3-directional
or wrap-around geometry); 乃, 乜, 儿, 几, 九 (Phase-3 hook-family — all missing
heng_zhe_wan_gou-family primitive).

**Main-channel B3 C's (7)**: 尣, 韦, 毋, 心 (needs 卧钩), 牙, 冂 (needs wider
heng_zhe), 七 (needs pie_wan).

**Retry FAILs from B3 (12)**: 攴, 方, 子, 兀, 长, 夂, 夊, 歹, 夕, 比, 纟, 尢.
Several are terminal-freeze candidates.

**Retry C's from B3 (19)**: 氏, 旡, 气, 火, 巳, 见, 贝, 斤, 厄, 耂, 毛, 手, 礻, 片,
寸(R2), 尸(R2), 己(R2), 弓(R2), 几(R2). See `retry_log.jsonl` for B4 queue.

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B3 postmortem).

## Not promoted from B7 (C/FAIL, deferred or terminal-freeze)

**Main-channel B7 FAILs (8)**:
- p3_char_0187_仡 (亻+乞 L-R; 乞's inline 乙-body hook mis-shaped)
- p3_char_0188_边 (辶+力 wrap; chuo_walk + li_power double-transform failure — see P-COMP-004 corollary)
- p3_char_0196_东 (BANK_DEVIATION on shu_gou-at-diagonal; fresh dong_spine_diagonal FAILed)
- p3_char_0209_冎 (rare 5-stroke; layout/anchor mismatch)
- p3_char_0212_处 (5-stroke pie+pie+na+shu+dian; anchor cluster miss)
- p3_char_0213_処 (処 = 夂+几; BANK_DEVIATION full inline; no 夂/几 bank; heng_zhe_wan_gou family)
- p3_char_0214_记 (讠+己; 己's inline hook family unresolved)
- p3_char_0233_那 (冄+阝 6-stroke; er_ear position/scale mismatch on right)

**Main-channel B7 C's (9)**:
- p3_char_0190_加 (L-R placement — li_power baked geometry)
- p3_char_0191_仫 (亻+么; BANK_DEVIATION mo_right_variant OK-but-not-clean)
- p3_char_0193_癶 (mirror-symmetric footprint; near-PASS, close)
- p3_char_0205_冋 (rare 4-stroke)
- p3_char_0207_册 (5-stroke; sibling of 冊 which PASSed)
- p3_char_0211_冯 (冫+马; 马-body inline sub-PASS; sibling of chronic 马 freeze)
- p3_char_0217_凹 (character-specific polylines)
- p3_char_0218_刍 (rare 4-stroke)
- p3_char_0223_地 (土+也; 也 chronic gap — heng_zhe_wan_gou family)

**Retry FAILs from B7 (2)** → terminal-freeze:
- p3_char_0170_发__retry_1 (top-heavy composition still off; specific
  parameter tuning insufficient)
- p3_char_0177_仗__retry_1 (亻+丈 X-cross; pie/na crossing off-anchor)

**Retry C's from B7 (3)** → per P-COMP-006, no mechanism-change available:
- p3_char_0155_必 R1 C (wo_gou belly + 3-dian tuning improved but not PASS)
- p3_char_0179_付 R1 C (扌+寸 L-R proportion improved but not PASS)
- p3_char_0180_打 R1 C (扌+丁 L-R proportion improved but not PASS)

**Retry PASSes from B7 (2)**:
- p3_char_0168_用__retry_1 PASS (moved s1 pie to share top-left with box)
- p3_char_0136_比__retry_1 PASS (sibling-pair discipline: 匕/匕 rebalance
  — validates B6 sibling-pair table for 匕 family)

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B7 postmortem).

## Not promoted from B6 (C/FAIL, deferred or terminal-freeze)

**Main-channel B6 FAILs (8)**:
- **Wave/wraparound cluster** (3): 刅 (刀+2 ticks, 4 strokes — inline heng_zhe_gou
  wrong topology), 水 (4 strokes, 3-directional shu_gou + 3 pies — genuine
  bank gap for calligraphic 水), 发 (5 strokes, top-heavy proportion).
- **Chronic-freeze family, first Phase-3 appearance** (1): 风 (4 strokes,
  needs heng_xie_wan_gou — P-COMP-008 candidate; inline BANK_DEVIATION
  FAILed. Bare 风 was terminal-frozen in B4).
- **L-R proportion cluster** (3): 引 (弓+丨, 4 strokes — 弓 rendered as
  crude polylines, no bank primitive), 他 (亻+也, 5 strokes — 也 requires
  heng_zhe_wan_gou family for top arc), 仗 (亻+丈, 5 strokes — 丈 inline
  proportions off).
- **Rare structure** (1): 丱 (5 strokes; symmetric 丨丨丨丨 with lateral
  ticks — inline BANK_DEVIATION, unusual anchor spread).

**Main-channel B6 C's (10)**: 比, 办, 卬, 必, 可, 168_用, 169_疋, 179_付,
180_打, 183_仞.

**Cluster identification**:
- 必 uses draw_wo_gou; C came from dot placement (fixable via trajectory-diff)
- 打, 付 = 扌+丁/寸 L-R proportion (扌 too wide vs GT); trajectory-diff
- 用 = 4-stroke box + strokes; close proportion
- 疋, 仞 = rare structures, close
- 比 = 匕/双匕 sibling confusion (P-COMP-003 relevant)
- 办, 卬, 可 = each close but off in a specific proportion

**Retry outcomes (14 R1 slots — 2 PASS, 12 FAIL)**:
- **PASSes (2)**: 内 R1 PASS (trajectory-diff for pie head raised above box
  top — worked); 义 R1 **A** (P-A-005 recipe).
- **Terminal-freezes (12, all FAIL at R1 or R2)**:
  - `heng_zhe_wan_gou` family (P-COMP-008 candidate spec failed): 乌 R1,
    仇 R1, 仉 R1, 冗 R1 — spec didn't cash. Composition-level issues also
    at play, not just missing primitive.
  - 马 R1 FAIL — genuinely different 3-turn compound (heng_zhe_zhe_gou
    with down-left hook, not heng_zhe_wan_gou); no bank primitive fits.
  - Trajectory-diff FAILs: 予 R1, 亢 R1, 以 R1, 见 R1, 兮 R1 — each
    trajectory hint failed to close the gap; second-round FAIL puts
    them past P-COMP-006 threshold.
  - 无 R1 FAIL, 气 R1 FAIL — both were LOW-priority "burn-test" retries
    per B5 postmortem; result confirms LOW ranking.

**All 12 FAILs terminal-frozen per P-COMP-006** (no new bank primitive
or trajectory-diff was added between R1-attempt-hint and the R1 attempt
itself; the P-COMP-008 candidate spec was inline hint, not bank; test
failed, so hypothesis is ruled out for these items — see B6 postmortem).

See `retry_log.jsonl`, `errata.md`, `sandbox.md` (B6 postmortem).

## Not promoted from B5 (C/FAIL, deferred or terminal-freeze)

**Main-channel B5 FAILs (11)**: 马, 乌 (both need heng_zhe_wan_gou for
main body); 以 (2-radical asymmetric pie/na proportion); 予 (heng_pie
tightness); 亢 (shu_wan_gou tuning for wide 儿-bottom); 仇, 仉 (both
need heng_zhe_wan_gou for 九/几 s2); 见 (box proportion + shu_wan_gou);
内, 內 sibling pair (both need box + inner-人 fitting); 兮 (wan_gou
tuning); 冗 (mi_cover + heng_zhe_wan_gou).

**Cluster identification**:
- **Missing-primitive cluster (heng_zhe_wan_gou)**: 马, 乌, 仇, 仉, 冗
  (5/11 FAILs). Same compound previously blocked 九, 几, 儿, 瓦, 爪 in
  B3/B4 (all now terminal-frozen at R2). Sandbox provides inline spec
  for B6 R1 retries.
- **Proportion / L-R composition cluster**: 以, 亢, 见, 兮, 內 (5/11).
  Fixable via trajectory-diff, no new primitive needed.
- **予**: standalone heng_pie tightness — trajectory-diff.

**Main-channel B5 C's (12)**: 巛, 川, 幺, 乡 (multi-curve calligraphic
family); 义 (short 3-stroke cross proportion); 仃 (亻+丁 sizing); 无
(top-heavy proportion); 仑 (亻+匕 composition); 仓 (人+匕 sizing); 气
(missing 气-specific hook — see p2_radical_111_气 which R2-froze); 切
(七+刀 composition); 冘 (top mi + underside 人 fit).

**Retry outcomes (R2 slots — 9 items, 0 PASS)**:
- **Terminal-freeze (R2 FAIL, 8)**: 牙, 乃, 乜, 九, 水, 瓦, 爪, 几.
  All satisfy P-COMP-006 (no new bank primitive between R1 and R2).
- **Terminal-freeze (R2 C, 1)**: 儿 R2-C — P-COMP-006 applies to
  R2-C too.

See `retry_log.jsonl`, `errata.md`, `sandbox.md` (B5 postmortem).

## Not promoted from B4 (C/FAIL, deferred or terminal-freeze)

**Main-channel B4 FAILs (8)**: 刁, 丸, 也, 卂, 与, 夊, 飞, 子 — hook/curve
cluster; several need the still-missing heng_zhe_wan_gou-family
primitive; 飞 is idiosyncratic (BANK_DEVIATION fresh_components).

**Main-channel B4 C's (13)**: 丁, 刂, 久, 乇, 亍, 于, 兀, 么, 及, 夂, 已, 尢, 才.

**Retry FAILs at R2 (14 — terminal-freeze candidates)**: 旡, 气, 火, 巳,
贝, 厄, 攴, 方, 兀, 比, 歹, 夕, 夂, 夊 — all had 2 consecutive FAIL rounds.

**Retry FAILs at R1 (7 — B5 R2 queue)**: 牙, 乃, 乜, 九, 水, 瓦, 爪, 儿.

**Retry C's at R2 (8 — terminal-freeze candidates)**: 氏, 子, 纟, 见, 斤,
耂, 毛, 手 — all had 2 rounds of C-verdicts.

**Retry C's at R1 (2 — B5 R2)**: 儿, 几 (Phase-3 char; radical version
was terminal-frozen in B3).

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B4 postmortem).

## Not promoted from B2 (C/FAIL, deferred or terminal-freeze)

**Main-channel B2 FAILs (18)**: 兀, 夕, 幺, 夂, 子, 比, 长, 歹, 方, 风, 火, 旡, 见, 肀, 爿, 攴, 气, 殳
**Main-channel B2 C's (13)**: 纟, 巳, 尢, 夊, 贝, 厄, 斤, 耂, 毛, 片, 氏, 礻, 手
**Retry FAILs (8)**: 丿(R2), 㔾, 巛, 飞, 宀, 女, 犭, 马
**Retry C's (7)**: 儿(R2), 阝, 几, 讠, 寸, 弓, 己, 门, 尸

See `errata.md`, `retry_log.jsonl`, and `sandbox.md` (B2 postmortem) for
diagnoses. Terminal-freeze candidates (2 batches, still not close) called
out in retry_log.jsonl.

## Import convention

Bank files use flat imports (no package). Composites reference sibling primitives directly:

```python
from pie import draw_pie          # ok inside success_bank/code/
from na import draw_na
from ti import draw_ti
```

Callers (drawers in `attempts/<id>/generated.py`) should add `success_bank/code/` to `sys.path` before importing, e.g.:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from ba import draw_ba
from shou_hand import draw_shou
```

## Not promoted from B10 (C/FAIL, terminal-freeze or do-not-queue)

**Main FAILs (15)** clustered:
- **Cluster A — 疒-family bank gap (do-not-queue, terminal-freeze)** (4):
  疙 (疒+乞), 疟 (疒+虐-inner), 疠 (疒+万), 疝 (疒+山). All 5-stroke 疒
  radical requires 2 dians + heng + long pie + ti; no whole-radical
  bank primitive. Consistent chronic pattern from G4 (疒-cluster). Also
  疌 (肀-top + 止-body) — similar bank gap, terminal-freeze.
- **Cluster B — 亻+X (do-not-queue partial, some retry-eligible)** (5):
  佚 (亻+失, X-cross bottom — 亻 used bank, 失 inline, no mechanism-change),
  社 (礻+土 — B11 R1 P-A-007 candidate: call shi_spirit + tu_earth),
  佛 (亻+弗, hook-compound right; do-not-queue per P-COMP-011/012),
  即 (皀+卩, 皀 no bank; do-not-queue),
  佞 (亻+二+女, 3-part — B11 R1 P-A-007 candidate: call ren_left +
  er_two + nu_woman all as bank primitives).
- **Cluster C — novel 8-stroke unique compositions** (4):
  事 (unique 龶+口+亅 layout; no whole-radical decomposition available;
  do-not-queue), 乖 (千 shell + mirror-hook cluster; do-not-queue),
  乶 (甫+乙 rare; do-not-queue),
  畅 (甲/申 + 勿-like — B11 R1 MEDIUM candidate: try draw_you_by 由 +
  extend s5 shu for 申's top-extension).
- **Cluster D — hook-compound not in bank** (1):
  经 (纟+圣 — no 纟 whole-radical; 又+土 right could be tried).
- **Cluster E — 8-stroke novel** (1):
  乶 (see above).

**Main C's (9)** — no retries queued per P-COMP-006 unless mechanism-change:
张, 佘, 每, 改, 块, 到, 甾, 疚, 学.

**R1 outcomes (5)** from B10 queue:
- **运 R1 A** — trajectory-diff mechanism-change worked (P-A-005 recipe:
  called draw_pie_zhe for s3 with explicit corner instead of collapsed
  diagonal + kept draw_chuo for 辶). Promoted as inline template
  reference (not standalone wrapper).
- **身 R1 C** — improved but still C. Terminal-freeze (2-round no PASS).
- **凫 R1 FAIL** — P-A-008 test did not unlock. Terminal-freeze.
- **条 R1 FAIL** — P-A-008 test did not unlock. Terminal-freeze.
- **两 R1 FAIL** — speculative queue did not unlock. Terminal-freeze.

See `errata.md` and `sandbox.md` (B10 postmortem).

## B12 promotions (2026-08-09) — 10 A-verdict primitives + 1 R1 A

### Wrapper file (1)

| # | Kind | Item ID | Char | Batch | File | Fn signature |
|---|------|---------|------|-------|------|--------------|
| 168 | radical/char | p3_char_0463_神 (A, SOLO) | 神 | B12 | `shen_god.py` | `draw_shen(d, ox=0.0, oy=0.0, scale=1.0)` + `draw_shen_left_hemisphere(d, ox=0.0, oy=0.0, scale=1.0)` (礻-adaptation exemplar; the hemisphere entry encodes the 57-px-shifted 礻 for compound-left placement; high downstream reuse for 社/祈/福/祝/礼) |

### Inline-template pointers (9 A verdicts + 1 R1 A)

Not standalone .py files — retrieval via attempt-file paths per B7/B11
convention. Curator lists here so drawers know these recipes exist.

| # | Item ID | Char | Batch | Attempt path | Reuse hint |
|---|---------|------|-------|--------------|------------|
| 169 | p3_char_0443_面 (A, SOLO) | 面 | B12 | `attempts/p3_char_0443_面/generated.py` | 9-stroke frame (top heng + short pie + shu + heng_zhe_box + interior shus/hengs + bottom heng). Template for future 面/緬 |
| 170 | p3_char_0445_点 (A) | 点 | B12 | `attempts/p3_char_0445_点/generated.py` | 占-top (卜+口) + 灬-bottom stack with per-radical quant BANK_DEVIATION. Template for future 占-top compounds |
| 171 | p3_char_0447_信 (A) | 信 | B12 | `attempts/p3_char_0447_信/generated.py` | 亻 called at default + 言 inlined (dian+3 hengs) + 口-flat DEVIATIONed. Template for future 亻+言-family (誠/請/謝) |
| 172 | p3_char_0449_美 (A) | 美 | B12 | `attempts/p3_char_0449_美/generated.py` | 羊-top (6 strokes) + 大-compressed-flat bottom DEVIATIONed on 1.45× aspect. Template for future 羊-top compounds (羚/差/群) |
| 173 | p3_char_0466_盃 (A) | 盃 | B12 | `attempts/p3_char_0466_盃/generated.py` | **Archetype-2 template stack**: 不 (0094 template) + 皿 (0195 template). NO BANK_DEVIATION — both fit natively. Reuse for any X+皿 vertical stack |
| 174 | p3_char_0468_盅 (A) | 盅 | B12 | `attempts/p3_char_0468_盅/generated.py` | **Archetype-2 template stack**: 中 (0100 template) + 皿 (0195 template). Reuse for X+皿 vertical stacks |
| 175 | p3_char_0476_俅 (A, SOLO) | 俅 | B12 | `attempts/p3_char_0476_俅/generated.py` | 亻 DEVIATIONed for compound-left crowding + 求 (7 strokes: heng+shu_gou+dian+ti+pie+na+dian). Template for 亻+求-family (球/救/裘) |
| 176 | p3_char_0482_俎 (A) | 俎 | B12 | `attempts/p3_char_0482_俎/generated.py` | 仌-left (pie+dian×2) + 且 (shu+heng_zhe_box+3 hengs). Reuse 且 sub-pattern for 助/組/宜 |
| 177 | p3_char_0483_草 (A) | 草 | B12 | `attempts/p3_char_0483_草/generated.py` | 3-band vertical (艹+日+十) all 3 whole-radicals DEVIATIONed on band-break aspect (>2.1×). Template for future 3-band vertical compounds |
| — | p3_char_0393_实__retry_1 (R1 A) | 实 | B12 | `attempts/p3_char_0393_实__retry_1/generated.py` | 宀 called via mian_roof at scale=0.85 (compressed-top variant) + 头 inlined. Retrieval hint: **for compressed-宀 compounds, call mian_roof at scale 0.80-0.90 rather than default 1.0** |

## Not promoted from B12 (C/FAIL, terminal-freeze or do-not-queue)

**Main FAILs (23)** clustered:

- **Cluster A — 疒-family bank gap (do-not-queue, terminal-freeze)** (5):
  疤(446), 疫(450), 疬(452), 疭(454), 疮(456). Reaffirms B10 terminal-freeze
  (9 cumulative 疒 FAILs). No bank push per P-COMP-008 refutation.
- **Cluster B — 亻+X (mixed: 3 queueable, 3 do-not-queue)** (6):
  侯(464) **B13 R1 HIGH kind-(a)** (ren_left uniform-shift ~70px),
  便(469) **B13 R1 HIGH kind-(a)**,
  俊(480) **B13 R1 MEDIUM kind-(a)**,
  侷(472) (亻+局 hook-compound; do-not-queue P-COMP-012),
  係(474) (亻+系, no bank for 系; do-not-queue kind-(e)),
  俉(478) (亻+吾, multi-DEVIATION on 五+口; do-not-queue kind-(e)).
- **Cluster C — 3-part / L-R composition kind-(d)/(e) do-not-queue** (5):
  亲(461), 城(473) [B13 R1 LOW kind-(b1)], 结(467), 度(453), 济(481).
- **Cluster D — novel/unique/traditional (do-not-queue)** (6):
  畐(438), 乹(442), 将(439), 畑(440), 癸(458), 带(459), 皅(460).

**Main C's (4)** — no retries queued per P-COMP-006 unless mechanism-change:
畏(436), 种(437), 前(441), 皈(462).

**R1 outcomes (5)** from B12 queue — 3/5 = 60% recovery, up from B11's 0/4:
- **实 R1 A** ✓ Kind (a) validated. mian_roof called at scale=0.85; promoted
  as inline template + retrieval hint above.
- **治 R1 PASS** ✓ Kind (b1) parameter-tune validated. Wide-flat 口 inlined
  with box bottom_right aligned to shu depth.
- **放 R1 PASS** ✓ Kind (b1) with mixed-strategy (方 stroke-level fixes +
  pu_action bank call at scale=0.85).
- **例 R1 C** ✗ Kind (a) partial rescue only. 3-radical L-R with 亻/刂 fixed
  but 歹-middle inline noisy. Boundary case for kind-(a). Terminal-freeze.
- **侔 R1 FAIL** ✗ Kind (b) MISCLASSIFIED (was really kind (d) —
  inter-primitive spacing). Terminal-freeze; sharpens P-A-010-v2.

See `errata.md` and `sandbox.md` (B12 postmortem).
