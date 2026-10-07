"""ParagraphDemo: Paragraph 多行对齐。"""

from manim import *


class ParagraphDemo(Scene):
    def construct(self):
        para = Paragraph(
            "Paragraph 把多行文本",
            "排列成一个整体对象",
            "支持逐行设置对齐",
            alignment="center",
            font_size=32,
        )
        self.play(FadeIn(para, shift=UP))
        self.play(para[2].animate.set_color(YELLOW))
        self.wait(0.5)
