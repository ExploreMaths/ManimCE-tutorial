from manim import *


class MobjectMethods(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=0.6)
        circle = Circle().set_fill(RED, opacity=0.6).to_edge(RIGHT)
        self.add(circle)
        self.play(FadeIn(square))
        self.play(square.animate.shift(2 * LEFT))
        square.save_state()
        self.play(square.animate.rotate(PI / 4).scale(0.5))
        self.play(square.animate.restore())
        self.play(square.animate.next_to(circle, LEFT, buff=0.1))
