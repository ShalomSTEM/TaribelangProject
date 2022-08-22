from GameFrame import RoomObject, Globals
import os



class ML2_Elders(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
<<<<<<< HEAD
        self.set_image(
            os.path.join(Globals.milbiL2_path, "ML2_elder.png"), height=50, width=25
        )
=======

        self.set_image("Images/MilbiL2/ML2_elder.png", height=50, width=25)
>>>>>>> b6c820cbf7b3262b2b7ea2f6e34dcb141049f842
