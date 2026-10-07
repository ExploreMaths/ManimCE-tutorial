"""MatrixTexHelpersDemo: matrix_to_tex_string 与 matrix_to_mobject。"""

from manim import *

import numpy as np


class MatrixTexHelpersDemo(Scene):
    def construct(self):
        np_matrix = np.array([[1, 2], [3, 4]])

        # 先得到 LaTeX 字符串，再转成 mobject（内部即 MathTex）
        tex_string = matrix_to_tex_string(np_matrix)
        mob = matrix_to_mobject(np_matrix)

        # 实际输出: \left[ \begin{array}{cc}1 & 2\\3 & 4\end{array} \right]
        print(tex_string)
        self.play(Write(mob), run_time=1.5)
        self.wait(0.5)
