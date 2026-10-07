from manim import *


class VMobjectStyles(Scene):
    def construct(self):
        fill_only = Square().set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        stroke_only = Circle().set_fill(opacity=0).set_stroke(BLUE, width=8)
        faded = RoundedRectangle().set_fill(RED, opacity=0.4).set_stroke(WHITE, width=2)
        group = VGroup(fill_only, stroke_only, faded).arrange(RIGHT, buff=0.6)
        self.play(FadeIn(group))
        self.play(group.animate.set_opacity(0.4))
        self.wait(0.5)
