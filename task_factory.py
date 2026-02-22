"""Task factory for Project LOGO-EVO.

Generates procedural turtle/logo tasks and saves ground-truth PNGs and metadata.
"""

import os
import io
import math
import random
import json
import turtle
from PIL import Image

WIDTH = 800
HEIGHT = 600
# Save dataset into user's Documents folder as requested
OUT_DIR = "/Users/peilinwu/Documents/AI memory research/dataset_pilot"

COLORS = [
    "red", "green", "blue", "orange", "purple",
    "brown", "black", "cyan", "magenta", "gold", "navy", "lime"
]

# ==========================================
# 1. Core Rendering & Helper Functions
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

def _move_centered(t: turtle.Turtle, cx: float, cy: float):
    t.penup()
    t.goto(cx, cy)
    t.pendown()

# ==========================================
# 2. Level 1 Primitives
# ==========================================

def draw_regular_polygon(t: turtle.Turtle, n: int, size: float, color: str):
    """Draws a regular polygon, rotating it to sit 'flat' on the bottom."""
    if n < 3: return
    cx, cy = t.position()
    apothem = size / (2 * math.tan(math.pi / n))
    
    # Move to center-bottom edge
    t.penup()
    t.goto(cx, cy)
    t.setheading(270) # Down
    t.forward(apothem)
    t.left(90) # Face right
    t.backward(size/2) # Move to corner
    
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.forward(size)
        t.left(360.0 / n)
    t.end_fill()
    
    # Reset
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_circle(t: turtle.Turtle, size: float, color: str):
    """Draw a filled circle with `size` as diameter."""
    r = size / 2.0
    cx, cy = t.position()
    t.penup(); t.goto(cx, cy - r); t.setheading(0); t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_rectangle(t: turtle.Turtle, width: float, height: float, color: str):
    """Draws a centered rectangle."""
    cx, cy = t.position()
    t.penup(); t.goto(cx - width/2, cy - height/2); t.setheading(0); t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width); t.left(90)
        t.forward(height); t.left(90)
    t.end_fill()
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_star(t: turtle.Turtle, size: float, color: str):
    """Draw a centered 5-point star."""
    cx, cy = t.position()
    outer = size / 2.0
    inner = outer * 0.382
    points = []
    for i in range(10):
        angle = math.pi/2 + i * (math.pi/5)
        r = outer if i % 2 == 0 else inner
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    
    t.penup(); t.goto(points[0]); t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for p in points[1:]: t.goto(p)
    t.goto(points[0])
    t.end_fill()
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_leaf(t: turtle.Turtle, size: float, angle_deg: int, color: str):
    """Draws a leaf starting from current position (stem), growing outward."""
    step = max(0.5, size * 0.02)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        for _ in range(angle_deg):
            t.forward(step)
            t.right(1)
        t.right(180 - angle_deg)
    t.end_fill()

# ==========================================
# 3. Level 2 Compound Shapes
# ==========================================

def draw_flower(t, petal_count, petal_size, angle_deg, colors):
    """Spirograph-style flower where petals share a center."""
    cx, cy = t.position()
    rot = 360.0 / petal_count
    for i in range(petal_count):
        t.penup(); t.goto(cx, cy); t.setheading(i * rot); t.pendown()
        col = colors[i % len(colors)]
        draw_leaf(t, petal_size, angle_deg, col)
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_house(t, size, c1, c2):
    cx, cy = t.position()
    draw_regular_polygon(t, 4, size, c1)
    # Roof
    t.penup(); t.goto(cx, cy + size/2); t.pendown()
    # Move up to center of triangle roof
    tri_r = size * math.sqrt(3) / 6
    t.penup(); t.goto(cx, cy + size/2 + tri_r); t.pendown()
    draw_regular_polygon(t, 3, size, c2)
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_badge(t, size, c1, c2):
    draw_circle(t, size, c1)
    draw_star(t, size*0.6, c2)

def draw_window(t, size, c1, c2):
    draw_regular_polygon(t, 4, size, c1)
    gap = size * 0.05
    pane = (size - 3*gap)/2
    cx, cy = t.position()
    off = pane/2 + gap/2
    for dx in [-off, off]:
        for dy in [-off, off]:
            t.penup(); t.goto(cx+dx, cy+dy); t.pendown()
            draw_regular_polygon(t, 4, pane, c2)
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_snowman(t, bottom, color="white"):
    cx, cy = t.position()
    y = cy - bottom/2
    for s in [bottom, bottom*0.7, bottom*0.5]:
        t.penup(); t.goto(cx, y + s/2); t.pendown()
        draw_circle(t, s, color)
        y += s
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_pine_tree(t, size):
    cx, cy = t.position()
    t.penup(); t.goto(cx, cy - size*0.25); t.pendown()
    draw_rectangle(t, size*0.2, size*0.25, "brown")
    for i in range(3):
        y = cy - size*0.05 + i*(size*0.18)
        t.penup(); t.goto(cx, y); t.pendown()
        draw_regular_polygon(t, 3, size*(1-i*0.2), "green")

