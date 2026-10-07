"""MatchingShapesDemo: TransformMatchingShapes 及 mismatches 处理."""

from manim import *


class MatchingShapesDemo(Scene):
    def construct(self):
        # 形状相同的子对象一一对应：各自飞过去，而不是整体变形
        src = VGroup(
            Circle(radius=0.3).set_fill(RED, opacity=0.6),
            Square(0.6).set_fill(GREEN, opacity=0.6),
            Triangle().set_fill(BLUE, opacity=0.6).scale(0.6),
        ).arrange(RIGHT, buff=0.8).shift(UP * 1.2)

        tar = VGroup(
            Square(0.6).set_fill(GREEN, opacity=0.6),
            Triangle().set_fill(BLUE, opacity=0.6).scale(0.6),
            Circle(radius=0.3).set_fill(RED, opacity=0.6),
        ).arrange(RIGHT, buff=0.8).shift(UP * 1.2)

        self.add(src)
        self.play(TransformMatchingShapes(src, tar), run_time=1.2)
        self.wait(0.3)

        # 数量不匹配时：fade_transform_mismatches=True 让多余/缺失的部分淡入淡出
        src2 = VGroup(*[Circle(radius=0.25).set_fill(TEAL, opacity=0.6) for _ in range(2)]).arrange(RIGHT)
        tar2 = VGroup(*[Circle(radius=0.25).set_fill(TEAL, opacity=0.6) for _ in range(4)]).arrange(RIGHT).shift(DOWN * 1.5)
        self.add(src2)
        self.play(
            TransformMatchingShapes(src2, tar2, fade_transform_mismatches=True),
            run_time=1.2,
        )
        self.wait(0.3)
