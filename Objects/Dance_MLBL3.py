import os

from GameFrame import RoomObject, Globals


class Dance_MLBL3(RoomObject):
    def __init__(self, room, x, y, index):
        self.arrows = ["leftArrow.png", "downArrow.png", "upArrow.png", "rightArrow.png"]
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", self.arrows[index])), 64, 64)
        


class DanceBG_MLBL3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image(os.path.join("Overlays", "DanceBG.png")), 274, 70)