def draw_ice_cream(t: turtle.Turtle, size: float, flavor: str):
    """Draws an ice cream: An inverted triangle (cone) with a circle (scoop) sitting on the flat top."""
    cx, cy = t.position()
    
    # 1. Draw Cone (Inverted Triangle)
    # We want the flat side on TOP.
    height = size * math.sqrt(3) / 2
    half_w = size / 2
    
    # Vertices relative to center (cx, cy)
    top_left = (cx - half_w, cy + height/2)
    top_right = (cx + half_w, cy + height/2)
    bottom_tip = (cx, cy - height/2)
    
    t.penup(); t.goto(top_left); t.pendown()
    t.fillcolor("orange") # Cone color
    t.begin_fill()
    t.goto(top_right)
    t.goto(bottom_tip)
    t.goto(top_left)
    t.end_fill()
    
    # 2. Draw Scoop (Circle)
    # It sits on the flat top line.
    # Center of circle should be: top_y + radius - small_overlap
    scoop_radius = size * 0.4
    scoop_center_y = (cy + height/2) + scoop_radius * 0.8 # 0.8 to sink it in slightly
    
    t.penup()
    t.goto(cx, scoop_center_y - scoop_radius) # Move to bottom of circle
    t.setheading(0)
    t.pendown()
    t.fillcolor(flavor)
    t.begin_fill()
    t.circle(scoop_radius)
    t.end_fill()
    
    # Reset
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()





def draw_traffic_light(t, h):
    cx, cy = t.position()
    w = h/3
    draw_rectangle(t, w, h, "grey")
    gap = h/4
    y = cy + gap
    for c in ["red", "yellow", "green"]:
        t.penup(); t.goto(cx, y); t.pendown()
        draw_circle(t, w*0.6, c)
        y -= gap
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_rocket(t, w, h, c):
    cx, cy = t.position()
    draw_rectangle(t, w, h, c)
    # Nose
    t.penup(); t.goto(cx, cy + h/2 + w*0.4); t.pendown() # approximate center for nose
    draw_regular_polygon(t, 3, w, "red")
    # Fin
    t.penup(); t.goto(cx, cy - h/2 - w*0.2); t.pendown()
    draw_regular_polygon(t, 3, w*0.8, "red")
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_dumbbell(t, size):
    cx, cy = t.position()
    draw_rectangle(t, size*3, size*0.2, "grey")
    for x in [cx - size*1.5 - size/2, cx + size*1.5 + size/2]:
        t.penup(); t.goto(x, cy); t.pendown()
        draw_regular_polygon(t, 4, size, "black")
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_glasses(t, size):
    cx, cy = t.position()
    draw_rectangle(t, size*0.6, size*0.1, "black") # Bridge
    for dx in [-size*0.9, size*0.9]:
        t.penup(); t.goto(cx + dx, cy); t.pendown()
        draw_circle(t, size, "blue")
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_car(t, length, color):
    cx, cy = t.position()
    h = length/2
    draw_rectangle(t, length, h, color)
    wy = cy - h/2
    for dx in [-length/3, length/3]:
        t.penup(); t.goto(cx+dx, wy); t.pendown()
        draw_circle(t, h/2, "black")
    t.penup(); t.goto(cx, cy); t.pendown()

