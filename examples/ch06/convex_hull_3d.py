from manim import *


class ConvexHullDemo(ThreeDScene):
    def construct(self):
        rng = np.random.default_rng(0)
        points = [rng.uniform(-2.5, 2.5, 3) for _ in range(12)]
        dots = VGroup(*[Dot3D(p, radius=0.06, color=YELLOW) for p in points])
        hull = ConvexHull3D(*points)
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)
        self.play(FadeIn(dots), run_time=1)
        self.play(Create(hull), run_time=2)
        self.wait(1)
