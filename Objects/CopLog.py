from GameFrame import RoomObject
import os


class CopLog(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join("CopG3", "Coplog.png"))
        self.set_image(image, 64, 64)

        self.x_speed = - 4

    def step(self):
        if self.x < -self.width:
            self.room.add_points()
            self.delete_object(self)