def draw_bowtie(t: turtle.Turtle, size: float, color: str):
    """Draws a bowtie: Left Triangle(>) + Square + Right Triangle(<)."""
    cx, cy = t.position()
    
    # 1. Center Square
    # draw_regular_polygon draws flat bottom. Let's just draw manually to be safe & centered.
    half_s = size / 2
    t.penup(); t.goto(cx - half_s, cy - half_s); t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size); t.left(90)
    t.end_fill()
    
    # Triangle Height (for equilateral)
    tri_h = size * math.sqrt(3) / 2
    
    # 2. Left Triangle (Pointing Right >)
    # Vertex touches square at (cx - half_s, cy)
    vertex_x = cx - half_s
    base_x = vertex_x - tri_h
    t.penup(); t.goto(vertex_x, cy); t.pendown()
    t.begin_fill()
    t.goto(base_x, cy + half_s) # Top Left
    t.goto(base_x, cy - half_s) # Bottom Left
    t.goto(vertex_x, cy)        # Back to vertex
    t.end_fill()
    
    # 3. Right Triangle (Pointing Left <)
    # Vertex touches square at (cx + half_s, cy)
    vertex_x = cx + half_s
    base_x = vertex_x + tri_h
    t.penup(); t.goto(vertex_x, cy); t.pendown()
    t.begin_fill()
    t.goto(base_x, cy + half_s) # Top Right
    t.goto(base_x, cy - half_s) # Bottom Right
    t.goto(vertex_x, cy)        # Back to vertex
    t.end_fill()

    # Reset
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_candy(t: turtle.Turtle, size: float, color: str):
    """Draws a candy: Triangle(>) + Circle + Triangle(<)."""
    cx, cy = t.position()
    radius = size / 2
    
    # 1. Center Circle
    draw_circle(t, size, color)
    
    # Triangle Geometry
    # We want them to look like wrappers, slightly smaller than the candy body usually looks good, 
    # but prompt asked for same side length logic. Let's match size.
    tri_h = size * math.sqrt(3) / 2
    half_s = size / 2
    
    # 2. Left Wrapper (Pointing Right >)
    # Vertex touches circle at (cx - radius, cy)
    vertex_x = cx - radius
    base_x = vertex_x - tri_h
    t.penup(); t.goto(vertex_x, cy); t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(base_x, cy + half_s)
    t.goto(base_x, cy - half_s)
    t.goto(vertex_x, cy)
    t.end_fill()
    # 3. Right Wrapper (Pointing Left <)
    vertex_x = cx + radius
    base_x = vertex_x + tri_h
    t.penup(); t.goto(vertex_x, cy); t.pendown()
    t.begin_fill()
    t.goto(base_x, cy + half_s)
    t.goto(base_x, cy - half_s)
    t.goto(vertex_x, cy)
    t.end_fill()

    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_tv(t, w):
    draw_rectangle(t, w, w*0.7, "black")
    draw_rectangle(t, w*0.8, w*0.7*0.8, "blue")

def draw_donut(t, size):
    draw_circle(t, size, "brown")
    draw_circle(t, size*0.4, "white")

def draw_target(t, size):
    draw_regular_polygon(t, 4, size, "red")
    draw_regular_polygon(t, 4, size*0.6, "white")
    draw_regular_polygon(t, 4, size*0.3, "red")

def draw_framed_star(t, size, c):
    draw_regular_polygon(t, 4, size, "black")
    draw_star(t, size*0.5, c)

def draw_door(t, w, h, c):
    cx, cy = t.position()
    draw_rectangle(t, w, h, c)
    t.penup(); t.goto(cx + w*0.3, cy); t.pendown()
    draw_circle(t, w*0.1, "gold")
    t.penup(); t.goto(cx, cy); t.pendown()


def draw_butterfly(t, size, color):
    """4 leaves as wings."""
    cx, cy = t.position()
    # Top wings
    for ang in [30, 330]:
        t.setheading(ang)
        draw_leaf(t, size, 90, color)
        t.penup(); t.goto(cx, cy); t.pendown()
    # Bottom wings
    for ang in [150, 210]:
        t.setheading(ang)
        draw_leaf(t, size*0.7, 70, color)
        t.penup(); t.goto(cx, cy); t.pendown()
    t.setheading(90)

def draw_sun(t, r):
    draw_circle(t, r*2, "yellow")
    cx, cy = t.position()
    
    ray_length = r * 0.5
    ray_width = r * 0.15  # Slightly thicker for better visibility
    
    for i in range(8):
        t.penup()
        t.goto(cx, cy)
        angle = i * 45
        t.setheading(angle)
        
        # 1. Move exactly to the edge of the circle (Radius = r)
        t.forward(r) 
        
        # 2. Offset to the corner so the ray is centered on this angle
        t.left(90)
        t.forward(ray_width / 2)
        t.right(90) # Now facing the correct outward direction again
        
        t.pendown()
        t.fillcolor("orange")
        t.begin_fill()
        
        # 3. Draw the Ray (Manual rectangle to preserve rotation)
        t.forward(ray_length)  # Go Out
        t.right(90)
        t.forward(ray_width)   # Short side
        t.right(90)
        t.forward(ray_length)  # Go Back
        t.right(90)
        t.forward(ray_width)   # Short side (touching circle)
        
        t.end_fill()
        
    # Reset Turtle
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_flower_pot(t, size):
    cx, cy = t.position()
    # Pot
    draw_regular_polygon(t, 4, size, "brown")
    # Flower on top
    t.penup(); t.goto(cx, cy + size); t.pendown()
    cols = ["pink", "purple", "red", "pink", "purple", "red"]
    draw_flower(t, 6, size*0.5, 60, cols)
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_dragonfly(t, size):
    cx, cy = t.position()
    # Body
    draw_rectangle(t, size*0.15, size, "blue")
    # Wings
    wing_y = cy + size*0.2
    for ang in [70, 110, 250, 290]:
        t.penup(); t.goto(cx, wing_y); t.setheading(ang); t.pendown()
        draw_leaf(t, size*0.8, 100, "cyan")
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()


