"""MobjectTableDemo: MobjectTable 用任意 mobject 作单元格。"""

from manim import *


class MobjectTableDemo(Scene):
    def construct(self):
        table = MobjectTable(
            [
                [Circle(fill_opacity=0.5), Square(fill_opacity=0.5), Triangle(fill_opacity=0.5)],
                [Dot(), Cross(), Star()],
            ],
            h_buff=1.8,
            include_outer_lines=True,
        )
        self.play(FadeIn(table), run_time=1.5)

        self.play(table.get_entries((1, 1)).animate.set_color(RED), run_time=1.0)
        self.wait(0.5)
