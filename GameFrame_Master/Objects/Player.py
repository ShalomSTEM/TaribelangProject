from GameFrame import RoomObject

class Player(RoomObject):
    def __init__(self,room,x,y,size):
        RoomObject.__init__(self,room,x,y)
        self.set_image('Images/Brown.png',size,size)
