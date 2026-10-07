"""FunctionGraphDemo: Axes.plot 绘制显函数、get_area 填充区域。"""

from manim import *


class FunctionGraphDemo(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-4, 4, 1),
            y_range=(-2, 2, 1),
            x_length=10,
            y_length=5,
        )
        sin_graph = axes.plot(np.sin, color=BLUE)
        cos_graph = axes.plot(np.cos, color=GREEN)

        self.play(Create(axes), run_time=1.0)
        self.play(Create(sin_graph), Create(cos_graph), run_time=1.5)

        # get_area：填充两条曲线之间的区域
        area = axes.get_area(
            sin_graph,
            x_range=(0, PI),
            bounded_graph=cos_graph,
            opacity=0.4,
        )
        self.play(FadeIn(area), run_time=1.0)

        # input_to_graph_point（别名 i2gp）：取曲线上指定 x 的点
        dot = Dot(axes.input_to_graph_point(PI / 2, sin_graph), color=RED)
        self.play(FadeIn(dot), run_time=0.5)
        self.wait(0.5)
