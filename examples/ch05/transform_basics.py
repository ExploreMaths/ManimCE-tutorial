"""TransformBasics: Transform / ReplacementTransform / TransformFromCopy / MoveToTarget / Restore."""

from manim import *


class TransformBasics(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=0.5)
        circle = Circle().set_fill(GREEN, opacity=0.5)
        triangle = Triangle().set_fill(BLUE, opacity=0.5)

        # Transform：原地变形，原物体留在场景里（变成目标的样子）
        self.add(square)
        self.play(Transform(square, circle), run_time=0.6)
        self.wait(0.2)

        # ReplacementTransform：目标物接替原物出现在场景中
        self.play(ReplacementTransform(square, triangle), run_time=0.6)
        self.wait(0.2)

        # TransformFromCopy：从原物“复制一份”变过去，原物保留
        self.play(TransformFromCopy(triangle, circle.copy().shift(RIGHT * 2)), run_time=0.6)
        self.wait(0.2)

        # generate_target + MoveToTarget：先准备好目标状态，再一次变换到位
        triangle.generate_target()
        triangle.target.shift(LEFT * 2).scale(0.5)
        self.play(MoveToTarget(triangle), run_time=0.6)
        self.wait(0.2)

        # save_state + Restore：记住当前状态，之后一键还原
        triangle.save_state()
        self.play(triangle.animate.rotate(PI / 2).shift(UP * 0.5), run_time=0.5)
        self.play(Restore(triangle), run_time=0.5)
        self.wait(0.3)
