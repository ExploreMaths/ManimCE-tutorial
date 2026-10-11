from manim import *


class ComplexTrackerDemo(Scene):
    def construct(self):
        plane = ComplexPlane()
        self.add(plane)
        tracker = ComplexValueTracker(1 + 0j)
        dot = always_redraw(
            lambda: Dot(plane.n2p(tracker.get_value()), color=YELLOW)
        )
        self.add(dot)
        self.play(tracker.animate.set_value(1j), run_time=2)
        self.play(tracker.animate.set_value(-1 + 0j), rate_func=there_and_back, run_time=2)
        self.wait()
