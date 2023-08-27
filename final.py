from manimlib.imports import *
from math import*

class Final(Scene):
    def construct(self):
        # Cake 1 Cake 1 Cake 1 Cake 1 Cake 1
        title1 = TextMobject("Cake Slices")
        self.play(Write(title1))
        self.play(ApplyMethod(title1.shift,UP*3.4,run_time=2))
        self.wait(3)

        heading1 = TextMobject("Slice 1")
        heading1.shift(UP*2.8)
        heading1.scale(.75)
        self.play(Write(heading1,run_time=2))
        self.wait(3)

        sector1 = Sector(radius=2,angle=math.radians(101.25),arc_center=np.array([-0.3,1,0]),color=MAROON_B)
        sector1.scale(1.75)
        self.play(GrowFromCenter(sector1))
        self.wait(1)

        text1 = TexMobject(r"\text{Radius} = 8")
        text1.move_to((0,.1,0))
        text1.scale(.6)
        self.play(Write(text1))
        self.wait(1.5)

        text2 = TexMobject(r"\text{Arc Length} = 4.5 \pi")
        text2.move_to((0,-.3,0))
        text2.scale(.6)
        self.play(Write(text2))
        self.wait(1.5)

        text3 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot r")
        text3.move_to((0,-.7,0))
        text3.scale(.6)
        self.play(Write(text3))
        self.wait(4)

        text4 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot 8")
        text4.move_to((0,-.7,0))
        text4.scale(.6)
        self.play(Transform(text3,text4))
        self.wait(1)

        text5 = TexMobject(r"\text{Circumference} = 16 \pi")
        text5.move_to((0,-.7,0))
        text5.scale(.6)
        self.play(Transform(text3,text5))
        self.wait(3)

        text6 = TexMobject(r"\frac{\text{Arc Length}}{\text{Circumference}} = \frac{\theta}{360}")
        text6.move_to((0,-1.3,0))
        text6.scale(.6)
        self.play(Write(text6))
        self.wait(6)

        text7 = TexMobject(r"\frac{4.5 \pi}{16 \pi} = \frac{\theta}{360}")
        text7.move_to((0,-1.3,0))
        text7.scale(.6)
        self.play(Transform(text6,text7))
        self.wait(1)

        text8 = TexMobject(r"0.28125 = \frac{\theta}{360}")
        text8.move_to((0,-1.3,0))
        text8.scale(.6)
        self.play(Transform(text6,text8))
        self.wait(1)

        text9 = TexMobject(r"\theta = 101.25^{\circ}")
        text9.move_to((0,-1.1,0))
        text9.scale(.6)
        self.play(Transform(text6,text9))
        self.wait(3)

        text10 = TexMobject(r"\text{Circle Area} = \pi \cdot  r^{2}")
        text10.move_to((0,-1.5,0))
        text10.scale(.6)
        self.play(Write(text10))
        self.wait(4)

        text11 = TexMobject(r"\text{Circle Area} = \pi \cdot  8^{2}")
        text11.move_to((0,-1.5,0))
        text11.scale(.6)
        self.play(Transform(text10,text11))
        self.wait(1)

        text12 = TexMobject(r"\text{Circle Area} = 64 \pi")
        text12.move_to((0,-1.5,0))
        text12.scale(.6)
        self.play(Transform(text10,text12))
        self.wait(3)

        text13 = TexMobject(r"\frac{\text{Sector Area}}{\text{Total Area}} = \frac{\theta}{360}")
        text13.move_to((0,-2.1,0))
        text13.scale(.6)
        self.play(Write(text13))
        self.wait(6)

        text14 = TexMobject(r"\frac{\text{Sector Area}}{64 \pi} = \frac{101.25}{360}")
        text14.move_to((0,-2.1,0))
        text14.scale(.6)
        self.play(Transform(text13,text14))
        self.wait(1)

        text15 = TexMobject(r"\frac{\text{Sector Area}}{64 \pi} = \frac{9}{32}")
        text15.move_to((0,-2.1,0))
        text15.scale(.6)
        self.play(Transform(text13,text15))
        self.wait(1)

        text16 = TexMobject(r"\frac{\text{Sector Area}}{64 \pi} = 0.28125")
        text16.move_to((0,-2.1,0))
        text16.scale(.6)
        self.play(Transform(text13,text16))
        self.wait(1)

        text17 = TexMobject(r"\text{Sector Area} = 18 \pi")
        text17.move_to((0,-1.9,0))
        text17.scale(.6)
        self.play(Transform(text13,text17))
        self.wait(6)

        self.play(ApplyMethod(heading1.shift,4*LEFT),ApplyMethod(sector1.shift,4*LEFT),ApplyMethod(text1.shift,4*LEFT),ApplyMethod(text2.shift,4*LEFT),ApplyMethod(text3.shift,4*LEFT),ApplyMethod(text6.shift,4*LEFT),ApplyMethod(text10.shift,4*LEFT),ApplyMethod(text13.shift,4*LEFT))










        # Speedy Cakes Speedy Cakes Speedy Cakes Speedy Cakes Speedy Cakes
        heading2 = TextMobject("Slice 2")
        heading2.shift(UP*2.8)
        heading2.scale(.75)
        heading3 = TextMobject("Slice 3")
        heading3.shift(UP*2.8,RIGHT*4)
        heading3.scale(.75)
        self.play(Write(heading2,run_time=.6),Write(heading3,run_time=.6))

        sector2 = Sector(radius=3,angle=math.radians(72),arc_center=np.array([-0.5,1,0]),color=TEAL)
        sector2.scale(1.75)
        sector3 = Sector(radius=4,angle=math.radians(45),arc_center=np.array([3.5,1,0]),color=PURPLE)
        sector3.scale(1.75)
        self.play(GrowFromCenter(sector2,run_time=.6),GrowFromCenter(sector3,run_time=.6))

        ctext1 = TexMobject(r"\text{Radius} = 10")
        ctext1.move_to((0,.1,0))
        ctext1.scale(.6)
        cctext1 = TexMobject(r"\text{Radius} = 12")
        cctext1.move_to((4,.1,0))
        cctext1.scale(.6)
        self.play(Write(ctext1,run_time=.6),Write(cctext1,run_time=.6))

        ctext2 = TexMobject(r"\text{Arc Length} = 4 \pi")
        ctext2.move_to((0,-.3,0))
        ctext2.scale(.6)
        cctext2 = TexMobject(r"\text{Arc Length} = 3 \pi")
        cctext2.move_to((4,-.3,0))
        cctext2.scale(.6)
        self.play(Write(ctext2,run_time=.6),Write(cctext2,run_time=.6))

        ctext3 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot r")
        ctext3.move_to((0,-.7,0))
        ctext3.scale(.6)
        cctext3 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot r")
        cctext3.move_to((4,-.7,0))
        cctext3.scale(.6)
        self.play(Write(ctext3,run_time=.6),Write(cctext3,run_time=.6))

        ctext4 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot 10")
        ctext4.move_to((0,-.7,0))
        ctext4.scale(.6)
        cctext4 = TexMobject(r"\text{Circumference} = 2 \cdot \pi \cdot 12")
        cctext4.move_to((4,-.7,0))
        cctext4.scale(.6)
        self.play(Transform(ctext3,ctext4,run_time=.6),Transform(cctext3,cctext4,run_time=.6))

        ctext5 = TexMobject(r"\text{Circumference} = 20 \pi")
        ctext5.move_to((0,-.7,0))
        ctext5.scale(.6)
        cctext5 = TexMobject(r"\text{Circumference} = 24 \pi")
        cctext5.move_to((4,-.7,0))
        cctext5.scale(.6)
        self.play(Transform(ctext3,ctext5,run_time=.6),Transform(cctext3,cctext5,run_time=.6))

        ctext6 = TexMobject(r"\frac{\text{Arc Length}}{\text{Circumference}} = \frac{\theta}{360}")
        ctext6.move_to((0,-1.3,0))
        ctext6.scale(.6)
        cctext6 = TexMobject(r"\frac{\text{Arc Length}}{\text{Circumference}} = \frac{\theta}{360}")
        cctext6.move_to((4,-1.3,0))
        cctext6.scale(.6)
        self.play(Write(ctext6,run_time=.6),Write(cctext6,run_time=.6))

        ctext7 = TexMobject(r"\frac{4 \pi}{20 \pi} = \frac{\theta}{360}")
        ctext7.move_to((0,-1.3,0))
        ctext7.scale(.6)
        cctext7 = TexMobject(r"\frac{3 \pi}{24 \pi} = \frac{\theta}{360}")
        cctext7.move_to((4,-1.3,0))
        cctext7.scale(.6)
        self.play(Transform(ctext6,ctext7,run_time=.6),Transform(cctext6,cctext7,run_time=.6))

        ctext8 = TexMobject(r"0.2 = \frac{\theta}{360}")
        ctext8.move_to((0,-1.3,0))
        ctext8.scale(.6)
        cctext8 = TexMobject(r"0.125 = \frac{\theta}{360}")
        cctext8.move_to((4,-1.3,0))
        cctext8.scale(.6)
        self.play(Transform(ctext6,ctext8,run_time=.6),Transform(cctext6,cctext8,run_time=.6))

        ctext9 = TexMobject(r"\theta = 72^{\circ}")
        ctext9.move_to((0,-1.1,0))
        ctext9.scale(.6)
        cctext9 = TexMobject(r"\theta = 45^{\circ}")
        cctext9.move_to((4,-1.1,0))
        cctext9.scale(.6)
        self.play(Transform(ctext6,ctext9,run_time=.6),Transform(cctext6,cctext9,run_time=.6))

        ctext10 = TexMobject(r"\text{Circle Area} = \pi \cdot  r^{2}")
        ctext10.move_to((0,-1.5,0))
        ctext10.scale(.6)
        cctext10 = TexMobject(r"\text{Circle Area} = \pi \cdot  r^{2}")
        cctext10.move_to((4,-1.5,0))
        cctext10.scale(.6)
        self.play(Write(ctext10,run_time=.6),Write(cctext10,run_time=.6))

        ctext11 = TexMobject(r"\text{Circle Area} = \pi \cdot  10^{2}")
        ctext11.move_to((0,-1.5,0))
        ctext11.scale(.6)
        cctext11 = TexMobject(r"\text{Circle Area} = \pi \cdot  12^{2}")
        cctext11.move_to((4,-1.5,0))
        cctext11.scale(.6)
        self.play(Transform(ctext10,ctext11,run_time=.6),Transform(cctext10,cctext11,run_time=.6))

        ctext12 = TexMobject(r"\text{Circle Area} = 100 \pi")
        ctext12.move_to((0,-1.5,0))
        ctext12.scale(.6)
        cctext12 = TexMobject(r"\text{Circle Area} = 144 \pi")
        cctext12.move_to((4,-1.5,0))
        cctext12.scale(.6)
        self.play(Transform(ctext10,ctext12,run_time=.6),Transform(cctext10,cctext12,run_time=.6))

        ctext13 = TexMobject(r"\frac{\text{Sector Area}}{\text{Total Area}} = \frac{\theta}{360}")
        ctext13.move_to((0,-2.1,0))
        ctext13.scale(.6)
        cctext13 = TexMobject(r"\frac{\text{Sector Area}}{\text{Total Area}} = \frac{\theta}{360}")
        cctext13.move_to((4,-2.1,0))
        cctext13.scale(.6)
        self.play(Write(ctext13,run_time=.6),Write(cctext13,run_time=.6))

        ctext14 = TexMobject(r"\frac{\text{Sector Area}}{100 \pi} = \frac{72}{360}")
        ctext14.move_to((0,-2.1,0))
        ctext14.scale(.6)
        cctext14 = TexMobject(r"\frac{\text{Sector Area}}{144 \pi} = \frac{45}{360}")
        cctext14.move_to((4,-2.1,0))
        cctext14.scale(.6)
        self.play(Transform(ctext13,ctext14,run_time=.6),Transform(cctext13,cctext14,run_time=.6))

        ctext15 = TexMobject(r"\frac{\text{Sector Area}}{100 \pi} = \frac{1}{5}")
        ctext15.move_to((0,-2.1,0))
        ctext15.scale(.6)
        cctext15 = TexMobject(r"\frac{\text{Sector Area}}{144 \pi} = \frac{1}{8}")
        cctext15.move_to((4,-2.1,0))
        cctext15.scale(.6)
        self.play(Transform(ctext13,ctext15,run_time=.6),Transform(cctext13,cctext15,run_time=.6))

        ctext16 = TexMobject(r"\frac{\text{Sector Area}}{100 \pi} = 0.20")
        ctext16.move_to((0,-2.1,0))
        ctext16.scale(.6)
        cctext16 = TexMobject(r"\frac{\text{Sector Area}}{144 \pi} = 0.125")
        cctext16.move_to((4,-2.1,0))
        cctext16.scale(.6)
        self.play(Transform(ctext13,ctext16,run_time=.6),Transform(cctext13,cctext16,run_time=.6))

        ctext17 = TexMobject(r"\text{Sector Area} = 20 \pi")
        ctext17.move_to((0,-1.9,0))
        ctext17.scale(.6)
        cctext17 = TexMobject(r"\text{Sector Area} = 18 \pi")
        cctext17.move_to((4,-1.9,0))
        cctext17.scale(.6)
        self.play(Transform(ctext13,ctext17,run_time=.6),Transform(cctext13,cctext17,run_time=.6))









        # Transition + End Transition + End Transition + End Transition + End Transition + End
        self.wait(4)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text6),FadeOut(text10),FadeOut(ctext1),FadeOut(ctext2),FadeOut(ctext3),FadeOut(ctext6),FadeOut(ctext10),FadeOut(cctext1),FadeOut(cctext2),FadeOut(cctext3),FadeOut(cctext6),FadeOut(cctext10))
        self.play(ApplyMethod(heading1.shift,DOWN),ApplyMethod(sector1.shift,DOWN),ApplyMethod(heading2.shift,DOWN),ApplyMethod(sector2.shift,DOWN),ApplyMethod(heading3.shift,DOWN),ApplyMethod(sector3.shift,DOWN),ApplyMethod(text13.shift,UP),ApplyMethod(ctext13.shift,UP),ApplyMethod(cctext13.shift,UP))
        self.wait(1)
        c11 = Ellipse(width=3.5,height=5,color=GREEN)
        self.play(ShowCreation(c11))
        self.wait(3)
        self.play(FadeOut(c11),FadeOut(heading1),FadeOut(sector1),FadeOut(heading2),FadeOut(sector2),FadeOut(heading3),FadeOut(sector3),FadeOut(text13),FadeOut(ctext13),FadeOut(cctext13),FadeOut(title1))
        self.wait(7)

        credit0 = TextMobject("Credits:")
        self.play(ApplyMethod(credit0.shift,UP*3))

        credit1 = TextMobject("Thanks to Andrew Juang for coding most of animation and doing the audio.")
        credit1.shift(UP*2)
        credit1.scale(.6)
        self.play(ShowCreation(credit1))
        self.wait(.5)

        credit2 = TextMobject("Thanks to Mohammad Khan for animating, compiling, and editing the video.")
        credit2.shift(UP)
        credit2.scale(.6)
        self.play(ShowCreation(credit2))
        self.wait(.5)

        credit3 = TextMobject("Thanks to Ken Li for creating the story, the script, and the minecraft world.")
        credit3.scale(.6)
        self.play(ShowCreation(credit3))
        self.wait(.5)

        credit4 = TextMobject("Thanks to Ivan Wei for allowing us to film on his minecraft server.")
        credit4.shift(DOWN)
        credit4.scale(.6)
        self.play(ShowCreation(credit4))
        self.wait(.5)

        credit5 = TextMobject("Thanks to Jeremy Ku-Benjet for helping us with tech support.")
        credit5.shift(DOWN*2)
        credit5.scale(.6)
        self.play(ShowCreation(credit5))
        self.wait(.5)

        credit6 = TextMobject("Thanks to Alvin Li for being comic relief.")
        credit6.shift(DOWN*3)
        credit6.scale(.6)
        self.play(ShowCreation(credit6))
        self.wait(3)

        self.play(FadeOut(credit0),FadeOut(credit1),FadeOut(credit2),FadeOut(credit3),FadeOut(credit4),FadeOut(credit5),FadeOut(credit6))
        self.wait(2)
