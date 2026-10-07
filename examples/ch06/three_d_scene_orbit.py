from manim import *


class ThreeDOrbit(ThreeDScene):
    def construct(self):
        cube = Cube(side_length=2)
        dot = Dot3D([1.5, 1.5, 1.5], color=YELLOW)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(cube), FadeIn(dot), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.4, about="theta")
        self.wait(1.5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1.2, run_time=1.5)
        self.wait(0.5)
