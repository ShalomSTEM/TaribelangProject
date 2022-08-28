from GameFrame import Level, Globals
from Objects.TitleMilbiButton import TitleMilbiButton
import os
from enum import IntEnum


class TitleScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("MilbiL3/PlaceHolderBackgroundMLBL3.png")
        button1 = TitleMilbiButton(self, 160, 160, Globals.EnumWTC_Taribelang)
        # button2 = TitleLeftButton(self, 0, 0, EnumTitle.Milbi)
        self.add_room_object(button1)
        # self.add_room_object(button2)
