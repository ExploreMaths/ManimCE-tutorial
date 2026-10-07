"""IndicationBasics: FocusOn / Indicate / Flash / Circumscribe 四种常用强调。"""

from manim import *


class IndicationBasics(Scene):
    def construct(self):
        square = Square().shift(LEFT * 2.5)
        circle = Circle().shift(RIGHT * 2.5)
        text = Text("重点", font_size=40)
        self.add(square, circle, text)

        self.play(FocusOn(circle), run_time=0.8)
        self.play(Indicate(square), run_time=0.8)
        self.play(Flash(circle.get_center()), run_time=0.7)
        self.play(Circumscribe(text), run_time=1.2)
        self.wait(0.5)
