"""MathTableDemo: MathTable 公式表格与单元格定位。"""

from manim import *


class MathTableDemo(Scene):
    def construct(self):
        table = MathTable(
            [["x", "x^2"], ["2", "4"], ["3", "9"], ["4", "16"]],
            include_outer_lines=True,
        )
        self.play(Create(table), run_time=1.5)
        self.play(table.get_entries((2, 2)).animate.set_color(RED), run_time=0.8)
        self.wait(0.5)
