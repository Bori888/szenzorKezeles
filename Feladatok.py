#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

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

    def akumlator_allapot(self):
        #konzoolablakra kiirás
        akuErtek  = ("Az aku töltötségi\n szintje: " +str(int(self.ev3.battery.voltage())/1000)+ " V")
        print(akuErtek)
        #robotra kiirás
        self.ev3.screen.print(akuErtek)
        wait(3000)


    def ne_zuhanjon_le(self):
        #: Haladjon az asztal széle fele a robot majd álljon meg a szélén.
        
        while(self.cs.reflection()>45):
            self.robot.drive(100, 0)
            print("Szín",self.cs.reflection() )
        self.robot.stop(Stop.BRAKE)
        



    def vissza_all_ne_zuhanjon_le(self):
        self.ido.reset()
        self.ne_zuhanjon_le()
        eltelt_ido = self.ido.time()
        self.ido.pause()
        self.robot.drive(-100, 0)
        wait(eltelt_ido)
        self.robot.stop(Stop.BRAKE)

    def adativ_sebesseg_radar(self):
        while(self.us.distance()>100):
            self.robot.drive(self.us.distance(), 0)
            print("Távolság: " +str(self.us.distance()) )
        self.robot.stop(Stop.BRAKE)

    def keprnyore_rajzolas(self):
        self.robot.drive(100,0) 
        self.ido.reset()
        hol = 0
        while(self.ido.time()< 3000):
            if (self.cs.reflection()< 45):
                self.ev3.screen.draw_line(hol, 0, hol, 127)  
            hol +=1
            wait(3000/170)     
        self.robot.stop(Stop.BRAKE)
        wait(10000)



    def alljon_meg_a_vonal_utan(self):
        while(self.cs.reflection()>30):
            self.robot.drive(100, 0)
            print("Szín",self.cs.reflection() )
        while(self.cs.reflection()<30):
            self.robot.drive(100, 0)
            print("Szín",self.cs.reflection() )
        self.robot.stop(Stop.BRAKE)

    def alljon_meg_a_vonal_utan2(self):
        vege = False
        fekete =False
        self.robot.drive(100, 0)
        while not vege:
            if self.cs.reflection() < 39 :
                fekete = True
            if fekete and self.cs.reflection() > 39+5 :
                vege = True
        self.robot.stop(Stop.BRAKE)
    
    def hany_vonal(self, db, seb, hatar):
        for vonalak in range(db):
            vege = False
            fekete =False
            self.robot.drive(seb, 0)
            while not vege:
                if self.cs.reflection() < hatar :
                    fekete = True
                if fekete and self.cs.reflection() > hatar+5 :
                    vege = True
            self.robot.stop(Stop.BRAKE)
            
    
    def hany_vonal_param(self):
        self.hany_vonal(5,100,39)

    def hany_vonal_param_hatra(self):
        self.hany_vonal(5,-100,39)

    def vonal_idoben_merve(self, db, seb, hatar):
        hosszak=[]
        for vonalak in range(db):
            vege = False
            fekete =False
            self.robot.drive(seb, 0)
            while not vege:
                if self.cs.reflection() < hatar :
                    fekete = True
                    self.ido.reset()
                if fekete and self.cs.reflection() > hatar+5 :
                    vege = True
                    hossz = self.ido.time()
                    hosszak.append(hossz)
        self.robot.stop(Stop.BRAKE)
        print(hosszak)
        return hosszak
    def rovid_vagy_hosszu(self):
        hosszak= self.vonal_idoben_merve(5,100,39)
        max_i =0
        min_i = 0
        for index in range(len (hosszak)):
            if hosszak[index]<hosszak[min_i]:
                min_i = index
            if hosszak[index]>hosszak[max_i]:
                max_i = index

        for csipog in range(max_i+1):
            self.ev3.speaker.beep(50,500)
            wait(100)

    def zenedoboz(self):
        hosszak= self.vonal_idoben_merve(5,100,39)
        max_i =0
        min_i = 0
        for index in range(len (hosszak)):
            if hosszak[index]<hosszak[min_i]:
                min_i = index
            if hosszak[index]>hosszak[max_i]:
                max_i = index
        kozepertek=(hosszak[min_i]+hosszak[max_i])/2

        for index in range(len(hosszak)):
            if hosszak[index]<kozepertek:
                self.ev3.speaker.beep(200,100)
            else:
                self.ev3.speaker.beep(200,200)
            wait(100)

                



        



    def csipog(self):
        self.ev3.speaker.beep()

