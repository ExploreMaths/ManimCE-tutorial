"""FadeTransformDemo: FadeTransform / FadeTransformPieces / FadeToColor."""

from manim import *


class FadeTransformDemo(Scene):
    def construct(self):
        # FadeTransform：先淡出原物、再淡入目标物（注意它在 transform 模块，不在 fading 模块）
        square = Square().set_fill(RED, opacity=0.6)
        circle = Circle().set_fill(GREEN, opacity=0.6)
        self.add(square)
        self.play(FadeTransform(square, circle), run_time=0.8)
        self.wait(0.2)

        # FadeTransformPieces：按子对象一一对应做淡入淡出变换
        src = VGroup(*[Square(0.4).set_fill(BLUE, opacity=0.6) for _ in range(4)]).arrange(RIGHT)
        dst = VGroup(*[Circle(0.25).set_fill(YELLOW, opacity=0.6) for _ in range(4)]).arrange(RIGHT)
        self.play(FadeTransformPieces(src, dst), run_time=0.9)
        self.wait(0.2)

        # FadeToColor：整体渐变为指定颜色
        self.play(FadeToColor(dst, PURPLE), run_time=0.6)
        self.wait(0.3)
