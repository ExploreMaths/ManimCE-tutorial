from manim import *


class CameraWalk(MovingCameraScene):
    def construct(self):
        dots = VGroup(
            *[Dot([i * 2.0 - 5, (-1) ** i, 0], radius=0.25) for i in range(6)]
        )
        self.add(dots)
        self.camera.frame.move_to(dots[2])
        self.wait(0.5)
        self.play(self.camera.frame.animate.move_to(dots[4]), run_time=1.5)
        self.play(self.camera.frame.animate.scale(0.5), run_time=1)
        self.play(self.camera.auto_zoom(dots[1:4], margin=1), run_time=1.5)
        self.wait(0.5)
