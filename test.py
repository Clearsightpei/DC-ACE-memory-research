"""Test file for individual function testing.

Use this to quickly test a single drawing function before adding it to task_factory.py
"""

import os
import io
import math
import turtle
from PIL import Image

from chinese_strock import stroke_heng_zhe_zhe_pie

WIDTH = 800
HEIGHT = 600
OUT_DIR = "/Users/peilinwu/Documents/AI memory research"

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
        print(f"✅ Saved: {path}")
    except Exception as e:
        print(f"❌ Error saving {path}: {e}")


def stroke_wan_gou(t: turtle.Turtle, size: float):
    """弯钩 ㇁ - Arc bulging right, hook left-up."""
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


# ==========================================
# Main Test Function
# ==========================================

def test_function():
    """Main test function - modify this to test different functions."""

    # Create output directory
    os.makedirs(OUT_DIR, exist_ok=True)

    # Setup turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    turtle.tracer(0, 0)  # Turn off animation for faster rendering

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")

    # Test position (center of screen)
    test_x = 0
    test_y = 0

    # Move to test position
    t.penup()
    t.goto(test_x, test_y)
    t.pendown()

    stroke_wan_gou(t, 100)

    # Example 2: Test Chinese character 人 (Person)
    # draw_chinese_person(t, 100)

    # Example 3: Test simple rectangle
    # draw_test_rectangle(t, 100, 150, "blue")

    # Example 4: Test individual stroke
    # stroke_heng(t, 80)

    # ==========================================

    # Update screen and save
    turtle.update()
    output_path = os.path.join(OUT_DIR, "test_output.png")
    save_canvas_to_png(screen, output_path)

    print(f"\n🎨 Test complete!")
    print(f"📁 Output saved to: {output_path}")
    print(f"📍 Position: ({test_x}, {test_y})")

    # Close turtle window
    try:
        turtle.done()
    except:
        pass

if __name__ == "__main__":
    print("🧪 Starting function test...")
    test_function()
