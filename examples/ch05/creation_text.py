"""CreationText: Write / Unwrite / AddTextWordByWord / letter-by-letter."""

from manim import *


class CreationText(Scene):
    def construct(self):
        text = Text("逐字书写", font_size=48)

        # Write：沿笔画描出轮廓再填充
        self.play(Write(text), run_time=1.2)
        self.play(Unwrite(text), run_time=0.9)

        # AddTextWordByWord：按词组整体出现
        words = Text("一词 一词 出现", font_size=40)
        self.play(AddTextWordByWord(words), run_time=1.5)
        self.wait(0.3)

        # AddTextLetterByLetter：逐字符淡入
        letters = Text("逐字出现", font_size=40).shift(DOWN * 1.8)
        self.play(AddTextLetterByLetter(letters), run_time=1.2)
        self.wait(0.3)
