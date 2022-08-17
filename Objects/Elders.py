from GameFrame import RoomObject, Globals

class ML2_Elders(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image('Images/ML2_elder.png', height=50, width=25)


