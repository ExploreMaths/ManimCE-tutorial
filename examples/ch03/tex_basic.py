"""TexBasic: Tex 文本模式与 MathTex 公式模式。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class TexBasic(Scene):
    def construct(self):
        formula = MathTex(r"e^{i\pi} + 1 = 0")
        text = Tex(r"这是欧拉恒等式：$e^{i\pi} + 1 = 0$", tex_template=TexTemplateLibrary.ctex)
        text.next_to(formula, DOWN, buff=0.8)

        self.play(Write(formula))
        self.play(FadeIn(text))
        self.wait(0.5)
