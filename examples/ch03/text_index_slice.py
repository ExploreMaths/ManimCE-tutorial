"""TextIndexSlice: Text 两种索引约定——渲染字符索引与原文切片。"""

from manim import *


class TextIndexSlice(Scene):
    def construct(self):
        t2c_text = Text("t2c 按原文切片着色", t2c={"[0:3]": YELLOW}, font_size=36)
        direct_text = Text("Hello World", font_size=48)

        self.play(Write(t2c_text))
        self.play(FadeOut(t2c_text), Write(direct_text))
        # direct_text[0:5] 按“去掉空白后的渲染字符”计数：Hello
        # 空格不占位，World 从索引 5 开始
        self.play(
            direct_text[0:5].animate.set_color(BLUE),
            direct_text[5:10].animate.set_color(RED),
        )
        self.wait(0.5)
