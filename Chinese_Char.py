"""Chinese Character Generator for DC-ACE Research.

Generates PNG images of 30 basic Chinese characters using stroke data.
Each character is drawn 3 times with variations in scale/position.
"""

import json
import turtle
import os
import io
from PIL import Image

class ChineseCharacterGenerator:
    def __init__(self, file_path):
        """Load character stroke data from graphics.txt"""
        self.data_map = {}
        print(f"Loading character database from {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                self.data_map[item['character']] = item
        print(f"✅ Loaded {len(self.data_map)} characters")

    def draw_to_png(self, char, output_path, scale=0.5, offset_x=0, offset_y=0):
        """Draw a Chinese character and save as PNG"""
        if char not in self.data_map:
            print(f"❌ Character not found: {char}")
            return False

        success = False
        try:
            # Initialize Turtle
            screen = turtle.Screen()
            screen.setup(600, 600)
            screen.bgcolor("white")
            turtle.tracer(0, 0)  # Disable animation for speed

            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0)
            t.pensize(4)
            t.pencolor("black")

            # Get stroke data
            medians = self.data_map[char]['medians']

            # Draw each stroke
            for stroke in medians:
                t.penup()
                # Convert coordinates: 1024 coordinate system -> centered Turtle coords
                # Correct transformation: flip Y-axis only
                start_x = (stroke[0][0] - 512) * scale + offset_x
                start_y = (stroke[0][1] - 512) * scale + offset_y
                t.goto(start_x, start_y)
                t.pendown()

                for x, y in stroke[1:]:
                    turtle_x = (x - 512) * scale + offset_x
                    turtle_y = (y - 512) * scale + offset_y
                    t.goto(turtle_x, turtle_y)

            # Save to PNG
            turtle.update()
            canvas = screen.getcanvas()
            try:
                ps = canvas.postscript(colormode="color")
                b = io.BytesIO(ps.encode("utf-8"))
                img = Image.open(b)
                img.load(scale=1)
                rgba = img.convert("RGBA")
                rgba.save(output_path, "PNG")
                print(f"✅ Saved: {output_path}")
                success = True
            except Exception as e:
                print(f"❌ Error saving {output_path}: {e}")
                success = False

        except turtle.Terminator:
            # Handle turtle termination gracefully
            pass
        except Exception as e:
            print(f"❌ Error drawing {char}: {e}")
        finally:
            # Always try to close the screen
            try:
                turtle.Screen().bye()
            except:
                pass
            # Reset turtle module
            turtle.TurtleScreen._RUNNING = True

        return success

def generate_all_characters():
    """Generate 30 basic Chinese characters, 3 samples each"""

    # 30 basic characters with metadata
    characters = [
        ("一", "yī", "one", "horizontal line"),
        ("人", "rén", "person", "two strokes forming a person"),
        ("入", "rù", "enter", "two strokes entering downward"),
        ("八", "bā", "eight", "two strokes separating outward"),
        ("刀", "dāo", "knife", "curved blade shape"),
        ("力", "lì", "power/strength", "muscular arm shape"),
        ("又", "yòu", "again/also", "right hand shape"),
        ("十", "shí", "ten", "cross/plus shape"),
        ("工", "gōng", "work/labor", "three horizontal lines"),
        ("土", "tǔ", "earth/soil", "ground with line above"),
        ("木", "mù", "wood/tree", "tree with branches"),
        ("火", "huǒ", "fire", "flames rising"),
        ("水", "shuǐ", "water", "flowing water"),
        ("口", "kǒu", "mouth", "square opening"),
        ("日", "rì", "sun/day", "sun with line inside"),
        ("月", "yuè", "moon/month", "crescent moon"),
        ("田", "tián", "field", "rice field grid"),
        ("目", "mù", "eye", "eye with pupils"),
        ("白", "bái", "white", "sun with line"),
        ("山", "shān", "mountain", "three peaks"),
        ("女", "nǚ", "woman", "seated figure"),
        ("子", "zǐ", "child", "baby with arms up"),
        ("夕", "xī", "evening", "crescent moon"),
        ("大", "dà", "big/large", "person with arms spread"),
        ("小", "xiǎo", "small/little", "three small dots"),
        ("王", "wáng", "king", "three horizontal lines with vertical"),
        ("车", "chē", "vehicle/car", "cart from above"),
        ("贝", "bèi", "shell/treasure", "cowrie shell"),
        ("门", "mén", "door/gate", "two door panels"),
        ("言", "yán", "speech/words", "mouth speaking"),
    ]

    # Output directory
    output_dir = "/Users/peilinwu/Documents/AI memory research/Chinese_2"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize generator
    graphics_path = "/Users/peilinwu/Documents/AI memory research/draw_character/graphics.txt"
    gen = ChineseCharacterGenerator(graphics_path)

    print(f"\n🖌️  Generating {len(characters)} characters × 3 samples each...")
    print(f"📂 Output: {output_dir}\n")

    # Variations for 3 samples (scale, offset_x, offset_y)
    variations = [
        (0.5, 0, 0),      # Sample 1: Medium, centered
        (0.6, -30, 20),   # Sample 2: Larger, offset left-up
        (0.45, 25, -15),  # Sample 3: Smaller, offset right-down
    ]

    total = 0
    detailed_metadata = []

    for idx, (char, pinyin, meaning, description) in enumerate(characters, 1):
        char_samples = []
        for sample_num, (scale, offset_x, offset_y) in enumerate(variations, 1):
            # Filename format: 01_一_1.png, 01_一_2.png, 01_一_3.png
            filename = f"{idx:02d}_{char}_{sample_num}.png"
            output_path = os.path.join(output_dir, filename)

            success = gen.draw_to_png(char, output_path, scale, offset_x, offset_y)
            if success:
                total += 1
                char_samples.append({
                    "filename": filename,
                    "scale": scale,
                    "offset_x": offset_x,
                    "offset_y": offset_y
                })

        detailed_metadata.append({
            "index": idx,
            "character": char,
            "pinyin": pinyin,
            "meaning": meaning,
            "description": description,
            "prompt": f"Draw Chinese character '{char}' ({pinyin}, meaning: {meaning}) - {description}",
            "samples": char_samples
        })

    print(f"\n✅ Generated {total} Chinese character images!")
    print(f"📊 Expected: {len(characters) * 3} = {len(characters)} chars × 3 samples")

    # Create comprehensive metadata
    metadata = {
        "total_characters": len(characters),
        "samples_per_character": 3,
        "total_images": total,
        "description": "DC-ACE Chinese Character Dataset - 30 basic characters with stroke-accurate rendering",
        "characters": detailed_metadata
    }

    import json
    metadata_path = os.path.join(output_dir, "characters.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"📊 Metadata saved to {metadata_path}")

if __name__ == "__main__":
    generate_all_characters()
