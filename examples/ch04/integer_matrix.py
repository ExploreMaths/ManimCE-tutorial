"""IntegerMatrixDemo: IntegerMatrix 与行/列/元素访问。"""

from manim import *


class IntegerMatrixDemo(Scene):
    def construct(self):
        matrix = IntegerMatrix(
            [[1, 2, 3], [4, 5, 6]],
            add_background_rectangles_to_entries=True,
        )
        self.play(Write(matrix), run_time=1.5)

        # get_rows / get_columns / get_entries 返回 VGroup，可直接做动画
        self.play(matrix.get_rows()[0].animate.set_color(RED), run_time=1.0)
        self.play(matrix.get_columns()[2].animate.set_color(BLUE), run_time=1.0)
        self.play(matrix.get_entries()[3].animate.scale(1.5), run_time=0.8)
        self.wait(0.5)
