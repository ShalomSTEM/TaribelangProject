from GameFrame import RoomObject, Globals
import os


class MilbiL1InstructionImg(RoomObject):
    def __init__(self,room,imgName, x, y, w,h):
        RoomObject.__init__(self, room, x, y)
        self.set_image(os.path.join("Images/MilbiL1", imgName), w, h)
