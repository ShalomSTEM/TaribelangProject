from GameFrame import RoomObject
import os


class CopG2_Dirt(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join('CopG2', 'dirt.png'))
        self.set_image(image, 32, 32)
