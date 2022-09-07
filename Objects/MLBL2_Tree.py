from GameFrame import RoomObject, Globals
import os


class MLBL2_Tree(RoomObject):
    def __init__(self, room, x, y, img):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image(os.path.join(Globals.milbiL2_alt_path, img))
        self.set_image(image, 100, 100)
