import time

from GameFrame import RoomObject, Globals


class WaterIcon_Flash(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image("MilbiL1/Water_Bar_00.png", 50, 300)

    def flash(self):
        print("flashing")
        self.set_image("MilbiL1/Water_Bar_17.png", 50, 300)
