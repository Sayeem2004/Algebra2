#!/usr/bin/env python

from manimlib.imports import *

class FirstScene(Scene):
    def construct(self):
        c1 = Circle()
        c1.move_to(np.array([5,0,0]))
        c2 = Circle()
        c2.move_to(np.array([-5,0,0]))
        s1 = Square()
        s1.move_to(np.array([-1,0,0]))
        s2 = Square()
        s2.move_to(np.array([1,0,0]))
        self.play(GrowFromCenter(s1,run_time=3),GrowFromCenter(s2,run_time=3))
        self.play(Transform(s1,c1,run_time=3),Transform(s2,c2,run_time=3))
        d1 = Dot(radius=.5)
        self.play(Transform(s1,d1,run_time=3),Transform(s2,d1,run_time=3))
        self.play(ShrinkToCenter(s1,run_time=1),ShrinkToCenter(s2,run_time=1))

class CakeSolutionP1(Scene):
    def construct(self):
        t1 = TextMobject("Portion 1")
        t2 = TextMobject("Portion 1")
        t2.move_to(np.array([0,3,0]))
        self.play(Write(t1,run_time = 2))
        self.play(Transform(t1,t2))
        self.wait(5)
