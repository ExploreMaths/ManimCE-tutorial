"""CreationSubsets: ShowIncreasingSubsets / ShowSubmobjectsOneByOne / SpiralIn."""

from manim import *


class CreationSubsets(Scene):
    def construct(self):
        dots = VGroup(*[Dot().shift(i * RIGHT * 0.9) for i in range(5)])
        dots.shift(UP * 1.5 + LEFT * 1.8)

        # 子对象一批一批地显示出来
        self.play(ShowIncreasingSubsets(dots), run_time=1.5)
        self.wait(0.3)

        # 子对象逐个显示（最后只保留最后一个？不——逐个点亮）
        squares = VGroup(*[Square(0.5).shift(i * RIGHT * 0.9) for i in range(4)])
        squares.shift(DOWN * 0.5 + LEFT * 1.4)
        self.play(ShowSubmobjectsOneByOne(squares), run_time=1.6)
        self.wait(0.2)

        # 螺旋飞入
        rings = VGroup(*[Circle(radius=0.25).shift(1.5 * np.cos(i) * RIGHT + 1.5 * np.sin(i) * UP) for i in np.linspace(0, 2 * PI, 6)[:-1]])
        self.play(SpiralIn(rings), run_time=1.4)
        self.wait(0.3)
