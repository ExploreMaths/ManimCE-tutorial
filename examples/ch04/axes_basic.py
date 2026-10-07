"""AxesDemo: Axes 的基本创建、坐标互转与坐标读取线。"""

from manim import *


class AxesDemo(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-3, 3, 1),
            y_range=(-2, 2, 1),
            x_length=9,
            y_length=6,
            axis_config={"include_tip": True},
        )
        labels = axes.get_axis_labels(
            x_label=Text("x", font_size=36),
            y_label=Text("y", font_size=36),
        )

        self.play(Create(axes), run_time=1.5)
        self.play(FadeIn(labels), run_time=0.5)

        # coords_to_point：坐标 -> 场景点；point_to_coords 为其逆运算
        dot = Dot(axes.coords_to_point(2, 1), color=RED)
        x_line = DashedLine(axes.coords_to_point(2, 0), axes.coords_to_point(2, 1))
        y_line = DashedLine(axes.coords_to_point(0, 1), axes.coords_to_point(2, 1))
        self.play(Create(x_line), Create(y_line), FadeIn(dot), run_time=1.0)

        coord = Text("(2, 1)", font_size=30).next_to(dot, UR, buff=0.1)
        self.play(Write(coord), run_time=0.8)
        self.wait(0.5)
