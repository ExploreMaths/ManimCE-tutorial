"""TitleDemo: Title 与下划线宽度行为。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class TitleDemo(Scene):
    def construct(self):
        title = Title("第三节：文本与公式")
        narrow = Title("窄标题", match_underline_width_to_text=True)

        self.add(title)
        self.wait(0.5)
        self.play(FadeIn(narrow))
        self.wait(0.5)
