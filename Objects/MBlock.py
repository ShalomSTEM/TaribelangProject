from GameFrame import RoomObject
import os


class MBlock(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join('Museum', 'MusBrick2.png'))


        self.set_image(image, 32, 32)
        self.depth = 100
