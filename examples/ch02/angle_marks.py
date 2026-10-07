"""AngleMarks: Angle / RightAngle / Elbow / TangentLine / TangentialArc."""

from manim import *


class AngleMarks(Scene):
    def construct(self):
        line1 = Line(ORIGIN, RIGHT * 2)
        line2 = Line(ORIGIN, UP * 1.5 + RIGHT)
        angle = Angle(line1, line2, radius=0.6, dot=True, dot_color=RED)
        value = Angle(line1, line2, radius=0.45).get_value(degrees=True)
        label = Text(f"{value:.0f}°", font_size=30).move_to(
            Angle(line1, line2, radius=0.9).point_from_proportion(0.5)
        )

        hline = Line(LEFT * 5 + UP * 2, LEFT * 3 + UP * 2)
        vline = Line(LEFT * 4 + UP * 2, LEFT * 4 + UP * 0.5)
        right_angle = RightAngle(hline, vline, length=0.35)

        circle = Circle(radius=1.2).shift(RIGHT * 3.5 + DOWN * 1.5)
        tangent = TangentLine(circle, alpha=0.25, length=2, color=YELLOW)

        self.play(Create(line1), Create(line2))
        self.play(Create(angle), Write(label))
        self.play(Create(hline), Create(vline), Create(right_angle))
        self.play(Create(circle), Create(tangent))
        self.wait(1)
