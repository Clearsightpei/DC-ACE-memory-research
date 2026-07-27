# Success Bank — INDEX (G3 coord-bank)

**Phase-1-only reconstruction.** This bank was reset after a Phase-2
restart mishap in which a pruning-parser bug misinterpreted radical
aliasing rows (丨/一/丶/乛 reusing shu/heng/dian/heng_gou) as
authorising deletion of the referenced primitive files themselves.
Four primitives (`heng.py`, `shu.py`, `dian.py`, `heng_gou.py`) were
lost and have been re-extracted from their passing Phase-1 attempts;
`heng.py` was reconstructed against its passing-attempt docstring
(200x12 px horizontal, canvas-centered) since the attempt only
imported the primitive without inlining logic.

The bank now contains **only Phase-1 stroke primitives** that
correspond to passing `p1_stroke_*` attempts. No Phase-2 radicals are
included. Format for every entry:
`def draw_<name>(t, ox=0, oy=0, scale=1.0)` where `t` is a PIL
`ImageDraw` and `(ox, oy, scale)` are numeric offsets on a 300x300
canvas — no 米字格 anchors, no cell references, no joint specs. Pure
coord format.

| # | name | file | strokes | mastered at |
|---|------|------|---------|-------------|
| 1 | 横 (heng) | heng.py | 1 | p1_stroke_01_横 |
| 2 | 竖 (shu) | shu.py | 1 | p1_stroke_02_竖 |
| 3 | 撇 (pie) | pie.py | 1 | p1_stroke_03_撇 |
| 4 | 捺 (na) | na.py | 1 | p1_stroke_04_捺 |
| 5 | 点 (dian) | dian.py | 1 | p1_stroke_05_点 |
| 6 | 提 (ti) | ti.py | 1 | p1_stroke_06_提 |
| 7 | 弯钩 (wan gou) | wan_gou.py | 1 (compound) | p1_stroke_07_弯钩 |
| 8 | 卧钩 (wo gou) | wo_gou.py | 1 (compound) | p1_stroke_08_卧钩 |
| 9 | 横撇 (heng pie) | heng_pie.py | 1 (compound) | p1_stroke_09_横撇 |
| 10 | 横钩 (heng gou) | heng_gou.py | 1 (compound) | p1_stroke_10_横钩 |
| 11 | 横折 (heng zhe) | heng_zhe.py | 1 (compound) | p1_stroke_11_横折 |
| 12 | 竖提 (shu ti) | shu_ti.py | 1 (compound) | p1_stroke_12_竖提 |
| 13 | 竖弯 (shu wan) | shu_wan.py | 1 (compound) | p1_stroke_13_竖弯 |
| 14 | 竖折 (shu zhe) | shu_zhe.py | 1 (compound) | p1_stroke_15_竖折 |
| 15 | 撇点 (pie dian) | pie_dian.py | 1 (compound) | p1_stroke_17_撇点 |
| 16 | 撇折 (pie zhe) | pie_zhe.py | 1 (compound) | p1_stroke_18_撇折 |
| 17 | 橫折提 (heng zhe ti) | heng_zhe_ti.py | 1 (compound) | p1_stroke_20_橫折提 |
| 18 | 横折钩 (heng zhe gou) | heng_zhe_gou.py | 1 (compound) | p1_stroke_22_横折钩 |
| 19 | 横撇弯钩 (heng pie wan gou) | heng_pie_wan_gou.py | 1 (compound) | p1_stroke_24_横撇弯钩 |
| 20 | 竖折撇 (shu zhe pie) | shu_zhe_pie.py | 1 (compound) | p1_stroke_27_竖折撇 |
| 21 | 竖折折 (shu zhe zhe) | shu_zhe_zhe.py | 1 (compound) | p1_stroke_28_竖折折 |
| 22 | 横折折撇 (heng zhe zhe pie) | heng_zhe_zhe_pie.py | 1 (compound) | p1_stroke_29_横折折撇 |
| 23 | 横折折折 (heng zhe zhe zhe) | heng_zhe_zhe_zhe.py | 1 (compound) | p1_stroke_30_横折折折 |
| 24 | 竖钩 (shu gou) | shu_gou.py | 1 (compound) | p1_stroke_14_竖钩 (batch-3 retry PASS) |
| 25 | 竖弯钩 (shu wan gou) | shu_wan_gou.py | 1 (compound) | p1_stroke_23_竖弯钩 (batch-3 retry PASS) |
| 26 | 丨 radical (gun_radical) | gun_radical.py | 1 (variant of shu — scooping head) | p2_radical_001_丨 (bootstrap) |
| 27 | 亅 radical (jue_radical) | jue_radical.py | 1 (alias — wraps shu_gou at +22,-5,0.85) | p2_radical_002_亅 (bootstrap) |
| 28 | 丿 radical (pie_radical) | pie_radical.py | 1 (variant of pie — softer scoop; P10) | p2_radical_003_丿 (bootstrap) |
| 29 | 乛 radical (heng_gou_radical) | heng_gou_radical.py | 1 (variant of heng_gou — thinner, shorter) | p2_radical_004_乛 (bootstrap) |
| 30 | 一 (yi) | yi.py | 1 (inlined 横 with soft-taper width profile) | p2_radical_005_一 (bootstrap) |
| 31 | 乙 radical (yi_radical) | yi_radical.py | 1 (continuous 横折弯钩-form sweep) | p2_radical_006_乙 (bootstrap) |
| 32 | 乚 radical (ya_radical) | ya_radical.py | 1 (alias — wraps shu_wan_gou at -45,-12,1.2) | p2_radical_007_乚 (bootstrap) |
| 33 | 丶 radical (dian_radical) | dian_radical.py | 1 (variant of dian — longer, slimmer) | p2_radical_008_丶 (bootstrap) |
| 34 | 八 (ba) | ba.py | 2 (pie + na, V-notch top) | p2_radical_009_八 (bootstrap) |
| 35 | 冫 (bing) | bing.py | 2 (dian + inlined down-left slash w/ up-right hook) | p2_radical_012_冫 (bootstrap) |
| 36 | 卜 (bu) | bu.py | 2 (shu + dian) | p2_radical_013_卜 (bootstrap) |
| 37 | 刂 (dao_pang) | dao_pang.py | 2 (short shu + shu_gou) | p2_radical_016_刂 (bootstrap) |
| 38 | 儿 (er_ren) | er_ren.py | 2 (pie + shu_wan_gou) | p2_radical_017_儿 (bootstrap) |
| 39 | 二 (er) | er.py | 2 (two heng — upper short, lower long) | p2_radical_018_二 (bootstrap) |
| 40 | 匚 (fang) | fang.py | 2 (heng + inlined 竖折) | p2_radical_019_匚 (B1, pos 51) |
| 41 | 几 (ji) | ji.py | 2 (inlined 撇 + inlined 横折弯钩 bezier) | p2_radical_022_几 (B1, pos 54) |
| 42 | 卩 (jie_radical) | jie_radical.py | 2 (fully inlined 横折钩 + 竖) | p2_radical_023_卩 (B1, pos 55) |
| 43 | 冖 (mi_radical) | mi_radical.py | 1 (inlined 横钩 tuned wider) | p2_radical_026_冖 (B1, pos 58) |
| 44 | 凵 (qu_radical) | qu_radical.py | 1 (inlined U-shape: shu + heng + shu) | p2_radical_027_凵 (B1, pos 59) |
| 45 | 亻 (ren_pang) | ren_pang.py | 2 (pie + shu, left-radical scale) | p2_radical_029_亻 (B1, pos 61) |
| 46 | 十 (shi) | shi.py | 2 (heng crossing shu at center — TR4 exemplar) | p2_radical_031_十 (B1, pos 63) |
| 47 | 亠 (tou_radical) | tou_radical.py | 2 (dian + heng) | p2_radical_033_亠 (B1, pos 65) |
| 48 | 匸 (xi_radical) | xi_radical.py | 2 (heng + inlined 竖折, similar to 匚) | p2_radical_034_匸 (B1, pos 66) |
| 49 | 又 (you) | you.py | 2 (pie + heng_pie / na-like) | p2_radical_037_又 (B1, pos 69) |
| 50 | 艹 (cao_zi_tou) | cao_zi_tou.py | 3 (fully inlined: heng + two 竖 tails) | p2_radical_039_艹 (B1, pos 71) |
| 51 | 川 (chuan) | chuan.py | 3 (inlined 撇 + 2 shu, spaced verticals) | p2_radical_043_川 (B1, pos 75) |
| 52 | 辶 (zou_zhi) | zou_zhi.py | 3 (dian + inlined 横折折撇 + inlined 平捺) | p2_radical_044_辶 (B1, pos 76) |
| 53 | 寸 (cun) | cun.py | 3 (heng + shu_gou + dian) | p2_radical_045_寸 (B1, pos 77) |
| 54 | 干 (gan) | gan.py | 3 (two heng + shu) | p2_radical_048_干 (B1, pos 80) |
| 55 | 工 (gong) | gong.py | 3 (heng + shu + heng) | p2_radical_049_工 (B1, pos 81) |
| 56 | 廾 (gong_radical) | gong_radical.py | 4 (inlined) | p2_radical_051_廾 (B1, pos 83) |
| 57 | 广 (guang) | guang.py | 3 (dian + inlined heng + inlined 撇) | p2_radical_052_广 (B1, pos 84) |
| 58 | 彐 (ji_radical) | ji_radical.py | 3 (fully inlined: 3 tapered segments) | p2_radical_054_彐 (B1, pos 86) |
| 59 | 口 (kou) | kou.py | 3 (shu + heng_zhe + heng — box) | p2_radical_057_口 (B1, pos 89) |
| 60 | 宀 (bao_gai_tou) | bao_gai_tou.py | 3 (dian + heng_gou + inlined short shu) | p2_radical_060_宀 (B1, pos 92) |
| 61 | 山 (shan) | shan.py | 3 (shu + inlined 竖折 + shu) | p2_radical_063_山 (B1, pos 95) |
| 62 | 彡 (shan_radical) | shan_radical.py | 3 (three pie at descending scale) | p2_radical_064_彡 (B1, pos 96) |
| 63 | 尸 (shi_radical) | shi_radical.py | 3 (fully inlined: heng_zhe_gou + heng + pie) | p2_radical_065_尸 (B1, pos 97) |
| 64 | 饣 (shi_pang) | shi_pang.py | 3 (inlined pie + inlined 横钩 + inlined shu_ti) | p2_radical_066_饣 (B1, pos 98) |
| 65 | 士 (shi_male) | shi_male.py | 3 (heng + shu + heng, upper heng wider) | p2_radical_067_士 (B1, pos 99) |
| 66 | 扌 (shou_pang) | shou_pang.py | 3 (heng + shu_gou + ti) | p2_radical_068_扌 (B1, pos 100) |
| 67 | 厂 (chang) | chang.py | 2 (heng + inlined nearly-vertical 丿) | p2_radical_014_厂 (B1 retry-1 graduation, pos 46) |
| 68 | 氵 (san_dian_shui) | san_dian_shui.py | 3 (dian + dian + ti) | p2_radical_069_氵 (B2, pos 101) |
| 69 | 纟 (si_zi_pang) | si_zi_pang.py | 3 (inlined 2× 撇折 hooks + long 提) | p2_radical_070_纟 (B2, pos 102) |
| 70 | 巳 (si) | si.py | 3 (fully inlined 横折 + 横 + 竖弯钩, PIL px) | p2_radical_071_巳 (B2, pos 104) |
| 71 | 土 (tu) | tu.py | 3 (heng + shu + heng, bottom heng wider) | p2_radical_072_土 (B2, pos 103) |
| 72 | 囗 (wei_radical) | wei_radical.py | 3 (shu + heng_zhe + heng, enclosing scale) | p2_radical_073_囗 (B2, pos 105) |
| 73 | 夕 (xi) | xi.py | 3 (inline 撇 + inline 横折撇 2-arc + dian) | p2_radical_075_夕 (B2, pos 107) |
| 74 | 小 (xiao) | xiao.py | 3 (shu_gou + inline left pie + dian) | p2_radical_076_小 (B2, pos 108) |
| 75 | 灬 (huo_bottom) | huo_bottom.py | 4 (4 inline dots, PIL px) | p2_radical_087_灬 (B2, pos 119) |
| 76 | 歹 (dai) | dai.py | 4 (inline top-heng + short pie + 横撇 composite + dian) | p2_radical_090_歹 (B2, pos 122) |
| 77 | 厄 (e) | e.py | 4 (chang envelope + inline 横折 + inline 竖弯钩) | p2_radical_092_厄 (B2, pos 124) |
| 78 | 父 (fu) | fu.py | 4 (inline short 撇 + short 点 + big 撇 + big 捺 crossing) | p2_radical_095_父 (B2, pos 127) |
| 79 | 耂 (lao_radical) | lao_radical.py | 4 (inline 2 hengs + short shu + long sweeping pie) | p2_radical_102_耂 (B2, pos 134) |
| 80 | 毛 (mao) | mao.py | 4 (inline 撇 + 2 hengs + shu_wan_gou) | p2_radical_103_毛 (B2, pos 135) |
| 81 | 木 (mu) | mu.py | 4 (inline heng + shu + pie + na crossing) | p2_radical_104_木 (B2, pos 136) |
| 82 | 牛 (niu) | niu.py | 4 (pie + 2 hengs + shu, all bank) | p2_radical_106_牛 (B2, pos 138) |
| 83 | 日 (ri) | ri.py | 4 (fully inline tall rectangle — kou doesn't fit aspect) | p2_radical_114_日 (B2, pos 146) |
| 84 | 礻 (shi_ceremony_pang) | shi_ceremony_pang.py | 4 (inline dian + 横撇 + shu + right dian) | p2_radical_116_礻 (B2, pos 148) |
| 85 | 文 (wen) | wen.py | 4 (dian + heng + crossing 撇 + 捺, inline PIL) | p2_radical_124_文 (B3, pos 151) |
| 86 | 心 (xin) | xin.py | 4 (wo_gou bowl + left/mid/right dots) | p2_radical_126_心 (B3, pos 153) |
| 87 | 爻 (yao) | yao.py | 4 (stacked 乂 pair, inline PIL) | p2_radical_128_爻 (B3, pos 155) |
| 88 | 曰 (yue_speak) | yue_speak.py | 4 (squat rectangle + middle heng) | p2_radical_129_曰 (B3, pos 156) |
| 89 | 月 (yue) | yue.py | 4 (撇 + tall 横折钩 + 2 interior 横) | p2_radical_130_月 (B3, pos 157) |
| 90 | 爫 (zhao_top) | zhao_top.py | 4 (3 short 撇 + arched top 横撇, variant_pie) | p2_radical_131_爫 (B3, pos 158) |
| 91 | 一 (yi_char) | yi_char.py | 1 (draw_yi at (0,-45,1.0)) | p3_char_0001_一 (B3, pos 159) |
| 92 | 丨 (gun_char) | gun_char.py | 1 (identity alias for gun_radical) | p3_char_0002_丨 (B3, pos 160) |
| 93 | 乙 (yi_second) | yi_second.py | 1 (identity alias for yi_radical) | p3_char_0003_乙 (B3, pos 161) |
| 94 | 丶 (dian_char) | dian_char.py | 1 (dian_radical at scale 1.15) | p3_char_0004_丶 (B3, pos 162) |
| 95 | 丿 (pie_char) | pie_char.py | 2 (thin uniform pies via variant_pie) | p3_char_0005_丿 (B3, pos 163) |
| 96 | 乚 (la_char) | la_char.py | 1 (ya_radical at scale 1.5) | p3_char_0006_乚 (B3, pos 164) |
| 97 | 亅 (jue_char) | jue_char.py | 1 (inline 竖钩 with proper hook) | p3_char_0008_亅 (B3, pos 165) |
| 98 | 了 (liao) | liao.py | 2 (inline 横钩 top + wan_gou descender) | p3_char_0009_了 (B3, pos 166) |
| 99 | 丩 (jiu_char) | jiu_char.py | 2 (continuous 竖折 left + top-hook shaft right) | p3_char_0010_丩 (B3, pos 167) |
| 100 | 十 (shi_char) | shi_char.py | 2 (shi radical at scale 1.1) | p3_char_0013_十 (B3, pos 170) |
| 101 | 乂 (yi_cross) | yi_cross.py | 2 (variant_pie + variant_na crossing X) | p3_char_0014_乂 (B3, pos 171) |
| 102 | 二 (er_char) | er_char.py | 2 (er radical at (0,+10,1.0)) | p3_char_0015_二 (B3, pos 172) |
| 103 | 又 (you_char) | you_char.py | 2 (you radical at scale 1.15) | p3_char_0017_又 (B3, pos 174) |
| 104 | 儿 (er_ren_char) | er_ren_char.py | 2 (er_ren radical at scale 1.3) | p3_char_0019_儿 (B3, pos 176) |
| 105 | 亠 (tou_char) | tou_char.py | 2 (identity alias for tou_radical) | p3_char_0020_亠 (B3, pos 177) |
| 106 | 几 (ji_char) | ji_char.py | 2 (ji radical with recentering) | p3_char_0021_几 (B3, pos 178) |
| 107 | 亻 (ren_pang_char) | ren_pang_char.py | 2 (identity alias for ren_pang) | p3_char_0022_亻 (B3, pos 179) |
| 108 | 八 (ba_char) | ba_char.py | 2 (identity alias for ba) | p3_char_0024_八 (B3, pos 181) |
| 109 | 七 (qi) | qi.py | 2 (inline top heng + shu_wan_gou) | p3_char_0027_七 (B3, pos 184) |
| 110 | 冖 (mi_char) | mi_char.py | 2 (identity alias for mi_radical) | p3_char_0028_冖 (B3, pos 185) |
| 111 | 冫 (bing_char) | bing_char.py | 2 (bing at (0,+15,1.0)) | p3_char_0030_冫 (B3, pos 187) |
| 112 | 厂 (chang_char) | chang_char.py | 2 (identity alias for chang) | p3_char_0031_厂 (B3, pos 188) |
| 113 | 凵 (qu_char) | qu_char.py | 2 (qu_radical at scale 1.05, oy=-15) | p3_char_0032_凵 (B3, pos 189) |
| 114 | 刁 (diao_char) | diao_char.py | 2 (inline 横折竖 + 提, PIL px) | p3_char_0034_刁 (B4, pos 201) |
| 115 | 丁 (ding_char) | ding_char.py | 2 (heng + shu_gou) | p3_char_0035_丁 (B4, pos 202) |
| 116 | 刂 (dao_pang_char) | dao_pang_char.py | 2 (identity alias for dao_pang) | p3_char_0036_刂 (B4, pos 203) |
| 117 | 勹 (bao_char) | bao_char.py | 2 (inline pie + continuous envelope, cubic bezier) | p3_char_0037_勹 (B4, pos 204) |
| 118 | 之 (zhi_char) | zhi_char.py | 3 (variant_dian + inline 横撇 + variant_na 平捺) | p3_char_0039_之 (B4, pos 206) |
| 119 | 丫 (ya_char) | ya_char.py | 3 (variant_pie mirror pair + tapered_line 竖, thin uniform) | p3_char_0040_丫 (B4, pos 207) |
| 120 | 上 (shang_char) | shang_char.py | 3 (heng + shu + heng at three positions) | p3_char_0045_上 (B4, pos 212) |
| 121 | 久 (jiu_long_char) | jiu_long_char.py | 3 (variant_pie ×2 + variant_na crossing) | p3_char_0046_久 (B4, pos 213) |
| 122 | 子 (zi_char / zi) | zi_char.py | 3 (liao skeleton + crossing heng) | p3_char_0049_子 (B4, pos 216) + p2_radical_082_子__retry_1 (B4 GRADUATE) |
| 123 | 亍 (chu_char) | chu_char.py | 3 (2 hengs + jue_char) | p3_char_0050_亍 (B4, pos 217) |
| 124 | 于 (yu_char) | yu_char.py | 3 (2 hengs + shu_gou) | p3_char_0051_于 (B4, pos 218) |
| 125 | 亡 (wang_char) | wang_char.py | 3 (dian + heng + inline 竖折) | p3_char_0052_亡 (B4, pos 219) |
| 126 | 下 (xia_char) | xia_char.py | 3 (heng + shu + dian) | p3_char_0053_下 (B4, pos 220) |
| 127 | 亼 (ji_meet_char) | ji_meet_char.py | 3 (kiss_apex 人-roof + heng, thin uniform) | p3_char_0054_亼 (B4, pos 221) |
| 128 | 三 (san_char) | san_char.py | 3 (draw_yi ×3 with length_px override) | p3_char_0055_三 (B4, pos 222) |
| 129 | 小 (xiao_char) | xiao_char.py | 3 (identity alias for xiao) | p3_char_0057_小 (B4, pos 224) |
| 130 | 兀 (wu_char) | wu_char.py | 3 (heng + er_ren) | p3_char_0058_兀 (B4, pos 225) |
| 131 | 卄 (nian_char) | nian_char.py | 3 (inline 3-line: 2 near-verticals + crossbar) | p3_char_0062_卄 (B4, pos 229) |
| 132 | 门 (men_char) | men_char.py | 3 (inline 点 + 竖 + 横折钩, tall/narrow) | p3_char_0063_门 (B4, pos 230) |
| 133 | 叉 (cha_char) | cha_char.py | 3 (you_char alias + variant_dian in crook) | p3_char_0064_叉 (B4, pos 231) |
| 134 | 囗 (wei_char) | wei_char.py | 3 (identity alias for wei_radical) | p3_char_0066_囗 (B4, pos 233) |
| 135 | 山 (shan_char) | shan_char.py | 3 (identity alias for shan) | p3_char_0067_山 (B4, pos 234) |
| 136 | 干 (gan_char) | gan_char.py | 3 (identity alias for gan) | p3_char_0069_干 (B4, pos 236) |
| 137 | 口 (kou_char) | kou_char.py | 3 (identity alias for kou) | p3_char_0071_口 (B4, pos 238) |
| 138 | 孑 (jie_char) | jie_char.py | 3 (inline 横撇 + 弯钩 + 提) | p3_char_0074_孑 (B4, pos 241) |
| 139 | 艹 (cao_char) | cao_char.py | 3 (identity alias for cao_zi_tou) | p3_char_0078_艹 (B4, pos 245) |
| 140 | 宀 (mian_char) | mian_char.py | 3 (identity alias for bao_gai_tou) | p3_char_0080_宀 (B4, pos 247) |
| 141 | 屮 (chu_radical_char) | chu_radical_char.py | 3 (inline shaft + mirrored 竖折 arms) | p3_char_0084_屮 (B5, pos 251) |
| 142 | 工 (gong_char) | gong_char.py | 3 (identity alias for gong radical) | p3_char_0087_工 (B5, pos 252) |
| 143 | 川 (chuan_char) | chuan_char.py | 3 (chuan radical at scale 1.15, oy=-5) | p3_char_0088_川 (B5, pos 253) |
| 144 | 廾 (nian_horns) | nian_horns.py | 4 (inline cap 横 + long 撇 + crossbar + right 竖) | p3_char_0092_廾 (B5, pos 254) |
| 145 | 弋 (yi_ge) | yi_ge.py | 3 (heng + 斜钩 belly bezier + dot) | p3_char_0093_弋 (B5, pos 255) |
| 146 | 不 (bu_char) | bu_char.py | 4 (inline heng + pie + shu + dian) | p3_char_0094_不 (B5, pos 256) |
| 147 | 丹 (dan) | dan.py | 4 (撇 + 横折钩 frame + interior 点 + crossing 横) | p3_char_0095_丹 (B5, pos 257) |
| 148 | 以 (yi_pron) | yi_pron.py | 4 (inline 竖提 + 短点 + long 撇 + dot; PIL-pixel recipe) | p3_char_0098_以 (B5, pos 258) |
| 149 | 中 (zhong) | zhong.py | 4 (bank kou at scale 0.55 + inline central shu protruding) | p3_char_0100_中 (B5, pos 259) |
| 150 | 亓 (qi_ji) | qi_ji.py | 4 (inline 2 hengs + pie + shu, thin ~5px) | p3_char_0101_亓 (B5, pos 260) |
| 151 | 日 (ri_char) | ri_char.py | 4 (identity alias for ri radical) | p3_char_0106_日 (B5, pos 261) |
| 152 | 仃 (ding_ren) | ding_ren.py | 5 (compressed ren_pang + inline heng + shu_gou) | p3_char_0107_仃 (B5, pos 262) |
| 153 | 心 (xin_char) | xin_char.py | 4 (identity alias for xin radical) | p3_char_0112_心 (B5, pos 263) |
| 154 | 仉 (zhang_ren) | zhang_ren.py | 4 (tall inline 亻 + bank 几 at scale 0.85) | p3_char_0113_仉 (B5, pos 264) |
| 155 | 仌 (bing_ren) | bing_ren.py | 4 (stacked asymmetric 人 via kiss_apex) | p3_char_0115_仌 (B5, pos 265) |
| 156 | 文 (wen_char) | wen_char.py | 4 (identity alias for wen radical) | p3_char_0124_文 (B5, pos 266) |
| 157 | 冈 (gang) | gang.py | 4 (PIL-pixel 冂 frame + 乂 inside via variant_pie/variant_na) | p3_char_0127_冈 (B5, pos 267) |
| 158 | 太 (tai_char) | tai_char.py | 4 (heng + X-crossing at u_pie=0.24 + crotch dian) | p3_char_0128_太 (B5, pos 268) |
| 159 | 龶 (zhu_top) | zhu_top.py | 4 (3 stacked hengs + piercing shu, thin ~4px) | p3_char_0129_龶 (B5, pos 269) |
| 161 | 丷 (ba_dot) | ba_dot.py | 2 (asymmetric variant_dian + variant_pie, thin ~4px) | p2_radical_021_丷__retry_4 (B5 GRADUATE) |

**Total: 160 primitives** (v7 curator note: `_shared_helpers.py` also
lives in `code/` but is a helper module, not a mastered item).

## Batch B3 (2026-07-22, positions 151-200 judged + 13 retries)

29 main-curriculum PASSes recorded above (bank entries 85-113). No
retry graduations — all 13 retries FAILed (many used the new variant
helpers but still couldn't hit the target). 21 main-curriculum FAILs
added to errata.md. Overall pass rate 29/50 = **58%**, recovering
from B2's 34% collapse (Phase-3 easy chars aided recovery). Cumulative
through 200 items: 52%, still below G1's 54%. See sandbox.md "B3
diagnostic" and evolution.md 2026-07-22 for the second-pass v7
response.

## Batch B1 (2026-07-18, positions 51–100 judged + 2 retries)

27 main-curriculum PASSes recorded above (bank entries 40–66), plus 1
retry graduation (`chang.py`, entry 67 — 厂 passed on retry_1). 23
main-curriculum FAILs added to errata.md; retry #1 for 刀 also FAILed
(retry_n=1). Overall pass rate 27/50 = **54%**, marginally worse than
G1 no-memory (60%) on this batch — the second consecutive batch where
G3 underperformed the control. See `sandbox.md` "Batch B1 diagnostic"
section and `principle_bank.md` §TR8 (new inline-fresh rule).

Naming policy:
- Pure-composition entries (only bank primitive calls with scaled
  offsets): `cun`, `gan`, `gong`, `ren_pang`, `shan_radical`, `shi`,
  `shi_male`, `shou_pang`, `tou_radical`, `you`, `kou`.
- Composition-plus-inline (some bank + custom recipe): `chang`,
  `bao_gai_tou`, `chuan`, `fang`, `guang`, `jie_radical`, `mi_radical`,
  `shan`, `shi_pang`, `xi_radical`, `zou_zhi`.
- Fully inlined (no bank calls — inlining beat force-fit): `cao_zi_tou`,
  `gong_radical`, `ji` (几), `ji_radical` (彐), `qu_radical`,
  `shi_radical` (尸).

## Bootstrap batch (2026-07-17, positions 33–50 judged)

14 PASSes recorded above. Naming policy applied:
- Radicals orthographically same as a mastered stroke but whose PASS
  render is a variant (softer / thinner / longer) got a
  `<pinyin>_radical.py` file with the variant code inlined (丨, 丿, 乛, 丶).
- Radicals that are pure aliases at a fixed transform got a thin
  wrapper delegating to the primitive (亅→shu_gou, 乚→shu_wan_gou).
- Multi-stroke radicals got a plain `<pinyin>.py` composing primitives
  (八, 冫, 卜, 刂, 儿, 二).
- `yi.py` = 一 (character-and-radical coincide).
  `yi_radical.py` = 乙 (pinyin collision with 一 — files are distinct).
- Existing primitives (heng, shu, pie, dian, heng_gou, shu_gou,
  shu_wan_gou, na) reused as building blocks — none were modified.

4 FAILs (勹, 匕, 厂, 刀) added to errata.md; see sandbox.md for
failure-mode analysis and principle_bank.md updates.

Notes:
- Re-extracted after reset: `heng.py` (reconstructed from docstring —
  passing attempt only imported), `shu.py`, `dian.py`, `heng_gou.py`
  (all extracted verbatim from their passing attempts).
- **Re-reconstructed after reset**: `shu_gou.py` and `shu_wan_gou.py`
  (batch-3 retry graduations, originally passed on retry — retry_attempts
  folder was wiped during the Phase-2 restart, so these two files were
  synthesised fresh matching G3's coord format based on `shu.py` conventions).
- The Phase-1 strokes not on this list (16 斜钩, 19 横斜钩,
  21 横折弯, 25 横折弯钩, 26 横折折, 31 竖折折钩,
  32 横折折折钩) had no passing attempt in the current record and are
  intentionally absent.
- `_anchor.py` is not part of this bank — G3 uses raw coord offsets,
  not 米字格 anchors.
- Phase-2 radicals have been removed pending re-derivation in the
  Phase-2 restart.

## Batch B2 (2026-07-18, positions 101–150 judged + 8 retries)

17 main-curriculum PASSes recorded above (bank entries 68–84). No
retry graduations — all 8 retries FAILed. 33 main-curriculum FAILs
added to errata.md. Overall pass rate 17/50 = **34%**, worst yet
(bootstrap 78%, B1 54%, B2 34%) and worse than G1 no-memory (38%).
See `sandbox.md` "Batch B2 diagnostic" and `evolution.md` for the
v7 memory self-evolution taken in response.

**v7 addition**: `_shared_helpers.py` module in `code/` provides
common `tapered_bezier` / `tapered_line` helpers and NEW adaptive
primitives `variant_pie`, `variant_na`, `variant_dian` — these expose
angle / taper / width knobs that the frozen `(ox, oy, scale)`
signature cannot vary. Future B3+ bank entries should prefer these
adaptive helpers when a stroke's form differs from the standalone
primitive by more than uniform scaling. See `principles_stroke_family.md`
P11 and `form_catalog.md`.

## Batch B4 (2026-07-23, positions 201–250 judged + 8 retries)

27 main-curriculum PASSes recorded above (bank entries 114–140), plus
**1 retry graduation**: `zi_char.py` (entry 122) — 子 finally PASSed
on retry_1 after B3's inline-弯钩 fix. This is the **first non-zero
retry** since B1 (B2 0/8, B3 0/13; B4 1/8 = 12%). 23 main-curriculum
FAILs added to errata; 7 retry FAILs incremented. Overall main pass
rate 27/50 = **54%** (slight drop from B3's 58%), retry rate 1/8 = 12%,
cumulative through 250 items: **52%** — G1 no-memory sits at ~55%, so
G3 remains ~3pp below control. See `sandbox.md` "B4 diagnostic" and
`evolution.md` 2026-07-23 for the third-pass response.

**B4 helper-usage finding**: `grep -l "kiss_apex|pie_point|mirror_dian_pair"
attempts/*__retry_*/generated.py` returns ZERO. None of the 8 retries
used the B3-second-pass composition helpers — even 夂/夊/兀 whose
retry rationales explicitly cited them. The composition helpers exist
but retrievals from `memory_index.md` did not reach them under retry
prompts. Main attempts DO use them (6 files: 大, 个, 久, 亼, 夂, 及)
so the retrieval is not universally broken — it's the retry path that
skipped the helpers. This is the primary evolution lever for B5.

Naming policy for B4:
- Identity aliases (7): `dao_pang_char`, `xiao_char`, `wei_char`,
  `shan_char`, `gan_char`, `kou_char`, `cao_char`, `mian_char`.
- Alias-plus-decoration: `cha_char` (又+dian), `wu_char` (heng+儿).
- Pure bank composition: `ding_char`, `shang_char`, `xia_char`, `chu_char`,
  `yu_char`, `zi_char`, `san_char`.
- Fully inline / mixed (custom recipe): `diao_char`, `bao_char`,
  `nian_char`, `men_char`, `jie_char`, `wang_char`.
- Adaptive-helper-driven: `zhi_char`, `ya_char`, `jiu_long_char`,
  `ji_meet_char`.

## Batch B5 (2026-07-24, positions 251–300 judged + 17 retries)

19 main-curriculum PASSes recorded above (bank entries 141–159), plus
**1 retry graduation**: `ba_dot.py` (entry 161) — 丷 finally PASSed on
retry_4 by **explicitly REJECTING the recommended `mirror_dian_pair`
helper** and hand-rendering asymmetric per GT observation with thin
~4 px widths (P12). 31 main-curriculum FAILs added to errata; 16 retry
FAILs incremented; **3 items terminally frozen at retry_n=5**
(p2_radical_028_人, p2_radical_030_入, p2_radical_046_大 — see errata
top-section). Overall main pass rate 19/50 = **38%** (worst yet — drop
from B4's 54%); retry rate 1/17 = 6%. Cumulative through 300 items:
**49.6%**, first batch to drop below 50% and now ~3.8 pp below G1
no-memory (~53%).

**B5 helper-usage finding**: 17/17 retries wrote the RETRY-TIME
CHECKLIST header (Q1/Q2/Q3) AND imported at least one helper from
`_shared_helpers.py` (mean 6.5 helper calls each). The B4→B5 retrieval
fix is fully in place. Yet only 丷 PASSed — and it PASSed by REJECTING
its recommended helper. The other 16 retries followed the recommended
helper to the letter and failed. This **falsifies the helper-composition
hypothesis** for the X-crossing family (人, 入, 大, 义, 从, 天,
太-crotch, 火, 见, 长-捺). See `sandbox.md` "B5 diagnostic" and the
head curator's `evolution.md` 2026-07-24 entry for the honest reckoning.

B5 naming policy:
- Identity aliases (5): `gong_char`, `chuan_char`, `ri_char`,
  `xin_char`, `wen_char`.
- Alias-plus-nudge / compression: `chuan_char` (scale 1.15 nudge),
  `zhong` (kou at 0.55 + inline shu), `ding_ren` (compressed 亻 + 丁),
  `zhang_ren` (tall inline 亻 + bank 几).
- Pure inline / PIL-pixel recipe: `chu_radical_char`, `nian_horns`,
  `bu_char`, `qi_ji`, `yi_pron` (PIL-px), `zhu_top`, `gang` (PIL-px frame).
- Adaptive-helper-driven (variant_pie/na/dian, kiss_apex): `yi_ge`,
  `dan`, `bing_ren`, `tai_char`, `ba_dot` (graduated retry).
- `ba_dot` naming: the only retry graduate. Named _dot to disambiguate
  from `ba.py` (八 radical) and `ba_char.py` (八 char). Its docstring
  records the "reject the recommended helper" lesson as principle.
