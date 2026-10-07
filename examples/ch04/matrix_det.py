"""MatrixDetDemo: DecimalMatrix 与 get_det_text 行列式标注。"""

from manim import *


class MatrixDetDemo(Scene):
    def construct(self):
        matrix = DecimalMatrix(
            [[1.5, 2.0], [3.0, 4.5]],
            element_to_mobject_config={"num_decimal_places": 1},
        )
        # get_det_text 生成 "det(A) =" 标签，与矩阵等高排列
        det = get_det_text(matrix, determinant="0.8")
        group = VGroup(det, matrix).arrange(RIGHT)

        self.play(Write(group), run_time=2.0)
        self.wait(0.5)
