"""SectionsDemo: split one Scene into named sections via next_section()."""

from manim import *


class SectionsDemo(Scene):
    def construct(self):
        self.next_section("intro")
        title = Text("Section 演示", font_size=48)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)

        self.next_section("shift")
        self.play(title.animate.shift(UP * 2), run_time=1.0)
        self.wait(0.5)

        self.next_section("outro")
        self.play(FadeOut(title), run_time=1.0)
        self.wait(0.5)
