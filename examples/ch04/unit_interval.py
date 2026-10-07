"""UnitIntervalDemo: UnitInterval 默认 0-1、unit_size=10，且整体居中。"""

from manim import *


class UnitIntervalDemo(Scene):
    def construct(self):
        ui = UnitInterval()
        ui.add_labels(
            {
                0: Text("0", font_size=30),
                0.5: Text("0.5", font_size=30),
                1: Text("1", font_size=30),
            }
        )
        # 注意：UnitInterval 以自身中心对齐原点，
        # number_to_point(0) 位于场景 x = -5 处，而不是原点。
        dot = Dot(ui.number_to_point(0.75), color=YELLOW)

        self.play(Create(ui), run_time=1.5)
        self.play(FadeIn(dot), run_time=0.5)

        arrow = Arrow(
            ui.number_to_point(0.25),
            ui.number_to_point(0.75),
            buff=0,
            color=BLUE,
        )
        self.play(GrowArrow(arrow), run_time=1.0)
        self.wait(0.5)
