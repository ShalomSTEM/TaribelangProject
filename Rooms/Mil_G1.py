from GameFrame import Globals, Level
from GameFrame.TextObject import TextObject

class Mil_G1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        text = TextObject(self, Globals.SCREEN_HEIGHT/2, Globals.SCREEN_HEIGHT/2, text='Mil_G1', size=60, font='Comic Sans MS', colour=(0, 0, 0))
        self.add_room_object(text)