# ==========================================
# 8. Level 3 Systemic Patterns (The Architect's Test)
# ==========================================

def draw_village_circle(t, radius, count, house_size):
    """L3: Arranges houses in a circle, facing inward."""
    cx, cy = t.position()
    angle_step = 360.0 / count
    
    for i in range(count):
        # Calculate polar coordinates
        angle = i * angle_step
        rad_angle = math.radians(angle)
        
        # Position house on the perimeter
        x = cx + radius * math.cos(rad_angle)
        y = cy + radius * math.sin(rad_angle)
        
        # Move to position
        t.penup(); t.goto(x, y); t.setheading(angle + 90) # Face center? Or outward? Let's face upright for simplicity first, or align with radius.
        # Actually, standard house draws upright. Let's just place them.
        t.setheading(90) 
        t.pendown()
        
        # Diversity: Random roof colors
        c1 = random.choice(COLORS)
        c2 = random.choice(COLORS)
        draw_house(t, house_size, c1, c2)
        
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_flower_grid(t, rows, cols, cell_size):
    """L3: Draws a grid of flowers."""
    cx, cy = t.position()
    # Start from top-left to center the grid
    width = cols * cell_size
    height = rows * cell_size
    start_x = cx - width / 2 + cell_size / 2
    start_y = cy + height / 2 - cell_size / 2
    
    for r in range(rows):
        for c in range(cols):
            x = start_x + c * cell_size
            y = start_y - r * cell_size
            t.penup(); t.goto(x, y); t.pendown()
            
            # Random flower properties
            petals = random.choice([5, 6, 8])
            p_size = cell_size * 0.3
            cols_list = random.sample(COLORS, 3)
            draw_flower(t, petals, p_size, 60, cols_list)
            
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_snow_family(t, count, start_size):
    """L3: Draws a line of snowmen getting smaller."""
    cx, cy = t.position()
    gap = start_size * 0.8
    # Start on the left
    current_x = cx - (count * gap) / 2
    current_size = start_size
    
    for i in range(count):
        t.penup(); t.goto(current_x, cy); t.pendown()
        draw_snowman(t, current_size)
        
        current_x += gap
        current_size *= 0.8 # Shrink factor
        
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_galaxy_spiral(t, arms, stars_per_arm):
    """L3: Arranges stars/badges in a spiral."""
    cx, cy = t.position()
    draw_sun(t, 40) # Center
    
    max_r = 250
    for i in range(arms * stars_per_arm):
        # Logarithmic spiral formula
        angle = i * (360 / stars_per_arm) * 0.5
        radius = 60 + (i / (arms * stars_per_arm)) * max_r
        
        rad = math.radians(angle)
        x = cx + radius * math.cos(rad)
        y = cy + radius * math.sin(rad)
        
        t.penup(); t.goto(x, y); t.pendown()
        if i % 2 == 0:
            draw_star(t, random.uniform(10, 20), "gold")
        else:
            draw_badge(t, random.uniform(15, 25), "blue", "white")

    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()
