from manim import *


class VectorFieldDemo(Scene):
    def construct(self):
        def field(p):
            return np.array([-p[1], p[0], 0]) / 3

        vf = ArrowVectorField(field, x_range=[-7, 7, 1], y_range=[-4, 4, 1])
        self.play(Create(vf), run_time=1.5)
        sl = StreamLines(field, x_range=[-7, 7, 0.8], y_range=[-4, 4, 0.8],
                         noise_factor=0.2)
        self.add(sl)
        self.play(Create(sl), run_time=3)
        self.wait()
