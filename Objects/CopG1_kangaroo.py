import os
from GameFrame import RoomObject


class CopG1_kangaroo (RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = self.load_image(os.join.path("CoppleL1", ))
