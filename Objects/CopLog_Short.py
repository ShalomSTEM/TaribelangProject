from GameFrame import RoomObject
import os


class CopLog_Short(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("CopG3", "CopLog_short.png"))
        self.set_image(image, 64, 64)

        self.x_speed = - 4
