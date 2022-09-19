from GameFrame import RoomObject, Globals
import os


class ML2_People(RoomObject):
    def __init__(self, room, x, y, img):
        RoomObject.__init__(self, room, x, y)
        self.set_image(os.path.join("Images", "MilbiL2", img), height=100, width=100)
