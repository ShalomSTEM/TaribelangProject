from GameFrame import RoomObject, Globals
import os


class ML2_Elders(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(
            os.path.join(Globals.milbiL2_path, "ML2_elder.png"), height=50, width=25
        )
