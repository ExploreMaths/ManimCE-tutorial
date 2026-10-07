from manim import *


class DashedDemo(Scene):
    def construct(self):
        circle = Circle()
        dashed = DashedVMobject(
            circle, num_dashes=20, dashed_ratio=0.4, color=YELLOW
        ).shift(1.5 * UP)
        self.play(Create(dashed))
        curve = ParametricFunction(
            lambda t: [t, np.sin(2 * t), 0], t_range=[-PI, PI, 0.02]
        ).shift(1.8 * DOWN)
        segments = CurvesAsSubmobjects(curve)
        segments.set_color_by_gradient(BLUE, RED)
        self.play(Create(segments))
        self.wait(0.5)
