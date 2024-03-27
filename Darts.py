#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image
import random


class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #kép a kijelzőn

        self.kep1= Image(ImageFile.BOTTOM_LEFT)
        self.kep2= Image(ImageFile.BOTTOM_RIGHT)


        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopppr ora
        self.ido=StopWatch()
    
    def celtabla_rajzolas(self):
        self.ev3.screen.clear()
        self.ev3.screen.draw_circle(90,60,50,fill=True, color=Color.BLACK)
        
        db = 0
        for i in range(0,10,1):
            ketto = 2
            x= random.randint(ketto, 177-ketto)
            y= random.randint(ketto, 127-ketto)
            if (90-x)**2+(90-y)**2<=50**2:
                self.ev3.screen.draw_circle(x,y,ketto,fill=True, color=Color.WHITE)
                self.ev3.speaker.beep(500,100)
                db+=1
            else :
                self.ev3.screen.draw_circle(x,y,ketto,fill=True, color=Color.BLACK)
            wait(100)
        szoveg= "Talalat: ",db ,"."
        self.ev3.screen.draw_text(60,110,szoveg,Color.BLACK,None)
        wait(10000)
    
    def darts2(self):
        self.ev3.screen.draw_box(172,40,177,80, fill=True,color = Color.BLACK)

        y= random.randint(0, 127)

        for i in range(184):
            self.ev3.screen.draw_box(172,40,177,80, fill=True,color = Color.BLACK)
            self.ev3.screen.draw_circle(i,y,4,fill=True, color=Color.BLACK)
            wait(30)
            self.ev3.screen.draw_circle(i,y,4,fill=True, color=Color.WHITE)

        wait(5000)




        




    def csipog(self):
        self.ev3.speaker.beep()

