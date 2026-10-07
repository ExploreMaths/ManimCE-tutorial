"""MobjectMatrixDemo: MobjectMatrix 用任意 mobject 作元素。"""

from manim import *


class MobjectMatrixDemo(Scene):
    def construct(self):
        matrix = MobjectMatrix(
            [
                [Circle(), Square(), Triangle()],
                [Star(), Cross(), Dot()],
            ],
            h_buff=1.6,
        )
        self.play(FadeIn(matrix), run_time=1.5)

        self.play(matrix.get_columns()[2].animate.shift(UP * 0.4), run_time=1.0)
        self.play(matrix.get_rows()[1].animate.set_color(BLUE), run_time=1.0)
        self.wait(0.5)
