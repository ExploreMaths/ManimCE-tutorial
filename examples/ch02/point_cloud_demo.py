from manim import *


class PointCloudDemo(Scene):
    def construct(self):
        cloud = PointCloudDot(radius=1.2, density=15, color=YELLOW)
        small = PointCloudDot(radius=0.6, density=25, color=RED).shift(2.5 * RIGHT)
        self.play(FadeIn(cloud), FadeIn(small))
        self.play(cloud.animate.scale(1.3))
        self.wait(0.5)
