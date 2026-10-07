"""TextBasics: Text 的渐变、局部着色与字重字态。"""

from manim import *


class TextBasics(Scene):
    def construct(self):
        gradient_text = Text("渐变文字", gradient=(BLUE, GREEN))
        keycolored_text = Text("关键词着色：ManimCE 教程", t2c={"ManimCE": YELLOW})
        styled_text = Text("粗体与斜体", weight=BOLD, slant=ITALIC)

        self.play(Write(gradient_text))
        self.play(FadeOut(gradient_text), FadeIn(keycolored_text))
        self.play(FadeOut(keycolored_text), FadeIn(styled_text))
        self.wait(0.5)
