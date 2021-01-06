from manimlib.imports import *
from math import*

class Test(Scene):
    def construct(self):
        tex1 = TextMobject("In order to solve this problem we need to learn about arcs and sectors.")
        tex1.scale(.7)
        self.play(ShowCreation(tex1))
        self.wait(2)

        tex2 = TextMobject("But first we need to review what we know about circles.")
        tex2.scale(.7)
        self.play(Transform(tex1,tex2))
        self.wait(2)
        self.play(FadeOut(tex1))
        self.wait(1)

        c1 = Circle(radius=2,color=BLUE)
        self.play(ShowCreation(c1))
        self.wait(1)
        r1 = Line((0,0,0),(2,0,0),color=WHITE)
        n1 = TexMobject(r"2")
        n1.scale(.7)
        n1.move_to((1,-0.3,0))
        self.play(ShowCreation(n1),ShowCreation(r1))
        self.wait(1)

        c2 = Circle(radius=2,color=MAROON)
        tex3 = TexMobject(r"\text{The Circumference of a Circle is calculated as } 2 \pi r")
        tex3.scale(.7)
        tex3.shift(UP*3)
        self.play(ShowCreation(tex3,run_time=2),ShowCreation(c2,run_time=4))
        self.wait(2)
        temp1 = TexMobject(r"2 \pi r")
        temp2 = TexMobject(r"2 \pi 2")
        temp3 = TexMobject(r"4 \pi")
        temp1.shift(RIGHT*3)
        temp2.shift(RIGHT*3)
        temp3.shift(RIGHT*3)
        self.play(ShowCreation(temp1))
        self.wait(.5)
        self.play(Transform(temp1,temp2))
        self.wait(.5)
        self.play(Transform(temp1,temp3))
        self.wait(2)
        self.play(FadeOut(tex3),FadeOut(temp1))
        self.wait(1)

        c3 = Circle(radius=2,color=MAROON,fill_opacity=1)
        tex4 = TexMobject(r"\text{The Area of a Circle is calculated as } \pi r^2 ")
        tex4.scale(.7)
        tex4.shift(UP*3)
        self.play(ShowCreation(tex4,run_time=2),ShowCreation(c3,run_time=4))
        self.wait(2)
        temp4 = TexMobject(r"\pi r^2")
        temp5 = TexMobject(r"\pi 2^2")
        temp6 = TexMobject(r"4 \pi")
        temp4.shift(RIGHT*3)
        temp5.shift(RIGHT*3)
        temp6.shift(RIGHT*3)
        self.play(ShowCreation(temp4))
        self.wait(.5)
        self.play(Transform(temp4,temp5))
        self.wait(.5)
        self.play(Transform(temp4,temp6))
        self.wait(2)
        self.play(FadeOut(tex4),FadeOut(c3),FadeOut(c2,run_time=.2),FadeOut(temp4))
        self.wait(2)

        tex5 = TextMobject("Now we can learn about Arcs and Sectors.")
        tex5.scale(.7)
        tex5.shift(UP*3)
        tex6 = TextMobject("An arc is defined as a portion of a Circle.")
        tex6.scale(.7)
        tex6.shift(UP*3)
        self.play(ShowCreation(tex5))
        self.wait(2)
        self.play(Transform(tex5,tex6))
        self.wait(2)
        a1 = Arc(radius=2,angle=math.radians(45),color=MAROON)
        a2 = Arc(radius=2,angle=math.radians(90),color=MAROON)
        a3 = Arc(radius=2,angle=math.radians(270),color=MAROON)
        self.play(ShowCreation(a1,run_time=.5))
        self.wait(.5)
        self.play(ShowCreation(a2,run_time=1))
        self.wait(.5)
        self.play(ShowCreation(a3,run_time=2))
        self.wait(1)
        self.play(FadeOut(a1),FadeOut(a3))
        tex7 = TextMobject("An arc has a Central Angle and an Arc Length")
        tex7.scale(.7)
        tex7.shift(UP*3)
        r2 = Line((0,0,0),(0,2,0))
        self.play(ShowCreation(r2),Transform(tex5,tex7))
        self.wait(10)
        f1 = TexMobject(r"\frac{\text{Arc Length}}{\text{Circumference}} = \frac{\theta}{360}")
        f1.shift(RIGHT*4)
        f1.scale(.8)
        self.play(ShowCreation(f1))
        self.wait(8)

        self.play(FadeOut(tex5),FadeOut(r2),FadeOut(f1),FadeOut(a2))
        self.wait(2)
        tex8 = TextMobject("A Sector is defined as a region of a circle enclosed by an arc and 2 radii.")
        tex8.scale(.7)
        tex8.shift(UP*3)
        self.play(ShowCreation(tex8))
        self.wait(2)
        s1 = Sector(angle=math.radians(45),color=MAROON)
        s2 = Sector(angle=math.radians(90),color=MAROON)
        s3 = Sector(angle=math.radians(270),color=MAROON)
        s1.shift(RIGHT*.5,UP*.3)
        s2.shift(RIGHT*.5,UP*.5)
        s1.scale(2)
        s2.scale(2)
        s3.scale(2)
        self.play(ShowCreation(s1,run_time=.5))
        self.wait(.5)
        self.play(ShowCreation(s2,run_time=1))
        self.wait(.5)
        self.play(ShowCreation(s3,run_time=2))
        self.wait(1)
        self.play(FadeOut(s1),FadeOut(s3))
        tex9 = TextMobject("A sector has a Central Angle and a Sector Area")
        tex9.scale(.7)
        tex9.shift(UP*3)
        self.play(Transform(tex8,tex9))
        self.wait(10)
        f2 = TexMobject(r"\frac{\text{Sector Area}}{\text{Total Area}} = \frac{\theta}{360}")
        f2.shift(RIGHT*4)
        f2.scale(.8)
        self.play(ShowCreation(f2))
        self.wait(8)

        self.play(FadeOut(f2),FadeOut(c1),FadeOut(r1),FadeOut(n1),FadeOut(tex8),FadeOut(s2))
        self.wait(1)
        tex10 = TextMobject("Now back to those slices of cake.")
        tex10.scale(.7)
        self.play(ShowCreation(tex10))
        self.wait(.5)
        self.play(FadeOut(tex10))