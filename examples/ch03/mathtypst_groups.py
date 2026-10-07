"""MathTypstGroups: MathTypst 的 {{ }} 分组与 select 选择。"""

from manim import *


class MathTypstGroups(Scene):
    def construct(self):
        eq = MathTypst("{{ a^2 + b^2 : lhs }} = {{ c^2 : rhs }}")
        lhs = eq.select("lhs")
        rhs = eq.select("rhs")

        self.play(Write(eq))
        self.play(lhs.animate.set_color(BLUE), rhs.animate.set_color(RED))
        self.wait(0.5)
