"""MathTexLabels: substrings_to_isolate 隔离子串并按 label 选取。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class MathTexLabels(Scene):
    def construct(self):
        eq = MathTex(
            r"\frac{d}{dx} \int_a^x f(t) \, dt = f(x)",
            substrings_to_isolate=["a", "x"],
        )
        self.play(Write(eq))
        self.play(
            eq.get_part_by_tex("x").animate.set_color(YELLOW),
            eq.get_part_by_tex("a").animate.set_color(RED),
        )
        self.wait(0.5)
