#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok ,Darts

oraiMunka = Feladatok.Feladatok()
#oraiMunka.akumlator_allapot()

#oraiMunka.ne_zuhanjon_le()
#oraiMunka.vissza_all_ne_zuhanjon_le()
#oraiMunka.adativ_sebesseg_radar()
#oraiMunka.keprnyore_rajzolas()
#oraiMunka.alljon_meg_a_vonal_utan()
#oraiMunka.alljon_meg_a_vonal_utan2()
#oraiMunka.hany_vonal()
#oraiMunka.hany_vonal_param()
#oraiMunka.hany_vonal_param_hatra()
#print(oraiMunka.vonal_idoben_merve(5,100,39))
#oraiMunka.rovid_vagy_hosszu()
#oraiMunka.zenedoboz()
#oraiMunka.csipog()

darts = Darts.Darts()
#darts.celtabla_rajzolas()
darts.darts2()



darts.csipog()
