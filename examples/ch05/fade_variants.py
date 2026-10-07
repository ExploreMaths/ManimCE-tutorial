"""FadeVariants: FadeIn shift / target_position / scale, and FadeOut."""

from manim import *


class FadeVariants(Scene):
    def construct(self):
        anchor = Dot(LEFT * 4 + UP * 2, color=GREY_B)
        self.add(anchor)

        a = Square(0.7).set_fill(RED, opacity=0.6).shift(LEFT * 2 + UP)
        b = Circle(0.4).set_fill(GREEN, opacity=0.6)
        c = Triangle().set_fill(BLUE, opacity=0.6).scale(0.6).shift(RIGHT * 2 + UP)

        # 普通淡入
        self.play(FadeIn(a), run_time=0.8)
        # 淡入的同时从指定方向滑入
        self.play(FadeIn(b, shift=UP * 1.5), run_time=0.8)
        # 从某个点（或物体中心）飞入
        self.play(FadeIn(c, target_position=anchor), run_time=0.8)
        # 淡入的同时从小放大
        d = Star().set_fill(YELLOW, opacity=0.6).scale(0.6).shift(DOWN * 1.5)
        self.play(FadeIn(d, scale=0.2), run_time=0.8)

        # 淡出时可以整体向某个方向滑走
        group = VGroup(a, b, c, d)
        self.play(FadeOut(group, shift=RIGHT * 2), run_time=0.9)
        self.wait(0.3)
