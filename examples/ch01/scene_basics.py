"""SceneBasics: add / play / wait / remove on a single Scene."""

from manim import *


class SceneBasics(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, opacity=0.6)
        label = Text("play 才有动画", font_size=36)
        label.next_to(square, DOWN)

        # add 不播放动画，物体瞬间出现在画面里
        self.add(square)
        self.wait(0.5)

        # play 才有逐帧的动画过程
        self.play(FadeIn(label), run_time=1.0)
        self.play(square.animate.shift(LEFT * 2), run_time=1.0)
        self.play(FadeOut(label), run_time=0.5)

        # remove 与 add 一样没有动画，物体瞬间消失
        self.remove(square)
        self.wait(0.5)