def draw_traffic_scene(t, car_count, light_count):
    """
    L3: A busy street scene. 
    - Draws a road line.
    - Places traffic lights at regular intervals.
    - Places cars randomly in gaps, ensuring they don't overlap with light poles.
    """
    cx, cy = t.position()
    
    # 1. Draw Road (Full width across screen)
    road_y = cy - 50
    t.penup(); t.goto(cx, road_y); t.pendown()
    draw_rectangle(t, 800, 10, "grey") 
    
    # 2. Place Traffic Lights (Regular intervals)
    spacing = 600 / (light_count + 1)
    light_x_positions = []
    current_x = cx - 300 + spacing
    
    for i in range(light_count):
        t.penup(); t.goto(current_x, road_y + 60); t.pendown()
        draw_traffic_light(t, 60)
        light_x_positions.append(current_x)
        current_x += spacing

    # 3. Place Cars (Collision Avoidance with Lights AND other cars)
    car_x_positions = []
    car_length = 50
    for _ in range(car_count):
        valid_spot = False
        attempts = 0
        while not valid_spot and attempts < 20:
            tx = random.uniform(cx - 300, cx + 300)
            conflict = False

            # Check distance from lights (width approx 20)
            for lx in light_x_positions:
                if abs(tx - lx) < 40:
                    conflict = True
                    break

            # Check distance from other cars
            if not conflict:
                for car_x in car_x_positions:
                    if abs(tx - car_x) < car_length + 10:  # car_length + gap
                        conflict = True
                        break

            if not conflict:
                valid_spot = True
                c = random.choice(["red", "blue", "green", "silver"])
                t.penup(); t.goto(tx, road_y + 15); t.pendown()
                draw_car(t, car_length, c)
                car_x_positions.append(tx)
            attempts += 1
            
    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()

def draw_enchanted_garden(t, tree_count, pot_count, insect_count):
    """
    L3: A complex garden scene.
    - Background: Pine trees that MUST NOT OVERLAP (requires keeping track of state).
    - Foreground: Flower pots.
    - Sky: Random Butterflies and Dragonflies.
    """
    cx, cy = t.position()
    ground_y = cy - 100
    
    # 1. Pine Trees (Collision Detection)
    placed_trees = [] # Store (x, width)
    for _ in range(tree_count):
        h = random.uniform(100, 150)
        w = h * 0.5 
        
        # Try finding a spot
        for _ in range(50): 
            tx = random.uniform(cx - 300, cx + 300)
            overlap = False
            for (ex_x, ex_w) in placed_trees:
                min_dist = (w + ex_w) / 2 + 10 
                if abs(tx - ex_x) < min_dist:
                    overlap = True
                    break
            if not overlap:
                t.penup(); t.goto(tx, ground_y + h*0.2); t.pendown()
                draw_pine_tree(t, h)
                placed_trees.append((tx, w))
                break 

    # 2. Flower Pots (Collision Detection with trees and other pots)
    placed_pots = []  # Store (x, width)
    for _ in range(pot_count):
        pot_size = random.uniform(30, 50)

        # Try finding a spot
        for _ in range(50):
            px = random.uniform(cx - 250, cx + 250)
            py = ground_y - random.uniform(0, 20)
            overlap = False

            # Check collision with trees
            for (tree_x, tree_w) in placed_trees:
                min_dist = (pot_size + tree_w) / 2 + 10
                if abs(px - tree_x) < min_dist:
                    overlap = True
                    break

            # Check collision with other pots
            if not overlap:
                for (pot_x, pot_w) in placed_pots:
                    min_dist = (pot_size + pot_w) / 2 + 10
                    if abs(px - pot_x) < min_dist:
                        overlap = True
                        break

            if not overlap:
                t.penup(); t.goto(px, py); t.pendown()
                draw_flower_pot(t, pot_size)
                placed_pots.append((px, pot_size))
                break

    # 3. Insects (Sky)
    for _ in range(insect_count):
        ix = random.uniform(cx - 300, cx + 300)
        iy = cy + random.uniform(0, 150)
        t.penup(); t.goto(ix, iy); t.pendown()
        if random.random() > 0.5:
            draw_butterfly(t, random.uniform(20, 30), random.choice(COLORS))
        else:
            draw_dragonfly(t, random.uniform(20, 30))

    t.penup(); t.goto(cx, cy); t.setheading(90); t.pendown()
# ==========================================
# 4. Generator Class
# ==========================================

