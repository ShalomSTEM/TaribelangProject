from pickle import GLOBAL
from GameFrame import Level, Globals
from Objects.TitleMilbiButton import TitleMilbiButton
import os
from enum import IntEnum


class EnumTitle(IntEnum):
    WelcomeToCountry = 0
    Milbi = 1
    Carpet = 2
    Museum = 3
    Quiz = 4


class TitleScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("MilbiL3/PlaceHolderBackgroundMLBL3.png")
        button1 = TitleMilbiButton(self, 160, 160, EnumTitle.Milbi)
        self.add_room_object(button1)
