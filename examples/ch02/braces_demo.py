"""BracesDemo: Brace / BraceBetweenPoints / BraceLabel / BraceText / ArcBrace."""

from manim import *


class BracesDemo(Scene):
    def construct(self):
        obj = Rectangle(width=4, height=1.5, color=BLUE)
        obj.shift(UP * 1.5)
        self.play(Create(obj))

        brace = Brace(obj, direction=DOWN)
        brace_text = BraceText(obj, "width = 4", label_constructor=Text, font_size=30)
        self.play(GrowFromCenter(brace), Write(brace_text))
        self.wait(0.5)

        p1 = LEFT * 5 + DOWN * 2
        p2 = LEFT * 2 + DOWN * 3
        points_brace = BraceBetweenPoints(p1, p2, direction=RIGHT)
        points_line = Line(p1, p2)
        points_label = BraceLabel(
            Line(p1, p2),
            "\\sqrt{10}",
            brace_direction=RIGHT,
            font_size=30,
        )

        arc = Arc(radius=1.2, start_angle=PI / 4, angle=PI / 2).shift(RIGHT * 3 + DOWN * 1.5)
        arc_brace = ArcBrace(arc)

        self.play(Create(points_line), GrowFromCenter(points_brace), Write(points_label))
        self.play(Create(arc), GrowFromCenter(arc_brace))
        self.wait(0.5)
