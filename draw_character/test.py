import json
import turtle

class CharacterTurtleGenerator:
    def __init__(self, file_path):
        """加载数据"""
        self.data_map = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                self.data_map[item['character']] = item

    def draw_locally(self, char, scale=0.5):
        """在本地电脑直接弹窗绘图"""
        if char not in self.data_map:
            print(f"找不到汉字: {char}")
            return
        
        # 1. 初始化本地 Turtle 窗口
        screen = turtle.Screen()
        screen.setup(600, 600)
        t = turtle.Turtle()
        t.speed(5)
        t.pensize(4)
        
        # 2. 获取骨架数据
        medians = self.data_map[char]['medians']
        
        # 3. 核心绘图逻辑
        for stroke in medians:
            t.penup()
            # 坐标转换：将 1024 坐标系转为以 (0,0) 为中心的 Turtle 坐标
            start_x = (stroke[0][0] - 512) * scale
            start_y = (512 - stroke[0][1]) * scale # 翻转Y轴
            t.goto(start_x, start_y)
            t.pendown()
            
            for x, y in stroke[1:]:
                t.goto((x - 512) * scale, (512 - y) * scale)
        
        t.hideturtle()
        print(f"汉字 '{char}' 绘制完成！")
        screen.exitonclick()

# --- 测试运行 ---
if __name__ == "__main__":
    # 只要确保 graphics.txt 在当前目录下即可
    gen = CharacterTurtleGenerator('graphics.txt')
    
    gen.draw_locally("陶")
   
