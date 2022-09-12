from GameFrame import RoomObject, Globals
import os


class Stne_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(os.path.join(Globals.milbiL3_alt_path, "Stne_MLBL3.png"))
        self.set_image(image, 64, 64)
