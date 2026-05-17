"""Atomic and compound Chinese strokes as turtle functions.

Vendored from PNG生产程序/chinese_strock.py for self-containment.
Each function draws one stroke at the turtle's current position
and returns it to the start position with heading 90.
"""

import turtle


def stroke_dian(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(315); t.pendown()
    for i in range(int(0.2 * size)):
        t.pensize(max(1, 5 - i // 2))
        t.forward(1)
    t.penup(); t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(5); t.pendown(); t.forward(size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_shu(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.forward(size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_pie(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(260); t.pendown()
    for _ in range(60):
        t.forward(size / 60); t.right(1)
    t.penup(); t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_na(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(300); t.pendown()
    for _ in range(40):
        t.forward(size / 40); t.left(1)
    t.penup(); t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_ti(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(30); t.pendown(); t.forward(0.8 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng_zhe(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(0); t.pendown(); t.forward(size)
    t.setheading(270); t.forward(0.9 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng_pie(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(0); t.pendown(); t.forward(0.8 * size)
    t.setheading(225)
    for _ in range(40):
        t.forward(1.2 * size / 40); t.right(0.5)
    t.penup(); t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(0); t.pendown()
    for i in range(int(size)):
        t.forward(1)
        if i < size / 2: t.right(0.1)
        else: t.left(0.1)
    t.setheading(225); t.forward(0.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng_zhe_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(0); t.pendown(); t.forward(size)
    t.setheading(270); t.forward(2.5 * size)
    t.setheading(135); t.forward(0.3 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_heng_zhe_ti(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(0); t.pendown(); t.forward(size)
    t.setheading(270); t.forward(1.5 * size)
    t.setheading(30); t.forward(0.6 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_shu_ti(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.forward(1.5 * size)
    t.setheading(30); t.forward(0.6 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_shu_zhe(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.forward(size)
    t.setheading(0); t.forward(1.5 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_shu_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.forward(2.0 * size)
    t.setheading(135); t.forward(0.3 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_shu_wan_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.forward(size)
    t.circle(0.3 * size, 90)
    t.setheading(0); t.circle(3 * size, 10)
    t.setheading(90); t.forward(0.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_xie_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.circle(2.7 * size, 30)
    t.setheading(90); t.forward(0.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_wan_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(270); t.pendown(); t.circle(-3 * size, 20)
    t.setheading(110); t.forward(0.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_pie_dian(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(225); t.pendown(); t.forward(size)
    t.setheading(315); t.forward(1.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_pie_zhe(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(225); t.pendown(); t.forward(size)
    t.setheading(0); t.forward(0.8 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


def stroke_wo_gou(t: turtle.Turtle, size: float):
    t.pencolor("black"); t.pensize(3)
    sx, sy = t.position()
    t.setheading(-45); t.pendown(); t.circle(1.5 * size, 60)
    t.setheading(135); t.forward(0.2 * size); t.penup()
    t.goto(sx, sy); t.setheading(90); t.pensize(1)


STROKES = {
    "dian":              {"fn": stroke_dian,         "char": "点",   "meaning": "dot",                       "size_range": (10, 25)},
    "heng":              {"fn": stroke_heng,         "char": "横",   "meaning": "horizontal",                "size_range": (40, 100)},
    "shu":               {"fn": stroke_shu,          "char": "竖",   "meaning": "vertical",                  "size_range": (40, 100)},
    "pie":               {"fn": stroke_pie,          "char": "撇",   "meaning": "throw",                     "size_range": (40, 100)},
    "na":                {"fn": stroke_na,           "char": "捺",   "meaning": "press",                     "size_range": (40, 100)},
    "ti":                {"fn": stroke_ti,           "char": "提",   "meaning": "rise",                      "size_range": (40, 100)},
    "heng_zhe":          {"fn": stroke_heng_zhe,     "char": "横折", "meaning": "horizontal-fold",           "size_range": (40, 80)},
    "heng_pie":          {"fn": stroke_heng_pie,     "char": "横撇", "meaning": "horizontal-throw",          "size_range": (40, 80)},
    "heng_gou":          {"fn": stroke_heng_gou,     "char": "横钩", "meaning": "horizontal-hook",           "size_range": (40, 80)},
    "heng_zhe_gou":      {"fn": stroke_heng_zhe_gou, "char": "横折钩","meaning": "horizontal-fold-hook",     "size_range": (30, 60)},
    "heng_zhe_ti":       {"fn": stroke_heng_zhe_ti,  "char": "横折提","meaning": "horizontal-fold-rise",     "size_range": (30, 60)},
    "shu_ti":            {"fn": stroke_shu_ti,       "char": "竖提", "meaning": "vertical-rise",             "size_range": (30, 60)},
    "shu_zhe":           {"fn": stroke_shu_zhe,      "char": "竖折", "meaning": "vertical-fold",             "size_range": (30, 60)},
    "shu_gou":           {"fn": stroke_shu_gou,      "char": "竖钩", "meaning": "vertical-hook",             "size_range": (40, 80)},
    "shu_wan_gou":       {"fn": stroke_shu_wan_gou,  "char": "竖弯钩","meaning": "vertical-curve-hook",      "size_range": (30, 60)},
    "xie_gou":           {"fn": stroke_xie_gou,      "char": "斜钩", "meaning": "slant-hook",                "size_range": (40, 80)},
    "wan_gou":           {"fn": stroke_wan_gou,      "char": "弯钩", "meaning": "curved-hook",               "size_range": (40, 80)},
    "pie_dian":          {"fn": stroke_pie_dian,     "char": "撇点", "meaning": "throw-dot",                 "size_range": (30, 60)},
    "pie_zhe":           {"fn": stroke_pie_zhe,      "char": "撇折", "meaning": "throw-rise",                "size_range": (30, 60)},
    "wo_gou":            {"fn": stroke_wo_gou,       "char": "卧钩", "meaning": "lying-hook",                "size_range": (40, 80)},
}
