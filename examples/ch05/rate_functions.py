"""RateFunctionsRace: 多个小球以不同 rate_func 同向下落，直观对比速率曲线。"""

from manim import *


class RateFunctionsRace(Scene):
    def construct(self):
        funcs = [linear, smooth, rush_from, rush_into, there_and_back, wiggle]
        colors = [WHITE, BLUE, GREEN, ORANGE, PURPLE, RED]

        dots = VGroup(
            *[
                Dot(color=color).to_edge(UP).shift(RIGHT * x)
                for color, x in zip(colors, [-4, -2.4, -0.8, 0.8, 2.4, 4])
            ]
        )
        labels = VGroup(
            *[
                Text(f.__name__, font_size=18).next_to(dot, DOWN, buff=0.15)
                for dot, f in zip(dots, funcs)
            ]
        )
        finish = Line(LEFT * 5, RIGHT * 5, color=GREY).to_edge(DOWN, buff=1.5)
        self.add(dots, labels, finish)

        self.play(
            *[
                dot.animate(rate_func=f, run_time=3).shift(DOWN * 4.2)
                for dot, f in zip(dots, funcs)
            ]
        )
