from GameFrame import RoomObject
import os


class CopG2_Water(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join('CopG2', 'Water.jpg'))
        self.set_image(image, 32, 32)

