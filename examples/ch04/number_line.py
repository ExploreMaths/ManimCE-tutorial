"""NumberLineDemo: NumberLine 的刻度、自定义标签与坐标互转。"""

from manim import *


class NumberLineDemo(Scene):
    def construct(self):
        line = NumberLine(
            x_range=[-4, 4, 1],
            length=10,
            include_tip=True,
        )
        # 用 Text 作为标签，避免依赖 LaTeX
        line.add_labels(
            {
                -3: Text("-3", font_size=30),
                -1: Text("-1", font_size=30),
                1: Text("1", font_size=30),
                3: Text("3", font_size=30),
            }
        )
        dot = Dot(line.number_to_point(2.5), color=RED)

        self.play(Create(line), run_time=1.5)
        self.play(FadeIn(dot), run_time=0.5)

        # number_to_point 与 point_to_number 互逆
        x_val = line.point_to_number(dot.get_center())
        coord = Text(f"x = {x_val:.1f}", font_size=30)
        coord.next_to(dot, UP)
        self.play(Write(coord), run_time=1.0)
        self.wait(0.5)
