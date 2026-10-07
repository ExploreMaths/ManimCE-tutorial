"""ParametricImplicitDemo: plot_parametric_curve 与 plot_implicit_curve 对照。"""

from manim import *


class ParametricImplicitDemo(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            x_length=7,
            y_length=7,
        )
        # 参数方程：单位圆
        circle = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=(0, 2 * PI),
            color=BLUE,
        )
        # 隐函数：x^2 + y^2 = 4（半径 2 的圆）
        implicit = axes.plot_implicit_curve(
            lambda x, y: x**2 + y**2 - 4,
            color=YELLOW,
        )

        self.play(Create(axes), run_time=1.0)
        self.play(Create(circle), run_time=1.5)
        self.play(Create(implicit), run_time=1.5)
        self.wait(0.5)
