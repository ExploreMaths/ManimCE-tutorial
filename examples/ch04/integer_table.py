"""IntegerTableDemo: IntegerTable 的行/列标签与单元格定位。"""

from manim import *


class IntegerTableDemo(Scene):
    def construct(self):
        table = IntegerTable(
            [[1, 2, 3], [4, 5, 6]],
            row_labels=[Text("R1", font_size=30), Text("R2", font_size=30)],
            col_labels=[Text("C1", font_size=30), Text("C2", font_size=30), Text("C3", font_size=30)],
            include_outer_lines=True,
            include_inner_lines=False,
        )
        self.play(Create(table), run_time=1.5)

        # get_cell 按 (行, 列) 定位；标签也占行列编号
        cell = table.get_cell((2, 3))
        self.play(cell.animate.set_fill(YELLOW, opacity=0.5), run_time=1.0)
        self.wait(0.5)
