from GameFrame import RoomObject, Globals
import os


class Black(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.depth=20
        self.set_image(os.path.join("Images/MilbiL1", "black.jpg"), 1200,700)
