from manim import *


class ZoomDemo(ZoomedScene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(LEFT * 2.5)
        square = Square(side_length=0.4, fill_color=BLUE, fill_opacity=1).shift(RIGHT)
        self.add(dot, square)
        self.activate_zooming(animate=True)
        self.play(self.zoomed_camera.frame.animate.move_to(dot), run_time=1.5)
        self.wait(1)
