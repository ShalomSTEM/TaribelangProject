from GameFrame import RoomObject


class Grass(RoomObject):
    def __init__(self, room, x, y, size):
        RoomObject.__init__(self, room, x, y)
        self.set_image("MilbiL1/Green.png", size, size)
