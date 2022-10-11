import os

from GameFrame import Level, Globals, EnumLevels

class Instructions_G3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)


        self.set_background_image(os.path.join("MilbiL3", "Instructions"))
        self.roomNum = EnumLevels.Instruction_MLBL3

