from GameFrame import RoomObject, Globals
import os


class Grass(RoomObject):
    def __init__(self, room, x, y, size):
        RoomObject.__init__(self, room, x, y)
        self.set_image(os.path.join("Images/MilbiL1", "Green.png"), size, size)
