from manim import *


class ThreeDLinesAndSurface(ThreeDScene):
    def construct(self):
        line = Line3D(ORIGIN, [2, 2, 2])
        arrow = Arrow3D([-2.5, 0, 0], [-2.5, 0, 2])
        dot = Dot3D([2, -1.5, 1], color=YELLOW)

        def saddle(u, v):
            return np.array([u, v, 0.5 * u * v])

        surface = Surface(
            saddle,
            u_range=(-2, 2),
            v_range=(-2, 2),
            resolution=(16, 16),
        )
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(line), Create(arrow), FadeIn(dot), run_time=1)
        self.play(Create(surface), run_time=2)
        self.wait(0.5)
        self.move_camera(theta=20 * DEGREES, run_time=1)
