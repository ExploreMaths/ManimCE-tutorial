"""ImageArrayDemo: ImageMobject built from an in-memory numpy array."""

import numpy as np

from manim import *


class ImageArrayDemo(Scene):
    def construct(self):
        # Build a 64x64 RGBA checkerboard in memory — no external file needed.
        n = 64
        grid = np.indices((n, n)).sum(axis=0) % 2
        rgb = np.zeros((n, n, 4), dtype=np.uint8)
        rgb[grid == 0] = (88, 196, 221, 255)  # TEAL-ish
        rgb[grid == 1] = (10, 20, 68, 255)  # dark navy

        image = ImageMobject(rgb)
        image.scale(3)

        self.play(FadeIn(image))
        self.play(image.animate.rotate(PI / 8).shift(LEFT * 2))
        self.wait(1)
