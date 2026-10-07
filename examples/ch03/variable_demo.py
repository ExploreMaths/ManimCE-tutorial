"""VariableDemo: Variable 显示变量及其依赖更新。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class VariableDemo(Scene):
    def construct(self):
        x = Variable(0, "x", var_type=DecimalNumber, num_decimal_places=1)
        y = Variable(0, "x^2", var_type=DecimalNumber, num_decimal_places=1)
        y.next_to(x, RIGHT, buff=1.5)
        y.add_updater(lambda m: m.set_value(x.tracker.get_value() ** 2))

        self.add(x, y)
        self.play(x.tracker.animate.set_value(3), run_time=2)
        self.wait(0.5)