class TaskGenerator:
    def __init__(self, seed: int | None = None):
        if seed is not None: random.seed(seed)
        os.makedirs(OUT_DIR, exist_ok=True)
        self.screen = turtle.Screen()
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.bgcolor("white")
        turtle.tracer(0, 0)
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.metadata = []
        self.counters = {} # Track ID per type

    def _get_id(self, prefix):
        if prefix not in self.counters: self.counters[prefix] = 0
        self.counters[prefix] += 1
        return f"{prefix}_{self.counters[prefix]}"

    def _rand_pos(self, margin):
        x = random.uniform(-WIDTH/2 + margin, WIDTH/2 - margin)
        y = random.uniform(-HEIGHT/2 + margin, HEIGHT/2 - margin)
        return x, y
    
    def _save(self, fname, level, prompt, params):
        turtle.update()
        save_canvas_to_png(self.screen, os.path.join(OUT_DIR, fname))
        self.metadata.append({"id": fname, "level": level, "prompt": prompt, "params": params})
        self.t.clear()
        self.t.penup(); self.t.home(); self.t.pendown()

    def generate_all(self):
        print("🏭 Generating tasks...")

        # --- Level 1 ---
        # Polygons (25)
        for _ in range(25):
            n = random.choice([3, 4, 5, 6,7,8,9,10])
            s = random.uniform(30, 100)
            c = random.choice(COLORS)
            x, y = self._rand_pos(s+20)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_regular_polygon(self.t, n, s, c)
            self._save(self._get_id("L1_Poly") + ".png", 1, 
                       f"Draw a {c} {n}-sided regular polygon size {int(s)} at ({int(x)},{int(y)}).", 
                       {"type": "poly", "n": n, "size": s, "color": c})

        # Rectangles (10)
        for _ in range(10):
            w, h = random.uniform(40,120), random.uniform(30,90)
            c = random.choice(COLORS)
            x, y = self._rand_pos(max(w,h)+20)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_rectangle(self.t, w, h, c)
            self._save(self._get_id("L1_Rect") + ".png", 1, 
                       f"Draw a {c} rectangle {int(w)}x{int(h)} at ({int(x)},{int(y)}).", 
                       {"type": "rect", "w": w, "h": h})

        # Circle, Star, Leaf (5 each)
        for type_name, func in [("Circle", draw_circle), ("Star", draw_star)]:
            for _ in range(5):
                s = random.uniform(40, 120)
                c = random.choice(COLORS)
                x, y = self._rand_pos(s)
                self.t.penup(); self.t.goto(x, y); self.t.pendown()
                func(self.t, s, c)
                self._save(self._get_id(f"L1_{type_name}") + ".png", 1,
                           f"Draw a {c} {type_name} size {int(s)} at ({int(x)},{int(y)}).",
                           {"type": type_name.lower(), "size": s, "color": c})
        
        # Leaf needs extra param angle
        for _ in range(5):
            s = random.uniform(40, 100); ang = random.randint(60, 120); c = random.choice(COLORS)
            x, y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_leaf(self.t, s, ang, c)
            self._save(self._get_id("L1_Leaf") + ".png", 1,
                       f"Draw a {c} leaf angle {ang} size {int(s)} at ({int(x)},{int(y)}).",
                       {"type": "leaf", "size": s, "angle": ang})

       

        # --- Level 2 (5 samples each) ---
        # Helper to simplify loop
        def gen_l2(name, draw_fn, prompt_fn, param_fn):
            for _ in range(5):
                x, y = self._rand_pos(100)
                self.t.penup(); self.t.goto(x, y); self.t.pendown()
                draw_fn(self.t, x, y) # Pass center to helper wrapper
                self._save(self._get_id(f"L2_{name}") + ".png", 2, prompt_fn(), param_fn())

        # 1. House
        for _ in range(5):
            s = random.uniform(60, 120); c1, c2 = random.sample(COLORS, 2)
            x, y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_house(self.t, s, c1, c2)
            self._save(self._get_id("L2_House")+".png", 2, f"House size {int(s)} {c1}/{c2}", {"type":"house"})

        # 2. Badge
        for _ in range(5):
            s = random.uniform(50, 120); c1, c2 = random.sample(COLORS, 2)
            x, y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_badge(self.t, s, c1, c2)
            self._save(self._get_id("L2_Badge")+".png", 2, f"Badge size {int(s)} {c1}/{c2}", {"type":"badge"})

        # 3. Window
        for _ in range(5):
            s = random.uniform(80, 150); c1, c2 = random.sample(COLORS, 2)
            x, y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_window(self.t, s, c1, c2)
            self._save(self._get_id("L2_Window")+".png", 2, f"Window size {int(s)} {c1}/{c2}", {"type":"window"})

        # 4. Flower
        for _ in range(5):
            cnt = random.randint(5, 12); s = random.uniform(40, 100); ang = random.randint(40, 90)
            cols = [random.choice(COLORS) for _ in range(cnt)]
            x, y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_flower(self.t, cnt, s, ang, cols)
            self._save(self._get_id("L2_Flower")+".png", 2, f"Flower {cnt} petals size {int(s)}", {"type":"flower"})

        # 5. Snowman
        for _ in range(5):
            b = random.uniform(50, 100); x,y = self._rand_pos(b)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_snowman(self.t, b)
            self._save(self._get_id("L2_Snowman")+".png", 2, f"Snowman base {int(b)}", {"type":"snowman"})

        # 6. Pine Tree
        for _ in range(5):
            s = random.uniform(80, 150); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_pine_tree(self.t, s)
            self._save(self._get_id("L2_Pine")+".png", 2, f"Pine Tree size {int(s)}", {"type":"pine"})

        # 7. Ice Cream
        for _ in range(5):
            s = random.uniform(50, 100)
            f_color = random.choice(["pink", "lightgreen", "sienna", "cornsilk"]) 
            f_name = {"pink":"strawberry", "lightgreen":"mint", "sienna":"chocolate", "cornsilk":"vanilla"}[f_color]
            
            x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_ice_cream(self.t, s, f_color)
            self._save(self._get_id("L2_IceCream")+".png", 2, f"Ice Cream size {int(s)} {f_name}", {"type":"icecream"})

        # 8. Traffic Light
        for _ in range(5):
            h = random.uniform(80, 150); x,y = self._rand_pos(h)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_traffic_light(self.t, h)
            self._save(self._get_id("L2_Traffic")+".png", 2, f"Traffic Light height {int(h)}", {"type":"traffic"})

        # 9. Rocket
        for _ in range(5):
            w, h = random.uniform(30, 60), random.uniform(80, 150); c = random.choice(COLORS); x,y = self._rand_pos(h)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_rocket(self.t, w, h, c)
            self._save(self._get_id("L2_Rocket")+".png", 2, f"Rocket {int(w)}x{int(h)}", {"type":"rocket"})

        # 10. Dumbbell
        for _ in range(5):
            s = random.uniform(30, 60); x,y = self._rand_pos(s*4)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_dumbbell(self.t, s)
            self._save(self._get_id("L2_Dumbbell")+".png", 2, f"Dumbbell size {int(s)}", {"type":"dumbbell"})

        # 11. Spectacles
        for _ in range(5):
            s = random.uniform(30, 60); x,y = self._rand_pos(s*3)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_glasses(self.t, s)
            self._save(self._get_id("L2_Glasses")+".png", 2, f"Glasses size {int(s)}", {"type":"glasses"})

        # 12. Car
        for _ in range(5):
            l = random.uniform(80, 150); c = random.choice(COLORS); x,y = self._rand_pos(l)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_car(self.t, l, c)
            self._save(self._get_id("L2_Car")+".png", 2, f"Car len {int(l)} {c}", {"type":"car"})

        # 13. Bowtie
        for _ in range(5):
            s = random.uniform(40, 80); c = random.choice(COLORS); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_bowtie(self.t, s, c)
            self._save(self._get_id("L2_Bowtie")+".png", 2, f"Bowtie size {int(s)} {c}", {"type":"bowtie"})

        # 14. Candy
        for _ in range(5):
            s = random.uniform(30, 60); c = random.choice(COLORS); x,y = self._rand_pos(s*3)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_candy(self.t, s, c)
            self._save(self._get_id("L2_Candy")+".png", 2, f"Candy size {int(s)} {c}", {"type":"candy"})

        # 15. TV
        for _ in range(5):
            w = random.uniform(80, 150); x,y = self._rand_pos(w)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_tv(self.t, w)
            self._save(self._get_id("L2_TV")+".png", 2, f"TV width {int(w)}", {"type":"tv"})

        # 16. Donut
        for _ in range(5):
            s = random.uniform(50, 120); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_donut(self.t, s)
            self._save(self._get_id("L2_Donut")+".png", 2, f"Donut size {int(s)}", {"type":"donut"})

        # 17. Target
        for _ in range(5):
            s = random.uniform(60, 120); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_target(self.t, s)
            self._save(self._get_id("L2_Target")+".png", 2, f"Target size {int(s)}", {"type":"target"})

        # 18. Framed Star
        for _ in range(5):
            s = random.uniform(60, 120); c=random.choice(COLORS); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_framed_star(self.t, s, c)
            self._save(self._get_id("L2_FrameStar")+".png", 2, f"Framed Star size {int(s)} {c}", {"type":"framed_star"})

        # 19. Door
        for _ in range(5):
            w, h = random.uniform(40, 80), random.uniform(80, 140); c=random.choice(COLORS); x,y = self._rand_pos(h)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_door(self.t, w, h, c)
            self._save(self._get_id("L2_Door")+".png", 2, f"Door {int(w)}x{int(h)} {c}", {"type":"door"})

        # 21. Butterfly (New)
        for _ in range(5):
            s = random.uniform(50, 100); c=random.choice(COLORS); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_butterfly(self.t, s, c)
            self._save(self._get_id("L2_Butterfly")+".png", 2, f"Butterfly size {int(s)} {c}", {"type":"butterfly"})
            
        # 22. Sun (New)
        for _ in range(5):
            r = random.uniform(30, 60); x,y = self._rand_pos(r*2)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_sun(self.t, r)
            self._save(self._get_id("L2_Sun")+".png", 2, f"Sun radius {int(r)}", {"type":"sun"})

        # 23. Flower Pot (New)
        for _ in range(5):
            s = random.uniform(50, 100); x,y = self._rand_pos(s*2)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_flower_pot(self.t, s)
            self._save(self._get_id("L2_Pot")+".png", 2, f"Flower Pot size {int(s)}", {"type":"pot"})
            
        # 24. Dragonfly (New)
        for _ in range(5):
            s = random.uniform(60, 120); x,y = self._rand_pos(s)
            self.t.penup(); self.t.goto(x, y); self.t.pendown(); draw_dragonfly(self.t, s)
            self._save(self._get_id("L2_Dragonfly")+".png", 2, f"Dragonfly size {int(s)}", {"type":"dragonfly"})

        # --- LEVEL 3: SYSTEMIC PATTERNS ---
        
        # 25. Village
        for _ in range(5):
            r = random.uniform(100, 160); cnt = random.randint(5, 10); h_s = random.uniform(30, 50)
            x, y = self._rand_pos(r + h_s + 20)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_village_circle(self.t, r, cnt, h_s)
            self._save(self._get_id("L3_Village")+".png", 3, f"Village circle radius {int(r)} count {cnt}", {"type":"village"})

        # 26. Flower Grid
        for _ in range(5):
            rows = random.randint(2, 4); cols = random.randint(2, 4); sz = random.uniform(40, 60)
            margin = max(rows, cols) * sz * 0.6 + 40
            x, y = self._rand_pos(margin)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_flower_grid(self.t, rows, cols, sz)
            self._save(self._get_id("L3_Garden")+".png", 3, f"Flower Grid {rows}x{cols}", {"type":"garden"})

        # 27. Snowman Family
        for _ in range(5):
            cnt = random.randint(3, 5); start_sz = random.uniform(60, 90)
            x, y = self._rand_pos(cnt * start_sz/2 + 40)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_snow_family(self.t, cnt, start_sz)
            self._save(self._get_id("L3_Family")+".png", 3, f"Snowman Family count {cnt}", {"type":"family"})

        # 29. Galaxy Spiral
        for _ in range(5):
            arms = random.randint(3, 5); stars = random.randint(5, 10)
            x, y = self._rand_pos(260)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_galaxy_spiral(self.t, arms, stars)
            self._save(self._get_id("L3_Galaxy")+".png", 3, f"Galaxy Spiral arms {arms}", {"type":"galaxy"})

        # 30. Traffic Scene (NEW)
        for _ in range(5):
            cars = random.randint(3, 6); lights = random.randint(2, 4)
            x, y = self._rand_pos(350)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_traffic_scene(self.t, cars, lights)
            self._save(self._get_id("L3_Traffic") + ".png", 3,
                       f"Draw a traffic scene with a full-width road, {lights} traffic lights evenly spaced, and {cars} non-overlapping cars that avoid both lights and other cars",
                       {"type": "traffic_scene", "lights": lights, "cars": cars})

        # 31. Enchanted Garden (NEW)
        for _ in range(5):
            trees = random.randint(3, 6); pots = random.randint(4, 8); insects = random.randint(3, 6)
            x, y = self._rand_pos(350)
            self.t.penup(); self.t.goto(x, y); self.t.pendown()
            draw_enchanted_garden(self.t, trees, pots, insects)
            self._save(self._get_id("L3_Garden_Complex") + ".png", 3,
                       f"Draw an enchanted garden with {trees} non-overlapping pine trees in the background, {pots} flower pots that don't overlap with trees or each other, and {insects} flying insects (butterflies/dragonflies) in the sky",
                       {"type": "enchanted_garden", "trees": trees, "pots": pots, "insects": insects})
        # Metadata
        with open(os.path.join(OUT_DIR, "tasks.json"), "w") as f:
            json.dump(self.metadata, f, indent=2)
        
        print(f"✅ Generated {len(self.metadata)} tasks.")
        try: self.screen.bye()
        except: pass

if __name__ == "__main__":
    gen = TaskGenerator()
    gen.generate_all()
    