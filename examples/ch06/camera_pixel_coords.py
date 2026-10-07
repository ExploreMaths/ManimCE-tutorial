from manim import *


class PixelCoords(Scene):
    def construct(self):
        dots = VGroup(Dot(ORIGIN), Dot(RIGHT * 3 + UP * 2), Dot(LEFT * 4 + DOWN * 2.5))
        labels = VGroup()
        for d in dots:
            x, y = self.camera.points_to_pixel_coords(d, [d.get_center()])[0]
            labels.add(Text(f"({x:.0f}, {y:.0f})", font_size=20).next_to(d, UP))
        self.add(dots, labels)
        self.wait(0.5)
