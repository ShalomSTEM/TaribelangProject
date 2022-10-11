import os

from GameFrame import RoomObject


class Cockatoo(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        cockatoo_image = self.load_image(os.path.join("CoppleS", "cockatoo.png"))
        self.set_image(cockatoo_image, 64, 64)
