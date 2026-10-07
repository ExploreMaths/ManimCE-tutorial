from manim import *


class ThreeDSolids(ThreeDScene):
    def construct(self):
        solids = VGroup(
            Cube(),
            Sphere(),
            Cone(),
            Cylinder(),
            Torus(major_radius=1, minor_radius=0.35),
            Prism(dimensions=[1.5, 1.0, 0.8]),
        )
        solids.arrange(RIGHT, buff=0.8)
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)
        self.play(FadeIn(solids), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(2)
        self.stop_ambient_camera_rotation()
