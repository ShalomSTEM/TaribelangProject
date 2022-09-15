import os

from GameFrame import RoomObject, Globals


class Spear_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join("MilbiL3", "Spear.png"))
        self.set_image(image, 32, 32)
