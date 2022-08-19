from GameFrame import RoomObject

class Dirt(RoomObject):
    def __init__(self,room,x,y,size):
        RoomObject.__init__(self,room,x,y)
        self.set_image('Images/MilbiL1/Brown.png',size,size)
