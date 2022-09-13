from GameFrame import RoomObject
import os


class CopStick(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("MilbiL1", "Green.png"))
        self.set_image(image, 64, 64)

        self.x_speed = - 4
