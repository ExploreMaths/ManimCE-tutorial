"""DecimalTableDemo: DecimalTable 小数表格，可省略内线。"""

from manim import *


class DecimalTableDemo(Scene):
    def construct(self):
        table = DecimalTable(
            [[3.14159, 2.71828], [1.41421, 1.73205]],
            element_to_mobject_config={"num_decimal_places": 2},
            include_inner_lines=False,
            include_outer_lines=True,
        )
        self.play(Create(table), run_time=1.5)
        self.wait(0.5)
