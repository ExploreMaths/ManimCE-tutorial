"""CompositionDemo: AnimationGroup / Succession / LaggedStart / LaggedStartMap."""

from manim import *


class CompositionDemo(Scene):
    def construct(self):
        # AnimationGroup：多个动画并行播放（lag_ratio=0）
        a = Dot(LEFT * 3 + UP).set_color(RED)
        b = Dot(LEFT * 3 + DOWN).set_color(BLUE)
        self.play(AnimationGroup(FadeIn(a), FadeIn(b)), run_time=0.7)
        self.wait(0.2)

        # Succession：严格一个接一个（lag_ratio=1）
        c = Square().set_fill(GREEN, opacity=0.5).shift(RIGHT * 2 + UP)
        self.play(
            Succession(
                GrowFromCenter(c, run_time=0.4),
                c.animate.shift(DOWN * 1.5).set_run_time(0.4),
                FadeOut(c, run_time=0.4),
            ),
            run_time=1.3,
        )
        self.wait(0.2)

        # LaggedStart：同一动画错峰开始（lag_ratio=0.05）
        dots = VGroup(*[Dot().shift(i * RIGHT * 0.8 + LEFT * 2.4 + DOWN * 1.8) for i in range(5)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.3), run_time=1.0)
        self.wait(0.2)

        # LaggedStartMap：对一组子对象批量生成同一种动画
        squares = VGroup(*[Square(0.4).set_fill(YELLOW, opacity=0.6) for _ in range(5)])
        squares.arrange(RIGHT, buff=0.4).shift(DOWN * 0.5 + LEFT * 1.6)
        self.play(LaggedStartMap(FadeIn, squares, shift=UP * 0.8, lag_ratio=0.2), run_time=1.0)
        self.wait(0.3)
