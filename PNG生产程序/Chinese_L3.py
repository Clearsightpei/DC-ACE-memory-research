"""Level 3 Chinese Character Generator for DC-ACE Research.

Generates PNG images of 30 compound Chinese characters using stroke data.
Each character is drawn 2 times with variations in scale/position.
"""

import json
import turtle
import os
import subprocess
import tempfile

class ChineseCharacterGeneratorL3:
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
                # Correct transformation: keep X as-is, adjust Y
                start_x = (stroke[0][0] - 512) * scale + offset_x
                start_y = (stroke[0][1] - 512) * scale + offset_y
                t.goto(start_x, start_y)
                t.pendown()

                for x, y in stroke[1:]:
                    turtle_x = (x - 512) * scale + offset_x
                    turtle_y = (y - 512) * scale + offset_y
                    t.goto(turtle_x, turtle_y)

            # Save to PNG via Ghostscript: canvas → .ps → gs → .png
            turtle.update()
            canvas = screen.getcanvas()
            try:
                with tempfile.NamedTemporaryFile(suffix=".ps", delete=False) as tmp:
                    tmp_ps = tmp.name
                canvas.postscript(file=tmp_ps, colormode="color")

                result = subprocess.run(
                    [
                        "gs",
                        "-dNOPAUSE", "-dBATCH", "-dSAFER",
                        "-sDEVICE=png16m",
                        "-r150",
                        f"-sOutputFile={output_path}",
                        tmp_ps,
                    ],
                    capture_output=True,
                    text=True,
                )
                os.unlink(tmp_ps)

                if result.returncode != 0:
                    print(f"❌ Ghostscript error for {output_path}: {result.stderr[:120]}")
                    success = False
                else:
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
    """Generate 30 Level 3 Chinese characters, 2 samples each"""

    # 30 Level 3 compound characters with metadata
    characters = [
        ("二", "èr", "two", "two horizontal lines"),
        ("三", "sān", "three", "three horizontal lines"),
        ("从", "cóng", "from/follow", "two people following"),
        ("众", "zhòng", "crowd/many people", "three people together"),
        ("林", "lín", "forest/woods", "two trees side by side"),
        ("森", "sēn", "dense forest", "three trees together"),
        ("吕", "lǚ", "surname Lü", "two mouths stacked"),
        ("品", "pǐn", "product/quality", "three mouths forming triangle"),
        ("昌", "chāng", "prosperous", "two suns stacked"),
        ("晶", "jīng", "crystal/bright", "three suns forming triangle"),
        ("炎", "yán", "inflammation/flame", "two fires stacked"),
        ("焱", "yàn", "flames/blaze", "three fires forming triangle"),
        ("圭", "guī", "jade tablet", "two earths stacked"),
        ("双", "shuāng", "pair/double", "two birds together"),
        ("多", "duō", "many/much", "two evenings together"),
        ("回", "huí", "return/回", "enclosed square within square"),
        ("因", "yīn", "because/cause", "large enclosed with small inside"),
        ("困", "kùn", "sleepy/trapped", "tree enclosed in box"),
        ("国", "guó", "country/nation", "jade enclosed in box"),
        ("呆", "dāi", "dull/foolish/stay", "mouth with tree above"),
        ("尖", "jiān", "sharp/pointed", "small on top of large"),
        ("好", "hǎo", "good", "woman with child"),
        ("明", "míng", "bright/clear", "sun and moon together"),
        ("男", "nán", "male/man", "field with power"),
        ("加", "jiā", "add/plus", "power with mouth"),
        ("信", "xìn", "letter/trust/believe", "person with words"),
        ("问", "wèn", "ask/question", "door with mouth"),
        ("闪", "shǎn", "flash/dodge", "door with person"),
        ("囚", "qiú", "prisoner", "person enclosed in box"),
        ("杏", "xìng", "apricot", "tree with mouth below"),
    ]

    # Output directory
    output_dir = "/Users/peilinwu/Documents/AI memory research/Chinese_L3"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize generator
    graphics_path = "/Users/peilinwu/Documents/AI memory research/draw_character/graphics.txt"
    gen = ChineseCharacterGeneratorL3(graphics_path)

    print(f"\n🖌️  Generating Level 3: {len(characters)} characters × 1 sample each...")
    print(f"📂 Output: {output_dir}\n")

    # Variations for 1 sample (scale, offset_x, offset_y)
    variations = [
        (0.5, 0, 0),      # Sample 1: Medium, centered
    ]

    total = 0
    # Build metadata skeleton first, samples filled in as generated
    detailed_metadata = [
        {
            "index": idx,
            "character": char,
            "pinyin": pinyin,
            "meaning": meaning,
            "description": description,
            "prompt": f"Draw Chinese character '{char}' ({pinyin}, meaning: {meaning}) - {description}",
            "samples": []
        }
        for idx, (char, pinyin, meaning, description) in enumerate(characters, 1)
    ]

    # Generate all characters once per round, 2 rounds total
    # Order: 二_1, 三_1, ...(all chars)..., 二_2, 三_2, ...
    for sample_num, (scale, offset_x, offset_y) in enumerate(variations, 1):
        for idx, (char, pinyin, meaning, description) in enumerate(characters, 1):
            filename = f"{idx:02d}_{char}_{sample_num}.png"
            output_path = os.path.join(output_dir, filename)

            success = gen.draw_to_png(char, output_path, scale, offset_x, offset_y)
            if success:
                total += 1
                detailed_metadata[idx - 1]["samples"].append({
                    "filename": filename,
                    "scale": scale,
                    "offset_x": offset_x,
                    "offset_y": offset_y
                })

    print(f"\n✅ Generated {total} Level 3 Chinese character images!")
    print(f"📊 Expected: {len(characters)} = {len(characters)} chars × 1 sample")

    # Create comprehensive metadata
    metadata = {
        "total_characters": len(characters),
        "samples_per_character": 1,
        "total_images": total,
        "level": 3,
        "description": "DC-ACE Level 3 Chinese Character Dataset - 30 compound characters composed of basic radicals",
        "characters": detailed_metadata
    }

    import json
    metadata_path = os.path.join(output_dir, "characters_L3.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"📊 Metadata saved to {metadata_path}")

if __name__ == "__main__":
    generate_all_characters()
