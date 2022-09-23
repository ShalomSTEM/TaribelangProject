from GameFrame import EnumLevels, Level, TextObject, Globals
import os

from Objects import Controller2


class ControllerOverlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.add_room_object(Controller2(self, 0, 0))
    def complete(self):
        Globals.next_level = Globals.oldRoom
        self.running = False