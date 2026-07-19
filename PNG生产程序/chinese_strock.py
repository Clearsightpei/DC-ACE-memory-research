"""Chinese Stroke Library for DC-ACE Research.

Implements the "Physics" of Chinese characters using relative vectors.
Generates 32 strokes (6 Basic + 26 Compound) with 5 samples each.
"""

import os
import io
import math
import random
import json
import turtle
from PIL import Image
import re
import random
import numpy as np

WIDTH = 800
HEIGHT = 600
OUT_DIR = "/Users/peilinwu/Documents/AI memory research/chinese_strokes_dataset"

# ==========================================
# Core Rendering Functions
# ==========================================

def save_canvas_to_png(screen: turtle.Screen, path: str) -> None:
    """Save the current turtle screen to a PNG using postscript + PIL."""
    canvas = screen.getcanvas()
    try:
        ps = canvas.postscript(colormode="color")
        b = io.BytesIO(ps.encode("utf-8"))
        img = Image.open(b)
        img.load(scale=1)
        rgba = img.convert("RGBA")
        rgba.save(path, "PNG")
    except Exception as e:
        print(f"Error saving {path}: {e}")

# ==========================================
# Part 1: The 6 Basic Strokes (原子笔画)
# ==========================================

def stroke_dian(t: turtle.Turtle, size: float):
    """点 (Dot) - Teardrop shape at 315° (South-East)."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(315)
    t.pendown()
    # Teardrop: thick start, sharp end
    for i in range(int(0.2 * size)):
        t.pensize(max(1, 5 - i // 2))
        t.forward(1)

    # Reset
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng(t: turtle.Turtle, size: float):
    """横 (Horizontal) - Straight line at 0° (East) with slight upward tilt."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(5)  # Slight upward tilt
    t.pendown()
    t.forward(size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_shu(t: turtle.Turtle, size: float):
    """竖 (Vertical) - Straight line at 270° (South)."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_pie(t: turtle.Turtle, size: float):
    """撇 (Throw) - Curved sweep from 260° to 200° (South-West)."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(260)
    t.pendown()
    # Curve towards 200°
    for i in range(60):
        t.forward(size / 60)
        t.right(1)  # Gradual curve
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_na(t: turtle.Turtle, size: float):
    """捺 (Press) - Curved sweep from 300° to 340° (South-East)."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(300)
    t.pendown()
    # Curve towards 340°
    for i in range(40):
        t.forward(size / 40)
        t.left(1)  # Gradual curve
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_ti(t: turtle.Turtle, size: float):
    """提 (Rise) - Sharp straight line at 30° (North-East)."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(30)
    t.pendown()
    t.forward(0.8 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

# ==========================================
# Part 2: The 26 Compound Strokes (复合折笔)
# ==========================================

# Group A: Right-Angle Folds (方折)

def stroke_heng_zhe(t: turtle.Turtle, size: float):
    """横折 ┐ - Horizontal then vertical right angle."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(size)
    t.setheading(270)
    t.forward(0.9 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_pie(t: turtle.Turtle, size: float):
    """横撇 ㇇ - Horizontal then throw."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(0.8 * size)
    t.setheading(225)
    # Curved throw
    for i in range(40):
        t.forward(1.2 * size / 40)
        t.right(0.5)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_gou(t: turtle.Turtle, size: float):
    """横钩 乛 - Horizontal with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    # Slight arch down
    for i in range(int(size)):
        t.forward(1)
        if i < size / 2:
            t.right(0.1)
        else:
            t.left(0.1)
    # Sharp hook
    t.setheading(225)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_zhe_gou(t: turtle.Turtle, size: float):
    """横折钩 - Horizontal, vertical, hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(size)
    t.setheading(270)
    t.forward(2.5 * size)
    t.setheading(135)
    t.forward(0.3 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_zhe_ti(t: turtle.Turtle, size: float):
    """横折提 ㇊ - Horizontal, vertical, then rise."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(size)
    t.setheading(270)
    t.forward(1.5 * size)
    t.setheading(30)
    t.forward(0.6 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)


def stroke_heng_zhe_zhe(t: turtle.Turtle, size: float):
    """横折折 ㇅ - Two right angles."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(size)
    t.setheading(270)
    t.forward(0.8 * size)
    t.setheading(0)
    t.forward(0.8 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_xie_gou(t: turtle.Turtle, size: float):
    """横斜钩 ⺄ - Horizontal, slanted curve with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(0.8 * size)
    # Slanted curve
    t.setheading(270)  
    t.circle(2.4 * size, 40)
    # Hook up
    t.setheading(90)
    t.forward(0.2 * size)
    t.penup()
    
def stroke_heng_zhe_wan_gou(t: turtle.Turtle, size: float):
    """横折弯钩 ㇈ - Horizontal, slant, curve, hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(10)
    t.pendown()
    t.forward(0.7 * size)
    t.setheading(260)
    t.forward(1 * size)
    # Curve to east
    t.setheading(-30)
    t.circle(1 * size, 60)
    # Hook up
    t.setheading(95)
    t.forward(0.1 * size)
    t.penup()
    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_pie_wan_gou(t: turtle.Turtle, size: float):
    """横撇弯钩 ㇌ - Short horizontal, throw, belly curve, hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(1.9 * size)
    t.setheading(240)
    t.forward(1.75 * size)
    # Belly curve
    t.setheading(-45)
    t.circle(-2.5 * size, 60)
    # Hook
    t.setheading(145)
    t.forward(0.75 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_zhe_zhe_pie(t: turtle.Turtle, size: float):
    """横折折撇 ㇋ - Horizontal, slant down, slide right, long throw."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(0)
    t.pendown()
    t.forward(0.25 * size)
    t.setheading(240)
    t.forward(0.3 * size)
    t.setheading(0)
    t.forward(0.1 * size)
    t.setheading(90)
    t.circle(0.4 * size, -80)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_zhe_zhe_zhe_gou(t: turtle.Turtle, size: float):
    """横折折折钩 𠄎 - Multiple folds with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(8)
    t.pendown()
    t.forward(1.8 * size)
    t.setheading(250)
    t.forward(1.5 * size)
    t.setheading(0)
    t.forward(0.72 * size)
    t.setheading(270)
    t.circle(-6 * size, 20)
    # Hook up
    t.setheading(120)
    t.forward(0.6 * size)
    t.penup()
    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_heng_zhe_zhe_zhe(t: turtle.Turtle, size: float):
    """横折折折 ㇎ - Same as above but no hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(8)
    t.pendown()
    t.forward(1.8 * size)
    t.setheading(250)
    t.forward(1.5 * size)
    t.setheading(0)
    t.forward(0.72 * size)
    t.setheading(270)
    t.circle(-6 * size, 20)
    t.penup()
    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

# Group B: Vertical-Based Folds (竖折)

def stroke_shu_ti(t: turtle.Turtle, size: float):
    """竖提 𠄌 - Long vertical then rise."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(1.5 * size)
    t.setheading(30)
    t.forward(0.6 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_shu_zhe(t: turtle.Turtle, size: float):
    """竖折 𠃊 - Vertical then horizontal."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(size)
    t.setheading(0)
    t.forward(1.5 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_shu_gou(t: turtle.Turtle, size: float):
    """竖钩 亅 - Long vertical with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(2.0 * size)
    t.setheading(135)
    t.forward(0.3 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)


def stroke_shu_wan_gou(t: turtle.Turtle, size: float):
    """竖弯钩 乚 - Vertical, curve, horizontal, hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(size)
    t.circle(0.3 * size, 90)
    t.setheading(0)
    t.circle(3 * size, 10)
    t.setheading(90)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_shu_zhe_pie(t: turtle.Turtle, size: float):
    """竖折撇 ㄣ - Vertical, horizontal, then throw."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(250)
    t.pendown()
    t.forward(1.0 * size)
    t.setheading(0)
    t.forward(0.8 * size)
    t.setheading(250)
    t.forward(1 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_shu_zhe_zhe(t: turtle.Turtle, size: float):
    """竖折折 𠃑 - Vertical, horizontal, vertical."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.forward(size)
    t.setheading(0)
    t.forward(0.8 * size)
    t.setheading(270)
    t.forward(0.8 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)


def stroke_shu_zhe_zhe_gou(t: turtle.Turtle, size: float):
    """竖折折钩 ㇉ - Vertical, horizontal, vertical, hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(250)
    t.pendown()
    t.forward(0.8 * size)
    t.setheading(0)
    t.forward(0.6 * size)
    t.setheading(90)
    t.circle(3.0 * size, -20)
    t.setheading(135)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

# Group C: Slanted & Curved Hooks (斜弯折)

def stroke_pie_dian(t: turtle.Turtle, size: float):
    """撇点 𡿨 - Throw then long dot."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(225)
    t.pendown()
    t.forward(size)
    t.setheading(315)
    t.forward(1.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_pie_zhe(t: turtle.Turtle, size: float):
    """撇折 𠃋 - Throw then rise."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(225)
    t.pendown()
    t.forward(size)
    t.setheading(0)
    t.forward(0.8 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_xie_gou(t: turtle.Turtle, size: float):
    """斜钩 ㇂ - Long convex arc with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.circle(2.7 * size, 30)
    # Hook up
    t.setheading(90)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_wan_gou(t: turtle.Turtle, size: float):
    """弯钩 ㇁ - Arc bulging right, hook left-up."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()

    t.setheading(270)
    t.pendown()
    t.circle(-3 * size, 20)
    # Hook up
    t.setheading(110)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

def stroke_wo_gou(t: turtle.Turtle, size: float):
    """卧钩 ㇃ - Lying curve with hook."""
    t.pencolor("black")
    t.pensize(3)
    start_x, start_y = t.position()
    t.setheading(-45)
    t.pendown()
    t.circle(1.5 * size, 60)
    # Hook
    t.setheading(135)
    t.forward(0.2 * size)
    t.penup()

    # Reset
    t.goto(start_x, start_y)
    t.setheading(90)
    t.pensize(1)

# ==========================================
# Generator Class
# ==========================================

class ChineseStrokeGenerator:
    def __init__(self, seed: int | None = None):
        if seed is not None:
            random.seed(seed)
        os.makedirs(OUT_DIR, exist_ok=True)
        self.screen = turtle.Screen()
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.bgcolor("white")
        turtle.tracer(0, 0)
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.metadata = []
        self.counters = {}

    def _get_id(self, prefix):
        if prefix not in self.counters:
            self.counters[prefix] = 0
        self.counters[prefix] += 1
        return f"{prefix}_{self.counters[prefix]}"

    def _rand_pos(self, margin):
        x = random.uniform(-WIDTH/2 + margin, WIDTH/2 - margin)
        y = random.uniform(-HEIGHT/2 + margin, HEIGHT/2 - margin)
        return x, y

    def _save(self, fname, level, prompt, params):
        turtle.update()
        save_canvas_to_png(self.screen, os.path.join(OUT_DIR, fname))
        self.metadata.append({
            "id": fname,
            "level": level,
            "prompt": prompt,
            "params": params
        })
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.pendown()

    def generate_all(self):
        print("🖌️  Generating Chinese Strokes (30 types × 5 samples)...")

        # All 32 strokes with metadata
        strokes = [
            # Basic Strokes (6)
            ("Dian", "点", "dot", stroke_dian, (10, 25)),
            ("Heng", "横", "horizontal", stroke_heng, (40, 100)),
            ("Shu", "竖", "vertical", stroke_shu, (40, 100)),
            ("Pie", "撇", "throw/left-falling", stroke_pie, (40, 100)),
            ("Na", "捺", "press/right-falling", stroke_na, (40, 100)),
            ("Ti", "提", "rise", stroke_ti, (40, 100)),

            # Compound Strokes Group A (13)
            ("HengZhe", "横折", "horizontal-vertical fold", stroke_heng_zhe, (40, 80)),
            ("HengPie", "横撇", "horizontal-throw", stroke_heng_pie, (40, 80)),
            ("HengGou", "横钩", "horizontal hook", stroke_heng_gou, (40, 80)),
            ("HengZheGou", "横折钩", "horizontal-vertical-hook", stroke_heng_zhe_gou, (30, 60)),
            ("HengZheTi", "横折提", "horizontal-vertical-rise", stroke_heng_zhe_ti, (30, 60)),
            ("HengZheZhe", "横折折", "horizontal double fold", stroke_heng_zhe_zhe, (30, 60)),
            ("HengXieGou", "横斜钩", "horizontal slant hook", stroke_heng_xie_gou, (30, 60)),
            ("HengZheWanGou", "横折弯钩", "horizontal fold curve hook", stroke_heng_zhe_wan_gou, (30, 60)),
            ("HengPieWanGou", "横撇弯钩", "horizontal throw curve hook", stroke_heng_pie_wan_gou, (30, 60)),
            ("HengZheZhePie", "横折折撇", "horizontal double fold throw", stroke_heng_zhe_zhe_pie, (30, 60)),
            ("HengZheZheZheGou", "横折折折钩", "horizontal triple fold hook", stroke_heng_zhe_zhe_zhe_gou, (25, 50)),
            ("HengZheZheZhe", "横折折折", "horizontal triple fold", stroke_heng_zhe_zhe_zhe, (25, 50)),

            # Compound Strokes Group B (8)
            ("ShuTi", "竖提", "vertical-rise", stroke_shu_ti, (30, 60)),
            ("ShuZhe", "竖折", "vertical-horizontal fold", stroke_shu_zhe, (30, 60)),
            ("ShuGou", "竖钩", "vertical hook", stroke_shu_gou, (40, 80)),
            ("ShuWanGou", "竖弯钩", "vertical curve hook", stroke_shu_wan_gou, (30, 60)),
            ("ShuZhePie", "竖折撇", "vertical fold throw", stroke_shu_zhe_pie, (30, 60)),
            ("ShuZheZhe", "竖折折", "vertical double fold", stroke_shu_zhe_zhe, (30, 60)),
            ("ShuZheZheGou", "竖折折钩", "vertical double fold hook", stroke_shu_zhe_zhe_gou, (30, 60)),

            # Compound Strokes Group C (5)
            ("PieDian", "撇点", "throw-dot", stroke_pie_dian, (30, 60)),
            ("PieZhe", "撇折", "throw-rise", stroke_pie_zhe, (30, 60)),
            ("XieGou", "斜钩", "slant hook", stroke_xie_gou, (40, 80)),
            ("WanGou", "弯钩", "curved hook", stroke_wan_gou, (40, 80)),
            ("WoGou", "卧钩", "lying hook", stroke_wo_gou, (40, 80)),
        ]

        # Generate all strokes once per round, 5 rounds total
        # Order: dian_1, heng_1, ...(all strokes)..., dian_2, heng_2, ...
        for sample_num in range(1, 3):
            for name_en, char, meaning, func, size_range in strokes:
                size = random.uniform(size_range[0], size_range[1])
                x, y = self._rand_pos(max(size * 3, 100))

                self.t.penup()
                self.t.goto(x, y)
                self.t.pendown()

                func(self.t, size)

                self._save(
                    self._get_id(f"L1_Stroke_{name_en}") + ".png",
                    1,
                    f"Draw Chinese stroke {char} ({name_en}/{meaning}) size {int(size)} at ({int(x)},{int(y)})",
                    {
                        "type": f"stroke_{name_en.lower()}",
                        "stroke": char,
                        "pinyin": name_en.lower(),
                        "meaning": meaning,
                        "size": size,
                        "x": x,
                        "y": y
                    }
                )

        # Save metadata
        metadata_path = os.path.join(OUT_DIR, "chinese_strokes.json")
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)

        print(f"✅ Generated {len(self.metadata)} Chinese stroke samples.")
        print(f"📊 Metadata saved to {metadata_path}")

        try:
            self.screen.bye()
        except:
            pass

if __name__ == "__main__":
    gen = ChineseStrokeGenerator()
    gen.generate_all()
