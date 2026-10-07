from manim import *


class PolyhedraShowcase(ThreeDScene):
    def construct(self):
        solids = VGroup(
            Tetrahedron(edge_length=1.4),
            Octahedron(edge_length=1.4),
            Icosahedron(edge_length=1.4),
            Dodecahedron(edge_length=1.2),
        )
        solids.arrange(RIGHT, buff=0.6)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.play(FadeIn(solids), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(2)
        self.stop_ambient_camera_rotation()
