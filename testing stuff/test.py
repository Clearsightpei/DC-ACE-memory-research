import os
import io
import sys
import turtle
import importlib.util
import inspect
from PIL import Image

# 1. Setup paths
RESEARCH_PATH = "/Users/peilinwu/Documents/AI memory research"
GEN_FILE_PATH = os.path.join(RESEARCH_PATH, "generated_characters.py")
REPORT_DIR = os.path.join(RESEARCH_PATH, "visual_reports")

if RESEARCH_PATH not in sys.path:
    sys.path.append(RESEARCH_PATH)

# ==========================================
# Dynamic Import & Rendering
# ==========================================

def get_all_draw_functions(file_path):
    """Dynamically loads the file and returns all functions starting with 'draw_'."""
    spec = importlib.util.spec_from_file_location("generated_characters", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [
        (name, func) for name, func in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("draw_")
    ]

def save_canvas_to_png(screen, path):
    """Saves current canvas to PNG using Ghostscript."""
    canvas = screen.getcanvas()
    try:
        ps = canvas.postscript(colormode="color")
        img = Image.open(io.BytesIO(ps.encode("utf-8")))
        img.save(path, "PNG")
    except Exception as e:
        print(f"❌ Error saving {os.path.basename(path)}: {e}")

def run_batch_generation():
    """Generates individual PNGs for all detected functions."""
    # Create the target folder
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    print(f"🧪 Scanning {os.path.basename(GEN_FILE_PATH)}...")
    draw_funcs = get_all_draw_functions(GEN_FILE_PATH)
    print(f"📂 Output Folder: {REPORT_DIR}")
    print(f"🎨 Found {len(draw_funcs)} characters to render.")

    # Setup Turtle once
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor("white")
    turtle.tracer(0, 0)
    
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)

    for name, func in draw_funcs:
        # Clear for the next character
        t.clear()
        t.penup()
        t.goto(0, 0)
        t.setheading(90)
        t.pendown()
        
        print(f"🖌️  Drawing: {name}...", end="\r")
        
        try:
            # Execute the character drawing
            func(t)
            turtle.update()
            
            # Save to its own file
            file_path = os.path.join(REPORT_DIR, f"{name}.png")
            save_canvas_to_png(screen, file_path)
        except Exception as e:
            print(f"\n⚠️  Failed to draw {name}: {e}")

    print(f"\n✅ Batch complete! {len(draw_funcs)} files in /visual_reports/")
    # Keep the window from hanging if run in an IDE
    try:
        turtle.bye()
    except:
        pass

if __name__ == "__main__":
    run_batch_generation()