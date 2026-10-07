"""LinearTransformationDemo: 切变矩阵的线性变换动画。"""

from manim import *


class LinearTransformationDemo(LinearTransformationScene):
    def construct(self):
        # 默认已包含背景/前景 NumberPlane 与 i_hat、j_hat 基向量
        self.add_unit_square()
        self.wait(0.3)

        # 切变：x 轴不变，j_hat 移到 (1, 1)
        self.apply_matrix([[1, 1], [0, 1]], run_time=2.0)
        self.wait(0.5)
