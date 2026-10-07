"""AnnotationsDemo: SurroundingRectangle / BackgroundRectangle / Cross / Underline / Label / LabeledLine / LabeledArrow / LabeledPolygram."""

from manim import *


class AnnotationsDemo(Scene):
    def construct(self):
        formula = MathTex("e^{i\\pi} + 1 = 0", font_size=48)
        box = SurroundingRectangle(formula, color=YELLOW, buff=0.2, corner_radius=0.1)
        bg = BackgroundRectangle(formula, color=BLACK, fill_opacity=0.8, buff=0.1)
        under = Underline(formula, color=BLUE, buff=0.15)

        self.play(Write(formula))
        self.play(FadeIn(bg), Create(box), Create(under))

        cross_target = Cross(formula.copy(), stroke_color=RED)
        self.play(Write(cross_target))
        self.play(FadeOut(cross_target), run_time=0.5)

        line = LabeledLine(
            label="a",
            label_position=0.3,
            label_config={"font_size": 36},
            start=LEFT * 5 + DOWN * 2,
            end=LEFT * 2 + DOWN * 2.5,
        )
        arrow = LabeledArrow(
            label=Text("v", font_size=36),
            start=RIGHT * 0.5 + DOWN * 2,
            end=RIGHT * 3 + DOWN * 1,
        )
        poly = LabeledPolygram(
            [LEFT * 1.2, RIGHT * 1.2, UP * 1.2 + RIGHT * 0.4],
            label="\\Delta",
            color=WHITE,
        ).shift(DOWN * 0.3 + RIGHT * 4.2)

        self.play(Create(line), Create(arrow), Create(poly))
        self.wait(0.5)
