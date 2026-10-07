"""SquareToCircle: the classic first Manim scene.

Rendered by scripts/render_examples.py (one Scene class per file).
"""

from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_stroke(BLUE, width=4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        self.wait()
