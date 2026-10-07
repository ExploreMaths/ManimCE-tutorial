"""MathTexGroups: MathTex 的 {{ }} 双花括号分组。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class MathTexGroups(Scene):
    def construct(self):
        eq = MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")

        self.play(Write(eq))
        self.play(
            eq[0].animate.set_color(BLUE),
            eq[2].animate.set_color(RED),
            eq[4].animate.set_color(GREEN),
        )
        self.wait(0.5)
