from GameFrame import RoomObject
import os


class MBlockDoor(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join('Museum', 'exit2.png'))
        self.set_image(image, 64, 64)

        self.depth = 100
